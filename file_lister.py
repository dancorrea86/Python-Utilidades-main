import os

class FileLister:

    def __init__(self, source, extension):
        self.source = source
        self.extension = extension

    def list_files(self):
        files = []
        for file in os.listdir(self.source):
            if file.endswith(self.extension):
                files.append(file)

        return files