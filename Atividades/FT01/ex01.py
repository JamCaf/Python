produto = str(input("Diga o produto desejado:"))
preço = float(input("Diga o valor do produto:"))

match produto:
    case "smartphone": 
        print(preço*0.9)
    
    case "tablet": 
        print(preço*0.85)
    
    case "laptop": 
        print(preço*0.80)
    
    case _: 
        print("Não há desconto")