import type { APIRoute } from 'astro';
import { SITE } from '../config';
import { SERVICOS } from '../data/servicos';
import { BAIRROS, CIDADES } from '../data/locais';
import { POSTS } from '../lib/posts';

export const GET: APIRoute = ({ site }) => {
  const u = (p: string) => new URL(p, site).href;
  const txt = `# ${SITE.nome}

> ${SITE.slogan}. Orçamento pelo WhatsApp. Em Pelotas a caçamba de entulho também é chamada de coletora. Caçambas de até 5 m³ (máximo da Lei Municipal nº 4.850/2002), por até 72 horas na via pública.

## Serviços
${SERVICOS.map((s) => `- [${s.nome}](${u(`/${s.slug}/`)}): ${s.curto}`).join('\n')}

## Bairros de Pelotas
${BAIRROS.map((b) => `- [${b.nome}](${u(`/bairros/${b.slug}/`)})`).join('\n')}

## Cidades vizinhas
${CIDADES.map((c) => `- [${c.nome}](${u(`/cidades/${c.slug}/`)})`).join('\n')}

## Guias
- [Perguntas frequentes](${u('/perguntas-frequentes/')})
${POSTS.map((p) => `- [${p.titulo}](${u(p.url)}): ${p.descricao}`).join('\n')}
`;
  return new Response(txt, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
