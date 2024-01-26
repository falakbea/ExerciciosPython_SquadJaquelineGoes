import random

def selecionarPalavraAleatoria():
    palavras = ["python", "programacao", "jogo", "computador", "algoritmo", "desenvolvimento", "tecnologia", "inteligencia", "artificial", "aprendizado", "linguagem", "dados", "estrutura", "software", "hardware", "web", "internet", "seguranca", "criptografia", "ciberespaco"]
    return random.choice(palavras)

def substituirLetra(letra, palavraUsuario, palavraSecreta):
    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] == letra:
            palavraUsuario = palavraUsuario[:i] + letra + palavraUsuario[i+1:]
    return palavraUsuario

def main():
    palavraSecreta = selecionarPalavraAleatoria()
    vidas = 5

    tamanhoDaPalavra = len(palavraSecreta)

    palavraUsuario = '_' * tamanhoDaPalavra

    while True:
        if '_' not in palavraUsuario or vidas == 0:
            break
        print(palavraUsuario)
        letraEscolhida = input("Escolha uma letra:\n")
        if letraEscolhida in palavraSecreta:
            palavraUsuario = substituirLetra(letraEscolhida, palavraUsuario, palavraSecreta)
        else:
            vidas -= 1
            print("\nOps, uma vida a menos.\n")

    if vidas == 0:
        print(f"\nGame over :p\nA palavra era: {palavraSecreta}\n")
    else:
        print(f"\nVocê venceu! Restaram {vidas} vidas.\n")

main()
