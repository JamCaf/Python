estadocivil = str(input("Digite o seu estado civil:"))

match estadocivil.upper():
    case "S":
        print("Solteiro")
    
    case "C":
        print("Casado")

    case "V":
        print("Viúvo")
    
    case _:
        print("Estado civil desconhecido")