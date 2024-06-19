
import streamlit as st
import numpy as np

#----------------------------------------------------------------------
#Cofiguracion de pagina
st.set_page_config(
    page_title="MI 1RA APP",
    page_icon=":shake:",
    layout="wide",#"centered" or "wide"
    initial_sidebar_state="collapsed",#"auto" or "expanded" or "collapsed"
    
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#BORRAR footer "Made by Streamlit"
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#----------------------------------------------------------------------


#SIDEBAR
st.sidebar.markdown("Creado por ...")
st.sidebar.markdown("[MAJ](#section-1)") #IR A UNA SESTION DEL DOC


#PAGINA PRINCIPAL
st.title('MAJ :dog:')
st.header("[Link](https://www.google.com)")
st.header("MAJ") #IR A UNA SESTION DEL DOC




#CONTENEDOR COLUMNAS


col1, col2, col3 = st.columns(3)



with col1:
   st.header("Tecnologico")
   st.image("img/avatar.png")


with col2:
   st.header("Jugador")
   st.image("img/bungeJumping.jpg")


with col3:
   st.header("Coach")
   st.image("img/majCoach.jpg",width=383)


colA, colB, colC = st.columns([2,3,2])



with colA:
   st.header("Tecnologico")
   st.title('2')
   st.image("img/avatar.png")


with colB:
   st.header("Jugador")
   st.title('3')

   st.image("img/bungeJumping.jpg")


with colC:
   st.header("Coach")
   st.title('2')
   st.image("img/majCoach.jpg",width=330)

#Da formato de CODIGO
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

#Formato matematico
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.header('Esto es "header"')
st.markdown('Esto es "markdown"')
st.caption('''La consola interactiva
La consola interactiva, al igual que Geany, nos
permite escribir código de Python pero sin la
necesidad de guardarlo en un archivo .py. En
cambio, el código se ejecuta instantáneamente
a medida que lo vamos escribiendo.
Para abrir la consola interactiva debemos
ejecutar el programa llamado Python (command
line), o bien presionar las teclas Windows + R y
escribir “python” (sin comillas)''')

st.write('''La consola interactiva
La consola interactiva, al igual que Geany, nos
permite escribir código de Python pero sin la
necesidad de guardarlo en un archivo .py. En
cambio, el código se ejecuta instantáneamente
a medida que lo vamos escribiendo.
Para abrir la consola interactiva debemos
ejecutar el programa llamado Python (command
line), o bien presionar las teclas Windows + R y
escribir “python” (sin comillas)''')

'hola'

'**halo**'

st.markdown("[MAJ](#section-1)") #IR A UNA SESTION DEL DOC


# Boton para accionar Ballons
# st.button('button acciona festejos de globos',st.balloons())
from PIL import Image
imag = Image.open('img/avatar.png')
st.image(imag, caption='MARTIN JAUMA')


#GRAFICO DE BURBUJAS AZUL
import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_bar().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)


# BOX EXPANDER
with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("img/avatar.png")

#KPI
st.title('KPI')

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# #Take FOTO
# picture = st.camera_input("Take a picture")

# if picture:
#     st.image(picture)







