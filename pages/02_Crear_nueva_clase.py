import datetime

import streamlit as st

from containers.ServiceContainer import ServiceContainer
from src.Domain.Class.ValueObjects.Weekday import Weekday
from src.Services.Class.Create.ClassCreator import ClassCreator
from src.Services.Class.Create.CreateClassCommand import CreateClassCommand

WEEKDAY_VALUES_TRANSLATIONS = {
    'Lunes': Weekday.MONDAY.name,
    'Martes': Weekday.TUESDAY.name,
    'Miércoles': Weekday.WEDNESDAY.name,
    'Jueves': Weekday.THURSDAY.name,
    'Viernes': Weekday.FRIDAY.name,
    'Sábado': Weekday.SATURDAY.name,
    'Domingo': Weekday.SUNDAY.name,
}


def get_selected_weekday_value(option):
    return WEEKDAY_VALUES_TRANSLATIONS[option]


with st.form("create_class_form"):

    st.write("Creación de Clase")

    subject = st.text_input("Materia")

    degree = st.text_input("Carrera")

    section = st.text_input("Aula/Curso")

    academic_period = st.text_input("Periodo académico")

    weekday = st.selectbox(
        'Día',
        WEEKDAY_VALUES_TRANSLATIONS.keys()
    )

    schedule_start_time = st.time_input('Hora inicio', datetime.time(7, 0))

    schedule_end_time = st.time_input('Hora fin', datetime.time(9, 0))

    submitted = st.form_submit_button("Guardar")

    if submitted:

        # Validate form data
        if not subject:
            st.error("Materia es requerida")
            st.stop()
        elif not degree:
            st.error("Carrera es requerida")
            st.stop()
        elif not section:
            st.error("Sección es requerida")
            st.stop()
        elif not academic_period:
            st.error("Periodo académico es requerido")
            st.stop()

        command = CreateClassCommand(
            subject=subject,
            degree=degree,
            section=section,
            academic_period=academic_period,
            weekly_schedule=[
                {
                    'weekday': get_selected_weekday_value(weekday),
                    'start_time': schedule_start_time.strftime('%H:%M'),
                    'end_time': schedule_end_time.strftime('%H:%M'),
                }
            ]
        )

        try:
            ClassCreator(ServiceContainer.class_repository()).handle(command)

            st.success("Clase creada con éxito")
        except Exception as e:
            st.error(e)

