"""Infografico CPA/UNIFEI - Grupo 3 (docentes).
Gera infografico_cpa.png e infografico_cpa.pdf (A4).

COMO USAR
1) Os dados vem da pasta dados/ (planilhas enviadas pela CPA, ver dados/dicionario.md).
2) Os graficos sao calculados direto das planilhas. Os textos ficam no bloco
   "EDITE AQUI": se os dados mudarem, confira se os numeros citados batem com
   o resumo que o script imprime no terminal.
3) Rode:  python infografico_cpa.py
"""
import os
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyBboxPatch, Rectangle

PASTA = os.path.dirname(os.path.abspath(__file__))
DADOS = os.path.join(PASTA, "Dados")

# ============================ EDITE AQUI ============================
TITULO = (
    "Só 147 docentes responderam à CPA em 2025.2, 31% a menos.\n"
    "82% de quem respondeu diz usar os resultados para melhorar"
)
SUBTITULO = ("Autoavaliação institucional da UNIFEI, exigida pelo SINAES "
             "(Lei 10.861/2004) | Público: docentes")

SECAO1 = "1. Menos docentes estão sendo ouvidos"
NOTA1 = ("Em Itajubá, os respondentes caíram de 159 para 93 (-42%). "
         "Em Itabira, ficaram estáveis (55 para 54).")

SECAO2 = "2. Quem responde usa os resultados: a concordância subiu de 67% para 82%"
PERGUNTA2 = ("\"Tenho acesso aos resultados das avaliações institucionais e realizo "
             "ações de melhorias na minha prática profissional\" (docentes)")
NOTA2 = ("Autodeclaração de quem respondeu: não mede o efeito da CPA nem representa "
         "os docentes que não participaram.")

SECAO3 = "3. Mas só metade dos estudantes percebe essas melhorias"
PERGUNTA3 = ("dos estudantes concordam que \"a instituição utiliza os resultados das "
             "avaliações internas (CPA) e externas (MEC) para promover melhorias\" "
             "(2025.2). 37% ficaram neutros.")
NOTA3 = ("E eles avaliam vocês: em 2025.2, estudantes deram notas a 484 turmas "
         "(média 8,5 de 10). Esse retorno só chega à sua prática se você o consulta.")

ACAO_TITULO = "O que fazer agora"
ACAO_LINHAS = [
    "1. Responda à CPA no SIGAA neste semestre: sua visão entra no relatório do campus.",
    "2. Consulte os resultados e as notas das suas turmas e leve os pontos ao colegiado.",
    "3. Conte aos alunos o que mudou a partir da avaliação: é isso que fecha o ciclo.",
]

FONTES = ("Fonte: CPA/UNIFEI, Avaliação Institucional 2024.2 a 2025.2, respostas agregadas "
          "de discentes e docentes dos campi Itajubá, Itabira e EaD (participacao.xlsx, "
          "respostas_alternativas.xlsx, respostas_notas.xlsx). Os semestres anteriores não "
          "constam na base. O total de docentes da UNIFEI não consta na base: por isso a "
          "participação aparece em número de respondentes, e não em %. \"Concordam\" = "
          "Concordo totalmente + Concordo.")
# ====================================================================

ACCENT = "#0B5563"
GRAY = "#9AA5AB"
NEUTRO = "#D5DCDF"
DISC = "#5F6B71"
DARK = "#1F2A30"
LIGHT = "#EEF3F4"
MUTED = "#6B777D"


