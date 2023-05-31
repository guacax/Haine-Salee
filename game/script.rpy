# Vous pouvez placer le script de votre jeu dans ce fichier.

define current_chapter = 1

# Le jeu commence ici
label start:

    show screen tabs_interface
    show screen relation_bar

    $ jump("school_courtyard")
