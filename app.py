import streamlit as st
import pandas as pd
from google_sheets import read_sheet

# Cargar datos desde Google Sheets
df = read_sheet()

# Título de la app
st.title("🔬404 Material - VIBES🛰️")

# Botón para ir a gestión de inventario
if st.button("🔧 Go to Inventory Management"):
    st.switch_page("pages/inventory.py")

# Barra de búsqueda
search_term = st.text_input("🔍 Search material or keyword:", "")

# Filtros por ubicación y estante
location_filter = st.selectbox(
    "📍 Filter by Location:",
    ["All"] + sorted(df["Location"].dropna().unique().tolist())
)

shelf_filter = st.selectbox(
    "🗄️ Filter by Shelf:",
    ["All"] + sorted(df["Shelf"].dropna().unique().tolist())
)

# Aplicar búsqueda y filtros
filtered_df = df[df.apply(
    lambda row: search_term.lower() in str(row.to_list()).lower(),
    axis=1
)]

if location_filter != "All":
    filtered_df = filtered_df[filtered_df["Location"] == location_filter]

if shelf_filter != "All":
    filtered_df = filtered_df[filtered_df["Shelf"] == shelf_filter]

# Mostrar resultados
st.write(f"📋 {len(filtered_df)} Material(s) found:")

if not filtered_df.empty:
    st.dataframe(filtered_df)
else:
    st.warning("⚠️ No Material was found.")

# Botón para descargar resultados
if not filtered_df.empty:
    st.download_button(
        "📥 Save search results in a CSV file",
        filtered_df.to_csv(index=False).encode("utf-8"),
        "materiales_filtrados.csv",
        "text/csv"
    )
