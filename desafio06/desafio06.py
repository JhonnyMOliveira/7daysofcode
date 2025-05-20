# Script oficial do Desafio 06 - 7DaysOfCode | Python & Pandas (Alura)
# Objetivo: Calcular a quantidade de empréstimos realizados entre 2015 e 2020 
# por curso de graduação a partir de diferentes fontes de dados (Excel + JSON)

from pathlib import Path
import pandas as pd
import json

# === 1. Criação da estrutura de diretórios ===
pasta_dados = Path('dados')
pasta_dados.mkdir(parents=True, exist_ok=True)

# === 2. Leitura dos arquivos ===
# Excel
df_excel = pd.read_excel('dados/matricula_alunos.xlsx', skiprows=1)
df_excel.columns = ['matricula_ou_siape', 'tipo_vinculo_usuario', 'curso']
df_excel['matricula_ou_siape'] = df_excel['matricula_ou_siape'].astype(str)

# JSON
with open('dados/cadastro_alunos.json', 'r', encoding='utf-8') as f:
    dados_json = json.load(f)

lista_dataframes = []
for item in dados_json:
    registros_str = item['registros']
    registros_list = json.loads(registros_str)
    temp_df = pd.DataFrame(registros_list)
    lista_dataframes.append(temp_df)

df_json = pd.concat(lista_dataframes, ignore_index=True)
df_json['matricula_ou_siape'] = df_json['matricula_ou_siape'].astype(str)

# === 3. Unificação das duas bases de alunos ===
df_alunos = pd.concat([df_excel, df_json], ignore_index=True)

# === 4. Filtragem por cursos de interesse e tipo de vínculo ===
cursos_interesse = [
    'BIBLIOTECONOMIA',
    'CIÊNCIAS SOCIAIS',
    'COMUNICAÇÃO SOCIAL',
    'DIREITO',
    'FILOSOFIA',
    'PEDAGOGIA'
]
df_alunos['curso'] = df_alunos['curso'].str.upper()

df_graduacao = df_alunos[
    (df_alunos['tipo_vinculo_usuario'] == 'ALUNO DE GRADUAÇÃO') &
    (df_alunos['curso'].isin(cursos_interesse))
]

# === 5. Importação do dataset de empréstimos ===
df = pd.read_csv('../desafio04/dataset_completo.csv')
df['matricula_ou_siape'] = df['matricula_ou_siape'].astype(str)

# === 6. Mesclagem e filtragem final ===
df_merged = pd.merge(df, df_graduacao, on='matricula_ou_siape', how='inner')
df_merged['ano'] = pd.to_datetime(df_merged['data_emprestimo']).dt.year
df_filtrado = df_merged[(df_merged['ano'] >= 2015) & (df_merged['ano'] <= 2020)]

# === 7. Tabela cruzada com totais ===
tabela = pd.pivot_table(
    df_filtrado,
    index='curso',
    columns='ano',
    values='id_emprestimo',
    aggfunc='count',
    fill_value=0,
    margins=True,
    margins_name='Total'
)

# === 8. Exportação da tabela para CSV (opcional) ===
tabela.to_csv('dados/emprestimos_por_curso.csv')