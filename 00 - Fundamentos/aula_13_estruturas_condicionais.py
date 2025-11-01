import sys


saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")


saldo_1 = 2000.0
saque_1 = float(input("Informe o valor do saque: "))

if saldo_1 >= saque_1:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")



opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantida para o saque: "))
elif opcao == 2:
  print("Exibindo o extrato...")
else:
  sys.exit("Opção inválida")


MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade == IDADE_ESPECIAL:
  print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")



# Estrutura condicional aninhada
conta_normal = False
conta_universitaria = False
conta_especial = True

saldo_2 = 2000
saque_2 = 5000
cheque_especial = 450

if conta_normal:
    
    if saldo_2 >= saque_2:
        print("Saque realizado com sucesso!")
    elif saque_2 <= (saldo_2 + cheque_especial):
        print("Saque realizado com uso de cheque especial!")
    else:
        print("Não foi possível realizar o saque!")

elif conta_universitaria:
    
    if saldo_2 >= saque_2:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente")

elif conta_especial:
    
    print("Conta especial selecionada!")

else:
    
    print("Sistema não reconhece seu tipo de conta, entre em contato com o seu gerente")


# Estrutura condicional ternária
saldo_3 = 2000
saque_3 = 2000

status = "Sucesso" if saldo_3 >= saque_3 else "Falha"
print(f"{status} ao realizar o saque!")
