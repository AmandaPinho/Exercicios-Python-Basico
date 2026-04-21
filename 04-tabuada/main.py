try:
    num=int(input("Digite um número inteiro: "))
    print(f"Tabuada de {num}")
    
    print("SOMA")
    for i in range(1, 11):
            resultado = num + i
            print(f"{num} + {i:2} = {resultado:.2f}")
    print("-"*30)

    print("SUBTRAÇÃO")
    for i in range(1, 11):
            resultado = num - i
            print(f"{num+i:2} - {num} = {resultado:.2f}")
    print("-"*30)

    print("MULTIPLICAÇÃO")
    for i in range(1, 11):
            resultado = num * i
            print(f"{num} x {i:2} = {resultado:.2f}")
    print("-"*30)

    print("DIVISÃO")
    for i in range(1, 11):
            dividendo = num * i
            print(f"{dividendo:2} / {num} = {i:2}")
            
except ValueError:
       print("Erro: Digite apenas números inteiros")

