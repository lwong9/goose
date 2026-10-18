# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("YOU") # Player
define ufog = Character("?") # UFO Duck
define starg = Character("Stargazing Goose")
define rg = Character("Rainbow Goose")
define sg = Character("Goose with Shoe")
define tg = Character("Suspicious Goose")
define rlg = Character("Real Goose")
define cg1 = Character("Child Goose 1")
define cg2 = Character("Child Goose 2")
define cg3 = Character("Child Goose 3")

# DUOLINGO SYSTEM 
default learned_words = ["Honk?"]
default meanings = ["???"]
default final_sentence = ""

init python:
    def submit_final_sentence(words):
        # 1. FIX: Use 'global' so Python can modify the variable outside this function
        global final_sentence 
        
        # Reset the sentence first so it doesn't just append forever if clicked twice
        final_sentence = "" 
        
        for word in words:
            final_sentence += (word + " ")
            
screen duolingo():
    default active_sentence = []
    default word_bank = list(learned_words)
    hbox:
        align (0.5, 0.4)
        spacing 100
        frame: 
            background Solid("#ffffff")
            vbox: 
                xsize 500
                ysize 500

                label "Known Words:" xalign 0.5
                for index in range(len(learned_words)):
                    label "[learned_words[index]], Meaning: [meanings[index]]" align (0.0, 0.0)
        frame:
            background Solid("#ff0000")
            vbox:
                align (0.5, 0.4)
                spacing 30
                xsize 500
                ysize 500

                # --- TARGET SENTENCE LINE ---
                label "Speak:" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 15
                    yminimum 60 
                    
                    for index, word in enumerate(active_sentence):
                        textbutton word:
                            action [
                                RemoveFromSet(active_sentence, word),
                                AddToSet(word_bank, word)
                            ]
                    
                    if not active_sentence:
                        text "_________________________" color "#777"

                null height 40

                # --- WORD BANK ---
                label "Word Bank:" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 15
                    
                    for word in word_bank:
                        textbutton word:
                            action [
                                RemoveFromSet(word_bank, word),
                                AddToSet(active_sentence, word)
                            ]

                null height 50

                # SUBMIT SENTENCE
                textbutton "Submit":
                    xalign 0.5
                    action [
                        Function(submit_final_sentence, active_sentence), 
                        Return() # This safely exits the screen back to your scene!
                    ]


label start:
    # START OF THE INTRODUCTION

    scene black 
    scene intro1 with dissolve

    "Another long day has passed. You fall into routine, your shoes following the worn and familiar path back to your home."
    "The sky has long since turned dark and the cold night wraps around your shoulders. But you're used to it."
    
    scene intro2 with dissolve

    "You happily admire on the baguette in your hand. It's from the new bakery that recently opened across your street."
    "You stumbled upon it by accident, but apparently, crowds from all over the world have FLOCKED here to try it."
    "You can't wait to eat it once you get home."

    scene intro3 with dissolve

    "Suddenly, you hear a strange sound in the distance."

    play sound "UFO_beep.mp3" # NEED

    mc "(Huh?)"

    scene intro4 with dissolve

    mc "?????"
    ufog "Honk honk honk honk."
    "Before you have time to process it, you feel your skin start to heat up. The light from the strange carrier grows brighter and you can barely keep your eyes open."

    scene intro5 with dissolve

    "Slowly, the bread in your hand detaches and begins floating towards the spacecraft."
    mc "No!!!! My baguette!!!!"

    scene intro6 with dissolve 

    "You reach up for the baguette."
    "Then, you feel your feet start to lift from the ground."

    scene intro7 with dissolve 

    mc "Ah!! Help!!!!"
    ufog "Honk honk honk."
    mc "Who are you?!"

    scene intro8 with dissolve

    $ renpy.pause()

    scene intro9 with dissolve

    $ renpy.pause()

    scene intro10 with dissolve

    "You vision blurs and you find yourself unresponsive, passed out on the floor of the aircraft."
    "The ground underneath you rattles and whirs."
    "Time and reality contort into disfigured notions as you travel with your kidnapper..."

    scene intro11 with dissolve 

    "When you open your eyes again, the world around you has changed."
    "The space carrier gently places you back onto the ground and you take in the unfamiliar world around you..."
    mc "Is that a..."
    mc "...goose?"

    scene ufo day with dissolve 

    show ufog idle 

    menu: 
        "Talk to the Goose":
            mc "Hello?"

            show ufog speak 
            ufog "Honk."

            jump first_ufog

    return

