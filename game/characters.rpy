define current_character = None

# Pour chaque personnage avec lequel il y a des points de relation :
define relation_armin = 0 # Nécessaire pour conserver les points de relation avec les sauvegardes
image Armin = "characters/Armin.png"

define relation_nael = 0
image Nael = "characters/Nael.png"

define relation_cassandre = 0
image Cassandre = "characters/Cassandre.png"

image Mao = "characters/Mao.png"


init python :

    def show_character(character:str, attribute:str="", **args) :
        '''Affiche l'image du personnage et sa barre de relation (si elle existe)'''
        character = character.lower()
        global current_character
        current_character = character
        image_name = character
        if attribute != "" :
            image_name += " " + attribute
        renpy.show(image_name, tag="character", **args)

    def hide_character() :
        '''Cache l'image du personnage et sa barre de relation'''
        global current_character
        renpy.hide("character")
        current_character = None

    def has_relation(character:str=None):
        '''Retourne vrai si character (ou le personnage courant) a une barre de relation'''
        if character==None : character=current_character
        return character.lower() in ["armin","nael","cassandre"]

    def get_relation(character:str=None) :
        '''Retourne la valeur de la relation avec character (ou le personnage courant)'''
        if character==None : character=current_character
        character = character.lower()
        if character=="armin" :
            return relation_armin
        elif character=="nael" :
            return relation_nael
        elif character=="cassandre" :
            return relation_cassandre
        return None

    def update_relation(points:int) :
        '''Met à jour la relation avec le personnage actuellement à l'écran'''
        if current_character=="armin" :
            global relation_armin
            relation_armin += points
            relation_armin = max(-100, min(100, relation_armin))
        elif current_character=="nael" :
            global relation_nael
            relation_nael += points
            relation_nael = max(-100, min(100, relation_nael))
        elif current_character=="cassandre" :
            global relation_cassandre
            relation_cassandre += points
            relation_cassandre = max(-100, min(100, relation_cassandre))
        return None
        


screen relation_bar :
    if current_character != None and has_relation():
        frame :
            xysize (87,388)
            xalign 0.0 yalign 0.5
            pos (0.9,0.5)
            padding (0,0)
            background None

            bar :
                bar_vertical True
                value AnimatedValue(get_relation(current_character)+100, 200, delay=1.0)
                left_bar "gui/bar/relation_bar_empty.png"
                right_bar "gui/bar/relation_bar_full.png"
                xysize (87,388)
                align (0.5,0.5)
                top_gutter 0
                bottom_gutter 70
            text str(get_relation(current_character)) :
                align (0.5,0.925)
                size 20
                color "#C92667"