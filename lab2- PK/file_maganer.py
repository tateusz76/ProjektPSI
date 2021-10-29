class FileManager:

    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        file = open(self.filename)
        print(file.read())
        file.close()

    def update_file(self, text):
        file = open(self.filename, "a")
        file.write(text)
        file.close()