a=input("Digite um valor para o lado a:")
b=input("Digite um valor para o lado b:")
c=input("Digite um valor para o lado c:")

def lados(a,b,c):
    
    if  a == b and b == c:
        return "equilátero"
    elif a == b and b != c:
        return "isósceles" 
    else:
         return "escaleno"
    