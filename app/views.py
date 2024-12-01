from django.shortcuts import render
from pathlib import Path
import requests

# Define the music download function
def download_music():
    MUSIC_URL = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    AUDIO_DIR = Path(__file__).resolve().parent.parent / "static" / "audio"
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    music_path = AUDIO_DIR / "background_music.mp3"
    if not music_path.exists():
        response = requests.get(MUSIC_URL, stream=True)
        if response.status_code == 200:
            with open(music_path, "wb") as music_file:
                for chunk in response.iter_content(chunk_size=1024):
                    music_file.write(chunk)
            print(f"Music file downloaded to: {music_path}")
        else:
            print(f"Failed to download music. Status code: {response.status_code}")

# View function for home
def home(request):
    # Ensure the music file is present
    download_music()
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')
