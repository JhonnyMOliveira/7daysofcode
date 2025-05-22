# Script oficial do Desafio 07 - 7DaysOfCode | Python & Pandas (Alura)
# Objetivo: Analisar a evolução percentual de empréstimos por curso de pós-graduação
# entre os anos de 2017, 2018, 2019 e 2022 para apoiar a diretoria da biblioteca.

import pandas as pd
from pathlib import Path

def process_data_for_post_grad_loans(
    alunos_path: str = 'dados/df_alunos.csv',
    emprestimos_path: str = '../desafio04/dataset_completo.csv'
) -> pd.DataFrame:
    """
    Processa os dados para calcular a evolução percentual de empréstimos
    para cursos de pós-graduação entre anos específicos.

    Args:
        alunos_path (str): Caminho para o arquivo CSV de alunos.
        emprestimos_path (str): Caminho para o arquivo CSV de empréstimos.

    Returns:
        pd.DataFrame: DataFrame contendo a evolução percentual de empréstimos
                      por curso de pós-graduação e ano.
    """
    # 1. Carregar os datasets
    try:
        df_alunos = pd.read_csv(alunos_path)
        df_emprestimos = pd.read_csv(emprestimos_path)
    except FileNotFoundError as e:
        print(f"Erro: Arquivo não encontrado. Verifique os caminhos. {e}")
        return pd.DataFrame()

    # Garantir que as colunas de merge sejam strings
    df_alunos['matricula_ou_siape'] = df_alunos['matricula_ou_siape'].astype(str)
    df_emprestimos['matricula_ou_siape'] = df_emprestimos['matricula_ou_siape'].astype(str)

    # 2. Filtrar alunos de pós-graduação
    df_pos_grad = df_alunos[df_alunos['tipo_vinculo_usuario'] == 'ALUNO DE PÓS-GRADUAÇÃO'].copy()

    # 3. Realizar o merge com os empréstimos
    # O suffix '_alunos' é adicionado para evitar colunas duplicadas
    df_merged = pd.merge(df_emprestimos, df_pos_grad, on='matricula_ou_siape', how='inner')

    # 4. Converter a coluna 'data_emprestimo' para datetime e extrair o ano
    df_merged['data_emprestimo'] = pd.to_datetime(df_merged['data_emprestimo'])
    df_merged['ano_emprestimo'] = df_merged['data_emprestimo'].dt.year

    # 5. Considerar apenas os anos de interesse: 2017, 2018, 2019 e 2022
    anos_interesse = [2017, 2018, 2019, 2022]
    df_filtrado_anos = df_merged[df_merged['ano_emprestimo'].isin(anos_interesse)].copy()

    # 6. Agrupar por curso e ano para contar o número de empréstimos
    df_contagem_emprestimos = df_filtrado_anos.groupby(['curso', 'ano_emprestimo']).size().reset_index(name='total_emprestimos')

    # 7. Pivotar a tabela para ter anos como colunas
    df_pivot = df_contagem_emprestimos.pivot(index='curso', columns='ano_emprestimo', values='total_emprestimos').fillna(0)

    # 8. Calcular a evolução percentual
    # Para 2018 em relação a 2017
    df_pivot['percentual_2018_vs_2017'] = ((df_pivot[2018] - df_pivot[2017]) / df_pivot[2017] * 100).round(2).fillna(0)
    df_pivot['percentual_2018_vs_2017'] = df_pivot['percentual_2018_vs_2017'].replace([float('inf'), -float('inf')], 0)

    # Para 2019 em relação a 2018
    df_pivot['percentual_2019_vs_2018'] = ((df_pivot[2019] - df_pivot[2018]) / df_pivot[2018] * 100).round(2).fillna(0)
    df_pivot['percentual_2019_vs_2018'] = df_pivot['percentual_2019_vs_2018'].replace([float('inf'), -float('inf')], 0)

    # Para 2022 em relação a 2019
    df_pivot['percentual_2022_vs_2019'] = ((df_pivot[2022] - df_pivot[2019]) / df_pivot[2019] * 100).round(2).fillna(0)
    df_pivot['percentual_2022_vs_2019'] = df_pivot['percentual_2022_vs_2019'].replace([float('inf'), -float('inf')], 0)

    # Reordenar colunas para melhor visualização
    colunas_finais = [
        2017, 2018, 'percentual_2018_vs_2017',
        2019, 'percentual_2019_vs_2018',
        2022, 'percentual_2022_vs_2019'
    ]
    df_resultado = df_pivot[colunas_finais].reset_index()
    df_resultado.rename(columns={
        2017: 'emprestimos_2017',
        2018: 'emprestimos_2018',
        2019: 'emprestimos_2019',
        2022: 'emprestimos_2022'
    }, inplace=True)

    return df_resultado

