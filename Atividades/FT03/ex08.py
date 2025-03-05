l1 = float(input("Digite um número para o lado 1:"))
l2 = float(input("Digite um número para o lado 2:"))
l3 = float(input("Digite um número para o lado 3:"))

if  l1 == l2 and l2 == l3:
    print("O triângulo é equilátero")
elif l1 == l2 and l2 != l3:
    print("O triângulo é isósceles") 
else:
    print("O triângulo é escaleno")