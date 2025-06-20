#Calculando IMC

peso = float(input("Digite seu peso (em kg): ")) #variável chamada PESO; FLOAT - o  numero digitado pode ter virgula; INPUT - faz a pergunta e espera vc digitar algo

 
altura = float(input("Digite sua altura (em metros): ")) #igual a linha anterior, mas agora para ALTURA


imc = peso / (altura ** 2) #calculando o IMC com a formula 


print("Seu IMC é:", imc) # mostra o resultado


#agora vai começar a verificação

if imc < 18.5: 

    print("Você está abaixo do peso.") # vai aparecer essa mensagem se o IMC for menor que 18,5

# ELIF significa SENÃO, SE...

elif imc < 25: #SE NÃO ESTAVA ABAIXO DE 18,5, VEJA SE ESTÁ ABAIXO DE 25

    print("Seu peso está normal.") #se for de 18,5 até 24,9 vai aparecer esta mensagem de peso normal


elif imc < 30: #SE NÃO ERA NENHUM DOS ANTERIORES, VERIFIQUE SE É DE 25 A 29,9

    print("Você está com sobrepeso.")


#SE NAO FOR NENHUMA DAS CONDIÇÕES ANTERIORES
else:

    print("Você está com obesidade.")
