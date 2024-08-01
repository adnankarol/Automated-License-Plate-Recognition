# Script inspired and taken from https://github.com/karndeepsingh/custom_model_detectron2/blob/main/voc2coco.py

__author__ = "Adnan Karol"
__version__ = "1.0.0"
__maintainer__ = "Adnan Karol"
__email__ = "adnanmushtaq5@gmail.com"
__status__ = "DEV"

# Import Dependencies
import sys
import os
import json
import xml.etree.ElementTree as ET
import glob

START_BOUNDING_BOX_ID = 1
PRE_DEFINE_CATEGORIES = None
# If necessary, pre-define category and its id
# PRE_DEFINE_CATEGORIES = {"D00": 1, "D10": 2, "D20": 3, "D40": 4}


def find_elements(root, name):
    """
    Find all elements with the specified tag name in the XML root.

    Args:
        root (xml.etree.ElementTree.Element): The root element of the XML tree.
        name (str): The tag name of the elements to find.

    Returns:
        list: A list of matching elements.
    """
    return root.findall(name)


def get_single_element(root, name, length):
    """
    Find and validate a single element with the specified tag name in the XML root.

    Args:
        root (xml.etree.ElementTree.Element): The root element of the XML tree.
        name (str): The tag name of the element to find.
        length (int): Expected number of matching elements.

    Returns:
        xml.etree.ElementTree.Element: The matching element.

    Raises:
        ValueError: If the element is not found or the number of elements is incorrect.
    """
    elements = root.findall(name)
    if len(elements) == 0:
        raise ValueError(f"Cannot find {name} in {root.tag}.")
    if length > 0 and len(elements) != length:
        raise ValueError(f"The size of {name} is supposed to be {length}, but is {len(elements)}.")
    if length == 1:
        elements = elements[0]
    return elements


def extract_filename_as_int(filename):
    """
    Extract and convert the filename (without extension) to an integer.

    Args:
        filename (str): The filename to convert.

    Returns:
        int: The integer representation of the filename.

    Raises:
        ValueError: If the filename cannot be converted to an integer.
    """
    try:
        filename = filename.replace("\\", "/")
        filename = os.path.splitext(os.path.basename(filename))[0]
        return int(filename)
    except ValueError:
        raise ValueError(f"Filename {filename} is supposed to be an integer.")


def generate_category_mapping(xml_files):
    """
    Generate a mapping of category names to IDs from a list of XML files.

    Args:
        xml_files (list): A list of XML file paths.

    Returns:
        dict: A dictionary mapping category names to IDs.
    """
    class_names = []
    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall("object"):
            class_names.append(member[0].text)
    class_names = list(set(class_names))
    class_names.sort()
    return {name: i for i, name in enumerate(class_names)}


def convert_voc_to_coco(xml_files, json_file):
    """
    Convert Pascal VOC annotations to COCO format and save to a JSON file.

    Args:
        xml_files (list): A list of Pascal VOC XML annotation files.
        json_file (str): Path to the output COCO format JSON file.
    """
    json_dict = {
        "images": [],
        "type": "instances",
        "annotations": [],
        "categories": []
    }

    categories = PRE_DEFINE_CATEGORIES if PRE_DEFINE_CATEGORIES is not None else generate_category_mapping(xml_files)
    bounding_box_id = START_BOUNDING_BOX_ID

    for xml_file in xml_files:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        path_elements = find_elements(root, "path")

        if len(path_elements) == 1:
            filename = os.path.basename(path_elements[0].text)
        elif len(path_elements) == 0:
            filename = get_single_element(root, "filename", 1).text
        else:
            raise ValueError(f"{len(path_elements)} paths found in {xml_file}")

        image_id = extract_filename_as_int(filename)
        size = get_single_element(root, "size", 1)
        width = int(get_single_element(size, "width", 1).text)
        height = int(get_single_element(size, "height", 1).text)

        image = {
            "file_name": filename,
            "height": height,
            "width": width,
            "id": image_id,
        }
        json_dict["images"].append(image)

        for obj in find_elements(root, "object"):
            category = get_single_element(obj, "name", 1).text
            if category not in categories:
                categories[category] = len(categories)
            category_id = categories[category]

            bndbox = get_single_element(obj, "bndbox", 1)
            xmin = int(get_single_element(bndbox, "xmin", 1).text) - 1
            ymin = int(get_single_element(bndbox, "ymin", 1).text) - 1
            xmax = int(get_single_element(bndbox, "xmax", 1).text)
            ymax = int(get_single_element(bndbox, "ymax", 1).text)
            assert xmax > xmin
            assert ymax > ymin

            width = xmax - xmin
            height = ymax - ymin

            annotation = {
                "area": width * height,
                "iscrowd": 0,
                "image_id": image_id,
                "bbox": [xmin, ymin, width, height],
                "category_id": category_id,
                "id": bounding_box_id,
                "ignore": 0,
                "segmentation": [],
            }
            json_dict["annotations"].append(annotation)
            bounding_box_id += 1

    for category, cid in categories.items():
        json_dict["categories"].append({
            "supercategory": "none",
            "id": cid,
            "name": category
        })

    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    with open(json_file, "w") as json_fp:
        json.dump(json_dict, json_fp)
    
    print(f"Conversion successful: {json_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Pascal VOC annotation to COCO format."
    )
    parser.add_argument("xml_dir", help="Directory path to XML files.", type=str)
    parser.add_argument("json_file", help="Output COCO format JSON file.", type=str)
    args = parser.parse_args()
    
    xml_files = glob.glob(os.path.join(args.xml_dir, "*.xml"))
    print(f"Number of XML files: {len(xml_files)}")

    convert_voc_to_coco(xml_files, args.json_file)
