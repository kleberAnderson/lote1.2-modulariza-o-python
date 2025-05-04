#Exercício 019 - Receba 2 valores reais. Calcule e mostre o maior deles.
def big_number(num1, num2):
    print("primeiro número {}, segundo número {}".format(num1, num2))
    if num1 > num2:
        print(num1, " > ", num2)
    elif num2 > num1:
        print(num2, ">", num1)
    else:
        print("Números iguais")

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
big_number(n1, n2)