# data_pipeline/synthetic_data_generator.py
import pandas as pd

data = {"PatientID": [1, 2, 3], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
df.to_csv("data_pipeline/patient_data.csv", index=False)
print("CSV file created!")