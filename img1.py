import glob
import os
from PIL import Image

pa="./data/*.jpg"
images = glob.glob(pa)
i=0
for image in images:
        img= Image.open("./data/frame"+str(i)+".jpg")
        i=i+1
        w,h=img.size
        a=(0,0,w/2,h)
        img1=img.crop(a)
        img1.save(image)
print("done")
