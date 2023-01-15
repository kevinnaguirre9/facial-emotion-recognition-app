import pandas as pd
import streamlit as st
import altair as alt

from containers.ServiceContainer import ServiceContainer
from src.Services.EmotionRecognition.Search.EmotionRecognitionsSearcher import EmotionRecognitionsSearcher
from src.Services.EmotionRecognition.Search.SearchEmotionRecognitionsQuery import SearchEmotionRecognitionsQuery
from src.Services.Session.Search.SearchSessionsQuery import SearchSessionsQuery
from src.Services.Session.Search.SessionsSearcher import SessionsSearcher


# ---------- PAGE STYLES-CONFIGS ----------

st.set_page_config(layout="wide")

st.sidebar.title("Sistema de Reconocimiento de Emociones")

st.title("Sesiones de reconocimiento de emociones")

# ---------- END PAGE STYLES-CONFIGS ---------


# ---------- SHOW STATISTICS ----------

def show_statistics(session_id: str):
    st.session_state.session_id_statistics = session_id


# ---------- END SHOW STATISTICS ----------


# ---------- SEARCH SESSIONS ----------

query = SearchSessionsQuery({}, 1, 5)

sessions_response = SessionsSearcher(
    ServiceContainer.session_repository(),
    ServiceContainer.class_repository()
).handle(query)

if not sessions_response.sessions():
    st.write("No hay sesiones disponibles")
    st.stop()

# ---------- END SEARCHING ----------


# ---------- START SESSIONS LIST ----------

columns = st.columns(5)
fields = ["№", 'Clase', 'Inicio', "Fin", "Acciones"]
for col, field_name in zip(columns, fields):
    header_text = f'<p style="color:rgb(255, 75, 75); font-size: 15px;">{field_name}</p>'
    col.markdown(header_text, unsafe_allow_html=True)


for index, session_response in enumerate(sessions_response.sessions()):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(index + 1)
    with col2:
        st.write(f'{session_response.class_subject()} - {session_response.class_degree()}')
    with col3:
        st.write(session_response.started_at())
    with col4:
        st.write(session_response.ended_at() if session_response.ended_at() else "En curso")
    with col5:
        st.button(
            'Ver Estadísticas',
            key=index,
            help="Ver Estadísticas",
            on_click=show_statistics,
            kwargs={"session_id": session_response.session_id()}
        )


# ---------- END SESSIONS LIST ----------


# ---------- STATISTICS FOR EMOTION RECOGNITION SESSION ----------

if 'session_id_statistics' in st.session_state:

    st.title("Estadísticas de la sesión")

    search_emotion_recognitions_query = SearchEmotionRecognitionsQuery(
        {
            "session_id": st.session_state.session_id_statistics
        }
    )

    emotion_recognitions = EmotionRecognitionsSearcher(
        ServiceContainer.emotion_recognition_repository()
    ).handle(search_emotion_recognitions_query)

    if not emotion_recognitions.emotion_recognitions():
        st.write("No hay estadísticas disponibles")
        st.stop()

    emotion_recognition_raw_records = list(
        map(
            lambda emotion_recognition_response: emotion_recognition_response.to_dict(),
            emotion_recognitions.emotion_recognitions()
        )
    )

    # ---------- BASIC METRICS  ----------

    df = pd.DataFrame(emotion_recognition_raw_records)

    df['recorded_at'] = pd.to_datetime(df['recorded_at'])

    df = df.set_index('recorded_at')

    df = df.drop(columns=['emotion_recognition_id', 'session_id'])

    df_grouped = df.mean().round().sort_values(ascending=False)

    st.write('Promedio de estudiantes por emociones')

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    col1.metric('Feliz', df_grouped['happy'])
    col2.metric('Triste', df_grouped['sad'])
    col3.metric('Enojado', df_grouped['angry'])
    col4.metric('Sorprendido', df_grouped['surprised'])
    col5.metric('Neutral', df_grouped['neutral'])
    col6.metric('Disgustado', df_grouped['disgusted'])
    col7.metric('Con miedo', df_grouped['fearful'])

    # ---------- END BASIC METRICS  ----------

    # ---------- GRAPHIC METRICS  ----------

    st.write('Gráfico del promedio de emociones por estudiantes')
    st.line_chart(df)

    # Altair chart
    df = pd.DataFrame(emotion_recognition_raw_records)
    df['recorded_at'] = pd.to_datetime(df['recorded_at'])
    df = df.set_index('recorded_at')
    df = df.drop(columns=['emotion_recognition_id', 'session_id'])

    df_grouped = df.mean().reset_index()
    df_grouped.columns = ['emotion', 'total_students']

    source_dataframe = pd.DataFrame(df_grouped)

    bar_chart = alt.Chart(source_dataframe).mark_bar().encode(
        x=alt.X('emotion', title='Emotion'),
        y=alt.Y('total_students', title='Average students'),
        color=alt.Color('emotion', legend=None),
    )

    st.altair_chart(bar_chart, use_container_width=True)

    # ---------- END GRAPHIC METRICS  ----------

# ---------- END STATISTICS FOR EMOTION RECOGNITION SESSION ----------



