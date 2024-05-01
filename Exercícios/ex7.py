salario = float(input("Digite seu slário: "))
aumento = salario * 0.15
salario_final = salario + aumento
print("O funcionário que ganhava R${:.2f}, com 15%, passou a ganhar R${:.2f}".format(salario,salario_final))