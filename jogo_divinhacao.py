import random  # importa ferramenta pra gerar números aleatórios

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Pede ao jogador um número
palpite = int(input("Adivinhe um número de 1 a 10: "))

# Verifica se acertou
if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Errou! O número era", numero_secreto)
