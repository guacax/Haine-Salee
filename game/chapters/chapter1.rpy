define chapter1_progression = 0

label chapter1_school_courtyard :

    $ show_room("school_courtyard")

    if chapter1_progression == 0 :

        $ show_character("Armin")

        menu:
            "Bonjour"
            "Salut !":
                $ update_relation(+10)
                menu:
                    "Comment vas-tu ?"
                    "Vous savez, je ne crois pas qu'il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd'hui avec vous, je dirais que c'est d'abord des rencontres":
                        $ update_relation(-50)
                    "Ça va":
                        pass

            "(Bousculer Armin)":
                $ update_relation(-10)
                menu:
                    "Hein"
                    "(Partir en riant)":
                        $ update_relation(-10)
                    "(Partir comme si de rien n'était)":
                        pass
        
        menu:
            "D'accord, c'est super"
            "...":
                pass
    
        $ chapter1_progression = 1


    elif chapter1_progression == 2 :

        $ show_character("Cassandre")

        menu :
            "Je suis Cassandre, l'élève modèle du lycée (du moins j'essaie), je suis timide, maladroit et je me fais bully par les grosses brutes du lycée."

            "Cassandre, c'est super !" :
                $ update_relation(5)
            
            "(Bully Cassandre)" :
                $ update_relation(-10)
        
        menu :
            "Au revoir"
            "..." :
                pass
        
        $ chapter1_progression = 3
    

    jump room_end


label chapter1_school_main_hallway :

    $ show_room("school_main_hallway")

    if chapter1_progression == 1 :

        $ show_character("Nael")

        menu :
            "Hé, t'es nouvelle ici ? J'ai jamais vu ta tête traîner dans les parages. T'es perdue ou quoi ?"
            "Non, je suis nouvelle. J'essaie juste de trouver mon chemin.":
                $ update_relation(5)
            "Perdue ? Pas autant que toi dans une salle de classe, apparemment.":
                $ update_relation(-5)
        
        menu :
            "C'est super !"
            "..." :
                pass
        
        $ chapter1_progression = 2
    
    jump room_end