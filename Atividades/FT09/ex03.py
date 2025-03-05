Computadores_1 = {"Marca": "Asus",
                  "Ecra": "14Pol",
                  "RAM": [4,8,12]
} #a

Computadores_1.update({"Disco": ["128G", "256G"] })
print(Computadores_1) #b

n = float(input("Digite um valor de RAM:"))

if n in Computadores_1["RAM"]:
    print("Valor correto")
else:
    print("Valor incorreto") #c

Computadores_1["RAM"] = 16 #d
print(Computadores_1)

import copy
Computadores_2 = copy.deepcopy(Computadores_1)
print(Computadores_2) #e

Computadores_2["Marca"] = "Lenovo"
Computadores_2.update({"RAM": ["4", "8"]}) 
print(Computadores_2) #f

import copy
Computadores_3 = copy.deepcopy(Computadores_2)
Computadores_3["Marca"] = "HP"
Computadores_3["Disco"] = "256G"
print(Computadores_3) #g

lista = [Computadores_1, Computadores_2, Computadores_3]

for i in lista:
    print(lista) #h

marcas = ""
for x in lista:
    if "128G" in x["Disco"]:
        marcas = marcas+ "" +x["Marca"]

print(marcas) #i

for x in lista:
    if 8 and 12 in x["RAM"]:
        print(x["Marca"]) #j

#sliliana.oliveira@gmail.com