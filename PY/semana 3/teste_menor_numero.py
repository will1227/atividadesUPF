a = int(input("valor A "))
b = int(input("valor B "))
c = int(input("valor C "))

menor = 0

if(a < b and a < c):
    menor = a
    
elif (b < a and b < c):
    menor = b
    
else :
    menor = c
    
print ("o menor numero é:", + menor)