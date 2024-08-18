import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


st.title("MedApp")

FullTimeHours = 37.5
WorkHoursPrDay = 7.5

FullTimeHours= st.number_input("Antall timer fulltid i uken",0.0,100.0,FullTimeHours)


VacancyRate = 80.0


VacancyRate = st.number_input("Hilken stillingsprosent har vedkommene:",0.0,100.0,VacancyRate)

WorkingHoursPrWeek = round(FullTimeHours*VacancyRate/100,1)

st.write(f"Personen jobber {WorkingHoursPrWeek} timer i uken")




col1, col2 = st.columns((1,1))


with col1:

    st.title("Sykemeldes med utgangspunkti i prosent:")

    SickLeavePercentage = 25.0

    SickLeavePercentage = st.number_input("Hilken sykemeldingsprosent vurderes:",0.0,100.0,SickLeavePercentage)

    SickLeaveHours = round(SickLeavePercentage*WorkingHoursPrWeek/100,1)
    SickLeaveDays = round(SickLeaveHours/WorkHoursPrDay,1)


    st.subheader(f"Personen sykemeldes {SickLeaveHours} timer pr uke")
    st.subheader(f"Personen sykemeldes {SickLeaveDays} dager pr uke")

with col2:

    st.title("Sykemeldes med utgangspunkti i dager:")


    OnsketDagerSykPrUke = 0.0

    OnsketDagerSykPrUke = st.number_input("Hvor mange dager syk vurderes:",0.0,100.0,OnsketDagerSykPrUke)

    SickLeavePercentage = round((OnsketDagerSykPrUke*WorkHoursPrDay)/WorkingHoursPrWeek)*100

    st.subheader(f"Dersom man ønsker {OnsketDagerSykPrUke} sykedager pr uke, blir sykeprosenten {SickLeavePercentage}%")
