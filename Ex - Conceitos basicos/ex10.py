nome, idade, profissao, hobby = [(nome) for nome in input("Entre com o seu nome, idade, profissão e hobby separados por espaços: ").split()]

idade_convertida = int(idade)

if idade_convertida > 18:
    minha_idade = idade_convertida - 18
else:
    minha_idade = 18 - idade_convertida



print(f"Amei te conhecer, {nome}! Me chamo Débora, e moro no estado de SP! Temos {minha_idade} anos de diferença de idade! E apesar de eu gostar de {hobby}, meu hobby favorito é assistir filmes! Espero que você goste de trabalhar como {profissao}. Até mais! ")

