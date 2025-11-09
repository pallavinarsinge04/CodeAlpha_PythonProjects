import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved = 0
    for file in os.listdir(source_folder):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))
            moved += 1
    print(f"✅ Moved {moved} .jpg files from {source_folder} → {destination_folder}")

# Example usage
source = input("Enter source folder path: ")
destination = input("Enter destination folder path: ")
move_jpg_files(source, destination)
