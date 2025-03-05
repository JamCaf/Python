# Elabora uma script em python que peça ao utilizador dois números e devolva a divisão do primeiro número introduzido pelo seguinte. Trate erros como divisão por zero e valores inválidos.

try: 
    x = int(input("Digite o numerador: ")) 
    y = int(input("Digite o denominador: ")) 
    print("Resultado da divisão:", x / y) 
except ZeroDivisionError: 
    print("Erro: Não é possível dividir por zero.") 
except ValueError: 
    print("Erro: Apenas números inteiros são permitidos.")