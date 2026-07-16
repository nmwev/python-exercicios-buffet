import pandas as pd

cat = pd.read_csv("salgados_semana.csv")

# Filtra por tipo para pedidos em fornecedores separados
frito = cat[cat["tipo"] == "frito"]
assado = cat[cat["tipo"] == "assado"]

print("=== FRITOS ===")
print(frito.groupby("item")["quantidade"].sum())

print("=== ASSADOS ===")
print(assado.groupby("item")["quantidade"].sum())