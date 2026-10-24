"""Base SINTÉTICA para ensino; não representa razão auxiliar real da CSN Mineração."""
import csv, random, zipfile, json, hashlib, collections, io
from datetime import date, timedelta
from pathlib import Path
OUT=Path(__file__).resolve().parents[1] / '03_base_sintetica'; OUT.mkdir(parents=True,exist_ok=True); N=500_000; SEED=20251031
TARGET_CENTS=1_099_416_900_000 # R$ 10.994.169.000 (DFP consolidada, R$ mil 10.994.169)
rng=random.Random(SEED)
# Partition exact published net book value among 500,000 synthetic records.
weights=[rng.randint(100,10000) for _ in range(N)]
W=sum(weights)
net=[TARGET_CENTS*w//W for w in weights]
net[-1]+=TARGET_CENTS-sum(net)
assert sum(net)==TARGET_CENTS
cats=['Máquinas e equipamentos','Instalações industriais','Obras em andamento','Veículos e equipamentos móveis','Edificações','Infraestrutura de mina','Direito de uso']
locations=['Congonhas/MG','Arcos/MG','Operação logística','Outras unidades']
flags={}
# Deliberately injected control exceptions, NOT allegations against the company.
for label,begin,count in [('SEM_DOCUMENTO',500,70),('SEM_LOCALIZACAO',1500,60),('DATA_FUTURA',2500,45),('SEM_RESPONSAVEL',3500,55),('STATUS_INCONSISTENTE',4500,50)]:
 for i in range(begin,begin+count): flags[i]=label
head=['id_ativo','categoria','unidade','data_aquisicao','data_inicio_uso','status','responsavel','documento_suporte','custo_historico_centavos','depreciacao_acumulada_centavos','valor_contabil_liquido_centavos','excecao_inserida','natureza_dado']
counts=collections.Counter(); gross=0; dep=0; samples=[]; flagged=[]; seen_ids=set()
random_sample=set(rng.sample(range(N),120))
with zipfile.ZipFile(OUT/'CSN_Mineracao_2025_Base_Sintetica_500mil.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 with z.open('base_imobilizado_sintetica_500000.csv','w') as raw:
  f=io.TextIOWrapper(raw,encoding='utf-8',newline=''); wr=csv.writer(f);wr.writerow(head)
  for i,nv in enumerate(net):
   cat=cats[i%len(cats)]; loc=locations[i%len(locations)]; ex=flags.get(i,'');
   factor=0 if cat=='Obras em andamento' else rng.randint(10,160)
   da=nv*factor//100; cost=nv+da
   acquired=date(2012,1,1)+timedelta(days=rng.randint(0,5100)); use=acquired+timedelta(days=rng.randint(0,180))
   if ex=='DATA_FUTURA': use=date(2026,1,15)
   if ex=='SEM_LOCALIZACAO': loc=''
   status='INATIVO' if ex=='STATUS_INCONSISTENTE' else 'ATIVO'
   resp='' if ex=='SEM_RESPONSAVEL' else 'RESP-'+str(i%125+1).zfill(3)
   doc='' if ex=='SEM_DOCUMENTO' else 'DOC-SIM-'+str(i+1).zfill(7)
   row=[f'ATV-{i+1:07d}',cat,loc,acquired.isoformat(),use.isoformat(),status,resp,doc,cost,da,nv,ex,'SIMULADO']
   wr.writerow(row);gross+=cost;dep+=da;counts[ex or 'SEM_EXCECAO']+=1
   if ex: flagged.append(row)
   if i in random_sample: samples.append(row)
  f.flush()
 z.writestr('LEIA-ME.txt','Base inteiramente SIMULADA. Valores em centavos de real. Saldo liquido conciliado apenas matematicamente ao imobilizado CONSOLIDADO da DFP CSN MINERACAO SA 31/12/2025, pagina 11 de 117 (pagina fisica 12), R$ 10.994.169 mil. Nao ha evidencia de que registros individuais existam na empresa. Excecoes deliberadamente inseridas para fins didaticos. Codigo gerador entregue separadamente.\n')
assert gross-dep==TARGET_CENTS
manifest={'empresa':'CSN MINERAÇÃO S.A.','exercicio':2025,'natureza':'BASE SINTÉTICA','fonte':'DFP 2025 CSN Mineração S.A. versão 2, balanço consolidado, página impressa 11 de 117','registros':N,'seed':SEED,'valor_liquido_centavos':TARGET_CENTS,'custo_total_centavos':gross,'depreciacao_total_centavos':dep,'diferenca_conciliacao_centavos':gross-dep-TARGET_CENTS,'excecoes':dict(counts),'amostra_aleatoria':len(samples),'amostra_dirigida_excecoes':len(flagged)}
(OUT/'CSN_Mineracao_2025_Manifesto_Base_Sintetica.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
with (OUT/'CSN_Mineracao_2025_Amostras_Auditoria.csv').open('w',encoding='utf-8-sig',newline='') as f:
 wr=csv.writer(f);wr.writerow(['tipo_selecao']+head)
 for row in flagged:wr.writerow(['DIRIGIDA_EXCECAO']+row)
 for row in samples:wr.writerow(['ALEATORIA']+row)
print(json.dumps(manifest,ensure_ascii=False,indent=2))
