
consulta = int(input("digite [1] para consulta´[2] para saque [3] para deposito [4] para sair: "))

saldo = float(0.00)

if consulta == 1:

    print("seu saldo e: " + str(saldo))

elif consulta == 2:

    print("voce não tem saldo para sacar")

elif consulta == 3:

    deposito = float("digite o valor: ")

    saldo = saldo + deposito

else:
    print("até a proxima")

