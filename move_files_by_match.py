import shutil
import os

class MoveFilesByMatch:
    def __init__(self, src_dir, dest_dir, match_str):
        self.src_dir = src_dir
        self.dest_dir = dest_dir
        self.match_str = match_str

    def move_files(self):
        for file in os.listdir(self.src_dir):
            if self.match_str in file:
                shutil.move(os.path.join(self.src_dir, file), self.dest_dir)
                print(f"Movendo arquivo: {file}")

if __name__ == "__main__":
    src_dir = "C:\\Users\\Daniel_Maciel\\Desktop\\Nomear"
    dest_dir = "C:\\Users\\Daniel_Maciel\\Desktop\\Nomear\\Declaracao"
    match_str = "Declaracao"
    mover = MoveFilesByMatch(src_dir, dest_dir, match_str)
    mover.move_files()