import os
import random
import shutil

def split_images(source_dir, train_dir, test_dir, split_ratio=0.7):
    classes = ["Alluvial soil", "Black", "Clay soil","Chalky", "Red soil", "Mary", "Sand", "Silt"]
    
    for class_name in classes:
        class_source_dir = os.path.join(source_dir, class_name)
        class_train_dir = os.path.join(train_dir, class_name)
        class_test_dir = os.path.join(test_dir, class_name)
        
        os.makedirs(class_train_dir, exist_ok=True)
        os.makedirs(class_test_dir, exist_ok=True)
        
        images = os.listdir(class_source_dir)
        random.shuffle(images)
        
        split_index = int(len(images) * split_ratio)
        train_images = images[:split_index]
        test_images = images[split_index:]
        
        for image in train_images:
            src_path = os.path.join(class_source_dir, image)
            dst_path = os.path.join(class_train_dir, image)
            shutil.copy(src_path, dst_path)
            
        for image in test_images:
            src_path = os.path.join(class_source_dir, image)
            dst_path = os.path.join(class_test_dir, image)
            shutil.copy(src_path, dst_path)
            
    print("Data split complete.")

# Specify paths
source_folder = "C:\\Users\\goseg\\Train"
train_folder = "C:\\Users\\goseg\\Trains"
test_folder = "C:\\Users\\goseg\\Tests"
split_ratio = 0.7

# Call the split_images function
split_images(source_folder, train_folder, test_folder, split_ratio)
