import pandas as pd

# Carregando o DataFrame do desafio01
df = pd.read_csv('../desafio02/dataset_completo.csv')

# Remoção da coluna desnecessária
df = df.drop(columns=['registro_sistema'])

# Conversão da coluna de matrícula para string
df['matricula_ou_siape'] = df['matricula_ou_siape'].astype(str)

# Padronização da coluna 'localizacao' como inteiro
df['localizacao'] = df['localizacao'].fillna(0).astype(float).astype(int)

# Função de classificação CDU
def classificar_cdu(valor):
    try:
        valor = int(str(valor).strip())
        if 0 <= valor <= 99:
            return 'Generalidades. Ciência e conhecimento'
        elif 100 <= valor <= 199:
            return 'Filosofia e psicologia'
        elif 200 <= valor <= 299:
            return 'Religião'
        elif 300 <= valor <= 399:
            return 'Ciências sociais'
        elif 400 <= valor <= 499:
            return 'Classe vaga'
        elif 500 <= valor <= 599:
            return 'Matemática e ciências naturais'
        elif 600 <= valor <= 699:
            return 'Ciências aplicadas'
        elif 700 <= valor <= 799:
            return 'Belas artes'
        elif 800 <= valor <= 899:
            return 'Linguagem. Língua. Linguística'
        elif 900 <= valor <= 999:
            return 'Geografia. Biografia. História'
        else:
            return 'Código fora da faixa CDU'
    except:
        return 'Valor inválido'

# Aplicação da função para criar nova coluna
df['classe_cdu'] = df['localizacao'].apply(classificar_cdu)

# Exportando o novo DataFrame para o próximo desafio
df.to_csv('../desafio03/dataset_completo.csv', index=False)