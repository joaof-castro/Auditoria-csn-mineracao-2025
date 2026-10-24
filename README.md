# Auditoria acadêmica — CSN Mineração S.A. (CMIN3) | 2025

> **Projeto didático e independente da companhia.** Não constitui auditoria independente, asseguração, parecer profissional nem acusação de irregularidades. O banco detalhado de imobilizado é **100% sintético**.

## Objetivo

Organizar um dossiê acadêmico de auditoria das demonstrações financeiras de 2025 da **CSN Mineração S.A.**, com comparativos de 2024, planejamento, avaliação de riscos, materialidade, procedimentos analíticos, amostragem e documentação dos papéis de trabalho.

## Ordem recomendada de leitura

1. `01_fontes_publicas/`: DFP 2025 (documento principal), DFP 2024 (apoio histórico) e Formulário de Referência 2026 (contexto complementar, posterior ao exercício).
2. `02_planejamento/`: análise de demonstrações, memorando e planilha de materialidade/riscos/programas.
3. `03_base_sintetica/`: manifesto, testes, amostras e ZIP com 500 mil linhas de imobilizado simulado.
4. `04_papeis_trabalho/`: matriz de PTs, minutas, aprofundamento de PT 320/500/520/530 e complementares.
5. `05_codigo/`: gerador Python reproduzível.
6. `06_revisao/`: conferência dos códigos, pendências e checklist antes do PDF final.

## Números oficiais de referência

Valores do **balanço consolidado de 31/12/2025**, DFP versão 2, expressos na publicação em milhares de reais:

| Indicador | R$ mil | Fonte |
|---|---:|---|
| Ativo total | 33.553.574 | DFP 2025, página impressa 11 (página física 12) |
| Imobilizado | 10.994.169 | DFP 2025, página impressa 11 (página física 12) |
| Caixa e equivalentes | 8.871.892 | DFP 2025, página impressa 11 (página física 12) |
| Receita líquida | 18.025.121 | DFP 2025, página impressa 13 (página física 14) |

A materialidade global acadêmica foi preliminarmente definida em 0,5% da receita líquida, ou **R$ 90.125.605**, sem representar limite normativo obrigatório.

## Base simulada e reprodutibilidade

- Registros: **500.000**; semente: `20251031`.
- Valor líquido total: **R$ 10.994.169.000,00** (conciliação matemática com o saldo publicado).
- Exceções fictícias: **280**; seleções dirigidas: **280**; seleções aleatórias: **120**.
- O arquivo ZIP contém um CSV grande. Os valores monetários das linhas estão em **centavos**, conforme dicionário da planilha de testes.

Execute a partir da raiz do repositório:

```bash
python 05_codigo/validar_base.py
```

Para regenerar os dados (substitui ZIP, amostras e manifesto; requer espaço em disco):

```bash
python 05_codigo/gerar_base_imobilizado.py
```

A conciliação exata é uma propriedade do algoritmo e **não demonstra existência, completude, direitos, avaliação ou controle real de bens da CSN Mineração**.

## Classificação das evidências

- **Fonte pública:** números, políticas e informações efetivamente presentes na DFP e documentos públicos.
- **Procedimento planejado:** ações que exigiriam acesso a razão auxiliar, documentos, confirmações e controles internos não disponibilizados.
- **Simulação:** registros e exceções criados artificialmente para demonstrar técnicas de auditoria.

## Situação e limitações

Esta é a **Etapa 7 — pacote pré-final para revisão**. O roteiro original foi conferido: contém **27 PTs obrigatórios**. O **PT SÍNTESE é complementar**, não uma 28ª exigência. Veja `06_revisao/PARECER_DE_CONFERENCIA_DO_ENUNCIADO.md`. A cobertura das demais normas do intervalo NBC TA 200–600 e a completude de cada PT ainda exigem validação. As referências específicas, programas e conclusões precisam da revisão final descrita em `06_revisao/CHECKLIST_PRE_ENTREGA.md`.

## Publicação e autoria

Este pacote foi organizado localmente para futura publicação; **não foi enviado ao GitHub**. Verifique os direitos de redistribuição dos PDFs públicos antes de publicar os documentos integrais. Alternativamente, mantenha links oficiais e não publique as cópias. Não inclua dados pessoais, credenciais ou informações confidenciais.

## Integridade

`INVENTARIO_SHA256.csv` lista os arquivos incluídos e seus hashes SHA-256. Arquivos finais ainda não produzidos não constam no pacote.

## Guia de publicação no GitHub

Siga o roteiro em [`07_guia_github/PASSO_A_PASSO_PUBLICACAO.md`](07_guia_github/PASSO_A_PASSO_PUBLICACAO.md). Prefira criar o repositório como **privado** até concluir a revisão.
