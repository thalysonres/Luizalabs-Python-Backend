frutas = ['laranja', 'maca', 'uva']
print(frutas)
print(frutas[0]) # laranja
print(frutas[2]) # uva  
print(frutas[-2]) # maca


frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["ferrari", "f50", 4200000, 2020, 2900, "São Paulo", True]
print(carro)


# Lista com lista // lista aninhada // matriz
matriz = [
    [1, "a", 2],
    ["b", 3, 4], 
    [6, 5, "c"]  
]

print(matriz[0])     # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"


# Fatiamento de listas (slicing) // lista começa no índice zero, o último índice não é incluído
lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]



# Iterar lista
carros = ["gol", "uno", "palio"]

for carro in carros:
    print(carro)



#Função enumerate
for indice, carro in enumerate(carros):
    print(indice, carro)



#Fitrar lista com FOR
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)


#Filtrar lista COM LIST COMPREHENSION
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)


#Modificando valores da lista com FOR
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)


#Modificando valores da lista COM LIST COMPREHENSION
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)