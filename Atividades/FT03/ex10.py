operação = str(input("Digite a operação desejada:"))
num1 = float(input("Digite um valor para x:"))
num2 = float(input("Digite um valor para y:"))

if operação == "+":
    print(num1 + num2)
elif operação == "-":
    print(num1-num2)
elif operação == "*":
    print(num1*num2)
elif operação == "/":
    if num2 == 0:
        print("Não pode dividir um número por 0")
    else:
        print(num1/num2)
else:
    print("Operação inválida")