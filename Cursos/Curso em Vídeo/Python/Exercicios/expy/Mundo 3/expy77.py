palavras = ("APRENDER",
    "PROGRAMAR",
    "LINGUAGEM",
    "PYTHON",
    "CURSO",
    "GRATIS",
    "ESTUDAR",
    "PRATICAR",
    "TRABALHAR",
    "MERCADO",
    "PROGRAMADOR",
    "FUTURO",
)

for i in palavras:
    print(f"\nNa palavra {i} temos as vogais ", end="")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end=" ")