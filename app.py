import streamlit as st
import pandas as pd
import numpy as np
import preprocessor, helper

w_data = pd.read_csv('1. Weather Data.csv')

# load preprocessor.py
w_data = preprocessor.preprocess(w_data)

# sidebar ui
st.sidebar.title('Weather Data Analysis')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', (
        'Unique Wind Speeds', 'Clear Weather', 'Wind Speeds 4 Km per hr', 'Rename', 'Visibility',
        'Standard Deviation', 'Snow', 'Instances', 'Mean Value', 'Min', 'Max', 'Fog', 'Cv40', 'Wcc50'
))

if user_menu == 'Unique Wind Speeds':
    st.subheader('All instances of Unique Wind Speeds')
    uws = helper.UniqueWindSpeeds(w_data)
    st.table(uws)


if user_menu == 'Clear Weather':
    st.subheader('Number of times Clear Weather has occurred')
    wc = helper.WeatherClear(w_data)
    st.table(wc)

if user_menu == 'Wind Speeds 4 Km per hr':
    st.subheader('Wind Speeds exactly 4 Km per hr')
    ws = helper.WindSpeed4Kmperhr(w_data)
    st.table(ws)

if user_menu == 'Rename':
    st.subheader('Rename column "Weather" to "Weather Condition"')
    r = helper.rename(w_data)
    st.table(r)

if user_menu == 'Visibility':
    st.subheader('Mean of the Visibility Column')
    visibility = helper.Visibility(w_data)
    st.table(visibility)

if user_menu == 'Standard Deviation':
    st.subheader('Standard Deviation of Pressure Column')
    std = helper.StandardDeviation(w_data)
    st.table(std)

if user_menu == 'Variance':
    st.subheader('Variance of Relative Humidity Column')
    var = helper.Variance(w_data)
    st.table(var)

if user_menu == 'Snow':
    st.subheader('All instances when snow was recorded')
    sn = helper.Snow(w_data)
    st.table(sn)

if user_menu == 'Instances':
    st.subheader('All instances When Wind Speed is above 24 and Visibility is 25')
    ii = helper.Instances(w_data)
    st.table(ii)

if user_menu == 'Mean Value':
    st.subheader('All instances of the mean value of each column against each Weather condition"')
    mv = helper.MeanValue(w_data)
    st.table(mv)

if user_menu == 'Min':
    st.subheader('All instances of the Minimum value of each column against each Weather Condition')
    min = helper.Min(w_data)
    st.table(min)

if user_menu == 'Max':
    st.subheader('All instances of the Maximum value of each column against the Weather Condition')
    max = helper.Max(w_data)
    max = st.table(max)

if user_menu == 'Fog':
    st.subheader('All Records where Weather Condition is Fog')
    fog = helper.Fog(w_data)
    st.table(fog)

if user_menu == 'Cv40':
    st.subheader('All instances when Weather Condition is clear or visibility is above 40')
    cv40 = helper.Cv(w_data)
    st.table(cv40)

if user_menu == 'Wcc50':
    st.subheader('All instances when Weather Condition is clear and relative humidity > 5 or visibility > 40')
    wcc = helper.Wcc(w_data)
    st.table(wcc)