import os

word = input("Qual palavra deseja cortar?\n")


def rename_files(directory):
    for filename in os.listdir(directory):
        if word in filename:
            new_filename = filename.replace(word, "")
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# Replace 'path_to_directory' with the path where your files are located
directory_path = './Os Meus Amigos sao um Barato'

rename_files(directory_path)
