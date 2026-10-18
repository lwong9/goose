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

default acquired_items = []

# DUOLINGO SYSTEM 
default learned_words = ["Honk?"]
default meanings = ["???"]
default final_sentence = ""

init python:
    def submit_final_sentence(words):
        global final_sentence 
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
            background Frame("images/vocab_frame.png", 25, 25, 25, 25)
            ysize 500
            xpadding 20
            ypadding 20
            vbox: 
                xsize 500
                yalign 0.0          # Forces the vbox content to start at the very top
                spacing 10

                label "Known Words:" xalign 0.5
                for index in range(len(learned_words)):
                    text "[learned_words[index]], Meaning: [meanings[index]]" xalign 0.0 yalign 0.0
        frame:
            background Frame("images/speak_frame.png", 25, 25, 25, 25)
            xpadding 20
            ypadding 20
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
                        Return() 
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
    play music "audio/background_nm.mp3" volume 0.5

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
    
    stop music fadeout 1.0
    window hide
    pause 1.5

    play music "audio/background.mp3" volume 0.5
    show screen show_location(1)
    

# Custom tooltip
screen general_tooltip():
    # 1. Grab the active tooltip text from whatever the mouse is hovering over
    $ tooltip = GetTooltip()
    
    # 2. Only show the visual box if there is actual text to display
    if tooltip:
        text "[tooltip]":
            xalign 0.5 
            yalign 0.5
            color "#d1d1d1"
            outlines [
                # (4, "#40404061", 0, 0), 
                (2, "#40404089", 1, 1)     
            ]

# ALL LOCATIONS
# UFOG - HILL ENTRANCE - MAIN STREET - PARK
#          HILL          

default night_trigger = False
default nighttime = False
default met_friends = False

screen show_location(i):
    if i == 1: # (1) - UFO
        if nighttime:
            add "images/ufo night.jpg"
        else:
            add "images/ufo day.jpg"
        add "images/ufog idle.png"
        imagemap:
            ground "images/ufog idle.png"
            hotspot (852, 44, 260, 1003) action [Hide(), Play("sound", "audio/buttonclick.mp3"), Jump("guess")] tooltip "The goose that brought you here"
    elif i == 2: # (2) - HILL ENTRANCE
        timer 0.01 action If(night_trigger == True, true=Jump("rest"), false=None)
        if nighttime: 
            add "images/hill entrance night.jpg"
            imagemap: 
                ground "images/hill entrance night.jpg"
                hotspot (821, 408, 348, 335) action [Hide(), Play("sound", "audio/buttonclick.mp3"), Show("hill_screen")] tooltip "Push through the trees"
        else:
            add "images/hill entrance day.jpg"
            imagemap: 
                ground "images/hill entrance day.jpg"
                hotspot (821, 408, 348, 335) action [Hide(), Play("sound", "audio/buttonclick.mp3"), Show("hill_screen")] tooltip "Push through the trees"
            if met_friends and not have_candy:
                imagebutton:
                    idle "images/sparkle idle.png"
                    hover "images/sparkle hover.png"
                    align (0.9, 0.9)
                    tooltip "There is something in the foliage."
                    action [Play("sound", "audio/buttonclick.mp3"), Hide(), Jump("find_candy")] 
    elif i == 3: # (3) - MAIN STREET
        add "images/main street.jpg"
        imagebutton:
            idle Transform("images/rainbow goose.png", zoom=0.6)
            align (0.6, 0.75)
            tooltip "A rainbow goose."
            action [Hide(), Play("sound", "audio/buttonclick.mp3"), Jump("rainbow")]
        imagebutton:
            if shoe_returned:
                idle Transform("images/shoes goose happy.png", zoom=0.5)
            else:
                idle Transform("images/shoes goose.png", zoom=0.5)
            align (0.1, 0.4)
            tooltip "A goose with only one shoe."
            action [Hide(), Play("sound", "audio/buttonclick.mp3"), Jump("shoe")]

    elif i == 4: # (4) - PARK
        add "images/park.jpg"
        imagemap: 
            ground "images/park.jpg"
            hotspot (990, 549, 439, 262) action [Hide(), Play("sound", "audio/buttonclick.mp3"), Jump("friends")] tooltip "A group of geese friends."
        imagebutton:
            if have_shoe:
                idle Transform("images/thief goose happy.png", zoom=0.45)
            else:
                idle Transform("images/thief goose.png", zoom=0.45)
            align (0.25, 0.65)
            tooltip "A suspicious-looking goose."
            action [Hide(), Play("sound", "audio/buttonclick.mp3"), Jump("thief")]
        
        imagebutton:
            idle Transform("images/real goose.png", zoom=0.45)
            align (0.95, 0.85)
            tooltip "An interesting-looking goose."
            action [Hide(), Play("sound", "audio/buttonclick.mp3"), Jump("real")]
            
            
    else:
        text "Location not found"
    use general_tooltip()


    # calculate the next screens
    default right_i = i + 1
    default left_i = i - 1
    default i_max = 4
    default i_min = 1

    if nighttime:
        $ i_max = 2
       
    if not i == i_min:
        imagebutton:
            idle "images/left.png"
            hover "images/left_hover.png"
            xalign 0.05
            yalign 0.5
            action [Hide(), Play("sound", "audio/buttonclick.mp3"), Show("show_location", i=left_i)]
    if not i == i_max:
        imagebutton:
            idle "images/right.png"
            hover "images/right_hover.png"
            xalign 0.95
            yalign 0.5
            action [Hide(), Play("sound", "audio/buttonclick.mp3"), Show("show_location", i=right_i)]

    
    

