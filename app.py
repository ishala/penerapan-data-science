import streamlit as st
import pandas as pd
from modules.data_load import json_list, curricular_df, grade_df
from modules.data_preprocess import *
from modules.modelling import *

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
    # Section Tuition
    tuition = st.radio(
        f'What\'s {pronoun} Tuition Status?',
        [v.capitalize() 
        for v in list(json_list['tuition_fees_val'].values())],
        horizontal=True
    )
    # Section Unemploy Rate
    unemploy_rate = st.number_input(
        f'How is {pronoun} Unemployment Rate?'
    )

# Section Debtor
with sec1_col2_eco:
    # Section Debtor
    debtor = st.radio(
        f'What\'s {pronoun} Debtor Status?',
        [v.capitalize() 
        for v in list(json_list['debtor'].values())],
        horizontal=True
    )
    # Section Inflation
    inflation_rate = st.number_input(
        f'How is {pronoun} Inflation Rate?'
    )

st.divider()
st.markdown('## **Student Performances**')
st.write('Please edit on the tables below!')

st.markdown("### **Curricular Units**")
edited_curr_df = st.data_editor(curricular_df, 
                                hide_index=True,
                                disabled=['Curricular Type'])

# Calculate Total Units Enrolled
edited_curr_df, total_enrolled_un = total_units_enrolled(edited_curr_df)
# Calculate Total Units Approved
edited_curr_df, total_approved_un = total_units_approved(edited_curr_df)
# Calculate Total Units No Eval
edited_curr_df, without_eval = units_without_eval(edited_curr_df)
# Calculate Approval Rate
edited_curr_df, approval_rate = calculate_approval_rate(edited_curr_df)
# Calculate Economic Pressure
econ_press = econ_pressure(gender, marital, debtor,
                           unemploy_rate, inflation_rate)

st.markdown("### **Student Grades**")
edited_grd_df = st.data_editor(grade_df, hide_index=True)

# Calculate Weighted Avg Grade
edited_grd_df, weighted_avg_grd = weighted_avg_grade(edited_curr_df, edited_grd_df)

st.divider()
st.subheader(':blue[Student Performance Result]')

col1_perform, col2_perform = st.columns(2)

with col1_perform:
    st.markdown(f'**Total Units Enrolled:** {total_enrolled_un}')
    st.markdown(f'**Total Units Approved:** {total_approved_un}')
    st.markdown(f'**Total Units Without Eval:** {without_eval}')

with col2_perform:
    st.markdown(f'**Total Approval Rate:** {approval_rate}')
    st.markdown(f'**Average Grade:** {weighted_avg_grd}')
    st.markdown(f'**Student Economy Pressure:** {econ_press}')

### Submit Predict
st.divider()

st.subheader('Student Prediction')

col1_predict, col2_predict = st.columns(2)

with col1_predict:
    predict = st.button(label='Predict')
    if predict:
        # Collecting Data
        fixed_df = pd.DataFrame([{
            'Approval_rate': approval_rate,
            'Curricular_units_2nd_sem_approved': edited_curr_df[
                edited_curr_df['Curricular Type'] == '2nd Semester Approved']['Total Units'].values[0],
            'Total_units_approved': total_approved_un,
            'Curricular_units_2nd_sem_grade': grade_df['2nd Semester Grade'].values[0],
            'Curricular_units_1st_sem_approved': edited_curr_df[
                edited_curr_df['Curricular Type'] == '1st Semester Approved']['Total Units'].values[0],
            'Curricular_units_1st_sem_grade': grade_df['1st Semester Grade'].values[0],
            'Weighted_avg_grade': weighted_avg_grd,
            'Tuition_fees_up_to_date': tuition,
            'Scholarship_holder': scholarship,
            'Curricular_units_2nd_sem_enrolled': edited_curr_df[
                edited_curr_df['Curricular Type'] == '2nd Semester Enrolled']['Total Units'].values[0],
            'Total_units_enrolled': total_enrolled_un,
            'Curricular_units_1st_sem_enrolled': edited_curr_df[
                edited_curr_df['Curricular Type'] == '1st Semester Enrolled']['Total Units'].values[0],
            'Admission_grade': grade_df['Admission Grade'].values[0],
            'Displaced': displaced,
            'Previous_qualification_grade': grade_df['Previous Qualification Grade'].values[0],
            'Curricular_units_2nd_sem_evaluations': edited_curr_df[
                edited_curr_df['Curricular Type'] == '2nd Semester Eval']['Total Units'].values[0],
            'Total_units_without_eval': without_eval,
            'Curricular_units_2nd_sem_without_evaluations': edited_curr_df[
                edited_curr_df['Curricular Type'] == '2nd Semester No Eval']['Total Units'].values[0],
            'Econ_pressure': econ_press,
            'Application_mode': application_mode,
            'Gender': gender,
            'Debtor': debtor,
            'Age_at_enrollment': age
        }])

        # Scaling Weighted Avg Grade
        fixed_df = scaling_avg_grade(fixed_df)
        # Encoding Categorical Data
        encoded_df = encoding_data(fixed_df, json_list)

        # PCA
        pca_df = pca_helper(fixed_df)

        # Predictions
        pred_res = predict_function(pca_df)[0]
        if pred_res == 2:
            class_res = ':green[Graduate]'
        elif pred_res == 1:
            class_res = ':yellow[Enrolled]'
        elif pred_res == 0:
            class_res = ':red[Dropout]'
        
        st.markdown(f'### Student Result: {class_res}')