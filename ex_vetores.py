import random as ran 

# Cria vetor com 10 números inteiros aleatórios entre 1 e 100
vetores = [ran.randint(1, 100) for _ in range(10)]

# Maior e menor
maior = vetores[0]
menor = vetores[0]

for num in vetores:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print("Maior número:", menor)
print("Menor número:", menor) 

# Soma e Média 
soma = sum(vetores)
print("A soma é:",soma)
media = sum(vetores) / len(vetores)
print("A média é:",media)

# Ordenação Bubble Sort
for i in range(len(vetores)):
    for j in range(len(vetores) - 1):
        if vetores[j] > vetores[j + 1]:
            # Troca os valores vizinhos se estiver fora de ordem
            vetores[j], vetores[j + 1] = vetores[j + 1], vetores[j]

print("Vetor ordenado (crescente):", vetores)


