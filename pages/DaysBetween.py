import streamlit as st
import pandas as pd    
from datetime import datetime,timedelta

if st.button("Hovedmeny - Tilbake til MedCalc menyen."):
    st.switch_page("MedCalc.py")
    
conDaysBetween = st.container(border=True)
conDaysBetween.subheader("Beregne antall dager mellom to datoer")

StartDate = conDaysBetween.date_input("Fra dato?",datetime.now())
EndDate = conDaysBetween.date_input("Til og med dato?",datetime.now())
if EndDate < StartDate:
    st.write("Fra dato må være større eller lik slutt dato.")
else:
    days= EndDate-StartDate
    dayCount = days.days 
    conDaysBetween.write(f"Antall dager {dayCount}.") 
