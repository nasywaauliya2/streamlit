import streamlit as st
import pandas as pd
import numpy as np

# TITLE
st.title("Dashboard Sederhana Streamlit")


# HEADER
st.header("Visualisasi Data Menggunakan Streamlit")


# SUBHEADER
st.subheader("Contoh Data Tabel dan Grafik")


# CAPTION
st.caption("Data ini hanya contoh untuk keperluan pembelajaran")


# TEXT (PARAGRAF)
st.text(
    "Aplikasi ini dibuat menggunakan Streamlit. "
    "Pada halaman ini ditampilkan contoh tabel data "
    "serta grafik sederhana tanpa menggunakan matplotlib."
)


# CODE (POTONGAN KODE)
st.code(
    """
import streamlit as st
import pandas as pd

st.title("Contoh Streamlit")
st.line_chart(data)
    """,
    language="python"
)


# DATA FRAME
data = pd.DataFrame({
    "Hari": ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"],
    "Penjualan": [120, 150, 170, 160, 180]
})

st.subheader("Tabel Data Penjualan")
st.dataframe(data)


# CHART (TANPA MATPLOTLIB)
st.subheader("Grafik Penjualan")
st.line_chart(data["Penjualan"])
