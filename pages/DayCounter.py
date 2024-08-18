import streamlit as st
import pandas as pd    
from datetime import datetime,timedelta

StartDate = st.date_input("Fra og med hvilken dato?",datetime.now())

dayCount = 0
dayCount= st.number_input("Hvor mange dager frem i tid?",dayCount)

EndDate = StartDate + timedelta(days=dayCount)


StartDateF = StartDate.strftime("%d. %b %y")
EndDateF = EndDate.strftime("%d. %b %y")

st.write(f"{dayCount} dager fra {StartDateF} blir {EndDateF}.") 