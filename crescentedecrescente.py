a = int(input('Digite um numero:'))
b = int(input('Digite outro numero:'))
c = int(input('Outro número'))
d = int(input('Outro'))
e = int(input('Outro número'))
ordem=input('Ordem crescente ou decrescente?')
num = (a,b,c,d,e)
if ordem== 'crescente':
  print('Essa é a ordem crescente:',sorted(num))
if ordem== 'decrescente':
  print('Essa é a ordem decrescente:', sorted(num, reverse=True))
