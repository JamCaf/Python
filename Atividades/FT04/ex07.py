x=1
soma=0
Num_ins=0
Num=int(input("Digite um número N para a soma dos números de 1 a N:"))

while x<=Num:
    Num_ins=(input(f"Introduza o {x}º número: \t"))
    soma+=int(Num_ins)
    
    x+=1

    print(f"O total dos {Num} números introduzidos tem como soma: {soma}")

