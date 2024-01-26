"""
peça dois números e imprima o maior deles
"""
numero1 = int(input("Entre com o primeiro número: "))
maior = numero1
numero2 = int(input("Entre com o segundo número: "))

if maior > numero2:
    print(f"Entre {numero1} e {numero2} o maior número é {maior}")

else:
    print(f"Entre {numero1} e {numero2} o maior número é: {numero2}")