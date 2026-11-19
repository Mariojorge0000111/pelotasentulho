# Busca fotos no Pexels (sem repetir as já usadas nos sites de aluguel) e gera WebP 1600, 800 e 480.
# Uso: PK=<chave> python3 scripts/imagens.py <lista.json>   (lista: [[nome, busca], ...])
import json, os, sys, io, urllib.request, urllib.parse
from PIL import Image
KEY = os.environ['PK']
lista = json.load(open(sys.argv[1]))
usados_p, tam_p, cred_p = 'src/data/pexels-usados.json', 'src/data/imagens.json', 'scripts/imagens-origem.json'
usados = set(json.load(open(usados_p)))
tam = json.load(open(tam_p)) if os.path.exists(tam_p) else {}
cred = json.load(open(cred_p)) if os.path.exists(cred_p) else {}
def get(url):
    req = urllib.request.Request(url, headers={'Authorization': KEY, 'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req, timeout=60).read()
for item in lista:
    nome, q = item[0], item[1]
    pular = int(item[2]) if len(item) > 2 else 0
    if nome in tam: continue
    d = json.loads(get('https://api.pexels.com/v1/search?' + urllib.parse.urlencode({'query': q, 'per_page': 40, 'orientation': 'landscape'})))
    cand = [p for p in d['photos'] if p['id'] not in usados and p['width'] >= 1600]
    if len(cand) <= pular:
        print('SEM FOTO', nome, q); continue
    foto = cand[pular]
    raw = get(foto['src']['original'] + '?auto=compress&cs=tinysrgb&w=1600')
    im = Image.open(io.BytesIO(raw)).convert('RGB')
    if im.width > 1600: im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
    im.save(f'public/images/{nome}.webp', 'WEBP', quality=72, method=6)
    for w in (800, 480):
        im.resize((w, round(im.height * w / im.width)), Image.LANCZOS).save(f'public/images/{nome}-{w}.webp', 'WEBP', quality=72, method=6)
    tam[nome] = [im.width, im.height]
    usados.add(foto['id'])
    cred[nome] = {'id': foto['id'], 'alt': foto['alt'], 'fotografo': foto['photographer'], 'busca': q}
    print(nome, foto['id'], '|', foto['alt'][:100])
json.dump(sorted(usados), open(usados_p, 'w'))
json.dump(tam, open(tam_p, 'w'), indent=0)
json.dump(cred, open(cred_p, 'w'), indent=1, ensure_ascii=False)
