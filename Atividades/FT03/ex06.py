x = float(input("Digite um número inteiro x:"))
y = float(input("Digite um número inteiro y:"))
z = float(input("Digite um número inteiro z:"))

if x >= y and x >= z :
    print(x, "é o maior número")
elif y >= x and y >= z:
    print(y, "é o maior número") 
else:
    print(z, "é o maior número")