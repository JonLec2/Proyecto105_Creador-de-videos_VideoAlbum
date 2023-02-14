import cv2
import os
import numpy
path="Images/"
images=[]

images1=os.listdir(path)
for filename in images1:
    name, extension =os.path.splitext(filename)
    if extension=='':
        continue
    if extension in ['.gif', '.png', '.jpg', 'jpeg', 'jfif']:
       file_name=path+name+extension
       images.append(file_name)
      
       
print(images)
frame=cv2.imread(images[0])
dimensions=frame.shape
size=(frame.shape[0], frame.shape[0])
print(size)

out=cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
