# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# define e = Character('Eileen', color="#c8ffc8")
init:
    $ n = Character('Nicole', color="#c8ffc8")
    $ j = Character('Javier', color="#c8ffc8")
    $ k = Character('Kim')
    $ b = Character('Betsy')
    $ pov = None
    $ r = None

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
    image bg dorm2 = "resources/bg/dorm-night.png"
    image bg dorm3 = "resources/bg/dorm-night-light.png"
    image bg forest = "resources/bg/forest.png"
    image bg school = "resources/bg/school.png"
    image bg street = "resources/bg/street.png"
    image bg fbday = "resources/bg/forest-building-day.jpg"
    image bg fbsunset = "resources/bg/forest-building-sunset.jpg"

    # Activities
    $ school_studying = False
    $ supplies_shopping = False
    $ forest_adventure = False

label start:
    scene bg dorm1
    with fade

    "Are you a boy or a girl?"
    menu:
        "Boy":
            $ pov = j
            jump boy
        "Girl":
            $ pov = n
            jump girl

label boy:
    "You wake up to the sunrise, and just like everyday, you grab your towel and head towards the door with the intention to take a shower."
    "Rommate" "Hold it there!"
    "His loud call surprises you, and you look back at him with a frown."

    pov "What's up? I'm going to take a bath."

    show k happy at charcenter
    with fade(0.5)
    k "I can see that! I suppose you think this is just an ordinary day in school and you're going to get ready for class."
    pov "Eeh, yeah. So...?"
    k "Hah, as I thought, you forgot! Today is a break day!"
    pov "Oooh, right! Sweet. It's not every day that you have good news for me."

    show k angry at charcenter
    k "Hey, it's not my fault that I have such a bad luck!"
    pov "I know, I know."
    "I just hope he doesn't..."

    show k happy at charcenter
    k "...Anyway! Let's do something fun today. What would you like to do?"
    "There you go. *sigh* Guess my free day will be a bros day..."
    jump choice

label choice:
    menu:
        "Go to the library and study" if not school_studying:
            pov "Let's go to the library and study. We have midterms next week, so we have to prepare."
            show k angry at charcenter
            k "Whaaaat? We have a free day and you want to study?"
            pov "You have to study anyway, so quit your whining."
            jump school
        "Shop supplies" if not supplies_shopping:
            pov "Let's go to the city and buy some supplies for the room. We are running low on food and class resources." 
            show k surprise at charcenter
            k "Ooh, you are right. We don't have enough snacks and my notebooks are all almost done."
            show k happy at charcenter
            k "I bet even you ain't able to fill a notebook before mid semester."
            "Sure, I don't make ramdom drawings here and there, and use it to make rogue-like games character stats calculations..."
            jump end
        "Quest in the forest" if not forest_adventure:
            pov "I'm in the mood for a quest in the forest. How about we explore the west side today?"
            show k happy at charcenter 
            with vpunch
            k "For real? I'm up for an adventure too! Let's do this!"
            "Have I made a mistake...?"
            jump end

label school:
    scene bg school
    with fade(1.5)

    show k sad at charcenter
    with fade(0.5)
    k "That was a lot of studying, now I'm tired."
    pov "You actually did a good job today, Kim!"

    show k happy at charcenter
    k "Sure did, right? Thanks for the help, I think I can aim for a B+ on the midterm now."
    pov "Why not aim for an A?" 

    show k neutral at charcenter
    k "Too much stress man, you know me."
    "Sure I do."
    pov "Well, the study went so well we actually have time to do more stuff."

    show k happy at charcenter 
    with vpunch
    k "Awesome! What would you like to do?"

    jump choice

label street:
    return

label forest:
    return

label girl:
    "Coming soon."
    jump end

label end:
    "That's it for now. See you soon."

