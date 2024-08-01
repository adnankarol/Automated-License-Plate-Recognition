# Script to Convert Images names from Strings to Numbers
__author__ = "Adnan Karol"
__version__ = "1.0.0"
__maintainer__ = "Adnan Karol"
__email__ = "adnanmushtaq5@gmail.com"
__status__ = "DEV"

# Import Dependencies

import os
from os import listdir
from os.path import isfile, join

# Define the path to the images directory
IMAGE_DIR = "Data/images/"

def rename_images_to_numbers(directory):
    """
    Rename image files in the specified directory from string names to numerical names.

    Args:
        directory (str): The path to the directory containing the image files.

    Raises:
        ValueError: If the specified directory does not exist or is empty.
    """
    if not os.path.exists(directory):
        raise ValueError(f"The directory {directory} does not exist.")
    
    if not os.listdir(directory):
        raise ValueError(f"The directory {directory} is empty.")
    
    only_files = [f for f in listdir(directory) if isfile(join(directory, f))]
    
    if not only_files:
        raise ValueError("No files found in the specified directory.")

    for count, filename in enumerate(only_files, start=1):
        new_name = f"{count}.jpg"
        old_path = join(directory, filename)
        new_path = join(directory, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")

if __name__ == "__main__":
    try:
        rename_images_to_numbers(IMAGE_DIR)
        print("Image renaming completed successfully.")
    except ValueError as e:
        print(f"Error: {e}")
