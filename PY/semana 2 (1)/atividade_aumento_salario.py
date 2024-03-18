nome = input("Digite o nome ")
salario = float(input("digite o salario atual "))
reajuste = float(input("informe o reajuste " ))

salarionovo = (salario * (reajuste / 100)) + salario

print (salarionovo)


print ("ola %s, seu novo salario é %s" % (nome, salarionovo))