from weightcalc import dungeoncalc, skillcalc, slayercalc

dungeon = dungeoncalc('58dfc909-be4a-497b-871e-a13f636d37f0', 1000)
skill = skillcalc('8805940', 221, 424)
slayer = slayercalc(713, 224, 20)

print (f"Your dungeon weight is {dungeon}")

print (f"Your skill weight is {skill}")

print (f"Your slayer weight is {slayer}")

print (f"Your total weight is {dungeon+skill+slayer}")