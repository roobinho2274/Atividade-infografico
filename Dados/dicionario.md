# Avaliação Institucional da UNIFEI: discentes e docentes, 2024.2 a 2025.2

## Sobre os dados

A **Avaliação Institucional** é uma pesquisa feita pela Comissão Própria de Avaliação (CPA) da UNIFEI, como
exige o Sistema Nacional de Avaliação da Educação Superior (SINAES). A cada semestre de aplicação, estudantes
de graduação (**discentes**) e professores (**docentes**) respondem a um questionário online com afirmações
sobre a universidade.

Este conjunto de dados traz as respostas **já agregadas**: em vez de uma linha por pessoa, cada linha informa
quantas pessoas de um grupo (por exemplo, discentes de um curso em um campus) escolheram determinada resposta.
Não há nenhuma informação que permita identificar estudantes, professores, turmas ou disciplinas, e os
comentários escritos não foram incluídos.

Semestres disponíveis: **2024.2, 2025.1, 2025.2**. Os demais semestres de 2024 e 2025 não constam na base
de origem.

| Semestre | Discentes | Docentes |
|---|---|---|
| 2024.2 | 449 | 201 |
| 2025.1 | 777 | 214 |
| 2025.2 | 403 | 147 |

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| `participacao.xlsx` | Quantas pessoas responderam, por semestre, público, campus e curso. |
| `respostas_alternativas.xlsx` | Quantas pessoas escolheram cada resposta das perguntas de múltipla escolha. |
| `respostas_notas.xlsx` | Distribuição das notas de 1 a 10 que os discentes deram aos professores das disciplinas. Tem duas abas: por curso e por turma. |
| `dicionario.md` | Este documento. |

## Como o questionário é organizado

As perguntas são agrupadas em 8 seções, que correspondem às 10 dimensões de avaliação definidas pelo SINAES
(Lei nº 10.861/2004).

| Seção | Dimensões do SINAES | Tema |
|---|---|---|
| Seção 1 | 1 e 8 | Missão, Plano de Desenvolvimento Institucional (PDI), planejamento e avaliação |
| Seção 2 | 2 | Políticas para o ensino, a pesquisa, a pós-graduação e a extensão |
| Seção 3 | 3 | Responsabilidade social da instituição |
| Seção 4 | 4 | Comunicação com a sociedade |
| Seção 5 | 5 e 6 | Políticas de pessoal, organização e gestão |
| Seção 6 | 7 | Infraestrutura física |
| Seção 7 | 9 | Políticas de atendimento aos estudantes |
| Seção 8 | 10 | Sustentabilidade financeira |

Cada pergunta tem um **código** no formato `D.G.P`. O primeiro número é a dimensão do SINAES, o segundo é o
grupo de perguntas e o terceiro é a ordem da pergunta no grupo. Por isso o código `8.1.1` aparece na Seção 1,
que reúne as dimensões 1 e 8.

Discentes e docentes respondem a questionários **diferentes**. O mesmo código pode corresponder a perguntas
diferentes para cada público, e às vezes também entre semestres. Para identificar uma pergunta, use sempre a
combinação de semestre, público, código e texto da pergunta.

## Colunas

### participacao.xlsx

| Coluna | Descrição |
|---|---|
| `semestre` | Semestre da avaliação, no formato ano.período (ex.: 2025.1). |
| `publico` | `Discente` (estudante de graduação) ou `Docente` (professor). |
| `campus` | `Itajubá`, `Itabira` ou `EaD` (cursos a distância). |
| `curso` | Curso de graduação do estudante. Fica em branco para docentes, porque um professor pode lecionar em vários cursos e a avaliação não registra a qual deles ele se refere. |
| `participantes` | Número de pessoas que concluíram o questionário. |

### respostas_alternativas.xlsx

