#Método [].append Adicionar itens ao final da lista
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)  # [1, 'Python', [40, 30, 20]]  



#Método [].clear Remover todos os itens da lista
lista = [1, "Python", [40, 30, 20]]
print(lista)  # [1, 'Python', [40, 30, 20]]

lista.clear()
print(lista)  # []



#Método [].copy Retorna uma cópia rasa da lista
lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista) # [1, 'Python', [40, 30, 20]]
print(id(l2), id(lista))  # IDs diferentes

l2[0] = 2
print(lista)  # [1, 'Python', [40, 30, 20]]
print(l2)     # [2, 'Python', [40, 30, 20]]



#Método [].count Retorna o número de ocorrências de um valor na lista
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))     # 2
print(cores.count("verde"))    # 1



#Método [].extend Adiciona os itens de uma lista (ou qualquer iterável) ao final da lista
linguagens = ["Python", "JS", "C"]
print(linguagens)  # ['Python', 'JS', 'C']

linguagens.extend(["Java", "PHP", "C"])
print(linguagens)  # ['Python', 'JS', 'C', 'Java', 'PHP', 'C'] 



#Método [].index Retorna o índice do primeiro elemento com o valor especificado
linguagens = ["Python", "Java", "C", "Java", "C#"]

print(linguagens.index("Python"))  # 0
print(linguagens.index("Java"))    # 1



#Método [].pop Remove o último item da lista e o retorna
linguagens = ["Python", "JS", "C", "Java", "C#"]

print(linguagens.pop())  # C#
print(linguagens.pop())  # Java
print(linguagens.pop())  # C
print(linguagens.pop(0))  # Python
print(linguagens)



#Método [].remove Remove o primeiro item da lista com o valor especificado
linguagens = ["Python", "JS", "C", "Java", "C"]

linguagens.remove("C")
print(linguagens) # ['Python', 'JS', 'Java', 'C']



#Método [].reverse Inverte os itens da lista
linguagens = ["Python", "JS", "C", "Java", "C#"]

linguagens.reverse()
print(linguagens)  # ['C#', 'Java', 'C', 'JS', 'Python']



#Método [].sort Ordena os itens da lista
linguagens = ["Python", "JS", "C", "Java", "C#"]
linguagens.sort()
print(linguagens)  # ['C', 'C#', 'JS', 'Java', 'Python']

linguagens = ["Python", "JS", "C", "Java", "C#"]
linguagens.sort(reverse=True)
print(linguagens) # ['Java', 'Python', 'JS', 'C#', 'C']

linguagens = ["Python", "JS", "C", "Java", "C#"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)  # ['C', 'JS', 'C#', 'Java', 'Python']

linguagens = ["Python", "JS", "C", "Java", "C#"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)  # ['Python', 'Java', 'JS', 'C#', 'C'] 



#Método [].len Retorna o tamanho da lista  // função buit-in len()
linguagens = ["Python", "JS", "C", "Java", "C#"]
print(len(linguagens))  # 5


#Método [].sorted Retorna uma nova lista ordenada // função buit-in sorted() // mesma sintaxe do sort() mas é uma função
linguagens = ["Python", "JS", "C", "Java", "C#"]

print(sorted(linguagens, key=lambda x: len(x)))  # ['C', 'C#', 'JS', 'Java', 'Python']
print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ['Python', 'Java', 'JS', 'C#', 'C']
print(sorted(linguagens))  # ['C', 'C#', 'JS', 'Java', 'Python']