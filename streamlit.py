# mi_app.py

import streamlit as st
from turtle import color
import altair as alt
import numpy as np
import pandas as pd
import datetime
import time as time
from PIL import Image
from streamlit_option_menu import option_menu

def main():
    st.title("Mi Aplicación de Streamlit")
    st.write("¡Bienvenido a mi aplicación!")

    st.write("Este es un texto")

    df1 =  pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a', 'b', 'c']
    )

st.write(pd.DataFrame({
    'Coluna A': [1, 2,3,4,5],
    'Coluna B': ["Cachorro", "Gato", "Cavalo","Vaca","Zebra"],
}))

st.markdown(':fireworks:')

# title
st.title('Texto com maior destaque - Título')

# header
st.header('Texto com pouco destaque - Cabeçalho')

# subheader
st.subheader("Texto com pouco destaque - subcabeçalho")

# markdown
"Texto sem nenhuma função"
st.write('Este é um *write*')
st.markdown('Este é um *markdown*')

# caption
st.caption('Texto com fonte pequena usado para descrições e outros detalhamentos')

# code
code = '''if(hungry > 0):
    return "go to refrigerator"
else:
    return "study Streamlit"'''
st.code(code, language='python')

# text
st.text('Texto usando st.text')

# Latex https://katex.org/docs/supported.html
st.latex('\int x²+y²+32ab \isin x²+y²+z²')

#Dataframe
st.header('DATAFRAME')
"Gerando um dataframe aleatório 5x5"
df = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %d' % i for i in range(5)))

st.subheader("Exemplo 1 - imprimindo o Dataframe")
st.dataframe(df)

st.subheader("Exemplo 2 - Alterando as dimensões")
st.dataframe(df, 300, 200)


st.subheader("Exemplo 3 - Dando um destaque nos maiores valores")
st.dataframe(df.style.highlight_max(axis=1)) ### maiores valores =0 colunas e =1 filas


st.header('TABLE - Similar ao Dataframe, mas o conteúdo de TABLE é estático')
st.subheader("Exemplo 4 - Imprimindo os dados com Table")
st.table(df)

st.header('METRIC - Similar ao Dataframe, mas o conteúdo de TABLE é estático')
st.subheader('Exemplo 5 - Temperatura')
st.metric(label="Temperatura", value="22 °C", delta="1 °C")

st.subheader('Exemplo 6 - Exemplo com 3 colunas')
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "25 °C", "2 °C")
col2.metric("Vento", "10 Km/h", "-8%")
col3.metric("Humidade", "86%", "4%")

st.subheader('Exemplo 7 - alterando cor do delta')
st.metric(label="Gas price", value=4, delta=-0.5,
     delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
     delta_color="off")

st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })

meuObjeto = {
    'banana': 'amarela',
    'limão': 'verde',
    'laranja': 'laranja'
 }

st.json(meuObjeto)

