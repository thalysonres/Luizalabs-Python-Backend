#Métodos da classe dict

#Método {}.clear  // Limpa o dicionário
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "idade": 31, "telefone": "99999-9999"},
    "maria@gmail.com": {"nome": "Maria", "idade": 25, "telefone": "99999-9991"},
    "joao@gmail.com": {"nome": "João", "idade": 28, "telefone": "99999-9992"}
}

contatos.clear()

print(contatos)  #Saída: {}



#Método {}.copy // Retorna uma cópia rasa do dicionário
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

copia = contatos.copy()
copia["thalyson@gmail.com"] = {"nome": "Tay"}

print(contatos["thalyson@gmail.com"]) #Saída: {'nome': 'Thalyson', 'telefone': '99999-9999'}
print(copia["thalyson@gmail.com"])   #Saída: {'nome': 'Tay'}



#Método {}.fromkeys // Cria um novo dicionário com chaves de um iterável e valores padrão
dict.fromkeys(["nome", "idade", "telefone"]) #{'nome': None, 'idade': None, 'telefone': None}  // cria chaves com valor None

dict.fromkeys(["nome", "idade", "telefone"], "vazio")
#{'nome': 'vazio', 'idade': 'vazio', 'telefone': 'vazio'} // cria chaves com valor padrão



#Método {}.get // Retorna o valor da chave especificada
contatos = {
  "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

# print(contatos["chave"]) #Gera um erro KeyError
print(contatos.get("chave")) #Saída: None
print(contatos.get("chave", "Não encontrado")) #Saída: Não encontrado
print(contatos.get("chave", {})) #Saída: {}
print(contatos.get("thalyson@gmail.com", {})) #Saída: {'nome': 'Thalyson', 'telefone': '99999-9999'}



#Método {}.items // Retorna uma visão dos pares chave-valor do dicionário // retorna uma lista de tuplas
contatos = {
  "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

print(contatos.items()) #Saída: dict_items([("thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"})])



#Método {}.keys // Retorna uma visão das chaves do dicionário // retorna uma lista de chaves
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

print(contatos.keys()) #Saída: dict_keys(["thalyson@gmail.com"])


novo_dicionario = {"a": 100, 1: "teste", "b": "python"}
print(novo_dicionario.keys()) #Saída: dict_keys(['a', 1, 'b'])



#Método {}.pop // Remove a chave especificada e retorna o valor correspondente
contatos_03 = {
    "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

resultado = contatos_03.pop("thalyson@gmail.com ", {}) # Aqui ele removeu os itens do dicionário porque encontrou a chave
print(resultado) # {'nome': 'Thalyson', 'telefone': '99999-9999'}

resultado = contatos_03.pop("thalyson@gmail.com", {}) # Como a chave não existe mais, ele retorna o valor padrão repassado
print(resultado) # {} 



#Método {}.popitem // Remove e retorna um par chave-valor aleatório do dicionário
contatos_2 = {
    "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

print(contatos_2.popitem()) # Remove o item do dicionário
# print(contatos_2.popitem()) # KeyError



#Método {}.setdefault // Retorna o valor da chave especificada. Se a chave não existir, insere a chave com o valor padrão
contato = {
    "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

contato.setdefault("nome", "Giovanna") # Como a chave "nome" não existe, ele cria a chave com o valor padrão
print(contato) #Saída: {'nome': 'Thalyson', 'idade': 31}, 'nome': 'Giovanna'}

print(contato.setdefault("idade", 31)) #31 // Como a chave "idade" não existe, ele cria a chave com o valor padrão
print(contato) #{'thalyson@gmail.com': {'nome': 'Thalyson', 'telefone': '99999-9999'}, 'nome': 'Giovanna', 'idade': 31}



#Método {}.update // Atualiza o dicionário com os pares chave-valor de outro dicionário ou iterável de pares chave-valor
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "telefone": "99999-9999"}
}

contatos.update({"thalyson@gmail.com": {"nome": "Tay"}}) # Atualiza o valor da chave existente
print(contatos) #Saída: {'thalyson@gmail.com': {'nome': 'Tay'}}

contatos.update({"maria@gmail.com": {"nome": "Maria", "telefone": "99999-9991"},}) # chaves que não existem são adicionadas
print(contatos) #Saída: {'thalyson@gmail.com': {'nome': 'Tay'}, 'maria@gmail.com': {'nome': 'Maria', 'telefone': '99999-9991'}}



#Métodos {}.values // Retorna uma visão dos valores do dicionário // retorna uma lista de valores, sem as chaves
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "idade": 31, "telefone": "99999-9999"},
    "maria@gmail.com": {"nome": "Maria", "idade": 25, "telefone": "99999-9991"},
    "joao@gmail.com": {"nome": "João", "idade": 28, "telefone": "99999-9992"}
}

print(contatos.values()) 
#Saída: dict_values([{'nome': 'Thalyson', 'idade': 31, 'telefone': '99999-9999'}, 
# {'nome': 'Maria', 'idade': 25, 'telefone': '99999-9991'}, 
# {'nome': 'João', 'idade': 28, 'telefone': '99999-9992'}])



#Método {}.in // Verifica se uma chave existe no dicionário
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "idade": 31, "telefone": "99999-9999"},
    "maria@gmail.com": {"nome": "Maria", "idade": 25, "telefone": "99999-9991"},
    "joao@gmail.com": {"nome": "João", "idade": 28, "telefone": "99999-9992"}
}

resultado = "thalyson@gmail.com" in contatos # True
print(resultado)

resultado = "sabrina@gmail.com" in contatos # False
print(resultado)

resultado = "idade" in contatos["joao@gmail.com"] # True
print(resultado)

resultado = "altura" in contatos["thalyson@gmail.com"] # False
print(resultado)   

resultado = "telefone" in contatos["maria@gmail.com"] # True
print(resultado)



#Método {}.del // Remove a chave especificada do dicionário
contatos = {
    "thalyson@gmail.com": {"nome": "Thalyson", "idade": 31, "telefone": "99999-9999"},
    "maria@gmail.com": {"nome": "Maria", "idade": 25, "telefone": "99999-9991"},
    "joao@gmail.com": {"nome": "João", "idade": 28, "telefone": "99999-9992"}
}

del contatos["maria@gmail.com"]["telefone"] # Remove a chave "telefone" do dicionário da Maria
del contatos["joao@gmail.com"] # Remove o dicionário do João

print(contatos) #{'thalyson@gmail.com': {'nome': 'Thalyson', 'idade': 31, 'telefone': '99999-9999'}, 'maria@gmail.com': {'nome': 'Maria', 'idade': 25}}