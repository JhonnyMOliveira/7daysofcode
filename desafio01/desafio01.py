# desafio01.py

import pandas as pd
import requests
import glob
from pathlib import Path

# ----------------------------
# Instalação (caso necessário):
# pip install pandas pyarrow
# ----------------------------

def criar_pastas():
    """Cria diretórios para armazenar os arquivos"""
    Path("dados/emprestimos").mkdir(parents=True, exist_ok=True)
    Path("dados/exemplares").mkdir(parents=True, exist_ok=True)

def baixar_arquivos_emprestimos():
    """Baixa os arquivos CSV de empréstimos por ano e semestre"""
    lista_emprestimos = [f'{ano}{sem}' for ano in range(2010, 2021) for sem in [1, 2] if not (ano == 2020 and sem == 2)]
    
    for ano in lista_emprestimos:
        url = f"https://raw.githubusercontent.com/franciscofoz/7_Days_of_Code_Alura-Python-Pandas/main/Dia_1-Importando_dados/Datasets/dados_emprestimos/emprestimos-{ano}.csv"
        r = requests.get(url)
        with open(f"dados/emprestimos/emprestimos-{ano}.csv", "wb") as f:
            f.write(r.content)

def baixar_arquivo_acervo():
    """Baixa o arquivo .parquet com os dados do acervo"""
    url = "https://github.com/franciscofoz/7_Days_of_Code_Alura-Python-Pandas/raw/main/Dia_1-Importando_dados/Datasets/dados_exemplares.parquet"
    r = requests.get(url)
    with open("dados/exemplares/dados_exemplares.parquet", "wb") as f:
        f.write(r.content)

def carregar_e_concatenar_csvs():
    """Lê e concatena todos os arquivos CSV da pasta empréstimos"""
    caminhos_csv = glob.glob("dados/emprestimos/*.csv")
    dataframes = []
    for caminho in caminhos_csv:
        try:
            df = pd.read_csv(caminho, sep=',', encoding='utf-8')
            dataframes.append(df)
        except Exception as e:
            print(f"Erro ao ler {caminho}: {e}")
    
    if not dataframes:
        raise ValueError("Nenhum arquivo CSV foi carregado corretamente.")
    return pd.concat(dataframes, ignore_index=True)

def tratar_dados_emprestimos(df):
    """Limpa e trata os dados do DataFrame de empréstimos"""
    df = df.drop_duplicates()
    
    # Converte colunas de datas
    df['data_devolucao'] = pd.to_datetime(df['data_devolucao'], errors='coerce')
    df['data_emprestimo'] = pd.to_datetime(df['data_emprestimo'], errors='coerce')
    df['data_renovacao'] = pd.to_datetime(df['data_renovacao'], errors='coerce')

    return df

def carregar_acervo():
    """Lê o arquivo de acervo em formato parquet"""
    return pd.read_parquet('dados/exemplares/dados_exemplares.parquet')

def mesclar_dados(df_emprestimos, df_acervo):
    """Realiza a junção dos dados de empréstimos com os de acervo"""
    df_completo = pd.merge(df_emprestimos, df_acervo, on='codigo_barras', how='left')

    faltando = df_completo['id_exemplar'].isnull().sum()
    percentual = (faltando / len(df_completo)) * 100
    print(f"Linhas sem correspondência no acervo: {faltando} ({percentual:.2f}%)")

    return df_completo

def main():
    print(">>> Iniciando o desafio 01...")
    criar_pastas()
    baixar_arquivos_emprestimos()
    baixar_arquivo_acervo()
    
    df_emprestimos = carregar_e_concatenar_csvs()
    df_emprestimos = tratar_dados_emprestimos(df_emprestimos)

    df_acervo = carregar_acervo()
    df_completo = mesclar_dados(df_emprestimos, df_acervo)

    # Exporta o resultado final como Parquet (opcional)
    df_completo.to_parquet("dados/df_completo.parquet", index=False)
    print(">>> Desafio 01 finalizado com sucesso!")

if __name__ == "__main__":
    main()