| Coluna | Descrição |
|---|---|
| `semestre`, `publico`, `campus`, `curso` | Iguais às de `participacao.xlsx`. |
| `secao` | Seção do questionário (ver tabela acima). |
| `codigo` | Código da pergunta. |
| `pergunta` | Texto da pergunta ou afirmação. |
| `respondida_por_turma` | `VERDADEIRO` quando o estudante responde a pergunta uma vez para cada disciplina que cursou no semestre (ver explicação abaixo). |
| `ordem_alternativa` | Posição da resposta na escala: 1 = Concordo totalmente, 2 = Concordo, 3 = neutro, 4 = Discordo, 5 = Discordo totalmente. Nas perguntas de Sim ou Não: 1 = Sim, 2 = Não. |
| `alternativa` | Texto da resposta escolhida. |
| `respostas` | Número de pessoas que escolheram essa resposta. |

### respostas_notas.xlsx

Contém a pergunta em que o estudante atribui uma nota de 1 a 10 ao professor de cada disciplina cursada.
Só existe para os discentes, nos semestres 2025.1 e 2025.2.

| Coluna | Descrição |
|---|---|
| `semestre`, `publico`, `campus`, `curso` | Iguais às de `participacao.xlsx`. |
| `secao`, `codigo`, `pergunta` | Identificação da pergunta (somente na aba `notas_por_curso`). |
| `turma` | Somente na aba `notas_por_turma`. Código sorteado (ex.: `2025.1-T001`) que representa uma disciplina com um professor. Serve apenas para agrupar as notas de uma mesma turma: não tem relação com códigos oficiais e muda a cada geração do arquivo. |
| `nota` | Nota atribuída, de 1 a 10. |
| `respostas` | Quantas vezes essa nota foi dada. Um mesmo estudante avalia todas as turmas que cursou, então o total de respostas é maior que o número de estudantes. |

## Como interpretar as contagens

**Perguntas sobre a instituição.** Cada pessoa responde uma vez. Somando as respostas de uma pergunta, chega-se
ao número de participantes do grupo. Exemplo: se um curso teve 20 participantes, as cinco alternativas de uma
pergunta somam 20. A exceção são as perguntas que só existem no questionário dos cursos a distância, ou só no
presencial: elas somam apenas quem respondeu aquele questionário.

**Perguntas respondidas por turma** (`respondida_por_turma = VERDADEIRO`). Na Seção 2, o estudante responde
uma vez para cada disciplina cursada. A coluna `respostas` conta **quantos estudantes diferentes** escolheram
aquela resposta em pelo menos uma disciplina. Como um estudante pode concordar em uma disciplina e discordar em
outra, ele pode ser contado em mais de uma alternativa, e a soma pode passar do número de participantes.
Para comparar grupos, prefira proporções dentro de cada alternativa a somas. Essas linhas estão agregadas por
curso e não identificam a disciplina.

**Notas.** Cada linha conta respostas, não pessoas. A aba `notas_por_curso` soma 9596 respostas
e inclui todas as notas de 1 a 10 registradas. A aba `notas_por_turma` soma 7770, porque exclui as turmas
marcadas como inválidas no processamento da avaliação. Notas 0 foram descartadas, porque a escala da pergunta
é de 1 a 10.

## Cuidados e limitações

- Nem todos os estudantes e professores respondem. Os resultados refletem quem participou, não toda a
  comunidade.
- Alguns cursos têm poucos participantes. Percentuais calculados sobre grupos muito pequenos variam bastante.
- Os docentes aparecem agregados apenas por campus.
- Os cursos a distância (EaD) usam um questionário um pouco diferente na Seção 6 (infraestrutura), com
  perguntas sobre o ambiente virtual de aprendizagem. A pergunta 7.1.1 tem uma versão para cada questionário,
  e as perguntas 7.1.5 a 7.1.8 só existem no EaD. Alguns estudantes de cursos a distância aparecem
  vinculados aos campi de Itajubá ou Itabira, e não a `EaD`.
- O texto da resposta neutra mudou ao longo do tempo ("Indiferente / neutro" e "Nem concordo nem discordo"),
  mas a posição na escala (3) é a mesma.
- Os textos das perguntas foram padronizados (espaços e pontuação final) para que versões do mesmo enunciado
  fiquem iguais.

