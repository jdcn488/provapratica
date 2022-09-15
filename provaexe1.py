n1 = int(input("digite o primeiro numero: "))

n2 = int(input("digite o segundo numero: "))

n3 = int(input("digite o terceiro numero: "))

if n1>n2 and n1>n3:

    print("O maior é: "+str(n1))

elif n2>n1 and n2>n3:

    print("O maior é: "+str(n2))

else:

    print("O maior é: "+str(n3))