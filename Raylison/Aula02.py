#Calculo de Medía de 4 bimestres!
n1=float(input("Qual nota do primeiro bimestre? "))
n2=float(input("Qual nota do segundo bimestre? "))
n3=float(input("Qual nota do terceiro bimestre? "))
n4=float(input("Qual nota do quarto bimestre? "))
media=float(7.0)
soma=float((n1+n2+n3+n4)/4) #Está somando as notas, e dividindo pela quantidade de bimestres.
print("Sua média final é:",soma)
if soma >= media: #Está verificando se a medía, esta a cima ou abaixo
    print("Aprovado")
else:
    print("Reprovado")