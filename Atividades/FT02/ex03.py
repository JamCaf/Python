num = input("Digite um número inteiro:")
num = int(num)

dobro = 2*num 

print("O dobro de", num, "é", dobro)

output = "O dobro de %s é %s"%(num,dobro)

output2 = "O dobro de {} é {}".format(num,dobro)

output3 = f"O dobro de {num} é {dobro}"

print(f"O dobro de {num} é {dobro}")