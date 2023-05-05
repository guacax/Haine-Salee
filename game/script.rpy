# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"


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

    show armin
    $ show_love(characters_love["armin"])
    
    menu:
        "Bonjour"
        "Salut !":
            jump armin_content

        "(Bousculer Armin)":
            jump armin_neutre
    
    label armin_content:
        $ update_love("armin", characters_love["armin"], 0)
        menu:
            "Comment vas-tu ?"
            "Vous savez, je ne crois pas qu'il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd'hui avec vous, je dirais que c'est d'abord des rencontres":
                pass
            "Ça va":
                pass
        jump suite
        

    label armin_neutre:
        $ update_love("armin", characters_love["armin"], -10)
        menu:
            "Hein"
            "(Partir en riant)":
                pass
            "(Partir comme si de rien n'était)":
                pass
        jump suite

label suite:
    
    hide armin
    $ hide_love(characters_love["armin"])

    menu:
        "(Fin de la démo)":
            pass

        


label end_and_reset:
    python:
        for char in characters_love:
            characters_love[char] = 50  # reset tout le monde à 50
    return

