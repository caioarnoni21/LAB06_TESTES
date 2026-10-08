from math import inf, nan

import pytest

from laboratorio6 import (
    FAIXAS_VENTO,
    calcular_imc,
    categorizar_imc,
    classificar_pessoa,
    classificar_por_faixas,
    classificar_vento,
    tem_frete_gratis,
)


@pytest.mark.parametrize("peso,altura,imc,categoria", [
    (64, 2, 16, "abaixo do peso"),
    (88, 2, 22, "peso normal"),
    (108, 2, 27, "sobrepeso"),
    (128, 2, 32, "obesidade"),
], ids=["abaixo-do-peso", "peso-normal", "sobrepeso", "obesidade"])
def test_classes_validas_imc(peso, altura, imc, categoria):
    assert calcular_imc(peso, altura) == pytest.approx(imc)
    assert categorizar_imc(imc) == categoria
    assert classificar_pessoa(peso, altura) == categoria


@pytest.mark.parametrize("imc,esperado", [
    (18.49, "abaixo do peso"), (18.5, "peso normal"), (18.51, "peso normal"),
    (24.99, "peso normal"), (25, "sobrepeso"), (25.01, "sobrepeso"),
    (29.99, "sobrepeso"), (30, "obesidade"), (30.01, "obesidade"),
], ids=[
    "18.5-abaixo", "18.5-exato", "18.5-acima",
    "25-abaixo", "25-exato", "25-acima",
    "30-abaixo", "30-exato", "30-acima",
])
def test_fronteiras_imc(imc, esperado):
    assert categorizar_imc(imc) == esperado


@pytest.mark.parametrize("peso", [0, -1], ids=["zero", "negativo"])
def test_peso_nao_positivo(peso):
    with pytest.raises(ValueError, match="peso"):
        calcular_imc(peso, 1.75)


@pytest.mark.parametrize("altura", [0, -1], ids=["zero", "negativa"])
def test_altura_nao_positiva(altura):
    with pytest.raises(ValueError, match="altura"):
        calcular_imc(70, altura)


@pytest.mark.parametrize("velocidade,esperado", [
    (10, "calmo"), (30, "moderado"), (50, "forte"), (70, "tempestade"),
], ids=["calmo", "moderado", "forte", "tempestade"])
def test_classes_vento(velocidade, esperado):
    assert classificar_por_faixas(velocidade, FAIXAS_VENTO) == esperado
    assert classificar_vento(velocidade) == esperado


@pytest.mark.parametrize("velocidade,esperado", [
    (19.99, "calmo"), (20, "moderado"), (20.01, "moderado"),
    (39.99, "moderado"), (40, "forte"), (40.01, "forte"),
    (59.99, "forte"), (60, "tempestade"), (60.01, "tempestade"),
], ids=[
    "20-abaixo", "20-exato", "20-acima",
    "40-abaixo", "40-exato", "40-acima",
    "60-abaixo", "60-exato", "60-acima",
])
def test_fronteiras_vento(velocidade, esperado):
    assert classificar_por_faixas(velocidade, FAIXAS_VENTO) == esperado
    assert classificar_vento(velocidade) == esperado


@pytest.mark.parametrize("valor,premium,peso,esperado", [
    (200, True, 30, True),
    (200, True, 31, False),
    (200, False, 30, False),
    (200, False, 31, False),
    (199, True, 30, False),
    (199, True, 31, False),
    (199, False, 30, False),
    (199, False, 31, False),
], ids=["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"])
def test_tabela_decisao_frete(valor, premium, peso, esperado):
    assert tem_frete_gratis(valor, premium, peso) is esperado


@pytest.mark.parametrize("valor,peso,esperado", [
    (199.99, 30, False), (200, 30, True), (200.01, 30, True),
    (200, 29.99, True), (200, 30.01, False),
])
def test_fronteiras_frete(valor, peso, esperado):
    assert tem_frete_gratis(valor, True, peso) is esperado


def test_tabela_generica_diferente():
    faixas = [(0, "negativo"), (10, "pequeno"), (inf, "grande")]
    assert classificar_por_faixas(-1, faixas) == "negativo"
    assert classificar_por_faixas(0, faixas) == "pequeno"
    assert classificar_por_faixas(10, faixas) == "grande"


@pytest.mark.parametrize("faixas", [
    [], [(20, "a")], [(20, "a"), (10, "b"), (inf, "c")],
    [(20, "a"), (20, "b"), (inf, "c")],
])
def test_tabelas_invalidas(faixas):
    with pytest.raises(ValueError):
        classificar_por_faixas(5, faixas)


@pytest.mark.parametrize("valor", [nan, inf, -inf])
def test_valores_nao_finitos(valor):
    with pytest.raises(ValueError):
        categorizar_imc(valor)
    with pytest.raises(ValueError):
        calcular_imc(valor, 1.75)
    with pytest.raises(ValueError):
        calcular_imc(70, valor)
