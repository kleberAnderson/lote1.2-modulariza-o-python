#Exercício 025 - Receba a hora de início e de final de um jogo (HH,MM) sabendo que o tempo máximo é de 24 horas e pode começar num dia e terminar noutro.
def calcular_hora(h, m):
    if h == 0:
        if m == 0:
            print("Tempo máximo ultrapassado.")
        elif m < 0:
            m = (m + 60)
            print("horas - {}:{}".format(h, m))
        else:
            print("horas - {}:{}".format(h, m))
    elif h < 0:
        h = h + 24
        if m == 0:
            print("horas - {}:{}".format(h, m))
        elif m < 0:
            m = m + 60
            print("horas - {}:{}".format(h, m))
        else:
            print("horas - {}:{}".format(h, m))
    elif m == 0:
        print("horas - {}:{}".format(h, m))
    elif m < 0:
        h = h + 1
        m = m + 60
        print("horas - {}:{}".format(h, m))
    else:
        print("horas - {}:{}".format(h, m))

print("Digite o horário de início do jogo.")
hi = int(input("Digite as horas: "))
mi = int(input("Digite os minutos: "))
print("Digite o horário do fim do jogo.")
hf = int(input("Digite as horas: "))
mf = int(input("Digite os minutos: "))

horas = hf - hi
minutes = mf - mi

calcular_hora(horas, minutes)
