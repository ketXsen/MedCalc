import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


st.subheader("Velg i menyen")


if st.button("SickByDaysAndPercent - Du velger antall dager personen er syk og får ut sykemeldingsprosenten, eller omvendt."):
    st.switch_page("pages/SickByDaysAndPercent.py")
if st.button("RateCounter - Du kan beregne antall tidstakster."):
    st.switch_page("pages/RateCounter.py")
if st.button("DayCounter - Legger til x antall dager og gir en ny dato."):
    st.switch_page("pages/DayCounter.py")    


col1, col2 = st.columns((1,1))


with col1:
    
    st.write(f"")
    

with col2:

    st.write(f"")

