lineA="[Welcome to the tutorial. The text in each gameplay section will feature certain objects that you can interact with. They will be surrounded by square brackets]"
lineB="[To utilise the ‘Examine’ command, type ‘examine obj’, with the letters ‘obj’ replaced by the object you want to examine. For example - ‘examine key’. You will receive a short description of the object.]"
lineC="[To utilise the ‘Pick’ command, type ‘pick obj’, with the letters ‘obj’ replaced by the object you want to pick up. For example - ‘pick key’. You will add the object to your inventory]"
lineD="[To utilise the ‘inventory’ command, type ‘inventory’. You will be able to see the objects you have in your inventory.]"
screenTut1=[lineA,lineB,lineC,lineD]

lineE="[To utilise the ‘Use’ command, type ‘use obj1’ or ‘use obj1 obj2’, with the letters obj1 and obj2 replaced by the objects that you want to use. The form ‘use obj1 obj2’ will result in obj1 being used on obj2, for example ‘use key door’ will result in the key being used on the door.]"
lineF="[Please note that sometimes objects may be hidden inside other objects, and as such will not be immediately visible. Make sure to examine all object carefully, and choose the ‘use’ button on objects frequently to see what what can be done with them - it might not be obvious in the first instance]"
lineG="[To view these instructions again, type ‘tutorial’ in the commands section.]"
lineH="[Best of luck - and glory to Admiral Radius!]"
screenTut2=[lineE,lineF,lineG,lineH]




from screen import *
from gameplay_text import *

def displayPuzzleText(room):
    for i in room:
        print(i)
        print()

def initialHeader():
    ClearScreen()
    header2()
    print()

def exit_command():
    print("Press Enter to return")
    input()

def display_commands():
    print("What do you do?")
    print("[Commands: examine, pick, use, inventory, tutorial, quit]")

def examine_command(command,room_items):
    command=command.split(" ")
    if len(command)==1:
        initialHeader()
        print("Sorry, you have to follow up the examine command with a noun.")
        print("For example: examine key")
        print()
        exit_command()
    else:
        itemSelected=Item
        correctInput=False
        for i in room_items:
            if i.name==command[1]:
                itemSelected=i
                correctInput=True
        if correctInput:
            initialHeader()
            print(f"Chosen Item: {itemSelected.name}")
            print()
            print(itemSelected.descr)
            print()
            exit_command()
        else:
            initialHeader()
            print("Sorry, we don't recognise an item with that name.")
            print()
            exit_command()

def pick_command(command,room_items):
    command=command.split(" ")
    if len(command)==1:
        initialHeader()
        print("Sorry, you have to follow up the examine command with a noun.")
        print("For example: pick key")
        exit_command()
    else:
        itemSelected=Item
        correctInput=False
        for i in room_items:
            if i.name==command[1]:
                itemSelected=i
                correctInput=True
        if correctInput:
            initialHeader()
            print(f"You are trying to get: {itemSelected.name}")
            if itemSelected.pick==True:
                inventory.addItem(itemSelected)
                print()
                print("You have successfully picked up this item.")
                print()
                exit_command()
            else:
                print("Sorry, you can't pick that up.")
                print()
                exit_command()
        else:
            initialHeader()
            print("Sorry, we don't recognise an item with that name.")
            print()
            exit_command()

def inventory_command():
    inventory_looping=True
    while inventory_looping:
        initialHeader()
        print("INVENTORY CONTENTS")
        print()
        if not inventory.inventory:
            print("Your inventory is currently empty.")
            print()
            exit_command()
            inventory_looping=False
        else: 
            print("You currently have the following items in your inventory:")
            for i in inventory.inventory:
                print(f"{i.name}")
            print()
            print("Type name of item to get its description, or press Enter to continue")
            descr=input().lower()
            for i in inventory.inventory:
                if descr==i.name:
                    initialHeader()
                    print(f"Chosen Item: {i.name}")
                    print()
                    print(f"Item Description: {i.descr}")
                    print()
                    exit_command()
                else:
                    inventory_looping=False

