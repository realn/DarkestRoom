
define lookedAround = False
define lookedAtBed = False
define lookedUnderBed = False
define lookedAtVial = False
define takenVial = False
    
label lb_entrence_bed_look:
    menu:
        "Look.."
        
        "..around.":
            "You see not too small, simple, rectangular room around you. Beside the bed, opposite from it, there's a desk, and on the left wall you see a sturdy looking door." 
            $ lookedAround = True
        
        "..at the bed.":
            "This is a simple, metal bed placed beside the wall. It isn't much comfortable, but can be used to sleep. There is empty space under it."
            $ lookedAtBed = True
        
        "..under the bed." if lookedAtBed:
            m "What's this?"
            "You see a small, broken, glass object laying under the bed."
            $ lookedUnderBed = True
                    
        "..at nothing.":
            call lb_look_noop
    
    return
    
label lb_entrence_bed_use:
    menu:
        "Use.."
        
        "..your hand to take the vial from under the bed." if lookedUnderBed and 'vial' not in inv_items:
            call lb_entrence_bed_takeviel
        
        "..nothing":
            call lb_use_noop
            
    return
    
label lb_entrence_bed_walk:
    menu:
        "Walk.."
        
        "..to the door." if lookedAround:
            call lb_walkto_entrence_door
        
        "..nowhere.":
            call lb_walk_noop
            
    return
    
label lb_entrence_bed_takeviel:
    "You have taken the vial, and put into your pocket."
    python:
        global inv_items
        inv_items['vial'] = '..broken vial'
        takenVial = True
    return
    
