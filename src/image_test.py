from dalle2 import Dalle2
dalle = Dalle2("sess-q3JpYmKLzWgsiXdbQOAYZpKT5p7jtALHN8zy3DEI")
file_paths = dalle.generate_and_download("One hunter turned round caught a football")
print(file_paths)
