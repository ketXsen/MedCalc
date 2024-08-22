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
res = f"Din BMI er {bmi:.1f}"+"\n\r"
if bmi < 16:
    bmiLowLevel = 0
    bmiHighLevel = 16-0.0000001
    desc = "Svært undervektig."
elif bmi <= 18.5:
    bmiLowLevel = 16
    bmiHighLevel = 18.5
    desc = "Undervektig"
elif bmi <= 25:
    bmiLowLevel = 18.5+0.000001
    bmiHighLevel = 25-0.0000001
    desc = "Sunn og normal vekt"
elif bmi <= 30:
    bmiLowLevel = 25+0.000001
    bmiHighLevel = 30-0.0000001
    desc = "Overvekt"
elif bmi <= 35:
    bmiLowLevel = 30+0.000001
    bmiHighLevel = 35-0.0000001
    desc = "Moderat fedme"
elif bmi <= 40:
    bmiLowLevel = 35+0.000001
    bmiHighLevel = 40-0.0000001    
    desc = "Alvorlig fedme"
else:
    bmiLowLevel = 40+0.000001
    bmiHighLevel = 1000   
    desc = "Svært alvorlig fedme"

low = round(bmiLowLevel *((Høyde/100) ** 2),1)
high = round(bmiHighLevel *((Høyde/100) ** 2),1)
res += f"{desc} ( {low} kg - {high} kg)"


conPerson.write(res)


