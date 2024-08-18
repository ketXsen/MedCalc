import streamlit as st
import pandas as pd    
from datetime import datetime

def validateStrAsTime(str):
    ret = ""
    if len(str) < 5 or len(str) > 5:
        ret = "tiden må være HH:MM"
    st.write(ret)



StarttimeS = st.text_input("Når startet du?","12:00")
validateStrAsTime(StarttimeS)
EndtimeS = st.text_input("Når var du ferdig?","12:00")
validateStrAsTime(EndtimeS)

Starttime = datetime.strptime(StarttimeS, "%H:%M").time()
Endtime = datetime.strptime(EndtimeS, "%H:%M").time()


minCountFirst = 20
minCountRest = 15


minWork = ((Endtime.hour*60)+Endtime.minute) -((Starttime.hour*60)+Starttime.minute)

if Endtime < Starttime:
    minWork += (60*24)

st.write(f"Du har jobbet i {minWork} minutter.")

rateCount = 1
minWork -=minCountFirst


while minWork > -1:
    rateCount += 1
    minWork -=minCountRest

rateCount -= 1

st.write(f"Du får {rateCount} tidstakst(er). Du mangler {minWork*-1} minutt(er) for å få en til")
