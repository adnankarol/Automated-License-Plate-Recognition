# Script to Convert Images names from RDD2020 to Numbers

import os
from os import listdir
from os.path import isfile, join

mypath = "Data/images/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

count = 0
for names in onlyfiles:
    count = count + 1
    print(names)
    os.rename(mypath + names, mypath + str(count) + ".jpg")