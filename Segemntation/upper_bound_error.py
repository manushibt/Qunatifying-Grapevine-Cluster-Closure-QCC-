'''
from PIL import Image
     
image = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3345.png")
    
print("Filename: ", image.filename)
print("Format: ", image.format)
print("Mode: ", image.mode)
print("Size: ", image.size)
print("Width: ", image.width)
print("Height: ", image.height)
print("Is Animated: ", (getattr(image, "is_animated", False)))
print("Frames in Image", getattr(image, "n_frames", 1))
image.close()   # close image file


import numpy as np
from PIL import Image

im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3345.png"))
print(np.unique(im))
im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3349.png"))
print(np.unique(im)) # np.unique( )??? ??????????,?????????


'''


import numpy
import PIL
from PIL import Image
#image = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3345.png")
label = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3345.png")
label = numpy.asarray(label)
#set =set(label)
cnts = len(label)
cnt = 0
for I in label:
    label[label==I] = cnt 
    cnt += 1
PIL.Image.write(label, "label_path")




