nota1= float(input("Digite 1ª nota: "))
nota2= float(input("Digite 2ª nota: "))
nota3= float(input("Digite 3ª nota: "))

media= (nota1+nota2+nota3)/3
print(f"Média: {media:.2f}")

if media>=7:    
    print("Aprovado(a)!")
else:
    print("Reprovado(a)!")