import pandas as pd
df = pd.read_csv("data/per_person__travel_modes__travel_purpose_08102025_094303.csv", sep=';')
for col in df.columns:
    try:
        df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
    except ValueError:
        pass
df.columns = (
    df.columns.str.strip()
    .str.lower()
    # .str.replace(' ', '_')
    .str.replace(r'[^\w\d_]+', '', regex=True)
)

df.to_csv('data_clean.csv', index=False)
