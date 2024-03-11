tipo = input("selecione o tipo de combustivel (G para gasolina e A para alcool)")
litros = float(input("selecione a quantidade de combustivel "))
ValorA = 2.90
ValorG = 3.30
valorBruto = 0
ValorLiquido = 0
print("--------------------------------------")
#testando se o tipo esta correto
if (tipo == "A" or tipo == "G"):
    if (tipo == "A"):
        print("Alcool selecionado")
        ValorBruto = ValorA * litros
        #calculando 5% do alcool
        if (litros > 20):
            ValorLiquido = ValorBruto - (ValorBruto * 0.05)
        #calculando 3% do alcool
        else:
            ValorLiquido = ValorBruto - (ValorBruto * 0.03)
        
    else:
        print("Gasolina selecionada")
        ValorBruto = ValorG * litros
        if (litros > 20):
        #calculando 6% da gasolina    
            ValorLiquido = ValorBruto - (ValorBruto * 0.06)
        #calculando 4% da gasolina
        else:
            ValorLiquido = ValorBruto - (ValorBruto * 0.04)
    



else:
    print("tipo de combustivel nao localizado")


print("você abasteceu", + litros, "do combustivel", + tipo) 
print("valor total do combustivel", + ValorBruto)
print("valor com desconto", + ValorLiquido)









