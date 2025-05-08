import pandas as pd
import numpy as np

def total_units_enrolled(df):
    first_sem = df[df['Curricular Type'] == '1st Semester Enrolled']['Total Units'].values[0]
    second_sem = df[df['Curricular Type'] == '2nd Semester Enrolled']['Total Units'].values[0]
    
    total_enrolled_un = int(first_sem) + int(second_sem)

    new_row = pd.DataFrame([{
        'Curricular Type': 'Total Units Enrolled',
        'Total Units': total_enrolled_un
    }])

    df = pd.concat([df, new_row], ignore_index=True)

    return df, total_enrolled_un

def total_units_approved(df):
    total_enrolled_un = (df['1st Semester Approved'] + 
                         df['2nd Semester Approved'])

    df['Total Units Approved'] = total_enrolled_un

    return df

def units_without_eval_col(df):
    without_eval = (df['1st Semester No Eval'] +
                    df['2nd Semester No Eval'])

    df['Total Units Without Eval'] = without_eval
    
    return df

def approval_rate_col(df):
    approval_rate = (df['Total Units Approved'] /
                     df['Total Units Enrolled'])

    df['Approval Rate'] = approval_rate
    df['Approval Rate'] = df['Approval Rate'].fillna(0)

    return df

def weighted_avg_grade_col(curricular_df, grade_df):
    total_credits = (curricular_df['1st Semester Enrolled'] + curricular_df['1st Semester Enrolled'])
    weigthed_grade = ((grade_df['1st Semester Grade'] * curricular_df['1st Semester Enrolled']) +
                       (grade_df['2nd Semester Grade'] * curricular_df['2nd Semester Enrolled']) /
                       total_credits) 

    grade_df['Weighted Avg Grade'] = weigthed_grade

    grade_df['Weighted Avg Grade'] = grade_df['Weighted Avg Grade'].fillna(0, axis=0)

    return grade_df

def econ_pressure_col(df):
    marital_weight = np.where(df['Marital_status'] == 1, 1, 2)
    debtor_weight = np.where(df['Debtor'] == 1, 1.5, 1)  # lebih berat kalau berutang
    gender_weight = np.where(df['Gender'] == 1, 1.5, 1)

    total_weight = marital_weight * debtor_weight * gender_weight

    df['Econ_pressure'] = (df['Unemployment_rate'] * df['Inflation_rate']) * total_weight
    return df