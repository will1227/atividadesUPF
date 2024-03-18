salario = float(input("Insira o seu salario "))
imposto = float(0)



if (salario <= 2000):
    print("voce esta isento")
elif(salario > 2000.01 and salario <= 3000.00):
    imposto = (0.08	 * (salario - 2000.00))
    print (imposto)
elif(salario > 3000.01 and salario <= 4500.00):
    imposto = (80 + 0.18 * (salario - 3000.00))
    print (imposto)
else:
    imposto = (350 + 0.28 * (salario - 4500))
    print (imposto)
    
    