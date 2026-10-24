"""Validação em streaming do arquivo sintético ZIP, sem carregar 500 mil linhas na RAM."""
import csv,json,zipfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base=root/'03_base_sintetica'
manifest=json.loads((base/'manifesto.json').read_text(encoding='utf8'))
count=net=gross=dep=exceptions=0
with zipfile.ZipFile(base/'base_imobilizado_500mil.zip') as z:
 with z.open('base_imobilizado_sintetica_500000.csv') as raw:
  import io
  for row in csv.DictReader(io.TextIOWrapper(raw,encoding='utf8')):
   count+=1
   net+=int(row['valor_contabil_liquido_centavos'])
   gross+=int(row['custo_historico_centavos'])
   dep+=int(row['depreciacao_acumulada_centavos'])
   exceptions+=bool(row['excecao_inserida'])
   assert row['natureza_dado']=='SIMULADO'
assert count==manifest['registros']==500000
assert net==manifest['valor_liquido_centavos']==1099416900000
assert gross-dep==net
assert exceptions==280
print('OK:',count,'registros; valor líquido R$',f'{net/100:,.2f}','; exceções:',exceptions)
