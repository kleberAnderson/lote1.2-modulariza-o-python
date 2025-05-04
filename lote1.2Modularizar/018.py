#Exercício 019 - Receba 2 valores reais. Calcule e mostre o maior deles.
def number(num1, num2):
    return abs(num1 - num2)

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
print("A diferença entre os dois valores reais: {}".format(number(v1, v2)))
