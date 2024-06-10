import streamlit as st
import pandas as pd
#import plotly.express as px

# Com uma visão mensal
#faturamento por unidade… 
# tipo de produto mais vendido, contribuição por filial,
#Desempenho das forma de pagamento…
#Como estão as avaliações das filiais?



df = pd.read_csv("../spermarket sales/supermarket_sales.csv", sep=";", decimal=",")
df

