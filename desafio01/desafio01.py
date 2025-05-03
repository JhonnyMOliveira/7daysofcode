# desafio01.py

import os
import pandas as pd

# Definir o caminho base da pasta de dados
caminho_base = os.path.join("..", "dados")

# Verificar se o diretório existe
if not os.path.exists(caminho_base):
    raise FileNotFoundError(f"Pasta de dados não encontrada em: {caminho_base}")

# Listar todos os arquivos da pasta
arquivos = os.listdir(caminho_base)

# Verificar quais arquivos estão presentes
print("Arquivos encontrados na pasta dados:", arquivos)

# Inicializar os DataFrames como None
df_emprestimos = None
df_exemplares = None

# Verificar e carregar os dados de empréstimos
if "emprestimos.csv" in arquivos:
    df_emprestimos = pd.read_csv(os.path.join(caminho_base, "emprestimos.csv"))
elif "emprestimos.parquet" in arquivos:
    df_emprestimos = pd.read_parquet(os.path.join(caminho_base, "emprestimos.parquet"))
else:
    raise FileNotFoundError("Arquivo de empréstimos não encontrado (CSV ou Parquet).")

# Verificar e carregar os dados de exemplares
if "exemplares.csv" in arquivos:
    df_exemplares = pd.read_csv(os.path.join(caminho_base, "exemplares.csv"))
elif "exemplares.parquet" in arquivos:
    df_exemplares = pd.read_parquet(os.path.join(caminho_base, "exemplares.parquet"))
else:
    raise FileNotFoundError("Arquivo de exemplares não encontrado (CSV ou Parquet).")

# Verificar se os DataFrames foram carregados corretamente
if df_emprestimos is None or df_exemplares is None:
    raise ValueError("Erro ao carregar os dados.")

# Unir os DataFrames pelo campo 'codigo_exemplar'
df = pd.merge(df_emprestimos, df_exemplares, on="codigo_exemplar", how="inner")

# Exibir as primeiras linhas do DataFrame unificado
print("DataFrame unificado:")
print(df.head())
