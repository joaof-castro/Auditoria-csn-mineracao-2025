# Dicionário da base sintética de imobilizado (500.000 linhas)

**Origem:** gerador `05_codigo/gerar_base_imobilizado.py` (seed 20251031). **Formato:** CSV UTF-8 dentro de `03_base_sintetica/base_imobilizado_500mil.zip`. **Natureza:** 100% sintética.

| Variável | Tipo | Significado e domínio |
|---|---|---|
| `id_ativo` | texto | Chave única `ATV-0000001` a `ATV-0500000`. |
| `categoria` | texto | Categoria simulada: máquinas/equipamentos, instalações, obras, veículos, edificações, infraestrutura, direito de uso. |
| `unidade` | texto | Localização/unidade simulada; vazia nas 60 flags `SEM_LOCALIZACAO`. |
| `data_aquisicao` | data ISO `AAAA-MM-DD` | Data sintética de aquisição entre 2012 e 2025. |
| `data_inicio_uso` | data ISO `AAAA-MM-DD` | Início de uso simulado; 45 datas futuras inseridas intencionalmente. |
| `status` | texto | `ATIVO` ou `INATIVO` em flags de inconsistência. |
| `responsavel` | texto | Identificador `RESP-xxx`; vazio em 55 exceções. |
| `documento_suporte` | texto | Identificador documental fictício `DOC-SIM-xxxxxxx`; vazio em 70 exceções. |
| `custo_historico_centavos` | inteiro | Custo histórico simulado em centavos de R$. |
| `depreciacao_acumulada_centavos` | inteiro | Depreciação acumulada simulada em centavos de R$. |
| `valor_contabil_liquido_centavos` | inteiro | Custo menos depreciação em centavos de R$. |
| `excecao_inserida` | texto | Vazio ou `SEM_DOCUMENTO`, `SEM_LOCALIZACAO`, `DATA_FUTURA`, `SEM_RESPONSAVEL`, `STATUS_INCONSISTENTE`. |
| `natureza_dado` | texto | Sempre `SIMULADO`. |

**Relação de conciliação:** `custo_historico_centavos - depreciacao_acumulada_centavos = valor_contabil_liquido_centavos`, em todas as linhas. O somatório líquido foi **forçado** para R$ 10.994.169.000,00, não obtido por análise de registros reais. O arquivo `manifesto.json` guarda os totais e a distribuição de flags. O arquivo `amostras.csv` guarda as 120 seleções aleatórias e 280 dirigidas.