default first_ufog_questions = []

label first_ufog:
    show ufog idle
    menu: 
        set first_ufog_questions

        "Why did you take me here?":
            show ufog speak
            ufog "Honk honk." #TENTATIVE LANGUAGE
            jump first_ufog

        "What is this place?":
            show ufog speak
            ufog "Honk honk honk honk."
            jump first_ufog

        "What did you do with my baguette?":
            show ufog speak
            ufog "Honk. Honk."
            jump first_ufog
        
        "Can I go back home?" if len(first_ufog_questions) >= 3:
            show ufog speak
            ufog "Honk honk honk. Honk honk honk honk."
            show ufog idle
    
    "This isn't working. Maybe you should try to speak in the goose language."

    call screen duolingo

    ufog "Honk?"
    
    "You give a frustrated sigh."
    "You want to go back to Earth, but you're not sure how to communicate with the goose that brought you here."
    "If you look around, you might find some clues."

    # END OF THE INTRODUCTION

    # START OF THE GAME

    show screen show_location(1)
    

# ALL LOCATIONS
# UFOG - HILL ENTRANCE - MAIN STREET - PARK
#          HILL          

default night_trigger = False
default nighttime = False

screen show_location(i):
    if i == 1: # (1) - UFO
        if nighttime:
            add "images/ufo night.png"
        else:
            add "images/ufo day.png"
        add "images/ufog idle.png"
        imagemap:
            ground "images/ufog idle.png"
            hotspot (852, 44, 260, 1003) action [Hide(), Jump("guess")] tooltip "The goose that brought you here"

            $ tooltip = GetTooltip()

            if tooltip:
                text "[tooltip]" xalign 0.5 yalign 0.5
    elif i == 2: # (2) - HILL ENTRANCE
        timer 0.01 action If(night_trigger == True, true=Jump("rest"), false=None)
        if nighttime: 
            add "images/hill entrance night.jpg"
            imagemap: 
                ground "images/hill entrance night.jpg"
                hotspot (821, 408, 348, 335) action [Hide(), Show("hill_screen")] tooltip "Push through the trees"
                $ tooltip = GetTooltip()

                if tooltip:
                    text "[tooltip]" xalign 0.5 yalign 0.5
        else:
            add "images/hill entrance day.jpg"
            imagemap: 
                ground "images/hill entrance day.jpg"
                hotspot (821, 408, 348, 335) action [Hide(), Show("hill_screen")] tooltip "Push through the trees"
                $ tooltip = GetTooltip()

                if tooltip:
                    text "[tooltip]" xalign 0.5 yalign 0.5
    elif i == 3: # (3) - MAIN STREET
        add "images/main street.png"
        imagebutton:
            idle Transform("images/rainbow goose.png", zoom=0.5)
            align (0.6, 0.8)
            tooltip "A rainbow goose."
            action [Hide(), Jump("rainbow")]
        imagebutton:
            idle Transform("images/shoes goose.png", zoom=0.45)
            align (0.1, 0.7)
            tooltip "A goose with only one shoe."
            action [Hide(), Jump("shoe")]

        $ tooltip = GetTooltip()

        if tooltip:
            text "[tooltip]" xalign 0.5 yalign 0.5

    elif i == 4: # (4) - PARK
        add "images/park.png"
        imagebutton:
            idle Transform("images/thief goose.png", zoom=0.5)
            align (0.8, 0.7)
            tooltip "A suspicious-looking goose."
            action [Hide(), Jump("thief")]
        
        imagebutton:
            idle Transform("images/real goose.png", zoom=0.25)
            align (0.2, 0.6)
            tooltip "An interesting-looking goose."
            action [Hide(), Jump("real")]

        imagebutton:
            idle Transform("images/goose friends.png", zoom=0.25)
            align (0.5, 0.6)
            tooltip "A group of geese friends."
            action [Hide(), Jump("friends")]
        
        $ tooltip = GetTooltip()

        if tooltip:
            text "[tooltip]" xalign 0.5 yalign 0.5
    else:
        text "Location not found"


    # calculate the next screens
    default right_i = i + 1
    default left_i = i - 1
    python: 
        if right_i > 4:
            right_i = 1
        if left_i < 1:
            left_i = 4

    imagebutton:
        idle "images/right.png"
        hover "images/right_hover.png"
        xalign 0.95
        yalign 0.5
        action [Hide(), Show("show_location", i=right_i)]
    imagebutton:
        idle "images/left.png"
        hover "images/left_hover.png"
        xalign 0.05
        yalign 0.5
        action [Hide(), Show("show_location", i=left_i)]

