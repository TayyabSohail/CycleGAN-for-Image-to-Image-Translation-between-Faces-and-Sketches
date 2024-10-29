# CycleGAN-for-Image-to-Image-Translation-between-Faces-and-Sketches

# Project Overview
This project implements a CycleGAN model using the Person Face Sketches dataset to perform image-to-image translation between real face images and sketches. The objective is to translate a face image into a corresponding sketch and convert sketches back into realistic face images.

The CycleGAN architecture allows for this translation without the need for paired data, learning the mappings between the two domains (faces and sketches). The training was conducted in an end-to-end manner, saving model weights after each epoch to ensure that progress was not lost. Strategies such as dataset batching and tuning hyperparameters (learning rate, batch size) were applied to optimize model performance and address memory limitations.

# Tools and Technologies Used

Programming Language: Python

# Libraries:

TensorFlow/Keras: For building and training the CycleGAN model

NumPy: For data manipulation

OpenCV/PIL: For image preprocessing and transformation

## Dataset: Person Face Sketches

# Techniques:

CycleGAN architecture for unpaired image-to-image translation

End-to-end training and evaluation

Model weight saving after each epoch

Memory optimization through batching and hyperparameter adjustment


# Setup and Installation

## Clone the repository:

git clone https://github.com/your-username/cyclegan-face-sketch-translation.git

cd cyclegan-face-sketch-translation

## Install the required dependencies:

pip install -r requirements.txt

Download the Person Face Sketches dataset or your dataset of choice, and ensure it is structured for use with CycleGAN.

## How to Run

Train the CycleGAN model:

python train.py

## Test the model on new face or sketch images:

python test.py --input_image <path_to_image>

The model will output translated images (sketches from faces or faces from sketches) after training.


# Results
The CycleGAN model successfully translates between real face images and their sketch equivalents. During testing, the model generated convincing face reconstructions from sketches and produced accurate sketches from real face images.
