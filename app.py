import streamlit as st
import gspread
import json
from google.oauth2.service_account import Credentials

st.title("Tes Koneksi Google Sheets")

# Ambil credential dari Secrets
creds_dict = json.loads(st.secrets["GOOGLE_CREDS_JSON"])

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_info(
    creds_dict,
    scopes=scopes
)

client = gspread.authorize(credentials)

# GANTI dengan NAMA spreadsheet kamu (harus sama persis)
spreadsheet_name = "Recap Visit YOVI"
sheet = client.open(spreadsheet_name).sheet1

data = sheet.get_all_records()

st.success("Berhasil terhubung ke Google Sheets 🎉")
st.write(data)

