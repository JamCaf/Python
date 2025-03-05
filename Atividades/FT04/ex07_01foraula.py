contador=1
soma_numeros=0
numero_inserido=0
total_numeros_introduzidos = int(input("Introduza o total de números inteiros positivos: "))
while contador <= total_numeros_introduzidos:
    numero_inserido = (input(f"introduza o {contador}º número: \t"))
    soma_numeros += int(numero_inserido)
    contador += 1
print(f"O total dos {total_numeros_introduzidos} números introduzidos tem como soma: {soma_numeros}")