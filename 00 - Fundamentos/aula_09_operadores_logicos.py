saldo = 1000
saque = 200
limite = 100

x = saldo >= saque and saque <= limite
y = saldo >= saque or saque <= limite
print(x)
print(y)

contatos_emergencia = [] #lista vazia

print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 1500;") #string cheia
print(not "")  #string vazia

saldo_1 = 1000
saque_1 = 250
limite_1 = 200
conta_especial = True


print("\n")
print(saldo_1 >= saque_1 and saque_1 <= limite_1 or conta_especial and saldo >= saque)
print((saldo_1 >= saque_1 and saque_1 <= limite_1) or (conta_especial and saldo >= saque), "\n")



# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True


print (True and True) # = True
print (True and False) # = False
print (False and False) # = False
print (True or True) # = True
print (True or False) # = True
print (False or False) # = False
print("\n")

conta_normal_com_saldo_suficiente = saldo_1 >= saque_1 and saque_1 <= limite_1
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp)