import pandas as pd
import json

# Sample JSON data
# json_data = '''
# [
#     {"Name": "John Doe", "Age": 30, "City": "New York"},
#     {"Name": "Jane Smith", "Age": 25, "City": "Los Angeles"},
#     {"Name": "Sam Brown", "Age": 22, "City": "Chicago"}
# ]
# '''

data = [
    ["name", "email", "phone"],
    ['test','test@gmail.com',1]
]

# Load JSON data
# data = json.loads(json_data)

# Convert JSON data to a DataFrame
df = pd.DataFrame(data)

# Write DataFrame to an Excel file
excel_file = 'output1.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data successfully written to {excel_file}")