## Perguntas por semestre e público

As respostas possíveis listadas são as que apareceram nos dados.


### 2024.2: Discentes

| Seção | Código | Pergunta | Tipo | Por turma | Respostas possíveis |
|---|---|---|---|---|---|
| Seção 1 | 1.1.1 | Conheço a missão da universidade e os objetivos estratégicos definidos no PDI | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 1 | 1.1.2 | As decisões institucionais consideram a opinião dos estudantes | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 1 | 8.1.1 | A instituição utiliza os resultados das avaliações internas (CPA) e externas (MEC) para promover melhorias | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 2 | 2.1.1 | De forma geral o ensino ofertado pela instituição no semestre foi satisfatório | Alternativa | Sim | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 2 | 2.1.2 | O relacionamento entre professores e estudantes é respeitoso e construtivo | Alternativa | Sim | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 3 | 3.1.1 | A instituição promove ações de inclusão e diversidade | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 4 | 4.1.1 | Recebo informações claras e atualizadas sobre eventos, prazos e atividades acadêmicas | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 5 | 5.1.1 | Sinto-me seguro(a) para denunciar ou relatar casos de assédio moral ou desrespeito | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 5 | 5.1.2 | Os técnicos-administrativos (secretaria, apoio, etc.) são atenciosos e prestativos | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 5 | 6.1.1 | As coordenações de curso são acessíveis e dialogam com os alunos | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | As salas de aula são adequadas e bem equipadas para o processo de aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 6 | 7.1.2 | Os laboratórios e bibliotecas atendem às necessidades do curso | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 6 | 7.1.3 | Os espaços de convivência, estudo e lazer são acessíveis e bem cuidados | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 6 | 7.1.4 | A estrutura física é acessível a pessoas com deficiência | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 7 | 9.1.1 | Recebo orientação adequada sobre minha vida acadêmica (matrícula, disciplinas, estágios, etc.) | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 7 | 9.1.2 | A instituição oferece suporte emocional e psicológico quando necessário | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 7 | 9.1.3 | Tenho acesso a bolsas, auxílios ou serviços de apoio estudantil quando preciso | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 8 | 10.1.1 | Percebo que os investimentos feitos contribuem para a melhoria da qualidade do curso | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |


### 2024.2: Docentes

| Seção | Código | Pergunta | Tipo | Por turma | Respostas possíveis |
|---|---|---|---|---|---|
| Seção 1 | 1.1.1 | A missão da universidade, visão, valores e os objetivos estratégicos definidos no Plano de desenvolvimento institucional - PDI alinham-se à minha prática pedagógica e considero que esses princípios são utilizados como referência nos programas e projetos articulados com a política de ensino, pesquisa, extensão e gestão | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 1 | 8.1.1 | Tenho acesso aos resultados das avaliações institucionais internas (CPA) e externas (MEC) e, a partir delas, realizo ações de melhorias na minha prática profissional | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 2 | 2.1.1 | A instituição estimula a realização de atividades de ensino, pesquisa e extensão | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 3 | 3.1.1 | A instituição promove a responsabilidade social com ações voltadas para a inclusão e o desenvolvimento socioeconômico, ambiental e cultural | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 3 | 3.2.1 | A instituição valoriza a promoção da equidade de gênero, raça e inclusão | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo |
| Seção 4 | 4.1.1 | Os canais de comunicação interna e externa são eficientes e acessíveis também a pessoas com necessidades especiais | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 5 | 5.1.1 | O ambiente de trabalho é LIVRE de comportamentos discriminatórios ou de assédio. Sinto-me respeitado(a) por alunos, líderes e colegas de trabalho | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 5 | 5.1.2 | Sou reconhecido(a) pelo meu desempenho, esforço e dedicação | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 5 | 5.2.1 | A instituição oferece plano de carreira e de capacitação que atendam às necessidades dos docentes | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 5 | 6.1.1 | Há participação e representatividade dos segmentos da comunidade acadêmica nos processos decisórios | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | As instalações da universidade passam por melhorias, manutenções periódicas e políticas de conservação para se tornarem adequadas à aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 6 | 7.1.2 | Nos espaços físicos da instituição, há condições de acessibilidade para pessoas com deficiências | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 6 | 7.2.1 | O atendimento institucional no período noturno é eficiente e adequado às demandas de docentes e discentes desse turno | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 7 | 9.1.1 | A instituição promove programas de apoio ao discente (assistência estudantil, bolsas acadêmicas, apoio psicopedagógico e incentivo à organização dos estudantes) | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo |
| Seção 8 | 10.1.1 | A aplicação de recursos para programas de ensino, pesquisa e extensão é feita de forma democrática e transparente | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |
| Seção 8 | 10.1.2 | A gestão de recursos para a capacitação do corpo docente é feita de forma transparente, democrática e considera a relevância para a prática docente | Alternativa | Não | Concordo totalmente; Concordo; Indiferente / neutro; Discordo; Discordo totalmente |


