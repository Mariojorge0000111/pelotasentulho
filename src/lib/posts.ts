import { hojeISO } from '../config';

// Artigos ficam em src/content/blog/*.md. Só entram no site os que têm data <= hoje (fuso de São Paulo).
// A automação diária do GitHub (publicar-agendados.yml) refaz o site e libera os agendados na data certa.
export interface Post {
  slug: string;
  url: string;
  titulo: string;
  tituloSeo?: string;
  descricao: string;
  data: string;
  atualizado?: string;
  imagem: string;
  imagemAlt: string;
  palavraChave: string;
  silo: string;
  faq?: { p: string; r: string }[];
  Content: any;
  compiledContent: () => string | Promise<string>;
}

const arquivos = import.meta.glob('../content/blog/*.md', { eager: true }) as Record<string, any>;

export const TODOS: Post[] = Object.entries(arquivos).map(([caminho, m]) => {
  const slug = caminho.split('/').pop()!.replace(/\.md$/, '');
  return { slug, url: `/blog/${slug}/`, ...m.frontmatter, Content: m.Content, compiledContent: m.compiledContent };
});

const hoje = process.env.HOJE ?? hojeISO(); // HOJE=AAAA-MM-DD só para testes locais
export const POSTS: Post[] = TODOS.filter((p) => p.data <= hoje).sort((a, b) =>
  a.data < b.data ? 1 : a.data > b.data ? -1 : a.titulo.localeCompare(b.titulo, 'pt-BR'),
);
const publicados = new Set(POSTS.map((p) => p.slug));

export const publicado = (slug: string) => publicados.has(slug);
export const post = (slug: string) => POSTS.find((p) => p.slug === slug);

// Remove o link (mantém o texto) de artigos ainda não publicados
export function semLinksFuturos(html: string): string {
  return html.replace(/<a href="\/blog\/([a-z0-9-]+)\/"[^>]*>(.*?)<\/a>/g, (tudo, slug, texto) => (publicados.has(slug) ? tudo : texto));
}
