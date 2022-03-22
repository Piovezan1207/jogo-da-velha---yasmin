visu = [0,1,2,3,4,5,6,7,8]
jogo = [0,0,0,0,0,0,0,0,0]

vitorias = [[1,1,1,0,0,0,0,0,0] , [0,0,0,1,1,1,0,0,0] , [0,0,0,0,0,0,1,1,1] , [1,0,0,1,0,0,1,0,0], [0,1,0,0,1,0,0,1,0] , [0,0,1,0,0,1,0,0,1] , [0,0,1,0,1,0,1,0,0] , [1,0,0,0,1,0,0,0,1] ] 

def malha():
    print(
    """
    {} | {} | {}
    --------------
    {} | {} | {}
    --------------
    {} | {} | {}
    """.format(visu[0],visu[1],visu[2],visu[3],visu[4],visu[5],visu[6],visu[7],visu[8]))

def jogada(numero, simbolo):
    while(1):
        jogada = input("Jogador {}, faça sua jogada. Você é o {}\n".format(numero, simbolo))
        try:
            if int(jogada) < 0 or int(jogada) > 8:
                print("Você deve jogar um número entre 0 e 8")
            elif jogo[int(jogada)] != 0:
                print("Esse local já foi jogado alguma vez")
            else:
                jogo[int(jogada)] = numero
                visu[int(jogada)] = simbolo
                malha()
                break
        except:
            print("Você deve escrever um NUMERO!")
    
    return verificaVitoria(jogo)

def verificaVitoria(jogo):
    for vitoria in vitorias:
        valoresMalha = []
        for val in range(0, 9):
            if vitoria[val] != 0:
                valoresMalha.append(jogo[val])
        if 0 in valoresMalha:
            pass
        elif 1 in valoresMalha and 2 in valoresMalha:
            pass
        elif 1 in valoresMalha:
            print("jogador 1 ganhou")
            return True
        elif 2 in valoresMalha:
            print("jogador 2 ganhou")
            return True

    if not 0 in jogo:
        print("DEU VELHA")
        return True

    return False




malha()

while(0 in jogo):
    if jogada(1,'O') : break
    if jogada(2,'x'): break
    


    

    


