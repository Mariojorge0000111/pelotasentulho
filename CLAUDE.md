# pelotasentulho · Pelotas Entulho (pelotasentulho.com.br)

Site de aluguel (rank and rent) do Mário Jorge. Ranqueia no Google para tele entulho / caçamba de entulho / coletora de entulho em Pelotas (RS). Os leads vão para o WhatsApp dele (5555991438702) e ele mesmo os repassa. Marca genérica "Pelotas Entulho": quando o site for alugado, troca-se só o `src/config.ts` (nome, WhatsApp, horário, empresa, GA4).

## Stack e publicação
- Astro 7 + @astrojs/sitemap, Node 22 (`.node-version`). `trailingSlash: 'always'`, CSS inline.
- Cloudflare Pages: cada push na `main` publica sozinho (build `npm run build`, saída `dist`).
- Domínio: https://pelotasentulho.com.br (registrado no Registro.br). Sitemap: `/sitemap-index.xml`.
- Antes de mexer: `git pull` (a automação diária faz commits na `main`).
- Commits: autor Mário Jorge, mensagem em português.

## Artigos agendados
- Artigos em `src/content/blog/*.md`. Frontmatter: `titulo`, `tituloSeo` (opcional), `descricao`, `data`, `silo`, `imagem`, `imagemAlt`, `palavraChave`, `faq`.
- Só entram no site os artigos com `data` <= hoje (fuso de São Paulo). Links para artigos ainda não publicados viram texto simples até a data chegar (`semLinksFuturos` em `src/lib/posts.ts`).
- `.github/workflows/publicar-agendados.yml` roda todo dia às 06:17, anota em `src/data/publicacoes.txt`, faz commit (o push dispara a Cloudflare) e avisa o IndexNow.
- `[[CTA]]` sozinho numa linha do artigo vira o botão de WhatsApp no meio do texto.
- `python3 scripts/checar.py` confere título, descrição, palavras, CTA, FAQ e palavra-chave repetida.

## Onde fica cada coisa
- Serviços na raiz: `src/data/servicos.ts` → `/<slug>/` (aluguel-de-cacamba-de-entulho, tele-entulho, recolhimento-de-entulho, cacamba-para-obra-e-reforma, tamanhos-de-cacamba, coletora-de-entulho). Template `src/pages/[servico].astro`.
- `src/data/bairros/*.json` (10 bairros, texto único) e `src/data/cidades/*.json` (6 cidades vizinhas). Template `src/components/PaginaLocal.astro`. Origem: `scripts/gerar-locais.py` (não rodar de novo por cima de edições).
- Silos do blog em `src/data/silos.ts`; páginas `/blog/categoria/<silo>/`.
- `src/components/FormOrcamento.astro`: formulário (nome, bairro, tipo de entulho, quando) que abre o WhatsApp; na home e em `/orcamento/`.
- `src/data/faq.ts`: FAQ geral (`home: true` aparece na home).
- Imagens: `public/images/<nome>.webp` (1600), `-800` e `-480`; tamanhos em `src/data/imagens.json`. `scripts/imagens.py` baixa do Pexels sem repetir IDs de `src/data/pexels-usados.json` (inclui os dos outros sites). A chave do Pexels fica com o Mário, nunca no repositório.
- IndexNow: chave em `public/a8606fee262a094fdb5ed66d4bc03e54.txt`; `scripts/indexnow.sh` envia o sitemap inteiro.
- Design: branco + superfície #f3f6f7, azul-petróleo #0b6e8a, amarelo de sinalização #f2b300, verde WhatsApp #15803d. Fonte Manrope.
- Sem crédito da SVG no rodapé (não deixar rastro da rede de sites de aluguel).

## Analytics, Cloudflare e Search Console
- Google Analytics 4: propriedade "pelotasentulho.com.br" na conta "Sites SVG" (a401060034), fluxo web 16375593817, ID `G-5883MK1R4X` em `src/config.ts` (`ga4`). Evento `clique_whatsapp` em todo link wa.me e no envio do formulário (área `formulario`).
- Pendente: marcar `clique_whatsapp` como evento principal quando ele aparecer no GA (até 24 h depois do primeiro clique).
- Cloudflare Pages: projeto `pelotasentulho` (https://pelotasentulho.pages.dev), criado em 19/11/2026, ligado ao GitHub (main, `npm run build`, `dist`).
- Domínio adicionado à Cloudflare (plano Free) em 19/11/2026. Nameservers: arnold.ns.cloudflare.com e rosemary.ns.cloudflare.com (troca no Registro.br feita pelo Mário). Depois de ativo: domínio personalizado no Pages (raiz + www), Crawler Hints ligado e Search Console por propriedade de domínio.

## Regras de conteúdo
- Título 30–60 caracteres, descrição 130–160. Um H1 por página.
- Cada artigo mira uma palavra-chave diferente; nada de disputar busca com home, serviço, bairro ou cidade.
- Honestidade: nada de endereço, CNPJ, avaliações, depoimentos, número de clientes, anos de mercado ou preço inventado. Preço só como fatores.
- Regras locais (conferidas em 19/11/2026 no SAPL da Câmara de Pelotas, https://sapl.pelotas.rs.leg.br/norma/1404): Lei Municipal nº 4.850/2002. Só empresas cadastradas e autorizadas pela SMTT (vistoria semestral); caçamba máx. 5 m³; faixas refletivas amarelas (10x30 cm); nome, telefone e número nas laterais; em frente à obra (lado oposto se proibido estacionar; senão a SMTT indica local); preferência no passeio com 1 m livre; na pista: 20 cm de sarjeta livre, altura máx. 2,30 m, 10 m da esquina; máx. 72 h por caçamba na via pública; penalidades recaem sobre a empresa (advertência, multa em URM, apreensão, suspensão, cassação). Lona no transporte e pintura em cores vivas: alteração de 2008 (Lei 5.525) citada pela prefeitura.
- Ecopontos do Sanep: JK (Av. JK, 3.195), Laranjal (R. Bom Jesus, 95, Bal. Valverde), Balsa (R. Paulo Guilayn, 201), Cerquinha (R. Eng. Hugo Veiga, 155), Gotuzzo (R. Machado de Assis, junto ao R7). Seg a sáb, 8h–12h e 13h–17h, até 1,5 m³ por pessoa. Entulho e poda vão para o aterro municipal.
- Em Pelotas a caçamba é chamada de "coletora". Cidades vizinhas: sempre "conforme agenda da empresa parceira, com possível taxa de deslocamento".
- Sem travessão longo e sem clichês de IA. Frases curtas e diretas. Texto diferente do site de Santa Maria.

## Combinados com o Mário
- Quando precisar de uma confirmação dele, mandar notificação no celular.
- Responder em português.
