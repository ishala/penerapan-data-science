import joblib
import os
import pandas as pd
import numpy as np

MODULE_DIR = os.path.dirname(__file__)

PICKLE_PATH = os.path.join(MODULE_DIR, '..', 'models')
SCALER_PATH = os.path.join(PICKLE_PATH, 'weightedAvgGrade.pkl')
PCA_PATH = os.path.join(PICKLE_PATH, 'pca.pkl')
MODEL_PATH = os.path.join(PICKLE_PATH, 'xgb_model.pkl')

def scaling_avg_grade(df):
    grade_scaler = joblib.load(SCALER_PATH)

    df['Weighted_avg_grade'] = grade_scaler.transform(
        pd.DataFrame(df['Weighted_avg_grade']))

    return df

def reversing_json(json_item):
    reversed_dict = {v.lower(): int(k) for k, v in json_item.items()}

    return reversed_dict

def encoding_data(df, json_list):
    reversed_app_mode = reversing_json(json_list['application_mode_val'])
    reversed_gender = reversing_json(json_list['gender_val'])
    reversed_scholarship = reversing_json(json_list['scholarship_hold_val'])
    reversed_displaced = reversing_json(json_list['displaced_val'])
    reversed_tuition = reversing_json(json_list['tuition_fees_val'])
    reversed_debtor = reversing_json(json_list['debtor'])

    df['Application_mode'] = df['Application_mode'].str.lower()\
                            .map(reversed_app_mode)
    df['Tuition_fees_up_to_date'] = df['Tuition_fees_up_to_date'].str.lower()\
                                    .map(reversed_tuition)
    df['Gender'] = df['Gender'].str.lower().map(reversed_gender)
    df['Scholarship_holder'] = df['Scholarship_holder'].str.lower()\
                                .map(reversed_scholarship)
    df['Displaced'] = df['Displaced'].str.lower().map(reversed_displaced)
    df['Debtor'] = df['Debtor'].str.lower().map(reversed_debtor)

    return df

def pca_helper(df):
    pca = joblib.load(PCA_PATH)
    pca_df = pca.transform(df)
    
    return pca_df

def predict_function(x_test):
    model = joblib.load(MODEL_PATH)
    
    y_pred = model.predict(x_test)
    y_pred_classes = np.argmax(y_pred, axis=1) if y_pred.ndim > 1 else y_pred
    
    return y_pred_classes