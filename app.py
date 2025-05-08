import streamlit as st
import pandas as pd
from modules.data_load import json_list
from modules.data_preprocess import total_units_enrolled

st.title('Student Status Predictions')
st.subheader(':green[Graduate] vs :blue[Enrolled] vs :red[Dropout]', divider='gray')

# Section Profil Siswa
st.markdown('## **Student Profile**')

sec1_col1_profile, sec1_col2_profile, sec1_col3_profile = st.columns(3)

# Gender Section
with sec1_col1_profile:
    gender = st.radio(
        'Gender',
        [v.capitalize() 
        for v in list(json_list['gender_val'].values())],
        horizontal=True
    )

pronoun = 'His' if gender == 'Male' else 'Her'

# Application Mode Section
with sec1_col2_profile:
    application_mode = st.selectbox(
        f'What\'s {pronoun} Application Mode?',
        [v.capitalize() 
        for v in list(json_list['application_mode_val'].values())],
        index=None,
        placeholder="Select the application mode..."
    )

# Age at Enrollment Section
with sec1_col3_profile:
    age = st.text_input(
        f'What\'s {pronoun} Age at Enrollment?',
        placeholder='e.g 20, 25, etc.'
    )

# Marital Status Section
marital = st.radio(
    f'What\'s {pronoun} Marital Status?',
    [v.capitalize() 
     for v in list(json_list['marital_status_val'].values())],
    horizontal=True
)

sec2_col1_profile, sec2_col2_profile = st.columns(2)

# Section Scholarship
with sec2_col1_profile:
    scholarship = st.radio(
        f'What\'s {pronoun} Scholarship Status?',
        [v.capitalize() 
        for v in list(json_list['scholarship_hold_val'].values())],
        horizontal=True
    )

# Section Displaced
with sec2_col2_profile:
    displaced = st.radio(
        f'What\'s {pronoun} Displaced Status?',
        [v.capitalize() 
        for v in list(json_list['displaced_val'].values())],
        horizontal=True
    )

st.divider()

# Section Performa Siswa
st.markdown('## **Student Economy**')
sec1_col1_eco, sec1_col2_eco = st.columns(2)

# Section Tuition
with sec1_col1_eco:
    tuition = st.radio(
        f'What\'s {pronoun} Tuition Status?',
        [v.capitalize() 
        for v in list(json_list['tuition_fees_val'].values())],
        horizontal=True
    )
    
    unemploy_rate = st.number_input(
        f'How is {pronoun} Unemployment Rate?'
    )

# Section Debtor
with sec1_col2_eco:
    debtor = st.radio(
        f'What\'s {pronoun} Debtor Status?',
        [v.capitalize() 
        for v in list(json_list['debtor'].values())],
        horizontal=True
    )

    inflation_rate = st.number_input(
        f'How is {pronoun} Inflation Rate?'
    )

st.divider()
st.markdown('## **Student Performances**')
st.write('Please edit on the tables below!')

st.markdown("### **Curricular Units**")
curricular_df = pd.DataFrame([
    {'Curricular Type': '1st Semester Enrolled', 'Total Units': 0,},
    {'Curricular Type': '1st Semester Approved', 'Total Units': 0},
    {'Curricular Type': '1st Semester No Eval', 'Total Units': 0},
    {'Curricular Type': '2nd Semester Enrolled', 'Total Units': 0},
    {'Curricular Type': '2nd Semester Approved', 'Total Units': 0},
    {'Curricular Type': '2nd Semester No Eval', 'Total Units': 0}
])

edited_curr_df = st.data_editor(curricular_df, 
                                hide_index=True,
                                disabled=['Curricular Type'])

# Calculate Total Units Enrolled
edited_curr_df, total_enrolled_un = total_units_enrolled(edited_curr_df)


st.markdown("### **Student Grades**")
grade_df = pd.DataFrame([
    {
    '1st Semester Grade': 0.0,
    '2nd Semester Grade': 0.0,
    'Admission Grade': 0.0,
    'Previous Qualification Grade': 0.0
    }
])

edited_grd_df = st.data_editor(grade_df, hide_index=True)

st.subheader(':blue[Student Performance Result]')

col1_perform, col2_perform = st.columns(2)

with col1_perform:
    st.markdown('**Total Units Enrolled:**', total_enrolled_un)