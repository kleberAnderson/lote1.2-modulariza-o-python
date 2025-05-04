#Exercício 023 - Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem.
#Mostre os 4 números em ordem crescente:
def ordenar_numeros(n1, n2, n3, n):
    print("Números ordenados:")
    if n > n3:
        print("==> {}, {}, {}, {}".format(n1, n2, n3,n))
    elif n > n2:
        print("==> {}, {}, {}, {}".format(n1, n2, n, n3))
    elif n > n1:
        print("==> {}, {}, {}, {]".format(n1, n, n2, n3))
    else:
        print("==> {}, {}, {}, {}".format(n, n1, n2, n3))


print("Digite três valor em ordem crescente:")
num1 = float(input("Digite o 1º valor: "))
num2 = float(input("Digite o 2º valor: "))
num3 = float(input("Digite o 3º valor: "))
print("Digite o 4º valor em fora de ordem:")
num = float(input("Digite o 4º valor: "))
ordenar_numeros(num1, num2,num3, num)

