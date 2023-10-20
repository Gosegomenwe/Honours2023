import os
import pandas as pd
import shutil

# Load the CSV file with the custom delimiter (;)
csv_file = "classes.csv"
df = pd.read_csv(csv_file, sep=';')

# Function to move the images to the appropriate folder
def move_images(image_folder, label_folder, image_names):
    for image_name in image_names:
        src_path = os.path.join(image_folder, image_name)
        dst_path = os.path.join(label_folder, image_name)
        shutil.move(src_path, dst_path)

# Define the image folder and the output folders for each label
image_folder = "train"
output_folders = ["Chalky", "Mary", "Sand", "Silt"]

# Loop through the rows of the CSV file and move images to the appropriate folders
for index, row in df.iterrows():
    image_names = [row["Name"]]
    for i, label in enumerate(["Chalky", "Mary", "Sand", "Silt"]):
        if row[label] == 1:
            label_folder = output_folders[i]
            move_images(image_folder, label_folder, image_names)
            break
