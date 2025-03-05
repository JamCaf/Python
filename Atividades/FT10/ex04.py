Txt="""Python é uma linguagem de programação 
de alto nível, interpretada de script, imperativa, orientada a objetos
funcional, de tipagem dinâmica forte"""

print(Txt.upper()) #a

a = input("Digite uma palavra:")

if a in Txt:
    print("A palavra está contida no texto")
else:
    print("A palavra não está contida no texto") #b

print(Txt.count("o")) #c

print(Txt.replace("p","_")) #d


