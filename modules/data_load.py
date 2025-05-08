import json
import os
import pandas as pd

# Data JSON
MODULE_DIR = os.path.dirname(__file__)

JSON_PATH = os.path.join(MODULE_DIR, '..', 'data', 'jsons')

file_list = [f for f in os.listdir(JSON_PATH) 
             if os.path.isfile(os.path.join(JSON_PATH, f))]

json_list = {}

for file in file_list:
    json_file_path = os.path.join(JSON_PATH, file)
    key_name = os.path.splitext(file)[0]  
    
    with open(json_file_path, 'r') as json_f:
        json_list[key_name] = json.load(json_f)


# Template Dataframe
curricular_df = pd.DataFrame([
    {'Curricular Type': '1st Semester Enrolled', 'Total Units': 0,},
    {'Curricular Type': '1st Semester Approved', 'Total Units': 0},
    {'Curricular Type': '1st Semester Eval', 'Total Units': 0},
    {'Curricular Type': '1st Semester No Eval', 'Total Units': 0},
    {'Curricular Type': '2nd Semester Enrolled', 'Total Units': 0},
    {'Curricular Type': '2nd Semester Approved', 'Total Units': 0},
    {'Curricular Type': '2nd Semester Eval', 'Total Units': 0},
    {'Curricular Type': '2nd Semester No Eval', 'Total Units': 0}
])

grade_df = pd.DataFrame([
    {
    '1st Semester Grade': 0.0,
    '2nd Semester Grade': 0.0,
    'Admission Grade': 0.0,
    'Previous Qualification Grade': 0.0
    }
])