### 2025.1: Discentes

| Seção | Código | Pergunta | Tipo | Por turma | Respostas possíveis |
|---|---|---|---|---|---|
| Seção 1 | 1.1.1 | Conheço a missão da universidade e os objetivos estratégicos definidos no PDI | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 1 | 1.1.2 | As decisões institucionais consideram a opinião dos estudantes | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 1 | 8.1.1 | A instituição utiliza os resultados das avaliações internas (CPA) e externas (MEC) para promover melhorias | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.1 | De forma geral o ensino ofertado pela instituição no semestre foi satisfatório | Alternativa | Sim | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.2 | O relacionamento entre professores e estudantes é respeitoso e construtivo | Alternativa | Sim | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.3 | Considerando as suas respostas anteriores, atribua uma nota entre 1 e 10 para o(a) docente da disciplina | Nota | Sim | 1 a 10 |
| Seção 3 | 3.1.1 | A instituição promove ações de inclusão e diversidade | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 4 | 4.1.1 | Recebo informações claras e atualizadas sobre eventos, prazos e atividades acadêmicas | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.1.1 | Sinto-me seguro(a) para denunciar ou relatar casos de assédio moral ou desrespeito | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.1.2 | Os técnicos-administrativos (secretaria, apoio, etc.) são atenciosos e prestativos | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 6.1.1 | As coordenações de curso são acessíveis e dialogam com os alunos | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | As salas de aula são adequadas e bem equipadas para o processo de aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | Os ambientes virtuais são adequados e bem equipados para o processo de aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 6 | 7.1.2 | Os laboratórios e bibliotecas atendem às necessidades do curso | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.3 | Os espaços de convivência, estudo e lazer são acessíveis e bem cuidados | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.4 | A estrutura física é acessível a pessoas com deficiência | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.5 | O ambiente virtual de aprendizagem (AVA) é estável, acessível e de fácil utilização | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 6 | 7.1.6 | O suporte técnico oferecido para resolução de problemas no AVA é eficiente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 6 | 7.1.7 | O atendimento acadêmico a distância (coordenação, tutoria, secretaria) é satisfatório | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo totalmente |
| Seção 6 | 7.1.8 | As ferramentas tecnológicas (vídeo, fóruns, chats, recursos interativos) contribuem efetivamente para minha aprendizagem/atuação docente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 7 | 9.1.1 | Recebo orientação adequada sobre minha vida acadêmica (matrícula, disciplinas, estágios, etc) | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 7 | 9.1.2 | A instituição oferece suporte emocional e psicológico quando necessário | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 7 | 9.1.3 | Tenho acesso a bolsas, auxílios ou serviços de apoio estudantil quando preciso | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 8 | 10.1.1 | Percebo que os investimentos feitos contribuem para a melhoria da qualidade do curso | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |


### 2025.1: Docentes

