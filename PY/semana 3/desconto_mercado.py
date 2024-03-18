produto = input("escreva o nome do produto ")
quantidade = float(input("Insira a quantidade do produto "))
preco = float(input("insira o valor do produto "))

total = (quantidade * preco)

desconto = 0

totalPagar = (total - desconto)



if (quantidade <= 5):
    desconto = total * 0.02
elif (quantidade > 5 and  quantidade <= 10):
    desconto = total * 0.03
else :
    desconto = total * 0.05
    
total = total - desconto

print("-----------------------------------------------------------------------")
print("valor desconto R$ ", desconto)
print("total a pagar R$ ", total)