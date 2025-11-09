#Tuplas é criada passando os valores separados por vírgula e entre parênteses

frutas = ("laranja", "pera", "uva",)  #Boa prática: vírgula no final
letras = tuple("python")
numeros = tuple([1, 2, 3, 4, 5])
pais = ("Brasil",) 

#Acessando elementos da tupla
frutas = ("laranja", "pera", "uva", "maca")
print(frutas[0])  #laranja
print(frutas[-1]) #maca


#Tuplas aninhadas
matriz = (
  (1, "a", 2),
  ("b", 3, 4),
  (6, 5, "c"),
)

print(matriz[0])    # (1, "a", 2)
print(matriz[0][0]) # 1
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # "c"


#Fatiamento de tuplas
tupla = ( "p", "y", "t", "h", "o", "n" )

print(tupla[2:])      # ('t', 'h', 'o', 'n')
print(tupla[:2])      # ('p', 'y')
print(tupla[1:4])     # ('y', 't', 'h')
print(tupla[0:3:2])  # ('p', 't')
print(tupla[:])       # ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1])    # ('n', 'o', 'h', 't', 'y', 'p')


#Iterando sobre tuplas
carros = ("gol", "uno", "palio")

for carro in carros:
    print(carro)


#Enumerate em tuplas
carros = ("gol", "uno", "palio")

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")  



#Métodos da classe tuple

#Método ().count
cores = ("verde", "amarelo", "azul", "branco", "verde")

cores.count("verde")  #2
cores.count("azul")   #1
cores.count("preto")  #0


#Método ().index
linguagens = ("python", "java", "c#", "python", "javascript")
linguagens.index("python")    #0
linguagens.index("python") #3


#Método ().len  
linguagens = ("python", "java", "c#", "python", "javascript")

len(linguagens)  #5