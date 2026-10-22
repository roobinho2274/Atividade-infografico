INFOGRÁFICO CPA/UNIFEI - GRUPO 3 (DOCENTES)
===========================================

O script infografico_cpa.py gera dois arquivos nesta pasta:
  - infografico_cpa.png
  - infografico_cpa.pdf (tamanho A4)


ARQUIVOS DA PASTA
-----------------
  infografico_cpa.py        Script que monta o infográfico.
  dados_participacao.csv    Dados do gráfico (por enquanto FICTÍCIOS).
  Atividade_3_...pdf        Enunciado da atividade.


COMO RODAR
----------
1. Abra um terminal DENTRO desta pasta.
   No VS Code: menu Terminal > New Terminal (já abre na pasta).
   Se abrir em outro lugar, entre na pasta com:
     cd "G:\Meu Drive\02_Mestrado\Disciplinas\Visualização de dados\Atividade infografico"

2. Execute:
     python infografico_cpa.py

3. Deve aparecer a mensagem:
     Gerado: infografico_cpa.png e infografico_cpa.pdf

4. Abra o PNG ou o PDF para conferir o resultado.

Observações:
  - Rode SEMPRE de dentro desta pasta. Se não encontrar o CSV, o script
    usa valores de exemplo (50% em todos os semestres).
  - Feche o PNG ou o PDF antes de rodar, porque o Windows pode impedir a
    gravação se o arquivo estiver aberto.
  - Em outro computador, instale antes a biblioteca:
      python -m pip install matplotlib


COMO ATUALIZAR COM OS DADOS REAIS
---------------------------------
1. Edite dados_participacao.csv (Excel ou Bloco de Notas) e mantenha o
   mesmo formato:

     periodo,docentes_pct,discentes_pct
     2023.1,38,52
     2023.2,35,49
     ...

   - periodo:        semestre (ex.: 2025.1)
   - docentes_pct:   % de docentes que responderam à CPA (só o número)
   - discentes_pct:  % de discentes (opcional; pode deixar vazio)
   - Use apenas números que estão nos relatórios da CPA.
   - Se usar o Excel, salve como "CSV UTF-8 (delimitado por vírgulas)".

2. No infografico_cpa.py, no bloco "EDITE AQUI", altere:

   a) DADOS_FICTICIOS = False
      (remove a marca "RASCUNHO: DADOS DE EXEMPLO". Mude só quando o CSV
      tiver os dados reais.)

   b) TITULO: a Big Idea, com o número real do último semestre.
      Hoje: "Só 27% dos docentes responderam à CPA em 2025.1 ..."

   c) TITULO_GRAFICO: uma afirmação que bata com os dados reais.
      Hoje: "A participação docente caiu de 38% para 27% em dois anos"

   d) FONTE_GRAFICO: relatório usado, campus, período e abrangência.

   e) FONTES (rodapé): todas as fontes consultadas, incluindo a base
      legal da CPA (Lei 10.861/2004 - SINAES).

   f) CONTEXTO: confirme "desde 2006" e o texto de "Por que importa".

   g) ACAO_LINHAS: confirme se os relatórios por curso estão em
      cpa.unifei.edu.br e remova o "[VERIFICAR]".

3. Salve e rode de novo: python infografico_cpa.py

4. Confira na imagem se não sobrou nenhum "[PREENCHER]" ou "[VERIFICAR]".


AINDA PENDENTE PARA A ENTREGA
-----------------------------
  - Evidência para a 2ª parte do desafio: os docentes usarem os resultados
    da CPA para melhorar as práticas acadêmicas (ex.: um caso real de
    mudança feita a partir da CPA, ou um fluxo
    responder > relatório > colegiado > melhoria).
  - Texto de entrega com:
      (a) público-alvo e necessidade de informação
      (b) objetivo da comunicação
      (c) mensagem central (Big Idea)
      (d) fontes de dados utilizadas
