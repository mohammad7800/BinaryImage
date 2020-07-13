from PIL import Image
import os

for i in os.listdir('.'):
    if os.path.isdir(i):
        Image.open(i + '/0.jpg').resize((8, 13)).save(i + '/0.jpg')
        Image.open(i + '/1.jpg').resize((8, 13)).save(i + '/1.jpg')
