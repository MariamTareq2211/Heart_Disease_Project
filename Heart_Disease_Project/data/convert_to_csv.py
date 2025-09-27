import pandas as pd

# column names from UCI dataset description
columns = [
    "age","sex","cp","trestbps","chol","fbs","restecg","thalach",
    "exang","oldpeak","slope","ca","thal","target"
]

# load cleveland dataset
df = pd.read_csv("D:\Downloads\heart+disease\processed.cleveland.data", names=columns)

# replace '?' with NaN
df = df.replace("?", pd.NA)

# convert numeric columns properly
for col in ["ca","thal"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# save as csv
df.to_csv("heart_disease.csv", index=False)
print("Saved heart_disease.csv with shape:", df.shape)
print(df.head())