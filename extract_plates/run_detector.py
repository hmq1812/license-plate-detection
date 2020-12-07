from yolo import YOLO
from PIL import Image
import os

model = YOLO()

input_dir = './input/'
output_dir = './output/'
for filename in os.listdir(input_dir):
    if filename.endswith((".jpg", ".png", ".jpeg")) and (filename[:-4] + '0' + '.jpg') not in os.listdir(output_dir):
        path = os.path.join(input_dir, filename)
        img = Image.open(path)   
        plates = model.detect_image(img)
        for index, plate in enumerate(plates):
            plate.save(output_dir + filename.split('.')[0] + str(index) + '.jpg')
