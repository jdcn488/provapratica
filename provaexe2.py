
idade = int(input("digite a sua idade: "))

tempo = int(input("digite o tempo de serviço: "))

if idade >= 65:

    print("Voce esta apto para se aposentar")

elif tempo >= 30:

    print("Voce esta apto para se aposentar")

elif idade == 60 and tempo >= 25:

    print("Voce esta apto para se aposentar")

else:
    print("Voce não esta apto para se aposentar")