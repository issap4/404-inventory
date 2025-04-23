import pandas as pd
import streamlit as st
from google_sheets import read_sheet, write_sheet

def load_data():
    try:
        df = read_sheet()
        return df
    except Exception as e:
        st.error(f"❌ Error al cargar los datos desde Google Sheets: {e}")
        return None

def save_data(df):
    try:
        write_sheet(df)
    except Exception as e:
        st.error(f"❌ Error al guardar los datos en Google Sheets: {e}")

# ✅ Cargar datos aquí
df = load_data()
if df is None:
    st.stop()

st.subheader('📦 Inventory Management')

if st.button("🔍 Go to Search and Filters"):
    st.switch_page("app.py")

# Agregar un nuevo material
st.subheader('➕ Add New Material')
with st.form(key='add_form'):
    material = st.text_input('Material')
    description = st.text_input('Description')
    container = st.text_input('Container')
    location = st.selectbox('Location', ["locker 1", "locker 2", "locker 3", "work-table"])
    shelf = st.selectbox('Shelf', ["top", "bottom", "2nd", "3er", "4th", "5th", "on", "under"])
    amount = st.number_input('Amount', min_value=0)
    keywords = st.text_input('Keywords')

    submit_button = st.form_submit_button(label='Add Material')

    if submit_button:
        new_material = pd.DataFrame({
            'Material': [material],
            'Description': [description],
            'Container': [container],
            'Location': [location],
            'Shelf': [shelf],
            'Amount': [amount],
            'Keywords': [keywords]
        })
        
        df = pd.concat([df, new_material], ignore_index=True)
        save_data(df)  # ✅ Cambiar guardado
        df = load_data()
        st.cache_data.clear()
        st.success('Material successfully added!')

# Modificar un material existente
st.subheader('✏️ Modify Material in Stock')
material_to_modify = st.selectbox('Select the material to modify: ', df['Material'].unique())
selected_material = df[df['Material'] == material_to_modify].iloc[0]

with st.form(key='modify_form'):
    new_description = st.text_input('Description', value=selected_material['Description'])
    new_container = st.text_input('Container', value=selected_material['Container'])
    new_location = st.selectbox('Location', ["locker 1", "locker 2", "locker 3", "work-table"], index=["locker 1", "locker 2", "locker 3", "work-table"].index(selected_material['Location']) if selected_material['Location'] in ["locker 1", "locker 2", "locker 3", "work-table"] else 0)
    new_shelf = st.selectbox('Shelf', ["top", "bottom", "2nd", "3er", "4th", "5th", "on", "under"], index=["top", "bottom", "2nd", "3er", "4th", "5th", "on", "under"].index(selected_material['Shelf']) if selected_material['Shelf'] in ["top", "bottom", "2nd", "3er", "4th", "5th", "on", "under"] else 0)
    new_amount = st.number_input('Amount', value=selected_material['Amount'])
    new_keywords = st.text_input('Keywords', value=selected_material['Keywords'])

    submit_button = st.form_submit_button(label='Modify Material')

    if submit_button:
        df.loc[df['Material'] == material_to_modify, ['Description', 'Container', 'Location', 'Shelf', 'Amount', 'Keywords']] = [
            new_description, new_container, new_location, new_shelf, new_amount, new_keywords
        ]
        save_data(df)
        st.cache_data.clear()
        st.success('Material successfully modified!')

# Eliminar un material
st.subheader('🗑️ Delete Material')
material_to_delete = st.selectbox('Select the material to delete:', df['Material'].unique())

delete_button = st.button(label='Delete Material')

if delete_button:
    df = df[df['Material'] != material_to_delete]
    save_data(df)
    st.cache_data.clear()
    st.success('Material successfully deleted!')
