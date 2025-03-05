soma=0
produto=1

N = int(input("Digite um valor de N para que seja feita a soma e o produto dos N primeiros números naturais:"))

N=int(N)

for x in range(1,N+1):
    soma+=x
    produto*=x
    
print("soma=", soma)
print("produto=", produto)