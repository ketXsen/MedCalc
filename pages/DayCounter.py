import streamlit as st
import pandas as pd    
from datetime import datetime,timedelta

if st.button("Hovedmeny - Tilbake til MedCalc menyen."):
    st.switch_page("MedCalc.py")
    
conDayCounter = st.container(border=True)
conDayCounter.subheader("Beregne antall dager til neste resept")

StartDate = conDayCounter.date_input("Fra og med hvilken dato?",datetime.now())

dayCount = 28
dayCount= conDayCounter.number_input("Hvor mange dager har du skrevet ut for?",dayCount)

EndDate = StartDate + timedelta(days=dayCount)


StartDateF = StartDate.strftime("%d. %b %y")
EndDateF = EndDate.strftime("%d. %b %y")

conDayCounter.write(f"Neste resept tidligst {EndDateF.lower()}.") 