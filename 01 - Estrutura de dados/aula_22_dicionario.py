#Dicionário

pessoa_01 = {"nome": "Thalyson", "idade": 31, "altura": 1.84} #Passar dados imutáveis

pessoa = dict(nome="Thalyson", idade=31, altura=1.84) #mesma declaração

pessoa["telefone"] = "99999-9999"   # {"nome": "Thalyson", "idade": 31, "altura": 1.84, "telefone": "99999-9999"}

print(pessoa)


#Acessar os dados

dados = {"nome": "Thalyson", "idade": 31, "altura": 1.84, "telefone": "99999-9999"}

dados["nome"]  # Thalyson
dados["idade"] # 31 
dados["altura"] # 1.84
dados["telefone"] # 99999-9999

dados["nome"] = "Maria" #Alterar o valor da chave nome
dados["idade"] = 25    #Alterar o valor da chave idade

print(dados) # {'nome': 'Maria', 'idade': 25, 'altura': 1.84, 'telefone': '99999-9999'}


#Dicionário aninhados // chave para o valor deve ser um objeto imutável como Strings e números
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "idade": 31, "telefone": "99999-9999"},
    "maria@gmail.com": {"nome": "Maria", "idade": 25, "telefone": "99999-9991"},
    "joao@gmail.com": {"nome": "João", "idade": 28, "telefone": "99999-9992", "extra": { "a": 1,}}
}

contatos["thalyson@gmail.com"]["idade"] # 31
contatos["joao@gmail.com"]["nome"]  # João

telefone = contatos["thalyson@gmail.com"]["telefone"] #99999-9999
print(telefone)

extra = contatos["joao@gmail.com"]["extra"]["a"]  # 1 
print(extra)


#Iterar sobre dicionários
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():  #mesmo resultado do de cima porém mais legível
    print(chave, valor) 

