import cv2
import os
import glob
from PIL import Image
from multiprocessing import Pool
pa="./videoplayback_Trim.mp4"
cam = cv2.VideoCapture(pa)
try:
        if not os.path.exists('data'):
                os.makedirs('data')
except OSError:
        print ('Error: Creating directory of data')
currentframe = 0
while(True):
        ret,frame = cam.read()
        if ret:
                name = './data/frame' + str(currentframe) + '.jpg'
                print ('Creating...' + name)
                cv2.imwrite(name, frame)
                currentframe += 1
        else:
                break
        
cam.release()
cv2.destroyAllWindows()
print("10 frames fetching completed")
os.system('python img1.py')
print("croping executed")
