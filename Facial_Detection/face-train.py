import os
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "Images")
x_train =[]
y_labels=[]

for root,dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root,file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","_").lower()
            print(label,path)
            # x_train.append(path)
            # y_labels.append(path)
            pil_image = Image.open(path).convert("L") #grauscale
            image_array =np.array(pil_image, "uint8") #"uint8 = unsigned integer of 8 bite
            print(image_array)












