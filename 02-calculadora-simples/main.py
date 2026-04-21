while True:
    print("-"*5, "CALCULADORA SIMPLES", "-"*5)
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    print("-"*30)

    opcao= input("Digite a opção desejada: ")
    if opcao == '0':
        print("Fim do programa")
        break

    if opcao in ['1','2','3','4']:
        try:
            num1=float(input("Digite 1º número: "))
            num2=float(input("Digite 2º número: "))
            match int(opcao):
                case 1:
                    print(f"Resultado: {num1} + {num2} = {num1+num2}")
                case 2:
                    print(f"Resultado: {num1} - {num2} = {num1-num2}")
                case 3:
                    print(f"Resultado: {num1} * {num2} = {num1*num2}")
                case 4:
                    if num2==0:
                        print("Não é permitida a divisão por zero")
                    else:
                        print(f"Resultado: {num1} / {num2} = {num1/num2}")
        
        except ValueError:
            print("Erro! Tente novamente")
    else:
        print("Digite apenas as opções válidas")
