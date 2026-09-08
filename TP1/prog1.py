import fonctions as f

while True:
    a = int(input("Saisir le premier nombre : "))
    b = int(input("Saisir le deuxième nombre : "))

    res = f.puissance(a, b)
    print("Résultat :", res)
