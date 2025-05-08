import json
import os

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
