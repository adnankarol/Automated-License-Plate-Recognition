# Automated-License-Plate-Recognition

A repository for training a custom Detectron2-based object detector specifically for car license plate detection.

## Introduction

Detecting and recognizing vehicle license plates is a crucial task in various applications, including automated parking systems, traffic management, and law enforcement. This repository provides a framework to train a custom object detector using Detectron2, Facebook AI Research’s state-of-the-art library for object detection and segmentation. The goal is to create a robust model that can accurately detect license plates in vehicle images, facilitating tasks such as automatic license plate recognition (ALPR).

## Overview

This project leverages the Detectron2 library to build a custom object detection model specifically trained for detecting license plates on vehicles. The workflow involves preparing a dataset, configuring the training environment, and training the model.

The key steps are:

Dataset Preparation: Convert the Pascal VOC formatted dataset from Kaggle into the COCO format required by Detectron2.
Model Training: Utilize the converted dataset to train a custom Detectron2 model for license plate detection.

## Dataset

1. The dataset used for this project is available on Kaggle: [Car Plate Detection Dataset](https://www.kaggle.com/andrewmvd/car-plate-detection).

2. The data is provided in Pascal VOC format, with annotations in XML files specifying bounding boxes with `xmin`, `ymin`, `xmax`, and `ymax`.

## Model Overview

### About Detectron2
Detectron2 is a state-of-the-art detection and segmentation library developed by Facebook AI Research. It is the successor to Detectron and maskrcnn-benchmark. For more details, visit the [Detectron2 GitHub page](https://github.com/facebookresearch/detectron2).

## Configurations

### Data Preparation

1. **Collect Data**: Place the images and XML annotation files from Kaggle into a folder named `Data`.

2. **XML Example**:
    ```xml
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
    ```

3. **Convert to COCO Format**:
   1. **Rename Images**: Execute the command:
      ```bash
      python rename_images.py
      ```
   2. **Rename XML Files**: Execute the command:
      ```bash
      python rename_xmls.py
      ```

4. **Perform Conversion**:
   - Open the script `pascal_coco_conversion.py` and run the following command:
     ```bash
     python pascal_coco_conversion.py [path to XML files] [path to output JSON]
     ```

   - Example command:
     ```bash
     python pascal_coco_conversion.py ./Data/annotations ./Data/output.json
     ```

5. **Result**: The conversion will generate an `output.json` file, which prepares your data for training the Detectron2 model.

## Model Training

1. **Training**: Open the Jupyter Notebook `Training_Notebook.ipynb` to follow detailed steps for training the model.

## Additional Information

### Detectron2 Library
For more details on Detectron2, refer to the [Detectron2 GitHub repository](https://github.com/facebookresearch/detectron2).

### Python Version
This project is developed using Python 3.7.7 and pip 19.2.3.

### Contact
For any inquiries or issues, please reach out to me on LinkedIn: [Adnan](https://www.linkedin.com/in/adnan-karol-aa1666179/).
