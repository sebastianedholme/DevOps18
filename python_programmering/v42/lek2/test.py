import os
files_path = 'icons/'

files = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path, f))]
print(files)
