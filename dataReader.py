import pandas as pd

sheets_names = []
df = pd.read_excel("data/0_1mM.ods", engine="odf")

print(df.head())

