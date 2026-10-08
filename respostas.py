"""Respostas do Laboratório 6

EXERCÍCIO 1 - CLASSES DE EQUIVALÊNCIA
IMC                  Representante   Peso/altura usados nos testes
IMC < 18,5           16              64 kg / 2 m
18,5 <= IMC < 25     22              88 kg / 2 m
25 <= IMC < 30       27              108 kg / 2 m
IMC >= 30            32              128 kg / 2 m

Para pessoas, peso e altura devem ser positivos; portanto IMC > 0.
Entradas inválidas de calcular_imc: peso <= 0 e altura <= 0.
Testamos zero e negativo separadamente em cada entrada, mantendo a outra
válida.

EXERCÍCIO 2 - VALORES-LIMITE
Fronteira    Abaixo             Exato          Acima
18,5         18,49: abaixo      18,5: normal   18,51: normal
25           24,99: normal      25: sobrepeso  25,01: sobrepeso
30           29,99: sobrepeso   30: obesidade  30,01: obesidade

Os nove casos mostram os dois lados de cada uma das três fronteiras,
mais o próprio ponto de corte.
Embora seja possível compartilhar pontos para reduzir casos, mantivemos
os nove para tornar explícitos abaixo/exato/acima de cada fronteira.
Não existe um menor passo positivo nos reais; 0,01 é uma escolha de teste.

EXERCÍCIO 3 - GENERALIZAÇÃO E VENTO

Velocidade           Classe        Representante
v < 20               calmo         10
20 <= v < 40         moderado      30
40 <= v < 60         forte         50
v >= 60              tempestade    70

Fronteira    Abaixo             Exato          Acima
20           19,99: calmo       20: moderado   20,01: moderado
40           39,99: moderado    40: forte      40,01: forte
60           59,99: forte       60: tempestade 60,01: tempestade

A tabela segue a função de classificar o valor de V em relação as metricas de velociade

EXERCÍCIO 4 - TABELA DE DECISÃO COMPLETA
A = valor_compra >= 200; B = cliente_premium; C = peso <= 30.
S = verdadeiro; N = falso. Frete grátis = A e B e C.

Condição / ação       R1 R2 R3 R4 R5 R6 R7 R8
A: compra >= 200       S  S  S  S  N  N  N  N
B: premium             S  S  N  N  S  S  N  N
C: peso <= 30          S  N  S  N  S  N  S  N
Liberar frete grátis   S  N  N  N  N  N  N  N
Cobrar frete           N  S  S  S  S  S  S  S

Cada coluna corresponde exatamente ao teste com id R1 a R8.
Compra: S=200 e N=199. Premium: S=True e N=False.
Peso: S=30 e N=31. Os valores 200 e 30 verificam inclusão dos limites.

TABELA REDUZIDA POR DON'T CARE
O símbolo '-' significa que a condição pode ser S ou N sem mudar a ação.

Condição / ação       D1 D2 D3 D4
A: compra >= 200       N  S  S  S
B: premium             -  N  S  S
C: peso <= 30          -  -  N  S
Liberar frete grátis   N  N  N  S
Cobrar frete           S  S  S  N

D1 agrega R5, R6, R7, R8: sem compra mínima, premium e peso não importam.
D2 agrega R3, R4: atingida a compra mínima, sem premium o peso não importa.
D3 equivale a R2: compra mínima e premium satisfeitos, mas peso excedido.
D4 equivale a R1: as três condições são satisfeitas.

As quatro regras são disjuntas e cobrem 4 + 2 + 1 + 1 = 8 combinações.
A redução preserva a decisão de todas as regras da tabela completa.
"""


if __name__ == "__main__":
    print(__doc__)
