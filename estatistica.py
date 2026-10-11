
import pandas as pd

# Base de dados de vendas
dados = {
    "venda": [100, 200, 200, 300, 700]
}

df = pd.DataFrame(dados)

# Estatística descritiva
print("RESUMO ESTATÍSTICO")
print(df["venda"].describe())

print("\nMédia:", df["venda"].mean())
print("Mediana:", df["venda"].median())
print("Moda:", df["venda"].mode().tolist())
print("Amplitude:", df["venda"].max() - df["venda"].min())
print("Variância:", df["venda"].var())
print("Desvio padrão:", df["venda"].std())
