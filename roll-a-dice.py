import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

response=input("Press y to roll and n to exit: ")
no=random.randint(1,6)
while response=='y':
    print(no)
    if no==1:
        print(DICE_ART[0])
    if no==2:
        print(DICE_ART[1])
    if no==3:
        print(DICE_ART[2])
    if no==4:
        print(DICE_ART[3])
    if no==5:
        print(DICE_ART[4])
    if no==6:
        print(DICE_ART[5])
    
    response=input("Press y to roll again and n to exit: ")
  
    




