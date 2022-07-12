import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_vis

st.set_page_config(page_title='Data Visulaization',initial_sidebar_state='expanded')
st.title('Welcome to Our App for Data Overviwe')
#https://i.gifer.com/9lZ7.gif
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.gifer.com/4NB4.gif");
             background-size: cover    
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

#upload the dataset and display it
up_file = st.file_uploader('Please,Uploud Your Dataset')
if up_file != None:
    df = pd.read_csv(up_file)
    my_bar = st.progress(0)
    st.write(df)
    
    for percent_complete in range(100):
     time.sleep(0.01)
     my_bar.progress(percent_complete + 1)
    
    #Dispaly the dataset descripation
    st.markdown("___")
    st.markdown("# Discrip the data")
    st.write(data_vis.data_des(df))
    st.markdown("___")

    #Display the dataset columns type
    st.markdown("# Types of data")
    st.write(data_vis.data_types(df))
    st.markdown("___")

    # Nulls Check
    #st.markdown('for Nulls Checking click on the bleow markdown')
    
    st.markdown('# Nulls Check')
    st.write('The count for Nulls in the data is : ',data_vis.check_nulls(df))
    st.markdown("___")

    #Deplacit check
    st.markdown('# Daplacit Check')
    st.write("The count of daplicated values in the data is :",data_vis.check_duplicat(df))
    st.markdown("___")
    
    #Display the dataset overviwe
    st.markdown("# Overviwe of data")
    st.write(data_vis.overviwe(df))
    st.markdown("___")

    #Display the histogram
    st.markdown("# Plot Histogram")
    cols = st.selectbox('Select Column to Plot the Histogram',df.columns)
    st.write(data_vis.plot_hist(df,cols))
    st.markdown("___")

    #Plot corr data
    st.markdown('# Plot Corrolitaion')
    st.write(data_vis.corr_data(df))
    st.markdown("___")

    #Plot the interacations between columns
    st.markdown("# Plot the Interactions")
    col_1 = st.selectbox('Select Frist Column',df.columns)
    col_2 = st.selectbox('Select Second Column',df.columns)
    st.write(data_vis.plotting(df[col_1],df[col_2]))
    st.markdown("___")