def carregar_dados():
    part = pd.read_excel(os.path.join(DADOS, "participacao.xlsx"))
    alt = pd.read_excel(os.path.join(DADOS, "respostas_alternativas.xlsx"))
    notas = pd.read_excel(os.path.join(DADOS, "respostas_notas.xlsx"),
                          sheet_name="notas_por_turma")

    doc = part[part.publico == "Docente"]
    total = doc.groupby("semestre").participantes.sum()
    por_campus = doc.pivot_table(index="semestre", columns="campus",
                                 values="participantes", aggfunc="sum")

    def escala(publico, codigo):
        # % Concordam (1-2), Neutros (3) e Discordam (4-5) por semestre
        d = alt[(alt.publico == publico) & (alt.codigo == codigo)]
        t = d.pivot_table(index="semestre", columns="ordem_alternativa",
                          values="respostas", aggfunc="sum").fillna(0)
        n = t.sum(axis=1)
        return pd.DataFrame({
            "concordam": t[[1, 2]].sum(axis=1) / n * 100,
            "neutros": t[3] / n * 100,
            "discordam": t.drop(columns=[1, 2, 3]).sum(axis=1) / n * 100,
        })

    turmas = notas.groupby("semestre").turma.nunique()
    media = notas.groupby("semestre").apply(
        lambda x: (x.nota * x.respostas).sum() / x.respostas.sum(), include_groups=False)
    return total, por_campus, escala("Docente", "8.1.1"), escala("Discente", "8.1.1"), turmas, media


def imprimir_resumo(total, por_campus, uso_doc, uso_dis, turmas, media):
    print("Respondentes docentes:", total.to_dict())
    print("Por campus:\n", por_campus)
    print("Docentes 8.1.1 (%):\n", uso_doc.round(1))
    print("Discentes 8.1.1 (%):\n", uso_dis.round(1))
    print("Turmas avaliadas:", turmas.to_dict(), "| nota media:", media.round(1).to_dict())


def barra_escala(ax, linhas, rotulos, cor_conc, legenda=False):
    # Barras 100% empilhadas: concordam em destaque, o resto em cinza
    if legenda:  # rotulos diretos sobre os segmentos da primeira barra
        r = linhas.iloc[0]
        for txt, x, cor in (("Concordam", 0, cor_conc),
                            ("Neutros", r.concordam, MUTED),
                            ("Discordam", r.concordam + r.neutros, GRAY)):
            ax.text(x, -0.55, txt, color=cor, fontsize=9, fontweight="bold", va="bottom")
    for i, (_, r) in enumerate(linhas.iterrows()):
        ax.barh(i, r.concordam, color=cor_conc, height=0.62)
        ax.barh(i, r.neutros, left=r.concordam, color=NEUTRO, height=0.62)
        ax.barh(i, r.discordam, left=r.concordam + r.neutros, color=GRAY, height=0.62)
        ax.text(2, i, f"{r.concordam:.0f}%", color="white", fontsize=10.5,
                fontweight="bold", va="center")
    ax.set_yticks(range(len(rotulos)))
    ax.set_yticklabels(rotulos, color=DARK, fontsize=9.5)
    ax.set_xlim(0, 100)
    ax.set_ylim(len(rotulos) - 0.5, -0.5)
    ax.set_xticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.tick_params(length=0)