screen hill_screen():
    if nighttime:
        add "images/stargazing.jpg"
        imagemap:
            ground "images/stargazing.jpg" 
            hotspot (1330, 222, 212, 763) action [Hide(), Jump("stargaze")] tooltip "A goose that is staring at the stars."

            $ tooltip = GetTooltip()

            if tooltip:
                text "[tooltip]" xalign 0.5 yalign 0.5
    else:
        add "images/hill.jpg"
    imagebutton:
        idle "images/exit.png"
        hover "images/exit_hover.png"
        xalign 0.5
        yalign 0.95
        action [Hide(), Show("show_location", i=2)]

label explore:
    call screen show_location(i=1)
    return

label guess:
    if nighttime: 
        scene ufo night
    else: 
        scene ufo day
    show ufog idle
    call screen duolingo
    mc "[final_sentence]"

    if final_sentence != "Hok Hank Hounk ":
        show ufog speak
        ufog "Honk?"
        show ufog idle
        "That didn't work."
        jump explore
    else:
        "GO TO END" #TODO

label stargaze:
    scene stargazing
    if "Hounk" in learned_words:
        "The goose looks wistfully at the sky."
    else:
        starg "..."
        "The goose looks wistfully at the sky."
                
        starg "Honk honk, honk honk honk."
        starg "Honk. honk honk."
                
        menu:
            "Look into the telescope":
                scene earth
                $ renpy.pause()
                
        scene stargazing
                
        "The goose points at the sky."
        starg "Hounk."

        "You learned: Hounk (Earth)"
        $ learned_words.append("Hounk")
        $ meanings.append("Earth")
    call screen hill_screen

label rainbow:
    scene main street
    show rainbow goose
    if "Hoonk" in learned_words:
        rg "Hoonk!"
    else:
        rg "Hoonk!"
        menu: 
            "Honk?":
                rg "Honk! Hoonk!"
            "Hoonk?":
                rg "Hoonk!!!"
                "You learned: Hoonk (Hello)"
                $ learned_words.append("Hoonk")
                $ meanings.append("Hello");
    call screen show_location(3)

default init_shoe_quest = False
default shoe_returned = False
default have_shoe = True
default have_candy = False # need candy to feed the kids

label shoe:
    scene main street
    show shoes goose

    if not init_shoe_quest:
        sg "Hoonk?"
        call screen duolingo
        mc "[final_sentence]"

        if final_sentence == "Hoonk ":
            sg "Hoonk... Honk honk honk. Honk."
            "The goose points at its singular shoe sadly."
            sg "Honk honk honk, hank.... Hank!"

            menu: 
                "Hank?":
                    "The goose gestures in the direction of the park."
                    sg "Honk honk! Hank.... hank...."

            $ init_shoe_quest = True
        else:
            sg "Honk?"
    elif not shoe_returned:
        sg "Honk.... hank.... hank...."

        menu:
            "Return the shoe" if have_shoe:
                "The goose lights up."
                sg "Honk?? Honk honk!! Hank!!"
                sg "Hank honk honk honk!"
                
                "You learned: Hank (Return)"
                $ learned_words.append("Hank")
                $ meanings.append("Return")

                sg "Honk! Honk, honk."
                "The goose takes its shoe off and hands you a piece of candy."
                sg "Honk hik."
                $ have_candy = True
            "Come back later":
                pass
    else:
        sg "Hoonk!"
    call screen show_location(3)

default met_thief = False

