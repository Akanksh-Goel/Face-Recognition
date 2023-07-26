# Importing libraries
import cv2 #Computer Vision
import numpy as np
import face_recognition as faceReg
import os
# import matplotlib.pyplot as plt
#Loading training images
def faceRegProg():
    img = []
    img_in = ['Aahana', 'Akanksh', 'Manyata']
    for n in os.listdir('Training photos'):
        img.append(faceReg.load_image_file(os.path.join('Training photos',n)))
    #Converting to RGB
    for x in range(len(img)):
        img[x] = cv2.cvtColor(img[x],cv2.COLOR_BGR2RGB)
    #Training data set with face encodings
    demo_train_encode=[]
    for x in range(len(img)):
        demo_train_encode.append(faceReg.face_encodings(img[x])[0])
    global demo
    # Loading test image
    for n in os.listdir('C:/Users/RP Goel/Pictures/Camera Roll'):
        if n != 'WIN_20160630_15_48_33_Pro.jpg':
            # print("hi1")
            loc=os.path.join('C:/Users/RP Goel/Pictures/Camera Roll',n)
            if n.endswith('.jpg') or n.endswith('.jpeg'):
                # print("hi")
                demo=faceReg.load_image_file(loc)
    demo = cv2.cvtColor(demo, cv2.COLOR_BGR2RGB)
    demo_encode = faceReg.face_encodings(demo)[0]
    face = faceReg.face_locations(demo)[0]
    """cv2.resize(demo, (2, 2))"""
    t=True
    org=(10, 30)
    font = cv2.FONT_HERSHEY_TRIPLEX
    fontScale= 1
    color = (16,16,222)
    thickness = 2
    for x in range(len(img)):
        if faceReg.compare_faces([demo_train_encode[x]], demo_encode)==[True]:
            print("The person is eligible to drive this car.")
            fname="The person is eligible to drive this car"
            cv2.putText(demo, 'Eligible person', org, font, fontScale, color, thickness)
            t = False
            break
    if(t):
        print("The person is not eligible to drive this car.")
        fname="The person is not eligible to drive this car"
        cv2.putText(demo, "Not eligible", org, font, fontScale, color, thickness)
    """copy = img.copy()
    cv2.imshow('copy', copy)
    cv2.imshow('PM Modi',img)"""
    cv2.rectangle(demo, (face[3], face[0]),(face[1], face[2]), (255,0,255), 2)
    cv2.imwrite('./faceReg_app/static/result.jpg', demo)
    # os.remove(loc)
    # cv2.waitKey(0)
    return fname