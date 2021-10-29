class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        plik = open(self.file_name, 'r')
        dane = plik.read()
        print(dane)
        plik.close()

    def update_file(self, text_data):
        plik = open(self.file_name, 'a')
        plik.write(text_data)
        plik.close()
