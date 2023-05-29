# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"


# Le jeu commence ici
label start:

    # Affiche les onglets
    show screen tabs_interface
    # Affiche la barre de relation quand nécessaire
    show screen relation_bar

    scene bg lycee exterieur

    # Utiliser $ show_character("Armin") permet d'afficher la barre de relation en même temps
    $ show_character("Armin")
    
    menu:
        "Bonjour"
        "Salut !":
            jump armin_content

        "(Bousculer Armin)":
            jump armin_neutre
    
    label armin_content:
        $ update_relation(+10)
        menu:
            "Comment vas-tu ?"
            "Vous savez, je ne crois pas qu'il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd'hui avec vous, je dirais que c'est d'abord des rencontres":
                $ update_relation(-50)
            "Ça va":
                pass
        jump suite
        

    label armin_neutre:
        $ update_relation(-10)
        menu:
            "Hein"
            "(Partir en riant)":
                $ update_relation(-10)
            "(Partir comme si de rien n'était)":
                pass
        jump suite

label suite:
    
    menu:
        "D'accord, c'est super"
        "...":
            pass

    $ hide_character()

    menu:
        "(Fin de la démo)":
            pass
