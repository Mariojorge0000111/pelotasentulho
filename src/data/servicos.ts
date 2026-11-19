export interface Secao {
  h2: string;
  paragrafos: string[];
  lista?: string[];
}

export interface Servico {
  slug: string;
  nome: string;
  curto: string;
  titulo: string;
  descricao: string;
  h1: string;
  intro: string;
  imagem: string;
  imagemAlt: string;
  mensagem: string;
  silo: string;
  secoes: Secao[];
  faq: { p: string; r: string }[];
}

// Serviços ficam na raiz do site: /<slug>/
export const SERVICOS: Servico[] = [
  {
    slug: 'aluguel-de-cacamba-de-entulho',
    nome: 'Aluguel de caçamba de entulho',
    curto: 'Caçamba estacionária entregue na frente da obra, com prazo combinado e retirada quando encher.',
    titulo: 'Aluguel de Caçamba de Entulho em Pelotas RS',
    descricao: 'Aluguel e locação de caçamba de entulho em Pelotas: entrega na frente da obra, prazo combinado e retirada com destino licenciado. Orçamento no WhatsApp.',
    h1: 'Aluguel de caçamba de entulho em Pelotas',
    intro: 'Você manda o endereço e o tipo de entulho pelo WhatsApp e recebe tamanho, valor e prazo antes de fechar. A caçamba é deixada na frente da obra, você enche no seu ritmo e avisa quando estiver cheia. O caminhão recolhe e leva o entulho para um local de destino licenciado. Em Pelotas, muita gente chama esse serviço de coletora ou tele entulho.',
    imagem: 'aluguel-cacamba',
    imagemAlt: 'Caminhão poliguindaste carregando uma caçamba estacionária laranja em rua residencial, com outras caçambas verdes ao lado',
    mensagem: 'Olá! Vim pelo site Pelotas Entulho e quero alugar uma caçamba de entulho. Bairro: ',
    silo: 'contratar-cacamba',
    secoes: [
      {
        h2: 'Como funciona a locação da caçamba',
        paragrafos: [
          'A locação tem três momentos: a entrega, o período em que a caçamba fica com você e a retirada. Na entrega, o caminhão poliguindaste baixa a caçamba no ponto combinado. Dentro do terreno é sempre a melhor opção. Na rua, a caçamba fica em frente à obra, como manda a Lei Municipal nº 4.850/2002.',
          'Durante o prazo, você vai enchendo. Quando estiver cheia, avise pelo WhatsApp para agendar a retirada. Se a obra continua, peça a troca: a cheia sai e uma vazia entra no mesmo lugar, sem deixar duas caçambas ocupando a frente da casa.',
        ],
        lista: [
          'Mande endereço, bairro e o que vai descartar (foto ajuda)',
          'Receba o tamanho indicado, o valor e o prazo',
          'A caçamba chega no dia combinado',
          'Avise quando encher para retirada ou troca',
        ],
      },
      {
        h2: 'O que muda o valor do aluguel em Pelotas',
        paragrafos: [
          'Não há preço tabelado na cidade. O valor depende do tamanho da caçamba, da distância até o bairro, de quantos dias ela fica e, principalmente, do tipo de material. Entulho limpo de alvenaria, como tijolo, concreto, reboco e cerâmica, é o mais simples de destinar. Madeira, gesso, poda e material misturado podem custar mais para descartar.',
          'Por isso o orçamento é feito caso a caso, antes de qualquer compromisso. Pergunte o que está incluído: entrega, dias de permanência, retirada e quanto custa um dia extra ou uma troca. Quem vai ao Laranjal ou à zona rural deve perguntar também sobre deslocamento.',
        ],
      },
      {
        h2: 'Regras de Pelotas que valem para quem aluga',
        paragrafos: [
          'A Lei Municipal nº 4.850/2002 diz que só empresas cadastradas e autorizadas pela Secretaria de Transportes e Trânsito podem colocar caçamba na via pública. A caçamba tem no máximo 5 m³, faixas refletivas amarelas nas laterais e na frente, e o nome, o telefone e o número da caçamba pintados nas laterais.',
          'Na rua, a caçamba pode ficar no máximo 72 horas. Ela vai de preferência sobre o passeio, deixando 1 metro livre para quem passa a pé. Se ficar na pista, precisa deixar 20 cm de sarjeta livres para a água da chuva e estar a pelo menos 10 metros da esquina. Quem responde pela colocação e pela retirada é a empresa, mas vale combinar o ponto certo para não ter dor de cabeça.',
        ],
      },
      {
        h2: 'Antes de pedir, separe estas informações',
        paragrafos: [
          'Quanto mais claro o pedido, mais rápido sai o orçamento. Diga em que rua e bairro fica a obra, se a caçamba pode ficar dentro do terreno, que tipo de obra é e quando você quer começar. Uma foto do entulho, ou do cômodo que vai ser quebrado, resolve a maior parte das dúvidas sobre tamanho.',
        ],
        lista: [
          'Rua, número e bairro da obra',
          'Se há espaço no terreno ou se a caçamba fica na rua',
          'Tipo de entulho: alvenaria, piso, telha, madeira, poda',
          'Data em que você quer a caçamba',
        ],
      },
    ],
    faq: [
      {
        p: 'Quanto tempo posso ficar com a caçamba alugada?',
        r: 'O prazo é combinado no orçamento. Se a caçamba estiver na rua, a lei de Pelotas limita a permanência a 72 horas por caçamba. Dentro do terreno, o prazo depende só do que for combinado com a empresa.',
      },
      {
        p: 'Preciso estar em casa na entrega?',
        r: 'Não é obrigatório, mas ajuda. Deixe o ponto livre, sem carro estacionado, e explique bem onde a caçamba deve ficar.',
      },
      {
        p: 'Posso pedir mais de uma caçamba para a mesma obra?',
        r: 'Pode. Em obra maior o mais comum é a troca: sai a cheia e entra uma vazia no lugar, sem ocupar a rua com duas caçambas ao mesmo tempo.',
      },
      {
        p: 'Aluguel de caçamba e locação de caçamba são a mesma coisa?',
        r: 'São. Também se fala coletora, tele entulho, disk entulho e caçamba estacionária. Em todos os casos é a caixa metálica que fica na obra e depois é recolhida pelo caminhão.',
      },
    ],
  },
  {
    slug: 'tele-entulho',
    nome: 'Tele entulho',
    curto: 'Peça pelo WhatsApp: a caçamba vai até a obra e o entulho sai sem você precisar de caminhão.',
    titulo: 'Tele Entulho em Pelotas: Peça Caçamba pelo WhatsApp',
    descricao: 'Tele entulho em Pelotas RS: peça a caçamba pelo WhatsApp, receba na frente da obra e agende a retirada quando encher. Atende todos os bairros da cidade.',
    h1: 'Tele entulho em Pelotas',
    intro: 'Tele entulho é o jeito gaúcho de dizer "peça a caçamba pelo telefone". Você chama, a caçamba vem até a obra, você enche e ela vai embora com o entulho. Aqui o pedido é pelo WhatsApp: a mensagem já sai pronta, você completa com o bairro e recebe o orçamento sem compromisso.',
    imagem: 'tele-entulho',
    imagemAlt: 'Caminhão de carga coberto por lona estacionado em pátio de obra, pronto para transportar material',
    mensagem: 'Olá! Vim pelo site Pelotas Entulho (página de tele entulho) e preciso de uma caçamba. Bairro: ',
    silo: 'contratar-cacamba',
    secoes: [
      {
        h2: 'Tele entulho, disk entulho, coletora: o que é cada um',
        paragrafos: [
          'Os nomes mudam de cidade para cidade, mas o serviço é o mesmo. No Rio Grande do Sul é comum "tele entulho" e, em Pelotas, "coletora". Em outros estados aparece como disk entulho, caçamba estacionária ou contêiner de entulho. Todos falam de uma caixa metálica de até 5 m³ que fica na obra e é recolhida por um caminhão poliguindaste.',
          'O que não é tele entulho: o freteiro com caminhonete que leva sacos de entulho, ou a carroça. Esses podem ser úteis para volume muito pequeno, mas nem sempre têm destino licenciado para o material. Na dúvida, pergunte para onde vai o entulho.',
        ],
      },
      {
        h2: 'Como pedir tele entulho em 4 passos',
        paragrafos: [
          'O pedido leva poucos minutos. O que mais atrasa um orçamento é falta de informação, então mande tudo de uma vez.',
        ],
        lista: [
          'Toque no botão do WhatsApp: a mensagem já vem com o pedido',
          'Escreva o bairro, a rua e o que vai descartar',
          'Receba o tamanho indicado, o valor e o dia da entrega',
          'Quando encher, avise para retirada ou troca',
        ],
      },
      {
        h2: 'Quando o tele entulho vale mais que outras opções',
        paragrafos: [
          'Para poucos sacos de entulho de uma pequena reforma, os Ecopontos do Sanep aceitam até 1,5 m³ por pessoa, se você mesmo levar. Acima disso, ou quando não há carro para levar, a caçamba é o caminho mais prático: o entulho sai de uma vez, a obra fica limpa e você não precisa carregar nada.',
          'Também vale quando a obra gera entulho ao longo de vários dias. A caçamba fica disponível, os pedreiros jogam direto nela e a calçada não vira depósito de material solto, o que pode render problema com a fiscalização e com os vizinhos.',
        ],
      },
      {
        h2: 'Tele entulho em todos os bairros de Pelotas',
        paragrafos: [
          'O atendimento cobre as sete regiões administrativas da cidade: Centro, Fragata, Barragem, Três Vendas, Areal, São Gonçalo e Laranjal, além do Porto. Cidades vizinhas como Capão do Leão e Rio Grande podem ser atendidas conforme a agenda da empresa parceira, com possível taxa de deslocamento.',
        ],
      },
    ],
    faq: [
      {
        p: 'O tele entulho funciona no fim de semana?',
        r: 'Depende da agenda da empresa parceira. Mande a mensagem mesmo assim: o pedido fica registrado e a entrega é combinada para o primeiro horário disponível.',
      },
      {
        p: 'Quanto tempo leva para a caçamba chegar?',
        r: 'Depende do bairro e da agenda do dia. Pedidos feitos com um ou dois dias de antecedência costumam ser mais fáceis de encaixar.',
      },
      {
        p: 'Tele entulho leva móveis velhos?',
        r: 'Caçamba de entulho é para resíduo de obra. Móveis e volumosos têm destino próprio; pergunte no orçamento se dá para incluir algo junto e se há custo extra.',
      },
    ],
  },
  {
    slug: 'recolhimento-de-entulho',
    nome: 'Recolhimento de entulho',
    curto: 'Retirada e remoção de entulho de obra, reforma e limpeza de terreno, com destino licenciado.',
    titulo: 'Recolhimento e Retirada de Entulho em Pelotas',
    descricao: 'Recolhimento, retirada e remoção de entulho em Pelotas: caçamba na obra e destino licenciado para tijolo, concreto, piso e telha. Peça no WhatsApp.',
    h1: 'Recolhimento e retirada de entulho em Pelotas',
    intro: 'Entulho parado na calçada vira problema rápido: atrapalha quem passa, junta lixo e pode render multa. O recolhimento com caçamba resolve de uma vez. A caçamba fica na obra, recebe o entulho e é levada pelo caminhão para um destino licenciado. Serve para quem está no meio da obra e para quem já tem o entulho amontoado e quer se livrar dele.',
    imagem: 'recolhimento-entulho',
    imagemAlt: 'Restos de demolição amontoados na frente de um prédio, com ferragens, madeira e pedaços de alvenaria',
    mensagem: 'Olá! Vim pelo site Pelotas Entulho e preciso de recolhimento de entulho. Bairro: ',
    silo: 'regras-e-descarte',
    secoes: [
      {
        h2: 'Entulho já amontoado: como fica a retirada',
        paragrafos: [
          'Se o entulho já está no pátio ou na calçada, a caçamba é colocada o mais perto possível do monte. O carregamento para dentro da caçamba normalmente fica por conta de quem contratou, com pá e carrinho de mão. Se você precisa de ajuda para carregar, diga isso no pedido: algumas empresas oferecem o serviço à parte.',
          'Mande uma foto do monte com alguma referência de tamanho, como um carrinho de mão ou uma porta. Com isso dá para indicar se uma caçamba de 4 m³ basta ou se vão ser necessárias duas.',
        ],
      },
      {
        h2: 'Para onde vai o entulho recolhido',
        paragrafos: [
          'Entulho de obra não pode ir para terreno baldio, beira de arroio ou estrada. Em Pelotas, o Sanep encaminha o entulho que recebe nos Ecopontos para o aterro municipal. As empresas de caçamba levam o material para locais licenciados, onde parte dele pode ser triada e reaproveitada.',
          'Peça sempre que o destino seja informado. É a sua garantia de que o entulho da sua obra não vai aparecer num terreno da cidade com o seu endereço no meio dos restos.',
        ],
      },
      {
        h2: 'O que entra no recolhimento',
        paragrafos: [
          'A caçamba recebe resíduo de construção: tijolo, bloco, concreto, argamassa, reboco, piso, azulejo, telha cerâmica, louça sanitária, areia e terra. Madeira, gesso, metal e poda podem entrar em alguns casos, mas precisam ser avisados, porque têm destino diferente.',
        ],
        lista: [
          'Pode: alvenaria, concreto, piso, azulejo, telha cerâmica, louça, terra',
          'Avise antes: madeira, gesso, drywall, metal, vidro, poda',
          'Não pode: lixo doméstico, tinta, solvente, óleo, amianto, pneu, eletrônicos',
        ],
      },
    ],
    faq: [
      {
        p: 'A prefeitura recolhe entulho em Pelotas?',
        r: 'A prefeitura faz ações pontuais de recolhimento, e o Sanep mantém Ecopontos que recebem até 1,5 m³ por pessoa, levado pelo próprio morador. Para volume maior ou sem transporte próprio, a caçamba é o caminho.',
      },
      {
        p: 'Recolhimento, retirada e remoção de entulho são o mesmo serviço?',
        r: 'Sim. Todos os nomes se referem a tirar o entulho da obra e levar para um destino adequado, normalmente com caçamba estacionária.',
      },
      {
        p: 'Dá para recolher entulho de um terreno baldio?',
        r: 'Dá, desde que você seja o responsável pelo terreno ou tenha autorização do dono. Mande fotos para avaliar o volume e o tipo de material.',
      },
    ],
  },
  {
    slug: 'cacamba-para-obra-e-reforma',
    nome: 'Caçamba para obra e reforma',
    curto: 'Para reforma de banheiro, cozinha, troca de piso, demolição e construção nova.',
    titulo: 'Caçamba para Obra e Reforma em Pelotas RS',
    descricao: 'Caçamba para obra e reforma em Pelotas: banheiro, cozinha, troca de piso, telhado, demolição e construção. Veja qual tamanho pedir e chame no WhatsApp.',
    h1: 'Caçamba para obra e reforma em Pelotas',
    intro: 'Cada obra gera um tipo e uma quantidade de entulho. Uma reforma de banheiro cabe numa caçamba pequena. Uma demolição de casa pode pedir várias trocas. Aqui você vê o que esperar em cada caso e o que dizer no pedido para receber a caçamba certa.',
    imagem: 'obra-reforma',
    imagemAlt: 'Cômodo antigo em reforma, com paredes descascadas, piso de madeira gasto e vassoura encostada na parede',
    mensagem: 'Olá! Vim pelo site Pelotas Entulho e preciso de caçamba para obra/reforma. Tipo de obra e bairro: ',
    silo: 'entulho-por-obra',
    secoes: [
      {
        h2: 'Reforma de banheiro e cozinha',
        paragrafos: [
          'Quebrar piso e azulejo de um banheiro comum gera bem menos entulho do que parece, mas o material é pesado. Uma caçamba de 3 ou 4 m³ costuma bastar, mesmo com a louça e a bancada antigas. Na cozinha entram também a pia e, às vezes, parte de uma parede. O volume sobe um pouco, mas raramente passa de uma caçamba.',
        ],
      },
      {
        h2: 'Troca de piso, telhado e reforma da casa inteira',
        paragrafos: [
          'Troca de piso em vários cômodos, reboco novo e substituição de telhas geram volume maior. Telha cerâmica quebrada ocupa muito espaço por ser oca e irregular. Nesses casos, a caçamba de 5 m³, que é o máximo permitido em Pelotas, costuma ser a melhor escolha, às vezes com uma troca no meio da obra.',
          'Telha de fibrocimento antiga merece atenção: se for de amianto, não pode ir para a caçamba de entulho comum. Ela precisa de coleta e destino próprios.',
        ],
      },
      {
        h2: 'Demolição e construção nova',
        paragrafos: [
          'Demolir uma casa inteira gera dezenas de metros cúbicos. O trabalho é feito com trocas sucessivas: a caçamba enche, sai, outra entra. Combine o ritmo com a empresa antes de começar, para a máquina ou a equipe não ficar parada esperando caçamba vazia.',
          'Em construção nova, o entulho vem aos poucos: sobras de bloco, argamassa, embalagens e madeira de forma. Uma caçamba na obra durante as fases de alvenaria e acabamento mantém o canteiro organizado e evita material espalhado na calçada.',
        ],
      },
      {
        h2: 'Casas antigas e o Centro histórico',
        paragrafos: [
          'Pelotas tem muitos casarões do século XIX e do começo do século XX, principalmente no Centro. Reforma em imóvel inventariado ou tombado depende de autorização prévia dos órgãos de patrimônio. Resolva isso antes de quebrar qualquer coisa. Nessas casas, sem recuo e com calçada estreita, a caçamba normalmente fica na pista, por isso vale caprichar no pedido.',
        ],
      },
    ],
    faq: [
      {
        p: 'Qual caçamba pedir para reforma de banheiro?',
        r: 'Na maioria dos banheiros, uma caçamba de 3 ou 4 m³ resolve, incluindo piso, azulejo e louças. Mande as medidas do banheiro para confirmar.',
      },
      {
        p: 'Posso jogar a madeira da forma e do telhado na caçamba?',
        r: 'Avise antes. Madeira tem destino diferente do entulho de alvenaria, e algumas empresas pedem que ela vá separada ou cobram diferente.',
      },
      {
        p: 'Preciso de licença da prefeitura para colocar caçamba na frente da obra?',
        r: 'Quem precisa estar cadastrada e autorizada é a empresa de caçamba, pela Lei nº 4.850/2002. Para a obra em si, siga as exigências de alvará da prefeitura.',
      },
    ],
  },
  {
    slug: 'tamanhos-de-cacamba',
    nome: 'Tamanhos de caçamba',
    curto: 'Caçambas de 3, 4 e 5 m³: quanto cabe em cada uma e qual pedir para a sua obra.',
    titulo: 'Tamanhos de Caçamba de Entulho: 3, 4 e 5 m³',
    descricao: 'Qual tamanho de caçamba de entulho pedir em Pelotas: quanto cabe em 3, 4 e 5 m³, equivalência em carrinhos de mão e o limite de 5 m³ da lei municipal.',
    h1: 'Tamanhos de caçamba de entulho: qual pedir',
    intro: 'Em Pelotas, a caçamba de entulho tem no máximo 5 m³, pelo que diz a Lei Municipal nº 4.850/2002. A mais comum na cidade é a de 4 m³. Para saber qual pedir, conte o entulho em carrinhos de mão ou mande uma foto pelo WhatsApp.',
    imagem: 'tamanhos-cacamba',
    imagemAlt: 'Fileira de caçambas estacionárias laranja e azuis em pátio de piso intertravado',
    mensagem: 'Olá! Vim pelo site Pelotas Entulho e quero saber qual tamanho de caçamba pedir. Tipo de obra e bairro: ',
    silo: 'tamanhos-e-calculo',
    secoes: [
      {
        h2: 'Quanto cabe em cada caçamba',
        paragrafos: [
          'Um carrinho de mão de obra carrega uns 60 litros de entulho quando bem cheio. Com essa referência, dá para estimar: 1 m³ equivale a pouco mais de 16 carrinhos. Na prática, o entulho solto ocupa mais espaço do que a parede inteira ocupava, porque fica cheio de vazios. Por isso, na dúvida, peça um tamanho acima.',
        ],
        lista: [
          '3 m³: cerca de 50 carrinhos. Banheiro, cozinha pequena, muro baixo, limpeza de pátio',
          '4 m³: cerca de 65 carrinhos. Reforma de vários cômodos, troca de piso da casa',
          '5 m³: cerca de 80 carrinhos. Telhado, demolição parcial, obra nova. É o máximo permitido em Pelotas',
        ],
      },
      {
        h2: 'Volume e peso: o cuidado com a caçamba cheia demais',
        paragrafos: [
          'Entulho de alvenaria é pesado: um metro cúbico de tijolo e concreto quebrado pode passar de uma tonelada. O caminhão poliguindaste tem limite de carga, então encher a caçamba só com concreto e terra até a borda pode impedir a retirada.',
          'Também não dá para passar da borda. Entulho acima do limite cai no transporte, e a lei de Pelotas exige o material coberto por lona ou tela. Se a caçamba encheu antes do fim da obra, peça a troca em vez de empilhar.',
        ],
      },
      {
        h2: 'Como escolher sem errar',
        paragrafos: [
          'A forma mais segura é mandar uma foto do que vai ser quebrado, ou do monte de entulho, e dizer o tipo de obra. Quem trabalha com caçamba todo dia acerta o tamanho rápido. Se o volume ficar entre dois tamanhos, o maior quase sempre sai mais em conta do que pagar uma segunda caçamba.',
        ],
      },
    ],
    faq: [
      {
        p: 'Qual é a caçamba mais comum em Pelotas?',
        r: 'A de 4 m³ é a mais encontrada nas empresas da cidade. A disponibilidade de 3 e 5 m³ depende da empresa parceira.',
      },
      {
        p: 'Existe caçamba maior que 5 m³?',
        r: 'Para ficar na via pública em Pelotas, não. A Lei nº 4.850/2002 limita a caçamba estacionária a 5 m³.',
      },
      {
        p: 'Quantos sacos de entulho cabem numa caçamba de 4 m³?',
        r: 'Um saco de ráfia de entulho costuma ter uns 20 a 30 litros cheio. Uma caçamba de 4 m³ recebe algo entre 130 e 200 sacos, conforme o tamanho e o quanto cada um está cheio.',
      },
    ],
  },
  {
    slug: 'coletora-de-entulho',
    nome: 'Coletora de entulho',
    curto: 'Coletora é o nome que Pelotas dá à caçamba de entulho. Peça a sua pelo WhatsApp.',
    titulo: 'Coletora de Entulho em Pelotas: Peça pelo WhatsApp',
    descricao: 'Coletora de entulho em Pelotas RS: caçamba de até 5 m³ para obra, reforma e limpeza, de empresa autorizada pela prefeitura. Orçamento rápido no WhatsApp.',
    h1: 'Coletora de entulho em Pelotas',
    intro: 'Em Pelotas, quase ninguém fala "caçamba": fala coletora. É a mesma caixa metálica que fica na frente da obra, recebe o entulho e é levada pelo caminhão. Se você procurou "coletora em Pelotas", está no lugar certo. Mande o bairro e o tipo de entulho e receba o orçamento.',
    imagem: 'coletora-entulho',
    imagemAlt: 'Coletora de entulho cheia de tábuas e restos de madeira, encostada no meio-fio de uma calçada',
    mensagem: 'Olá! Vim pelo site Pelotas Entulho e preciso de uma coletora. Bairro: ',
    silo: 'contratar-cacamba',
    secoes: [
      {
        h2: 'Por que em Pelotas se diz coletora',
        paragrafos: [
          'O nome vem do próprio uso: a caixa coleta o entulho na obra. A prefeitura usa o mesmo termo, tanto nas notícias sobre o cadastro das empresas quanto nas ações de recolhimento que espalha pelos bairros. Por isso, na cidade, "coletora", "caçamba" e "tele entulho" são três jeitos de pedir a mesma coisa.',
        ],
      },
      {
        h2: 'Coletora de empresa autorizada',
        paragrafos: [
          'A Lei Municipal nº 4.850/2002 diz que só podem operar coletoras na rua as empresas cadastradas e autorizadas pela Secretaria de Transportes e Trânsito, com alvará de localização e vistoria semestral da frota. A coletora regular tem faixas refletivas amarelas, o nome e o telefone da empresa e um número de identificação pintados nas laterais.',
          'Isso protege você. Se a coletora estiver fora da regra, quem leva a multa e pode ter a caçamba apreendida é a empresa. Mas ninguém quer ver a caçamba ser retirada no meio da obra.',
        ],
        lista: [
          'Faixas refletivas amarelas nas laterais e na frente',
          'Nome, telefone e número da coletora visíveis',
          'Capacidade de no máximo 5 m³',
          'Entulho coberto por lona no transporte',
        ],
      },
      {
        h2: 'Onde a coletora fica',
        paragrafos: [
          'A coletora deve ficar em frente à obra. De preferência sobre o passeio, deixando 1 metro livre para pedestres. Se não houver espaço, fica na pista onde é permitido estacionar, a pelo menos 10 metros da esquina e com 20 cm de sarjeta livre para a água correr. Na rua, o limite é de 72 horas por coletora. Se a obra continuar, faz-se a troca.',
        ],
      },
    ],
    faq: [
      {
        p: 'Coletora e caçamba são a mesma coisa?',
        r: 'São. Coletora é como a caçamba de entulho é chamada em Pelotas e em boa parte da região sul do estado.',
      },
      {
        p: 'Quanto tempo a coletora pode ficar na rua em Pelotas?',
        r: 'Até 72 horas por coletora, segundo a Lei nº 4.850/2002. Dentro do terreno, vale o prazo combinado com a empresa.',
      },
      {
        p: 'De que tamanho é a coletora?',
        r: 'A mais comum na cidade é a de 4 m³. O máximo permitido para ficar na rua é 5 m³.',
      },
    ],
  },
];

export const servicoPorSlug = (s: string) => SERVICOS.find((x) => x.slug === s);
