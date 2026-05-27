def calculadora(num1, num2, operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Erro: Divisão por zero!"
        return num1 / num2
    else:
        return "Operação inválida!"


while True:
    print("\n--- Calculadora ---")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora(num1, num2, "+")
        print("Resultado:", resultado)
    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora(num1, num2, "-")
        print("Resultado:", resultado)
    elif opcao == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora(num1, num2, "*")
        print("Resultado:", resultado)
    elif opcao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calculadora(num1, num2, "/")
        print("Resultado:", resultado)
    elif opcao == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")