# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character() # Narrator
define mc = Character("YOU") # Player
define ufog = Character("?") # UFO Duck


# The game starts here.

label start:

    # START OF THE INTRODUCTION

    scene intro1 # NEED: intro1.png - scene of you walking along a path surrounded by trees? I imagine walking thru the arboretum or smth like that vibe

    n "Another long day has passed. You breathe a sigh of relief that the day has finally come to an end."
    n "The sky has long since turned dark and the cold night wraps around your shoulders. But you're used to it."
    n "You fall into routine, your shoes following the worn and familiar path back to your home."

    scene intro2 # NEED: intro2.png - scene of you getting out the big bread. This can be a copy of intro1 just with the bread

    n "Carefully, you unwrap the loaf of bread that you've kept in your bag. You figure it can't hurt to have a small late night snack."
    n "It's from the new bakery that recently opened across your street."
    n "You stumbled upon it by accident, but apparently, crowds from all over the world have FLOCKED here to try it."
    n "Suddenly, you hear a strange sound in the distance."

    play sound "UFO_beep.mp3" # NEED

    mc "(Huh?)"

    scene intro3 # NEED: intro3.png - scene of you looking up at the UFO. The light from the spacecraft is shining down on you. 

    mc "?????"
    ufog "Quack quack quack quack."
    n "Before you have time to process it, you feel your skin start to heat up. The light from the strange carrier grows brighter and you can barely keep your eyes open."
    n "Slowly, the bread in your hand detaches and begins floating towards the spacecraft."
    n "Then, you feel your feet start to lift from the ground."

    scene intro4 # NEED: intro4.png - scene of you and your bread floating up to the UFO. a goose with sunglasses and a suit is controlling the ufo 

    mc "Hello???"
    ufog "Quack quack quack."
    mc "Help!!"

    scene black with dissolve

    n "You vision blurs and you find yourself unresponsive, passed out on the floor of the aircraft."
    n "The ground underneath you rattles and whirs."
    n "Time and reality contort into disfigured notions as you travel with your kidnapper..."

    scene intro5 # NEED: intro5.png - scene of you coming back down from the aircraft into a strange goose world. This can be a copy 
    # of intro4 but with a slightly diff bg (and no bread)

    n "When you open your eyes again, the world around you has changed."
    n "The space carrier gently places you back onto the ground and you take in the unfamiliar world around you..."
    n "...filled with..."
    n "...Geese?"

    # END OF THE INTRODUCTION

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    return
