while True:
    nome_completo = input("Digite seu apelido: ")

    if nome_completo == "Biel":
        print('Olá, {}, seja bem vindo!'.format(nome_completo))
        break 
    else:
        print('Olá, {}, voce não esta cadastrado .'.format(nome_completo))

while True:
    senha = int(input("Digite sua senha de quatro digitos: "))

    if senha == 8015:
       print('Acesso permitido!\nBem vindo a calculadora 2000')
       break
    else:
       print('Acesso negado!\nTente novamente.')

while True:

    n1 = float(input('Indique o primeiro numero: '))
    operacao = input('Indique a operação desejada (+, -, *, /): ')
    n2 = float(input('Indique o segundo numero: '))

    if operacao == "+":
        resultado = n1 + n2
    elif operacao == "-":
        resultado = n1 - n2
    elif operacao == "*":
        resultado = n1 * n2
    elif operacao == "/":
        if n2 != 0:
            resultado = n1 / n2
        else:
            resultado = "Erro: ❌ Todo número dividido por 0 é indefinido"

    print("O resultado da operação {} {} {} é: {}".format(n1, operacao, n2, resultado))
    print()
    continuar = input("Deseja realizar outra operação? (s/n): ")
    if continuar.lower() != 's':
        print("Encerrando a calculadora. Até mais {}!".format(nome_completo))
        break
    