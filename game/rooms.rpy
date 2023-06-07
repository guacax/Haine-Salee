define current_room = None

init python :

    class MoveButton :
        '''Bouton de déplacement d'une salle à une autre'''

        def __init__(self, position:tuple, location:str):
            '''Constructeur
                Arguments:
                    position (tuple) -- position du bouton à l'écran
                    location (string) -- salle où mène ce bouton
            '''
            self.position = position
            self.location = location
            self.button = ImageButton("gui/button/move_idle.png", "gui/button/move_hover.png",
                xpos=self.position[0], ypos=self.position[1],
                focus_mask=True,
                clicked=self.on_click)
        
        def on_click(self) :
            renpy.hide_screen("room_moves")
            jump(self.location)
        

    def show_room(room:str) :
        '''Affiche le background de la salle'''
        global current_room
        renpy.show("bg "+room)
        current_room = room
    
    def hide_room() :
        '''Cache le background de la salle'''
        global current_room
        renpy.hide("bg")
        current_room = None

    '''
    move_buttons
        Keys : Nom de salle
        Values :
            tuple : position du bouton
            string : salle de destination
            integer : chapitre à partir duquel la salle est accessible
    '''
    move_buttons = {
        "school_courtyard" : [
            ((1000,900),"school_main_hallway", 1)
        ],
        "school_main_hallway" : [
            ((600,900),"school_courtyard", 1)
        ]
    }
    def get_move_buttons() :
        '''Récupère les boutons de déplacement de la salle courante'''
        global current_chapter
        global current_room
        buttons = []
        if current_room in move_buttons.keys() :
            for d in move_buttons[current_room] :
                if d[2] <= current_chapter :
                    buttons.append(MoveButton(d[0], d[1]))
        return buttons
    
    def jump(room:str) :
        '''Saute vers le label de la salle room du chapitre courant'''
        global current_chapter
        renpy.jump("chapter"+str(current_chapter)+"_"+room)

    
screen room_moves :
    for b in get_move_buttons() :
        add b.button

label room_end :
    $ hide_character()
    show screen room_moves
    pause
    jump room_end