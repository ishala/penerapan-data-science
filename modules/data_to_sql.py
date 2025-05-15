import pandas as pd
import os
from sqlalchemy import create_engine
from data_load import json_list

CURRENT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(CURRENT_DIR, '..', 'data', 'modified_data.csv')

DB_USER = 'postgres.uydwipcuxtobaiekcxxs'  
DB_PASSWORD = 'root123'
DB_HOST = 'aws-0-ap-southeast-1.pooler.supabase.com'
DB_PORT = '6543'
DB_NAME = 'postgres'

conn_str = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(conn_str)

df = pd.read_csv(DATA_PATH)

map_dict = {}

# Convert Keys into Integer
for key in json_list.keys():
    map_dict[key] = {int(k): v for k, v in json_list[key].items()}

# Add column Id
df.insert(0, 'student_id', range(1, len(df) + 1))

# Decoding Data
df['Marital_status'] = df['Marital_status'] \
    .map(map_dict['marital_status_val'])
df['Application_mode'] = df['Application_mode'] \
    .map(map_dict['application_mode_val'])
df['Course'] = df['Course'].map(map_dict['course_val'])
df['Daytime_evening_attendance'] = df['Daytime_evening_attendance'] \
    .map(map_dict['daytime_evening_val'])
df['Previous_qualification'] = df['Previous_qualification'] \
    .map(map_dict['previous_qual_val'])
df['Nacionality'] = df['Nacionality'] \
    .map(map_dict['nacionality_val'])
df['Mothers_qualification'] = df['Mothers_qualification'] \
    .map(map_dict['mother_qual_val'])
df['Fathers_qualification'] = df['Fathers_qualification'] \
    .map(map_dict['father_qual_val'])
df['Mothers_occupation'] = df['Mothers_occupation'] \
    .map(map_dict['mother_occupation_val'])
df['Fathers_occupation'] = df['Fathers_occupation'] \
    .map(map_dict['father_occupation_val'])
df['Displaced'] = df['Displaced'] \
    .map(map_dict['displaced_val'])
df['Educational_special_needs'] = df['Educational_special_needs'] \
    .map(map_dict['edu_special_needs_val'])
df['Debtor'] = df['Debtor'].map(map_dict['debtor'])
df['Tuition_fees_up_to_date'] = df['Tuition_fees_up_to_date'] \
    .map(map_dict['tuition_fees_val'])
df['Gender'] = df['Gender'].map(map_dict['gender_val'])
df['Scholarship_holder'] = df['Scholarship_holder'] \
    .map(map_dict['scholarship_hold_val'])
df['International'] = df['International'] \
    .map(map_dict['international_val'])

df.to_sql('students_performance', engine, index=False, if_exists='replace')