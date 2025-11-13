#antes da barra (/) os parâmetros são posicionais obrigatórios
#após a barra (/) os parâmetros são posicionais ou obrigatórios
#após o asterisco (*) os parâmetros são nomeados obrigatórios

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):  
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #válidos
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") #válidos
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #inválido

def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):  
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #válido
#criar_carro_2("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") #inválido
#criar_carro_2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #inválido

def criar_carro_3(modelo, ano, placa, /, marca, *, motor, combustivel):  
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_3("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #válido
criar_carro_3("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina") #válido
#criar_carro_3(marca="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #inválido




## Objeto de Primeira classe
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def test(a, b):
    return a * 2 + b * 3


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b) # funcao = somar
    print(f"O resultado da operação é = {resultado}")

exibir_resultado(10, 10, somar)  #O resultado da operação é = 20
exibir_resultado(10, 10, subtrair)  #O resultado da operação é = 0
exibir_resultado(10, 10, test)  #O resultado da operação 10 é = 50


#Atribuíndo a variável
op = somar

print(op(1, 23)) #24



#Escopo local e escopo global  // Não é uma boa prática alterar variáveis globais dentro de funções

salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista.append(2)
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus) #2500
print(lista) #[1, 2]
 

def salario_bonus_2(bonus, lista):
    global salario
    lista_aux = lista_2.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista_2 = [1]
salario_com_bonus_2 = salario_bonus_2(500, lista_2)
print(salario_com_bonus_2) #2500
print(lista_2) #[1, 2]


