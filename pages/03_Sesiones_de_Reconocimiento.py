import streamlit as st

from containers.ServiceContainer import ServiceContainer
from src.Services.Session.Search.SearchSessionsQuery import SearchSessionsQuery
from src.Services.Session.Search.SessionsSearcher import SessionsSearcher


# ---------- PAGE STYLES-CONFIGS ----------

st.set_page_config(layout="wide")

st.title("Sesiones de reconocimiento de emociones")

# ---------- END PAGE STYLES-CONFIGS ---------


# ---------- SHOW STATISTICS ----------

def show_statistics(session_id: str):
    st.session_state.session_id = session_id


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


# ---------- STATISTICS FOR SESSION ----------


if 'session_id' in st.session_state:

    st.write("Estadísticas de la sesión")

