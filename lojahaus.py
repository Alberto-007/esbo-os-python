print('Olá, bem vindo a Haus, sua loja de álbuns de musica pop, com os mais ultimos sucessos e hits do momento, fazemos entrega e aceitamos cartões, temos os albuns no formato vínil e CD para você.')
#entrada
name = input('Por favor digite seu nome:')
option = input('Digite uma opção: 1 - Fazer um pedido/2 - Sair')
while option == '1':
  order = input('No momento temos em estoque: Lady Gaga, Nicki Minaj ,Blackpink, Katy Perry e Madison Beer, por favor digite sua escolha:')
  formato = input('Seu álbum sera em: Vínil/CD?:')
  quantidade = int(input('Você vai querer quantos álbuns?:'))
  entrega = input('Você quer que seja para entrega?S/N')
  pagamento = input('O pagamento será em:Dinheiro/Cartão')
  if order == 'Lady Gaga' or 'Katy Perry' :
    order = 40
  elif order == 'Nicki Minaj' :
    order = 70
  elif order == 'Blackpink' :
    order = 130
  elif order == 'Madison Beer' :
    order = 68
  if formato == 'Vínil' :
    formato = 2
  if formato == 'CD' :
    formato = 0.5
  if entrega == 'S' :
    address = input('Digite seu endereço:')
  if pagamento == 'Cartão' :
    dc = input('Débito ou Crédito')
#processamento
  precofinal = order*quantidade+formato
#saida
  if entrega == 'S' and pagamento == 'Cartão' :
    print('Seu pedido de albúm de música deu:', precofinal+3, 'reais, entregaremos para', address, ', e pagamento será em Cartão de', dc,', obrigado por comprar na loja Haus, volte sempre,', name)
  elif entrega == 'S' and pagamento == 'Dinheiro' :
    print('Seu pedido de albúm de música deu:', precofinal+3, 'reais, entregaremos para', address, ', e pagamento será em Dinheiro, obrigado por comprar na loja Haus, volte sempre,', name)
  else :
    print('Seu pedido de albúm de música deu:', precofinal,'reais, obrigado por comprar na loja Haus, volte sempre,', name)
  break
else:
  print('Obrigado por usar o programa da loja Haus.')
