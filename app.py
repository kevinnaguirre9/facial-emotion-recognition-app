import logging
import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
import pandas as pd
import altair as alt
from containers.ServiceContainer import ServiceContainer
from src.Services.EmotionRecognition.Recognize.ClassroomStudentsEmotionsRecognizer import \
    ClassroomStudentsEmotionsRecognizer
import src

st.set_page_config(layout="wide")

st.set_option('deprecation.showPyplotGlobalUse', False)

st.sidebar.title("Students Emotion Recognition System")

#
# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         footer {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------

st.title('Face emotion detection containers')

st.subheader('Press start for capturing students in classroom!')

# if __name__ == "__main__":
container = ServiceContainer()
container.init_resources()
container.wire(packages=[src])

logger = logging.getLogger(__name__)
logger.debug("'--------------------------------------Starting streamlit app")

#
# LOGGER = logging.getLogger(__name__)
# LOGGER.addHandler(logging.StreamHandler())
#
# LOGGER.info('--------------------------------------')
# LOGGER.debug("Starting video streamer...")
# LOGGER.info('--------------------------------------')


# Just a simple callback when video ends
def endVideo():
    print("Video has ended!")


webrtc_streamer(
    key = "example",
    mode = WebRtcMode.SENDRECV,
    media_stream_constraints = {"video": True},
    # video_html_attrs={
    #     "style": {"width": "100%", "margin": "0 auto", "border": "5px white solid"},
    #     "controls": False,
    #     "autoPlay": True,
    # },
    video_frame_callback = ClassroomStudentsEmotionsRecognizer(
        container.emotion_recognition_repository(),
        'b31769ab-3221-44f6-a154-52a0e72a0347',
    ).recognize,
    on_video_ended = endVideo,
)

# --------------------------------------------------------------------------------------------------------------

datetime_str_one = '2022-12-25 09:30:00'
datetime_str_two = '2022-12-25 09:30:05'
datetime_str_three = '2022-12-25 09:30:10'
datetime_str_four = '2022-12-25 09:30:15'

# 👇️ convert string to datetime object
# datetime_one = datetime.strptime(datetime_str_one, '%Y-%m-%d %H:%M:%S')
# datetime_two = datetime.strptime(datetime_str_two, '%Y-%m-%d %H:%M:%S')
# datetime_three = datetime.strptime(datetime_str_three, '%Y-%m-%d %H:%M:%S')
# datetime_four = datetime.strptime(datetime_str_four, '%Y-%m-%d %H:%M:%S')

emotion_records = [
    {
        'emotion_recognition_id': 'uuid123',
        'session_id': 'uuid1',
        'happy': 11,
        'sad': 0,
        'angry': 0,
        'surprise': 5,
        'neutral': 5,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_one,
    },
    {
        'emotion_recognition_id': 'uuid456',
        'session_id': 'uuid1',
        'happy': 15,
        'sad': 0,
        'angry': 0,
        'surprise': 0,
        'neutral': 6,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_two,
    },
    {
        'emotion_recognition_id': 'uuid789',
        'session_id': 'uuid1',
        'happy': 12,
        'sad': 1,
        'angry': 1,
        'surprise': 1,
        'neutral': 6,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_three,
    },
    {
        'emotion_recognition_id': 'uuid101112',
        'session_id': 'uuid1',
        'happy': 9,
        'sad': 2,
        'angry': 1,
        'surprise': 3,
        'neutral': 5,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_four,
    },
]

# Matplotlib time graphic with the emotions by time
df = pd.DataFrame(emotion_records)
st.dataframe(df)
df['recorded_at'] = pd.to_datetime(df['recorded_at'])
df = df.set_index('recorded_at')
df = df.drop(columns=['emotion_recognition_id', 'session_id'])
st.dataframe(df)

st.title('Average students by emotion dataframe')
df_grouped = df.mean().round().sort_values(ascending=False)
st.dataframe(df_grouped)


st.title('First Mean Metrics')
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
col1.metric('Happy', df_grouped['happy'])
col2.metric('Sad', df_grouped['sad'])
col3.metric('Angry', df_grouped['angry'])
col4.metric('Surprised', df_grouped['surprise'])
col5.metric('Neutral', df_grouped['neutral'])
col6.metric('Disgusted', df_grouped['disgusted'])
col7.metric('Fearful', df_grouped['fearful'])

st.title('Emotion with the highest mean total')
st.write(df_grouped.idxmax())
st.write(df_grouped.max())

# plt.plot(df)
# plt.title('Total students by emotion')
# plt.xlabel('Time')
# plt.ylabel('Total students')
# plt.legend(
#     ['Happy', 'Sad', 'Angry', 'Surprised', 'Neutral', 'Disgusted', 'Fearful'],
#     fontsize='small',
# )
# st.pyplot()

# streamlit line charts with legends
st.title('Total students by emotion chart')
st.line_chart(df)

# -------------------------- Using altair --------------------------

st.title('Using ALTAIR')

emotion_records = [
    {
        'emotion_recognition_id': 'uuid123',
        'session_id': 'uuid1',
        'happy': 11,
        'sad': 0,
        'angry': 0,
        'surprise': 5,
        'neutral': 5,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_one,
    },
    {
        'emotion_recognition_id': 'uuid456',
        'session_id': 'uuid1',
        'happy': 15,
        'sad': 0,
        'angry': 0,
        'surprise': 0,
        'neutral': 6,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_two,
    },
    {
        'emotion_recognition_id': 'uuid789',
        'session_id': 'uuid1',
        'happy': 12,
        'sad': 1,
        'angry': 1,
        'surprise': 1,
        'neutral': 6,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_three,
    },
    {
        'emotion_recognition_id': 'uuid101112',
        'session_id': 'uuid1',
        'happy': 9,
        'sad': 2,
        'angry': 1,
        'surprise': 3,
        'neutral': 5,
        'disgusted': 0,
        'fearful': 0,
        'recorded_at': datetime_str_four,
    },
]

# Matplotlib time graphic with the emotions by time
df = pd.DataFrame(emotion_records)
st.dataframe(df)
df['recorded_at'] = pd.to_datetime(df['recorded_at'])
df = df.set_index('recorded_at')
df = df.drop(columns=['emotion_recognition_id', 'session_id'])
st.dataframe(df)

df_grouped = df.mean().reset_index()
df_grouped.columns = ['emotion', 'total_students']
st.dataframe(df_grouped)
# st.write(df_grouped.index)
# st.write(df_grouped.iloc[:, [0]].toList())
# st.write(df_grouped.iloc[:, [1]])
st.write(df_grouped['emotion'].tolist())
st.write(df_grouped['total_students'].tolist())

source_dataframe = pd.DataFrame(df_grouped)

bar_chart = alt.Chart(source_dataframe).mark_bar().encode(
    x=alt.X('emotion', title='Emotion'),
    y=alt.Y('total_students', title='Average students'),
    color=alt.Color('emotion', legend=None),
)

st.altair_chart(bar_chart, use_container_width=True)