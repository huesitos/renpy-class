# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

init:
    # Declare characters used by this game.
    $ charname = 'Sam'
    define s = Character(charname, color="#c8ffc8")

    # Character sprite
    image s happy = "resources/sam_happy.png"
    image s neutral = "resources/sam_neutral.png"
    image s surprise = "resources/sam_surprise.png"
    image s sad = "resources/sam_sad.png"
    image s frown = "resources/sam_frown.png"
    image s angry = "resources/sam_angry.png"

    # Backgrounds
    image bg black = "resources/bg_black_screen.jpg"
    image bg coderdojochi = "resources/bg_coderdojochi.jpg"
    image bg gamecenter = "resources/bg_game_center.jpg"
    image bg library = "resources/bg_library.jpg"

    $ charcenter = Position(xpos=0.5, xanchor=0.5, ypos=0.6, yanchor=0.5)

    # Variables
    python:
        gamecenter = False
        game = ''
        library = False
        gift = ''

# The game starts here.
label start:
    scene bg black
    "Lousy guy" "Hello there!"
    "Lousy guy" "What's my name you ask? I am [charname]."
    s "Hold on, where is my face?!"

    show s happy at charcenter
    with fade

    s "Now that's more like it! Mmm?"
    show s neutral at charcenter
    s "Where are we? We are at CoderDojoChi class!"

    scene bg coderdojochi
    with fade
    show s happy at charcenter
    s "This is the place where you will begin the way of the coder."

    show s sad at charcenter
    s "But the class is already over, so you'll have to come another day."
    
    show s happy at charcenter
    with hpunch
    s "But we can still have fun somewhere else! Where would you like to go?"

    menu:
        "Game center":
            s "You like videogames too? Awesome! Let's go play at the game center!"
            jump gamecenter
        "Library":
            s "There's nothing better to ease the mind than a quiet, relaxing reading. Let's go to the library!"
            jump library

    return

label gamecenter:
    scene bg gamecenter
    with fade
    $ gamecenter = True

    show s happy at charcenter
    with hpunch
    s "Look at all the games we can play! What do you want to play?"

    menu:
        "Smash Brothers":
            s "I see you like fighting games. That seems like fun. May the best man win!"
            $ game = "Smash Brothers"
            $ gift = "Kirby figurine"
        "Mario Party":
            s "So you like party games! Sounds like we're going to have some good laughs. May the best man win!"
            $ game = "Mario Party"
            $ gift = "Mario Star"
        "League of Legends":
            s "A battle arena game, neat. Let's show them what we've got!"
            $ game = "League of Legends"
            $ gift = "Teemo hat"
        "Age of Empires":
            s "A real time strategy, and old school too! I feel nostalgia now. May the best man win!"
            $ game = "Age of Empires"
            $ gift = "Cathedral wonder"

    # After playing
    show s happy at charcenter
    with dissolve
    s "That was lots of fun! Let's come back again another day. It's getting late... maybe we should go back to CoderDojoChi place."
    jump end

label library:
    scene bg library
    with fade
    $ library = True

    show s happy at charcenter
    with dissolve
    show s happy at charcenter
    with hpunch
    s "Look at all the books we can read here. I wish I could live long enough to read them all! What are you going to read?"
    $gift = renpy.input("Book name:")
    $gift = gift.strip()
    s "That sounds nice, I'll add it to my books to read list. Well, we have to be quiet here, so let's skip the talk and start the reading!"

    # After reading
    show s happy at charcenter
    with dissolve
    s "Well, time sure flies when you are having fun! It's about time we head back to CoderDojoChi place."
    jump end

label end:
    scene bg coderdojochi
    with fade
    show s happy at charcenter
    with dissolve

    s "Hope you enjoyed the trip, 'cause I did a lot. I had such a great time with you that I would like to give you a gift!"
    if gamecenter:
        s "You seemed to enjoy the {i}[game]{/i} game a lot, so I figured you'd like this {b}[gift]{/b}."
        # show gift
    else:
        s "I saw you were really into that {b}[gift]{/b} book, so I got you a copy from the library bookstore."

    s "I'll be going home then. Be sure to come for next class!"

    "Fin. Thanks for playing."