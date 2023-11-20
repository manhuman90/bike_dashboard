import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Memuat data
file_name = "day.csv"
bike_data = pd.read_csv(file_name)


# Membuat kolom baru untuk kategori suhu
def kategori_suhu(temp):
    if temp * 41 < 10:
        return "Dingin"
    elif 10 <= temp * 41 < 20:
        return "Sejuk"
    elif 20 <= temp * 41 < 30:
        return "Hangat"
    else:
        return "Panas"


bike_data["temp_category"] = bike_data["temp"].apply(kategori_suhu)

# Judul dashboard
st.title("Dashboard Analisis Data Peminjaman Sepeda")

# Visualisasi 1: Tren Peminjaman Sepeda Berdasarkan Musim dan Hari dalam Seminggu
st.subheader("Tren Peminjaman Sepeda Berdasarkan Musim dan Hari dalam Seminggu")
# Menampilkan boxplot
fig, ax = plt.subplots(figsize=(10, 6))
bike_data.boxplot(column="cnt", by=["season", "weekday"], ax=ax)
plt.xlabel("Musim dan Hari dalam Seminggu")
plt.ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# Visualisasi 2: Pola Peminjaman Berdasarkan Kondisi Cuaca
st.subheader("Pola Peminjaman Berdasarkan Kondisi Cuaca")
# Menampilkan bar plot
pola_cuaca = bike_data.groupby("weathersit")["cnt"].mean()
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.bar(pola_cuaca.index, pola_cuaca.values)
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Peminjaman")
plt.xticks(ticks=[0, 1, 2, 3], labels=["Clear", "Mist", "Light Rain", "Heavy Rain"])
st.pyplot(fig2)

# Visualisasi 3: Pengelompokan Sederhana Berdasarkan Rentang Suhu
st.subheader("Pengelompokan Peminjaman Berdasarkan Rentang Suhu")
# Menampilkan scatter plot
fig3, ax3 = plt.subplots(figsize=(8, 6))
for category in bike_data["temp_category"].unique():
    temp_subset = bike_data[bike_data["temp_category"] == category]
    ax3.scatter(temp_subset["temp"], temp_subset["cnt"], label=category)
plt.xlabel("Temperatur")
plt.ylabel("Jumlah peminjam")
plt.title("Pengelompokan peminjaman berdasarkan rentang suhu")
plt.legend()
st.pyplot(fig3)
