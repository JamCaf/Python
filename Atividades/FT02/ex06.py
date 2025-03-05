horas = int(input("Digite um valor inteiro para horas:"))
minutos = int(input("Digite um valor inteiro  para minutos:"))
segundos = int(input("Digite um valor inteiro para segundos:"))

conversão = horas*3600 + minutos*60 + segundos*1

print("O total em segundos é", conversão)