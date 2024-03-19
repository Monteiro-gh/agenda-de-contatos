class Nota:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

def adicionar_nota(notas, titulo, descricao):
    nova_nota = Nota(titulo, descricao)
    notas.append(nova_nota)
    print("Número adicionada com sucesso!")

def exibir_notas(notas):
    if notas:
        print("Seus Número:")
        for i, nota in enumerate(notas, start=1):
            print(f"Contato Número {i} : {nota.titulo} - Descrição: {nota.descricao}")
    else:
        print("Nenhuma nota encontrada.")

def deletar_nota(notas, indice):
    if indice < 0 or indice >= len(notas):
        print("Contato inválido.")
    else:
        del notas[indice]
        print("Número deletada com sucesso!")



def main():
    notas = []

    while True:
        print("\n:===Agenda de números===:")
        print("1. Adicionar Número")
        print("2. Ver Número Salvos")
        print("3. exluir Número")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do Número: ")
            descricao = input("Digite a descrição da Número: ")
            adicionar_nota(notas, titulo, descricao)
        elif opcao == "2":
            exibir_notas(notas)
        elif opcao == "3":
            indice = int(input("Digite o número de contato desejado: ")) - 1
            deletar_nota(notas, indice)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()