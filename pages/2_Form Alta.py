import streamlit as st
import json
import os
import uuid
from datetime import datetime


# Funciones -------------------------------------------------------

# Función para generar un ID único para cada registro
def generar_id():
    return str(uuid.uuid4())

# ----------------------------------------------------------


st.title("FORMULARIO DE ALTA")
    
with st.form(key='miForm', clear_on_submit=True):
        apellido= st.text_input("Apellido")
        nombre= st.text_input("Nombre")
        submit_button = st.form_submit_button("ALTA")
    
 
# Botón de envío
if submit_button:
    if apellido and nombre:
          # Generar un ID único
        id_unico = generar_id()
        
        # Obtener la fecha y hora actuales
        fecha_alta = datetime.now().strftime("%Y%m%d%H:%M")
        
        # Crear un diccionario con los datos del formulario
        datos = {
            "ID": id_unico,
            "Apellido": apellido.capitalize(),
            "Nombre": nombre.capitalize(),
            "FechaAlta": fecha_alta
        }
        # Especificar el directorio y nombre del archivo JSON
        directorio = "datos"  # Puedes cambiar esto a cualquier directorio que prefieras
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        archivo_json = os.path.join(directorio, "datos.json")
        
        # Leer el contenido existente del archivo JSON si existe
        if os.path.exists(archivo_json):
            with open(archivo_json, "r") as archivo:
                try:
                    datos_existentes = json.load(archivo)
                    # Verificar si el contenido es una lista
                    if not isinstance(datos_existentes, list):
                        datos_existentes = []
                except json.JSONDecodeError:
                    datos_existentes = []
        else:
            datos_existentes = []
        
        # Agregar los nuevos datos a los datos existentes
        datos_existentes.append(datos)
        
        # Guardar los datos en el archivo JSON
        with open(archivo_json, "w") as archivo:
            json.dump(datos_existentes, archivo, indent=4)
        
        # Mensaje de éxito
        # st.success(f"Formulario enviado con éxito. Los datos se han guardado en {archivo_json}.")
        st.success(f"Formulario enviado con éxito. Los datos de: {nombre} {apellido}, se han guardado en la Base de Datos")


       
    else:
        st.error("Por favor, complete todos los campos.")
            