screen hill_screen():
    if nighttime:
        add "images/stargazing.jpg"
        timer 0.01 action Play("music", "audio/stargaze.mp3")
        imagemap:
            ground "images/stargazing.jpg" 
            hotspot (1330, 222, 212, 763) action [Hide(), Play("sound", "audio/buttonclick.mp3"), Jump("stargaze")] tooltip "A goose that is staring at the stars."
            use general_tooltip()
    else:
        add "images/hill.jpg"
    imagebutton:
        idle "images/exit.png"
        hover "images/exit_hover.png"
        xalign 0.5
        yalign 0.95
        action [Hide(), Play("sound", "audio/buttonclick.mp3"), Show("show_location", i=2)]

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
    play sound "audio/honk3.mp3"
    mc "[final_sentence]"

    if final_sentence != "Hok Hank Hounk ":
        show ufog speak
        ufog "Honk?"
        show ufog idle
        "That didn't work. How should you tell it you want to go back home?"
        jump explore
    else:
        jump ending

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

        play sound "audio/word_shimmer.mp3"
        "You learned: Hounk (Earth)"
        
        $ learned_words.append("Hounk")
        $ meanings.append("Earth")
    play music "audio/background_nm.mp3" volume 0.5
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
                play sound "audio/word_shimmer.mp3"
                "You learned: Hoonk (Hello)"
                
                $ learned_words.append("Hoonk")
                $ meanings.append("Hello");
    call screen show_location(3)

default init_shoe_quest = False
default shoe_returned = False
default have_shoe = False
default have_candy = False # need candy to feed the kids

label shoe:
    scene main street
    show shoes goose

    if not init_shoe_quest:
        sg "Hoonk?"

        call screen duolingo
        mc "[final_sentence]"
        play sound "audio/honk3.mp3"

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
                hide shoes goose
                show shoes goose happy
                "The goose lights up."
                sg "Honk?? Honk honk!! Hank!!"
                sg "Hank honk honk honk!"
                
                play sound "audio/word_shimmer.mp3"
                "You learned: Hank (Return)"
                
                $ learned_words.append("Hank")
                $ meanings.append("Return")

                $ shoe_returned = True
                $ night_trigger = True # Now you may continue to night

            "Come back later":
                pass
    else:
        sg "Hoonk!"
    call screen show_location(3)

default met_thief = False

label thief:
    scene park
    if have_shoe:
        show thief goose happy
    else:
        show thief goose
    tg "Hoonk? Honk!"

    if not met_thief:
        call screen duolingo 
        mc "[final_sentence]"
        play sound "audio/honk3.mp3"

        if final_sentence == "Hoonk ":
            tg "Hoonk. Honk honk, honk."
            $ met_thief = True
        else: 
            tg "Honk?"
            call screen show_location(4)
    if not have_shoe:
        menu: 
            "Point at the shoe" if init_shoe_quest:
                tg "Honk!! Honk honk honk!!!!"

                call screen duolingo
                mc "[final_sentence]"
                play sound "audio/honk3.mp3"

                if final_sentence == "Hok Hik Hack " or final_sentence == "Hik Hok Hack ":
                    "The goose pauses and looks at you, surprised."
                    tg "Hok hik... hack? Honk? Honk honk?"
                    tg "Hack... honk honk honk. Hok hik hack..."
                    
                    hide thief goose
                    show shoe:
                        xalign 0.5
                        yalign 0.5
                    
                    "With a sigh, the goose gives you the shoe."
                    tg "Hok hik hack."

                    
                    "Acquired: Shoe"
                    hide shoe
                    $ acquired_items.append(["Shoe", "images/shoe.png"])
                    $ have_shoe = True
                else: 
                    "The goose glares at you angrily, but its eyes look sad."
                    "You think this goose looks somewhat lonely. Is that why it chose a life of crime?"
                    "Maybe you should try to befriend it."
                    
            "Come back later":
                "The goose looks kind of sad that you're leaving."
    else:
        tg "Hik hok hack!"
    call screen show_location(4)

