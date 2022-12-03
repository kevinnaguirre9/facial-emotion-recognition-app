import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
from streamlit_modal import Modal
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
import av
import cv2
import pandas as pd
import numpy as np

# st.set_page_config(layout="wide")

# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

#Face detection app
st.title('Face emotion detection app')

st.subheader('Press start for capturing students in classroom!')


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
model.load_weights('src/neural-network/model.h5')

# prevents openCL usage and unnecessary logging messages
cv2.ocl.setUseOpenCL(False)

# dictionary which assigns each label an emotion (alphabetical order)
emotions = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}


def detectEmotions(frame: av.VideoFrame) -> av.VideoFrame:

    newFrame = frame.to_ndarray(format="bgr24")

    #First, the haar cascade method is used to detect faces in each frame of the webcam feed.
    faceCascadeClassifier = cv2.CascadeClassifier('src/haarcascade_frontalface_default.xml')

    # Must be converted to gray 'cause we trained our model with gray colored images
    grayScaleFrame = cv2.cvtColor(newFrame, cv2.COLOR_BGR2GRAY)

    # Detect all faces in the video stream frame
    facesDetected = faceCascadeClassifier.detectMultiScale(grayScaleFrame,scaleFactor=1.3, minNeighbors=5)

    # For each detected face found in the frame, we predict their emotions
    for (cornerX, cornerY, width, heigth) in facesDetected:
        
        # draw a rectangle around the face in the original captured frame
        cv2.rectangle(newFrame, (cornerX, cornerY-50), (cornerX+width, cornerY+heigth+10), (255, 0, 0), 2)


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
        cv2.putText(newFrame, emotions[maxIndex], (cornerX+20, cornerY-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    return av.VideoFrame.from_ndarray(newFrame, format="bgr24")


# Just a simple callback when video ends
def endVideo():
    print("Video has ended!")

# webrtc_streamer(
#     key="example", 
#     mode=WebRtcMode.SENDRECV,
#     media_stream_constraints={"video": True},
#     # video_html_attrs={
#     #     "style": {"width": "100%", "margin": "0 auto", "border": "5px white solid"},
#     #     "controls": False,
#     #     "autoPlay": True,
#     # },
#     video_frame_callback=detectEmotions,
#     on_video_ended=endVideo,
# )





def openModal(identifier):
    # modal = Modal("Demo Modal", identifier)
    # # open_modal = st.button("Open")
    # # if open_modal:
    # #     modal.open()

    # # modal.open()

    # if modal.is_open():
    #     with modal.container():
    #         st.write("Text goes here")


    #         webrtc_streamer(
    #             key=f"example{identifier}",
    #             mode=WebRtcMode.SENDRECV,
    #             media_stream_constraints={"video": True},
    #             # video_html_attrs={
    #             #     "style": {"width": "100%", "margin": "0 auto", "border": "5px white solid"},
    #             #     "controls": False,
    #             #     "autoPlay": True,
    #             # },
    #             video_frame_callback=detectEmotions,
    #             on_video_ended=endVideo,
    #         )

    #         st.write("Some fancy text")
    #         value = st.checkbox("Check me", key=identifier)
    #         st.write(f"Checkbox checked: {value}")
    print(identifier)



user_data = [
    {
        'email': 'test@gmail.com',
        'uid': 'uuid1',
        'verified': True,
        'disabled': False,
    },
    {
        'email': 'test1@gmail.com',
        'uid': 'uuid2',
        'verified': True,
        'disabled': True,
    },
    {
        'email': 'test2@gmail.com',
        'uid': 'uuid3',
        'verified': True,
        'disabled': False,
    }
];

user_table = pd.DataFrame(user_data)


colms = st.columns((1, 2, 2, 1, 1))
fields = ["№", 'email', 'uid', 'verified', "action"]
for col, field_name in zip(colms, fields):
    # header
    col.write(field_name)

for x, email in enumerate(user_table['email']):
    col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
    col1.write(x)  # index
    col2.write(user_table['email'][x])  # email
    col3.write(user_table['uid'][x])  # unique ID
    col4.write(user_table['verified'][x])   # email status
    disable_status = user_table['disabled'][x]  # flexible type of button
    button_type_text = "Unblock" if disable_status else "Block"
    button_phold = col5.empty()  # create a placeholder
    do_action = button_phold.button(button_type_text, key=x, on_click=openModal, kwargs=dict(identifier=x))
    # if do_action:
    #         pass # do some action with a row's data
    #         button_phold.empty()  #  remove butt
