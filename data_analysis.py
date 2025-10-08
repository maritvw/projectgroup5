# Import required libraries
import pandas as pd
import chardet
import os

# Detect encoding of the CSV file
file = 'per_person__travel_modes__travel_purpose_08102025_094303.csv'
with open(file, 'rb') as f:
    rawdata = f.read(100000)
    result = chardet.detect(rawdata)

print(result)

# Use the detected encoding to read the file
enc = result['encoding']

# Read the dataset with semicolon separator (common for Dutch CSV files)
df = pd.read_csv(file, encoding=enc, sep=';')

# Display basic info about the dataset
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
df.head()