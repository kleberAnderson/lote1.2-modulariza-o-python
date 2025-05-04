#Exercício 027 - Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.
def calcular_velocidade(numero_voltas, extensao, tempo):
    kilometragem = numero_voltas * extensao
    duracao = tempo * 60
    percurso = kilometragem / duracao
    velocidade_media = percurso * 3.6
    print("Velocidade média ==> {} km/h".format(velocidade_media))

numv = int(input("Digite o número de voltas: "))
extm = float(input("Digite a extensão do circuito (em metros): "))
temp = int(input("Digite o tempo de duração (em minutos): "))
km = numv * extm
h = temp * 60
calcular_velocidade(numv, extm, temp)
