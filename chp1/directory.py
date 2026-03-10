import os

# specify the directory path
path = "/New Folder"

# get list of files and folders
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)