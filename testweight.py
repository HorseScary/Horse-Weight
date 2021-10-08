from weightcalc import dungeoncalc, skillcalc, slayercalc

uuid = input("UUID: ")
f4comp = input("Floor 4 Completions: ")
acaciacol = input("Acacia Collection: ")
souls = input("Fairy Souls: ")


dungeon = dungeoncalc(uuid, f4comp)
skill = skillcalc('8805940', 221, 424)
slayer = slayercalc(713, 224, 20)

print (f"Your dungeon weight is {dungeon}")

print (f"Your skill weight is {skill}")

print (f"Your slayer weight is {slayer}")

print (f"Your total weight is {dungeon+skill+slayer}")