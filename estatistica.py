82
import pandas as pd
from pathlib import Path

PASTA = Path(__file__).parent
ARQUIVO = PASTA / "dados.csv"
SAIDA = PASTA / "relatorio_estatistico.txt"


def main():
    if not ARQUIVO.exists():
        dados = pd.DataFrame({
            "vendas": [120, 150, 180, 200, 175, 220, 190, 250, 210, 230],
            "quantidade": [2, 3, 4, 5, 3, 6, 4, 7, 5, 6],
            "avaliacao": [4, 5, 3, 5, 4, 5, 4, 5, 3, 4],
        })
        dados.to_csv(ARQUIVO, index=False)
        print(f"Arquivo de exemplo criado: {ARQUIVO.name}")

    dados = pd.read_csv(ARQUIVO)

    print("\n" + "=" * 55)
    print("PROJETO DE ESTATÍSTICA DESCRITIVA")
    print("=" * 55)

    print("\n1. PRIMEIRAS LINHAS")
    print(dados.head())

    print("\n2. DIMENSÕES DO CONJUNTO DE DADOS")
    print(f"Linhas: {dados.shape[0]}")
    print(f"Colunas: {dados.shape[1]}")

    print("\n3. TIPOS DE DADOS")
    print(dados.dtypes)

    print("\n4. VALORES AUSENTES")
    print(dados.isnull().sum())

    print("\n5. REGISTROS DUPLICADOS")
    print(f"Total: {dados.duplicated().sum()}")

    numericos = dados.select_dtypes(include="number")

    if not numericos.empty:
        print("\n6. ESTATÍSTICAS DESCRITIVAS")
        print(numericos.describe().round(2))

        print("\n7. MEDIANA")
        print(numericos.median().round(2))

        print("\n8. MODA")
        print(numericos.mode().head(1))

        print("\n9. VARIÂNCIA")
        print(numericos.var().round(2))

        print("\n10. DESVIO-PADRÃO")
        print(numericos.std().round(2))

        print("\n11. ASSIMETRIA")
        print(numericos.skew().round(2))

        print("\n12. CORRELAÇÃO")
        print(numericos.corr().round(2))

    with open(SAIDA, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO DE ESTATÍSTICA DESCRITIVA\n\n")
        arquivo.write(f"Registros: {len(dados)}\n")
        arquivo.write(f"Colunas: {len(dados.columns)}\n\n")
        arquivo.write("Valores ausentes:\n")
        arquivo.write(dados.isnull().sum().to_string())
        arquivo.write("\n\nEstatísticas descritivas:\n")
        arquivo.write(numericos.describe().round(2).to_string())

    print(f"\nRelatório salvo em: {SAIDA.name}")
    print("\nAnálise concluída com sucesso!")


if __name__ == "__main__":
    main()

cat > estatistica.py <<'PY'
from pathlib import Path
import argparse

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ==========================================================
# CONFIGURACAO
# ==========================================================

PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_DADOS = PASTA_PROJETO / "data"
PASTA_SAIDA = PASTA_PROJETO / "outputs"

ARQUIVO_EXEMPLO = PASTA_DADOS / "vendas.csv"

COLUNAS_NUMERICAS = [
    "quantidade",
    "preco_unitario",
    "custo_unitario",
    "receita",
    "custo_total",
    "lucro",
]


# ==========================================================
# 1. GERACAO DE UMA BASE DE EXEMPLO
# ==========================================================

def gerar_dados_exemplo():
    """Cria uma base ficticia para demonstrar a analise."""

    dados = {
        "data": [
            "2026-01-05", "2026-01-06", "2026-01-07",
            "2026-01-08", "2026-01-09", "2026-01-10",
            "2026-01-11", "2026-01-12", "2026-01-13",
            "2026-01-14", "2026-01-15", "2026-01-16",
            "2026-01-17", "2026-01-18", "2026-01-19",
            "2026-01-20", "2026-01-21", "2026-01-22",
            "2026-01-23", "2026-01-24",
        ],
        "produto": [
            "Notebook", "Mouse", "Teclado", "Monitor",
            "Mouse", "Notebook", "Headset", "Teclado",
            "Monitor", "Notebook", "Mouse", "Headset",
            "Teclado", "Monitor", "Notebook", "Mouse",
            "Headset", "Monitor", "Teclado", "Notebook",
        ],
        "categoria": [
            "Computadores", "Acessorios", "Acessorios",
            "Monitores", "Acessorios", "Computadores",
            "Acessorios", "Acessorios", "Monitores",
            "Computadores", "Acessorios", "Acessorios",
            "Acessorios", "Monitores", "Computadores",
            "Acessorios", "Acessorios", "Monitores",
            "Acessorios", "Computadores",
        ],
        "quantidade": [
            2, 5, 3, 2, 8, 1, 4, 6, 3, 2,
            10, 3, 5, 2, 1, 7, 4, 3, 6, 2,
        ],
        "preco_unitario": [
            3500, 80, 150, 1200, 80, 3500, 250, 150,
            1200, 3500, 80, 250, 150, 1200, 3500,
            80, 250, 1200, 150, 3500,
        ],
        "custo_unitario": [
            2800, 40, 80, 850, 40, 2800, 140, 80,
            850, 2800, 40, 140, 80, 850, 2800,
            40, 140, 850, 80, 2800,
        ],
    }

    df = pd.DataFrame(dados)
    df["data"] = pd.to_datetime(df["data"])

    df["receita"] = (
        df["quantidade"] * df["preco_unitario"]
    )

    df["custo_total"] = (
        df["quantidade"] * df["custo_unitario"]
    )

    df["lucro"] = df["receita"] - df["custo_total"]

    return df


# ==========================================================
# 2. CARREGAMENTO DOS DADOS
# ==========================================================

def carregar_dados(caminho=None):
    """Carrega um CSV informado ou utiliza a base de exemplo."""

    if caminho:
        arquivo = Path(caminho).expanduser()

        if not arquivo.is_absolute():
            arquivo = Path.cwd() / arquivo

        if not arquivo.exists():
            raise FileNotFoundError(
                f"Arquivo nao encontrado: {arquivo}"
            )

        df = pd.read_csv(arquivo)
        print(f"Arquivo carregado: {arquivo}")

    else:
        PASTA_DADOS.mkdir(parents=True, exist_ok=True)

        if ARQUIVO_EXEMPLO.exists():
            df = pd.read_csv(ARQUIVO_EXEMPLO)
            print(f"Base de exemplo carregada: {ARQUIVO_EXEMPLO}")
        else:
            df = gerar_dados_exemplo()
            df.to_csv(
                ARQUIVO_EXEMPLO,
                index=False,
                date_format="%Y-%m-%d",
            )
            print(f"Base de exemplo criada: {ARQUIVO_EXEMPLO}")

    if df.empty:
        raise ValueError("O arquivo nao possui registros.")

    if len(df.columns) == 0:
        raise ValueError("O arquivo nao possui colunas.")

    if df.columns.duplicated().any():
        raise ValueError("O arquivo possui nomes de colunas duplicados.")

    df.columns = df.columns.astype(str).str.strip()

    if any(not coluna for coluna in df.columns):
        raise ValueError("Existe uma coluna sem nome.")

    return df


# ==========================================================
# 3. QUALIDADE E LIMPEZA DOS DADOS
# ==========================================================

def analisar_qualidade(df):
    """Apresenta indicadores de qualidade da base original."""

    print("\n" + "=" * 55)
    print("QUALIDADE DOS DADOS")
    print("=" * 55)

    print(f"Quantidade de linhas: {len(df)}")
    print(f"Quantidade de colunas: {len(df.columns)}")
    print(f"Linhas duplicadas: {df.duplicated().sum()}")
    print(f"Celulas vazias: {df.isna().sum().sum()}")

    qualidade = pd.DataFrame({
        "tipo": df.dtypes.astype(str),
        "valores_ausentes": df.isna().sum(),
        "percentual_ausente": (
            df.isna().mean() * 100
        ).round(2),
        "valores_unicos": df.nunique(),
    })

    print("\nDetalhamento por coluna:")
    print(qualidade.to_string())

    qualidade.to_csv(
        PASTA_SAIDA / "qualidade_dados.csv",
        index=True,
        index_label="coluna",
    )


def limpar_dados(df):
    """Remove duplicatas e trata valores ausentes."""

    df = df.copy()

    linhas_originais = len(df)
    duplicadas = int(df.duplicated().sum())

    df = df.drop_duplicates()

    # Converte colunas numericas reconhecidas.
    for coluna in COLUNAS_NUMERICAS:
        if coluna in df.columns:
            df[coluna] = pd.to_numeric(
                df[coluna],
                errors="coerce",
            )

    # Tenta converter a coluna data, quando existir.
    if "data" in df.columns:
        df["data"] = pd.to_datetime(
            df["data"],
            errors="coerce",
        )

    # Ausencias numericas: mediana.
    # Ausencias textuais: categoria "Nao informado".
    for coluna in df.columns:
        if pd.api.types.is_numeric_dtype(df[coluna]):
            if df[coluna].isna().any():
                mediana = df[coluna].median()

                if pd.notna(mediana):
                    df[coluna] = df[coluna].fillna(mediana)
        else:
            if df[coluna].isna().any():
                df[coluna] = df[coluna].fillna(
                    "Nao informado"
                )

    print("\n" + "=" * 55)
    print("LIMPEZA DOS DADOS")
    print("=" * 55)
    print(f"Linhas antes da limpeza: {linhas_originais}")
    print(f"Duplicatas removidas: {duplicadas}")
    print(f"Linhas depois da limpeza: {len(df)}")
    print(f"Ausencias restantes: {df.isna().sum().sum()}")

    return df


# ==========================================================
# 4. ESTATISTICA DESCRITIVA
# ==========================================================

def calcular_estatisticas(df):
    """Calcula medidas estatisticas das colunas numericas."""

    numericos = df.select_dtypes(include="number")

    if numericos.empty:
        raise ValueError(
            "Nao existem colunas numericas para analisar."
        )

    resultados = []

    for coluna in numericos.columns:
        serie = numericos[coluna].dropna()

        if serie.empty:
            continue

        moda = serie.mode()
        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)

        resultados.append({
            "variavel": coluna,
            "quantidade": serie.count(),
            "media": serie.mean(),
            "mediana": serie.median(),
            "moda": ", ".join(map(str, moda.tolist())),
            "minimo": serie.min(),
            "maximo": serie.max(),
            "amplitude": serie.max() - serie.min(),
            "variancia": serie.var(),
            "desvio_padrao": serie.std(),
            "coeficiente_variacao_pct": (
                serie.std() / abs(serie.mean()) * 100
                if serie.mean() != 0
                else np.nan
            ),
            "primeiro_quartil": q1,
            "terceiro_quartil": q3,
            "intervalo_interquartil": q3 - q1,
            "percentil_90": serie.quantile(0.90),
            "assimetria": serie.skew(),
            "curtose": serie.kurt(),
        })

    tabela = pd.DataFrame(resultados).set_index("variavel")

    tabela.to_csv(
        PASTA_SAIDA / "estatisticas_descritivas.csv",
        float_format="%.4f",
    )

    print("\n" + "=" * 55)
    print("ESTATISTICA DESCRITIVA")
    print("=" * 55)
    print(tabela.round(2).to_string())

    return tabela


