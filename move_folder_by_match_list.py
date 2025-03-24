import shutil
import os
from list_of_folders import folders

class MoveFilesByMatch:
    def __init__(self, src_dir, dest_dir):
        self.src_dir = src_dir
        self.dest_dir = dest_dir

    def move_files(self):
        for file in folders:     
            shutil.move(os.path.join(self.src_dir, file), self.dest_dir)
            print(f"Movendo arquivo: {file}")

if __name__ == "__main__":
    directory = input("Pasta onde estão os arquivos:")
    directory_destination = input("Pasta de destino:")
    mover = MoveFilesByMatch(directory, directory_destination)
    mover.move_files()