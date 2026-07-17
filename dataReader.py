import pandas as pd
import os



files = os.listdir("data")
sheets_names = ['Fluoresceine','Rhodamine B','Rhodamine 6G']


def read_data(file_path, sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, engine="odf")
    return df

print(os.path.join("data", files[0]))
print(read_data(os.path.join("data", files[0]), "Rhodamine B).head())