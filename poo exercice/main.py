'''
if __name__ == '__main__':
    #exerxcice 1
    #1
    print("marouane")
    #2
    Prenome = "Bouglace"
    print("mon Prenome est :", Prenome)
    #3
    age = 18
    print("mon age est :", age)
    #4
    parite = int(input("Entrez le nombre :"))
    if parite % 2 == 0:
        print("le nombre", parite, "est paire !")
    else:
        print("le nombre", parite, "est impaire !")
        #5
    mul = int(input("Entrez un nombre :"))
    for i in range(0, 11):
        print(i * mul)
    nbr1 = int(input("Entrez le 1er numero :"))
    nbr2 = int(input("Entrez le 2er numero :"))
    if nbr1 != 0:
        solution = -nbr2 / nbr1
        print("la solution de votre eq est: ", solution)
        #6
    nbr1 = int(input("Entrez le 1er numero :"))
    nbr2 = int(input("Entrez le 2er numero :"))
    nbr3 = int(input("Entrez le 3er numero :"))
    if nbr1 == 0:
        solution = -nbr3 / nbr2
        print("la solution de l'eq est: ", solution)
    else:
        discri = (nbr2 ** 2) - (4 * nbr1 * nbr3)
        x1 = -nbr2 - (discri ** 1 / 2) / (2 * nbr1)
        x2 = -nbr2 + (discri ** 1 / 2) / (2 * nbr1)
        print("les solutions de les eq est: x1 :", x1, "x2 :", x2)
        print()  # Séparation entre les deux boucles
    #exercice 2
        #1
    for i in range(1, 11):
        print(i)
        #2
    for i in range(1, 11):
        res = 10
        print(10 ,"*",i ,"=", res * i)
        #3
    for i in range(10, -1, -1):
        print(i)
    print("Démarrage !")
        #4
    for i in range(0, 15, 3):
        print(i)
        #5
    for i in range(1, 11):
        if i == 5:
            break
        print(i)
        #6
    for i in range(1, 11):
        if i ==5:
            continue
        print(i)
        #7
    # 1er cas
    a=0
    b=10
    for i in range(a, b):
        if a<b:
            print(i)
    for i in range(10, -1 , -1):
        if i % 2 == 1:
            print(i)
    # 2eme cas
    # Première boucle : Incrémente et affiche a tant que a < b
    a = 0
    b = 10

    while a < b:
        print(f"a = {a}")
        a += 1

    print()  # Séparation entre les deux boucles

    # Deuxième boucle : Décrémente b et affiche b si impaire, boucle tant que b != 0
    while b != 0:
        b -= 1
        if b % 2 != 0:  # Vérifie si b est impair
            print(f"b = {b}")
    print()  # Séparation entre les deux boucles
    # exercice 3
    temp=int(input(" Entrez la temperature de l'eau :"))
    if temp<= 0:
        print("c'est de la glace")
    elif temp < 100:
        print("c'est du liquide")
    else:
        print("c'est de la vapeur")
    print()  # Séparation'''
    # exercice 4
pi = 3.14
rayon=int(input("Entrez la rayon du sphere :"))
volume=4/3*(pi*rayon*3)
print("la volume du sphere est :",volume," ")

 exercice 5
#1
for i in range(9,0,-1):
    print(f"{i} {'*' * i}")
     #2
for i in range(5):  # 5 lignes
    for j in range(5):  # 5 colonnes
        print('*', end=' ')
    print()  # Retour à la ligne après chaque ligne
     #3
for i in range(9, 0, -1):
        print(f"{i} {'*' * (i + (i - 1))}")
    print()  # Séparation
    # exercice 6
     #1
    table = ["AAA", "BBB", "CCC"]
    for y in table:
        print(y)
    print()  # Séparation
     #2
    for x in range(0, 6, 2):
        x = x + 3
        print(x)
    print()  # Séparation
     #3

    print()  # Séparation
    # exercice 8
    table = ["Ananas", "Apple", "Kiwi", "Strawberry"]
    print("--------- Display items ---------")
    for item in table:
        print(item)
    print("\n--------- Add item ---------")
    table.append("banana")
    print("apres l'ajoute de Banane",table)

    print("\n-----------Remove item--------------")
    table.pop()
    print("apres supprimer le dernier element",table)

    print("------------Display the first item-------------")
    print("afficher le 1er element de la liste",table[0])

    print("------------Remove second item-------------")
    table.pop(1)
    print("apres supprimer le 2eme element de la liste:",table)
    print()  # Séparation
    # exercice 8
    table = ["France", "Espagne", "Maroc"]

    print("--------- Display items ---------")
    # 1. Afficher les éléments de la liste
    for item in table:
        print(item)

    print("\n--------- Add item ---------")
    # 2. Ajouter l'élément "USA" à cette liste
    table.append("USA")
    print("Liste après ajout de 'USA':", table)

    print("\n--------- Remove item ---------")
    # 3. Supprimer le dernier élément de la liste
    table.pop()
    print("Liste après supprimer le dernier élément:", table)

    print("\n--------- Display the first item ---------")
    # 4. Afficher le premier élément de la liste
    print("Premier élément de la liste:", table[0])

    print("\n--------- Remove second item ---------")
    # 5. Supprimer le 2ème élément de la liste
    table.pop(1)
    print("Liste après suppression du 2ème élément:", table)
'''