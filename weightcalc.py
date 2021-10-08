def dungeoncalc (uuid, f4comp):
    multi = int(uuid[1])
    multi = (multi/10) + 1
    return(f4comp * multi)

def skillcalc (acaciacol, souls, treasure):
    if len (acaciacol) >= 3:
        multi = (int(acaciacol[3]) * .01) + 2
    else:
        multi = (int(acaciacol[1]) * .01) + 2
    return ((souls + treasure) * multi)


def slayercalc (emen, petscore, minslot):
    multi = minslot * .01
    if multi <= 1:
        multi += 1
    return ((emen+petscore) * multi) 