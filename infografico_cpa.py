"""Infografico CPA/UNIFEI - Grupo 3 (docentes).
Gera infografico_cpa.png e infografico_cpa.pdf (A4).

COMO USAR
1) Edite o bloco "EDITE AQUI" (titulo, fonte, textos marcados com [PREENCHER]).
2) Crie dados_participacao.csv (mesma pasta) com as colunas:
       periodo,docentes_pct,discentes_pct
       2024.1,41,63
   (discentes_pct e opcional. Use so numeros que estao nos relatorios da CPA.)
3) Rode:  python infografico_cpa.py
Sem o CSV, o script usa dados de EXEMPLO e marca a imagem como rascunho.
"""
import csv
import os
import textwrap

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

# ============================ EDITE AQUI ============================
# True enquanto dados_participacao.csv tiver valores ficticios: mantem a marca
# de rascunho na imagem. Mude para False ao colocar os dados reais da CPA.
DADOS_FICTICIOS = True

TITULO = (
    "Só 27% dos docentes responderam à CPA em 2025.1:\n"
    "sem a sua voz, a avaliação não melhora o seu curso"
)
SUBTITULO = "Autoavaliação institucional da UNIFEI | Público: docentes"

CONTEXTO = [
    ("O que é",
     "A CPA conduz a autoavaliação institucional da UNIFEI desde 2006."),
    ("Quando e onde",
     "Todo semestre, no SIGAA: Ensino > Avaliação institucional."),
    ("Por que importa",
     "Os resultados são considerados por MEC e INEP e influenciam "
     "reconhecimento de cursos e renovação de credenciamento."),
]

TITULO_GRAFICO = "A participação docente caiu de 38% para 27% em dois anos"
FONTE_GRAFICO = ("Fonte: [PREENCHER: relatório CPA/UNIFEI, campus Itajubá, "
                 "período, abrangência]")

ACAO_TITULO = "O que fazer agora"
ACAO_LINHAS = [
    "1. Responda a CPA no SIGAA neste semestre.",
    "2. Consulte o relatório do seu curso em cpa.unifei.edu.br e leve ao colegiado. [VERIFICAR]",
]

FONTES = ("Fontes: CPA/UNIFEI (cpa.unifei.edu.br); UNIFEI, \"CPA 2025.1\" "
          "(unifei.edu.br/cpa-2025-1); [PREENCHER: relatórios usados no gráfico].")
# ====================================================================

ACCENT = "#0B5563"
GRAY = "#9AA5AB"
DARK = "#1F2A30"
LIGHT = "#EEF3F4"
ALERT = "#C0392B"


