import os
import string

dirName = "/cis/phd/yz4891/PaddleSeg/all_data/Twoclass_Annotations/twoclass_will/JPEGImages/"  #???????,?????
li=os.listdir(dirName)
#print (li)


for filename in li:
  newname = filename
  newname = newname.split(".")
  if newname[-1]=="jpeg":
    newname[-1]="jpg"
    newname = str.join(".",newname) #????str.join
    filename = dirName+filename
    newname = dirName+newname
    os.rename(filename,newname)
    print(newname,"updated successfully")
