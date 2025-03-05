
nome = str(input("Digite o seu nome:"))
idade = int(input("Digite a sua idade:"))
massa = float(input("Digite a sua massa corporal:"))
altura = float(input("Digite a sua altura:"))

IMC = massa / (altura*altura)

if  IMC < 17:
    print("Muito abaixo do peso ideal")
elif IMC >= 17 and IMC < 18.5:
    print("Abaixo do peso") 
elif IMC >= 18.5 and IMC < 25:
    print("Peso normal")
elif IMC >= 25 and IMC < 30:
    print("Acima do peso")
elif IMC >= 30 and IMC < 35:
    print("Obesidade I")
elif IMC >= 35 and IMC < 40:
    print("Obesidade II")
else:
    print("Obesidade mórbida")       