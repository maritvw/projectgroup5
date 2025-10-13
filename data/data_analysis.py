import pandas as pd
df = pd.read_csv("data/per_person_travel_modes_travel_purpose_08102025_094303.csv", sep=';')
for col in df.columns:
    try:
        df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
    except ValueError:
        pass
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace(r'[^\w\d_]+', '', regex=True)
)


# 🔹 Hernoem kolommen naar korte, logische namen
rename_map = {
    "travel_motives": "travel_motive",
    "population": "population",
    "travel_modes": "travel_mode",
    "margins": "margins",
    "region_characteristics": "region",
    "periods": "year",
    "average_per_person_per_year_trips_number": "trips_per_person",
    "average_per_person_per_year_distance_travelled_passenger_kilometres": "distance_per_person",
    "average_per_person_per_year_time_travelled_hours": "time_per_person"
}
df = df.rename(columns=rename_map)


df.to_csv('data_clean.csv',index=False)

