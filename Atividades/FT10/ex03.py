datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

dados = datas.replace(","," ")

inf = dados.split()

print(inf) #a

for x in inf:
    if "2022" in x:
        print(x) #b

dias = [] 
print(dias)

for x in inf:
    dias.append(x[:2])

dias.sort()
print(dias) #c
