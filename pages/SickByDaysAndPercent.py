import streamlit as st
import pandas as pd    


if st.button("Hovedmeny - Tilbake til MedCalc menyen."):
    st.switch_page("MedCalc.py")

conInfoWorker = st.container(border=True)

conInfoWorker.subheader("Info om arbeidstager:")

FullTimeHours = 37.5
WorkHoursPrDay = 7.5

FullTimeHours= conInfoWorker.number_input("Antall timer fulltid i uken",0.0,100.0,FullTimeHours,format="%0.1f")

VacancyRate = 80.0

VacancyRate = conInfoWorker.number_input("Hilken stillingsprosent har vedkommende:",0.0,100.0,VacancyRate,format="%0.1f")

WorkingHoursPrWeek = round(FullTimeHours*VacancyRate/100,1)

conInfoWorker.write(f"Personen jobber {WorkingHoursPrWeek} timer i uken")


conSickByDay = st.container(border=True)
  
conSickByDay.subheader("Hvor mange prosent sykmelding utgjør X antall dager?")

OnsketDagerSykPrUke = 0.0

OnsketDagerSykPrUke = conSickByDay.number_input("Hvor mange dager syk vurderes:",0.0,100.0,OnsketDagerSykPrUke,format="%0.1f")

SickLeavePercentage = round(((OnsketDagerSykPrUke*WorkHoursPrDay)/WorkingHoursPrWeek)*100,1)

conSickByDay.write(f"Dersom man ønsker {OnsketDagerSykPrUke} sykedag(er) pr uke og jobber {VacancyRate}% stilling, blir sykeprosenten {SickLeavePercentage}%")
    

conSickByPercent = st.container(border=True)

conSickByPercent.subheader("Hvor mange dager sykmelding utgjør X prosent?")

SickLeavePercentage = 25.0

SickLeavePercentage = conSickByPercent.number_input("Hilken sykemeldingsprosent vurderes:",0.0,100.0,SickLeavePercentage,format="%0.1f")

SickLeaveHours = round(SickLeavePercentage*WorkingHoursPrWeek/100,1)
SickLeaveDays = round(SickLeaveHours/WorkHoursPrDay,1)

conSickByPercent.write(f"Dersom man ønsker {SickLeavePercentage}% sykemelding og jobber {VacancyRate}% stilling, så utgjør det {SickLeaveHours} timer eller {SickLeaveDays} dag(er) pr. uke.")



