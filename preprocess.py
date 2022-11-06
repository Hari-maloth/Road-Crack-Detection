import sys
import io
from PIL import Image
from scipy import ndimage
from skimage.util import img_as_ubyte
from skimage import filters
from skimage.morphology import disk
import matplotlib.pyplot as plt
import os
from PIL import Image
import pillow_heif

''' Folder Structure :
         Main ----
                  -->Train
                          ->crack
                             >Imageslist
                          ->nocrack
                             >ImagesList
                  -->Test
                          ->crack
                             >ImagesList
                          ->nocrack
                             >ImagesList
                  -->Train
                          ->crack
                             >ImagesList
                          ->nocrack
                              >ImagesList
'''
for i in os.listdir("dataset/train/process"):
    if i[0]=='.':
        pass
    else:
        heif_file=pillow_heif.read_heif('dataset/train/process/'+i)
        image=Image.frombytes(heif_file.mode,heif_file.size,heif_file.data,"raw")
        image.resize((500,500))
        image.save("dataset/train/crack/"+i)
