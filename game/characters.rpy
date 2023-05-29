define current_character = None

# Pour chaque personnage avec lequel il y a des points de relation :
define armin_relation = 0 # Nécessaire pour conserver les points de relation avec les sauvegardes
image Armin = "characters/Armin.png"

define mao_relation = 0
image Mao = "characters/Mao.png"


init python :

    # Affiche l'image du personnage et sa barre de relation 
    def show_character(character:str, attribute:str="", **args) :
        character = character.lower()
        global current_character
        current_character = character
        image_name = character
        if attribute != "" :
            image_name += " " + attribute
        renpy.show(image_name, tag="character")

    def hide_character() :
        global current_character
        renpy.hide("character")
        current_character = None

    def has_relation(character:str=None) :
        if character==None : character=current_character
        return character.lower() in ["armin", "mao"]

    def get_relation(character:str=None) :
        if character==None : character=current_character
        character = character.lower()
        if character=="armin" :
            return armin_relation
        elif character=="mao" :
            return mao_relation
        return None

    def update_relation(points:int) :
        if current_character=="armin" :
            global armin_relation
            armin_relation += points
            armin_relation = max(-100, min(100, armin_relation))
        elif current_character=="mao" :
            global mao_relation
            mao_relation += points
            mao_relation = max(-100, min(100, mao_relation))
        return None
        


screen relation_bar :
    if current_character != None :
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