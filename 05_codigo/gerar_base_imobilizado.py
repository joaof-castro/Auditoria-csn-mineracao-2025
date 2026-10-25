"""Geração reproduzível de base inteiramente SINTÉTICA de imobilizado — projeto acadêmico.
Não representa razão auxiliar, controles ou bens efetivos da CSN Mineração S.A.
Execute a partir de qualquer pasta: python 05_codigo/gerar_base_imobilizado.py
"""
import csv, random, zipfile, json, collections, io
from datetime import date, timedelta
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'03_base_sintetica'; OUT.mkdir(parents=True,exist_ok=True)
N=500_000; SEED=20251031; CUTOFF=date(2025,12,31)
TARGET_CENTS=1_099_416_900_000  # DFP consolidada: R$ 10.994.169 mil
rng=random.Random(SEED)
weights=[rng.randint(100,10000) for _ in range(N)]
W=sum(weights)
net=[TARGET_CENTS*w//W for w in weights]
net[-1]+=TARGET_CENTS-sum(net)
assert sum(net)==TARGET_CENTS
cats=['Máquinas e equipamentos','Instalações industriais','Obras em andamento','Veículos e equipamentos móveis','Edificações','Infraestrutura de mina','Direito de uso']
locations=['Congonhas/MG','Arcos/MG','Operação logística','Outras unidades']
flags={}
for label,begin,count in [('SEM_DOCUMENTO',500,70),('SEM_LOCALIZACAO',1500,60),('DATA_FUTURA',2500,45),('SEM_RESPONSAVEL',3500,55),('STATUS_INCONSISTENTE',4500,50)]:
    for i in range(begin,begin+count): flags[i]=label
head=['id_ativo','categoria','unidade','data_aquisicao','data_inicio_uso','status','responsavel','documento_suporte','custo_historico_centavos','depreciacao_acumulada_centavos','valor_contabil_liquido_centavos','excecao_inserida','natureza_dado']
counts=collections.Counter(); gross=dep=0; random_rows=[]; directed=[]
# Seleção aleatória independente: há potencial sobreposição, quantificada no manifesto.
random_ids=set(rng.sample(range(N),120))
with zipfile.ZipFile(OUT/'base_imobilizado_500mil.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    with z.open('base_imobilizado_sintetica_500000.csv','w') as raw:
        f=io.TextIOWrapper(raw,encoding='utf-8',newline='');wr=csv.writer(f);wr.writerow(head)
        for i,nv in enumerate(net):
            cat=cats[i%len(cats)]; loc=locations[i%len(locations)]; ex=flags.get(i,'')
            factor=0 if cat=='Obras em andamento' else rng.randint(10,160)
            da=nv*factor//100;cost=nv+da
            # Todos os registros ordinários têm aquisição e início de uso até a data-base.
            acquired=date(2012,1,1)+timedelta(days=rng.randint(0,(CUTOFF-date(2012,1,1)).days))
            max_delay=(CUTOFF-acquired).days
            use=acquired+timedelta(days=rng.randint(0,min(180,max_delay)))
            if ex=='DATA_FUTURA': use=date(2026,1,15)
            if ex=='SEM_LOCALIZACAO':loc=''
            status='INATIVO' if ex=='STATUS_INCONSISTENTE' else 'ATIVO'
            resp='' if ex=='SEM_RESPONSAVEL' else 'RESP-'+str(i%125+1).zfill(3)
            doc='' if ex=='SEM_DOCUMENTO' else 'DOC-SIM-'+str(i+1).zfill(7)
            row=[f'ATV-{i+1:07d}',cat,loc,acquired.isoformat(),use.isoformat(),status,resp,doc,cost,da,nv,ex,'SIMULADO']
            wr.writerow(row);gross+=cost;dep+=da;counts[ex or 'SEM_EXCECAO']+=1
            if ex:directed.append(row)
            if i in random_ids:random_rows.append(row)
        f.flush()
    z.writestr('LEIA-ME.txt','Base 100% SINTÉTICA. Valores monetários em centavos. Não corresponde ao razão auxiliar real da CSN Mineração. O saldo líquido foi forçado a conciliar matematicamente com a DFP consolidada 2025.\n')
assert gross-dep==TARGET_CENTS
random_flagged=sum(bool(row[11]) for row in random_rows)
overlap={row[0] for row in directed}&{row[0] for row in random_rows}
manifest={'empresa':'CSN MINERAÇÃO S.A.','exercicio':2025,'natureza':'BASE SINTÉTICA','fonte':'DFP 2025 CSN Mineração S.A., versão 2, balanço consolidado, página impressa 11','registros':N,'seed':SEED,'valor_liquido_centavos':TARGET_CENTS,'custo_total_centavos':gross,'depreciacao_total_centavos':dep,'diferenca_conciliacao_centavos':0,'excecoes':dict(counts),'amostra_aleatoria':len(random_rows),'amostra_dirigida_excecoes':len(directed),'excecoes_na_amostra_aleatoria':random_flagged,'sobreposicao_ids':len(overlap),'ids_unicos_selecionados':len(random_rows)+len(directed)-len(overlap),'data_base':'2025-12-31','versao_gerador':'2.0'}
(OUT/'manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
with (OUT/'amostras.csv').open('w',encoding='utf-8-sig',newline='') as f:
    wr=csv.writer(f);wr.writerow(['tipo_selecao']+head)
    for row in directed:wr.writerow(['DIRIGIDA_EXCECAO']+row)
    for row in random_rows:wr.writerow(['ALEATORIA']+row)
print(json.dumps(manifest,ensure_ascii=False,indent=2))
