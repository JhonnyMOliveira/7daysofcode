import pandas as pd

# Realizando o Import do DataSet
dataset_completo = pd.read_csv('../desafio04/dataset_completo.csv')

def gerar_tabela(df, coluna):
    """
    Gera uma tabela de frequência absoluta e relativa (percentual)
    para uma coluna categórica.
    
    Parâmetros:
    - df: DataFrame
    - coluna: nome da coluna (string)
    
    Retorna:
    - DataFrame com contagem e percentual
    """

    freq = df[coluna].value_counts(dropna=False)
    percentual = df[coluna].value_counts(normalize=True, dropna=False) * 100
    tabela = pd.concat([freq, percentual.round(2)], axis=1)

    return tabela

# Chamadas para variáveis categóricas analisadas
tabela_vinculo = gerar_tabela(dataset_completo, 'tipo_vinculo_usuario')
tabela_colecao = gerar_tabela(dataset_completo, 'colecao')
tabela_biblioteca = gerar_tabela(dataset_completo, 'biblioteca')
tabela_cdu = gerar_tabela(dataset_completo, 'classe_cdu')

# Exibindo os resultados
print("\nDistribuição por Tipo de Vínculo:\n", tabela_vinculo)
print("\nDistribuição por Coleção:\n", tabela_colecao)
print("\nDistribuição por Biblioteca:\n", tabela_biblioteca)
print("\nDistribuição por Classificação CDU:\n", tabela_cdu)
