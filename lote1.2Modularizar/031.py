#Exercício 031 - Calcule e mostre o quadrado dos números entre 10 e 150.
def calcular_quadrado(num):
    return num ** 2

for i in range (1, 151):
    print("O quadrado do número(",i,") ==> {}".format(calcular_quadrado(i)))
