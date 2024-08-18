import streamlit as st
import pandas as pd

st.title("MedApp")

FullTimeHours = 37.5
WorkHoursPrDay = 7.5

FullTimeHours= st.number_input("Antall timer fulltid i uken",0.0,100.0,FullTimeHours)


VacancyRate = 80.0


VacancyRate = st.number_input("Hilken stillingsprosent har vedkommene:",0.0,100.0,VacancyRate)

WorkingHoursPrWeek = round(FullTimeHours*VacancyRate/100,1)

st.write(f"Personen jobber {WorkingHoursPrWeek} timer i uken")

SickLeavePercentage = 25.0

SickLeavePercentage = st.number_input("Hilken sykemeldingsprosent vurderes:",0.0,100.0,SickLeavePercentage)

SickLeaveHours = round(SickLeavePercentage*WorkingHoursPrWeek/100,1)
SickLeaveDays = round(SickLeaveHours/WorkHoursPrDay,1)


st.write(f"Personen sykemeldes {SickLeaveHours} timer pr uke")
st.write(f"Personen sykemeldes {SickLeaveDays} dager pr uke")

OnsketDagerSykPrUke = 0.0

OnsketDagerSykPrUke = st.number_input("Hvor mange dager syk vurderes:",0.0,100.0,OnsketDagerSykPrUke)

SickLeavePercentage = round((OnsketDagerSykPrUke*WorkHoursPrDay)/WorkingHoursPrWeek)*100

st.write(f"Dersom man ønsker {OnsketDagerSykPrUke} sykedager pr uke, blir sykeprosenten {SickLeavePercentage}%")
