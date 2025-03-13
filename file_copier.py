import os
import shutil

class FileCopier:

    def __init__(self, source, destination, extension):
        self.source = source
        self.destination = destination
        self.extension = extension

    def copier_files(self):
        for root, dirs, files in os.walk(self.source):
            for file in files:
                if file.endswith(self.extension):
                    # Caminho completo do arquivo de origem
                    source_file = os.path.join(root, file)
                    # Caminho completo do arquivo de destino
                    destination_file = os.path.join(self.destination, file)
                    # Copia o arquivo
                    shutil.copy(source_file, destination_file)
                    print(f"Copied: {source_file} -> {destination_file}")