# ==========================================================
# 5. IDENTIFICACAO DE VALORES ATIPICOS
# ==========================================================

def detectar_outliers(df):
    """Identifica possiveis outliers pelo metodo do IQR."""

    resultados = []

    for coluna in df.select_dtypes(include="number").columns:
        serie = df[coluna].dropna()

        if len(serie) < 4:
            continue

        q1 = serie.quantile(0.25)
        q3 = serie.quantile(0.75)
        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        mascara = (
            (serie < limite_inferior)
            | (serie > limite_superior)
        )

        resultados.append({
            "variavel": coluna,
            "limite_inferior": limite_inferior,
            "limite_superior": limite_superior,
            "quantidade_outliers": int(mascara.sum()),
            "percentual_outliers": round(
                mascara.mean() * 100, 2
            ),
        })

    tabela = pd.DataFrame(resultados)

    if not tabela.empty:
        tabela.to_csv(
            PASTA_SAIDA / "valores_atipicos.csv",
            index=False,
        )

    print("\n" + "=" * 55)
    print("POSSIVEIS VALORES ATIPICOS")
    print("=" * 55)

    if tabela.empty:
        print("Dados insuficientes para calcular outliers.")
    else:
        print(tabela.round(2).to_string(index=False))

    return tabela


# ==========================================================
# 6. ANALISE POR CATEGORIA
# ==========================================================

