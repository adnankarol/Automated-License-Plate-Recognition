# Detectron2_License_Plate_Detecttion
A Repository to Train a Custom Detectron2 based object detector for Car License Plate Detection.

# Table of Contents
1. [ Dataset ](#data)
2. [ Model ](#model)
3. [ Configurations ](#Configurations)
4. [ Model Training ](#Training) 
5. [ Additional Information ](#info)


<a name="data"></a>
# Section 1: Dataset

1. Dataset is taken from Kaggle: https://www.kaggle.com/andrewmvd/car-plate-detection

2. The data is present in the PascalVOC format as bounding boxes labelled as xmin, ymin, xmax and ymax, stored as xml files.

<a name="model"></a>
# Section 2: Model

## About the Detectron 2 Model
Detectron2 is Facebook AI Research's library that provides state-of-the-art detection and segmentation algorithms. It is the successor of Detectron and maskrcnn-benchmark.
Please read the github page for more information [here](https://github.com/facebookresearch/detectron2#:~:text=Detectron2%20is%20Facebook%20AI%20Research's,and%20production%20applications%20in%20Facebook.) .

<a name="Configurations"></a>
# Section 3: Configurations

## Data

1. Collect the images and xml annotation files from Kaggle into a single folder 'Data'.

2. The annotation of the bounding boxes are currently in an xml format, for example : 


        <annotation>
            <folder>images</folder>
            <filename>Cars0.png</filename>
            <size>
                <width>500</width>
                <height>268</height>
                <depth>3</depth>
            </size>
            <segmented>0</segmented>
            <object>
                <name>licence</name>
                <pose>Unspecified</pose>
                <truncated>0</truncated>
                <occluded>0</occluded>
                <difficult>0</difficult>
                <bndbox>
                    <xmin>226</xmin>
                    <ymin>125</ymin>
                    <xmax>419</xmax>
                    <ymax>173</ymax>
                </bndbox>
            </object>
        </annotation>

3. This has to be converted into the COCO format. 

4. Before conversion of pascal voc format to coco format, two additional steps need to be perfomed:
   1. Rename train images to integers. For this run the command:
       `python rename_images.py`
   2. Rename XML to integers, and also edit the filename inside each xml. For this run the command:
       `python rename_xmls.py`

5. In order to perform this, open the script `pascal_coco_conversion.py` and enter the command:

    `python .\pascal_coco_conversion.py [path to xml files] [path of output json]`

6. Sample command:

    `python .\pascal_coco_conversion.py .\Data\annotations .\Data\output.json`


7. A new file called 'output.json' is created.

8.   Finally, your data for training the Detectron 2 model is now ready.



<a name="Training"></a>
# Section 4: Model Training

1. Open the Notebook `Training_Notebook.ipynb` to follow all the steps for training the model. 

<a name="info"></a>
# Section 5: Additional Information

## Use of [Detectron2](https://github.com/facebookresearch/detectron2#:~:text=Detectron2%20is%20Facebook%20AI%20Research's,and%20production%20applications%20in%20Facebook.)
References: The model for Detectron2 is taken from repository of Facebook Research.

## Python Version
The whole project is developed with python version `Python 3.7.7` and pip version `pip 19.2.3`.

## Contact
In case of error, feel free to contact me over Linkedin at [Adnan](https://www.linkedin.com/in/adnan-karol-aa1666179/).
