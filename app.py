# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 06:05:21 2021

"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st
import math




pickle_in = open("best_model_latest.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return " welcome all"


def forecast(Future_Scheduled_Jobs,Tech_Count,Max_Temp,month_cos,weekday_sin,quarter_sin):
    
    
    prediction=model.predict(np.array([[Future_Scheduled_Jobs,Tech_Count,Max_Temp,month_cos,weekday_sin,quarter_sin]]))
    print(prediction)
    return prediction


def main():
    st.title("Income Forecast App")
    html_temp = """
    <div style="background-color:green;padding:20px">
    <h2 style="color:white;text-align:center;">Income Forecasting</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Date=st.date_input('Date input')
    Future_Scheduled_Jobs= st.number_input(label="Future_Scheduled_Jobs",format="%f")
    Tech_Count = st.number_input(label="Tech_count",format="%f")
    Max_Temp = st.number_input(label="Max_Temp",format="%f")
    
    

    
    
    
    
    
    
    dates=pd.to_datetime(Date)
    week_day=dates.dayofweek
    month=dates.month
    quater=dates.quarter
    
    month_cos= np.cos(2 * np.pi * (month/12))
    weekday_sin = np.sin(2 * np.pi * (week_day/7))
    quarter_sin = np.sin(2 * np.pi * (quater/4))
    
    

    
    
    
    result=""
    if st.button("Predict"):
        result=forecast(Future_Scheduled_Jobs,Tech_Count,Max_Temp,month_cos,weekday_sin,quarter_sin)
    st.success('The Forecasted Income ${}'.format(result))
    if st.button("About"):
        st.text("datacube.ai")
        st.text(" 2021 ")

if __name__=='__main__':
    main()


