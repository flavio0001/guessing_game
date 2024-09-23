def adivinhar_numero(min_valor, max_valor):
    if min_valor > max_valor:
        print("Erro. Intervalo inválido!")
        return

    palpite = (min_valor + max_valor) // 2
    resposta = input(f"O número é maior, menor ou igual a {palpite}? (maior/menor/igual): ").strip().lower()

    if resposta == 'igual':
        print(f"Acertei! O número é: {palpite}")
    elif resposta == 'maior':
        adivinhar_numero(palpite + 1, max_valor)
    elif resposta == 'menor':
        adivinhar_numero(min_valor, palpite - 1)
    else:
        print("Resposta inválida. Responda maior, menor ou igual.")
        adivinhar_numero(min_valor, max_valor)

def iniciar_jogo():
    print("Bem vindo ao jogo de adivinhação binária!")
    while True:
        try:
            min_valor = int(input("Digite o número mínimo: "))
            max_valor = int(input("Digite o número máximo: "))
            if min_valor >= max_valor:
                print("Erro. O valor mínimo deve ser menor que o valor máximo.")
                continue
            print(f"Pense em um número entre {min_valor} e {max_valor}. Vou tentar adivinhar!")
            adivinhar_numero(min_valor, max_valor)

            jogar_novamente = input("Quer jogar de novo? (s/n): ").strip().lower()
            if jogar_novamente != 's':
                print("Valeu por jogar! Até a próxima!")
                break
        except ValueError:
            print("Erro: por favor, insira números válidos.")
