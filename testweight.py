from weightcalc import dungeoncalc, skillcalc, slayercalc
#owo
#welcome message thing 
print("Whelcome to HorseWeight!\nSince im bad at coding HorseWeight curently does not support api\nEnter your stats below:")

#inputs for the functions 
uuid = input("UUID: ")
f4comp = input("Floor 4 Completions: ")
acaciacol = input("Acacia Collection: ")
souls = input("Fairy Souls: ")
treasure = input("Large Treasure Fished: ")
eman = input("Tier 3 Endermen Killed: ")
petscore = input("Pet Score: ")
minslot = input("Minion Slots: ")

#omg functions?!
dungeon = dungeoncalc(str(uuid), int(f4comp))
skill = skillcalc(str(acaciacol), int(souls), int(treasure))
slayer = slayercalc(int(eman), int(petscore), int(minslot))

#prints your weight 
print (f"Your dungeon weight is {dungeon}")
print (f"Your skill weight is {skill}")
print (f"Your slayer weight is {slayer}")
print (f"Your total weight is {dungeon+skill+slayer}")
