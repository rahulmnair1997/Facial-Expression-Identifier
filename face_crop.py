## This program first ensures if the face of a person exists in the given image or not then if it exists, it crops
## the image of the face and saves to the given directory.

import cv2
import os

directory ="C:/Users/admin/Desktop/INTEL/detect/images/neutral"
f_directory ="C:/Users/admin/Desktop/INTEL/detect/images/"
            
def facecrop(image):
    facedata = "C:/Users/admin/Desktop/INTEL/detect/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(facedata)
    img = cv2.imread(image)

    try:
        ## Some downloaded images are of unsupported type and should be ignored while raising Exception, so for that
        ## I'm using the try/except functions.
    
        minisize = (img.shape[1],img.shape[0])
        miniframe = cv2.resize(img, minisize)

        faces = cascade.detectMultiScale(miniframe)

        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            sub_face = img[y:y+h, x:x+w]

            f_name = image.split('/')
            f_name = f_name[-1]

            cv2.imwrite(f_directory + f_name, sub_face)
            print ("Writing: " + image)

    except:
        pass

if __name__ == '__main__':
    images = os.listdir(directory)
    i = 0
    
    for img in images:
        file = directory + img
        print (i)
        facecrop(file)
        i += 1
