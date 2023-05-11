import time
import time
from tqdm import tqdm
from tqdm import trange
import os
import cv2  
import numpy as np  
import matplotlib.pyplot as plt
from itertools import combinations

img_path = '/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label'
imgs = os.listdir(img_path)
names = []
for img in imgs:
    names.append(img)

add = list(combinations(names,2))
lenth =len(add)
print(len(add))
print (add[0])

#os.makedirs('/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_color')

i = 0
for im in add:
    im_path1 = img_path + '/'+ str(im[0])
    im_path2 = img_path + '/'+str(im[1])
    img1 = cv2.imread(im_path1)
    #gpu_frame.upload(img1 )
    img2_Ori = cv2.imread(im_path2)
    #gpu_frame.upload(img2_Ori )
    #print('im1',im_path1)
    img2 = cv2.resize(img2_Ori,(img1.shape[1], img1.shape[0])) 
    
    result3 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    cv2.imwrite('/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_wb/'+str(im[0][:-4]) +'_merge_'+ str(im[1]), result3 )
    #print('im2',im_path2)
   
    i=i+1
    percent= i/lenth*100
    print(percent)