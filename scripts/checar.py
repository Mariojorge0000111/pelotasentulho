# Confere tamanho de título/descrição, contagem de palavras e palavras-chave repetidas dos artigos.
import re, glob, sys, collections
kw = collections.Counter(); ok = True
for f in sorted(glob.glob('src/content/blog/*.md')):
    t = open(f).read()
    fm, corpo = t.split('---', 2)[1], t.split('---', 2)[2]
    g = lambda k: (re.search(rf'^{k}: "(.*)"$', fm, re.M) or [None, ''])[1]
    tit, desc, data, pk = g('titulo'), g('descricao'), g('data'), g('palavraChave')
    faq = len(re.findall(r'^  - p:', fm, re.M))
    palavras = len(re.findall(r'\w+', corpo)) + len(re.findall(r'\w+', fm.split('faq:')[-1]))
    kw[pk] += 1
    alerta = []
    if len(tit) > 60: alerta.append(f'titulo {len(tit)}')
    if not 120 <= len(desc) <= 160: alerta.append(f'desc {len(desc)}')
    if not 800 <= palavras <= 1700: alerta.append(f'palavras {palavras}')
    if '[[CTA]]' not in corpo: alerta.append('sem CTA')
    if faq < 2: alerta.append('faq')
    print(f"{data} {f.split('/')[-1][:45]:45} {palavras:5}p t{len(tit)} d{len(desc)} {' '.join(alerta)}")
    ok = ok and not alerta
for k, n in kw.items():
    if n > 1: print('PALAVRA-CHAVE REPETIDA', k); ok = False
print('Total', sum(kw.values()), 'OK' if ok else 'COM ALERTAS')
