#dungeon weight calculations
def dungeoncalc (uuid, f4comp):

    #dungeon weight multiplier 
    multi = uuid[0]
    multi = (int(multi)/10) + 1
    
    #returns dungeon weight 
    return(f4comp * multi)

#skill weight calculations 
def skillcalc (acaciacol, souls, treasure):
    #if there arn't 3 digets in acacia collection than it uses first diget 
    if len (acaciacol) >= 3:
        multi = (int(acaciacol[2]) * .01) + 2
    else:
        multi = (int(acaciacol[1]) * .01) + 2

    #returns skill weight 
    return ((souls + treasure) * multi)

#slayer weight calculations 
def slayercalc (emen, petscore, minslot):
    #multiplier creation 
    multi = minslot * .01

    #if the miltiplier is too small it makes it bigger 
    if multi <= 1:
        multi += 1
    #returns slayer weight 
    return ((emen+petscore) * multi) 