def analisar_categorias(df):
    """Resume receita e lucro por categoria, quando disponiveis."""

    colunas = {"categoria", "receita"}

    if not colunas.issubset(df.columns):
        return None

    agregacoes = {
        "receita": ("receita", "sum"),
    }

    if "lucro" in df.columns:
        agregacoes["lucro"] = ("lucro", "sum")

    if "quantidade" in df.columns:
        agregacoes["quantidade"] = ("quantidade", "sum")

    resumo = (
        df.groupby("categoria", dropna=False)
        .agg(**agregacoes)
        .sort_values("receita", ascending=False)
    )

    resumo.to_csv(PASTA_SAIDA / "resumo_por_categoria.csv")

    print("\n" + "=" * 55)
    print("RESUMO POR CATEGORIA")
    print("=" * 55)
    print(resumo.round(2).to_string())

    return resumo


# ==========================================================
# 7. VISUALIZACOES
# ==========================================================

def gerar_graficos(df):
    """Salva graficos estatisticos na pasta outputs."""

    numericos = df.select_dtypes(include="number")

    if numericos.empty:
        print("\nSem dados numericos para gerar graficos.")
        return

    # Histogramas e boxplots.
    for coluna in numericos.columns:
        serie = numericos[coluna].dropna()

        if serie.empty:
            continue

        fig, eixos = plt.subplots(1, 2, figsize=(12, 4))

        eixos[0].hist(
            serie,
            bins="auto",
            edgecolor="black",
        )
        eixos[0].set_title(f"Distribuicao: {coluna}")
        eixos[0].set_xlabel(coluna)
        eixos[0].set_ylabel("Frequencia")

        eixos[1].boxplot(serie, vert=True)
        eixos[1].set_title(f"Boxplot: {coluna}")
        eixos[1].set_ylabel(coluna)

        fig.tight_layout()
        nome = "".join(
            caractere if caractere.isalnum() else "_"
            for caractere in coluna
        )

        fig.savefig(
            PASTA_SAIDA / f"distribuicao_{nome}.png",
            dpi=150,
            bbox_inches="tight",
        )
        plt.close(fig)

    # Matriz de correlacao.
    if numericos.shape[1] >= 2:
        correlacao = numericos.corr()

        correlacao.to_csv(
            PASTA_SAIDA / "matriz_correlacao.csv"
        )

        fig, ax = plt.subplots(
            figsize=(
                max(7, len(correlacao.columns)),
                max(5, len(correlacao.columns) * 0.7),
            )
        )

        imagem = ax.imshow(
            correlacao,
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
        )

        ax.set_xticks(range(len(correlacao.columns)))
        ax.set_yticks(range(len(correlacao.index)))
        ax.set_xticklabels(
            correlacao.columns,
            rotation=45,
            ha="right",
        )
        ax.set_yticklabels(correlacao.index)

        for i in range(len(correlacao.index)):
            for j in range(len(correlacao.columns)):
                valor = correlacao.iloc[i, j]

                if pd.notna(valor):
                    ax.text(
                        j, i, f"{valor:.2f}",
                        ha="center",
                        va="center",
                        fontsize=8,
                    )

        ax.set_title("Matriz de correlacao")
        fig.colorbar(imagem, ax=ax, label="Correlacao")
        fig.tight_layout()
        fig.savefig(
            PASTA_SAIDA / "matriz_correlacao.png",
            dpi=150,
            bbox_inches="tight",
        )
        plt.close(fig)

    # Receita por categoria.
    if {"categoria", "receita"}.issubset(df.columns):
        receita_categoria = (
            df.groupby("categoria")["receita"]
            .sum()
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(9, 5))
        receita_categoria.plot(
            kind="bar",
            ax=ax,
            edgecolor="black",
        )

        ax.set_title("Receita total por categoria")
        ax.set_xlabel("Categoria")
        ax.set_ylabel("Receita")
        ax.tick_params(axis="x", rotation=30)

        fig.tight_layout()
        fig.savefig(
            PASTA_SAIDA / "receita_por_categoria.png",
            dpi=150,
            bbox_inches="tight",
        )
        plt.close(fig)

    print(f"\nGraficos salvos em: {PASTA_SAIDA}")


