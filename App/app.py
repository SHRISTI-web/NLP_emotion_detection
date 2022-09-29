from secrets import choice
import streamlit as st
import pandas as pd
import numpy as np
import joblib

def main():
    st.title("Emotion Classifier App")
    menu=["Home","Monitor","About"]

    choice=st.sidebar.selectbox("Menu",menu)

    if choice=="Home":
        st.subheader("Home-Emotion In Text")

    elif choice=="Monitor":
        st.subheader("Monitor App")
    else:
        st.subheader("About")       
         