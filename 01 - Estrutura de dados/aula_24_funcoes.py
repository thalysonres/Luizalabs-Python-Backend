def exibir_mensagem():
    print("Olá! Esta é uma mensagem exibida por uma função.")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2("Thalyson")
exibir_mensagem_3()
exibir_mensagem_3(nome="Thalyson")


def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor


def func_3():
    print("Início da func_3")
    return None #Padrão de retorno se não especificado


print(calcular_total([10, 20, 30])) #60
print(retorna_antecessor_e_sucessor(10)) #(9, 11)
print(func_3()) #None




def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados 
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
 

def exibir_poema(data_extenso, *args, **kwargs):  #args: tupla; kwargs: dicionário
                            #, *lista, **dicionario
     texto = "\n".join(args)
    #texto = "\n".join(lista)
     meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    #meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
     mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
     print(mensagem)

exibir_poema(
    "Sexta-feira, 26 de agosto de 2022",
    "Zen of Python",
    "Beautiul is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    autor="Tim Peters",
    ano=1999
)


def funcao(*args, **kwargs):
 print(funcao("python",2022,curso="dio"))


funcao()