def carregar_dados():
    if os.path.exists("dados_participacao.csv"):
        with open("dados_participacao.csv", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        per = [r["periodo"].strip() for r in rows]
        doc = [float(r["docentes_pct"].replace(",", ".")) for r in rows]
        dis = []
        for r in rows:
            v = (r.get("discentes_pct") or "").strip()
            dis.append(float(v.replace(",", ".")) if v else None)
        return per, doc, dis, DADOS_FICTICIOS
    per = ["2023.1", "2023.2", "2024.1", "2024.2", "2025.1"]
    return per, [50] * 5, [50] * 5, True  # valores ficticios, so para testar layout


def main():
    per, doc, dis, exemplo = carregar_dados()
    fig = plt.figure(figsize=(8.27, 11.69), facecolor="white")
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)
    bg.axis("off")

    # Cabecalho: a Big Idea e o primeiro ponto de leitura
    bg.add_patch(Rectangle((0, 0.86), 1, 0.14, color=ACCENT))
    titulo_wrap = "\n".join(textwrap.fill(l, 58) for l in TITULO.split("\n"))
    n_linhas = titulo_wrap.count("\n") + 1
    fs_titulo = 16.5 if n_linhas <= 2 else 13  # evita colidir com o subtitulo
    bg.text(0.05, 0.975, titulo_wrap, color="white", fontsize=fs_titulo,
            fontweight="bold", va="top", linespacing=1.25)
    bg.text(0.05, 0.875, SUBTITULO, color="#CFE3E7", fontsize=10, va="bottom")

    # Contexto: 3 blocos iguais (similaridade) e proximos (proximidade)
    x0, w, gap = 0.05, 0.28, 0.025
    for i, (cab, corpo) in enumerate(CONTEXTO):
        x = x0 + i * (w + gap)
        bg.add_patch(FancyBboxPatch((x, 0.70), w, 0.135,
                                    boxstyle="round,pad=0.004,rounding_size=0.01",
                                    facecolor=LIGHT, edgecolor="none"))
        bg.text(x + 0.015, 0.82, cab, color=ACCENT, fontsize=10.5,
                fontweight="bold", va="top")
        bg.text(x + 0.015, 0.795, textwrap.fill(corpo, 31), color=DARK,
                fontsize=8.6, va="top", linespacing=1.3)

    # Grafico: titulo-afirmacao, uma cor de destaque, rotulos diretos
    bg.text(0.05, 0.665, TITULO_GRAFICO, color=DARK, fontsize=11.5,
            fontweight="bold", va="bottom")
    ax = fig.add_axes([0.10, 0.31, 0.80, 0.33])
    x = list(range(len(per)))
    ax.plot(x, doc, color=ACCENT, lw=3, marker="o", ms=7, zorder=3)
    ax.scatter([x[-1]], [doc[-1]], s=170, color=ACCENT, zorder=4)
    for xi, v in zip(x, doc):
        ax.annotate(f"{v:.0f}%", (xi, v), textcoords="offset points",
                    xytext=(0, 11), ha="center", color=ACCENT,
                    fontsize=10, fontweight="bold")
    ult_dis = next((v for v in reversed(dis) if v is not None), None)
    doc_acima = ult_dis is None or doc[-1] >= ult_dis
    ax.annotate("Docentes", (x[-1], doc[-1]), textcoords="offset points",
                xytext=(14, 4 if doc_acima else -12), color=ACCENT,
                fontsize=10, fontweight="bold")
    if any(v is not None for v in dis):
        xs = [xi for xi, v in zip(x, dis) if v is not None]
        ys = [v for v in dis if v is not None]
        ax.plot(xs, ys, color=GRAY, lw=2, marker="o", ms=5, zorder=2)
        ax.annotate("Discentes", (xs[-1], ys[-1]), textcoords="offset points",
                    xytext=(14, -12 if doc_acima else 4), color=GRAY,
                    fontsize=10, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(per, color=DARK, fontsize=9)
    ax.set_xlim(-0.4, len(per) - 1 + 1.1)
    ax.set_ylim(0, 100)  # eixo comeca em zero: sem distorcao
    ax.set_yticks([0, 25, 50, 75, 100])
    ax.set_yticklabels([f"{t}%" for t in [0, 25, 50, 75, 100]], color=GRAY, fontsize=8.5)
    ax.grid(axis="y", color="#E3E8EA", lw=0.8)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRAY)
    ax.tick_params(length=0)
    bg.text(0.05, 0.272, textwrap.fill(FONTE_GRAFICO, 95), color="#6B777D",
            fontsize=7.8, va="top")

    # Chamada a acao
    bg.add_patch(FancyBboxPatch((0.05, 0.09), 0.90, 0.145,
                                boxstyle="round,pad=0.004,rounding_size=0.012",
                                facecolor="white", edgecolor=ACCENT, lw=2.2))
    bg.text(0.075, 0.22, ACAO_TITULO, color=ACCENT, fontsize=13,
            fontweight="bold", va="top")
    for j, linha in enumerate(ACAO_LINHAS):
        bg.text(0.075, 0.18 - j * 0.04, textwrap.fill(linha, 82), color=DARK,
                fontsize=9.6, va="top")

    # Rodape
    bg.text(0.05, 0.07, textwrap.fill(FONTES, 120), color="#6B777D",
            fontsize=7.4, va="top")

    if exemplo:
        fig.text(0.5, 0.47, "RASCUNHO: DADOS DE EXEMPLO", rotation=22,
                 fontsize=32, color=ALERT, alpha=0.22, ha="center",
                 va="center", fontweight="bold")
        print("ATENCAO: usando valores de EXEMPLO (sem CSV ou DADOS_FICTICIOS = True).")

    fig.savefig("infografico_cpa.png", dpi=200)
    fig.savefig("infografico_cpa.pdf")
    print("Gerado: infografico_cpa.png e infografico_cpa.pdf")


if __name__ == "__main__":
    main()
