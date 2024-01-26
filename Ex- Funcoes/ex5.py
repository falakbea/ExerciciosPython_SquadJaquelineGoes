def calcular_moedas_estrangeiras(valor_em_reais):
    taxas_de_cambio = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.2,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suíço': 0.42,
        'Euro': 5.36,
        'Libra Esterlina': 6.21
    }

    carteira_em_moedas = {moeda: valor_em_reais / taxa for moeda, taxa in taxas_de_cambio.items()}

    return carteira_em_moedas

def main():
    try:
        valor_em_reais = float(input("Digite a quantia em reais que você tem na carteira: R$ "))
        carteira_em_moedas = calcular_moedas_estrangeiras(valor_em_reais)

        print("\nQuantidade em moedas estrangeiras:")
        for moeda, quantidade in carteira_em_moedas.items():
            print(f"{moeda}: {quantidade:.2f}")

    except ValueError:
        print("Por favor, digite um valor numérico válido.")

if __name__ == "__main__":
    main()
