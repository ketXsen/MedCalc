import streamlit as st
import pandas as pd    
from datetime import datetime
import re

def validateStrAsTime(str):
    ret = ""

    reg = r"^(?:[01]\d|2[0-3])(?:[0-5]\d)$|^(?:[01]\d|2[0-3])[:.,][0-5]\d$"
    
       
    if bool(re.match(reg, str)):
        str = str[0]+str[1]+":"+str[len(str)-2]+str[len(str)-1]
    else:
        ret = "tiden må være HH:MM"
    st.write(ret)
    return str


if st.button("Hovedmeny - Tilbake til MedCalc menyen."):
    st.switch_page("MedCalc.py")

conRateCounter = st.container(border=True)


conRateCounter.subheader("Teller antall tidstakster:")

RateType = conRateCounter.selectbox("Hvilken type tidstakst:", ("Konsultasjon", "Sykebesøk"))

if RateType == "Konsultasjon":
    minCountFirst = 21
    minCountRest = 15
    infoText1 = "Når startet konsultasjonen?"
    infoText2 = "Når sluttet konsultasjonen?"
    infoText3 = "Konsultasjonen har vart i"
    #conRateCounter.write(f"Første takst etter {minCountFirst} minutter, og så en for hver påbegynte {minCountRest} minutter")
elif RateType == "Sykebesøk":
    minCountFirst = 31
    minCountRest = 15
    infoText1 = "Når dro du?"
    infoText2 = "Når var du tilbake?"
    infoText3 = "Sykebesøket har vart i"
    #conRateCounter.write(f"Første takst etter {minCountFirst} minutter, og så en for hver påbegynte {minCountRest} minutter")
else:
    conRateCounter.write("Ukjent tidstype")



StarttimeS = conRateCounter.text_input(infoText1,"12:00")
StarttimeS = validateStrAsTime(StarttimeS)
EndtimeS = conRateCounter.text_input(infoText2,"12:00")
EndtimeS = validateStrAsTime(EndtimeS)

Starttime = datetime.strptime(StarttimeS, "%H:%M").time()
Endtime = datetime.strptime(EndtimeS, "%H:%M").time()




minWork = ((Endtime.hour*60)+Endtime.minute) -((Starttime.hour*60)+Starttime.minute)

if Endtime < Starttime:
    minWork += (60*24)

conRateCounter.write(f"{infoText3} {minWork} minutter.")

rateCount = 1
minWork -=minCountFirst


while minWork > -1:
    rateCount += 1
    minWork -=minCountRest

rateCount -= 1

conRateCounter.write(f"Du får {rateCount} tidstakst(er). Du mangler {minWork*-1} minutt(er) for å få en til")
