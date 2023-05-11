from PIL import Image
import numpy as np     
image = Image.open("/cis/phd/yz4891/PaddleSeg/data/optic_disc_seg/Annotations/H0002.png")
print(" ------------------------standard______________________________________ ")
print("Filename: ", image.filename)
print("Format: ", image.format)
print("Mode: ", image.mode)
print("Size: ", image.size)
print("Width: ", image.width)
print("Height: ", image.height)
print("Is Animated: ", (getattr(image, "is_animated", False)))
print("Frames in Image", getattr(image, "n_frames", 1))
image.close()   # close image file


image = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3345.png")
print(" ------------------------my_lable_after change______________________________________ ")
image =image.convert("P")

im = np.asarray(image)
print('grey_lable', np.unique(im))
print("Mode: ", image.mode)
image = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3345.png")
print("Filename: ", image.filename)
print("Format: ", image.format)
#print("Mode: ", image.mode)
print("Size: ", image.size)
print("Width: ", image.width)
print("Height: ", image.height)
print("Is Animated: ", (getattr(image, "is_animated", False)))
print("Frames in Image", getattr(image, "n_frames", 1))
image.close()   # close image file


image = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations_color/IMG_3345.png")
print(" ------------------------my_lable_original______________________________________ ")
imagep =image.convert("P")
print("Mode: ", imagep.mode)
im = np.asarray(image)
print('origial', np.unique(im))
image = Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations_color/IMG_3345.png")
print("Filename: ", image.filename)
print("Format: ", image.format)
print("Mode: ", image.mode)
print("Size: ", image.size)
print("Width: ", image.width)
print("Height: ", image.height)
print("Is Animated: ", (getattr(image, "is_animated", False)))
print("Frames in Image", getattr(image, "n_frames", 1))
image.close()   # close image file








im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations_color/IMG_3345.png"))

print('origial', np.unique(im))
im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/dataset/annotations/IMG_3345.png"))
print('grey', np.unique(im))
im = np.asarray(Image.open("/cis/phd/yz4891/PaddleSeg/data/optic_disc_seg/Annotations/H0002.png"))
print('standard' , np.unique(im)) # np.unique( )??? ??????????,?????????
