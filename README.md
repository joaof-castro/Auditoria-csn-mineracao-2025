# Dossiê acadêmico de auditoria — CSN Mineração S.A. (CMIN3) — 2025

**Universidade de Brasília • Auditoria 1 (CCA0024), turma 02**  
**João Francisco de Castro Albuquerque — matrícula 241021720**  
**Professor Lucas Oliveira Gomes Ferreira**

## Documento principal
- **[Dossiê em PDF](08_Dossiê/Dossie_Academico_CSN_Mineracao_2025.pdf)** — 27 PTs, sumário, programas, evidências e anexos.
- [Word editável](08_Dossiê/Dossie_CSN_Mineracao_2025_WORD.docx).
- [Parecer de conferência](06_revisao/STATUS_FINAL_DE_CONFERENCIA.md) — requisitos atendidos e verificações ainda abertas.

## Estrutura
`08_Dossiê/` — dossiê final em PDF e Word e programa de estoques; `01_fontes_publicas/` — DFP 2024 e 2025 V2 e Formulário de Referência 2026; `02_planejamento/` — riscos, materialidade e seis ciclos; `03_base_sintetica/` — dados fictícios, dicionário, amostras, testes; `04_papeis_trabalho/` — 27 PTs e cálculos complementares; `05_codigo/` — gerador e validador; `06_revisao/` — enunciado transcrito, pareceres e testes; `07_fontes_e_matrizes/` — matriz das normas, rastreabilidade e limitações.

## Reprodução da base didática
Na raiz do repositório, com Python 3 (biblioteca padrão):
```bash
python 05_codigo/validar_base.py
# Atenção: o comando abaixo recria e sobrescreve os arquivos sintéticos
python 05_codigo/gerar_base_imobilizado.py
python 05_codigo/validar_base.py
```
A base ZIP contém **500.000 registros individuais sintéticos**, com 280 exceções intencionais. O saldo líquido total foi construído para coincidir com o imobilizado consolidado de 2025 (R$ 10.994.169.000). A seleção inclui 120 registros aleatórios e 280 dirigidos às exceções; não é amostra da população real. **Nenhuma exceção simulada é uma acusação contra a companhia.**

## Escopo e ressalvas
O dossiê foi desenvolvido a partir de documentos públicos e simulações acadêmicas, sem contato com a companhia, auditores ou terceiros, sem acesso a sistemas internos e sem opinião profissional. A opinião sem ressalvas reproduzida é **do auditor independente contratado** (DFP V2 pp. 111–114), não do estudante. A matriz `07_fontes_e_matrizes/MATRIZ_NORMAS_E_PT.csv` lista versões normativas e produtos, mas a conferência individual de **todos os itens numerados** permanece aberta, assim como a URL oficial primária exata da DFP V2. Não declarar revisão normativa integral sem concluir essas verificações.

## Fontes
`07_fontes_e_matrizes/RASTREABILIDADE_DOCUMENTAL_2025.md` contém links, datas de consulta, documentos, páginas e valores; os arquivos públicos usados estão em `01_fontes_publicas/`. Conferir licenças de redistribuição dos PDFs em repositório público.

## Programas de auditoria
Os seis ciclos (receitas, disponibilidades, estoques, imobilizado, passivos e estimativas) constam da planilha `02_planejamento/Etapa2_Materialidade_Riscos_Programas.xlsx`; programa complementar de estoques em `08_Dossiê/PROGRAMA_ESTOQUES.md`. A completude de cada programa requer revisão acadêmica.

## Status documental em 25/10/2026
O PDF final está publicado em `08_Dossiê/`. Alguns relatórios da pasta `06_revisao/` são registros históricos de etapas anteriores e não representam o estado atual. Consultar `06_revisao/STATUS_FINAL_DE_CONFERENCIA.md` para as ressalvas ainda abertas. Não alegar verificação integral de itens normativos nem execução de auditoria profissional.
