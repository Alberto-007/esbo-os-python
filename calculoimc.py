peso = float(input('Digite seu peso:'))
sexo = input('Digite seu sexo (M/F):')
altura = float(input('Digite sua altura:'))
IMC = (peso)/(altura**2)
if IMC < 20 :
  print('Sua situação é abaixo do peso')
elif IMC >= 20 and 25 >= IMC :
  print('Sua situação é peso normal') 
elif IMC >= 25 and 30 >= IMC :
  print('Sua situação é sobre peso')
elif IMC >= 30 and 40 >= IMC :
  print('Sua situação é obeso')
elif IMC >= 40 :
  print('Sua situação é obeso mórbido')
if sexo == 'M' :
  ideal = (72.7*altura) - 58
if sexo == 'F' :
  ideal = (62.1*altura) - 44.7
print('E seu peso ideal é:',round(ideal,2))
  
