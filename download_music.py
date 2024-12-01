import requests
from pathlib import Path

# URL of the suggested music
MUSIC_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# Define the static audio directory
BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "app" / "static" / "music"

# Ensure the directory exists
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# Download the music file
def download_music():
    response = requests.get(MUSIC_URL, stream=True)
    if response.status_code == 200:
        music_path = AUDIO_DIR / "background_music.mp3"
        with open(music_path, "wb") as music_file:
            for chunk in response.iter_content(chunk_size=1024):
                music_file.write(chunk)
        print(f"Music file downloaded to: {music_path}")
    else:
        print(f"Failed to download music. Status code: {response.status_code}")

if __name__ == "__main__":
    download_music()
