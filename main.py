import subprocess
WD="/home/smthing/songs" # Change this to your working directory
DOWNLOAD_DIR=f"{WD}/downloads" # Change this to your desired download directory
subprocess.run(["mkdir", "-p", f"{DOWNLOAD_DIR}"])
songs=[]
with open(f"{WD}/songs.txt","r") as f:
    song = f.read()
    songs = song.split("\n")
for song in songs:
    song=song[:len(song)-1]
    try:
        print(f"Downloading {song}...")
        subprocess.run([
    "yt-dlp","-x","--audio-format", "mp3","--audio-quality", "0","-o", f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",f"{song}"])
    except Exception as e:
        print(f"Error downloading {song}: {e}")
print(songs)