# ==========================================================
# 8. RELATORIO FINAL
# ==========================================================

def gerar_relatorio(df, estatisticas, outliers):
    """Cria um relatorio textual com os principais resultados."""

    linhas = [
        "RELATORIO DE ANALISE ESTATISTICA",
        "=" * 40,
        f"Registros analisados: {len(df)}",
        f"Colunas analisadas: {len(df.columns)}",
        f"Valores ausentes restantes: {df.isna().sum().sum()}",
        "",
        "ESTATISTICAS DESCRITIVAS",
        "-" * 40,
        estatisticas.round(2).to_string(),
        "",
        "VALORES ATIPICOS",
        "-" * 40,
    ]

    if outliers is not None and not outliers.empty:
        linhas.append(outliers.round(2).to_string(index=False))
    else:
        linhas.append("Nenhum resultado disponivel.")

    if "receita" in df.columns:
        linhas.extend([
            "",
            "INDICADORES DE RECEITA",
            "-" * 40,
            f"Receita total: R$ {df['receita'].sum():,.2f}",
            f"Receita media: R$ {df['receita'].mean():,.2f}",
            f"Maior receita por registro: R$ {df['receita'].max():,.2f}",
        ])

    if "lucro" in df.columns:
        linhas.append(
            f"Lucro total: R$ {df['lucro'].sum():,.2f}"
        )

    caminho = PASTA_SAIDA / "relatorio_estatistico.txt"
    caminho.write_text("\n".join(linhas), encoding="utf-8")

    print(f"\nRelatorio salvo em: {caminho}")


# ==========================================================
# 9. EXECUCAO PRINCIPAL
# ==========================================================

def main():
    parser = argparse.ArgumentParser(
        description="Projeto de estatistica descritiva com Python."
    )
    parser.add_argument(
        "--arquivo",
        help="Caminho de um arquivo CSV para analisar.",
    )
    args = parser.parse_args()

    PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

    df_original = carregar_dados(args.arquivo)

    analisar_qualidade(df_original)

    df_limpo = limpar_dados(df_original)

    df_limpo.to_csv(
        PASTA_SAIDA / "dados_limpos.csv",
        index=False,
        date_format="%Y-%m-%d",
    )

    estatisticas = calcular_estatisticas(df_limpo)
    outliers = detectar_outliers(df_limpo)

    analisar_categorias(df_limpo)
    gerar_graficos(df_limpo)
    gerar_relatorio(df_limpo, estatisticas, outliers)

    print("\n" + "=" * 55)
    print("ANALISE CONCLUIDA COM SUCESSO!")
    print(f"Resultados disponiveis em: {PASTA_SAIDA}")
    print("=" * 55)


if __name__ == "__main__":
    main()
PY
