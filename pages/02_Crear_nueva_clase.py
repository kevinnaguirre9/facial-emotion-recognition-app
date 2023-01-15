import datetime

import streamlit as st

from containers.ServiceContainer import ServiceContainer
from src.Services.Class.Create.ClassCreator import ClassCreator
from src.Services.Class.Create.CreateClassCommand import CreateClassCommand

st.set_page_config(layout="wide")

st.sidebar.title("Sistema de Reconocimiento de Emociones")

st.subheader("Creación de Clase")

with st.form("create_class_form", clear_on_submit=True):

    subject = st.text_input("Materia")

    degree = st.text_input("Carrera")

    section = st.text_input("Aula/Curso")

    academic_period = st.text_input("Periodo académico")

    submitted = st.form_submit_button("Guardar")

    if submitted:
        if not subject:
            st.error("Campo materia es requerido")
            st.stop()
        elif not degree:
            st.error("Por favor, indique una carrera")
            st.stop()
        elif not section:
            st.error("Aula/Curso es requerido")
            st.stop()
        elif not academic_period:
            st.error("El periodo académico es requerido")
            st.stop()

        command = CreateClassCommand(
            subject = subject,
            degree = degree,
            section = section,
            academic_period = academic_period,
        )

        try:
            ClassCreator(ServiceContainer.class_repository()).handle(command)

            st.success("Clase creada con éxito")
        except Exception as e:
            print(e)
            st.error(
                "Error al crear la clase, revise las advertencias del formulario o comuníquese con el administrador"
            )