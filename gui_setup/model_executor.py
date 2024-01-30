from db_login import get_odoo_credentials
from json_loader import load_json_files
from model_selector import select_json_file
from translator import translate_identifiers
from connector import connect_and_fetch_data
from mappings import id_to_name_mapping, id_to_duration_mapping
from preprocessing import extract_data
from model import total_order_from_data
from postprocessing import process_result

# Specify the folder path where your JSON files are located
json_folder_path = 'jsonModels'

# Load JSON files using the imported function
json_models = load_json_files(json_folder_path)

# Call the function to get the selected JSON file
selected_json = select_json_file(json_models)

if selected_json:
    url, db, username, password = get_odoo_credentials()
    
    # Translate identifiersp
    db_prop_names  = translate_identifiers(selected_json, id_to_name_mapping, id_to_duration_mapping)
    
    # Connect to odoo and fetch data
    db_values = connect_and_fetch_data(url, db, username, password, db_prop_names)
    
    # Extract 'name' and 'production_duration_expected'
    names, durations = extract_data(db_values)
    #pre_values = "[" + ', '.join(map(repr, names)) + "]\n" + "[" + ', '.join(map(str, durations)) + "]"

    # Optimization Model
    result = total_order_from_data(names, durations)
    
    # Optimal job order
    result_temp = process_result(result)
    
    
    
    
    
    