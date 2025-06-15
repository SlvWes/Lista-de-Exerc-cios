# Matrizes são como tabelas: uma lista de listas (ou seja, vários vetores organizados em linhas e colunas)

nlin = 3   # Número de linhas
ncol = 3   # Número de colunas

m = []  # Criando a matriz (lista vazia que vai guardar as linhas)

for i in range(nlin):       # Loop para cada linha
    l = []                  # Cria uma nova linha vazia
    for j in range(ncol):   # Loop para cada coluna dentro da linha
        l.append(i + j)     # Adiciona um valor na linha (aqui estamos usando a soma do i + j como exemplo)
    m.append(l)             # Adiciona a linha completa na matriz

# Agora vamos exibir a matriz de forma organizada
for i in range(len(m)):            # len(m) dá o número de linhas na matriz
    print()                        # Quebra a linha (pra cada nova linha da matriz)
    for j in range(len(m[i])):     # len(m[i]) dá o número de colunas naquela linha
        print(m[i][j], end=' ')    # Imprime cada valor da linha, tudo na mesma linha com espaço