def main():
    total, por_campus, uso_doc, uso_dis, turmas, media = carregar_dados()
    imprimir_resumo(total, por_campus, uso_doc, uso_dis, turmas, media)

    fig = plt.figure(figsize=(8.27, 11.69), facecolor="white")
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)
    bg.axis("off")

    # Cabecalho: a Big Idea e o primeiro ponto de leitura
    bg.add_patch(Rectangle((0, 0.875), 1, 0.125, color=ACCENT))
    titulo_wrap = "\n".join(textwrap.fill(l, 62) for l in TITULO.split("\n"))
    bg.text(0.05, 0.972, titulo_wrap, color="white", fontsize=15,
            fontweight="bold", va="top", linespacing=1.3)
    bg.text(0.05, 0.888, SUBTITULO, color="#CFE3E7", fontsize=9, va="bottom")

    # Secao 1: participacao (contagens, eixo a partir de zero)
    bg.text(0.05, 0.84, SECAO1, color=DARK, fontsize=12.5, fontweight="bold", va="bottom")
    ax1 = fig.add_axes([0.07, 0.64, 0.52, 0.185])
    sem = list(total.index)
    cores = [GRAY] * (len(sem) - 1) + [ACCENT]
    ax1.bar(range(len(sem)), total.values, color=cores, width=0.6)
    for i, v in enumerate(total.values):
        ax1.text(i, v + 6, f"{v:.0f}", ha="center", color=cores[i],
                 fontsize=12, fontweight="bold")
    ax1.set_xticks(range(len(sem)))
    ax1.set_xticklabels(sem, color=DARK, fontsize=9.5)
    ax1.set_ylim(0, total.max() * 1.2)
    ax1.set_yticks([])
    for s in ("top", "right", "left"):
        ax1.spines[s].set_visible(False)
    ax1.spines["bottom"].set_color(GRAY)
    ax1.tick_params(length=0)
    bg.text(0.05, 0.622, "Docentes que concluíram o questionário, por semestre",
            color=MUTED, fontsize=8, va="top")

    queda = (1 - total.iloc[-1] / total.iloc[-2]) * 100
    bg.add_patch(FancyBboxPatch((0.63, 0.655), 0.32, 0.165,
                                boxstyle="round,pad=0.004,rounding_size=0.01",
                                facecolor=LIGHT, edgecolor="none"))
    bg.text(0.65, 0.805, f"-{queda:.0f}%", color=ACCENT, fontsize=30,
            fontweight="bold", va="top")
    bg.text(0.65, 0.745, "de 2025.1 para 2025.2", color=ACCENT, fontsize=9.5,
            fontweight="bold", va="top")
    bg.text(0.65, 0.722, textwrap.fill(NOTA1, 36), color=DARK, fontsize=8.6,
            va="top", linespacing=1.3)

    # Secao 2: docentes usam os resultados (mesma codificacao da secao 3)
    bg.text(0.05, 0.575, SECAO2, color=DARK, fontsize=12.5, fontweight="bold", va="bottom")
    bg.text(0.05, 0.568, textwrap.fill(PERGUNTA2, 105), color=MUTED, fontsize=8.2,
            va="top", style="italic")
    ax2 = fig.add_axes([0.15, 0.43, 0.80, 0.095])
    barra_escala(ax2, uso_doc, list(uso_doc.index), ACCENT, legenda=True)
    bg.text(0.05, 0.418, NOTA2, color=MUTED, fontsize=8, va="top")

    # Secao 3: percepcao dos estudantes
    bg.text(0.05, 0.37, SECAO3, color=DARK, fontsize=12.5, fontweight="bold", va="bottom")
    ult_dis = uso_dis.iloc[-1]
    bg.text(0.05, 0.355, f"{ult_dis.concordam:.0f}%", color=DISC, fontsize=34,
            fontweight="bold", va="top")
    bg.text(0.24, 0.355, textwrap.fill(PERGUNTA3, 72), color=DARK, fontsize=9,
            va="top", linespacing=1.3)
    ax3 = fig.add_axes([0.24, 0.282, 0.71, 0.03])
    barra_escala(ax3, uso_dis.iloc[[-1]], [""], DISC)
    bg.text(0.05, 0.268, textwrap.fill(NOTA3, 105), color=DARK, fontsize=8.8,
            va="top", linespacing=1.3)

    # Chamada a acao
    bg.add_patch(FancyBboxPatch((0.05, 0.085), 0.90, 0.135,
                                boxstyle="round,pad=0.004,rounding_size=0.012",
                                facecolor="white", edgecolor=ACCENT, lw=2.2))
    bg.text(0.075, 0.207, ACAO_TITULO, color=ACCENT, fontsize=13,
            fontweight="bold", va="top")
    for j, linha in enumerate(ACAO_LINHAS):
        bg.text(0.075, 0.172 - j * 0.03, linha, color=DARK, fontsize=9.4, va="top")

    # Rodape
    bg.text(0.05, 0.068, textwrap.fill(FONTES, 125), color=MUTED,
            fontsize=7, va="top", linespacing=1.3)

    fig.savefig(os.path.join(PASTA, "infografico_cpa.png"), dpi=200)
    fig.savefig(os.path.join(PASTA, "infografico_cpa.pdf"))
    print("Gerado: infografico_cpa.png e infografico_cpa.pdf")


if __name__ == "__main__":
    main()
