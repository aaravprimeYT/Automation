# task is taking pictures for sharing to family

import dropbox
import time
import cv2
import random

startTime = time.time()

def takeSnapshot():
    number = random.randint(0,50)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while result:
        ret,frame = videoCaptureObject.read()
        imageName = "image" + str(number) + ".png"
        cv2.imwrite(imgName,frame)
        result = False
        startTime = time.time()
    return imgName
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFiles(imageName):
    accessToken = "Hq6d1c1qg4wAAAAAAAAAAYKlyT3MSZBlEcwVSxr7bxh0wkWUHcWGjGsylYO4eEUk"
    fileFrom = imageName
    fileTo = "/Automation/" + (imageName)

    dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom,"rb") as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print("File has been uploaded")

def main():
    while True:
        if((time.time()-startTime)>=1000000):
            name = takeSnapshot()
            uploadFiles(name)

main()  