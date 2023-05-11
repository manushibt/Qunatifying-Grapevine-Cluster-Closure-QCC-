import PIL
import numpy as np

label = PIL.Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations_color/IMG_3345.png")
label = np.array(label)

cnts = len(set(label))
cnt = 0
for i in set(label):
    label[label==i] = cnt 
    cnt += 1
#PIL.Image.write(label, "label_path")

im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations_color/IMG_3345.png"))

print('origial', np.unique(im))



