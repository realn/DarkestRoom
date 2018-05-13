
label lb_inv_list(action='look'): 
    python:
        menu_inv_items = []
        for key, value in inv_items.iteritems():
            menu_inv_items.append([value, key])
        menu_inv_items.append(["Nothing", 'return'])

    $ res = renpy.display_menu(menu_inv_items)
    if res == 'return':
        return
    
    $ item_label = 'lb_' + res + '_' + action
    
    call expression item_label
    return
    
    
label lb_vial_look:
    "It a cylinder shaped, medical vial, broken in half.
     It has a label saying 'Subject XV-II'"
    return
    