def style_dataframe_for_html(df: pd.DataFrame) -> str:
    """
    Aplica estilos ao DataFrame para exportação HTML.
    Cores para percentuais positivos e negativos e fundo alternado para linhas.
    """
    def color_negative_red(val):
        color = 'red' if val < 0 else 'green' if val > 0 else 'black'
        return f'color: {color}'

    styled_df = df.style.applymap(color_negative_red, subset=[
        'percentual_2018_vs_2017',
        'percentual_2019_vs_2018',
        'percentual_2022_vs_2019'
    ]).set_properties(**{'background-color': '#f8f8f8'}, subset=pd.IndexSlice[1::2, :]) # Linhas pares com fundo claro
    return styled_df.to_html(index=False)

def export_to_html_report(df_analysis: pd.DataFrame, output_path: str = 'relatorio_pos_graduacao.html'):
    """
    Exporta o DataFrame de análise para um arquivo HTML com um relatório completo.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relatório de Empréstimos - Pós-Graduação</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background-color: #f4f7f6; color: #333; }}
            .container {{ max-width: 1200px; margin: auto; background-color: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; text-align: center; margin-bottom: 30px; }}
            h2 {{ color: #34495e; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; margin-top: 40px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #e0e6ea; color: #333; font-weight: bold; }}
            tr:nth-child(even) {{ background-color: #f8f8f8; }}
            .positive {{ color: green; font-weight: bold; }}
            .negative {{ color: red; font-weight: bold; }}
            .neutral {{ color: black; }}
            ul {{ list-style-type: disc; margin-left: 20px; }}
            li {{ margin-bottom: 8px; }}
            .footer {{ text-align: center; margin-top: 50px; font-size: 0.9em; color: #7f8c8d; }}
            .dataframe tbody tr th {{ background-color: #e0e6ea; }} /* Estilo para o cabeçalho das linhas no dataframe */
            .dataframe {{ border: none !important; }}
            .dataframe thead th {{ border-bottom: 2px solid #ccc; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Relatório de Evolução de Empréstimos - Pós-Graduação</h1>
            <p>Este relatório apresenta a evolução percentual dos empréstimos realizados por alunos de pós-graduação entre os anos de 2017, 2018, 2019 e 2022.</p>

            <h2>Dados da Evolução Percentual</h2>
            {style_dataframe_for_html(df_analysis)}

            <h2>Análise da Diretoria</h2>
            <h3>💡 Possíveis Interpretações</h3>
            <ul>
                <li>A queda brusca de 2019 para 2022 pode estar fortemente associada aos efeitos da pandemia da COVID-19, que alterou a dinâmica de ensino, restringiu o acesso físico à biblioteca e incentivou o uso de materiais digitais.</li>
                <li>Cursos que apresentaram resiliência ou crescimento podem estar mais conectados a áreas com forte base tecnológica ou acesso remoto a conteúdo digital.</li>
            </ul>

            <h3>🎯 Recomendações para a Diretoria</h3>
            <ul>
                <li>Reforçar ações de incentivo à retomada do uso do acervo físico, especialmente nos cursos que sofreram maiores quedas.</li>
                <li>Investir em marketing direcionado para os cursos que mostraram resiliência, utilizando-os como referência de boas práticas.</li>
                <li>Investigar internamente os fatores que levaram ao crescimento de alguns cursos (ex: Bioinformática) e avaliar a replicabilidade dessas estratégias.</li>
                <li>Considerar parcerias com docentes e coordenações de curso para promover formações sobre o uso estratégico da biblioteca.</li>
            </ul>

            <div class="footer">
                <p>Relatório gerado em: {pd.Timestamp.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
                <p>&copy; 7DaysOfCode - Python & Pandas (Alura)</p>
            </div>
        </div>
    </body>
    </html>
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"\nRelatório HTML '{output_path}' gerado com sucesso!")
    except IOError as e:
        print(f"Erro ao salvar o arquivo HTML: {e}")


if __name__ == "__main__":
    # Caminhos para os arquivos de dados. Ajuste se necessário.
    # Criar pasta 'dados' se não existir
    pasta_dados = Path('dados')
    pasta_dados.mkdir(parents=True, exist_ok=True)

    alunos_file_path = 'dados/df_alunos.csv'
    emprestimos_file_path = '../desafio04/dataset_completo.csv'

    # Processar os dados
    df_final = process_data_for_post_grad_loans(alunos_file_path, emprestimos_file_path)

    if not df_final.empty:
        # Exportar para HTML
        export_to_html_report(df_final, 'relatorio_emprestimos_pos_graduacao.html')
    else:
        print("Não foi possível gerar o relatório HTML devido à falta de dados processados.")