#digito = int(input("Digite um número entre 1 e 9: "))
#inicial = 1
#while inicial <= 10:
#    print("{}".format(digito * inicial))
digito = int(input("Digite um número entre 1 e 9: "))
i = 1
while i < 11:
    resultado = digito * i
    print("{} x {} = {}".format(digito, i, resultado))
    i += 1