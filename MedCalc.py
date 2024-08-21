import streamlit as st
import pandas as pd

#st.set_page_config(layout="wide")


st.subheader("Velg i menyen")


if st.button("Beregne sykemeldingsgrad hos deltidsansatt"):
    st.switch_page("pages/SickByDaysAndPercent.py")
if st.button("Beregne antall tidstakster"):
    st.switch_page("pages/RateCounter.py")
if st.button("Beregne antall dager til neste resept"):
    st.switch_page("pages/DayCounter.py")    
if st.button("Beregne antall dager mellom to datoer"):
    st.switch_page("pages/DaysBetween.py")    



# col1, col2 = st.columns((1,1))


# with col1:
    
#     st.write(f"")
    

# with col2:

#     st.write(f"")

