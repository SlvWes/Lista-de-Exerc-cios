# Vetores (ou listas em Python) são usados pra guardar vários valores numa mesma variável
v = [5, 8, 9]                 # Aqui a gente criou uma lista com 3 números: 5, 8 e 9

print(v)                     # Isso vai mostrar a lista inteira na tela: [5, 8, 9]

print(v[1])                  # Aqui a gente tá acessando o número que tá na posição 1 da lista. 
                             # Lembrando: as posições começam no 0, então v[1] vai mostrar o 8

# Agora vamos mostrar os valores da lista um por um, todos na mesma linha
for i in range(len(v)):      # Esse for vai de 0 até o tamanho da lista - 1
    print(v[i], end=' ')     # O end=' ' serve pra não quebrar a linha a cada número, deixando tudo na horizontal
