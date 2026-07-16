import pandas as pd

df = pd.read_csv("eventos.csv")
df_premium = df[df["categoria"] == "premium"]
print(df.shape)
print(df.columns)
print(df.head(3))
print(df.groupby("categoria")["valor"].sum())