| Seção | Código | Pergunta | Tipo | Por turma | Respostas possíveis |
|---|---|---|---|---|---|
| Seção 1 | 1.1.1 | A missão da universidade, visão, valores e os objetivos estratégicos definidos no Plano de desenvolvimento institucional - PDI alinham-se à minha prática pedagógica e considero que esses princípios são utilizados como referência nos programas e projetos articulados com a política de ensino, pesquisa, extensão e gestão | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo |
| Seção 1 | 8.1.1 | Tenho acesso aos resultados das avaliações institucionais e realizo ações de melhorias na minha prática profissional | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.1 | A instituição estimula a realização de atividades de ensino, pesquisa e extensão | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.2 | Os alunos mantiveram postura adequada em sala de aula, prestando atenção às aulas e respeitando o professor. Atenção! PREENCHER SIM OU NÃO | Alternativa | Não | Sim; Não |
| Seção 3 | 3.1.1 | A instituição promove a responsabilidade social com ações voltadas para a inclusão e o desenvolvimento socioeconômico, ambiental e cultural | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 3 | 3.2.1 | A instituição valoriza a promoção da equidade de gênero, raça e inclusão | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 4 | 4.1.1 | Os canais de comunicação interna e externa são eficientes e acessíveis também a pessoas com necessidades especiais | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.1.1 | O ambiente de trabalho é LIVRE de comportamentos discriminatórios ou de assédio. Sinto-me respeitado(a) por alunos, líderes e colegas de trabalho | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 5 | 5.1.2 | Sou reconhecido(a) pelo meu desempenho, esforço e dedicação | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.2.1 | A instituição oferece plano de carreira e de capacitação que atendam às necessidades dos docentes | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 5 | 6.1.1 | Há participação e representatividade dos segmentos da comunidade acadêmica nos processos decisórios | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | As instalações da universidade passam por melhorias, manutenções periódicas e políticas de conservação para se tornarem adequadas à aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.2 | Nos espaços físicos da instituição, há condições de acessibilidade para pessoas com deficiências | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.2.1 | O atendimento institucional no período noturno é eficiente e adequado às demandas de docentes e discentes desse turno | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 7 | 9.1.1 | A instituição promove programas de apoio ao discente (assistência estudantil, bolsas acadêmicas, apoio psicopedagógico e incentivo à organização dos estudantes) | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 8 | 10.1.1 | A aplicação de recursos para programas de ensino, pesquisa e extensão é feita de forma democrática e transparente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 8 | 10.1.2 | A gestão de recursos para a capacitação do corpo docente é feita de forma transparente, democrática e considera a relevância para a prática docente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |


### 2025.2: Discentes

| Seção | Código | Pergunta | Tipo | Por turma | Respostas possíveis |
|---|---|---|---|---|---|
| Seção 1 | 1.1.1 | Conheço a missão da universidade e os objetivos estratégicos definidos no PDI | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 1 | 1.1.2 | As decisões institucionais consideram a opinião dos estudantes | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 1 | 8.1.1 | A instituição utiliza os resultados das avaliações internas (CPA) e externas (MEC) para promover melhorias | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.1 | De forma geral o ensino ofertado pela instituição no semestre foi satisfatório | Alternativa | Sim | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.2 | O relacionamento entre professores e estudantes é respeitoso e construtivo | Alternativa | Sim | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.3 | Considerando as suas respostas anteriores, atribua uma nota entre 1 e 10 para o(a) docente da disciplina | Nota | Sim | 1 a 10 |
| Seção 2 | 2.1.4 | Você cursaria novamente alguma outra disciplina com este(a) docente? | Alternativa | Sim | Sim; Não |
| Seção 3 | 3.1.1 | A instituição promove ações de inclusão e diversidade | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 4 | 4.1.1 | Recebo informações claras e atualizadas sobre eventos, prazos e atividades acadêmicas | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.1.1 | Sinto-me seguro(a) para denunciar ou relatar casos de assédio moral ou desrespeito | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.1.2 | Os técnicos-administrativos (secretaria, apoio, etc.) são atenciosos e prestativos | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 6.1.1 | As coordenações de curso são acessíveis e dialogam com os alunos | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | As salas de aula são adequadas e bem equipadas para o processo de aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | Os ambientes virtuais são adequados e bem equipados para o processo de aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.2 | Os laboratórios e bibliotecas atendem às necessidades do curso | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.3 | Os espaços de convivência, estudo e lazer são acessíveis e bem cuidados | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.4 | A estrutura física é acessível a pessoas com deficiência | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.5 | O ambiente virtual de aprendizagem (AVA) é estável, acessível e de fácil utilização | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.6 | O suporte técnico oferecido para resolução de problemas no AVA é eficiente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo totalmente |
| Seção 6 | 7.1.7 | O atendimento acadêmico a distância (coordenação, tutoria, secretaria) é satisfatório | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 6 | 7.1.8 | As ferramentas tecnológicas (vídeo, fóruns, chats, recursos interativos) contribuem efetivamente para minha aprendizagem/atuação docente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 7 | 9.1.1 | Recebo orientação adequada sobre minha vida acadêmica (matrícula, disciplinas, estágios, etc) | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 7 | 9.1.2 | A instituição oferece suporte emocional e psicológico quando necessário | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 7 | 9.1.3 | Tenho acesso a bolsas, auxílios ou serviços de apoio estudantil quando preciso | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 8 | 10.1.1 | Percebo que os investimentos feitos contribuem para a melhoria da qualidade do curso | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |


