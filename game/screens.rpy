################################################################################
## Initialisation
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Écrans de jeu
################################################################################


## Écran des dialogues #########################################################
##
## L’écran des dialogues est utilisé pour afficher les dialogues du joueur. Il
## prend deux paramètres, who(qui) et what(quoi) qui sont respectivement le
## nom du personnage en train de parler et le texte à afficher. (Le paramètre
## who(qui) peut être None si aucun nom n’est donné.)
##
## Cet écran affiche le texte correspondant à what. Il peut également créer un
## texte avec le paramètre who et l’identifiant « window » est utilisé pour
## déterminer les styles à appliquer.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Si il y a une side image, l'afficher au-dessus du texte. Ne pas
    ## l'afficher sur la version téléphone - pas assez de place.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Rendre la boîte du nom personnalisable à travers l'objet Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Écran de saisie #############################################################
##
## Cet écran est utilisé pour afficher renpy.input. Le paramètre prompt est
## utilisé pour passer le texte par défaut.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Écran des choix #############################################################
##
## Cet écran est utilisé pour afficher les choix qui seront fait par le joueur
## dans le jeu. Le premier paramètre, items, est une liste d'objets contenant
## chacun des champs de texte et d'action.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Écran des menus rapides #####################################################
##
## Les menus rapides sont affichés dans le jeu pour permettre un accès rapide à
## certaines fonctions.

screen quick_menu():

    ## Assure qu'il apparaît au-dessus des autres screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Retour") action Rollback()
            textbutton _("Historique") action ShowMenu('history')
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Sauvegarde") action ShowMenu('save')
            textbutton _("Sauvegarde R.") action QuickSave()
            textbutton _("Chargement R.") action QuickLoad()
            textbutton _("Préf.") action ShowMenu('preferences')


## Ce code garantit que le menu d’accès rapide sera affiché dans le jeu, tant
## que le joueur n’aura pas explicitement demandé à cacher l’interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Screens du menu principal et du menu de jeu
################################################################################

## Écran de navigation #########################################################
##
## Cet écran est disponible dans le menu principal et dans le menu de jeu. Il
## fournit l’accès aux autres menus et permet le démarrage du jeu.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Nouvelle partie") action Start()

        else:

            textbutton _("Historique") action ShowMenu("history")

            textbutton _("Sauvegarde") action ShowMenu("save")

        textbutton _("Charger") action ShowMenu("load")

        textbutton _("Préférences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Fin de la rediffusion") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu principal") action MainMenu()

        textbutton _("À propos") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## L'aide n’est ni nécessaire ni pertinente sur les appareils
            ## mobiles.
            textbutton _("Aide") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Le bouton pour quitter est banni sur iOS et inutile sur Android
            ## et sur le Web.
            textbutton _("Quitter") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Écran du menu principal #####################################################
##
## Utilisé pour afficher le menu principal quand Ren'Py démarre.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## Ceci assure que tout autre screen de menu est remplacé.
    tag menu

    add gui.main_menu_background

    ## Cette frame vide obscurcit le menu principal.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Écran du menu de jeu ########################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Réserve de l'expace pour la section de navigation.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Retour"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Écran « À propos... » #######################################################
##
## Cet écran présente le générique, les crédits et les informations de copyright
## relatives au jeu et à Ren’Py.
##
## Il n’y a rien de spécial sur cet écran. Par conséquent, il sert aussi
## d’exemple pour créer un écran personnalisé.

