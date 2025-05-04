#Exercício 033 - Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
def calcular_mostrar_serie(numero):
    print("série:")
    soma = 0
    for i in range(1, numero+1):
        print("{} / {} ==> {}".format(1, i, 1/i))
        soma += (1/i)
    return  print("Resultado da somatória ==> {}".format(soma))

num = int(input("Digite um número para calcular a série: "))
calcular_mostrar_serie(num)