
nome = "Thalyson"
idade = 31
profissao = "Analista"
linguagem = "Python"

dados = {"nome": "Thalyson", "idade": 31, "profissao": "Analista", "linguagem": "Python"}

# Primeira forma, modelo style   %s string   %d inteiro   %f float
print("Olá, me chamdo %s. Eu tenho %d anos de idade, trabalho como %s e " \
"estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))



## Segunda forma, método format
print("Olá, me chamdo {}. Eu tenho {} anos de idade, trabalho como {} e " \
"estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamdo {2}. Eu tenho {3} anos de idade, trabalho como {1} e " \
"estou matriculado no curso de {0}. Nome {2}".format(linguagem, profissao, nome, idade))

print("Olá, me chamdo {name}. Eu tenho {age} anos de idade, trabalho como {profissao} e " \
"estou matriculado no curso de {linguagem}.".format(name=nome, age=idade, profissao=profissao, linguagem=linguagem))

print("Olá, me chamdo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e " \
"estou matriculado no curso de {linguagem}.".format(**dados))



### Terceira forma, f-string
print(f"Olá, me chamdo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} estou matriculado no curso de {linguagem}.")


### Formatar string com f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}")  # "Valor de PI: 3.14"
print(f"Valor de PI: {PI:5.3f}") # "Valor de PI:      3.141"