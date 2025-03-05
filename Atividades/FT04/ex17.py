lista = []
x=1
n=0

for i in range(20):
    
    while x<=20:
       n=(int(input(f"Introduza o {x}º número:")))
       x+=1
       lista.append(n)
    
print(lista)
    
print(f"A soma dos números inseridos é:", sum(lista))

print(f"A média dos números inseridos é:", sum(lista)/len(lista)) 
