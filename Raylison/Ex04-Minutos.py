minutos=int(input("Quantos minutos você utilizou, no mês? "))
if minutos<200:
    preço=0.20
    resultado=minutos*preço
    print(f"Valor da sua conta será de R${resultado}")
else:
    if minutos<400:
        preço=0.18
        resultado=minutos*preço
        print(f"Valor da sua conta será de R${resultado}")
    else:
        preço=0.15
        resultado=minutos*preço
        print(f"Valor da sua conta será de R${resultado}")

