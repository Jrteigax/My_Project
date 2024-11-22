print('='* 5, 'CALCULADORA SIMPLES', '=' * 5)
while True:
    operação = input("Escolha uma operação: +, -, * ou / ")
    if operação == "+":
        s1 = float(input("Insira o primeiro número: "))
        s2 = float(input("Insira o segundo número: "))
        soma = s1 + s2
        print("Soma:", soma)
    elif operação == "-":
        s1 = float(input("Insira o primeiro número: "))
        s2 = float(input("Insira o segundo número: "))
        subtração = s1 - s2
        print("Subtração:", subtração)
    elif operação == "*":
        s1 = float(input("Insira o primeiro número: "))
        s2 = float(input("Insira o segundo número: "))
        multiplicação = s1 * s2
        print("Multiplicação:", multiplicação)
    elif operação == "/":
        s1 = float(input("Insira o primeiro número: "))
        s2 = float(input("Insira o segundo número: "))
        divisão = s1 / s2
        print("Divisão:", divisão)
    else:
        print("Operação inválida!")
        print('Calculadora finalizada')