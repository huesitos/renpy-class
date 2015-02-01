# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# define e = Character('Eileen', color="#c8ffc8")
init:
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

    "Are you a boy or a girl?"
    menu:
        "Boy":
            $ ask_name("Javier")
            jump boy
        "Girl":
            $ ask_name("Nicole")
            jump girl

label boy:
    "You wake up to the sunrise, and just like everyday, you grab your towel and head towards the door with the intention to take a shower."
    "Roommate" "[povname], hold it there!"
    "His loud call surprises you, and you look back at him with a frown."

    pov "What's up? I'm going to take a bath."

    show k happy at charcenter 
    with fade

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
            "Sure, I don't make random drawings here and there, and use it to make rogue-like games character stats calculations..."
            jump street
        "Quest in the forest" if not forest_adventure:
            pov "I'm in the mood for a quest in the forest. How about we explore the west side today?"
            show k happy at charcenter 
            with hpunch
            k "For real? I'm up for an adventure too! Let's do this!"
            "Have I made a mistake...?"
            jump forest

label school:
    scene bg school
    with fade
    $ school_studying = True

    if supplies_shopping:
        show k neutral at charcenter
        with dissolve

        if programming_book:
            pov "Well, I will be able to study some chapters of the {i}programming book{/i} I bought today. It seems to be pretty high level stuff."
            k "You are a smart guy, so you'll be done with it in no time."
            pov "Thanks, man."
        elif backpack:
            pov "It was a nice idea to buy the {i}backpack{/i}, we were able to carry the food here easely."
            show k happy at charcenter
            k "Very good indeed! Pass me some of that, all the studying is making me hungry."
            if fruits or nuts:
                k "Well, that was a very healthy snack."
                pov "Thus, the best one."
            else:
                show k sad at charcenter
                k "That was good, but I think I ate a bit more than what I should."
                pov "You didn't eat a {i}bit{/i} more, you ate everything we bought!"
                show k angry at charcenter
                with hpunch
                k "Hey! You ate too!"
                pov "But not as much as you... Nevermind, it's not a big deal."
        scene bg school
        with fade

    if forest_adventure:
        show k sad at charcenter
        with dissolve
        k "*sigh*"
        "Our little adventure in the forest must have exhausted him. He was so tired he didn't concentrate enough in studying..."
        pov "Don't worry, we all have our days."
        k "Yeah."
        scene bg school
        with fade
        show k neutral at charcenter
        with dissolve
    else:   
        $ school_studying_success = True
        show k sad at charcenter
        with dissolve
        k "That was a lot of studying, now I'm tired."
        pov "You actually did a good job today, Kim!"

        show k happy at charcenter
        k "Sure did, right? Thanks for the help, I think I can aim for a B+ on the midterm now."
        pov "Why not aim for an A?" 

        show k neutral at charcenter
        k "Too much stress man, you know me."
        "Sure I do."

    if not forest_adventure and not supplies_shopping:
        pov "Well, the study went so well we actually have time to do more stuff."
        show k happy at charcenter 
        with hpunch
        k "Awesome! What would you like to do?"
        jump choice
    else:
        pov "I think it's enough for today. Let's go back to our room."
        k "Alright."
        jump end

label street:
    scene bg street
    with fade
    show k neutral at charcenter
    with dissolve
    $ supplies_shopping = True

    k "I bought my notebooks. What did you buy?"

    menu:
        "Programming book":
            $ programming_book = True
            pov "An interesting {i}programming book{/i} I'd like to study later."
            k "Right, you want to program games."
        "New backpack":
            $ backpack = True
            pov "I bought a {i}new backpack{/i}."
            k "Good choice. Your old one is rather... well, old."
        "Survival kit for dummies":
            $ survival_kit = True
            if forest_adventure:
                pov "I found a {i}survival kit for dummies{/i} at the tools section. It has a compass, along with other things. I think it'll help us a lot next time we go for another \"adventure\"."
                k "Well thought. Next time we'll actually make some progress."
            else:
                pov "There was a {i}survival kit for dummies{/i} and somehow I have a hunch it might come in handy."
                k "Of course! Now we are totally prepared for a zombie apocalypse."
    
    show k happy at charcenter
    with dissolve
    k "How about we buy the snacks now?"

    menu:
        "Organic fruits and water":
            $ fruits = True

            pov "Let's buy {i}organic fruits and water{/i}."
            show k sad at charcenter
            k "I wanted some chips and drinks..."
        "Chips and soft-drinks":
            $ chips = True

            pov "Let's buy {i}chips and soft-drinks{/i}."
            k "Good choice!"
        "Nuts and juice":
            $ nuts = True

            pov "Let's buy {i}nuts and juice{/i}."
            k "Ok, but make it grape juice then."

    if school_studying:
        if fruits or nuts:
            $ chips = True
            pov "Like I said, you did a great job studying today. So, I'll make an exception and buy some chips for you today."
            show k happy at charcenter
            k "Aww, thanks pops!"
            "That kind of did sound like a dad talking..."
        else:
            pov "I did well today in my studies, so I'll reward myself with some..."
            menu:
                "Organic fruits and water":
                    $ fruits = True
                "Nuts and juice":
                    $ nuts = True
            k "Best excuse I've heard for self-indulgence."
            pov "Shh!"

    if not forest_adventure and not school_studying:
        pov "Well, we still have some free time to do more stuff."
        show k happy at charcenter 
        with hpunch
        k "Awesome! What would you like to do?"
        jump choice
    else:
        pov "I think it's enough for today. Let's go back to our room."
        k "Alright."
        jump end

