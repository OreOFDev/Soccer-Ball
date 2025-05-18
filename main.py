import random as r  # importa o módulo random com o apelido r
import time as t    # importa o módulo time com o apelido t

gols = 0           # variável global para contar gols do jogador
passes = 0         # variável global para contar passes feitos
dribles = 0        # variável global para contar dribles feitos
golInimigo = 0     # variável global para contar gols do inimigo
print("Bem Vindo Ao Soccer Ball")

def jogo():
    global gols, passes, dribles, golInimigo  # permite modificar as variáveis globais dentro da função
    
    print("Voce avanca!")
    pergunta = input("VOCE ESTA DO LADO DO GOL FAZER GOL? (s/n): ").lower()  # pergunta se o jogador está na posição de chute
    if pergunta == "s":  # se estiver do lado do gol para chutar
        menssagem = print("ESCOLHA O TIPO DO CHUTE! RAPIDO")  # pede para escolher tipo de chute (a variável menssagem não é usada)

        tipo = input("""  # recebe o tipo de chute desejado
                    C = CURVO
                    L = LONGO
                    R = RAPIDO
                    """).lower()
        
        if tipo == "c":  # chute curvo
            chance = r.randint(1,100)  # sorteia um número entre 1 e 100 para determinar resultado

            if chance <= 50 and chance > 35:  # chance entre 36 e 50 para gol
                print("O GOLEIRO TENTA PEGAR MAS VOCE MARCA")
                gols += 1  # incrementa gols

            elif chance >= 85:  # chance maior ou igual a 85 para um evento especial
                print("VOCE ERROU MAS PEGOU A BOLA")     
                avancar = input("DESEJA AVANCAR: (s/n): ").lower()  # pergunta se quer avançar

                if avancar == "s":  # se quiser avançar
                    chance = r.randint(1,100)  # nova chance sorteada
                    if chance > 50:  # chance maior que 50 para gol olímpico
                        print("OQUE UM GOL OLIMPICO NO ANGULO PORRA QUE ISSO")
                        print("OQUE O JUIZ TE DEU 2 GOLS POR ISSO???")
                        gols += 2  # soma 2 gols

                    else:
                        chance = r.randint(1,100)  # nova chance para passe ou erro
                        if chance > 50:  # chance para passe perfeito
                            print("VOCE DESVIOU DE TODOS E DEU UM PASSE PERFEITO!")
                            passes += 1
                        else:  # se não fez passe
                            print("Voce TOMOU UMA RASTEIRA! POIS NAO AVANCOU")
            else:
                print("Voce erra...")  # chute curvo que erra sem consequências especiais
        
        elif tipo == "l":  # chute longo
            chance = r.randint(1,100)  # sorteia chance

            if chance <= 50 and chance > 35:  # gol com chute de 10 metros
                print("VOCE FAZ UM CHUTE DE 10 METROS DE DISTANCIA!")
                gols += 1

            elif chance >= 85:  # gol no ângulo
                gols += 1
                print("VOCE ACERTA NO ANGULO!!!!!")     

            else:
                print("Voce erra...")  # chute longo que erra
        
        elif tipo == "r":  # chute rápido
            chance = r.randint(1,100)  # sorteia chance

            if chance <= 50 and chance > 35:  # chute rápido que erra
                print("CHUTE RAPIDO MAS VOCE ERRA!")

            elif chance >= 85 and chance < 100:  # gol rápido onde goleiro não vê
                print("FOI TAO RAPIDO QUE O GOLEIRO NEM VIU..")   
                gols += 1  

            elif chance == 100:  # sorte máxima, gol triplo
                print("Oque? fez gol no angulo e o goleiro nao viu o chute?")
                print("pera sua sorte foi de 100??? O JUIZ TE DEU 3 GOLS POR ISSO")
                gols += 3

            else:
                print("Voce erra...")  # chute rápido que erra

    else:  # caso o jogador não esteja do lado do gol para chutar   

        print("DECIDA RAPIDO!")
        decisao = input("""  # apresenta opções de movimento fora da posição de chute
                C = CORRER MAIS PARA FRENTE
                L = CORRER MAIS PARA TRAS
                P = PASSAR
                GG = CHUTE FORTE
                """)
        
        if decisao == "c":  # correr para frente
            chance = r.randint(1,100)  # sorteia chance
            if chance > 75:  # sucesso em correr para frente
                print("NINGUEM TE ALCANCE SELOKO!!")
            else:  # adversário está perto, drible necessário
                print("TEM UMA PESSOA MUITO PERTO DE VOCE SEJA RAPIDO DRIBLE!")
                drible = input("DESEJA Fazer um drible? (s/n): ").lower()  # pergunta se quer driblar

                if drible == "n":  # se não driblar
                    print("ELE TE DEU UMA RASTEIRA")
                else:  # tenta driblar
                    chance = r.randint(1,100)
                    if chance > 50:  # sucesso no drible e gol
                        print("VOCE SAI CORRENDO DRIBLANDO ELE E MARCA O GOL!")
                        dribles += 3
                        gols += 1
                    else:  # drible falhou (não há ação definida)
                        pass

        elif decisao == "l":  # correr para trás
            print("ALGUEM TE DEU UMA RASTEIRA E VOCE CAIU!")

        elif decisao == "p":  # passar a bola
            chance = r.randint(1,100)
            
            if chance > 75 and chance < 100:  # passe perfeito que conta como 2 passes
                print("PASSE PERFEITASSO CARAI!")
                print("O JUIZ CONTOU COMO 2 PASSES!")
                passes += 2

            elif chance <= 50:  # passe bom que conta como 1 passe
                print("PASSE BOM!")
                passes += 1

            else:  # passe errado
                print("VOCE ERROU O PASSE!")  
              
        elif decisao == "gg":  # chute forte de longe
            print("VOCE MARCOU DE MUITO LONGE!")
            gols += 1

def golInimigoF():
    chance = r.randint(1,100)  # sorteia chance para gol do inimigo

    if chance <= 50:  # gol simples do inimigo
        print("O INIMIGO MARCA O GOL!")
        golInimigo += 1

    elif chance >= 85:  # gol duplo do inimigo no ângulo
        print("O INIMIGO MARCA O GOL NO ANGULO 2 VEZES SEGUIDAS!")
        golInimigo += 2

    else:  # inimigo erra o chute
        print("O INIMIGO ERROU O CHUTE!")

# roda o jogo duas vezes
for i in range(2):
    jogo()
    
# imprime resultado final do jogo
print(f"Voce fez {gols} gols, {passes} passes e {dribles} dribles e tomou {golInimigo} gols no jogo!")