# BUG_REPORT: Currently allows you to use item not in inventory
# BUG_REPORT: No error handling for situation where user selects more than two items
def use_command(command,room_items):
    command=command.split(" ")
    if len(command)==1:
        initialHeader()
        print("Sorry, you have to follow up the use command with one or two nouns.")
        print()
        print("For example: use candle")
        print("For example: use key door")
        print()
        exit_command()
    else:
        itemSelected=Item
        item2Selected=Item
        correctInput=False
        correctInput2=False

        if len(command)==2:
            for i in room_items:
                if i.name==command[1]:
                    itemSelected=i
                    correctInput=True
            if correctInput:
                initialHeader()
                print(f"You are trying to use: {itemSelected.name}")
                print()
                print(itemSelected.item_use["self"])
                if itemSelected.item_used_alone==False:
                    itemSelected.item_used_alone=True
                print()
                exit_command()
                
        elif len(command)==3:
            for i in room_items:
                if i.name==command[1]:
                    itemSelected=i
                    correctInput=True
                        
                if i.name==command[2]:
                    item2Selected=i
                    correctInput2=True
                    
            if correctInput==True and correctInput2==True:
                key_value=-1
                initialHeader()
                print(f"You are trying to use {itemSelected.name} with {item2Selected.name}")
                print()
                for key in itemSelected.item_use.keys():
                    if key==item2Selected.name:
                        key_value=key
                if key_value != -1:
                    print(itemSelected.item_use[key_value])
                    if itemSelected.item_used_with_otherItem==False:
                        itemSelected.item_used_with_otherItem=True
                    if item2Selected.item_used_with_otherItem==False:
                        item2Selected.item_used_with_otherItem=True
                    print()
                    exit_command()
            else:
                print("Sorry, one of these items does not exist!")
                print()
                exit_command()

def dunno_command():
    initialHeader()
    print("Sorry, I don't recognise that command!")
    print()
    print("Please try 'examine','pick','inventory', 'use' 'tutorial' or 'quit'")
    print()
    exit_command()

# Note: Exit condition should always be at the end.
# TO DO: Add a tutorial option
def puzzle_room(room,room_items):
    looping=True
    while looping:
        initialHeader()
        displayPuzzleText(room)
        print()
        display_commands()
        command=input().lower()
        if "examine" in command:
            examine_command(command,room_items)
        elif "pick" in command:
            pick_command(command,room_items)
        elif command=="inventory":
            inventory_command()
        elif "use" in command:
            use_command(command,room_items)
        else:
            dunno_command()

def dialogueChoices(dialogue):
    looping=True
    while looping:
        selectedIndex=0
        ClearScreen()
        initialHeader()
        for i in range(0,len(dialogue)-1):
            print(dialogue[i][0])
        print(dialogue[len(dialogue)-1])
        print()

        # Note: Add error checking here for ints
        option=intChecker("Please select your dialogue option: ")
        if option<=len(dialogue)-1:
            if option==0:
                ClearScreen()
                initialHeader()
                looping=False
                break
            else:
                ClearScreen()
                initialHeader()
                for i in range(0,len(dialogue)):
                    if option==i:
                        selectedIndex=i-1
                        break
                print(dialogue[selectedIndex][0])
                print()
                for i in range(1,len(dialogue[selectedIndex])):
                    print(dialogue[selectedIndex][i])
                    input()
        else:
            print("Sorry, the number must be within the range of options provided.")
            print("Please press Enter and try again.")
            input()

def intChecker(message):
    while True:
        try:
            userInput=int(input(message))
        except ValueError:
            ClearScreen()
            initialHeader()
            print("Sorry, you have to type in a number.")
            print()
            continue
        else:
            return userInput
            break


def removeFromScene(object, location):
    if object in location:
        location.remove(object)


def addToScene(object, location):
    if object not in location:
        location.append(object)  


def puzzleNavigation(puzzle_text, puzzle_items):
    initialHeader()
    displayPuzzleText(puzzle_text)
    print()
    display_commands()
    command=input().lower()
    if "examine" in command:
        examine_command(command,puzzle_items)
    elif "pick" in command:
        pick_command(command,puzzle_items)
    elif command=="inventory":
        inventory_command()
    elif "use" in command:
        use_command(command,puzzle_items)
    elif command=="tutorial":
        ClearScreen()
        display(screenTut1)
        display(screenTut2)
        ClearScreen()
    elif command=="quit":
        ClearScreen()
        initialHeader()
        print()
        print("[Thank you for participating in the Chronosia Industries Cadet Interactive Experience.]")
        input("Please press Enter again to quit.")
        quit()
    else:
        dunno_command()

def addItemEverywhere(item, location_items):
    addToScene(item, inventory.inventory)
    for i in location_items:
        addToScene(item, i)

def removeItemEverywhere(item, location_items):
    removeFromScene(item, inventory.inventory)
    for i in location_items:
        removeFromScene(item, i)

def screensInRange(totalScreenList, low, high):
    for i in range(low, high+1):
        display(totalScreenList[i])

