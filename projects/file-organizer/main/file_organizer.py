from pathlib import Path
import time

path = Path.home()
downloads = path / 'Downloads'

#folder categories
categories = {
                'Documents' : ['.pdf', '.docx', '.txt'],
                'Images' : ['.jpg', '.jpeg', '.png'],
                'Videos' : ['.mp4', '.mkv'],
                'Audio' : ['.mp3', '.wav', '.flac', '.aac']
}

for item in downloads.iterdir():
    if item.is_dir():
        continue

    extension = item.suffix.lower()
    folder = 'Others'

    for category, extensions in categories.items():
        if extension in extensions:
            folder = category
            break

    destination = downloads / folder
    destination.mkdir(exist_ok=True)
    item.replace(destination / item.name)

print("The files in your 'Downloads' folder has been organized")
time.sleep(3)
