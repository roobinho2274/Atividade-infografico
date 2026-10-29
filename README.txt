INFOGRÁFICO CPA/UNIFEI - GRUPO 3 (DOCENTES)
===========================================

O script infografico_cpa.py lê as planilhas da CPA na pasta dados/ e gera
dois arquivos nesta pasta:
  - infografico_cpa.png
  - infografico_cpa.pdf (tamanho A4)


ARQUIVOS DA PASTA
-----------------
  infografico_cpa.py               Script que monta o infográfico.
  dados/participacao.xlsx          Respondentes por semestre, público e campus.
  dados/respostas_alternativas.xlsx  Respostas das perguntas de múltipla escolha.
  dados/respostas_notas.xlsx       Notas de 1 a 10 dadas pelos discentes às turmas.
  dados/dicionario.md              Explicação das colunas e cuidados com os dados.
  Atividade_3_...pdf               Enunciado da atividade.


COMO RODAR
----------
1. Abra um terminal nesta pasta (no VS Code: Terminal > New Terminal).

2. Na primeira vez, instale as bibliotecas:
     python -m pip install matplotlib pandas openpyxl

3. Execute:
     python infografico_cpa.py

4. O terminal mostra um resumo dos números calculados e, no final:
     Gerado: infografico_cpa.png e infografico_cpa.pdf

Observação: feche o PNG ou o PDF antes de rodar, porque o Windows pode
impedir a gravação se o arquivo estiver aberto.


O QUE O INFOGRÁFICO MOSTRA
--------------------------
  1. Respondentes docentes por semestre: 201 > 214 > 147 (-31% em 2025.2).
     Em Itajubá, foram de 159 para 93; em Itabira, de 55 para 54.
  2. Pergunta 8.1.1 dos docentes ("Tenho acesso aos resultados ... e realizo
     ações de melhorias"): a concordância foi de 67% para 80% e depois 82%.
  3. Pergunta 8.1.1 dos discentes ("A instituição utiliza os resultados ...
     para promover melhorias"): 48% concordam e 37% ficaram neutros (2025.2).
     Notas: 484 turmas avaliadas em 2025.2, com média 8,5.

Limitações (já indicadas no infográfico):
  - A base não traz o total de docentes da UNIFEI, então não dá para calcular
    a TAXA de participação, apenas o número de respondentes. Se a CPA informar
    o total de docentes por semestre, o gráfico 1 pode passar a mostrar %.
  - A pergunta 8.1.1 é uma autodeclaração de quem respondeu.
  - As perguntas de docentes e discentes são diferentes, então não são
    comparadas lado a lado como se fossem a mesma medida.


COMO ATUALIZAR
--------------
Os GRÁFICOS são calculados das planilhas automaticamente. Os TEXTOS ficam no
bloco "EDITE AQUI" do infografico_cpa.py e têm números escritos à mão
(TITULO, NOTA1, SECAO2, PERGUNTA3, NOTA3).

Se as planilhas mudarem (por exemplo, um novo semestre):
  1. Substitua os arquivos em dados/ mantendo os mesmos nomes e colunas.
  2. Rode o script e confira o resumo impresso no terminal.
  3. Ajuste os números dos textos no bloco "EDITE AQUI" para bater com o
     resumo.
  4. Rode de novo e confira a imagem.


AINDA PENDENTE PARA A ENTREGA
-----------------------------
  - Texto de entrega com:
      (a) público-alvo e necessidade de informação
      (b) objetivo da comunicação
      (c) mensagem central (Big Idea)
      (d) fontes de dados utilizadas
