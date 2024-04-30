#Calculadora Simples
valor1 = int(input("Informe o primeiro número: "))
valor2 = int(input("Informe o segundo número: "))
print("-> Soma : +")
print("-> subtração: -")
print("-> Multiplicação: *")
print("-> divisão: /")
operacao = input("Informe a operação com os sinais a cima: ")
resultado = 0

#fazendo Operação

if(operacao == '+'):
  resultado = valor1 + valor2
  print(valor1,operacao,valor2,'=',resultado)
elif(operacao == '-'):
  resultado = valor1 - valor2
  print(valor1,operacao,valor2,'=',resultado)
elif(operacao == '*'):
  resultado = valor1 * valor2
  print(valor1,operacao,valor2,'=',resultado)
elif(operacao == '/'):
  resultado = valor1 / valor2
  print(valor1,operacao,valor2,'=',resultado)
else:
  print("valor não encontrado")