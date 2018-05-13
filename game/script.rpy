# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Me")

define bLookedAround = False
define bStoodUp = False

define inv_items = {}

define room = ""
define place = ""
define actLookLb = ""
define actUseLb = ""
define actWalkLb = ""

init python:

    def getLookLabel():
        return "lb_" + room + "_" + place + "_look"
    
    def getUseLabel():
        return "lb_" + room + "_" + place + "_use"
        
    def getWalkLabel():
        return "lb_" + room + "_" + place + "_walk"

    def setPlaceActions():
        global actLookLb
        global actUseLb
        global actWalkLb
        actLookLb = getLookLabel()
        actUseLb = getUseLabel()
        actWalkLb = getWalkLabel()

# The game starts here.

label start:

    show darkroom with fade

    "..."
    
    "You slowly opened your eyes."
    
    m "... Ouch, what the hell..."
    
    "Your body feelt stiff, like was not moved for some time."
    
    "You take some deep breaths to fully realize and grasp your surroundings."
    
    "You think, you can move again."
    
    "In the next moment you realized, you've been laying on an bed."

    menu:
        "Stand up":
            jump lb_stoodUp

            
label lb_stoodUp:
    
    "With some leftover stiffnes, you stood up."
    
    m "Where the hell, am I?"
    
    call lb_walkto_entrence_bed
    jump lb_actions

    
label lb_actions:
    menu:
        "Your actions are..."
        
        "Look...":
            call expression actLookLb
        "Look at item..." if len(inv_items) > 0:
            call lb_inv_list('look')
        "Use...":
            call expression actUseLb
        "Walk...":
            call expression actWalkLb
            
    jump lb_actions
 
label lb_look_noop:
    "You stare blankly into empty space."
    return

label lb_use_noop:
    "You stare at your hand flexing."
    return

label lb_walk_noop:
    "You move slightly your foot, like you wanted to go somewhere."
    return
