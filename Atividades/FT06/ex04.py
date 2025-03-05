nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]

c_int=0
c_float=0
c_str=0
c_bool=0

for x in nums:
    if type(x)==int:
        c_int=c_int+1
        continue
    if type(x)==float:
        c_float=c_float+1
        continue
    if type(x)==str:
        c_str=c_str+1
        continue
    if type(x)==bool:
        c_bool=c_bool+1

print(c_int)
print(c_float)
print(c_str)
print(c_bool)

valores_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
media = sum(valores_inteiros) / len(valores_inteiros)
print(media)

lista_inteiros = [x for x in nums if isinstance(x, int) and not isinstance(x, bool)]
print(lista_inteiros)

# a. Calcula e Imprime a quantidade de inteiros, floats, strings e boleanos na lista
int_count = sum(isinstance(x, int) and not isinstance(x,bool) for x in nums)
float_count = sum(isinstance(x, float) for x in nums)
str_count = sum(isinstance(x, str) for x in nums)
bool_count = sum(isinstance(x, bool) for x in nums)
print(f"Quantidade de inteiros: {int_count}")
print(f"Quantidade de floats: {float_count}")
print(f"Quantidade de strings: {str_count}")
print(f"Quantidade de booleanos: {bool_count}")