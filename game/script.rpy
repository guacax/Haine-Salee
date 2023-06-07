init -1 python :
    
    class IconButton :
        '''
            Classe abstraite d'un bouton avec un fond qui change lors du survol
        '''
        def __init__(self, icon:str) :
            self.icon = icon
            self.is_selected = False
            self.button = Composite((200,200),
                (0,0), ImageButton("gui/button/background_selected.png" if self.is_selected else "gui/button/background_idle.png", 
                    "gui/button/background_hover.png",
                    focus_mask=None,
                    clicked=self.on_click),
                (0,0), Image("icons/"+icon+".png")
            )
        
        def on_click(self) :
            pass

        def selected(self, select:bool=True) :
            self.is_selected = select
            if select :
                self.button = Composite((200,200),
                    (0,0), ImageButton("gui/button/background_selected.png",
                        focus_mask=None,
                        clicked=self.on_click),
                    (0,0), Image("icons/"+self.icon+".png")
                )
            else :
                self.button = Composite((200,200),
                    (0,0), ImageButton("gui/button/background_idle.png", "gui/button/background_hover.png",
                        focus_mask=None,
                        clicked=self.on_click),
                    (0,0), Image("icons/"+self.icon+".png")
                )

define current_chapter = 1

# Le jeu commence ici
label start:

    call customization

    show screen tabs_interface
    show screen relation_bar

    $ jump("school_courtyard")
