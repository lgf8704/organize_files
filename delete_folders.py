import shutil
import os


def delete_folders(path='.'):
    print("Deleting files...")

    for folder in os.listdir(path):
        if len(folder) > 20:
            folder_path = os.path.join(path, folder)
            shutil.rmtree(folder_path)