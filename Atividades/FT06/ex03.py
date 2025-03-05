idades = [25, 15, 19, 22, 37, 78, 46, 2, 67]

count = 0
for i in idades:
    if i<18:
        count=count+1

print(count) #a
     
idades.sort(reverse = True)

print(idades) #b

x = float(input("Digite uma idade: "))

if x in idades:
    print("A idade está na lista")
    
else:
    print("não existe ninguém com essa idade na lista") #c
    