label forest:
    scene bg forest
    with fade
    show k happy at charcenter
    with dissolve
    $ forest_adventure = True
    pov "I swear this forest gives me goosebumps every time I come."
    k "Yeah! I feel the same way."
    "Yet you seem to be very happy about it..."
    k "This is where we left the exploration last time. I heard there is a house hidden in the forest. Want to go there?"
    pov "Do you know where that is?"
    k "Not at all. But we can roam around and maybe we'll find it. It should not be that hard! Where should we go now?"

    if survival_kit:
        show k surprise at charcenter
        pov "Or, we could make it easier using the appropiate tools. Remember that {i}survival kit for dummies{/i} I bought? It has a compass in it, so we can use it to make the exploring more efficient."
        show k happy at charcenter
        k "Well thought, my friend. So, how do we use it to find the house?"
        pov "Do you know at least in what direction it is?"
        k "I heard it was somewhat northwest from this point."
        pov "Alright. Let me see..."
        pov "Great. The compass is pointing North to our right. Therefore, we should go to..."
        jump explore
    else:
        scene bg forest
        with fade
        show k neutral at charcenter
        with dissolve
        "We walked around, but we didn't find anything interesting."
        pov "I guess we won't be able to find the house."
        k "Yeah, it's rather disappointing... Let's go."
    
    if not supplies_shopping and not school_studying:
        pov "Well, we still have some free time to do more stuff."
        show k happy at charcenter 
        with hpunch
        k "Awesome! What would you like to do?"
        jump choice
    else:
        pov "I think it's enough for today. Let's go back to our room."
        k "Alright."
        jump end

label explore:
    menu:
        "Up":
            
            show k neutral at charcenter
            k "That doesn't make sense..."
            "He's right..."
            pov "We should go..."
            jump explore
        "To the left":
            show k neutral at charcenter
            k "That doesn't make sense..."
            "He's right..."
            pov "We should go..."
            jump explore
        "Down":
            if position[1] == 2:
                show k neutral at charcenter
                k "I don't think that's the right way..."
                "He's right..."
                pov "We should go..."
                jump explore
            else:
                $ position[1] += 1
            if position >= [2,2]:
                jump forest_house
            else:
                show k happy at charcenter
                k "Alright, now where to?"
                jump explore
        "To the right":
            if position[0] >= 2:
                show k neutral at charcenter
                k "I don't think that's the right way..."
                "He's right..."
                pov "We should go..."
                jump explore
            $ position[0] += 1
            if position == [2,2]:
                jump forest_house
            else:
                show k happy at charcenter
                k "Alright, now where to?"
                jump explore

label forest_house:
    scene bg forest_house at truecenter
    with fade
    show k surprise at charcenter
    with dissolve
    $ forest_house = True

    pov "We found it!"
    show k happy at charcenter
    with hpunch
    k "WE DID IT! Look at it! It's huge and beautiful and magestic and AWESOME!"
    "He's like a child with a new toy."
    show k surprise at charcenter
    k "I wonder who lives there..."
    pov "You don't know?"
    k "Nope. Nobody really knows."
    show k happy at charcenter
    k "Let's find out!"
    pov "Of course not!"
    show k frown at charcenter
    k "What? Why not?"
    pov "Because it's very late and we can't just go knocking on random people houses."
    show k sad at charcenter
    k "Good point. Though I really want to investigate it..."
    show k surprise at charcenter
    k "Oooooh!"
    pov "What?"
    show k happy at charcenter
    with hpunch
    k "I have an idea! Let's pretend we have some research project and we want info on the house to do it."
    pov "Like an architecture project or something?"
    k "Even a history project!"
    pov "That's actually pretty reasonable. However, it's still too late to try it know. Maybe some other day."
    show k sad at charcenter
    k "Yeah, you are right."
    show k neutral at charcenter
    k "Let's go to our room then, I'm feeling tired now."
    jump end

label end:
    scene bg dorm2 
    with fade
    show k neutral at charcenter
    with dissolve
    
    pov "Wow, we actually had a rather busy day."
    if school_studying:
        show k frown at charcenter
        k "Yeah, and kind of boring too with all that studying."
        if school_studying_success:
            pov "But you did very good, and it will help you with your midterms."
            show k happy at charcenter
            k "Yup, I already feel smarter."
        else:
            pov "Any little study helps in the end. Even if it wasn't too good today, next time it'll be easier."

        show k neutral at charcenter
        if programming_book: 
            pov "I also had the chance to study my new {i}programming book{/i}." 
    if supplies_shopping:
        show k happy at charcenter
        k "I now have new notebooks and we bought supplies."
        if programming_book: 
            pov "And I got a new {i}programming book{/i}." 
            k "Good luck with that."
        if backpack: 
            pov "And I got a new {i}backpack{/i}."
            k "Now you can go to class with style."
        if survival_kit: 
            pov "And we have a new {i}survival kit for dummies{/i}." 
            show k neutral at charcenter
            if not (forest_adventure and forest_house): 
                k "Which I see no use for." 
            if forest_adventure and not forest_house: 
                k "Which will help us next time we decide to go for a forest adventure." 
    if forest_adventure:
        pov "And that walk in the forest was pretty good excercise."
        if not school_studying_success: 
            k "Tell me about it." 
        if forest_house:
            show k happy at charcenter
            pov "That house in the forest though..."
            k "Oooh, man! I'm so excited about the house in the forest."
            pov "I don't get where all the enthusiam comes from, but I can't lie I'm a little curious."
            k "Always so modest."
        else:
            pov "Maybe we'll be able to find the house next time."
    k "Well, I'm done for today. Good night mate."
    hide k
    with dissolve
    pov "I'm done too. Guess that's it for today..."
    "Thanks for playing."
    return

label girl:
    "Coming soon."
    return
