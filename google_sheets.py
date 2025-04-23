import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st
import json

SPREADSHEET_NAME = "Lab_Material_"  # 👈 Cambia esto por el nombre exacto de tu hoja

def get_worksheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = st.secrets["gcp_service_account"]
    creds_json = json.loads(json.dumps(creds_dict))  # convierte a JSON
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(creds_json, scope)
    client = gspread.authorize(credentials)
    sheet = client.open(SPREADSHEET_NAME).sheet1
    return sheet

def read_sheet():
    worksheet = get_worksheet()
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

def write_sheet(df):
    worksheet = get_worksheet()
    worksheet.clear()
    worksheet.update([df.columns.tolist()] + df.values.tolist())