### 2025.2: Docentes

| Seção | Código | Pergunta | Tipo | Por turma | Respostas possíveis |
|---|---|---|---|---|---|
| Seção 1 | 1.1.1 | A missão da universidade, visão, valores e os objetivos estratégicos definidos no Plano de desenvolvimento institucional - PDI alinham-se à minha prática pedagógica e considero que esses princípios são utilizados como referência nos programas e projetos articulados com a política de ensino, pesquisa, extensão e gestão | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 1 | 8.1.1 | Tenho acesso aos resultados das avaliações institucionais e realizo ações de melhorias na minha prática profissional | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo |
| Seção 2 | 2.1.1 | A instituição estimula a realização de atividades de ensino, pesquisa e extensão | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 2 | 2.1.2 | Você disponibilizou material didático aos alunos por meio da plataforma institucional (Sigaa)? | Alternativa | Não | Sim; Não |
| Seção 3 | 3.1.1 | A instituição promove a responsabilidade social com ações voltadas para a inclusão e o desenvolvimento socioeconômico, ambiental e cultural | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 3 | 3.2.1 | A instituição valoriza a promoção da equidade de gênero, raça e inclusão | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 4 | 4.1.1 | Os canais de comunicação interna e externa são eficientes e acessíveis também a pessoas com necessidades especiais | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.1.1 | O ambiente de trabalho é LIVRE de comportamentos discriminatórios ou de assédio. Sinto-me respeitado(a) por alunos, líderes e colegas de trabalho | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.1.2 | Sou reconhecido(a) pelo meu desempenho, esforço e dedicação | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 5.2.1 | A instituição oferece plano de carreira e de capacitação que atendam às necessidades dos docentes | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 5 | 6.1.1 | Há participação e representatividade dos segmentos da comunidade acadêmica nos processos decisórios | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.1 | As instalações da universidade passam por melhorias, manutenções periódicas e políticas de conservação para se tornarem adequadas à aprendizagem | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.1.2 | Nos espaços físicos da instituição, há condições de acessibilidade para pessoas com deficiências | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 6 | 7.2.1 | O atendimento institucional no período noturno é eficiente e adequado às demandas de docentes e discentes desse turno | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 7 | 9.1.1 | A instituição promove programas de apoio ao discente (assistência estudantil, bolsas acadêmicas, apoio psicopedagógico e incentivo à organização dos estudantes) | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 8 | 10.1.1 | A aplicação de recursos para programas de ensino, pesquisa e extensão é feita de forma democrática e transparente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
| Seção 8 | 10.1.2 | A gestão de recursos para a capacitação do corpo docente é feita de forma transparente, democrática e considera a relevância para a prática docente | Alternativa | Não | Concordo totalmente; Concordo; Nem concordo nem discordo; Discordo; Discordo totalmente |