fonte = pd.DataFrame({
    'a': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

st.subheader('Esse é o nosso dataset de exemplo')
fonte

graf_barras = alt.Chart(fonte).mark_bar().encode(
    x='a',
    y='b',
    color='a',
    tooltip=['a','b']
)
rotulo_barra = graf_barras.mark_text(
    dy= -8,
    size=17
).encode(
    text='b',    
)

st.subheader('Plot do gráfico de barras :)')
st.altair_chart(graf_barras+rotulo_barra, use_container_width=True)

df = fonte

graf_barras_novo = alt.Chart(df).mark_bar(
    cornerRadiusTopLeft=10,
    cornerRadiusTopRight=10
).encode(
    x = alt.X('a', sort='y'),
    y = 'b',
    color = alt.condition(
        alt.datum.b >43,
        alt.value('steelblue'),
        alt.value('black')
    )
)
rotulo = graf_barras_novo.mark_text(
    align = 'center',
    baseline = 'middle',
    size = 14,
    dy = 10
).encode(text='b')

linea_media = alt.Chart(df).mark_rule(color='red').encode(
    y='mean(b)'
)

st.altair_chart(graf_barras_novo+rotulo+linea_media, use_container_width=True)



graf_area = alt.Chart(fonte).mark_area(
    color='lightblue',
    interpolate='step-after',
    line=True    
).encode(
    x='a',
    y='b',
    tooltip=['a','b']
)
rotulo_area = graf_area.mark_text(
    dy= -8,
    dx=30,
    size=17
).encode(
    text='b',    
)

st.subheader('Gráfico de Área')
st.altair_chart(graf_area+rotulo_area, use_container_width=True)

graf_pizza = alt.Chart(fonte).mark_arc().encode(
    theta=alt.Theta(field='b', type='quantitative'),
    color = alt.Color(field='a', type='nominal'),
)

st.subheader('Exemplo de gráfico de pizza')
st.altair_chart(graf_pizza)


#Grafico de Lineas


Vendas = pd.DataFrame({
    'Month': ['01-Jan', '02-Feb', '03-Mar', '04-Apr', '05-May', '06-Jun',
     '07-Jul','08-Ago', '09-Set', '10-Oct', '11-Nov', '12-Dec'],
    'product_A': [28, 55, 43, 91, 81, 53, 19, 87, 52, 85, 101, 77],
    'product_B': [ 93, 68, 79, 84, 81, 97, 109, 99, 125, 115, 120, 88]

})

st.subheader('GRÁFICO DE LINHAS: PRODUTO A & B')

graf_linha_A = alt.Chart(Vendas).mark_line(
    point=alt.OverlayMarkDef(color='red',size=100, filled=False, fill='black'),
    color='red'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_A',
    axis=alt.Axis(grid=False),
    scale=alt.Scale(domain=(0,160))),
    tooltip = ['Month', 'product_A', 'product_B']
).properties(
    width=600,
    height=600,
    title = 'VENDAS MENSAIS DOS PRODUTOS A & B'
)

graf_linha_B = alt.Chart(Vendas).mark_line(
    point=alt.OverlayMarkDef(color='green',size=100, filled=False, fill='black'),
    color='green'
).encode(
    x = alt.X('Month'),
    y = alt.Y('product_B'),
    tooltip = ['Month', 'product_A', 'product_B']
)

rotulo_A = graf_linha_A.mark_text(
    dy = -15,
    size=14
).encode(
    text = 'product_A',
    color = alt.value('white')
)

rotulo_B = graf_linha_B.mark_text(
    dy = -15,
    size=14
).encode(
    text = 'product_B',
    color = alt.value('white')
)

st.altair_chart(graf_linha_A+graf_linha_B+rotulo_A+rotulo_B)

#Grafico de area 

df = pd.read_excel(
    io = './Datasets/faturamento.xlsx',
    engine='openpyxl',
    sheet_name='flow',
    usecols='A:B',
    nrows=15,
)

graf_area = alt.Chart(df).mark_area(
    #line={'color':'black'},
    color='gray'
).encode(
    x = 'Year:T',
    y = 'Value:Q'
)

rotulo = graf_area.mark_text(
    align='center',
    baseline='middle',
    color='white',    
    size=14,
    dy=-18
).encode(text='Value')

st.subheader('VALORES ANUAIS')
st.altair_chart(graf_area+rotulo, use_container_width=True)


#Grafico de pizza

df2 = pd.read_excel(
    io = './Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name = 'ricos',
    usecols = 'A:B',
    nrows = 9
)

st.subheader('Grafico de pizza- Mas ricos del mundo')

graf_pizza = alt.Chart(df2).mark_arc(
    innerRadius=0,
    outerRadius=150
).encode(
    theta = alt.Theta(field='Fortuna', type='quantitative', stack=True),
    color=alt.Color(
        field='Nome', 
        type='nominal',
        # legend=None
    ),
    tooltip = ['Nome', 'Fortuna']
).properties(width=700, height=450)

rotuloNome = graf_pizza.mark_text(radius=200, size=14).encode(text='Nome')
rotuloValor = graf_pizza.mark_text(radius=165, size=14).encode(text='Fortuna')
st.altair_chart(graf_pizza+rotuloNome+rotuloValor)

#Grafico de dispersion

source = pd.read_csv('./Datasets/vega_car.csv')

points = alt.Chart(source).mark_point().encode(
    x='Horsepower:Q',
    y='Miles_per_Gallon:Q',
    color=alt.Color('Origin:N')   
)
st.subheader('Grafico de dispersion')
st.altair_chart(points, use_container_width=True)

# Histograma

df3 = pd.read_excel(
    io = './Datasets/normal_dist.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:C',
    nrows=87,
)
Histograma = alt.Chart(df3).mark_bar().encode(
    x = alt.X('x', bin=alt.Bin(step=5)),
    y='sum(count)'
)
st.subheader('HISTOGRAMA - NOTAS DE 1000 ALUNOS')
st.altair_chart(Histograma,use_container_width=True)

#Widgets
df4 = pd.read_excel(
    io = './Datasets/faturamento.xlsx',
    engine = 'openpyxl',
    sheet_name = 'Interação',
    usecols = 'A:B',
    nrows = 40
)

st.subheader('Botão')
if st.button("Cliquei aqui"):
    st.write('Você me clicou')

def convert_df(df):
    return df.to_csv().encode('utf-8')
st.subheader('Botão de Download')
st.download_button(
    label="Baixar dados *.csv",
    data=convert_df(df),
    file_name='df.csv',
    mime='text/csv'    
)

st.subheader('Checkbox')
select = st.checkbox('Marque a caixa')
if select ==True:
    st.write('Fui selecionado')

st.subheader('Radio Button')
tipoRelatorio = st.radio(
    "Selecione el tipo de relatorio",
    ('Mensual', 'Semanal', 'Anual')
)
st.write('Usted selecciono el tipo:', tipoRelatorio)
    
st.subheader('Caixa de Seleccion')
Opciones = st.selectbox(
    "Selecione la materia prima para analizar:",
    ('Acero', 'Plastico', 'Caucho' )
)
st.write('Usted selecciono: ', Opciones)


st.subheader('Seleccion multiple')
multi = st.multiselect(
    "Selecione el banco de interes: ",
    ['Bradesco','Itau', 'Caixa', 'BB', 'Santander']
)
st.write(multi)

st.subheader('Sliders')
parcelas = st.slider(
    'Con cuantas parcelas quieres simular?:', 0, 60, 30)
st.write('Usted seleciono:', parcelas, 'Parcelas')

intervalo = st.slider(
    "Cual es el intervalo deseado?",
    0.0, 100.0, (25.0, 75.0)
)
st.write('Intervalo:', intervalo)


st.subheader('Datas')

d = st.date_input(
    'Selecione la data:',
    datetime.date(2022,10,1)
    )

st.write('La data selecionada fue',d)


#Imagem
cachorrinho = Image.open('./Mídia/dog.jpg')
st.subheader('1-Inserindo uma imagem')
st.image(cachorrinho, caption='Um cachorro desconfiado')

#Audio
meu_audio = open('./Mídia/Scratching The Surface.mp3','rb')
abrir_audio = meu_audio.read()
st.subheader('2-Arquivos de Áudio')
st.audio(abrir_audio, format='audio/mp3')

#Vídeo
arquivo_video = open('./Mídia/Buildings.mp4', 'rb')
abrir_video = arquivo_video.read()
st.subheader('3-Inserir um Vídeo')
st.video(abrir_video)


#Sidebar
varModal = st.sidebar.selectbox(
    "Seleccione la modal de transporte:",
    ("Terminal", "Maritimo", "Aereo", "Tren", "Otro")
)

st.write("La modal seleccionada fue:", varModal)

with st.sidebar:
    varCliente = st.radio(
        "Seleccione el cliente:",
        ("Espacio X", "Microsoft", "Apple", 'Google', "Amazon")
    )

    varBanco = st.multiselect(
        "Seleccione el bancop:",
        ["BrADESCO", "Itaú", "BB"]
    )

    varParcela = st.slider(
        "Cuántas parcelas desea financiar?", 0, 60, 20
    )

    varData = st.date_input(
        "Seleccione la data de vencimiento:",
        datetime.date(2021,1,1)
    )

    with st.spinner("Cargando la selección..."):
         time.sleep(2)
    st.success("Listo!")
                    

st.write("Cliente:", varCliente)
st.write("Banco:", varBanco)
st.write("Parcelas:", varParcela)
st.write("Data:", varData)


#Colunas

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Coluna 1")
    st.image('./Mídia/cat.jpg')

with col2:
    st.subheader("Coluna 2")
    st.image('./Mídia/dog.jpg')

with col3:
    st.subheader("Coluna 3")
    st.image('./Mídia/owl.jpg')

with col4:
    st.subheader("Coluna 4")
    st.image('./Mídia/dog_2.jpg')


col_1, col_2  =st.columns([3,1])
data = np.random.rand(100,1)

col_1.line_chart(data)
col_2.write(data)

#Expander
st.header('Expander')
st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("Ver detalles"):
    st.write('''
             Este es un ejemplo de expander ''')
    st.image("./Mídia/dice.jpg")

#Menus laterales

with st.sidebar:
    selected = option_menu(
        menu_title = "Menu principal",
        options = ["Inicio", "Ventas", "Relatorios", "Dashboards"],
        icons = ["house", "basket", "bandaid", "bar-chart"]
    )



if __name__ == "__main__":
    main()
