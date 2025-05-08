import joblib
import os
import pandas as pd

MODULE_DIR = os.path.dirname(__file__)

PICKLE_PATH = os.path.join(MODULE_DIR, '..', 'models')
SCALER_PATH = os.path.join(PICKLE_PATH, 'weightedAvgGrade.pkl')
PCA_PATH = os.path.join(PICKLE_PATH, 'pca.pkl')

def scaling_avg_grade(df):
    grade_scaler = joblib.load(SCALER_PATH)

    df['Weighted_avg_grade'] = grade_scaler.transform(
        pd.DataFrame(df['Weighted_avg_grade']))

    return df

def reversing_json(json_item):
    reversed_dict = {v: int(k) for k, v in json_item.items()}
    
    return reversed_dict

def encoding_data(df, json_list):
    reversed_app_mode = reversing_json(json_list['application_mode_val'])
    reversed_gender = reversing_json(json_list['gender_val'])
    reversed_scholarship = reversing_json(json_list['scholarship_hold_val'])
    reversed_displaced = reversing_json(json_list['displaced_val'])
    reversed_tuition = reversing_json(json_list['tuition_fees_val'])
    reversed_debtor = reversing_json(json_list['debtor'])

    df['Application_mode'] = df['Application_mode'].map(reversed_app_mode)
    df['Tuition_fees_up_to_date'] = df['Tuition_fees_up_to_date'].map(reversed_tuition)
    df['Gender'] = df['Gender'].map(reversed_gender)
    df['Scholarship_holder'] = df['Scholarship_holder'].map(reversed_scholarship)
    df['Displaced'] = df['Displaced'].map(reversed_displaced)
    df['Debtor'] = df['Debtor'].map(reversed_debtor)

    return df


    
def pca_helper(df):
    pca = joblib.load(PCA_PATH)
    pca_df = pca.transform(df)
    
    return pca_df