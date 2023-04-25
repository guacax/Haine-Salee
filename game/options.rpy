## Ce fichier contient les options qui peuvent être modifiées pour personnaliser
## votre jeu.
##
## Les lignes qui commencent avec deux dièses '#' sont des commentaires et vous
## ne devriez pas les décommenter. Les lignes qui commencent avec un seul dièse
## sont du code commenté et vous pouvez les décommentez quand c’est approprié
## (pour votre projet).


## Bases #######################################################################

## Un nom de jeu intelligible. Il est utilisé pour personnaliser le titre de la
## fenêtre par défaut et s’affiche dans l’interface ainsi que dans les rapports
## d’erreur.
##
## La chaîne de caractère contenu dans _() est éligible à la traduction.

define config.name = _("HaineSalee")


## Détermine si le titre renseigné plus haut est affiché sur l'écran du menu
## principal Configurez-le à False (Faux) pour cacher le titre.

define gui.show_name = True


## La version du jeu.

define config.version = "1.0"


## Texte placé sur l'écran "À propos" du jeu. Placez le texte entre triples
## guillemets, et laissez une ligne entre les paragraphes.

define gui.about = _p("""
""")


## Un nom court pour le jeu qui sera utilisé pour les répertoires et le nom de
## l’exécutable. Il ne doit contenir que des caractères ASCII et ne doit pas
## contenir d’espace, de virgules ou de points-virgules.

define build.name = "HaineSalee"


## Sons et musiques ############################################################

## Ces trois variables contrôlent, entre autres, quels mixeurs sont affichés
## au joueur par défaut. Configurer l’un de ceux-ci à False (Faux) cachera le
## mixeur concerné.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Pour autoriser le joueur à réaliser un test de volume, décommenter la ligne
## ci-dessous et utilisez-la pour configurer un son d’exemple.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Décommentez la ligne suivante pour configurer un fichier audio qui sera
## diffusé quand le joueur sera sur le menu principal. Ce son se poursuivra dans
## le jeu, jusqu’à ce qu'il soit stoppé ou qu’un autre fichier soit joué.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## Ces variables configurent les transitions qui sont utilisées quand certains
## événements surviennent. Chaque variable peuvent être configurée pour une
## transition. La valeur None indique qu’aucune transition ne doit être
## utilisée.

## À l’entrée ou à la sortie du menu du jeu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Entre les écrans du menu du jeu.

define config.intra_transition = dissolve


## La transition qui sera utilisée après le chargement d’une partie.

define config.after_load_transition = None


## La transition qui sera utilisé après la fin du jeu.

define config.end_game_transition = None


## Il n’y a pas de variable pour configurer la transition en début de partie. À
## la place, utilisez un état de transition juste après l’affichage de la toute
## première scène.


## Gestion des fenêtres ########################################################
##
## Cela contrôle l’affichage de la fenêtre de dialogue. Si « show », elle est
## toujours affichée. Si « hide », elle ne s’affiche que lorsque du dialogue est
## présent. Si « auto », La fenêtre est cachée avant chaque changement de scène
## et réapparait une fois le dialogue affiché.
##
## Après le début de la partie, cela peut-être changé avec les instructions
## « window show », « window hide » et « window auto ».

define config.window = "show"


## Transitions utilisées pour afficher ou cacher la fenêtre de dialogue

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Préférences par défaut ######################################################

## Contrôle la vitesse du texte. La valeur par défaut, 0, est infinie. Toute
## autre valeur est le nombre de caractères tapés par seconde.

default preferences.text_cps = 0


## Le délai d’avancée automatique. Des nombres importants entraînent une longue
## attente. Des valeurs réputées correctes sont comprises dans une plage allant
## de 0 à 30.

default preferences.afm_time = 15


## Répertoire de sauvegarde ####################################################
##
## Ces valeurs, dépendant de la plateforme, déterminent l’emplacement où Ren’Py
## stockera les fichiers de sauvegarde. Les fichiers de sauvegardes seront
## stockés dans :
##
## Windows : %APPDATA\RenPy\<config.save_directory>
##
## Macintosh : $HOME/Library/RenPy/<config.save_directory>
##
## Linux : $HOME/.renpy/<config.save_directory>
##
## Cela ne devrait généralement pas changer. Si vous le faîtes, choisissez
## toujours une chaîne de caractères littéraux, pas une expression.

define config.save_directory = "HaineSalee-1681543713"


## Icône #######################################################################
##
## L'icone affichée dans la barre des tâches ou sur le dock.

define config.window_icon = "gui/window_icon.png"


## Configuration de la compilation #############################################
##
## Cette section paramètre la façon dont Ren’Py transforme votre projet en
## fichier à distribuer.

init python:

    ## Les fonctions suivantes prennent en paramètres un format de fichier. Les
    ## formats de fichiers ne sont pas sensibles à la casse et correspondent au
    ## répertoire relatif au répertoire de base. Il n’y a pas de / à la fin. Si
    ## plusieurs formats correspondent, le premier est utilisé.
    ##
    ## Dans le format :
    ##
    ## / est le séparateur de répertoire.
    ##
    ## * correspond à tous les caractères à l’exception du séparateur de
    ##   répertoire.
    ##
    ## ** correspond à tous les caractères, y compris le séparateur de
    ##    répertoire.
    ##
    ## Par exemple, "*.txt" correspond à tous les fichiers txt dans le
    ## répertoire de base, "game/**.ogg" correspond à tous les fichiers ogg
    ## dans le répertoire game, mais aussi à tous ses répertoires. "**.psd"
    ## correspond à tous les fichiers psd quelque soit leur emplacement dans
    ## l’arborescence du fichier.

    ## Choisissez la valeur « None » pour les exclure de la distribution.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Pour archiver les fichiers, choisissez la valeur « archive ».

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Les fichiers correspondant au format de documentation sont dupliqués pour
    ## les compilation sur Mac, c'est pourquoi ils apparaissent deux fois dans
    ## l’archive zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## Une clé de licence A Google Play est requise pour télécharger les fichiers et
## permettre les achats dans l'application. Vous pourrez la trouver sur la page
## « Services & APIs » de la console de développement Google Play.

# define build.google_play_key = "..."


## Le nom d’utilisateur et du projet associé au projet itch.io, séparé par un
## slash.

# define build.itch_project = "renpytom/test-project"
