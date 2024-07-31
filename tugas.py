import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(page_title="Curriculum Vitae", layout="wide")

# Title
st.title("Curriculum Vitae")

# Foto
st.header("Foto")
image = Image.open('foto.jpg')  # Ganti dengan path foto Anda
st.image(image, caption='Foto Profil', width=400)

# Biodata
st.header("Biodata")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Nama")
    st.write("Muhamad Rifqi Rifquddin")  # Ganti dengan nama Anda

    st.subheader("Tempat, Tanggal Lahir")
    st.write("Jakarta, 18 Agustus 1993")  # Ganti dengan tempat dan tanggal lahir Anda

    st.subheader("Alamat")
    st.write("Jl. Mulawarman, Bekasi, Jawa Barat")  # Ganti dengan alamat Anda

with col2:
    st.subheader("Telepon")
    st.write("+62 812 83234242")  # Ganti dengan nomor telepon Anda

    st.subheader("Email")
    st.write("rifqi.hilotech@gmail.com")  # Ganti dengan email Anda

    st.subheader("LinkedIn")
    st.write("www.linkedin.com/in/muhamad-rifqi-rifquddin-a58198134")  # Ganti dengan LinkedIn Anda

# Pendidikan
st.header("Pendidikan")
education_data = [
    {"Institusi": "Universitas Diponegoro", "Jurusan": "S 1-Teknik Elektro", "Tahun": "2011 - 2015"},
]
for edu in education_data:
    st.subheader(edu["Institusi"])
    st.write(f"Jurusan: {edu['Jurusan']}")
    st.write(f"Tahun: {edu['Tahun']}")

# Pengalaman Kerja
st.header("Pengalaman Kerja")
work_experience = [
    {"Perusahaan": "PT. Hilotech Karya Anak Indonesia", "Jabatan": "System Support", "Tahun": "2018 - 2019"}
]
for work in work_experience:
    st.subheader(work["Perusahaan"])
    st.write(f"Jabatan: {work['Jabatan']}")
    st.write(f"Tahun: {work['Tahun']}")

# Pengalaman Organisasi
st.header("Pengalaman Organisasi")
org_experience = [
    {"Organisasi": "Himpunan Mahasiswa Teknik Elektro", "Jabatan": "Staff", "Tahun": "2013 - 2014"}
]
for org in org_experience:
    st.subheader(org["Organisasi"])
    st.write(f"Jabatan: {org['Jabatan']}")
    st.write(f"Tahun: {org['Tahun']}")

# Pengalaman Pelatihan
st.header("Pengalaman Pelatihan")
training_experience = [
    {"Pelatihan": "Bootcamp Data Science", "Tahun": "2024"},
    {"Pelatihan": "Pelatihan Data Science Kominfo", "Tahun": "2024"}
]
for training in training_experience:
    st.subheader(training["Pelatihan"])
    st.write(f"Tahun: {training['Tahun']}")

# Skill
st.header("Skill")
skills = [
    "Python",
    "Adobe Premiere Pro",
    "Adobe Photoshop",
    "Camera Operator",
    ]
st.write(", ".join(skills))