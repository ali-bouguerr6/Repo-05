import random

# Initial joke collection
jokes = [
    "Pourquoi les développeurs préfèrent le mode sombre ? Parce que la lumière attire les bugs !",
    "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème hardware.",
    "Pourquoi les développeurs Java portent des lunettes ? Parce qu'ils ne peuvent pas C# !"
]

dad_jokes = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière du bateau et jamais en avant ? Parce que sinon ils tombent dans le bateau.",
    "J’ai un ami électricien… mais il ne sait pas faire la lumière sur ses problèmes.",
    "Tu connais la blague du biscuit ? … Non ? Tant mieux, elle est trop crumble.",
    "Pourquoi les squelettes ne se battent-ils jamais entre eux ? Parce qu’ils n’ont pas les tripes.",
    "J’ai voulu écrire une blague sur le temps… mais elle n’est pas encore au point.",
    "Pourquoi les canards ont-ils autant de plumes ? Pour couvrir leurs fesses.",
    "J’ai acheté un chien d’occasion… Il était déjà assis.",
    "Tu connais la blague du lit ? Elle est faite pour dormir debout.",
    "Pourquoi l’ordinateur a-t-il froid ? Parce qu’il est toujours dans Windows.",
    "J’ai une blague sur les ascenseurs… mais elle a ses hauts et ses bas."
]


def print_random_joke():
    """Print a random joke from the collection."""
    all_jokes = jokes + dad_jokes
    joke = random.choice(all_jokes)
    print(f"😂 {joke}")

if __name__ == "__main__":
    print("Bienvenue au Générateur de Blagues !")
    print_random_joke()