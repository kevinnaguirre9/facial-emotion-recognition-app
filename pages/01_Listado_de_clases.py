import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

from containers.ServiceContainer import ServiceContainer
from src.Services.Class.ClassResponse import ClassResponse

from src.Services.Class.Search.ClassesSearcher import ClassesSearcher
from src.Services.Class.Search.SearchClassesQuery import SearchClassesQuery
from src.Services.EmotionRecognition.Recognize.ClassroomStudentsEmotionsRecognizer import \
    ClassroomStudentsEmotionsRecognizer
from src.Services.Session.Create.CreateSessionCommand import CreateSessionCommand
from src.Services.Session.Create.SessionCreator import SessionCreator
from src.Services.Session.Finish.FinishSessionCommand import FinishSessionCommand
from src.Services.Session.Finish.SessionFinisher import SessionFinisher

st.set_page_config(layout="wide")

st.sidebar.title("Sistema de Reconocimiento de Emociones")

st.title("Listado de clases")


classes_query = SearchClassesQuery({}, 1, 5)

classes = ClassesSearcher(ServiceContainer.class_repository())\
    .handle(classes_query)

if not classes.classes():
    st.write("No hay clases disponibles")
    st.stop()

def start_emotion_recognition_session(class_data: ClassResponse):
    create_session_command = CreateSessionCommand(class_data.class_id())

    session = SessionCreator(
        ServiceContainer.session_repository(),
        ServiceContainer.class_repository(),
    ).handle(create_session_command)

    st.session_state.session_id = session.session_id().value()
    st.session_state.class_subject = class_data.subject()

def finish_emotion_recognition_session():
    del st.session_state['session_id']


# ---------- START CLASSES LIST ----------

columns = st.columns(6)
fields = ["№", 'Materia', 'Carrera', 'Sección', "Periodo", "Acciones"]
for col, field_name in zip(columns, fields):
    header_text = f'<p style="color:rgb(255, 75, 75); font-size: 15px;">{field_name}</p>'
    col.markdown(header_text, unsafe_allow_html=True)


for index, class_response in enumerate(classes.classes()):
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.write(index + 1)
    with col2:
        st.write(class_response.subject())
    with col3:
        st.write(class_response.degree())
    with col4:
        st.write(class_response.section())
    with col5:
        st.write(class_response.academic_period())
    with col6:
        st.button(
            'Iniciar',
            key=index,
            help="Iniciar sesión de reconocimiento de emociones",
            on_click=start_emotion_recognition_session,
            kwargs={"class_data": class_response},
        )

# ---------- END CLASSES LIST ----------


# ---------- START WEB RTC STREAM ----------

if 'session_id' in st.session_state:

    st.write("Sesión de reconocimiento de emociones")

    webrtc_streamer(
        key="example",
        mode=WebRtcMode.SENDRECV,
        media_stream_constraints={"video": True},
        # video_html_attrs={
        #     "style": {"width": "100%", "margin": "0 auto", "border": "5px white solid"},
        #     "controls": False,
        #     "autoPlay": True,
        # },
        video_frame_callback=ClassroomStudentsEmotionsRecognizer(
            ServiceContainer.emotion_recognition_repository(),
            st.session_state.session_id,
        ).recognize,
        on_video_ended=SessionFinisher(ServiceContainer.session_repository(), st.session_state.session_id).handle,
    )

    st.button(
        'Finalizar',
        key='finish',
        help="Finalizar sesión de reconocimiento de emociones",
        on_click=finish_emotion_recognition_session,
    )

# ---------- END WEB RTC STREAM ----------