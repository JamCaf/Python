contador = 1
soma = 0

while contador <=4:
    numero = int(input(f"Digite o {contador}º número: "))
    soma = soma + numero
    contador = contador + 1

média = soma/4
print(f"A média dos números introduzidos é {média}")

# x+=1 é o mesmo que x = x + 1
# x-=1 é o mesmo que x = x - 1
# x*=1 é o mesmo que x = x * 1
# x/=1 é o mesmo que x = x / 1
# x%=1 é o mesmo que x = x % 1

contador = 0
soma = 0
while contador <4:
    numero = int(input(f"Introduza o {contador+1}º número: "))
    soma = soma + numero     
    contador =contador + 1
    
print(contador)
media = soma / contador
print(f"A média dos números introduzidos é {media}")