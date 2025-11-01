curso = "pYtHon"

print(curso.upper()) # "python"
print(curso.lower()) # "PYTHON"
print(curso.title()) # "Python"


curso_1 = "     Python  "

print(curso_1.strip() + ".") # "Python"
print(curso_1.lstrip()+ ".") # "Python  "
print(curso_1.rstrip()+ ".") # "     Python"


curso_2 = "Java"

print("###" + curso_2 + "###") # "###Python###"  
print(curso_2.center(12, "#")) # "###Python###"  // mesmo resultado, porém mais fácil

print(curso_2.center(12)) # "   Python   "

print(".".join(curso_2)) # "P.y.t.h.o.n"   usado em qualquer iterável
print("-".join(curso_2)) # "P-y-t-h-o-n"  

for letra in curso_2:   #mesmo resultado com FOR
    print(letra, end="-")
