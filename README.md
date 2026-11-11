# Análise Estatística Descritiva com Python
### Descriptive Statistical Analysis with Python

🇧🇷 Português | 🇺🇸 English

---

## 🇧🇷 Português

### Sobre o projeto

Projeto de análise estatística descritiva desenvolvido em Python, com foco na exploração, organização e interpretação de dados de vendas.

A aplicação utiliza bibliotecas de análise e visualização de dados para calcular métricas estatísticas, identificar possíveis problemas na qualidade dos dados, analisar correlações e gerar gráficos e relatórios automaticamente.

O projeto faz parte do meu portfólio de estudos em Análise de Dados e Ciência de Dados.

### Funcionalidades

- Leitura e processamento de arquivos CSV.
- Análise exploratória dos dados.
- Verificação da estrutura e dos tipos de dados.
- Identificação de valores ausentes e registros duplicados.
- Avaliação da qualidade dos dados.
- Cálculo de estatísticas descritivas.
- Cálculo de média, mediana e moda.
- Cálculo de variância e desvio-padrão.
- Análise de distribuição e assimetria.
- Identificação de valores atípicos (outliers).
- Cálculo e visualização da matriz de correlação.
- Análise de receita por categoria.
- Geração automática de gráficos e relatórios.

### Estatísticas analisadas

| Métrica | Descrição |
|---|---|
| Média | Valor médio dos dados |
| Mediana | Valor central dos dados ordenados |
| Moda | Valor mais frequente |
| Variância | Medida de dispersão |
| Desvio-padrão | Dispersão em relação à média |
| Assimetria | Distribuição dos valores em relação à média |
| Correlação | Relação entre variáveis numéricas |
| Outliers | Identificação de valores atípicos |

### Visualizações geradas

O projeto gera gráficos para facilitar a interpretação dos dados:

- Distribuição do custo unitário.
- Distribuição do lucro.
- Distribuição do preço unitário.
- Distribuição da quantidade.
- Distribuição da receita.
- Matriz de correlação.
- Receita por categoria.

### Relatórios gerados

Os resultados da análise são exportados automaticamente para a pasta `outputs/`.

| Arquivo | Descrição |
|---|---|
| `estatisticas_descritivas.csv` | Métricas estatísticas |
| `matriz_correlacao.csv` | Correlação entre variáveis |
| `qualidade_dados.csv` | Indicadores de qualidade |
| `valores_atipicos.csv` | Valores identificados como atípicos |
| `resumo_por_categoria.csv` | Resumo dos dados por categoria |
| `relatorio_estatistico.txt` | Relatório textual da análise |

### Tecnologias utilizadas

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- CSV
- Git e GitHub

### Estrutura do projeto

```text
estatistica_descritiva/
│
├── data/
│   └── vendas.csv
│
├── outputs/
│   ├── distribuicao_custo_unitario.png
│   ├── distribuicao_lucro.png
│   ├── distribuicao_preco_unitario.png
│   ├── distribuicao_quantidade.png
│   ├── distribuicao_receita.png
│   ├── estatisticas_descritivas.csv
│   ├── matriz_correlacao.csv
│   ├── matriz_correlacao.png
│   ├── qualidade_dados.csv
│   ├── receita_por_categoria.png
│   ├── relatorio_estatistico.txt
│   ├── resumo_por_categoria.csv
│   └── valores_atipicos.csv
│
├── estatistica.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Como executar

Clone o repositório:

```bash
git clone https://github.com/vitor1914/estatistica_descritiva.git
```

Entre na pasta:

```bash
cd estatistica_descritiva
```

Crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python estatistica.py
```

Os resultados serão gerados na pasta `outputs/`.

---

## 🇺🇸 English

### About the project

A descriptive statistical analysis project developed in Python, focused on exploring, organizing, and interpreting sales data.

The application uses data analysis and visualization libraries to calculate statistical metrics, identify potential data quality issues, analyze correlations, and automatically generate charts and reports.

This project is part of my Data Analytics and Data Science learning portfolio.

### Features

- CSV file reading and processing.
- Exploratory data analysis.
- Data structure and data type inspection.
- Missing values and duplicate records detection.
- Data quality assessment.
- Descriptive statistical calculations.
- Mean, median, and mode calculations.
- Variance and standard deviation calculations.
- Skewness and distribution analysis.
- Outlier detection.
- Correlation matrix calculation and visualization.
- Revenue analysis by category.
- Automatic chart and report generation.

### Technologies

- Python 3.12
- Pandas
- NumPy
- Matplotlib
- CSV
- Git and GitHub

### Project structure

The project organizes input data in the `data/` directory and stores generated charts, statistical summaries, and reports in the `outputs/` directory.

### Execution

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python estatistica.py
```

Generated results are saved in the `outputs/` directory.

---

## Autor | Author

**Israel Vitor**

- GitHub: [@vitor1914](https://github.com/vitor1914)
- Portfolio: [View Portfolio](https://vitor1914.github.io/meu-portfolio/)