import os
import cv2

path = r"C:\Users\Lohitaksh\Documents\Python\Project 105\PRO-C105-Project-Images-main\Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
print(frame.shape)

height, width, channels = frame.shape

size = (width, height)

#output = cv2.VideoWriter('Sunrise.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)
output = cv2.VideoWriter('Video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

#for i in range(count-1, 0, -1):
for i in range(0, count-1, 1):
    frame = cv2.imread(images[i])
    output.write(frame)

output.release()
print("Done!")    