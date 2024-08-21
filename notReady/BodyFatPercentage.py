import streamlit as st
import math

conBmi = st.container(border=True)
conBmi.subheader("Kroppsfettprosent kalkulator")

# Input for kjønn
gender = conBmi.selectbox("Velg kjønn", ["Mann", "Kvinne"])

# Input for målinger
waist = 100
waist = conBmi.number_input("Skriv inn midjemål (cm)", min_value=70, step=1, value=waist )
neck = 35.0
neck = conBmi.number_input("Skriv inn nakkeomkrets (cm)", min_value=15.0, step=0.5, value=neck)
height = 175
height = conBmi.number_input("Skriv inn høyde (cm)", min_value=120, step=1, value=height)

# Tilleggsmåling for kvinner
if gender == "Kvinne":
    hip = 70
    hip = conBmi.number_input("Skriv inn hoftemål (cm)", min_value=40, step=1, value=hip)

# Beregn kroppsfettprosent
if waist > 0 and neck > 0 and height > 0:
    if gender == "Mann":
        body_fat = 86.010 * math.log10(waist - neck) - 70.041 * math.log10(height) + 36.76
    elif gender == "Kvinne" and hip > 0:
        body_fat = 163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(height) - 78.387
    
    conBmi.write(f"Din kroppsfettprosent er {body_fat:.1f}%")
else:
    conBmi.write("Vennligst fyll inn alle målinger.")
