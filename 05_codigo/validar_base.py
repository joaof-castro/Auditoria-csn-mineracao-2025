"""Validação independente em streaming da base sintética, manifesto e amostras."""
import csv,json,zipfile,io,collections
from datetime import date
from pathlib import Path
root=Path(__file__).resolve().parents[1];base=root/'03_base_sintetica'
m=json.loads((base/'manifesto.json').read_text(encoding='utf-8'))
counts=collections.Counter(); n=net=gross=dep=0;ids=set();flags={};future_unflagged=0
with zipfile.ZipFile(base/'base_imobilizado_500mil.zip') as z:
    with z.open('base_imobilizado_sintetica_500000.csv') as raw:
        for row in csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8')):
            n+=1;id_=row['id_ativo'];assert id_ not in ids;ids.add(id_)
            nv=int(row['valor_contabil_liquido_centavos']);co=int(row['custo_historico_centavos']);de=int(row['depreciacao_acumulada_centavos'])
            assert co-de==nv and nv>=0 and de>=0
            net+=nv;gross+=co;dep+=de
            flag=row['excecao_inserida'];counts[flag or 'SEM_EXCECAO']+=1
            if flag:flags[id_]=flag
            assert row['natureza_dado']=='SIMULADO'
            if row['data_inicio_uso']>'2025-12-31' and flag!='DATA_FUTURA':future_unflagged+=1
assert n==m['registros']==500000
assert net==m['valor_liquido_centavos']==1099416900000
assert gross==m['custo_total_centavos'] and dep==m['depreciacao_total_centavos'] and gross-dep==net
assert dict(counts)==m['excecoes'] and sum(v for k,v in counts.items() if k!='SEM_EXCECAO')==280
assert future_unflagged==0
sample_counts=collections.Counter();sample_ids={}; random_flagged=0
with (base/'amostras.csv').open(encoding='utf-8-sig',newline='') as f:
    for row in csv.DictReader(f):
        kind=row['tipo_selecao'];sample_counts[kind]+=1;sample_ids.setdefault(kind,set()).add(row['id_ativo'])
        assert row['id_ativo'] in ids
        if kind=='DIRIGIDA_EXCECAO':assert flags.get(row['id_ativo'])==row['excecao_inserida']
        elif kind=='ALEATORIA':random_flagged+=bool(row['excecao_inserida'])
        else:raise AssertionError('Tipo de seleção inesperado')
assert sample_counts=={'DIRIGIDA_EXCECAO':280,'ALEATORIA':120}
assert len(sample_ids['DIRIGIDA_EXCECAO'])==280 and len(sample_ids['ALEATORIA'])==120
assert sample_ids['DIRIGIDA_EXCECAO']==set(flags)
overlap=len(sample_ids['DIRIGIDA_EXCECAO']&sample_ids['ALEATORIA'])
assert overlap==m['sobreposicao_ids'] and random_flagged==m['excecoes_na_amostra_aleatoria']
assert len(sample_ids['DIRIGIDA_EXCECAO']|sample_ids['ALEATORIA'])==m['ids_unicos_selecionados']
print(json.dumps({'status':'OK','registros':n,'saldo_liquido_reais':net/100,'excecoes':280,'amostras':dict(sample_counts),'sobreposicao':overlap,'ids_unicos':m['ids_unicos_selecionados'],'datas_futuras_sem_flag':future_unflagged},ensure_ascii=False,indent=2))
