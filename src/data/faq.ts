export interface Pergunta {
  p: string;
  r: string;
  home?: boolean;
}

export interface Grupo {
  titulo: string;
  itens: Pergunta[];
}

export const FAQ: Grupo[] = [
  {
    titulo: 'Como funciona',
    itens: [
      {
        p: 'Como funciona o tele entulho em Pelotas?',
        r: 'Você chama no WhatsApp e informa a rua, o bairro e o tipo de entulho. Recebe o tamanho de caçamba indicado, o valor e o dia da entrega. A caçamba fica na obra, você enche e avisa quando quiser a retirada ou a troca.',
        home: true,
      },
      {
        p: 'Caçamba, coletora e tele entulho são a mesma coisa?',
        r: 'Sim. Em Pelotas a caçamba de entulho é chamada de coletora, e no Rio Grande do Sul o serviço de pedir a caçamba é conhecido como tele entulho. Também aparecem os nomes disk entulho e caçamba estacionária.',
        home: true,
      },
      {
        p: 'Com quanta antecedência devo pedir a caçamba?',
        r: 'Um ou dois dias antes da data em que a obra vai gerar entulho costuma ser suficiente. Em semanas de muita procura, quanto antes, melhor.',
      },
      {
        p: 'Preciso carregar o entulho para dentro da caçamba?',
        r: 'Normalmente sim. O serviço padrão inclui entrega, permanência e retirada da caçamba. Se precisar de ajuda para carregar, diga no pedido, porque algumas empresas oferecem isso à parte.',
      },
      {
        p: 'Quem atende os pedidos feitos pelo site?',
        r: 'O site Pelotas Entulho recebe o seu pedido e o encaminha a uma empresa de caçambas que atende Pelotas. O orçamento, o prazo e as condições são confirmados com você antes de qualquer compromisso.',
      },
    ],
  },
  {
    titulo: 'Prazo e tamanho',
    itens: [
      {
        p: 'Quanto tempo a caçamba pode ficar na rua em Pelotas?',
        r: 'Até 72 horas por caçamba, segundo a Lei Municipal nº 4.850/2002. Se a obra continuar, faz-se a troca. Dentro do terreno, vale o prazo combinado com a empresa.',
        home: true,
      },
      {
        p: 'Quais tamanhos de caçamba existem?',
        r: 'Em Pelotas a caçamba pode ter no máximo 5 m³. A mais comum é a de 4 m³, que recebe cerca de 65 carrinhos de mão de entulho. A disponibilidade de 3 e 5 m³ depende da empresa.',
        home: true,
      },
      {
        p: 'Como sei o tamanho certo para a minha obra?',
        r: 'Mande uma foto do entulho, ou do que vai ser quebrado, com o tipo de obra. Com isso dá para indicar o tamanho. Na dúvida entre dois, o maior costuma sair mais barato do que pedir uma segunda caçamba.',
      },
      {
        p: 'Posso encher a caçamba acima da borda?',
        r: 'Não. Material acima da borda cai no transporte, e o entulho precisa seguir coberto por lona ou tela. Se encheu antes do fim da obra, peça a troca.',
      },
    ],
  },
  {
    titulo: 'O que pode ir na caçamba',
    itens: [
      {
        p: 'O que pode ser jogado na caçamba de entulho?',
        r: 'Resíduo de construção: tijolo, bloco, concreto, argamassa, reboco, piso, azulejo, telha cerâmica, louça sanitária, areia e terra. Madeira, gesso, metal e poda devem ser avisados antes.',
        home: true,
      },
      {
        p: 'O que não pode ir na caçamba?',
        r: 'Lixo doméstico, restos de comida, tinta, solvente, óleo, produtos químicos, telha de amianto, pneus, eletrônicos, pilhas e lâmpadas. Esses materiais têm coleta e destino próprios.',
      },
      {
        p: 'Posso colocar galhos e poda na caçamba?',
        r: 'Depende da empresa. Poda tem destino diferente do entulho de alvenaria e ocupa muito espaço. Avise no pedido e, se possível, mande uma foto.',
      },
    ],
  },
  {
    titulo: 'Preço e pagamento',
    itens: [
      {
        p: 'Quanto custa uma caçamba de entulho em Pelotas?',
        r: 'Não há preço tabelado. O valor depende do tamanho, do bairro, dos dias de permanência e do tipo de entulho. O orçamento é feito pelo WhatsApp, sem compromisso, antes de fechar.',
        home: true,
      },
      {
        p: 'O que deixa a caçamba mais cara?',
        r: 'Material misturado ou difícil de destinar (gesso, madeira, poda), distância maior, como Laranjal, zona rural ou outra cidade, dias extras e trocas. Entulho limpo de alvenaria é o mais simples.',
      },
    ],
  },
  {
    titulo: 'Regras e descarte',
    itens: [
      {
        p: 'Preciso de autorização para colocar caçamba na frente de casa?',
        r: 'Quem precisa estar cadastrada e autorizada pela Secretaria de Transportes e Trânsito é a empresa de caçamba, conforme a Lei nº 4.850/2002. Contrate só empresa regular.',
      },
      {
        p: 'Onde a caçamba pode ficar na rua?',
        r: 'Em frente à obra, de preferência sobre o passeio, com 1 metro livre para pedestres. Na pista, só onde é permitido estacionar, a pelo menos 10 metros da esquina e com 20 cm de sarjeta livre.',
      },
      {
        p: 'Posso levar o entulho ao Ecoponto?',
        r: 'Pode, se for pouco. Os Ecopontos do Sanep recebem até 1,5 m³ por pessoa, levado pelo próprio morador. Acima disso, ou sem transporte, a caçamba é o caminho.',
      },
      {
        p: 'Vocês atendem fora de Pelotas?',
        r: 'Capão do Leão, Rio Grande, Morro Redondo, Canguçu, Arroio do Padre e Turuçu podem ser atendidos conforme a agenda da empresa parceira, com possível taxa de deslocamento. Confirme pelo WhatsApp.',
      },
    ],
  },
];

export const FAQ_HOME = FAQ.flatMap((g) => g.itens).filter((i) => i.home);
export const FAQ_TODAS = FAQ.flatMap((g) => g.itens);