screen about():

    tag menu

    ## Cette déclaration concerne l’écran game_menu. L’élément vbox est ensuite
    ## inclus dans la fenêtre de l'écran game_menu.
    use game_menu(_("À propos"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about est généralement initialisé dans le fichier
            ## options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Conçu avec {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Écran de chargement et de sauvegarde ########################################
##
## Ces écrans permettent au joueur d’enregistrer le jeu et de le charger
## à nouveau. Comme ils partagent beaucoup d’éléments communs, ils sont
## tous les deux implémentés dans un troisième écran, appelé fichiers_slots
## (emplacement_de_fichier).
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Sauvegarde"))


screen load():

    tag menu

    use file_slots(_("Charger"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Sauvegardes automatiques"), quick=_("Sauvegardes rapides"))

    use game_menu(title):

        fixed:

            ## Cette instruction s’assure que l’évènement enter aura lieu avant
            ## que l’un des boutons ne fonctionne.
            order_reverse True

            ## Le nom de la page, qui peut être modifié en cliquant sur un
            ## bouton.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La grille des emplacements de fichiers.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A %d %B %Y, %H:%M"), empty=_("emplacement vide")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Boutons pour accéder aux autres pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) donne les nombres de 1 à 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Écran des préférences #######################################################
##
## L’écran de préférences permet au joueur de configurer le jeu pour mieux
## correspondre à ses attentes.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Préférences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Affichage")
                        textbutton _("Fenêtre") action Preference("display", "window")
                        textbutton _("Plein écran") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Avance rapide")
                    textbutton _("Texte non lu") action Preference("skip", "toggle")
                    textbutton _("Après les choix") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Des boites vbox additionnelles de type "radio_pref" ou
                ## "check_pref" peuvent être ajoutées ici pour ajouter des
                ## préférences définies par le créateur du jeu.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Vitesse du texte")

                    bar value Preference("text speed")

                    label _("Avance automatique")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volume de la musique")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Volume des sons")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Volume des voix")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Couper tous les sons"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## Écran de l'historique #######################################################
##
## Il s’agit d’un écran qui affiche l’historique des dialogues au joueur. Bien
## qu’il n'y ait rien de spécial sur cet écran, il doit accéder à l’historique
## de dialogue stocké dans _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Cette instruction permet d’éviter de prédire cet écran, car il peut être
    ## très large
    predict False

    use game_menu(_("Historique"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Cela positionne correctement l'écran si history_height est
                ## initialisé à None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Utilise pour la couleur du texte, la couleur par
                        ## défaut des dialogues du personnage si elle a été
                        ## initialisée.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("L'historique des dialogues est vide.")


## Ceci détermine quels tags peuvent être affichés sur le screen de
## l'historique.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Écran d'aide ################################################################
##
## Cet écran fournit des informations sur les touches et les boutons de souris.
## En interne, il utilise d’autres écrans (keyboard_help, mouse_help et
## gamepad_help) pour afficher une aide dédiée.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Aide"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Clavier") action SetScreenVariable("device", "keyboard")
                textbutton _("Souris") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Manette") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Entrée")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Espace")
        text _("Avance dans les dialogues sans effectuer de choix.")

    hbox:
        label _("Flèches directionnelles")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Echap.")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Ctrl")
        text _("Fait défiler les dialogues tant que la touche est pressée.")

    hbox:
        label _("Tab")
        text _("Active ou désactives les «sauts des dialogues».")

    hbox:
        label _("Page Haut")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Page Bas")
        text _("Avance jusqu'au prochain dialogue.")

    hbox:
        label "H"
        text _("Cache l’interface utilisateur.")

    hbox:
        label "S"
        text _("Prend une capture d’écran.")

    hbox:
        label "V"
        text _("Active la {a=https://www.renpy.org/l/voicing}{size=24}vocalisation automatique{/size}{/a}.")

    hbox:
        label "Shift+A"
        text _("Ouvre le menu d'accessibilité.")


screen mouse_help():

    hbox:
        label _("Bouton gauche")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Bouton central")
        text _("Cache l’interface utilisateur.")

    hbox:
        label _("Bouton droit")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Molette vers le haut\nClic sur le côté du Rollback")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Molette vers le bas")
        text _("Avance jusqu'au prochain dialogue.")


screen gamepad_help():

    hbox:
        label _("Bouton R1\nA/Bouton du bas")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Gâchettes gauche")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Bouton R1")
        text _("Avance jusqu'au prochain dialogue.")


    hbox:
        label _("Boutons directionnels, stick gauche")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Start, Guide")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Y/Bouton du haut")
        text _("Cache l’interface utilisateur.")

    textbutton _("Calibrage") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Écrans additionnels
################################################################################


## Écran de confirmation #######################################################
##
## Cet écran est appelé quand Ren'Py souhaite poser une question au joueur dont
## la réponse est oui ou non.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Cette instruction s’assure que les autres écrans resteront en arrière
    ## plan tant que cet écran sera affiché.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Oui") action yes_action
                textbutton _("Non") action no_action

    ## Le clic bouton droit et la touche Echap. correspondent à la réponse
    ## "non".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Écran de l’indicateur d'avance rapide #######################################
##
## L’écran skip_indicator est affiché pour indiquer qu’une avance rapide est en
## cours.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Avance rapide")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Cette transformation est utilisé pour faire clignoter les flèches l’une après
## l’autre.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Nous devons utiliser une police qui a le glyphe BLACK RIGHT-POINTING
    ## SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Écran de notification #######################################################
##
## Cet écran est utilisé pour affiché un message au joueur. (Par exemple, quand
## une sauvegarde rapide a eu lieu ou quand une capture d’écran vient d’être
## réalisée.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Écran NVL ###################################################################
##
## Cet écran est utilisé pour les dialogues et les menus en mode NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Les dialogues sont affichés soit dans une vpgrid soit dans une vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ce paramètre contrôle le maximum d’entrée dans le mode NVL qui peuvent être
## affichée simultanément.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Variantes pour les mobiles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Comme la souris peut ne pas être présente, nous remplaçons le menu rapide
## avec une version qui utilise des boutons plus gros et qui sont plus faciles à
## toucher du doigt.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Retour") action Rollback()
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
