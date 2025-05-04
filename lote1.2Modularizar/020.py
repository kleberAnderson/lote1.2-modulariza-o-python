#Receba 3 coeficientes A, B, C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
from math import sqrt

def function(a, b, c):
    d = ((b ** 2)-4*a*c)
    if d >= 0:
        if d > 0:
            print("Existem duas raízes:")
            x1 = (-b+(sqrt(d)))/(2*a)
            x2 = (-b-(sqrt(d)))/(2*a)
            print("1º raíz: {}".format(x1))
            print("2º raíz: {}".format(x2))
        else:
            print("Existe uma raíz:")
            x = (-b/(2*a))
            print("raíz: {}".format(x))
    else:
        print("Não existem raízes.")

print("Digite 3 coeficiêntes para calcular a existência de raízes.")
a1 = int(input("Digite o coeficiênte A: "))
b2 = int(input("Digite o coeficiênte B: "))
c3 = int(input("Digite o coeficiênte C: "))
function(a1, b2, c3)