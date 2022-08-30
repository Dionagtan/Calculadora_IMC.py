print("----Calculo IMC----")
print(30*"-")
peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura"))

calculo = float(peso / (altura * altura))
print(30*"-")

print(f"Índice de Massa Corporal (IMC) {round(calculo,2)}")
