# coding=utf-8
# Desenvolvido por Ruan Araújo


from random import randint

opcao = 0
tabuadaRandom = int(randint(1, 100))
numRandom = int(randint(1, 10))
tabuada = 0
resul = 0
resulU = 0
n2 = 1
pontuacao = 0
sair = 0
while opcao != 9 :
    print("#######################################################################")
    print("###                                     #####           ####        ###")
    print("###                                      ####          ####         ###")
    print("###        Jogo Tabuada!                  ####        ####          ###")
    print("###                                        ####      ####           ###")
    print("###         Pontuação: %i                    ####    ####            ###" % pontuacao)
    print("###                                          ####  ####             ###")
    print("###                                          ##########             ###")
    print("###                                          ####  ####             ###")
    print("###                                         ####    ####            ###")
    print("###                                        ####      ####           ###")
    print("###                                       ####        ####          ###")
    print("###                                      ####          ####         ###")
    print("###  Desenvolvido por Ruan Araújo       ####            ####        ###")
    print("#######################################################################")
    print(
        "###      Opções de estudo: \n###      1. Tabuadas aleatórias \n###      2.Tabuada pré-definida(Com números aleatórios)\n###      3.Tabuada pré-definida(Em sequência 1 ao 10)"
        "\n###      5.Informações\n###      9.Sair")
    opcao = 0
    opcao = int(input("###      Digite: "))

    # Formula a operação aleatória
    def tabAle(tbR, nmR):
        print("Digite o resultado da operação: %i x %i" % (tbR, nmR))
        return int(input("Resultado: "))


    # Efetua o cálculo
    def calculo(n1, n2):
        return n1 * n2


    # Formula a operação com tabuada pré-definida e números aleatórios(até 10)
    def tabPD(tbPD, nmR):
        print("Digite o resultado da operação: %i x %i" % (tbPD, nmR))
        return int(input("Resultado: "))


    # Formula e lista tabuada padrão(tabuada pré-definida)
    def listarTab(n1, n2, res, var):
        while (n2 <= 10):
            print("%i x %i" % (n1, n2))
            res = int(input("Resultado: "))
            if res == calculo(n1, n2):
                n2 += 1
                print("\n")
                var = 1
            else:
                print("Errado, resultado correto: %i" % calculo(n1, n2))
                var = 0
                break
        if var == 1:
            return 1
        else:
            return 0

    # Verifica a opção digitada

    # É invocado os dois métodos e comparados, mostrando assim o resultado, somando ou subtraindo pontuação
    if opcao == 1:
       sair = 0
       while sair != 9:
            tabuadaRandom = int(randint(1, 100))
            numRandom = int(randint(1, 10))
            if tabAle(tabuadaRandom, numRandom) == calculo(tabuadaRandom, numRandom):
                print("=================Correto=================")
                sair = int(input("\n#~1.Continuar.\n#~9.Para retornar ao menu inicial\n#~"))
                pontuacao += 10
            else:
                print("Errado, resultado correto: %i" % calculo(tabuadaRandom, numRandom))
                sair = int(input("\n#~1.Continuar.\n#~9.Para retornar ao menu inicial\n#~"))
                pontuacao = 0

    elif opcao == 2:
        sair = 0
        while sair != 9:
            numRandom = int(randint(1, 10))
            tabuada = int(input("Digite a tabuada que deseja estudar: "))
            if calculo(tabuada, numRandom) == tabPD(tabuada, numRandom):
                print("=================Correto=================")
                pontuacao += 5
                sair = int(input("\n#~1.Continuar.\n#~9.Para retornar ao menu inicial\n#~"))
            else:
                print("Errado, resultado correto: %i" % calculo(tabuadaRandom, numRandom))
                sair = int(input("\n#~1.Continuar.\n#~9.Para retornar ao menu inicial\n#~"))
                pontuacao = 0

    elif opcao == 3:
       sair = 0
       while sair != 9:
            tabuada = int(input("Digite a tabuada que deseja estudar: "))
            if listarTab(tabuada, n2, 0, 0) == 1:
                pontuacao += 3
                sair = int(input("\n#~1.Continuar.\n#~9.Para retornar ao menu inicial\n#~"))
            else:
                pontuacao = 0
                sair = int(input("\n#~1.Continuar.\n#~9.Para retornar ao menu inicial\n#~"))

    elif opcao == 5:
        print(
            "\n#~Programa desenvolvido para fins de estudo e entrenimento, selecione a opção que deseja, somando ou subtraindo assim sua pontuação!!\n"
            "#~ Ainda em desenvolvimento!!\n"
            "#~ Regras do jogo:\n"
            "#~  1.Cada opção de jogo possue sua própria pontuação, equivalendo à sua dificuldade.\n"
            "#~  2.Cada erro zera sua pontuação.")
        input("\nEnter para retornar ao menu inicial....\n")


#print("\nSaindo...")
