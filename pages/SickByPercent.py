import streamlit as st
import pandas as pd    

st.header("Hvor mange dager sykmelding utgjør X prosent?")

FullTimeHours = 37.5
WorkHoursPrDay = 7.5

FullTimeHours= st.number_input("Antall timer fulltid i uken",0.0,100.0,FullTimeHours)

VacancyRate = 80.0


VacancyRate = st.number_input("Hilken stillingsprosent har vedkommende:",0.0,100.0,VacancyRate)

WorkingHoursPrWeek = round(FullTimeHours*VacancyRate/100,1)

st.write(f"Personen jobber {WorkingHoursPrWeek} timer i uken")


SickLeavePercentage = 25.0

SickLeavePercentage = st.number_input("Hilken sykemeldingsprosent vurderes:",0.0,100.0,SickLeavePercentage)


SickLeaveHours = round(SickLeavePercentage*WorkingHoursPrWeek/100,1)
SickLeaveDays = round(SickLeaveHours/WorkHoursPrDay,1)


st.subheader(f"Dersom man ønsker {SickLeavePercentage}% sykemelding og jobber {VacancyRate}% stilling, så utgjør det {SickLeaveHours} timer eller {SickLeaveDays} dag(er) pr. uke.")