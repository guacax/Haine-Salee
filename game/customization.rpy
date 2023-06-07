init python :
    import random

    # Boutons des éléments de personnalisation
    class CustomizationButton(IconButton) :
        def __init__(self, icon, value, part) :
            super().__init__("customization/"+icon)
            self.value = value
            self.part = part

        def on_click(self) :
            if self.part == "hair" :
                global hair
                hair = self.value
            elif self.part == "skin" :
                global skin_color
                skin_color = self.value
            elif self.part == "eyes" :
                global eyes
                eyes = self.value
            elif self.part == "nose" :
                global nose
                nose = self.value
            elif self.part == "mouth" :
                global mouth
                mouth = self.value
            elif self.part == "shirt" :
                global shirt
                shirt = self.value
            renpy.restart_interaction() 
    
    # Boutons des catégories de personnalisation
    class CustomizationSuperButton(IconButton) :
        def __init__(self, icon, elements) :
            super().__init__("customization/"+icon)
            self.elements = elements

        def on_click(self) :
            global customization_buttons
            customization_buttons = [CustomizationButton(e[0], e[1], e[2]) for e in self.elements]
            renpy.restart_interaction() 
    
    # Boutons des signes astrologiques
    class AstroButton(IconButton) :
        def __init__(self, sign) :
            super().__init__("astro/"+sign)
            self.sign = sign
        def on_click(self) :
            if profil_astro != "" :
                customization_astrobutton[profil_astro].selected(False)
                if profil_astro == self.sign :
                    renpy.restart_interaction()
                    return
            global profil_astro
            profil_astro = self.sign
            self.selected(True)
            renpy.restart_interaction()

    # Validation de la personnalisation
    def customization_valid():
        if profil_name == '' :
            global profil_name
            profil_name = 'Salette'
        if profil_astro == '' :
            global profil_astro
            profil_astro = random.choice(list(customization_astrobutton.keys()))
        renpy.jump("customization_end")

# Nom
define profil_name = ''
define customization_name = VariableInputValue('profil_name')

#region Image de profil de Salette
define skin_color = "1"
define hair = "1"
define eyes = "1"
define nose = "1"
define mouth = "1"
define shirt = "1"

define profil_picture = Composite(
    (846, 1028),
    (0,0), "salette/back_hair_[hair].png",
    (0,0), "salette/skin_[skin_color].png",
    (0,0), "salette/shirt_[shirt].png",
    (0,0), "salette/eyes_[eyes].png",
    (0,0), "salette/mouth_[mouth].png",
    (0,0), ConditionSwitch(
        "nose == 'empty'", Null(),
        "True", "salette/nose_[nose].png"),
    (0,0), "salette/front_hair_[hair].png"
)

# Boutons de customisation
define customization_super_buttons = [
    CustomizationSuperButton("skin",[
        ("skin_1", "1", "skin"),
        ("skin_2", "2", "skin"),
        ("skin_3", "3", "skin")
    ]),
    CustomizationSuperButton("hair_1",[
        ("hair_1", "1", "hair"),
        ("hair_2", "2", "hair"),
        ("hair_3", "3", "hair")
    ]),
    CustomizationSuperButton("eyes_1",[
        ("eyes_1", "1", "eyes"),
        ("eyes_2", "2", "eyes")
    ]),
    CustomizationSuperButton("nose_1",[
        ("empty", "empty", "nose"),
        ("nose_1", "1", "nose"),
        ("nose_2", "2", "nose")
    ]),
    CustomizationSuperButton("mouth_2",[
        ("mouth_1", "1", "mouth"),
        ("mouth_2", "2", "mouth")
    ]),
    CustomizationSuperButton("shirt",[
        ("shirt_1", "1", "shirt"),
        ("shirt_2", "2", "shirt")
    ]),
]

define customization_buttons = []
#endregion

# Signe astro
define profil_astro = ""
define customization_astrobutton = {
    "Aries" : AstroButton("Aries"),
    "Taurus" : AstroButton("Taurus"),
    "Gemini" : AstroButton("Gemini"),
    "Cancer" : AstroButton("Cancer"),
    "Leo" : AstroButton("Leo"),
    "Virgo" : AstroButton("Virgo"),
    "Libra" : AstroButton("Libra"),
    "Scorpio" : AstroButton("Scorpio"),
    "Sagittarius" : AstroButton("Sagittarius"),
    "Capricorn" : AstroButton("Capricorn"),
    "Aquarius" : AstroButton("Aquarius"),
    "Pisces" : AstroButton("Pisces"),
}

screen customization :
    # Nom
    frame :
        xalign 0.5
        ypos 0.1
        xsize 500
        ysize 80

        text "Nom :"
        input value customization_name xpos 120

    # Pronoms (il faudrait utiliser pronoun_dropdown de pronountool.rpy)
    frame:
        pos (0.7,0.1)
        textbutton selectedpronouns+" V" action Show("pronoun_dropdown_menu",None, (0.7, 0.194))

    # Image de profil
    add profil_picture xpos 0.05 yalign 0.5 zoom 0.5

    # Catégories de l'image
    for i,b in enumerate(customization_super_buttons) :
        add b.button xysize (100,100) xpos (750+i*120) ypos 0.2

    # Éléménts de l'image
    for i,b in enumerate(customization_buttons) :
        add b.button xysize (75,75) xpos (600+i*100) ypos 0.3

    # Astro
    for i,b in enumerate(customization_astrobutton.values()) :
        add b.button xysize (100,100) xpos (200 + i*110) ypos 0.8

    # Validation
    textbutton "Valider":
            pos (0.8,0.8)
            action customization_valid


# Appeler ici pour ouvrir l'interface de personnalisation
label customization :
    $ customization_super_buttons[0].on_click()
    $ _return = None

    show bg customization
    show screen customization
    while True :
        pause

label customization_end :
    hide screen customization
    return 
