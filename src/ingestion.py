import os 
#Audio Video Downloader
from yt_dlp import YoutubeDL


def download_youtube_audio(url: str, output_path: str = "data/raw/plenary_hearing_30_10_2025"):
    """Downloads audio from YouTube and saves it as an mp3."""
    
    # Create directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
        # No extractor_args - let yt-dlp use defaults for this finished stream
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"{output_path}.mp3"
    except Exception as e:
        print(f"Error downloading: {e}")
        raise

# Initial 403 error - YouTube blocking the download
# iOS client bypass - Helped get past the block but doesn't support past livestreams
# Default behavior - Works best for archived/finished livestreams

if __name__ == "__main__":
    link = "https://www.youtube.com/watch?v=kEAPCtvTl0w"
    path = download_youtube_audio(link)
    print(f"Audio saved to: {path}")