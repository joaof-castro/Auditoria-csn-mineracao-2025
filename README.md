# Auditoria acadêmica — CSN Mineração S.A. (CMIN3) | 2025

**Trabalho acadêmico, independente da companhia.** Não constitui auditoria independente, asseguração ou opinião profissional. A base de imobilizado com 500 mil registros é **inteiramente sintética**.

## Estado do projeto
**Repositório completo para revisão acadêmica; dossiê definitivo ainda não aprovado.**
O caderno integrado é uma **versão para revisão**, com possíveis redundâncias e referências normativas/bibliográficas a conferir. Não apresentá-lo como relatório final de auditoria.

## Estrutura
- `00_dossie_preliminar/` — versão inicial consolidada (não definitiva).
- `01_fontes_publicas/` — DFP 2024, DFP 2025 e Formulário de Referência 2026.
- `02_planejamento/` — análises, materialidade, riscos e programas.
- `03_base_sintetica/` — base didática, manifesto, amostras e testes.
- `04_papeis_trabalho/` — planilhas e cadernos dos PTs, incluindo Etapas 9 e 10.
- `05_codigo/` — gerador e validador da base sintética.
- `06_revisao/` — caderno integrado, validações, pendências e checklists.
- `07_fontes_e_matrizes/` — matriz de 27 PTs e limitações das fontes.
- `INVENTARIO_SHA256.csv` — hashes de integridade dos arquivos.
- `GUIA_PUBLICACAO.md` — instruções de substituição segura.

## Base didática e conciliação
A DFP 2025 versão 2 registra imobilizado consolidado de R$ 10.994.169 mil. O total líquido da base simulada foi **construído** para coincidir matematicamente com esse valor. Isso não comprova existência, titularidade, completude ou avaliação dos ativos reais. As 280 exceções simuladas não são alegações contra a companhia e não equivalem automaticamente a distorções monetárias.

```bash
python 05_codigo/validar_base.py
```

Para gerar novamente a base, utilize `python 05_codigo/gerar_base_imobilizado.py` (sobrescreve os arquivos sintéticos).

## Uso acadêmico
Separar rigorosamente: (1) informações efetivamente documentadas em fontes públicas; (2) procedimentos planejados que exigiriam acesso a dados internos; e (3) simulações exclusivamente didáticas. Conferir itens normativos, notas explicativas e referências antes da entrega. O inventário registra a integridade, não a validade científica do conteúdo.

## Atenção
Não publicar dados pessoais, credenciais ou informações sigilosas. Verificar os direitos de redistribuição dos PDFs públicos.
