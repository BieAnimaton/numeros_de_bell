def perguntar_numero():
    valor = int(input("Digite o valor de entrada para calcular o número de Bell: "))

    return valor

def calcular_numero_bell(valor):
    num_bell = [[0 for cont1 in range(valor + 1)] for cont2 in range(valor + 1)]

    num_bell[0][0] = 1
    for cont1 in range(1, valor + 1):
        num_bell[cont1][0] = num_bell[cont1 - 1][cont1 - 1]

        for cont2 in range(1, cont1 + 1):
            num_bell[cont1][cont2] = num_bell[cont1 - 1][cont2 - 1] + num_bell[cont1][cont2 - 1]

    print("O número de Bell de {} é {}".format(valor, num_bell[valor][0]))

valor = perguntar_numero();
calcular_numero_bell(valor)