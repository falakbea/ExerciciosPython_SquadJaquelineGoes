valores_permitidos = ['M', 'V', 'N']

turno = input("Em que turno você estuda? Responda com:\nM para matutino\n" +
              "V para vespertino\nN para noturno.\n")

if turno not in valores_permitidos:
    print("Valor inválido!")

elif turno == 'M':
    print("Bom dia!")

elif turno == 'V':
    print("Boa tarde!")

else:
    print("Boa noite!")