#Exercício 034 - Receba um número. Calcule e mostre os resultados da tabuada desse número.
def tabuada(numero):
    for i in range(11):
        print("{} * {} ==> {}".format(i, numero, i * numero))

num = int(input("Digite um número para mostrar os resultados da tabuada: "))
tabuada(num)
