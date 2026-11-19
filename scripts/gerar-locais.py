# Gera src/data/bairros/*.json e src/data/cidades/*.json (texto único por local). Rodar uma vez; depois editar os JSON.
import json, os
B = 'src/data/bairros'; C = 'src/data/cidades'
UFPEL_SG = 'https://revistas.ufpel.edu.br/index.php/pixo/article/download/2581/2030'
bairros = [
 dict(slug='centro', nome='Centro', prep='no',
  titulo='Caçamba de Entulho no Centro de Pelotas',
  descricao='Caçamba de entulho e tele entulho no Centro de Pelotas: reforma de casarão, apartamento e loja, com caçamba na pista e troca rápida. Orçamento no WhatsApp.',
  h1='Caçamba de entulho no Centro de Pelotas',
  sobre='O Centro é a parte mais antiga e mais densa de Pelotas. Em volta da Praça Coronel Pedro Osório ficam o Mercado Central, o Theatro Guarany, a Biblioteca Pública e boa parte dos casarões que dão fama à cidade. É o bairro da reforma de apartamento, de sala comercial e de imóvel histórico, quase sempre sem recuo e com calçada estreita.',
  secoes=[
   dict(h2='Como é pedir caçamba no Centro', paragrafos=[
    'Nos endereços do Centro raramente há pátio ou garagem para receber a caçamba. A Lei nº 4.850/2002 manda colocá-la em frente à obra, de preferência no passeio, deixando 1 metro livre para pedestres. Com calçadas estreitas, quase sempre ela vai para a pista, junto ao meio-fio, com 20 cm de sarjeta livres e a pelo menos 10 metros da esquina.',
    'Como as quadras são curtas, a regra dos 10 metros da esquina pesa aqui. Imóvel de esquina ou muito perto dela pode precisar que a caçamba fique um pouco adiante. Se do seu lado da rua for proibido estacionar, a lei permite o lado oposto. Diga isso no pedido para o ponto ser combinado antes do caminhão chegar.']),
   dict(h2='Casarões e prédios antigos', paragrafos=[
    'Muitos imóveis do Centro são inventariados ou tombados. Antes de quebrar parede, trocar esquadria ou mexer na fachada, confirme as autorizações com a prefeitura e com os órgãos de patrimônio. A caçamba é a parte fácil. A licença da obra é o que costuma atrasar.',
    'Casarão antigo gera entulho diferente: tijolo maciço, argamassa de cal, forro de madeira, assoalho e telha francesa. A madeira deve ser avisada no pedido, porque tem destino diferente do entulho de alvenaria.'],
    lista=['Entrega cedo, antes do movimento do comércio','Caçamba na pista, junto ao meio-fio, longe da esquina','Troca no prazo: na rua, o limite é de 72 horas por caçamba']),
   dict(h2='Apartamento: o entulho desce antes da caçamba chegar', paragrafos=[
    'Em reforma de apartamento, o entulho desce em sacos pela escada ou pelo elevador de serviço, conforme o regulamento do prédio. Combine com o síndico os horários de obra e de uso do elevador. O ideal é juntar os sacos e pedir a caçamba quando estiver tudo pronto para descer, para ela não ficar na rua esperando material.'])],
  faq=[
   dict(p='Dá para colocar caçamba na rua no Centro de Pelotas?', r='Sim, em frente à obra. Se a calçada for estreita, a caçamba fica na pista onde o estacionamento é permitido, a pelo menos 10 metros da esquina e com 20 cm de sarjeta livre.'),
   dict(p='Moro num casarão tombado. Posso usar caçamba?', r='Pode. A caçamba não depende do tombamento, mas a obra sim. Confirme as autorizações de patrimônio antes de começar a quebrar.'),
   dict(p='Reformo um apartamento no Centro. Preciso de caçamba grande?', r='Quase sempre não. Reforma de apartamento gera pouco volume, e uma caçamba de 3 ou 4 m³ costuma resolver.')],
  proximos=['porto','simoes-lopes','fragata'], fontes=['https://pt.wikipedia.org/wiki/Pelotas']),
 dict(slug='porto', nome='Porto', prep='no',
  titulo='Caçamba de Entulho no Porto, Pelotas',
  descricao='Tele entulho e caçamba de entulho no bairro Porto, em Pelotas: casas antigas, prédios industriais e obras perto do Canal São Gonçalo. Peça no WhatsApp.',
  h1='Caçamba de entulho no bairro Porto, em Pelotas',
  sobre='O Porto nasceu nas margens do Canal São Gonçalo e foi, por muito tempo, o lado industrial e operário de Pelotas. Hoje mistura casario antigo, galpões e prédios de fábrica reaproveitados (vários deles ocupados pela UFPel), repúblicas de estudantes e obras de reforma para aluguel.',
  secoes=[
   dict(h2='Reforma de casa antiga e de imóvel para estudante', paragrafos=[
    'Boa parte das obras do Porto é de reforma: casa antiga transformada em moradia para estudante, banheiro novo, troca de piso, divisão de cômodos. São obras de volume médio, em que uma caçamba de 4 m³ costuma bastar. Às vezes é preciso uma troca no fim, quando sai o entulho do acabamento.',
    'As casas geminadas, coladas umas nas outras e sem recuo, fazem a caçamba ficar na pista. Combine a posição para não tapar a garagem do vizinho e para respeitar os 20 cm de sarjeta livre que a lei pede.']),
   dict(h2='Perto do canal: cuidado com chuva e água', paragrafos=[
    'Áreas próximas ao Canal São Gonçalo e às zonas baixas do bairro acumulam água quando chove forte. A sarjeta livre não é só exigência da lei: é por onde a água escoa. Caçamba encostada no meio-fio, sem espaço, vira barragem e alaga a frente da obra.',
    'Depois de alagamento, aparece muito entulho misturado: reboco que caiu, piso estufado, forro molhado, móveis. A caçamba recebe o entulho de obra. Móveis e eletrodomésticos estragados têm outro destino, então separe antes de encher.'],
    lista=['Deixe a sarjeta livre para a água correr','Separe móveis e eletrodomésticos do entulho','Peça a troca se a caçamba encher com reboco molhado, que pesa mais'])],
  faq=[
   dict(p='Vocês atendem a região do Porto e da Balsa?', r='Sim. O Porto e os loteamentos próximos ao canal fazem parte da área de atendimento em Pelotas.'),
   dict(p='Entulho molhado pesa mais na caçamba?', r='Pesa. Reboco e terra encharcados podem deixar a caçamba pesada demais antes de encher. Se for o caso, avise e peça troca mais cedo.'),
   dict(p='Posso colocar a caçamba na frente da república, onde há carro estacionado?', r='O ponto precisa estar livre na hora da entrega. Combine com os moradores para liberar a vaga no dia.')],
  proximos=['centro','navegantes','sao-goncalo'], fontes=['https://wp.ufpel.edu.br/avozdoporto/2024/02/10/porto-de-pelotas-a-historia-do-desenvolvimento-industrial-da-regiao-e-o-que-restou-dela/']),
 dict(slug='fragata', nome='Fragata', prep='no',
  titulo='Caçamba de Entulho no Fragata, Pelotas',
  descricao='Caçamba de entulho e coletora no Fragata, em Pelotas: obras em casa com pátio, Py Crespo e Av. Duque de Caxias. Orçamento rápido pelo WhatsApp.',
  h1='Caçamba de entulho no Fragata, em Pelotas',
  sobre='O Fragata é a grande região oeste de Pelotas, que cresceu ao longo da primeira metade do século XX a partir da Avenida Duque de Caxias. É bairro de casa térrea, muitas vezes com pátio, de comércio de rua e de loteamentos como o Py Crespo. É também onde muita gente amplia a casa aos poucos, cômodo por cômodo.',
  secoes=[
   dict(h2='Ampliação, muro e churrasqueira', paragrafos=[
    'No Fragata, a obra mais comum é a ampliação: um quarto a mais nos fundos, a área com churrasqueira, o muro novo, a garagem coberta. Nesse tipo de obra o entulho sai em duas fases. Primeiro vem a quebra e a escavação, com muita terra e tijolo. Depois sobram restos de bloco, argamassa e embalagem.',
    'Quando há pátio, a caçamba pode ficar dentro do terreno, e o limite de 72 horas da via pública deixa de valer. Fica valendo o prazo combinado com a empresa. É a forma mais tranquila de trabalhar numa obra que vai durar semanas.']),
   dict(h2='Terra de escavação e aterro', paragrafos=[
    'Fundação de ampliação e rebaixo de terreno geram terra, e terra é o material mais pesado que vai para a caçamba. Uma caçamba cheia só de terra pode passar do peso que o caminhão consegue levantar. Avise quando o entulho for principalmente terra, para receber a orientação de quanto encher.'],
    lista=['Caçamba dentro do pátio sempre que der','Terra pura: encha menos e peça troca','Separe a madeira das formas, que tem outro destino'])],
  faq=[
   dict(p='Atendem o Py Crespo e outros loteamentos do Fragata?', r='Sim. Todo o Fragata faz parte da área de atendimento. Informe a rua e o loteamento no pedido.'),
   dict(p='A caçamba pode ficar dentro do meu pátio?', r='Pode, se o portão e o caminho permitirem a manobra do caminhão poliguindaste. Mande a largura do portão e uma foto do acesso.'),
   dict(p='Posso jogar terra de escavação na caçamba?', r='Pode, mas terra é muito pesada. Avise no pedido para saber até onde encher.')],
  proximos=['simoes-lopes','centro','barragem'], fontes=['https://periodicos.ufpel.edu.br/index.php/Projectare/article/view/21729/13782']),
 dict(slug='tres-vendas', nome='Três Vendas', prep='nas',
  titulo='Caçamba de Entulho nas Três Vendas, Pelotas',
  descricao='Tele entulho e caçamba de entulho nas Três Vendas, em Pelotas: reformas, ampliações e obras perto da Av. Fernando Osório. Peça seu orçamento no WhatsApp.',
  h1='Caçamba de entulho nas Três Vendas, em Pelotas',
  sobre='As Três Vendas formam uma das regiões mais populosas de Pelotas, ao norte do Centro, com comércio próprio ao longo da Avenida Fernando Osório e da Avenida Ildefonso Simões Lopes. Quem mora ali resolve quase tudo sem ir ao Centro. A região tem muitas casas de família, conjuntos habitacionais e imóveis de aluguel para estudantes.',
  secoes=[
   dict(h2='Obras típicas das Três Vendas', paragrafos=[
    'Reforma de casa de conjunto habitacional, construção de segundo piso, troca de telhado e regularização de puxadinho estão entre os pedidos mais comuns da região. Construir um segundo andar gera pouca demolição, mas muita sobra de material ao longo de semanas. Nesse caso, a caçamba com troca programada funciona melhor do que uma única caçamba parada.',
    'Nas avenidas comerciais, a caçamba precisa respeitar a sinalização: onde é proibido estacionar, ela não pode ficar. A lei permite o lado oposto da rua. Se também não houver espaço ali, a empresa pede à Secretaria de Transportes a indicação de outro ponto próximo.']),
   dict(h2='Telhado: o entulho que mais ocupa espaço', paragrafos=[
    'Telha cerâmica quebrada é leve, mas ocupa muito espaço, porque fica cheia de vazios. Uma troca de telhado de casa média pode encher uma caçamba de 5 m³ com folga. Se as telhas forem de fibrocimento antigo, confirme se não são de amianto: nesse caso, elas não vão para a caçamba comum.'],
    lista=['Segundo piso: caçamba com trocas ao longo da obra','Telhado: prefira 5 m³','Avenida com proibição de estacionar: combine o ponto antes'])],
  faq=[
   dict(p='Vocês entregam caçamba nos conjuntos habitacionais das Três Vendas?', r='Sim. Informe a rua e o número. Em ruas estreitas, a entrega é combinada para um horário com menos carros estacionados.'),
   dict(p='Vou construir um segundo andar. Uma caçamba basta?', r='Raramente. O mais comum é trabalhar com trocas ao longo da obra, conforme o entulho for saindo.'),
   dict(p='Telha velha pode ir na caçamba?', r='Telha cerâmica sim. Telha de fibrocimento antiga deve ser verificada, porque, se tiver amianto, precisa de descarte próprio.')],
  proximos=['centro','areal','barragem'], fontes=['https://www.zapimoveis.com.br/guia-de-cidades/rs+pelotas/']),
 dict(slug='areal', nome='Areal', prep='no',
  titulo='Caçamba de Entulho no Areal, Pelotas',
  descricao='Caçamba de entulho e coletora no Areal, em Pelotas: obras perto da Av. Domingos de Almeida e da Av. JK, com Ecoponto na região. Orçamento no WhatsApp.',
  h1='Caçamba de entulho no Areal, em Pelotas',
  sobre='O Areal fica a leste do Centro, a caminho do Laranjal, e cresceu junto com as Três Vendas como uma das grandes regiões residenciais de Pelotas. A Avenida Domingos de Almeida e a Avenida Juscelino Kubitschek cortam o bairro, que tem o Museu da Baronesa, muitas casas, prédios novos e bastante comércio.',
  secoes=[
   dict(h2='Casas, prédios novos e reforma de comércio', paragrafos=[
    'No Areal convivem casas antigas de família, condomínios mais recentes e lojas ao longo das avenidas. Em casa, a caçamba costuma ficar no recuo ou na frente do portão. Em prédio, ela precisa da autorização do condomínio quando fica em área comum, e da calçada livre quando fica na rua.',
    'Reformas de loja nas avenidas precisam de atenção redobrada à sinalização. Onde há faixa de ônibus ou proibição de estacionar, a caçamba não pode ficar. O ponto alternativo deve ser combinado com a empresa antes da entrega.']),
   dict(h2='Ecoponto JK ou caçamba?', paragrafos=[
    'O Sanep mantém o Ecoponto JK, na Avenida Juscelino Kubitschek, que recebe até 1,5 m³ de material por pessoa, de segunda a sábado. Para pouco entulho e com carro disponível, vale levar. Para reforma de verdade, com mais de um carro cheio de entulho, a caçamba sai mais barata do que várias viagens, além de poupar o carro e as costas.'],
    lista=['Até 1,5 m³ e com transporte próprio: Ecoponto','Acima disso: caçamba de 3 a 5 m³','Loja na avenida: confira a sinalização antes'])],
  faq=[
   dict(p='Qual é o Ecoponto mais perto do Areal?', r='O Ecoponto JK, na Av. Juscelino Kubitschek, 3.195. Ele recebe até 1,5 m³ por pessoa, de segunda a sábado, das 8h às 12h e das 13h às 17h.'),
   dict(p='A caçamba pode ficar na garagem do prédio?', r='Pode, se o condomínio autorizar e se o caminhão conseguir manobrar. Na rua, siga as regras da Lei nº 4.850/2002.'),
   dict(p='Atendem o Areal e a região das Dunas?', r='Sim. Informe a rua e o bairro no pedido.')],
  proximos=['tres-vendas','sao-goncalo','laranjal'], fontes=['https://portal.sanep.com.br/residuos-solidos/ecopontos']),
 dict(slug='laranjal', nome='Laranjal', prep='no',
  titulo='Caçamba de Entulho no Laranjal, Pelotas',
  descricao='Caçamba de entulho no Laranjal, em Pelotas: obras em casa de praia, terrenos amplos e ruas de areia nos balneários. Orçamento e prazo pelo WhatsApp.',
  h1='Caçamba de entulho no Laranjal, em Pelotas',
  sobre='O Laranjal é a praia de Pelotas, na beira da Lagoa dos Patos, com os balneários Santo Antônio, Valverde e Los Angeles. Tem casas de veraneio, moradores o ano todo e muitos terrenos amplos. É também onde se constrói bastante: casa nova, piscina, muro, ampliação para a temporada.',
  secoes=[
   dict(h2='Ruas de areia e terreno amplo', paragrafos=[
    'Várias ruas do Laranjal são de areia ou de chão batido. O caminhão poliguindaste é pesado e precisa de piso firme para baixar e levantar a caçamba. Depois de muita chuva, rua de areia fofa ou encharcada pode impedir a manobra. Avise no pedido se a sua rua não é calçada.',
    'A vantagem é o espaço: na maioria dos terrenos a caçamba fica dentro do lote. Fora da via pública, o limite de 72 horas da lei municipal não se aplica, e o prazo é o combinado com a empresa.']),
   dict(h2='Obra antes da temporada', paragrafos=[
    'Muita gente reforma a casa de praia entre a primavera e o começo do verão. Nessa época a agenda das caçambas aperta. Peça com antecedência e combine a retirada antes de dezembro, para não ficar com caçamba no terreno quando a família chegar.',
    'Para pouco material, o Sanep tem o Ecoponto Laranjal, na Rua Bom Jesus, no Balneário Valverde, que recebe até 1,5 m³ por pessoa.'],
    lista=['Rua de areia: avise no pedido','Prefira deixar a caçamba dentro do terreno','Peça com antecedência na primavera'])],
  faq=[
   dict(p='O caminhão consegue entrar em rua de areia no Laranjal?', r='Normalmente sim, com o piso seco e firme. Depois de chuva forte pode ser preciso esperar. Informe se a rua não é calçada.'),
   dict(p='Tem taxa extra para o Laranjal?', r='Pode haver, pela distância do Centro. O orçamento informa o valor completo antes de você fechar.'),
   dict(p='Onde fica o Ecoponto do Laranjal?', r='Na Rua Bom Jesus, 95, no Balneário Valverde. Recebe até 1,5 m³ por pessoa, de segunda a sábado.')],
  proximos=['areal','sao-goncalo','navegantes'], fontes=['https://portal.sanep.com.br/residuos-solidos/ecopontos','https://periodicos.ufpel.edu.br/index.php/seur/article/view/20092/12727']),
 dict(slug='barragem', nome='Barragem', prep='na',
  titulo='Caçamba de Entulho na Barragem, Pelotas',
  descricao='Tele entulho e caçamba de entulho na região da Barragem, norte de Pelotas: obras em chácaras, terrenos e loteamentos novos. Peça orçamento no WhatsApp.',
  h1='Caçamba de entulho na região da Barragem, em Pelotas',
  sobre='A Barragem é a região administrativa do norte de Pelotas e leva o nome da Barragem Santa Bárbara, construída em 1968 e que hoje é a principal fonte de água da cidade. É uma área de transição entre a cidade e o campo, com loteamentos, chácaras, terrenos grandes e obras novas.',
  secoes=[
   dict(h2='Terrenos grandes e limpeza de área', paragrafos=[
    'Na Barragem aparecem pedidos diferentes dos do Centro: limpeza de terreno para construir, demolição de galpão ou de casa velha de madeira, cercamento e construção nova. Esse tipo de serviço mistura entulho com mato, galhos, madeira e às vezes lixo deixado por outras pessoas.',
    'Caçamba de entulho é para resíduo de obra. Antes de pedir, separe o que é poda e o que é lixo comum. Madeira e galhos podem ser aceitos por algumas empresas, mas precisam ser avisados, porque têm outro destino e podem mudar o valor.']),
   dict(h2='Perto da água, mais cuidado com o descarte', paragrafos=[
    'A região fica perto do Arroio Santa Bárbara e da área de proteção da barragem. Entulho largado em terreno ou à beira de arroio contamina o solo e a água que abastece a cidade, e dá multa. Por isso vale ainda mais contratar caçamba de empresa autorizada e saber para onde o material vai.'],
    lista=['Separe poda e lixo comum antes de encher','Mande foto do terreno para estimar o volume','Confirme se o caminhão chega até o lote'])],
  faq=[
   dict(p='Vocês atendem chácaras e loteamentos da Barragem?', r='Sim, conforme o acesso. Estradas de chão em boas condições normalmente permitem a entrega. Mande a localização no WhatsApp.'),
   dict(p='Posso colocar mato e galhos da limpeza do terreno na caçamba?', r='Avise antes. Poda tem destino diferente do entulho e algumas empresas pedem caçamba separada.'),
   dict(p='Demolição de casa de madeira vai na caçamba de entulho?', r='A madeira deve ser avisada no pedido. Em alguns casos é feita uma caçamba só de madeira, separada da alvenaria.')],
  proximos=['fragata','tres-vendas','simoes-lopes'], fontes=['https://anais-siiepe.ufpel.edu.br/2016/CB_02270.pdf']),
 dict(slug='sao-goncalo', nome='São Gonçalo', prep='no',
  titulo='Caçamba de Entulho no São Gonçalo e Balsa',
  descricao='Caçamba de entulho no São Gonçalo, em Pelotas: Balsa, Ambrósio Perret, Village, Umuarama e condomínios novos. Ecoponto Balsa perto. Peça no WhatsApp.',
  h1='Caçamba de entulho no São Gonçalo, em Pelotas',
  sobre='A região administrativa São Gonçalo fica entre o Canal São Gonçalo, o Arroio Pelotas e a Avenida Juscelino Kubitschek. Reúne loteamentos como Balsa, Ambrósio Perret, Navegantes, Village, Cruzeiro, Umuarama e Marina Ilha Verde, e é uma das áreas que mais crescem em Pelotas, com condomínios fechados e obras novas.',
  secoes=[
   dict(h2='Condomínio fechado: combine com a administração', paragrafos=[
    'Em condomínio fechado, a caçamba entra pela portaria e fica no lote ou na rua interna. Cada condomínio tem as suas regras: horário de entrada de caminhão, prazo máximo da caçamba, peso permitido nas ruas internas. Peça essas regras à administração antes de agendar, e passe-as no pedido.',
    'Obra nova em condomínio gera entulho constante: sobras de bloco, argamassa, cerâmica e embalagem. Muitas administrações exigem caçamba durante toda a obra, para não haver material solto no lote.']),
   dict(h2='Balsa e loteamentos antigos', paragrafos=[
    'Na Balsa e nos loteamentos mais antigos da região, a caçamba fica na rua, em frente à obra, seguindo a Lei nº 4.850/2002: de preferência no passeio, com 1 metro livre, ou na pista onde é permitido estacionar. Para pouco entulho, o Sanep tem o Ecoponto Balsa, na Rua Paulo Guilayn, que recebe até 1,5 m³ por pessoa.'],
    lista=['Condomínio: peça as regras da administração','Rua: caçamba em frente à obra, longe da esquina','Pouco entulho: Ecoponto Balsa'])],
  faq=[
   dict(p='A caçamba pode entrar no meu condomínio no São Gonçalo?', r='Pode, se a administração autorizar. Informe o horário permitido e onde a caçamba deve ficar.'),
   dict(p='Onde fica o Ecoponto Balsa?', r='Na Rua Paulo Guilayn, 201. Funciona de segunda a sábado, das 8h às 12h e das 13h às 17h, com limite de 1,5 m³ por pessoa.'),
   dict(p='Atendem o Ambrósio Perret e o Umuarama?', r='Sim. Toda a região do São Gonçalo faz parte da área de atendimento.')],
  proximos=['navegantes','porto','areal'], fontes=[UFPEL_SG,'https://portal.sanep.com.br/residuos-solidos/ecopontos']),
 dict(slug='simoes-lopes', nome='Simões Lopes', prep='no',
  titulo='Caçamba de Entulho no Simões Lopes, Pelotas',
  descricao='Tele entulho e caçamba de entulho no Simões Lopes, em Pelotas: casas antigas perto da ferrovia, comércio e reformas. Orçamento rápido no WhatsApp.',
  h1='Caçamba de entulho no Simões Lopes, em Pelotas',
  sobre='O Simões Lopes fica colado ao Centro, entre a Avenida Duque de Caxias, a Avenida Brasil e a BR-392, e tem a origem ligada à ferrovia e à antiga estação férrea. Com o tempo, ganhou comércio próprio e virou uma espécie de segundo centro para quem mora na zona oeste.',
  secoes=[
   dict(h2='Casas antigas, lotes estreitos', paragrafos=[
    'O bairro tem muitas casas antigas em lotes estreitos, coladas umas nas outras. Reforma ali costuma ser de casa inteira: piso, reboco, banheiro, telhado. O volume é médio e a caçamba quase sempre fica na pista, porque o passeio não comporta a caçamba e ainda 1 metro livre para pedestres.',
    'Em lote estreito, a frente do imóvel mede às vezes menos do que a caçamba com espaço para manobra. Avise se a sua frente é estreita ou se fica perto da esquina, para a empresa planejar onde baixar a caçamba.']),
   dict(h2='Comércio e obra rápida', paragrafos=[
    'Reforma de loja e de sala comercial pede velocidade: o comerciante quer reabrir logo. O ideal é programar a caçamba para o dia da quebra, encher em um ou dois dias e pedir a retirada logo em seguida, dentro das 72 horas permitidas na via pública.'],
    lista=['Frente estreita: avise no pedido','Loja: caçamba no dia da quebra e retirada rápida','Respeite a sarjeta livre de 20 cm'])],
  faq=[
   dict(p='Minha casa tem frente estreita. Cabe caçamba?', r='Na maioria dos casos, sim, na pista em frente ao imóvel. Mande uma foto da frente para combinar a posição.'),
   dict(p='Atendem perto da antiga estação férrea?', r='Sim. Todo o Simões Lopes faz parte da área de atendimento.'),
   dict(p='Quanto tempo a caçamba pode ficar na frente da loja?', r='Na via pública, até 72 horas por caçamba, pela Lei nº 4.850/2002.')],
  proximos=['centro','fragata','porto'], fontes=['https://www2.ufpel.edu.br/cic/2011/anais/pdf/CH/CH_01610.pdf','https://anais-siiepe.ufpel.edu.br/2025/SA_05308.pdf']),
 dict(slug='navegantes', nome='Navegantes', prep='no',
  titulo='Caçamba de Entulho no Navegantes, Pelotas',
  descricao='Caçamba de entulho e coletora no Navegantes, em Pelotas: reformas e ampliações nos Navegantes I, II e III, perto do Ecoponto Balsa. Peça no WhatsApp.',
  h1='Caçamba de entulho no Navegantes, em Pelotas',
  sobre='O Navegantes é um loteamento da região do São Gonçalo, criado no fim do século XX e dividido em Navegantes I, II e III. É um bairro de casas de família que cresce rápido, com muitas ampliações, novas construções e lotes sendo ocupados.',
  secoes=[
   dict(h2='Ampliação e construção no lote', paragrafos=[
    'No Navegantes, o pedido mais comum é para ampliar a casa: mais um quarto, a garagem, o muro, a laje para um segundo piso. São obras feitas por etapas, em que o entulho aparece aos poucos. Juntar o material num canto do lote e pedir a caçamba quando houver volume costuma economizar uma viagem.',
    'Quando der, deixe a caçamba dentro do lote. Na rua, ela fica em frente à obra, na pista onde é permitido estacionar, com 20 cm de sarjeta livre, e pode ficar até 72 horas.']),
   dict(h2='Área baixa: chuva e sarjeta livre', paragrafos=[
    'Partes da região do São Gonçalo são baixas e próximas a arroios e canais, e a prefeitura já incluiu bairros da área em mapas de risco de alagamento. Deixar a sarjeta livre ajuda a água a correr. Depois de chuva forte, entulho encharcado pesa mais: se for o caso, encha menos e peça a troca.'],
    lista=['Junte o entulho e peça a caçamba quando houver volume','Caçamba dentro do lote sempre que possível','Pouco material: Ecoponto Balsa, na Rua Paulo Guilayn'])],
  faq=[
   dict(p='Atendem os Navegantes I, II e III?', r='Sim. Informe a rua e qual dos Navegantes no pedido.'),
   dict(p='Vale a pena levar o entulho ao Ecoponto?', r='Para até 1,5 m³ e com transporte próprio, sim. O Ecoponto Balsa é o mais próximo. Acima disso, a caçamba compensa.'),
   dict(p='A caçamba pode ficar no meu lote?', r='Pode, se o caminhão conseguir entrar e manobrar. Mande uma foto do acesso.')],
  proximos=['sao-goncalo','porto','laranjal'], fontes=['https://revistas.ufpel.edu.br/index.php/pixo/article/download/6800/6058','https://wp.ufpel.edu.br/artenosul/2024/12/21/15o-ruas-de-lazer-promove-visibilidade-da-cultura-e-historia-do-bairro-navegantes/']),
]
cidades = [
 dict(slug='capao-do-leao', nome='Capão do Leão', prep='em',
  titulo='Caçamba de Entulho em Capão do Leão RS',
  descricao='Caçamba de entulho e tele entulho em Capão do Leão RS, a partir de Pelotas, conforme agenda e com possível taxa de deslocamento. Consulte no WhatsApp.',
  h1='Caçamba de entulho em Capão do Leão',
  sobre='Capão do Leão é vizinho de Pelotas, do lado sul, pela BR-116, e até 1982 fazia parte do município pelotense. É lá que fica o principal campus da UFPel. As obras vão de reforma de casa a construção em loteamentos e chácaras.',
  secoes=[
   dict(h2='Como funciona o atendimento em Capão do Leão', paragrafos=[
    'O atendimento sai de Pelotas, conforme a agenda da empresa parceira, e pode ter taxa de deslocamento. Mande o endereço completo e o tipo de obra para receber o valor total antes de fechar. Pedidos com antecedência são mais fáceis de encaixar.',
    'As regras de caçamba na via pública de Capão do Leão são as do próprio município, e não as de Pelotas. Pergunte à empresa como ela atua na cidade e prefira deixar a caçamba dentro do terreno, o que evita qualquer dúvida.']),
   dict(h2='Obras mais comuns', paragrafos=[
    'Reformas de casa, construção em lote novo, imóveis de aluguel para estudantes e limpeza de terreno estão entre os pedidos da cidade. Para obra com muitas semanas de entulho, combine trocas programadas, já que a caçamba vem de mais longe.'])],
  faq=[
   dict(p='Vocês atendem Capão do Leão?', r='Sim, conforme a agenda da empresa parceira e com possível taxa de deslocamento. Confirme pelo WhatsApp.'),
   dict(p='A taxa de deslocamento é cobrada à parte?', r='Quando existe, ela já aparece no orçamento, para você ver o valor total antes de fechar.')],
  proximos=[], fontes=['https://pt.wikipedia.org/wiki/Cap%C3%A3o_do_Le%C3%A3o']),
 dict(slug='rio-grande', nome='Rio Grande', prep='em',
  titulo='Caçamba de Entulho em Rio Grande RS',
  descricao='Caçamba de entulho em Rio Grande RS: consulte disponibilidade de atendimento a partir de Pelotas, com prazo e taxa de deslocamento no orçamento.',
  h1='Caçamba de entulho em Rio Grande',
  sobre='Rio Grande é a cidade portuária vizinha a Pelotas, na saída da Lagoa dos Patos para o mar. Tem mercado próprio de obras e empresas de caçamba locais. O atendimento a partir de Pelotas é possível em alguns casos, conforme a agenda e a distância.',
  secoes=[
   dict(h2='Quando faz sentido pedir a partir de Pelotas', paragrafos=[
    'Para obra pontual e com data flexível, vale consultar. A distância entre as duas cidades pesa no preço, principalmente quando são necessárias várias trocas. Em obra longa, uma empresa sediada em Rio Grande tende a ser mais prática. Mande o endereço e o tipo de obra para receber uma resposta direta.',
    'As regras de uso da via pública em Rio Grande são as do município, com legislação própria. Confirme com a empresa como a caçamba deve ser posicionada e por quanto tempo pode ficar na rua.']),
   dict(h2='Cassino e bairros da cidade', paragrafos=[
    'O balneário Cassino e os bairros mais afastados ficam mais longe ainda. Nesses casos, informe o endereço exato e se a rua é calçada ou de areia, para a empresa avaliar o acesso do caminhão.'])],
  faq=[
   dict(p='Vocês atendem Rio Grande?', r='Em alguns casos, conforme a agenda da empresa parceira e com taxa de deslocamento. Consulte pelo WhatsApp com o endereço da obra.'),
   dict(p='Vale a pena para obra grande?', r='Para obra com muitas trocas, uma empresa sediada em Rio Grande costuma ser mais vantajosa por causa da distância.')],
  proximos=[], fontes=['https://pt.wikipedia.org/wiki/Rio_Grande_(Rio_Grande_do_Sul)']),
 dict(slug='morro-redondo', nome='Morro Redondo', prep='em',
  titulo='Caçamba de Entulho em Morro Redondo RS',
  descricao='Caçamba de entulho em Morro Redondo RS para reforma, construção e limpeza de propriedade, a partir de Pelotas, com taxa de deslocamento. Consulte no WhatsApp.',
  h1='Caçamba de entulho em Morro Redondo',
  sobre='Morro Redondo fica na Serra dos Tapes, a noroeste de Pelotas, e é um município pequeno, de colonização europeia, com muitas propriedades rurais, sítios e casas de fim de semana.',
  secoes=[
   dict(h2='Obra em sítio e propriedade rural', paragrafos=[
    'Boa parte dos pedidos em Morro Redondo vem de sítio e chácara: reforma de casa, demolição de galpão, construção de casa nova. O ponto mais importante é o acesso. O caminhão poliguindaste precisa de estrada firme e de espaço para baixar a caçamba. Mande a localização e, se possível, fotos da entrada da propriedade.',
    'Como a distância é maior, o atendimento depende da agenda da empresa parceira e tem taxa de deslocamento. Programar a entrega e a retirada com antecedência evita viagens perdidas.']),
   dict(h2='Separar antes de encher', paragrafos=[
    'Em propriedade rural é comum juntar entulho, madeira, telha velha, cerca e sucata. Separe o entulho de obra do resto. Madeira e metal podem ter destino próprio, e alguns materiais, como telha de amianto, não podem ir para a caçamba comum.'])],
  faq=[
   dict(p='A caçamba chega até o meu sítio?', r='Depende da estrada e do espaço para manobra. Mande a localização e fotos do acesso para confirmar.'),
   dict(p='Tem taxa de deslocamento para Morro Redondo?', r='Normalmente sim, por causa da distância. Ela aparece no orçamento antes de você fechar.')],
  proximos=[], fontes=['https://pt.wikipedia.org/wiki/Morro_Redondo']),
 dict(slug='cangucu', nome='Canguçu', prep='em',
  titulo='Caçamba de Entulho em Canguçu RS',
  descricao='Caçamba de entulho em Canguçu RS: consulte disponibilidade de atendimento a partir de Pelotas para obra e reforma, com taxa de deslocamento no orçamento.',
  h1='Caçamba de entulho em Canguçu',
  sobre='Canguçu fica na Serra dos Tapes, ao norte de Pelotas, e é conhecida pela agricultura familiar, com milhares de pequenas propriedades rurais. A cidade tem área urbana própria e um interior muito extenso.',
  secoes=[
   dict(h2='Atendimento a partir de Pelotas', paragrafos=[
    'Pela distância, o atendimento em Canguçu é feito conforme a agenda da empresa parceira, com taxa de deslocamento. Funciona melhor para obra com data marcada e volume definido, de preferência com uma única caçamba ou poucas trocas.',
    'Para obra longa, com muitas trocas, compare com empresas que tenham base na própria cidade. Mande o endereço completo e o tipo de obra para receber uma resposta direta sobre a viabilidade.']),
   dict(h2='Área urbana e interior', paragrafos=[
    'Na área urbana, a caçamba fica em frente à obra, seguindo as regras do município de Canguçu. No interior, o acesso pela estrada e o espaço na propriedade definem se a entrega é possível. Informe se a estrada é de chão e como está depois de chuva.'])],
  faq=[
   dict(p='Vocês atendem Canguçu?', r='Conforme a agenda da empresa parceira e com taxa de deslocamento. Consulte pelo WhatsApp com o endereço.'),
   dict(p='Atendem o interior de Canguçu?', r='Depende do acesso e da distância. Mande a localização para avaliar.')],
  proximos=[], fontes=['https://pt.wikipedia.org/wiki/Cangu%C3%A7u']),
 dict(slug='arroio-do-padre', nome='Arroio do Padre', prep='em',
  titulo='Caçamba de Entulho em Arroio do Padre RS',
  descricao='Caçamba de entulho em Arroio do Padre RS, município cercado por Pelotas: reforma, construção e propriedade rural, com taxa de deslocamento. Consulte.',
  h1='Caçamba de entulho em Arroio do Padre',
  sobre='Arroio do Padre é um município pequeno, de colonização pomerana, totalmente cercado pelo território de Pelotas, na zona rural da Serra dos Tapes. A maior parte das obras é em propriedade rural: casa, galpão, estrebaria e reforma.',
  secoes=[
   dict(h2='Obra no interior', paragrafos=[
    'Em Arroio do Padre, a entrega da caçamba depende principalmente da estrada e do espaço na propriedade. Mande a localização no mapa e uma foto da entrada. Com chuva, estradas de chão podem atrasar a entrega ou a retirada, então combine uma data com folga.',
    'O atendimento sai de Pelotas, conforme a agenda da empresa parceira e com taxa de deslocamento.']),
   dict(h2='O que costuma ir para a caçamba', paragrafos=[
    'Demolição de construção antiga, troca de piso, reforma de banheiro e construção nova. Separe madeira, telha de fibrocimento, sucata e lixo comum do entulho de alvenaria, porque cada um tem destino diferente.'])],
  faq=[
   dict(p='Vocês atendem Arroio do Padre?', r='Sim, conforme a agenda da empresa parceira e com taxa de deslocamento. Confirme pelo WhatsApp.'),
   dict(p='O que preciso informar no pedido?', r='A localização da propriedade, as condições da estrada, o tipo de entulho e a data desejada.')],
  proximos=[], fontes=['https://pt.wikipedia.org/wiki/Arroio_do_Padre']),
 dict(slug='turucu', nome='Turuçu', prep='em',
  titulo='Caçamba de Entulho em Turuçu RS',
  descricao='Caçamba de entulho em Turuçu RS, vizinha a Pelotas pela BR-116, para obra, reforma e limpeza, com taxa de deslocamento. Consulte pelo WhatsApp.',
  h1='Caçamba de entulho em Turuçu',
  sobre='Turuçu é um município pequeno ao norte de Pelotas, às margens da BR-116 e da Lagoa dos Patos, conhecido pela produção de pimenta vermelha. Tem área urbana pequena e muitas propriedades rurais.',
  secoes=[
   dict(h2='Atendimento em Turuçu', paragrafos=[
    'O atendimento é feito a partir de Pelotas, conforme a agenda da empresa parceira e com taxa de deslocamento. Para economizar, programe a obra para precisar de uma só caçamba ou de poucas trocas, juntando o entulho antes de pedir.',
    'Informe o endereço completo, se a obra é na cidade ou no interior e como é o acesso para o caminhão.']),
   dict(h2='Obra em propriedade rural', paragrafos=[
    'Galpão, casa de colono, estufa e reforma de moradia são obras comuns na região. Separe o entulho de alvenaria de madeira, plástico de estufa, sucata e telhas de fibrocimento, que têm destinos próprios.'])],
  faq=[
   dict(p='Vocês atendem Turuçu?', r='Sim, conforme a agenda da empresa parceira e com taxa de deslocamento. Consulte pelo WhatsApp.'),
   dict(p='Dá para deixar a caçamba alguns dias na propriedade?', r='Dá, combinando o prazo no orçamento. Dentro da propriedade, vale o prazo acertado com a empresa.')],
  proximos=[], fontes=['https://pt.wikipedia.org/wiki/Turu%C3%A7u']),
]
for pasta, itens in ((B, bairros), (C, cidades)):
    os.makedirs(pasta, exist_ok=True)
    for d in itens:
        for s in d['secoes']: s.setdefault('lista', None)
        d['secoes'] = [{k: v for k, v in s.items() if v is not None} for s in d['secoes']]
        json.dump(d, open(f"{pasta}/{d['slug']}.json", 'w'), ensure_ascii=False, indent=2)
        print(pasta, d['slug'], len(d['titulo']), len(d['descricao']))
