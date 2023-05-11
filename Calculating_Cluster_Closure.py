import cv2
import numpy as np
import matplotlib.pyplot as plt
import os, glob
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

path = "...../"
#Search and List all files
search_criteria = "*.jpeg"
q = os.path.join(path, search_criteria)
ifiles = glob.glob(q)

search_criteria = "*.png"
q = os.path.join(path, search_criteria)
files = glob.glob(q)

#This is section is just to check wether you want to run for a specific image
# seg_img_value = "JJCabFranc_02072021_IMG_1343"
# img = cv2.imread(".../img.jpeg")
# seg_img = cv2.imread(".../segmented_img.png")

'''toggle this on if the cultivar is tight cluster'''
cultivar = 1
c = 1
df = pd.DataFrame()
grayImage = []
with PdfPages('count.pdf') as pdf_pages:
    #Loop through image files
    for file in files:
        '''Change this in a way where you have name of the file'''
        seg_img_value = file[125:-4]
        #Loop through segmented images
        for i in ifiles:
            if seg_img_value in i:
                #Read both of the image file
                img = cv2.imread(i)
                seg_img = cv2.imread(file)
                #Mask out the cluster bundaries False for bagkground and true for cluster pixels
                seg_mask = seg_img[:, :, 1] == 128
                #Make duplicate of the orginal images
                img2 = img.copy()
                #Covert the image into float
                img2 = img2.astype("float32")
                #Replace background pixels with NaN
                img2[seg_mask == False] = np.nan
                #Convert whole image into gery scale
                grayImage = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                #Check the toggle for cultivar
                if cultivar!=0:
                    grayImage = grayImage-40
                #Extract gray pixel only for cluster
                graynan = grayImage[np.isnan(grayImage) == False].astype('uint8')
                #Calculate Otsu's thresold
                ret3, th3 = cv2.threshold(graynan, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                #Convert gap pixels into white (255) and berries into black (0)
                img2[grayImage > ret3] = 255
                img2[grayImage <= ret3] = 0
                #Calculate total cluster area
                cluster_area = len(img2[img2[:, :, 1] == 0]) + len(img2[img2[:, :, 1] == 255])
                #Calculate total berry pixels devided by cluster area
                CC = ((len(img2[img2[:, :, 1] == 0]) / cluster_area) * 100)
                print(seg_img_value)
                print(CC)
                #Add values into dataframe
                df = df.append(pd.Series([i[43:-22],i[49:-13],file[54:-4],CC]),ignore_index=True)
                #Write images
                cv2.imwrite(path + "/final_segmented_img/" + seg_img_value + file[-9:], img2)
                fig = plt.figure(c)
                axes = fig.subplots(2, 2)
                axes[0, 0].imshow(img, cmap="brg")
                axes[0,0].set(title = file[-9:])
                axes[0, 1].imshow(grayImage, cmap="Greys")
                axes[1, 0].hist(grayImage.ravel(), 256, [0, 256])
                axes[1, 0].axvline(ret3, color='k', linestyle='dashed', linewidth=1)
                axes[1, 0].set(title=CC.__round__(2))
                axes[1, 1].imshow(img2, cmap="Greys")
                axes[1, 1].set(title=CC.__round__(2))
                pdf_pages.savefig(fig)
                c = c + 1
                plt.close(fig)

df.to_csv(path+"result.csv")
