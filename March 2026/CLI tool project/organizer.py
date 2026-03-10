from pathlib import Path
import shutil
import sys


def organize_files(folder_path):
    folder = Path(folder_path)

    categories = {
        ".pdf": "pdf",
        ".jpg": "images",
        ".jpeg": "images",
        ".png": "images",
        ".txt": "text",
        ".mp3": "audio",
    }

    for file in folder.iterdir():
        if file.is_file():
            extension = file.suffix.lower()

            if extension in categories:
                destination_folder = folder / categories[extension]
                destination_folder.mkdir(exist_ok=True)

                destination_path = destination_folder / file.name
                shutil.move(str(file), str(destination_path))

                print(f"Moved {file.name} to {destination_folder}")
            else:
                print(f"Skipped: {file.name} (unknown type)")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python organizer.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    organize_files(folder_path)