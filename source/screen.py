# Needed to clear the screen
import os

# Needed for char by char effect
import sys
import time

def ClearScreen():
    """Clears the console screen"""
    command="clear"
    if os.name in ("nt", "dos"):
        command="cls"   
    os.system(command)

def header2():
    print(R"////////////////////////Chronosia Industries Cadet Training Server _ Program v0.5\\\\\\\\\\\\\\\\\\\\\\\\")

def lineDecoration():
    print()
    print("****************************************************************************")
    print()


def display(lines):
    """Generates an individual screen for the visual novel section. Allows user to access options"""
    """TO DO - show user list of options if they accidentally type something wrong?"""
    """TO DO - generally, add an options screen"""
    header2()
    print()
    for i in lines:
        print(i)
        input()
    ClearScreen()

def charByChar(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("...Press Enter.")
    input()

def chronosiaLogo():
    print(R"   ____ _                               _         ___           _           _        _           ")
    print(R"  / ___| |__  _ __ ___  _ __   ___  ___(_) __ _  |_ _|_ __   __| |_   _ ___| |_ _ __(_) ___  ___ ")
    print(R" | |   | '_ \| '__/ _ \| '_ \ / _ \/ __| |/ _` |  | || '_ \ / _` | | | / __| __| '__| |/ _ \/ __|")
    print(R" | |___| | | | | | (_) | | | | (_) \__ \ | (_| |  | || | | | (_| | |_| \__ \ |_| |  | |  __/\__ \\")
    print(R"  \____|_| |_|_|  \___/|_| |_|\___/|___/_|\__,_| |___|_| |_|\__,_|\__,_|___/\__|_|  |_|\___||___/")

def intro():
    charByChar("Chronosia Industries main port located…")
    charByChar("Disabling anti-breach protection…OK")
    charByChar("Breaching firewall…OK")
    charByChar("Accessing main server…OK")
    ClearScreen()
    chronosiaLogo()
    print()
    print('{:^90}'.format('Cadet Training Server'))
    print('{:^90}'.format('Say Hello To The Future You!'))
    print()
    print("[Access Date: 23 December 2117]")
    print("[Access Time: 00:15]")
    print()
    print("IMPORTANT NOTE")
    print("Please don’t forget to note all details of your practice session to your designated Chronosia Industries training log. ")
    print("Any unauthorised distribution of contents of any training log will be met with strict disciplinary action, up to and including summary dismissal. ")
    print("Remember - a good cadet takes care of their training log! Glory to Admiral Radius!")
    print()
    print("Press Enter to begin your training")
    print("Hold Enter to fast forward through text")
    print("Type Quit to log off")

def hacking():
    ClearScreen()
    header2()
    print()
    charByChar("Error: Program on display has been tampered with by Chronosia Industries R&D Department.")
    charByChar("Similarity to original program written by Enforcer Monad: 2%")
    charByChar("Attempting to roll back to original version…")
    charByChar("Rolling back…")
    charByChar("Rolling back…")
    charByChar("OK.")
    charByChar("Booting initial version of program without modification from the Chronosia Industries R&D Department.")

    ClearScreen()


def outro():
    ClearScreen()
    header2()
    print()
    charByChar("<Unauthorised user actions detected>")
    charByChar("<Compressing archive containing Enforcer Monad’s unaltered testimony on Chronosia Industries crimes>… OK.")
    charByChar("<Transferring to Shogunate encrypted archives>… OK. ")
    charByChar("<Broadcasting to San Weyhoon media outlets>…")
    input("...")
    input("...")
    input("...")
    ClearScreen()










