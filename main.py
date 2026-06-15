import subprocess
from pathlib import Path
import sys

def nameclean(name):
    namesplitlist = name.split('｜')
    return namesplitlist[0].strip() if len(namesplitlist) > 0 else name.strip()
home = Path.home()
WD=f"{home}/Youtubemp3-download" # Change this to your working directory
DOWNLOAD_DIR=f"{WD}/downloads" # Change this to your desired download directory
subprocess.run(["mkdir", "-p", f"{DOWNLOAD_DIR}"])
songs=[]
with open(f"{WD}/songs.txt","r") as f:
    song = f.read()
    songs = song.split("\n")

if len(sys.argv) > 1:
    if sys.argv[1] == "cleanname":
        for item in Path(DOWNLOAD_DIR).iterdir():
            if item.is_file():
                new_name = nameclean(item.stem) + item.suffix
                new_path = item.parent / new_name
                item.rename(new_path)
        print("Renamed all files in the download directory.")
        sys.exit(0)
for song in songs:
    song=song[:len(song)-1]
    try:
        print(f"Downloading {song}...")
        subprocess.run([
    "yt-dlp","-x","--audio-format", "mp3","--audio-quality", "0","-o", f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",f"{song}"])
    except Exception as e:
        print(f"Error downloading {song}: {e}")
