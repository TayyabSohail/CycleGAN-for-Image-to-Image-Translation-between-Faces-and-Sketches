# CycleGAN-for-Image-to-Image-Translation-between-Faces-and-Sketches

## Research Paper: 
[Tayyab_question_4_report.pdf](https://github.com/user-attachments/files/17557277/Tayyab_question_4_report.pdf)

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
![WhatsApp Image 2024-10-21 at 10 03 22 PM](https://github.com/user-attachments/assets/0f2b7ad6-39ec-4997-a441-c25b0cc8276c)
![WhatsApp Image 2024-10-21 at 10 29 02 PM](https://github.com/user-attachments/assets/289508e4-70dc-46e4-88c3-d2a47de38901)
![WhatsApp Image 2024-10-21 at 10 04 03 PM](https://github.com/user-attachments/assets/def18455-4a64-4ebf-a00a-c9e9c7173457)
![WhatsApp Image 2024-10-21 at 10 03 45 PM](https://github.com/user-attachments/assets/f5349d8b-98b5-4496-8bac-42a9e42da450)


