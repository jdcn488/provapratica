
palavra = "saida"

digitado = []

inicio = 1

while inicio ==1:

    letra = str(input("digite a letra: "))

    if len(letra) > 1:
        print("so uma letra")
        continue

        digitado.append(letra)

        palavra =""

        for palavra_secreta in palavra:

            if letra_secreta in digitadas:
                palavra_secreta += letra_secreta
            else:
                palavra_secreta += '*'
        if palavra_secreta == palavra:
            print ("venceu")
        else:
            print ("perdeu")

