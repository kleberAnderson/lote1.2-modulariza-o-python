#Exercício 022 - Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
def procedure_ordenar(n1, n2):
    if n1 < n2:
        print("ordem ==> {}, {}".format(n1, n2))
    else:
        print("ordem ==> {}, {}".format(n2, n1))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 == num2:
    print("Números iguais.")
else:
    procedure_ordenar(num1, num2)