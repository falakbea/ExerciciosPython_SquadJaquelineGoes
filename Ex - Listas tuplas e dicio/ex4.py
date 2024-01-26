contatos = {
    'Zé do Gás': '969696969',
    'Tião do carreto': '3532-0000',
    'kzalberto': '5273-1234',
    'João da Tiana': '2689-5432',
    'Juarez do açougue' : '2342-6563',
    'Zequinha do marmitex' : '98966-4525clear'
}

def procurar_contato():
    nome = input("Digite o nome do contato que deseja procurar: ")
    telefone = contatos.get(nome)

    if telefone:
        print(f"O telefone de {nome} é: {telefone}")
    else:
        print(f"Contato {nome} não encontrado.")

        procurar_contato()