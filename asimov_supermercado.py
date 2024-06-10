import streamlit as st
import pandas as pd
#import plotly.express as px

st.set_page_config(layout="wide")

# Com uma visão mensal
#faturamento por unidade… 
# tipo de produto mais vendido, contribuição por filial,
#Desempenho das forma de pagamento…
#Como estão as avaliações das filiais?



df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df

