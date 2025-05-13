import joblib
import os
import pandas as pd
import numpy as np

MODULE_DIR = os.path.dirname(__file__)

PICKLE_PATH = os.path.join(MODULE_DIR, '..', 'models')
SCALER_PATH = os.path.join(PICKLE_PATH, 'scaler.pkl')
PCA_PATH = os.path.join(PICKLE_PATH, 'pca.pkl')
MODEL_PATH = os.path.join(PICKLE_PATH, 'xgb_model.pkl')
TRANSFORM_PATH = os.path.join(PICKLE_PATH, 'powertransform.pkl')

def transform_data(df, pt_cols):
    pt = joblib.load(TRANSFORM_PATH)
    df_cols = df.columns

    for col in df_cols:
        if col in pt_cols:
            reshaped = df[[col]].values
            transformed = pt.transform(reshaped)
            df[col] = transformed
        else:
            continue

    return df

def scaling_data(df, robust_cols):
    scaler = joblib.load(SCALER_PATH)

    # Pastikan kolom robust_cols semuanya ada di df
    missing_cols = [col for col in robust_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in input DataFrame: {missing_cols}")

    # Urutkan kolom sesuai dengan urutan robust_cols
    df_scaled_part = pd.DataFrame(scaler.transform(df[robust_cols]), 
                                  columns=robust_cols, 
                                  index=df.index)

    # Ganti kolom lama dengan versi scaled
    df.update(df_scaled_part)

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

def pca_helper(df, pca_cols):
    pca = joblib.load(PCA_PATH)

    # Validasi kolom
    missing_cols = [col for col in pca_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in input DataFrame: {missing_cols}")

    X_pca = df[pca_cols]
    
    X_pca = pca.transform(X_pca)

    return X_pca

def predict_function(x_test):
    model = joblib.load(MODEL_PATH)
    
    y_pred = model.predict(x_test)
    y_pred_classes = np.argmax(y_pred, axis=1) if y_pred.ndim > 1 else y_pred
    
    return y_pred_classes