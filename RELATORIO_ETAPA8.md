# Etapa 8 — Correção e validação reproduzível da base sintética

**Preparador:** João Francisco de Castro Albuquerque — matrícula 241021720  
**Empresa:** CSN Mineração S.A. — exercício 2025  
**Natureza:** estudo acadêmico, sem asseguração profissional

## Procedimentos efetivamente executados

1. Padronizados os nomes do gerador e do validador: `base_imobilizado_500mil.zip`, `manifesto.json` e `amostras.csv`.
2. Limitadas as datas de aquisição e início de uso de registros ordinários à data-base 31/12/2025. Os 45 registros com data futura permanecem identificados como exceções simuladas.
3. Mantidos os 500.000 registros, a semente 20251031 e a conciliação matemática ao saldo consolidado do imobilizado divulgado na DFP 2025.
4. Regenerados integralmente os três arquivos, a partir do código desta etapa.
5. Executado o validador, que verificou a quantidade, a unicidade dos IDs, o saldo, a relação custo menos depreciação, a natureza sintética, a distribuição das exceções, as amostras e as datas.

## Resultado confirmado

- Registros: **500.000**.
- Saldo líquido: **R$ 10.994.169.000,00**.
- Diferença de conciliação: **R$ 0,00**, por construção matemática.
- Exceções deliberadas: **280**.
- Seleção dirigida: **280**; seleção aleatória: **120**.
- Sobreposição de IDs: **0**; IDs únicos: **400**.
- Datas futuras não sinalizadas: **0**.
- Status do validador: **OK**.

## Limitações e pontos a desenvolver

- A base é integralmente simulada. Não evidencia saldos individuais, controle patrimonial, existência física ou distorções reais da CSN Mineração.
- A seleção dirigida inclui intencionalmente todos os casos marcados, sem inferência estatística.
- A seleção aleatória é uma amostra aleatória simples de registros sintéticos; qualquer inferência se restringe à população sintética e depende da natureza do teste.
- As flags documentais/cadastrais não representam automaticamente distorções monetárias; evitar projeção monetária indevida no PT 450 e PT 530.
- As categorias, locais, responsáveis, documentos e políticas de depreciação são **premissas fictícias** e não devem ser atribuídas à companhia.
- A próxima revisão deve testar premissas de depreciação, plausibilidade das categorias e integração das análises com os PT 500, 520, 530 e 540.

## Instruções de reprodução

A partir da raiz desta pasta:

```bash
python 05_codigo/gerar_base_imobilizado.py
python 05_codigo/validar_base.py
```

A execução do gerador substitui os três arquivos de dados na pasta `03_base_sintetica`. Recomenda-se arquivar as versões anteriores antes da atualização do repositório GitHub.
