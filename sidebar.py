import streamlit as st
import pandas as pd


with st.sidebar:
    st.title("MedApp")
    st.button("Sykemelding med utgangspunkti i prosent")
    st.link_button("Ta en titt på vg","https://www.vg.no")