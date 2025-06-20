# Pede a temperatura em Celsius

celsius = float(input("Digite a temperatura em Celsius: ").replace(",", ".")) #replace corrige caso digitem com vírgula

# Converte para Fahrenheit usando a fórmula
fahrenheit = (celsius * 9/5) + 32

# Mostra o resultado
print("A temperatura em Fahrenheit é:", fahrenheit)
