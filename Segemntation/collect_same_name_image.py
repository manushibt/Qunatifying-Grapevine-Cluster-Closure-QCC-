import os
import shutil
import cv2  
#path1 = "/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_color" # lable
#path2 = '/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/image_merge' # image

#path1 = "/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/twoclass_manushiextra/label/" # lable
#path2 = "/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/twoclass_manushiextra/JPEGImages/" # image

path1 = "/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_wb" # lable
path2 = '/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/image_merge' # image

path = os.getcwd()
jpg_list = [x.split('.')[0] for x in os.listdir(path2) if x.endswith(".jpg")]
png_list = [x.split('.')[0] for x in os.listdir(path1) if x.endswith(".png")]
a = [x for x in jpg_list if x not in png_list]  #两个列表都存在
b = [x for x in png_list if x not in jpg_list]
#print('image,no label',a) 
print('image',len(jpg_list)) 
print('lable',len(png_list)) 
print('image,no label',len(a))
print('lable, no image',len(b) )

# 第一个文件夹里的4415需要去掉 
#twoclass_emily 中的lable里的 Ries 6-25——2043多余
'''
#change the lable name with the same image name 
#前3个数据集是可以跑通的
#list = []
for label in b:   
    #print(image[:n])
    #n = image.index('_merge_')
    for image in a:
        #
        # image[:n]
        n = image.index('_merge_')
        m = label.index('_merge_')
        if image[:n] == label[m+7:] and label [:m] == image[n+7:]:
            #print (image, label,'are the same name')
            nwe_lable_name = '/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_wb/'+str(image)+ ".png"
            lable_path = "/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_wb/"+ str(label) + ".png"
            print (image, label,'are the same name')
            #lable = cv2.imread(lable_path)
            #cv2.imwrite('/home/yz4891/PaddleSeg/all_data/Twoclass_Annotations/total_images/label_merge_color/'+str(im[0][:-4]) +'_merge_'+ str(im[1]), result3 )
            #list.append(image)

            os.rename(lable_path,nwe_lable_name)
            

       # if image[n:] == label[:]
#print(len(list))

'''


