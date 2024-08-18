import streamlit as st
import pandas as pd    

st.header("Hvor mange prosent sykmelding utgjør X antall dager?")

FullTimeHours = 37.5
WorkHoursPrDay = 7.5

FullTimeHours= st.number_input("Antall timer fulltid i uken",0.0,100.0,FullTimeHours)


VacancyRate = 80.0


VacancyRate = st.number_input("Hilken stillingsprosent har vedkommende:",0.0,100.0,VacancyRate)

WorkingHoursPrWeek = round(FullTimeHours*VacancyRate/100,1)

st.write(f"Personen jobber {WorkingHoursPrWeek} timer i uken")

OnsketDagerSykPrUke = 0.0

OnsketDagerSykPrUke = st.number_input("Hvor mange dager syk vurderes:",0.0,100.0,OnsketDagerSykPrUke)

SickLeavePercentage = round(((OnsketDagerSykPrUke*WorkHoursPrDay)/WorkingHoursPrWeek)*100,1)

st.subheader(f"Dersom man ønsker {OnsketDagerSykPrUke} sykedag(er) pr uke og jobber {VacancyRate}% stilling, blir sykeprosenten {SickLeavePercentage}%")