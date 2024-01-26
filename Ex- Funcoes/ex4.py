def calcular_consumo_medio(litros, distancia):
    return distancia / litros if litros != 0 else None

def main():
    litros = float(input("Digite a quantidade de litros de combustível consumido: "))
    distancia = float(input("Digite a distância percorrida em quilômetros: "))

    consumo_medio = calcular_consumo_medio(litros, distancia)

    if consumo_medio is not None:
        print(f"O consumo médio de combustível é de {consumo_medio:.2f} km/l.")

if __name__ == "__main__":
    main()

