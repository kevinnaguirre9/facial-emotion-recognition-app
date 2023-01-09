import streamlit as st
from containers.ServiceContainer import ServiceContainer

from src.Services.Class.Search.ClassesSearcher import ClassesSearcher
from src.Services.Class.Search.SearchClassesQuery import SearchClassesQuery

st.set_page_config(layout="wide")

st.title("Listado de clases")

# # Path: pages\01_Listado_de_clases.py
classes_query = SearchClassesQuery({}, 1, 5)

classes = ClassesSearcher(ServiceContainer.class_repository())\
    .handle(classes_query)

if not classes.classes():
    st.write("No hay clases disponibles")
    st.stop()

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
        st.button('Iniciar', key=index, help="Iniciar sesión de reconocimiento de emociones")