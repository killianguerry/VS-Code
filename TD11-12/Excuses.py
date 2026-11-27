import random

# Listes des éléments composant une excuse
qui = [
    "Mon voisin",
    "Mon chat",
    "Ma soeur",
    "Mon petit frère",
    "Ma grand-mère",
    "Le chien du voisin",
    "Un extraterrestre",
    "Mon colocataire",
    "Le facteur",
    "Un pigeon",
]

action = [
    "a mangé",
    "a volé",
    "a perdu",
    "a cassé",
    "a caché",
    "a brûlé",
    "a jeté à la poubelle",
    "a vendu",
    "a renversé du café sur",
    "a kidnappé",
]

quoi = [
    "mon devoir",
    "mon ordinateur",
    "ma femme",
    "ma clé USB",
    "mes cahiers",
    "mon réveil",
    "mon vélo",
    "mon téléphone",
    "ma trousse",
    "mon cours de programmation",
]


def generer_excuse():
    """Construit une excuse aléatoire : qui + action + quoi."""
    return f"{random.choice(qui)} {random.choice(action)} {random.choice(quoi)} !"


if __name__ == "__main__":
    print("=== Générateur d'excuses ===")
    while True:
        print("\nExcuse :", generer_excuse())
        reponse = input("Une autre excuse ? (o/n) : ").strip().lower()
        if reponse != "o":
            print("Bonne chance avec le prof !")
            break
