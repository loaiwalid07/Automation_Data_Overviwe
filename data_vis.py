# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 06:02:26 2022

@author: loain
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,mean_absolute_error
from sklearn.svm import SVC


path = 'C:/Users/loain/OneDrive/Desktop/data_vis_proj/Stores.csv'

def read_data(path):
    df = pd.read_csv(path)
    return df

def check_nulls (df):
    return df.isnull().values.any() , df.isnull().any().sum()

def check_duplicat(df):
    return df.duplicated().sum()

def corr_data(df):
    df_coor = df.corr()
    return df_coor.style.background_gradient(cmap='coolwarm')

def plotting (x,y):
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelrotation = 45)
    ax.scatter(x,y)
    return fig

def data_des(df):
    return df.describe()

def data_types (df):
    return pd.DataFrame(data=dict(df.dtypes),index=['Type']).astype(str).T

def plot_hist (df,col):
    fig, ax = plt.subplots()
    ax.tick_params(axis='x', labelrotation = 45)
    ax.hist(df[col],bins=50)
    return fig
def overviwe (df):
    count_uin = []

    for i in range(0,len(df.columns)):
        count_uin.append(len(df.iloc[:,i].unique()))
    
    count_0 = (df == 0).sum()
    
    count_neg=(df < 0).sum()
    
    count_inf = np.isinf(df).sum()
    
    dff = pd.DataFrame(data = [count_uin,list(dict(count_0).values()),
    list(dict(count_neg).values()),list(dict(count_inf).values())]
    ,index=['Distinc','zeros','Negitives','Infinty'],
    columns=df.columns
    )
    return dff.T