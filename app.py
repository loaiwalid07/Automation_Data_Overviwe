import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import data_vis
import re
import plotly.express as px
import webbrowser

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

footer:after{
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

def card (header,value):
    return f"""
                <div class="card text-white bg-dark mb-3" style="max-width: 38rem;">
                <div class="card-header">{header}</div>
                <div class="card-body">
                    <p  class="card-text">{value}</p>
                </div>
                </div>
                """

#upload the dataset and display it
up_file = st.file_uploader('Please,Uploud Your Dataset')
if up_file != None:
    
# Read the dataset
    df = pd.read_csv(up_file)
    st.write(df)
    st.markdown("___")

# Display the dataset columns type
    st.markdown("# Types of data")
    st.write(data_vis.data_types(df))
    st.markdown("___")

#print the cat columns
    st.markdown(f"This columns are categorical data : {str(set(df.columns)-set(df._get_numeric_data().columns))}",unsafe_allow_html =  True)
    st.markdown("___")

# Data overveiw
    st.markdown("# Data Overveiw")
    dfff = data_vis.over_all(df)
    for i in dfff.columns:
        st.markdown(card(i,str(re.sub(r'(      )',"  ->  ",str(re.sub(r'(\n)'," <br> ",str(dfff[i])))))),unsafe_allow_html=True)
    st.markdown("___")

# Nulls Check
    #st.markdown('for Nulls Checking click on the bleow markdown')
    st.markdown('# Nulls Check')
    st.write(card("Nulls",str(re.sub(r'(      )',"  ->  ",str(re.sub(r'(\n)'," <br> ",str(data_vis.check_nulls(df))))))),unsafe_allow_html=True)
    #st.write('The count for Nulls in the data is : ',data_vis.check_nulls(df),unsafe_allow_html=True)
    st.markdown("___")

# Deplacit check
    st.markdown('# Daplacit Check')
    st.write(card("Daplacit Check",data_vis.check_duplicat(df)),unsafe_allow_html=True)
    #st.write("The count of daplicated values in the data is :",data_vis.check_duplicat(df))
    st.markdown("___")

# Plot corr data
    st.markdown('# Plot Corrolitaion')
    st.write(data_vis.corr_data(df))
    st.markdown("___")

# Plot the interacations between columns
    st.markdown("# Plot the Interactions")
    col_1 = st.selectbox('Select Frist Column',df.columns)
    col_2 = st.selectbox('Select Second Column',df.columns)
    st.write(data_vis.plotting(df[col_1],df[col_2]))
    st.markdown("___")

# Display the histogram
    st.markdown("# Plot Histogram")
    cols = st.selectbox('Select Column to Plot the Histogram',df.columns)
    st.write(data_vis.plot_hist(df,cols))
    st.markdown("___")

# Check list
    st.sidebar.header("Select the parts of code you want to display")
    ch_1 = st.sidebar.checkbox('Code For Types of data')
    ch_2 = st.sidebar.checkbox('Code For Data overveiw')
    ch_3 = st.sidebar.checkbox('Code For Nulls Check')
    ch_4 = st.sidebar.checkbox('Code For Daplacit Check')
    ch_5 = st.sidebar.checkbox('Code For Plot Corrolitaion')
    ch_6 = st.sidebar.checkbox('Code For Plot the interacations between columns')
    ch_7 = st.sidebar.checkbox('Code For histogram')

    st.sidebar.markdown('___')
    st.sidebar.markdown('*You can find the parts of code in the bottom of th page*')    
    code_1 = '''
    def data_types (df):
        return pd.DataFrame(data=dict(df.dtypes),index=['Type']).astype(str)
    '''
    code_2 = '''
    
    def data_des(df):
        return df.describe()

    def overviwe (df):
        df = df._get_numeric_data()
        count_uin = []

        for i in range(0,len(df.columns)):
            count_uin.append(len(df.iloc[:,i].unique()))
        
        count_0 = (df == 0).sum()
        
        count_neg=(df < 0).sum()
        
        count_inf = np.isinf(df).sum()
        
        dff = pd.DataFrame(data = [count_uin,list(dict(count_0).values()),
        list(dict(count_neg).values()),list(dict(count_inf).values())
                                ]
        ,index=['Distinc','zeros','Negitives','Infinty'
            ],
        columns=df.columns
        )
        return dff

    def over_all (df):
        df = df._get_numeric_data()
        df_des = data_des(df)
        df_over = overviwe(df)
        df_over = df_des.append(df_over)
        return df_over
    '''
    code_3 = '''
    def check_nulls (df):
        return df.isnull().sum()
    '''
    code_4 = '''
    def check_duplicat(df):
        return df.duplicated().sum()
    '''
    code_5 = '''
    def corr_data(df):
        df_coor = df.corr()
        return df_coor.style.background_gradient(cmap='coolwarm')
    '''
    code_6 = '''
    def plotting (x,y):
        fig = px.scatter(x=x,y=y)
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor= 'rgba(0, 0, 0, 0)')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        return fig
    '''
    code_7 = '''
    def plot_hist (df,col):
        fig_1 = px.histogram(df, x = col)
        #fig_1.update_layout(bargap=0.5)
        fig_1.update_layout(plot_bgcolor='rgba(0,0,0,0)',paper_bgcolor= 'rgba(0, 0, 0, 0)')
        fig_1.update_xaxes(showgrid=False)
        fig_1.update_yaxes(showgrid=False)
        return fig_1
    '''

    if ch_1 :
        st.code(code_1)
    if ch_2:
        st.code(code_2)
    if ch_3:
        st.code(code_3)
    if ch_4:
        st.code(code_4)
    if ch_5:
        st.code(code_5)
    if ch_6:
        st.code(code_6)
    if ch_7:
        st.code(code_7)
