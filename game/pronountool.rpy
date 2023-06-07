'''
    Permet d'accorder automatiquement en fonction des pronoms choisis par le joueur

    Il est possible d'utiliser les variables d'accords (voir dessous)
    ex : [elle] est sorti[e]

    Ou bien utiliser les balises {0}, {1} et {2}
    ex : jeune jeune {0}fille{/0}{1}garçon{/1}{2}enfant{/2}. 
'''

default pronounlist = [
    __("elle/elle"), # 0
    __("il/lui"), # 1
    __("iel/ellui"), # 2
    # __(), # 3
]

default pronoun = 0
default selectedpronouns = pronounlist[pronoun]

default ellelist = [
    __("elle"), # 0
    __("il"), # 1
    __("iel"), # 2
]

default elleindlist = [
    __("elle"), # 0
    __("lui"), # 1
    __("ellui"), # 2
]

default cellelist = [
    __("celle"), # 0
    __("celui"), # 1
    __("cellui"), # 2
]

default malist = [
    __("ma"), # 0
    __("mon"), # 1
    __("maon"), # 2
]

default talist = [
    __("ta"), # 0
    __("ton"), # 1
    __("taon"), # 2
]

default salist = [
    __("sa"), # 0
    __("son"), # 1
    __("saon"), # 2
]

default lalist = [
    __("la"), # 0
    __("le"), # 1
    __("lae"), # 2
] 

default elist = [
    __("e"), # 0
    __(""), # 1
    __("·e"), # 2
]

default nelist = [
    __("ne"), # 0
    __(""), # 1
    __("·ne"), # 2
]

default ricelist = [
    __("rice"), # 0
    __("eur"), # 1
    __("eur·ice"), # 2
]

default elleaulist = [
    __("elle"), # 0
    __("eau"), # 1
    __("elleau") # 2
]

# variables d'accords
default elle = ellelist[pronoun]
default elleind = elleindlist[pronoun]
default celle = cellelist[pronoun]
default ma = malist[pronoun]
default ta = talist[pronoun]
default sa = salist[pronoun]
default la = lalist[pronoun]

default e = elist[pronoun]
default ne = nelist[pronoun]
default rice = ricelist[pronoun]
default elleau = elleaulist[pronoun]

init python:
    def pronoun_update(p:int) :
        global pronoun
        global selectedpronouns
        global elle
        global elleind
        global celle 
        global ma
        global ta 
        global sa
        global la
        global e
        global ne
        global rice
        global elleau

        pronoun = p
        selectedpronouns = pronounlist[pronoun]
        elle = ellelist[pronoun]
        elleind = elleindlist[pronoun]
        celle = cellelist[pronoun]
        ma = malist[pronoun]
        ta = talist[pronoun]
        sa = salist[pronoun]
        la = lalist[pronoun]
        e = elist[pronoun]
        ne = nelist[pronoun]
        rice = ricelist[pronoun]
        elleau = elleaulist[pronoun]


    class PronounDropdown :
        def __init__(self, id) :
            self.id = id
            self.textbutton = TextButton(pronounlist[id], clicked=self.on_click)
        def on_click(self):
            pronoun_update(self.id)
            renpy.hide_screen("pronoun_dropdown_menu")
            renpy.restart_interaction()
        
        def get_all() :
            return [PronounDropdown(i) for i in range(len(pronounlist))]
                

    def tag_0(tag, argument, contents):
        if pronoun == 0:
            return contents

        return []

    def tag_1(tag, argument, contents):
        if pronoun == 1:
            return contents

        return []

    def tag_2(tag, argument, contents):
        if pronoun == 2:
            return contents

        return []

    config.custom_text_tags['0'] = tag_0
    config.custom_text_tags['1'] = tag_1
    config.custom_text_tags['2'] = tag_2


transform slide:
    yoffset -50
    easein .3 yoffset 0
    on hide:
        easeout .3 yoffset -30 alpha .0

# PAS UTILISE : Il faudrait que ce soit une image et pas un screen
screen pronoun_dropdown(position) :
    frame:
        pos position
        textbutton selectedpronouns+" V" action Show("pronoun_dropdown_menu",None, (position[0], position[1]+0.094))

# Menu déroulant permettant de changer de pronoms
screen pronoun_dropdown_menu(position):

    modal True

    # Cliquer en dehors du menu enlève le menu
    button:
        background None
        action Hide("pronoun_dropdown_menu")

    frame:
        pos position
        at slide
        has vbox
        for p in PronounDropdown.get_all() :
            add p.textbutton
