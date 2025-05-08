import pandas as pd
import numpy as np

def total_units_enrolled(df):
    first_sem = df[df['Curricular Type'] == '1st Semester Enrolled']['Total Units'].values[0]
    second_sem = df[df['Curricular Type'] == '2nd Semester Enrolled']['Total Units'].values[0]
    
    total_enrolled_un = int(first_sem) + int(second_sem)

    if 'Total Units Enrolled' in df['Curricular Type'].values:
        df.loc[df['Curricular Type'] == 'Total Units Enrolled', 'Total Units'] = total_enrolled_un
    else:
        new_row = pd.DataFrame([{
            'Curricular Type': 'Total Units Enrolled',
            'Total Units': total_enrolled_un
        }])
        df = pd.concat([df, new_row], ignore_index=True)

    return df, total_enrolled_un

def total_units_approved(df):
    first_sem = df[df['Curricular Type'] == '1st Semester Approved']['Total Units'].values[0]
    second_sem = df[df['Curricular Type'] == '2nd Semester Approved']['Total Units'].values[0]
    total_approved_un = int(first_sem) + int(second_sem)

    if 'Total Units Approved' in df['Curricular Type'].values:
        df.loc[df['Curricular Type'] == 'Total Units Approved', 'Total Units'] = total_approved_un
    else:
        new_row = pd.DataFrame([{
            'Curricular Type': 'Total Units Approved',
            'Total Units': total_approved_un
        }])
        df = pd.concat([df, new_row], ignore_index=True)

    return df, total_approved_un


def units_without_eval(df):
    first_no_eval = df[df['Curricular Type'] == '1st Semester No Eval']['Total Units'].values[0]
    second_no_eval = df[df['Curricular Type'] == '2nd Semester No Eval']['Total Units'].values[0]
    without_eval = int(first_no_eval) + int(second_no_eval)

    if 'Total Units Without Eval' in df['Curricular Type'].values:
        df.loc[df['Curricular Type'] == 'Total Units Without Eval', 'Total Units'] = without_eval
    else:
        new_row = pd.DataFrame([{
            'Curricular Type': 'Total Units Without Eval',
            'Total Units': without_eval
        }])
        df = pd.concat([df, new_row], ignore_index=True)
    
    return df, without_eval


def calculate_approval_rate(df):
    total_approved = df[df['Curricular Type'] == 'Total Units Approved']['Total Units'].values[0]
    total_enrolled = df[df['Curricular Type'] == 'Total Units Enrolled']['Total Units'].values[0]
    
    if total_enrolled != 0:
        approval_rate = float(total_approved) / float(total_enrolled)
    else:
        approval_rate = 0.0

    if 'Approval Rate' in df['Curricular Type'].values:
        df.loc[df['Curricular Type'] == 'Approval Rate', 'Total Units'] = approval_rate
    else:
        new_row = pd.DataFrame([{
            'Curricular Type': 'Approval Rate',
            'Total Units': approval_rate
        }])
        df = pd.concat([df, new_row], ignore_index=True)

    df = df.fillna(0)
    
    return df, approval_rate


def weighted_avg_grade(curricular_df, grade_df):
    first_sem_enroll = float(curricular_df[curricular_df['Curricular Type'] == '1st Semester Enrolled']['Total Units'].values[0])
    second_sem_enroll = float(curricular_df[curricular_df['Curricular Type'] == '2nd Semester Enrolled']['Total Units'].values[0])
    first_sem_grade = float(grade_df['1st Semester Grade'].values[0])
    second_sem_grade = float(grade_df['2nd Semester Grade'].values[0])

    total_credits = first_sem_enroll + second_sem_enroll

    if total_credits > 0:
        weighted_grade = ((first_sem_grade * first_sem_enroll) + 
                          (second_sem_grade * second_sem_enroll)) / total_credits
    else:
        weighted_grade = 0.0

    if 'Weighted Avg Grade' in grade_df.columns:
        grade_df.at[0, 'Weighted Avg Grade'] = weighted_grade
    else:
        grade_df['Weighted Avg Grade'] = weighted_grade

    grade_df = grade_df.fillna(0)

    return grade_df, weighted_grade



def econ_pressure(*inputs):
    gender, marital, debtor, unemploy_rt, inflation_rt = inputs
    marital_weight = np.where(marital != 'Single', 1, 2)
    debtor_weight = np.where(debtor == 'Yes', 1.5, 1)  
    gender_weight = np.where(gender == 'Male', 1.5, 1)

    total_weight = marital_weight * debtor_weight * gender_weight

    econ_pressure = (unemploy_rt * inflation_rt) * total_weight

    return econ_pressure