import random

a = input('username: ')
b = input('profile: ')

if a == 'HorseScary' and b == 'papaya':
    print(f"{a}'s profile {b} has a weight of {random.randint(20000,50000)}")

else:
    print(f"{a}'s profile {b} has a weight of {random.randint(1000,20000)}")