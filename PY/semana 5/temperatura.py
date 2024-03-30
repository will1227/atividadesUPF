print ("CONVERSÃO DE CRIPTOMOEDAS ")
print("----------------------------------------------------------------------------------------------------------------------------")
operacao = int(input('Digite a operação [1] para converter real em bitcoin [2] para converter Bitcoins em reais [3] para sair '))
valorTotal = 0
precoBTC = 354794


while(operacao == 1 or operacao == 2):
    if operacao == 1:
        valorReal = float(input('Digite o valor em reais '))
        valorTotal = valorReal / precoBTC
        print(
            "----------------------------------------------------------------------------------------------------------------------------")
        print("voce tem o total de ", + valorTotal, "Bitcoins em sua carteira ")
        print(
            "----------------------------------------------------------------------------------------------------------------------------")
    elif operacao == 2:
        valorBTC = float(input('Digite o valor em Bitcons '))
        valorTotal = valorBTC * precoBTC
        print(
            "----------------------------------------------------------------------------------------------------------------------------")
        print("os seus Bitcoins equivalem a  ", + valorTotal, "reais")
        print(
            "----------------------------------------------------------------------------------------------------------------------------")

    operacao = int(input('Digite a operação [1] para converter real em bitcoin [2] para converter Bitcoins em reais [3] para sair '))



print("FIM DO PROGRAMA")