print('Prato: 1- Vegetariano/ 2- Peixe/ 3- Frango/ 4- Carne')
prato = input('Escolha um prato, de 1 a 4: ')
if prato == '1' :
  caloriasprato = 180
elif prato == '2' :
  caloriasprato = 230
elif prato == '3' :
  caloriasprato = 250
elif prato == '4' :
  caloriasprato = 350
print('Sobremesa: 1- Abacaxi/ 2- Sorvete diet/ 3- Mousse diet/ 4- Mousse chocolate')
sobremesa = input('Escolha uma sobremesa, de 1 a 4: ')
if sobremesa == '1' :
 caloriassobremesa = 75
elif sobremesa == '2' :
  caloriassobremesa = 110
elif sobremesa == '3' :
  caloriassobremesa = 170
elif sobremesa == '4' :
  caloriassobremesa = 200
print('Bebida: 1- Chá/ 2- Suco de laranja/ 3- Suco de melão/ 4- Refrigerante diet')
bebida = input('Escolha uma bebida, de 1 a 4: ')
if bebida == '1' :
  caloriasbebida = 20
elif bebida == '2' :
  caloriasbebida = 70
elif bebida == '3' :
  caloriasbebida = 100
elif bebida == '4' :
  caloriasbebida = 65
print('O total de calorias é:', caloriasprato+caloriassobremesa+caloriasbebida)
