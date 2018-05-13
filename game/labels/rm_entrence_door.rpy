
label lb_entrence_door_look:
    menu:
        "Look.."
    
        "..at nothing.":
            call lb_look_noop
    
    return
    
    
label lb_entrence_door_use:
    menu:
        "Use.."
        
        "..nothing":
            call lb_use_noop
            
    return
    
label lb_entrence_door_walk:
    menu:
        "Walk.."
        
        "..to the bed.":
            call lb_walkto_entrence_bed
        
        "..nowhere.":
            call lb_walk_noop
            
    return
    