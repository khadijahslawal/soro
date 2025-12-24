# Transcribes audio with timestamps
from faster_whisper import WhisperModel

# 'base' is fast for testing; use 'large-v3' for final resume-quality results
def transcribe_audio(file_path:str, model_size:str = "base"):
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    nigerian_context = "This is a Nigerian senate plenary hearing."
    segments, info = model.transcribe(file_path, 
                                      beam_size=5,
                                      language="en",          # Force English to avoid 'Norwegian' glitch
                                      vad_filter=True,        # Enable Voice Activity Detection to skip static/silence
                                      vad_parameters=dict(min_silence_duration_ms=10000), # Ignore silence > 10s
                                      initial_prompt=nigerian_context # Priming the model with local context
                                      )

    print(f"Detected Language: {info.language}  - ({info.language_probability:.2f})")
    
    results = []
    
    for segment in segments:
        results.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": segment.text.strip()
        })
    return results

if __name__ == "__main__":
    audio_file = "data/raw/plenary_hearing_30_10_2025.mp3"
    transcript = transcribe_audio(audio_file)
    for entry in transcript[:5]:
        print(f"[{entry['start']}s] {entry['text']}")
