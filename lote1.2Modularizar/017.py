#Exercício 017 - Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/L.
#Receber o tempo de percurso e a velocidade média.
def calculo_qtd_gasolina(tempo_percurso, velocidade_media):
    percurso = tempo_percurso * velocidade_media
    return percurso / 12

tempcurso = float(input("Digite o tempo do percurso em Horas: "))
velmedia = int(input("Digite a velocidade média em Km/h: "))

print("Quantidade de litros gastos em na viagem: {} L".format(calculo_qtd_gasolina(tempcurso, velmedia)))


