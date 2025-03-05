ano = (int(input("Digite o ano para saber se é Bissexto:")))

if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
    print("O ano" , ano, "é Bissexto")
else:
    print("O ano" , ano, "não é Bissexto")