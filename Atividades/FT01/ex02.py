operação = str(input("Digite a operação desejada:"))
num1 = float(input("Digite um valor para num1:"))
num2 = float(input("Digite um valor para num2:"))

match operação:

    case "+":
        print(num1+num2)
    
    case "-":
        print(num1-num2)
    
    case "*":
        print(num1*num2)
    
    case "/":
        if num2 == 0:
            print("Não pode dividir um número por 0")
        else:
             print(num1/num2)

  