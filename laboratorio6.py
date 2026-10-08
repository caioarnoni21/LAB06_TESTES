from math import inf, isfinite


FAIXAS_IMC = [
    (18.5, "abaixo do peso"),
    (25, "peso normal"),
    (30, "sobrepeso"),
    (inf, "obesidade"),
]

FAIXAS_VENTO = [
    (20, "calmo"),
    (40, "moderado"),
    (60, "forte"),
    (inf, "tempestade"),
]


def classificar_por_faixas(valor, faixas):
    if not isfinite(valor):
        raise ValueError("O valor deve ser finito.")
    if not faixas or faixas[-1][0] != inf:
        raise ValueError("A tabela deve terminar com limite infinito.")
    anterior = -inf
    for limite, _ in faixas:
        if not limite > anterior:
            raise ValueError("Os limites devem ser estritamente crescentes.")
        anterior = limite
    for limite, rotulo in faixas:
        if valor < limite:
            return rotulo
    raise ValueError("Valor fora da tabela.")


def calcular_imc(peso, altura):
    if not isfinite(peso) or peso <= 0:
        raise ValueError("O peso deve ser positivo e finito.")
    if not isfinite(altura) or altura <= 0:
        raise ValueError("A altura deve ser positiva e finita.")
    return peso / altura**2


def categorizar_imc(imc):
    return classificar_por_faixas(imc, FAIXAS_IMC)


def classificar_pessoa(peso, altura):
    return categorizar_imc(calcular_imc(peso, altura))


def classificar_vento(velocidade):
    return classificar_por_faixas(velocidade, FAIXAS_VENTO)


def tem_frete_gratis(valor_compra, cliente_premium, peso):
    return valor_compra >= 200 and cliente_premium and peso <= 30


def main():
    print("Laboratório 6 - IMC, vento e frete")
    print("Use ponto ou vírgula para informar números decimais.")
    try:
        peso = float(input("Peso (kg): ").replace(",", "."))
        altura = float(input("Altura (m): ").replace(",", "."))
        imc = calcular_imc(peso, altura)
        print(f"IMC: {imc:.2f} | Classificação: {classificar_pessoa(peso, altura)}")
        print("A classificação usa o IMC sem arredondar.")
    except ValueError as erro:
        print(f"Entrada inválida: {erro}")
    print(f"Vento de 40: {classificar_vento(40)}")
    print(f"Frete grátis (R$ 200, premium, 30 kg): {tem_frete_gratis(200, True, 30)}")


if __name__ == "__main__":
    main()
