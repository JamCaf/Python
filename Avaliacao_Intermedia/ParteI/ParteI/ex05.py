# Elabora uma script em python que peça ao utilizador um número e some todos os números de 1 até esse mesmo número. Deves utilizar o tratamento de erros.

try: 
    numero = int(input("Digite um número inteiro: ")) 
    contador = 1
    soma = 0

    while contador <= numero:
        soma = soma + contador
        contador = contador + 1
    
    print("A soma de 1 até o número inserido é:", soma) 
    
except ValueError: 
    print("Erro: O valor deve ser um número inteiro.")