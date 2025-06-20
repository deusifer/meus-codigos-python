# Pede o primeiro número
num1 = float(input("Digite o primeiro número: ").replace(",", "."))

# Pede o segundo número
num2 = float(input("Digite o segundo número: ").replace(",", "."))

# Pede a operação
operador = input("Digite a operação (+, -, *, /): ")

# Faz o cálculo com base na operação escolhida
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida!"

# Mostra o resultado
print("Resultado:", resultado)
