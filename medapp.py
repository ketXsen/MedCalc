import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")



st.write("Velg i menyen")
if st.button("SickByDays - Du velger antall dager personen er syk, og får ut sykemeldingsprosenten."):
    st.switch_page("pages/SickByDays.py")
if st.button("SickByPercent - Du velger sykemeldingsprosenten, og får antall dager personen er syk."):
    st.switch_page("pages/SickByPercent.py")
if st.button("RateCounter - Du kan beregne antall tidstakster."):
    st.switch_page("pages/RateCounter.py")


col1, col2 = st.columns((1,1))


with col1:
    
    st.write(f"")
    

with col2:

    st.write(f"")

