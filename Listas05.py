from random import sample

tamanho = 20
valores = range(1, 99)

inteiros = sample(valores, tamanho)
pares = []
impares = []

for x in inteiros:
    if x % 2 != 0:
        impares.append(x)
    else:
        pares.append(x)

print("A lista de números inteiros é: ", inteiros)
print("\nA lista de números pares é: ", pares)
print("\nA lista de números ímpares é: ", impares)

