from file_maganer import FileManager

plik = FileManager("plik.txt")
plik.read_file()
plik.update_file("pierwszy update\n")
plik.read_file()
plik.update_file("drugi update\n")
plik.read_file()