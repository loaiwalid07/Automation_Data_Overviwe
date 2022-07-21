import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_vis
import re

hide_menu ="""
<style>
#MainMenu{
    visibility : hidden;
 }
header{
    visibility : hidden;
 }
.css-z3au9t{
    visibility : hidden;
    content:'';
}
viewerBadge_link__1S137{
    visibility : hidden;
}
footer{
    visibility : hidden;
    content: 'Loai Nazeer';

.navbar-brand{
        display:inline;
        font-size: 30px;
}

}
<style>  
"""

st.set_page_config(page_title='Data Overview',initial_sidebar_state="auto")

#Set the Navbar for the app
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-dark bg-dark">
  <a class="navbar-brand" href="#">
    <img src="https://cdn-icons-png.flaticon.com/512/190/190759.png" width="60" height="60" class="d-inline-block align-center" " alt="">
    Data Overveiw
  </a>
</nav>
""", unsafe_allow_html=True)

st.markdown(hide_menu,unsafe_allow_html=True)

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
             background: url("https://i.pinimg.com/originals/da/1e/0c/da1e0c3e41db28cefe8f12d9b1fac46a.jpg");
             background-size: cover    
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()

st.title('Welcome to Our App for Data Overveiw')

def card (header,value,title=''):
    return f"""
                <div class="card text-white bg-dark mb-3" style="max-width: 38rem;">
                <div class="card-header">{header}</div>
                <div class="card-body">
                    <h6 class="card-title">{title}</h6>
                    <p  class="card-text">{value}</p>
                </div>
                </div>
                """

#upload the dataset and display it
up_file = st.file_uploader('Please,Uploud Your Dataset')
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)

if up_file != None:
    
# Read the dataset
    st.markdown("___")
    df = pd.read_csv(up_file)
    st.write(df)
    st.markdown("___")


#Display the dataset columns type
    st.markdown("# Types of data")
    st.write(data_vis.data_types(df))
    st.markdown("___")

#Data overveiw
    st.markdown("# Data Overveiw")
    dfff = data_vis.over_all(df)
    for i in dfff.columns:
        st.markdown(card(i,str(re.sub(r'(      )',"  ->  ",str(re.sub(r'(\n)'," <br> ",str(dfff[i])))))),unsafe_allow_html=True)
    st.markdown("___")

# Nulls Check
    #st.markdown('for Nulls Checking click on the bleow markdown')
    st.markdown('# Nulls Check')
    st.write(card("Nulls",str(re.sub(r'(      )',"  ->  ",str(re.sub(r'(\n)'," <br> ",str(data_vis.check_nulls(df)))))),'count of nulls : '),unsafe_allow_html=True)
    #st.write('The count for Nulls in the data is : ',data_vis.check_nulls(df),unsafe_allow_html=True)
    st.markdown("___")

#Deplacit check
    st.markdown('# Daplacit Check')
    st.write(card("Daplacit Check",data_vis.check_duplicat(df),"The count of daplicated values in the data is :"),unsafe_allow_html=True)
    #st.write("The count of daplicated values in the data is :",data_vis.check_duplicat(df))
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

#Display the histogram
    st.markdown("# Plot Histogram")
    cols = st.selectbox('Select Column to Plot the Histogram',df.columns)
    st.write(data_vis.plot_hist(df,cols))
    st.markdown("___")



    




 
