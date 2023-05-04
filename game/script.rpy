# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")
transform center_right:
    pos (0.9,0.5)
init python:
    characters_love = {"armin": 50}
    def show_love(lovelevel):
        renpy.show(f"love {lovelevel}", [center_right])

    def hide_love(lovelevel):
        renpy.hide(f"love {lovelevel}")

    def update_love(character, curr_love, change):
        hide_love(characters_love[character])
        characters_love[character] += change
        show_love(characters_love[character])

# Le jeu commence ici
label start:

    # Affiche les onglets (je n'arrive pas à les charger autre part qu'ici)
    show screen tabs_interface

    scene bg lycee exterieur

    "Début du jeu"

    show armin
    $ show_love(characters_love["armin"])
    

    e "Bonjour"

    "Hello."

    menu:
        "Répondre gentiement":
            jump armin_content

        "Répondre pas gentiement":
            jump armin_neutre
    
    label armin_content:
        $ update_love("armin", characters_love["armin"], -10)
        "Sympa"
        jump suite
        

    label armin_neutre:
        $ update_love("armin", characters_love["armin"], 0)
        "Hein"
        jump suite

label suite:
    "cool"

        


label end_and_reset:
    python:
        for char in characters_love:
            characters_love[char] = 50  # reset tout le monde à 50
    return

