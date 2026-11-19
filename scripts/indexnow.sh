#!/usr/bin/env bash
# Avisa o IndexNow (Bing, Yandex, Seznam, Naver) sobre todas as URLs do sitemap. Rodar depois de um deploy grande.
set -e
URLS=$(curl -sS https://pelotasentulho.com.br/sitemap-0.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//' | sed 's/.*/"&"/' | paste -sd, -)
curl -sS -X POST https://api.indexnow.org/indexnow -H 'Content-Type: application/json; charset=utf-8' \
  -d "{\"host\":\"pelotasentulho.com.br\",\"key\":\"a8606fee262a094fdb5ed66d4bc03e54\",\"keyLocation\":\"https://pelotasentulho.com.br/a8606fee262a094fdb5ed66d4bc03e54.txt\",\"urlList\":[$URLS]}" -w '\nHTTP %{http_code}\n'
