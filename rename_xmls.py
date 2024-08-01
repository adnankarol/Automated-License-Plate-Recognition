# Script to Convert XML names from Strings to Numbers and also to edit the filename inside each XML file
__author__ = "Adnan Karol"
__version__ = "1.0.0"
__maintainer__ = "Adnan Karol"
__email__ = "adnanmushtaq5@gmail.com"
__status__ = "DEV"

# Import Dependencies
import os
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET

# Define the path to the XML files directory
XML_DIR = "Data/annotations/"

def rename_xml_files(directory):
    """
    Rename XML files in the specified directory from string names to numerical names.

    Args:
        directory (str): The path to the directory containing the XML files.

    Raises:
        ValueError: If the specified directory does not exist or is empty.
    """
    if not os.path.exists(directory):
        raise ValueError(f"The directory {directory} does not exist.")
    
    if not os.listdir(directory):
        raise ValueError(f"The directory {directory} is empty.")
    
    xml_files = [f for f in listdir(directory) if isfile(join(directory, f)) and f.endswith('.xml')]
    
    if not xml_files:
        raise ValueError("No XML files found in the specified directory.")
    
    for count, filename in enumerate(xml_files, start=1):
        new_name = f"{count}.xml"
        old_path = join(directory, filename)
        new_path = join(directory, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
        except Exception as e:
            print(f"Error renaming {filename}: {e}")
    
    return [f"{count}.xml" for count in range(1, len(xml_files) + 1)]

def update_xml_files(directory, xml_files):
    """
    Update the filename inside each XML file to reflect the new numerical name.

    Args:
        directory (str): The path to the directory containing the XML files.
        xml_files (list of str): List of XML filenames to update.
    """
    for xml_file in xml_files:
        print(f"Updating XML file: {xml_file}")
        tree = ET.parse(join(directory, xml_file))
        root = tree.getroot()
        
        for filename_elem in root.iter("filename"):
            # Update filename to match the new numerical name
            filename_elem.text = xml_file.replace(".xml", ".jpg")
        
        try:
            tree.write(join(directory, xml_file))
            print(f"Updated: {xml_file}")
        except Exception as e:
            print(f"Error updating {xml_file}: {e}")

if __name__ == "__main__":
    try:
        # Rename XML files
        xml_files = rename_xml_files(XML_DIR)
        
        # Update XML files with new filenames
        update_xml_files(XML_DIR, xml_files)
        
        print("XML files have been successfully renamed and updated.")
    except ValueError as e:
        print(f"Error: {e}")
