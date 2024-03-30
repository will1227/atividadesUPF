valorC = float(input("Insira o valor total da compra "))
prestacoes = int(input("Insira o numero de prestações "))
valorJ = 0
valorT = 0
if (prestacoes <= 5 and prestacoes >= 2) :
    valorJ = valorC * 0.05
    valorT = valorJ + valorC
    print ("valor da compra", + valorC)
    print("valor juros", + valorJ)
    print("valor total", + valorT)

elif (prestacoes > 5 and prestacoes <= 12) :
    valorJ = valorC * 0.10
    valorT = valorJ + valorC
    print ("valor da compra", + valorC)
    print("valor juros", + valorJ)
    print("valor total", + valorT)

else:
    print("numero de prestações invalidos")

repete = input("deseja repetir o programa? [S] ou [N]")

while (repete == "S"):
    valorC = float(input("Insira o valor total da compra "))
    prestacoes = int(input("Insira o numero de prestações "))
    valorJ = 0
    valorT = 0
    if (prestacoes <= 5 and prestacoes >= 2) :
        valorJ = valorC * 0.05
        valorT = valorJ + valorC
        print ("valor da compra", + valorC)
        print("valor juros", + valorJ)
        print("valor total", + valorT)

    elif (prestacoes > 5 and prestacoes <= 12) :
        valorJ = valorC * 0.10
        valorT = valorJ + valorC
        print ("valor da compra", + valorC)
        print("valor juros", + valorJ)
        print("valor total", + valorT)
        
    else:
        print("numero de prestações invalidos")

        
    repete = input("deseja repetir o programa? [S] ou [N]")

print("programa finalizado")