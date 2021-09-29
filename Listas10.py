from random import randint

numeros = []

for x in range(0, 100):
    random = (randint(1, 6)) 
    numeros.append(str(random))

num1 = numeros.count("1")
num2 = numeros.count("2")
num3 = numeros.count("3")
num4 = numeros.count("4")
num5 = numeros.count("5")
num6 = numeros.count("6")
print("O número 1 foi sorteado: ", num1, " vezes.")
print("O número 2 foi sorteado: ", num2, " vezes.")
print("O número 3 foi sorteado: ", num3, " vezes.")
print("O número 4 foi sorteado: ", num4, " vezes.")
print("O número 5 foi sorteado: ", num5, " vezes.")
print("O número 6 foi sorteado: ", num6, " vezes.")