import pandas as pd

# Read the JSON file into a DataFrame
df = pd.read_json('file.json')

# Write the DataFrame to a CSV file
df.to_csv('out.csv', index=False)
