#!/usr/bin/env python3

import os
import sys
from pathlib import Path

# Define the length of the filename's chunck that is repeated before being sufixed.
# For example it is 37 for the file names "WhatsApp Image 2023-09-18 at 00.57.02 (2).jpeg"
generic_filename_length = 37

valid_path = False

# Read the path from passed arguments. In cae of no passed argument, the current path is set the destination path.
if len(sys.argv) > 1:
    dir_name = sys.argv[1]
else:
    dir_name = os.path.dirname(os.path.realpath(__file__))

directory = os.fsencode(dir_name)
unique_files = []

# Check the validity og input path and iteratively ask for a valid one
while not valid_path:
    try:
        list_files = os.listdir(directory)
    except FileNotFoundError:
        print(f"No such directory ({dir_name}) exists.")
        dir_name = input("Enter the path again:")
        if dir_name in [".", "./"]:
            dir_name = os.path.dirname(os.path.realpath(__file__))
        elif dir_name in ["~", "~/"]:
            dir_name = os.path.expanduser("~")
        directory = os.fsencode(dir_name)
    else:
        valid_path = True

# iterate over the files in the directory and remove the file with same initials and size
for file in list_files:
    filename = os.fsdecode(file)
    info = (filename[:generic_filename_length], Path(filename).stat().st_size)
    if info in unique_files:
        print(filename, Path(filename).stat().st_size)
        os.remove(filename)
    else:
        unique_files.append(info)
