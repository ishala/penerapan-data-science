import streamlit as st

st.title('Student Status Predictions')
st.subheader(':green[Graduate] vs :blue[Enrolled] vs :red[Dropout]', divider='gray')

# Section Profil Siswa
st.subheader('Student Profile')


gender = st.radio(
    'Gender',
    ['Laki-laki', 'Perempuan'],
    horizontal=True
)

col1_profile, col2_profile = st.columns(2)
with col1_profile:
    age = st.text_input('Age at Enrollment')

with col2_profile:
    age = st.text_input('Age at Enollment')


if age != '':
    age = int(age)