default met_real_goose = False
default real_goose_questions = []

label real:
    scene park
    show real goose
    if not met_real_goose:
        rlg "Hoonk."

        call screen duolingo
        mc "[final_sentence]"
        play sound "audio/honk3.mp3"

        if final_sentence == "Hoonk ":
            rlg "Wow. You're getting the hang of this."
            rlg "Good job."
        else: 
            rlg "You know, it's really best practice to start your conversations off with 'hello.'"
        $ met_real_goose = True
    else:
        rlg "What's up."

    jump ask_real_questions

label ask_real_questions:
    scene park
    show real goose

    menu: 
        set real_goose_questions

        "You can speak?":
            rlg "Everyone speaks. These geese speak too, just in a different language."
            jump ask_real_questions
        "Are you from Earth?":
            rlg "Yeah. What about it."
            jump ask_real_questions
        "Why do you look so different from the other geese?":
            rlg "Are you calling me different because of how I look? That. is RACIST!"
            jump ask_real_questions

    if "Hik" not in learned_words:
        rlg "I've been in your shoes before. It took me awhile to get accustomed to this place."
        rlg "Here, I'll teach you a word that you can use."
        
        play sound "audio/word_shimmer.mp3"
        "You learned: Hik (You)"
        
        $ learned_words.append("Hik")
        $ meanings.append("You")
    
    call screen show_location(4)

default gave_candy = False
label friends:
    scene park
    show goose friends
    if "Hack" not in learned_words:
        cg1 "Honk! Hoonk!"
        cg2 "Hoonk!!"
        cg3 "Hoonk!!! Hoonk!!!!!"

        call screen duolingo 
        mc "[final_sentence]"
        play sound "audio/honk3.mp3"

        if final_sentence == "Hoonk ":
            cg1 "Hoonk!! Honk honk honk!"
            cg2 "Honk! Honk!"
            cg3 "Honk-tuah!"
            "The three geese link wings and happily jump around together."
            cg1 "Hack! Hack!"
            cg2 "Honk honk! Hack!!"
            cg3 "Hack, hack! Hik, hik, hok, hack!"

            play sound "audio/word_shimmer.mp3"
            "You learned: Hack (Friends)"
            
            $ learned_words.append("Hack")
            $ meanings.append("Friends")
            $ met_friends = True
        else:
            cg1 "Honk..? Honk honk honk?"
            cg2 "Honk..."
            cg3 "Honk-tuah?"
        call screen show_location(4)
    
    cg1 "Hack! Hack! Hack!"
    cg2 "Honk! Honk! Honk!"
    cg3 "Honk-tuah!"

    if not gave_candy:
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

                        play sound "audio/word_shimmer.mp3"
                        "You learned: Hok (Me)"
                        
                        $ learned_words.append("Hok")
                        $ meanings.append("Me")

                        menu:
                            "Who do you give the candy to?"

                            "Child Goose 1":
                                pass
                            "Child Goose 2":
                                pass
                            "Child Goose 3":
                                pass
                        
                        "You throw the candy and all three geese start wrestling for it."
                        $ gave_candy = True
            "Come back later":
                "These geese seem distracted. Maybe you should find something that grabs their attention."
    call screen show_location(4)


label rest:
    scene hill entrance day
    stop music fadeout 2.0

    "It's been a long day on this new planet. You decide to take a rest..."

    scene intro10 with dissolve

    "As you sit down and close your eyes, you can't help but miss home."
    "You've met plenty of interesting characters. Monologue"
    "You wonder if you'll ever be able to leave this unfamiliar place."

    scene hill entrance night 

    play music "audio/background_nm.mp3" volume 0.5

    "ok its night now"
    $ night_trigger = False
    $ nighttime = True
    call screen show_location(2)    

label find_candy:
    scene hill entrance day 
    show candy:
        xalign 0.5
        yalign 0.5
    "You find a piece of candy. Who put this here?"
    "Acquired: Candy"
    hide candy
    $ have_candy = True
    call screen show_location(2)

label ending:
    scene ufo night
    stop music fadeout 2.0
    show ufog speak
    ufog "Hik hank hounk?"
    ufog "Honk honk honk!"

    play music "audio/stargaze.mp3" volume 0.5

    scene end1 with fade
    "The goose that brought you here smiles."
    "Somehow, you seem to tell that it is trying to say \'Why didn\'t you say that earlier?\'"
    ufog "Honk honk."

    scene end2 with dissolve
    "The goose lets you into the spacecraft."
    "Finally, it seems like your time here has come to an end."

    scene end3 with dissolve
    "As the goose flies you back to Earth, you reminisce on the words you\'ve learned and the geese you\'ve met."
    "Will you ever return to this world? You\'re not sure."
    "Now it is time to go back to your familiar life."
    "But maybe the real familiar... were the friends we made along the way."
    "Heh."

    return
    