
def sacar(valor:float):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("Retire o seu dinheiro na boca do caixa.")
        #saldo -= valor
    print("Obrigado por ser nosso cliente, tenha um bom dia!")
    

sacar(1000)


def depositar(valor):
    saldo = 500
    saldo += valor