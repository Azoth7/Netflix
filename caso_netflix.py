import streamlit as st
import pandas as pd

st.title("Netflix")
sidebar = st.sidebar


Data_URL="movies.csv"
@st.cache
def load_data(nrows):
    data=pd.read_csv(Data_URL,nrows=nrows)
    return data


data=load_data(500)

if sidebar.checkbox("Show dataframe"):
    st.dataframe(data)

Titulo=sidebar.text_input("Titulo:")
btnTitulo=sidebar.button("Encontrar peli")
if (btnTitulo):
    data_Titulo=data.copy()
    data_Titulo["name"]=data_Titulo["name"].str.lower()
    filterbyrange=data_Titulo[data_Titulo["name"].str.contains(Titulo.lower())]
    count_row=filterbyrange.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyrange)

Director = sidebar.selectbox("Selecciona director:", data['director'].unique())
btnDirector=sidebar.button("Filtrar director")
if (btnDirector):
    filterbyDir=data[data["director"]==Director]
    count_row=filterbyDir.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyDir)