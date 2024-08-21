import streamlit as st
import pandas as pd    
from datetime import datetime,timedelta



if st.button("Hovedmeny - Tilbake til MedCalc menyen."):
    st.switch_page("MedCalc.py")
    
conPerson = st.container(border=True)
conPerson.subheader("Beregne BMI")

Høyde = 150
Høyde = conPerson.number_input("Høyde i cm:",50,220,Høyde)

Vekt = 80
Vekt = conPerson.number_input("Vekt i KG:",30,300,Vekt)

bmi = ( Vekt / ((Høyde/100) ** 2))
res = f"Din BMI er {bmi:.1f}. "
if bmi < 16:
    res += "Svært undervektig"
elif bmi <= 18.5:
    res += "Undervektig"
elif bmi <= 25:
    res += "Sunn og normal vekt"
elif bmi <= 30:
    res += "Overvekt"
elif bmi <= 35:
    res += "Moderat fedme"
elif bmi <= 40:
    res += "Alvorlig fedme"
else:
    res += "Svært alvorlig fedme"

conPerson.write(res)


