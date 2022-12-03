import numpy as np
import cv2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Create the model
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))


# emotions will be displayed on your face from the webcam feed
model.load_weights('model.h5')

# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

# dictionary which assigns each label an emotion (alphabetical order)
emotions = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

# start the webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Start reading frames from webcam
    readSucceed, frame = cap.read()
    
    if not readSucceed:
        break

    #First, the haar cascade method is used to detect faces in each frame of the webcam feed.
    faceCascadeClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Must be converted to gray 'cause we trained our model with gray colored images
    grayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect all faces in the video stream frame
    facesDetected = faceCascadeClassifier.detectMultiScale(grayScaleFrame,scaleFactor=1.3, minNeighbors=5)

    # For each detected face found in the frame, we predict their emotions
    for (cornerX, cornerY, width, heigth) in facesDetected:
        
        # draw a rectangle around the face in the original captured frame
        cv2.rectangle(frame, (cornerX, cornerY-50), (cornerX+width, cornerY+heigth+10), (255, 0, 0), 2)


        ##### Init prediction process

        # Region of interest, it is the specific face in the whole gray converted image
        roi_gray = grayScaleFrame[cornerY:cornerY + heigth, cornerX:cornerX + width]
        
        # The region of image containing the face is resized to 48x48 and is passed as input to the CNN
        croppedImage = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        
        # The network outputs a list of softmax scores (%) for the seven classes of emotions
        prediction = model.predict(croppedImage)

        # Get the index of the emotion with max score
        maxIndex = int(np.argmax(prediction))

        ##### End prediction process


        # Pu a text with the predicted emotion in each face in the original captured frame
        cv2.putText(frame, emotions[maxIndex], (cornerX+20, cornerY-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Now, show the image with the rectangles around the faces and their emotions predictions
    cv2.imshow('Video', cv2.resize(frame,(800,480),interpolation = cv2.INTER_CUBIC))
    
    # Exist emotion recognition process in case of ...
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Exit camera feed

cv2.destroyAllWindows() # Close windows opened by cv2 with imshow method