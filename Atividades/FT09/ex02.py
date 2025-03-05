notas = {"Matemática": 10,
         "Português": 9,
         "Biologia": 8
}

print(notas) #a

notas.update({"Inglês": 10})
notas.update({"Espanhol": 9})
print(notas) #b

notas.pop("Espanhol")
print(notas) #c

notas["Português"] = 10
print(notas) #d
