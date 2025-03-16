# IMC
# Entrada de Dados -> Processamento -> Saída

peso = float(input("Digite o seu peso em quilogramas:"))
altura = float(input("Digite a sua altura em metros"))

# Processamento

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade grau 1")
elif imc < 40:
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

#saida
print("seu imc é:", round(imc, 2))