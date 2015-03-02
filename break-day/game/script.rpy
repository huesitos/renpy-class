# You can place the script of your game in this file.

init:
    # Declare characters used by this game.
    define pov = Character('[povname]', color="#c8ffc8")
    define k = Character('Kim', color="#ffc8ff")
    define b = Character('Betsy', color="#ffc8ff")

    # Character sprites
    image k happy = "resources/leo/leo_happy.png"
    image k neutral = "resources/leo/leo_neutral.png"
    image k surprise = "resources/leo/leo_surprise.png"
    image k sad = "resources/leo/leo_sad.png"
    image k frown = "resources/leo/leo_frown.png"
    image k angry = "resources/leo/leo_angry.png"
    
    image s happy = "resources/sophie/sophie_smile.png"
    image s neutral = "resources/sophie/sophie_neutral.png"
    image s surprise = "resources/sophie/sophie_shock.png"
    image s sad = "resources/sophie/sophie_sad.png"
    image s frown = "resources/sophie/sophie_frown.png"
    image s angry = "resources/sophie/sophie_angry.png"

    $ charcenter = Position(xpos=0.5, xanchor=0.5, ypos=0.6, yanchor=0.5)

    # Backgrounds
    image bg dorm1 = "resources/bg/dorm-day.png"
    image bg dorm2 = "resources/bg/dorm-night-light.png"
    image bg dorm3 = "resources/bg/dorm-night.png"
    image bg forest = "resources/bg/forest.png"
    image bg school = "resources/bg/school.png"
    image bg street = "resources/bg/street.png"
    image bg forest_house = "resources/bg/forest-building-sunset.jpg"

    python:
        # Activities
        school_studying = False
        school_studying_success = False
        supplies_shopping = False
        forest_adventure = False
        forest_house = False
        position = [0,0]
        house_position = (2,2)

        # Item bought
        programming_book = False
        backpack = False
        survival_kit = False

        # Snack bought
        fruits = False
        chips = False
        nuts = False

        povname = ""
        def ask_name(default):
            global povname
            povname = renpy.input("What is your name?")
            povname = povname.strip()

            if not povname:
                povname = default

label start:
    scene bg dorm1 
    with fade

    # "Are you a boy or a girl?"
    # menu:
    #     "Boy":
    #         $ ask_name("Javier")
    #         jump boy
    #     "Girl":
    #         $ ask_name("Nicole")
    #         jump girl
    $ ask_name("Javier")
    jump boy
