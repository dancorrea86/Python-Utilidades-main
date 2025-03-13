from file_copier import FileCopier
from file_lister import FileLister
from pdf_reader import PdfReader

class Program:
    def __init__(self):
        self._running = True

    # def run(self):
    #     source_folder = input("Enter the source folder: ")
    #     destination_folder = input("Enter the destination folder: ")
    #     extension = input("Enter the extension of the files to copy: ")
    #     file_copier = FileCopier(source_folder, destination_folder, extension)
    #     file_copier.copier_files()

    # def run(self):
    #     source_folder = input("Enter the source folder: ")
    #     extension = input("Enter the extension of the files to copy: ")
    #     file_lister = FileLister(source_folder, extension)
    #     files = file_lister.list_files()
    #     f = open("files.txt", "w")
    #     for file in files:
    #         f.writelines(f'"{file.split("-")[0]}",')
    #         f.writelines("\n")
    #     f.close()

    def run(self):
        source_file = input("Enter the source file: ")
        pdf_lister = FileLister(source_file, ".pdf")
        files = pdf_lister.list_files()



        files_to_manteins = []
        files_to_move = []
        
        

if __name__ == "__main__":
    program = Program()
    program.run()




