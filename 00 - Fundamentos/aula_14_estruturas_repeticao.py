# Receba um número do teclado e exiba os 2 números seguintes
a = int(input("Informe um número inteiro: "))
print(a)

a += 1
print(a)

a += 1
print(a)


# Estrutura repetição For
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end="")

print() #adiciona uma quebra de linha



# Estrutura repetição For/Else
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end="")
else:
    print() #adiciona uma quebra de linha
    print("Executado no final do laço")



#range(stop) -> range object
#range(start, stop, step) -> range object
list(range(4))

# Exemplo utilizando a função bulit-in iterável
for numero in range(0, 11):
    print(numero, end=" ")


# Exemplo utilizando a função bulit-in range
for numero_1 in range(0, 51, 5):
    print(numero_1, end=" ")


# Extrutura repetição While
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

else:
    print("Obrigado por usar nosso sistema bancário, até logo!")




#Extrura repetição Break
while 1 == 1: # Mesma coisa que True
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    print(numero)


while True : 
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue 
    
    print(numero)



for numero in range(100):

    if numero == 12:
        break # Parar o laço quando a condição é atendida
    
    print(numero, end=" ")


for numero in range(100):

    if numero % 2 == 0: #exibe apenas números impares
        continue #Pular o laço quando a condição é atendida
    
    print(numero, end=" ")
