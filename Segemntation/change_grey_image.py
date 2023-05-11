'''
import os
from PIL import Image
import cv2 as cv
import numpy as np

label_dir = "/cis/phd/yz4891/PaddleSeg/dataset/annotations/"
label_process_dir = '/cis/phd/yz4891/PaddleSeg/dataset/label_process/'
if not os.path.exists(label_process_dir):
    os.makedirs(label_process_dir)

for file in os.listdir(label_dir):
    label = label_dir + file
    if os.path.isfile(label):
        print(file)
        # ???????????????
        label_array = cv.imread(label, 0)
        print('label:', label_array.shape)
        class_image = np.unique(np.array(label_array))
        print('class_image:', class_image)

        for i in class_image:
            if i in [255, 106, 0]:  # 84, 111, 208,

                pass
            else:
                print('---------------------------------------------------------------')
                
        label_array[label_array == 0] =   1   #??
        label_array[label_array == 255] = 0   #??
       # label_array[label_array == 106] = 2  
       # label_array[label_array == 84] = 2
       # label_array[label_array == 111] = 2
       # label_array[label_array == 208] = 2


        cv.imwrite(label_process_dir + file, label_array)


'''




import cv2
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rcParams['font.sans-serif'] = ['SimHei']     
matplotlib.rcParams['axes.unicode_minus'] = False




img = cv2.imread("/cis/phd/yz4891/PaddleSeg/dataset/annotations_color/IMG_3345.png", 0)
print("???shape: ", img.shape)
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("img")

# 1.OTSU???
ret2, mask_OTSU = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("OTSU?shape: ", mask_OTSU.shape)
plt.subplot(2, 2, 4)
plt.imshow(mask_OTSU, cmap='gray')
plt.title("OTSU")
cv2.imwrite('"/cis/phd/yz4891/PaddleSeg/dataset/lable1/IMG_3345.png"',mask_OTSU)#??????



from PIL import Image
     
image = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/lable1/IMG_3345.png")
    
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

im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/dataset/lable1/IMG_3345.png"))
print(np.unique(im))
#im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/dataset/lable1/IMG_3345.png"))
#print(np.unique(im)) # np.unique( )??? ??????????,?????????







