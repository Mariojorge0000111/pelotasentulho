import { POSTS } from '../lib/posts';

// Silos do blog: cada artigo pertence a um, e cada silo tem uma página pilar
export interface Silo {
  slug: string;
  nome: string;
  titulo: string;
  descricao: string;
  intro: string;
  pilar: { href: string; nome: string };
}

export const SILOS: Silo[] = [
  {
    slug: 'contratar-cacamba',
    nome: 'Contratar caçamba',
    titulo: 'Como Contratar Caçamba de Entulho em Pelotas',
    descricao: 'Guias para contratar caçamba de entulho e tele entulho em Pelotas RS: preço, prazo, como pedir, onde colocar e como checar se a empresa é autorizada.',
    intro: 'O que saber antes de fechar o aluguel da caçamba: como pedir, o que muda o preço, quanto tempo ela fica e como saber se a coletora é de empresa autorizada.',
    pilar: { href: '/aluguel-de-cacamba-de-entulho/', nome: 'Aluguel de caçamba de entulho em Pelotas' },
  },
  {
    slug: 'tamanhos-e-calculo',
    nome: 'Tamanhos e cálculo',
    titulo: 'Tamanho de Caçamba e Cálculo de Entulho: Guias',
    descricao: 'Qual tamanho de caçamba pedir, quanto cabe numa de 4 m³, como calcular o volume de entulho e quando sacos bastam. Guias práticos com as contas.',
    intro: 'As contas que evitam pedir caçamba grande demais ou pequena demais: volume, peso, carrinhos de mão e sacos.',
    pilar: { href: '/tamanhos-de-cacamba/', nome: 'Tamanhos de caçamba: 3, 4 e 5 m³' },
  },
  {
    slug: 'o-que-vai-na-cacamba',
    nome: 'O que vai na caçamba',
    titulo: 'O Que Pode e Não Pode na Caçamba: Guias por Material',
    descricao: 'Gesso, madeira, poda, terra, telha e móveis: o que pode ir na caçamba de entulho, o que vai separado e o que tem destino próprio em Pelotas.',
    intro: 'Material por material: o que a caçamba de entulho recebe, o que precisa ir separado e o que tem destino próprio.',
    pilar: { href: '/blog/o-que-pode-jogar-na-cacamba/', nome: 'O que pode e o que não pode na caçamba' },
  },
  {
    slug: 'regras-e-descarte',
    nome: 'Regras e descarte',
    titulo: 'Regras para Caçamba e Descarte de Entulho em Pelotas',
    descricao: 'Lei 4.850/2002 de Pelotas, caçamba na rua, Ecopontos do Sanep, bota-fora, reciclagem e multa por descarte irregular. Com as fontes oficiais.',
    intro: 'O que a lei de Pelotas exige de quem usa caçamba, onde descartar entulho de forma correta e como evitar multa.',
    pilar: { href: '/blog/cacamba-na-rua-em-pelotas/', nome: 'Caçamba na rua em Pelotas: o que diz a lei' },
  },
  {
    slug: 'entulho-por-obra',
    nome: 'Entulho por tipo de obra',
    titulo: 'Entulho por Tipo de Obra: Reforma, Demolição e Terreno',
    descricao: 'Quanto entulho sai de reforma de banheiro, cozinha, demolição, casarão antigo e limpeza de terreno em Pelotas, e qual caçamba pedir em cada caso.',
    intro: 'Cada obra gera um entulho diferente. Veja o que esperar e qual caçamba pedir para a sua.',
    pilar: { href: '/cacamba-para-obra-e-reforma/', nome: 'Caçamba para obra e reforma' },
  },
];

export const siloPorSlug = (s: string) => SILOS.find((x) => x.slug === s);
export const postsDoSilo = (s: string) => POSTS.filter((p) => p.silo === s);
