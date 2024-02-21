começo = str(input('você está pronto?'))                                                     #mensagem de entrada
nome_jogo = "Jogo da adivinhação"                                                            #atribuindo uma variavel str para o nome do jogo
if começo == 'sim' or começo == 'sim!' or começo == 'pronto' or começo =='pronto!':          #fazendo uma condicional para o início do jogo
    print('==============================')                                                  #símbolos para ornamentar o código
    print('{:=^30}'.format(nome_jogo))
    print('==============================\n')
    print('OBJETIVO: Advinhar a palavara misteriosa!!!\n1.Inicialmente,escolha uma letra\n2.Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela se encontra\n3.Entretanto, caso esta letra não exista na palavra,você irá sugerir outra letra\nVAMOS COMEÇAR???\n')

    print(30 * '-')                                                          #simbolos para ornamentar o código
    print('A PALAVRA MISTERIOSA É ****')                                      #mensagem artificial pra sabermos a quantidade de letras contida na palavra

    palavra_misteriosa = ['p','a','t','o']                                    #lista com as letras presentes na palavra misteriosa
    letras_contidas = []
    for c in range(0, len(palavra_misteriosa)) :
        letras_contidas.append('*')                                           #(comando usado para adicionar novas letras na lista)para cada letra contida na palavra,

    acertou = False                                                           #atribuição para que ao encerrar o código,quando o acertou for true
                                                                              #enquanto estiver no loop da adivinhação,a pergunta aparecerá,até o fim de jogo
    while acertou == False:                                                   #enquanto acertou for falso,tais coisas devem acontecer:
        letra = str(input('Qual letra você acha que contém na palavra? '))       #Para começarmos o jogo,deve-se colocar uma letra
        if len(letra) != 1:
            print('digite apenas uma letra!!!')                               #condição para caso haja uma invalidez ao digitar mais de uma letra ao mesmo ,o que não é possível
        for i in range(0, len(palavra_misteriosa)):
            if letra == palavra_misteriosa[i]:                                #se a letra digitada estiver na palavra misteriosa,insere
                letras_contidas[i] = letra
            print(letras_contidas[i])
        acertou = True
        for x in range(0,len(letras_contidas)):                                 #caso a letra estiver contida(como diz a variável)
            if letras_contidas[x] != '*':                                       #será substituida no lugar do símbolo *,que esconde a palavra
                continue
            acertou = False

    print('Parabéns,você adivinhou a palavra misteriosa!!!Fim de jogo!!!')      #ao término do jogo,quando todas as letras estiverem preenchidas,apareceráa mensagem:
else:                                                                           #listagem de regras da vertical com quebra de linha \n
    print('Poxa,que pena...Fica para a próxima!')



