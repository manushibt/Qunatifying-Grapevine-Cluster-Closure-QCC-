import os
from PIL import Image
import cv2 as cv
import numpy as np

#label_dir = "/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_color"
#label_process_dir = '/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_wb'

label_dir = "/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_wb"
label_process_dir = '/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_wb'

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
                
        label_array[label_array == 1] =   1
        #label_array[label_array == 1] =   1    #??
        label_array[label_array == 0] = 0   #??
       # label_array[label_array == 106] = 2  
       # label_array[label_array == 84] = 2
       # label_array[label_array == 111] = 2
       # label_array[label_array == 208] = 2


        cv.imwrite(label_process_dir + file, label_array)


