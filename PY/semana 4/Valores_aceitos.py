valorA = int(input("insira o valor de A "))
valorB = int(input("insira o valor de B "))
valorC = int(input("insira o valor de C "))
valorD = int(input("insira o valor de D "))

if (valorB > valorC and valorD > valorA and (valorC + valorD > valorA + valorB) and valorC > 0 and valorD > 0 and valorA % 2 == 0):
        print ("Valores aceito")
else :
        print("Valores nao aceitos")