label thief:
    scene park
    show thief goose
    tg "Hoonk? Honk!"

    if not met_thief:
        call screen duolingo 
        mc "[final_sentence]"

        if final_sentence == "Hoonk ":
            tg "Hoonk. Honk honk, honk."
            $ met_thief = True
        else: 
            tg "Honk?"
            call screen show_location(4)
    
    menu: 
        "Point at the shoe" if init_shoe_quest:
            tg "Honk!! Honk honk honk!!!!"

            call screen duolingo
            mc "[final_sentence]"

            if final_sentence == "Hok Hik Hack " or final_sentence == "Hik Hok Hack ":
                "The goose pauses and looks at you, surprised."
                tg "Hok hik... hack? Honk? Honk honk?"
                tg "Hack... honk honk honk. Hok hik hack..."
                "With a sigh, the goose gives you the shoe."
                tg "Hok hik hack."
                $ have_shoe = True
            else: 
                "The goose glares at you angrily, but its eyes look sad."
                "You think this goose looks somewhat lonely. Is that why it chose a life of crime?"
                
        "Come back later":
            "The goose looks kind of sad that you're leaving."
    call screen show_location(4)

default met_real_goose = False

label real:
    scene park
    show real goose
    if not met_real_goose:
        rlg "Hoonk."

        call screen duolingo
        mc "[final_sentence]"

        if final_sentence == "Hoonk ":
            rlg "Wow. You're getting the hang of this."
            rlg "Good job."
        else: 
            rlg "You know, it's really best practice to start your conversations off with 'hello.'"
        $ met_real_goose = True
    else:
        rlg "What's up."
    
    menu: 
        "You can speak?":
            rlg "Everyone speaks. These geese speak too, just in a different language."
        "Are you from Earth?":
            rlg "Yeah. What about it."
        "Why do you look so different from the other geese?":
            rlg "Are you calling me different because of how I look? That. is RACIST!"

    if "Hik" not in learned_words:
        rlg "I've been in your shoes before. It took me awhile to get accustomed to this place."
        rlg "Here, I'll teach you a word that you can use."
        
        "You learned: Hik (You)"
        $ learned_words.append("Hik")
        $ meanings.append("You")
    
    call screen show_location(4)

label friends:
    scene park
    show goose friends
    if "Hack" not in learned_words:
        cg1 "Honk! Hoonk!"
        cg2 "Hoonk!!"
        cg3 "Hoonk!!! Hoonk!!!!!"

        show screen duolingo 
        mc "[final_sentence]"

        if final_sentence == "Hoonk ":
            cg1 "Hoonk!! Honk honk honk!"
            cg2 "Honk! Honk!"
            cg3 "Honk-tuah!"
            "The three geese link wings and happily jump around together."
            cg1 "Hack! Hack!"
            cg2 "Honk honk! Hack!!"
            cg3 "Hack, hack! Hik, hik, hok, hack!"
            "You learned: Hack (Friends)"
            $ learned_words.append("Hack")
            $ meanings.append("Friends")
        else:
            cg1 "Honk..? Honk honk honk?"
            cg2 "Honk..."
            cg3 "Honk-tuah!"
        show screen show_location(4)
    
    cg1 "Hack! Hack! Hack!"
    cg2 "Honk! Honk! Honk!"
    cg3 "Honk-tuah!"

    menu:
        "Offer the candy" if have_candy:
            "The three geese gasp and whip their heads in your direction."
            "They all start honking wildly."
            menu: 
                "See who wants the candy":
                    "You dangle the candy in front of them."
                    cg1 "Hok! Hok!!"
                    cg2 "Hok!!!! Hok!!!!!"
                    cg3 "Hok!! Hok-tuah!"

                    "You learned: Hok (Me)"
                    $ learned_words.append("Hok")
                    $ meanings.append("Me")

                    $ night_trigger = True

                    menu:
                        "Who do you give the candy to?"

                        "Child Goose 1":
                            pass
                        "Child Goose 2":
                            pass
                        "Child Goose 3":
                            pass
                    
                    "You throw the candy and all three geese start wrestling for it."
        "Come back later":
            pass
    show screen show_location(4)


label rest:
    scene hill entrance day
    "It's been a long day on this new planet. You decide to take a rest..."

    scene intro10 with dissolve

    "As you sit down and close your eyes, you can't help but miss home."
    "You've met plenty of interesting characters. Monologue"
    "You wonder if you'll ever be able to leave this unfamiliar place."

    scene hill entrance night 

    "ok its night now"
    $ night_trigger = False
    $ nighttime = True
    call screen show_location(2)    



