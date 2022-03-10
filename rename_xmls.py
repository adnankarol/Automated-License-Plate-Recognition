# Script to Convert XML names from RDD2020 to Numbers and also to edit the filename inside each XML file

import os
from os import listdir
from os.path import isfile, join
import xml.etree.ElementTree as ET


mypath = "Data/annotations/"


# Section to Rename the File
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
count = 0
for names in onlyfiles:
    count = count + 1
    print("Renaming file: ", names)
    os.rename(mypath + names, mypath + str(count) + ".xml")


def updateXML(mypath, myfile):
    print(myfile)
    tree = ET.ElementTree(file = mypath + myfile)
    root = tree.getroot()

    print(root.iter("filename"))
    for vars in root.iter("filename"):
        vars.text = myfile.split(".")[0] + ".jpg"
    
    tree = ET.ElementTree(root)

    with open(mypath + myfile, "wb") as fileupdate:
        tree.write(fileupdate)


# Section to Edit the File
xml_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for xml_file in xml_files:
    print("Writing file: ", xml_file)
    updateXML(mypath,xml_file)