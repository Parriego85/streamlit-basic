import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="El bien y el mal",
    page_icon="☯",
    layout="wide",
)

st.title('My APP-HOME')

option = st.sidebar.selectbox(
    'Selecciona la vista',
    ('Home', 'Visualizaciones', 'Map'))

st.sidebar.write(option)


datos = pd.read_csv('data/red_recarga_acceso_publico_2021.csv', sep=";") #Carga de datos por un archivo csv

uploaded_file = st.sidebar.file_uploader("Choose a csv", type=["csv"])
if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)


if option == "Home":
    
    with st.expander("Detalles de la explicación - Haz clic para expandir"):
        st.write("""
            Esto es una explicacion blabla 
            1
            2
            3
            """)
        st.image("https://img.freepik.com/premium-photo/yinyang-symbol-good-evil-black-background_124507-33879.jpg?w=900", caption='YNG-YANG')

    
        with st.echo():
            st.write(datos)

        with st.echo():
            #Código para generar numeros pares
            lista = list(range(10))
            even_list= [x for x in lista if x%2==0]
            st.write(even_list)
elif option == "Map":
    datos_pal_mapa = datos[["latidtud", "longitud"]]
    datos_pal_mapa.columns = ["lat", "lon"]
    st.map(datos_pal_mapa, zoom=11)

elif option == "Visualizaciones":
    datos_pal_barchar = datos.groupby("DISTRITO")[["Nº CARGADORES"]].sum().reset_index()
    # puedes usar st.plotly`
    st.bar_chart(datos_pal_barchar,x= "DISTRITO", y= "Nº CARGADORES")












