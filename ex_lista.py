# Lista dinâmica:
# Insira 5 nomes digitados pelo usuário.
# Remova um nome escolhido.
# Verifique se determinado nome existe e exiba sua posição.

nome1 = input("Escreva o primeiro nome: ")
nome2 = input("Escreva o segundo nome: ")
nome3 = input("Escreva o terceiro nome: ")
nome4 = input("Escreva o quarto nome: ")
nome5 = input("Escreva o quinto nome: ")

usuarios = [nome1, nome2, nome3, nome4, nome5]

# Função para remover usuário 
def nome_remover():
    nome = input("Digite o nome que deseja remover: ")
    if nome in usuarios:
        usuarios.remove(nome)
        print(f"Nome '{nome}' removido da lista.")
    else:
        print(f"Nome '{nome}' não foi encontrado na lista.")

nome_remover()

print(usuarios)

resposta = input("Deseja verificar se um nome está na lista? (s/n): ").lower()

if resposta == "s":
    # Função para verificação
    def verificar_nome():
        nome = input("Digite o nome que deseja verificar: ")
        if nome in usuarios:
            posicao = usuarios.index(nome)
            print(f"Nome '{nome}' está na posição {posicao} da lista.")
        else:
            print(f"Nome '{nome}' não está na lista.")

    verificar_nome()
else:
    print("Verificação de nome ignorada.")

# Mostrar lista final
print("Lista final de usuários:", usuarios)

