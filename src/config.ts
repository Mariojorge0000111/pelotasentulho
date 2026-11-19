// =====================================================================
// CONFIGURAÇÃO DO SITE: tudo que muda quando o site for alugado fica aqui
// =====================================================================

export const SITE = {
  nome: 'Pelotas Entulho',
  slogan: 'Tele entulho e caçamba de entulho em Pelotas, RS',
  cidade: 'Pelotas',
  estado: 'RS',
  dominio: 'pelotasentulho.com.br',

  // WhatsApp com DDI + DDD + número, só números
  whatsapp: '5555991438702',
  // Telefone exibido no site (deixe vazio para não exibir)
  telefone: '',
  mensagemWhatsapp: 'Olá! Vim pelo site Pelotas Entulho e quero um orçamento de caçamba. Bairro: ',

  // Horário de atendimento (deixe vazio até combinar com a empresa parceira)
  horario: '',
  // Empresa parceira que atende (preencher quando o site for alugado)
  empresa: '',

  // ID do Google Analytics 4 (deixe vazio para não carregar o GA)
  ga4: 'G-5883MK1R4X',
};

export function linkWhatsapp(mensagem = SITE.mensagemWhatsapp): string {
  if (!SITE.whatsapp) return '/orcamento/';
  return `https://wa.me/${SITE.whatsapp}?text=${encodeURIComponent(mensagem)}`;
}

// Data de hoje no fuso de Pelotas (AAAA-MM-DD), usada para liberar artigos agendados
export function hojeISO(): string {
  return new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Sao_Paulo' }).format(new Date());
}

// Fontes oficiais usadas no conteúdo (conferidas em 19/11/2026)
export const FONTES = {
  lei4850: 'https://sapl.pelotas.rs.leg.br/norma/1404',
  lei4850Pdf: 'https://sapl.pelotas.rs.leg.br/media/sapl/public/normajuridica/2002/1404/1404_texto_integral.pdf',
  cadastroColetoras: 'https://www.pelotas.com.br/noticia/coletoras-de-entulhos-precisam-se-cadastrar-na-sstt',
  ecopontos: 'https://portal.sanep.com.br/residuos-solidos/ecopontos',
  guiaDoLixo: 'https://www.pelotas.com.br/lixo',
};
