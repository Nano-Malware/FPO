# Fonction pour calculer la somme
def somme_harmonique(n):
    somme = 0
    for i in range(1, n + 1):
        somme += 1 / i
    return somme

# Programme principal
n = int(input("Entrez un nombre entier n : "))
resultat = somme_harmonique(n)
print(f"La somme S est : {resultat}")
