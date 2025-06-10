#################################################### SETUP #############################################################
# import modules/packages
import random, sys, os, threading, time, keyboard, pygame, lines

# sound effects
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
folder = "media"
box = pygame.mixer.Sound(os.path.join(folder, 'box.wav'))
calendar = pygame.mixer.Sound(os.path.join(folder, 'calendar.wav'))
door_close = pygame.mixer.Sound(os.path.join(folder, 'door_close.wav'))
door_creak = pygame.mixer.Sound(os.path.join(folder, 'door_creak.wav'))
door_locked = pygame.mixer.Sound(os.path.join(folder, 'door_locked.wav'))
door_open = pygame.mixer.Sound(os.path.join(folder, 'door_open.wav'))
error = pygame.mixer.Sound(os.path.join(folder, 'error.wav'))
footsteps = pygame.mixer.Sound(os.path.join(folder, 'footsteps.wav'))
gasp = pygame.mixer.Sound(os.path.join(folder, 'gasp.wav'))
grenade = pygame.mixer.Sound(os.path.join(folder, 'grenade.wav'))
heartbeat = pygame.mixer.Sound(os.path.join(folder, 'heartbeat.wav'))
key_clatter = pygame.mixer.Sound(os.path.join(folder, 'key_clatter.wav'))
locker_close = pygame.mixer.Sound(os.path.join(folder, 'locker_close.wav'))
locker_locked = pygame.mixer.Sound(os.path.join(folder, 'locker_locked.wav'))
locker_open = pygame.mixer.Sound(os.path.join(folder, 'locker_open.wav'))
paper = pygame.mixer.Sound(os.path.join(folder, 'paper.wav'))
running = pygame.mixer.Sound(os.path.join(folder, 'running.wav'))
slash = pygame.mixer.Sound(os.path.join(folder, 'slash.wav'))
success = pygame.mixer.Sound(os.path.join(folder, 'success.wav'))
zip_up = pygame.mixer.Sound(os.path.join(folder, 'zip_up.wav'))

# some variables
weights = [35, 35, 10, 20]
dialogueSpeed = 0.04
endingSpeed = 0.06
dotSpeed = 0.6
optionSpeed = 0.01
pauseDialogue = 0.5
pauseTransition = 1
optionError = "..Please select one of the options.\n\n"
inventory = []
endings = []
largeBox = ["itemRubberDuck", "itemChewedHomework", "itemFreshCake", "itemGrenade"]
gameRunning = False

# set text behaviour
def dialogue(line, parameterSpeed, parameterPause):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(parameterSpeed)
    time.sleep(parameterPause)

# "clear" for pycharm
def clear():
    if os.name == 'nt':
        _ = os.system('cls')

# key events
def keyEvents():
    while True:
        key = keyboard.read_key()
        if key == "+":
            global dialogueSpeed, endingSpeed, dotSpeed, optionSpeed
            dialogueSpeed = 0.005
            endingSpeed = 0.03
            dotSpeed = 0.3
            optionSpeed = 0.005
            continue
        if key == "-":
            dialogueSpeed = 0.04
            endingSpeed = 0.06
            dotSpeed = 0.6
            optionSpeed = 0.01
            continue

# set up options
def chooseOption(numberOfOptions):  # teacher supplied
    option = 0
    while option < 1 or option > numberOfOptions:
        askOption = "\n   1 to " + str(numberOfOptions) + " -> "
        dialogue(askOption, dialogueSpeed, 0)

        option = input()
        if option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6':
            option = 0
        if option == '1' or option == '2' or option == '3' or option == '4' or option == '5' or option == '6':
            option = int(option)
        return option

################################################# USER INFO ############################################################
def userInfo():
    # dialogue
    clear()
    askUserName = "Enter your name.\n"
    userError = "..Please enter something.\n\n"

    # call function
    dialogue(askUserName, dialogueSpeed, 0)

    # store as username
    global username
    username = input("   ")
    time.sleep(pauseTransition)

    # jump scene
    if username == "":
        clear()
        dialogue(userError, dialogueSpeed, pauseTransition)
        userInfo()
    else:
        clear()
        gameExplanation()

############################################## GAME EXPLANATION ########################################################
def gameExplanation():

    # call functions
    dialogue(lines.expl_line1, dialogueSpeed, pauseDialogue)
    dialogue(lines.expl_line2, dialogueSpeed, pauseDialogue)
    dialogue(lines.expl_line3, dialogueSpeed, pauseDialogue)
    dialogue(lines.expl_line4, 0, 0)
    dialogue(lines.expl_line5, 0, pauseTransition)
    skipIntro()

################################################ INTRODUCTION ##########################################################
def skipIntro():
    # dialogue
    skipLine = "Skip introduction? Y/N"
    skipError = "..Please enter Y or N.\n\n"

    # call function
    dialogue(skipLine, dialogueSpeed, 0)

    # store as skip
    skip = input("\n   ")
    skip = skip.upper()
    time.sleep(pauseTransition)

    # jump scene
    if skip == "N" or skip == "NO":
        clear()
        introScene()
    elif skip == "Y" or skip == "YES":
        clear()
        entryScene()
    else:
        clear()
        dialogue(skipError, dialogueSpeed, pauseTransition)
        skipIntro()

def introScene():
    pygame.mixer.music.load(os.path.join(folder, 'intro_theme.mp3'))
    pygame.mixer.music.play(-1)

    # dialogue
    introLine1 = "It's a calm, sunny afternoon, and you decide to walk home with a friend after a long day of " \
                 "school.\033[0;49m You both ponder about assignments and upcoming tests, while occasionally teasing " \
                 "each other and such.\033[0;49m Just then, you remember the homework that is due soon.\033[0;49m You " \
                 "ask your friend if they want to stop by a cafe and work on it with you.\n\n"
    introLine2 = "Your friend hesitates for a moment, stopping in their tracks, before beginning to rummage through " \
                 "their bag.\033[0;49m You see their face gradually become worried.\n\n"
    introLine3 = '"Shoot.\033[0;49m Did I forget my homework at school?"\n\n'
    introLine4 = "You can see them panicking a bit.\033[0;49m You aren't exactly in a rush, so you wouldn't really " \
                 "mind going back.\033[0;49m How about walking back together?\n\n"
    introLine5 = '"No,\033[0;49m I have an important family event today, I REALLY need to go."\n\n'
    introLine6 = "I mean, it's just homework, right?\033[0;49m It's not that big of a deal.\033[0;49m Surely Mr. W " \
                 "wouldn't mind it if you missed it by just one day.\033[0;49m But then again, it is worth 90% of " \
                 "your final grade..\n\n"
    introLine7 = "Since you don't have any other plans and you're practically almost finished with your homework, " \
                 "you offer to go back and get their homework for them.\033[0;49m They thank you profusely before you " \
                 "go both your separate ways."

    # call functions
    footsteps.play()
    dialogue(introLine1, dialogueSpeed, pauseDialogue)
    dialogue(introLine2, dialogueSpeed, pauseDialogue)
    dialogue(introLine3, dialogueSpeed, pauseDialogue)
    dialogue(introLine4, dialogueSpeed, pauseDialogue)
    dialogue(introLine5, dialogueSpeed, pauseDialogue)
    dialogue(introLine6, dialogueSpeed, pauseDialogue)
    footsteps.play()
    dialogue(introLine7, dialogueSpeed, pauseTransition)

    # jump scene
    clear()
    entryScene()

################################################### ENTRY ##############################################################
def entryScene():
    pygame.mixer.music.load(os.path.join(folder, 'main_theme.mp3'))
    pygame.mixer.music.play(-1)

    # dialogue
    entryLine1 = "You're back standing in front of the school.\033[0;49m It's only been a little while since you've " \
                 "left, but it seems that everyone has gone home already.\033[0;49m It's eerily quiet here.\n\n"

    # call functions
    dialogue(entryLine1, dialogueSpeed, pauseTransition)
    entryOption()

def entryOption():
    # dialogue
    entryOptions = ["   (1) Search inside the school.\n",
                    "   (2) Search the schoolyard.\n",
                    "   (3) Go home.\n"]
    entryLine2 = "\nNevertheless, you swallow back that off-feeling, knowing that your friend is depending on you."

    # call functions
    for line in entryOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(3)
    time.sleep(pauseTransition)
    if option == 1:
        footsteps.play()
        dialogue(entryLine2, dialogueSpeed, pauseTransition)
        clear()
        schoolScene()
    elif option == 2:
        footsteps.play()
        dialogue(entryLine2, dialogueSpeed, pauseTransition)
        clear()
        yardScene()
    elif option == 3:
        clear()
        exitScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        entryOption()

################################################## SCHOOL ##############################################################
def schoolScene():
    # dialogue
    schoolLine1 = "The sounds of the creaking school door echoes through the empty hallways.\033[0;49m There doesn't " \
                  "seem to be anyone as you look around, but all of the lights are still on.\033[0;49m Surely there " \
                  "should be some lingering teachers or students around?\n\n"

    # call functions
    door_creak.play()
    dialogue(schoolLine1, dialogueSpeed, pauseTransition)
    schoolOption()

def schoolOption():
    # dialogue
    schoolOptions = ["   (1) Search the homeroom class.\n",
                     "   (2) Search the staff room.\n",
                     "   (3) Search your friend's locker.\n",
                     "   (4) Search the schoolyard.\n",
                     "   (5) Leave the school.\n",
                     "   (6) Go to the bathroom?\n"]
    schoolLine2 = "\nAll the bathrooms are locked after school hours.\033[0;49m However, there's always an open one " \
                  "at the very end of the campus, but none of the staff actually know about it.\n\n"
    schoolLine3 = "You're positive your friend wouldn't leave their homework in there, yet you really wanted to go " \
                  "for some reason."

    # call functions
    for line in schoolOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(6)
    time.sleep(pauseTransition)
    if option == 1:
        clear()
        classScene()
    elif option == 2:
        clear()
        staffScene()
    elif option == 3:
        clear()
        lockerScene()
    elif option == 4:
        clear()
        yardScene()
    elif option == 5:
        clear()
        entryScene()
    elif option == 6:
        dialogue(schoolLine2, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(schoolLine3, dialogueSpeed, pauseTransition)
        clear()
        bathroomScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        schoolOption()

################################################### CLASS ##############################################################
def classScene():
    # dialogue
    classLine1 = "As you look around the classroom, you don't see anyone except for some leftover schoolbags.\033[" \
                 "0;49m Strange.\n\n"

    # call functions
    door_open.play()
    dialogue(classLine1, dialogueSpeed, pauseTransition)
    classOption()

def classOption():
    # dialogue
    classOptions = ["   (1) Search the student desks.\n",
                    "   (2) Look at the floor.\n",
                    "   (3) Leave the classroom.\n",
                    "   (4) Search Mr. W's desk.\n"]
    if "itemStaffKeycard" in inventory:
        classOptions.pop()
    classLine2 = "\nYou search through each of the student's desks until you find what seems to be your friend's " \
                 "desk.\033[0;49m You dig through, pulling out random papers in search of the homework.\n\n"
    classLine3 = "To your dismay, you don't find it.\033[0;49m However, as you shove all the papers back into the " \
                 "desk, a loose piece of paper flies out!\033[0;49m You quickly catch it before it touches the floor, " \
                 "catching a glance at what it is..\n\n"
    classLine4 = "Oh!\033[0;49m It's the birthday letter you wrote for your friend.\033[0;49m Ah, right! Their " \
                 "birthday is on the same day as the homework's due date.\033[0;49m Haha, what a birthday gift!\033[" \
                 "0;49m You carefully slip the letter back into their desk, subtly laughing to yourself."
    classLine5 = "\nYou look down at the pristine, white floor, scanning for any loose papers..\n\n"
    classLine6 = "..."
    classLine7 = "\n\nYou look at the floor harder..\n\n"
    classLine8 = "Uhm.\033[0;49m It's not there."
    classLine9 = "\nMaybe there's extra copies of the homework somewhere in here.\n\n"
    classLine10 = "You flip through the folders and rummage through his stuff.\033[0;49m Unfortunately, he doesn't " \
                  "have any extras.\n\n"
    classLine11 = "However, as you search through Mr. W's bag, you do find a staff keycard..\n\n"

    # call function
    for line in classOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(len(classOptions))
    time.sleep(pauseTransition)
    if option == 1:
        paper.play()
        dialogue(classLine2, dialogueSpeed, pauseDialogue)
        dialogue(classLine3, dialogueSpeed, pauseDialogue)
        calendar.play()
        dialogue(classLine4, dialogueSpeed, pauseTransition)
        clear()
        classOption()
    elif option == 2:
        dialogue(classLine5, dialogueSpeed, pauseTransition)
        dialogue(classLine6, dotSpeed, pauseTransition)
        dialogue(classLine7, dialogueSpeed, 3)
        dialogue(classLine8, dialogueSpeed, pauseTransition)
        clear()
        classOption()
    elif option == 3:
        clear()
        schoolScene()
    elif option == 4:
        dialogue(classLine9, dialogueSpeed, pauseDialogue)
        paper.play()
        dialogue(classLine10, dialogueSpeed, pauseDialogue)
        box.play()
        dialogue(classLine11, dialogueSpeed, pauseTransition)
        keycardOption()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        classOption()

def keycardOption():
    # dialogue
    keycardOptions = ["   (1) Take it!\n",
                      "   (2) ..This is an invasion of privacy.\n"]
    keycardLine1 = "\nThis should be useful for later.\n\n"
    keycardLine2 = "Like the kleptomaniac you are, you psych yourself up before taking the keycard and slipping it " \
                   "into your pocket.\n\n"
    keycardLine3 = "\033[38;5;14mOBTAINED 'STAFF KEYCARD'\033[0;49m"
    keycardLine4 = "\nOkay, scaredy-cat.\n\n"
    keycardLine5 = "You zip up the bag, brushing it off before setting it back down onto the floor."

    # call function
    for line in keycardOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(keycardLine1, dialogueSpeed, pauseDialogue)
        zip_up.play()
        dialogue(keycardLine2, dialogueSpeed, pauseDialogue)
        success.play()
        dialogue(keycardLine3, dialogueSpeed, pauseTransition)
        inventory.append("itemStaffKeycard")
        clear()
        classOption()
    elif option == 2:
        dialogue(keycardLine4, dialogueSpeed, pauseDialogue)
        zip_up.play()
        dialogue(keycardLine5, dialogueSpeed, pauseTransition)
        clear()
        classOption()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        keycardOption()

################################################### STAFF ##############################################################
def staffScene():
    # dialogue
    staffLine1 = "Well, since there seems to be no one around, you could probably search the staff room.\033[0;49m " \
                 "Cautiously, you peek inside to see if there's anyone inside.\n\n"
    staffLine2 = "Of course, it's empty.\n\n"

    # call functions
    dialogue(staffLine1, dialogueSpeed, pauseDialogue)
    dialogue(staffLine2, dialogueSpeed, pauseTransition)
    staffOption()

def staffOption():
    # dialogue
    staffOptions = ["   (1) Search inside the staff room.\n",
                    "   (2) Leave.\n"]
    staffLine3 = "..."
    staffLine4 = "\n\nAh, of course.\033[0;49m The door can only be unlocked by staff.."
    staffLine5 = "\n\nYou fish for the keycard in your pocket and swipe it through the door's sensor.\033[0;49m The " \
                 "door opens with a click, slowly cracking open as you cautiously look around once more.\n\n"
    staffLine6 = "You quickly find Mr. W's cubicle.\033[0;49m Scanning through, there is a laptop, a calendar, " \
                 "several piles of schoolwork, and several scattered pens.\n\n"
    staffLine7 = "You aren't supposed to be here, anyway."

    # call functions
    for line in staffOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    print("")
    time.sleep(pauseTransition)
    if option == 1:
        if "itemStaffKeycard" in inventory:
            door_locked.play()
            dialogue(staffLine3, dotSpeed, pauseTransition)
            dialogue(staffLine4, dialogueSpeed, pauseTransition)
            door_open.play()
            dialogue(staffLine5, dialogueSpeed, pauseDialogue)
            dialogue(staffLine6, dialogueSpeed, pauseTransition)
            cubicleOption()
        else:
            door_locked.play()
            dialogue(staffLine3, dotSpeed, pauseTransition)
            dialogue(staffLine4, dialogueSpeed, pauseTransition)
            clear()
            staffOption()
    elif option == 2:
        footsteps.play()
        dialogue(staffLine7, dialogueSpeed, pauseTransition)
        clear()
        schoolScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        staffOption()

def cubicleOption():
    # dialogue
    cubicleOptions = ["   (1) Use the laptop.\n",
                      "   (2) Examine the calendar.\n",
                      "   (3) Search the piles of schoolwork.\n",
                      "   (4) Leave.\n"]
    cubicleLine1 = "\nYou try to use the computer, but it's locked behind a password.\033[0;49m After a few " \
                   "unsuccessful attempts, you finally get a hint..\n\n"
    cubicleLine2 = "\n..What kind of..\n\n"
    cubicleLine3 = "It's just a bunch of black and white squares.\033[0;49m You call this a hint?\n\n"
    cubicleLine4 = "\nThe calendar is hung on the inner sidewall of the cubicle, skipped to April.\033[0;49m It has " \
                   "several markings with dates for meetings and assignment due dates, including the homework's due " \
                   "date next Monday.\n\n"
    cubicleLine5 = "Other than that, nothing seems to be very significant."
    cubicleLine6 = "\nYou dig through the piles of schoolwork, pulling out several marked and unmarked assignments " \
                   "from students.\033[0;49m You catch a glimpse of your name in the sea of paper.\033[0;49m It's the " \
                   "unit test from last Friday!\n\n"
    cubicleLine7 = "You scan the top of your paper..\n\n"
    cubicleLine8 = f'   "{username},\033[0;49m Period: 1,\033[0;49m April 11.."\n\n'
    cubicleLine9 = "..Huh?\n\n"
    cubicleLine10 = "..Is that a 65%?\033[0;49m Here you thought you aced this test.\033[0;49m Wow, and it looks like " \
                    "everyone else did really well.\n\n"
    cubicleLine11 = "Other than that, there's no extra homework lying around.\n\n"
    cubicleLine12 = "Frustrated, you carefully stack up the papers back to its original state, as if no one touched it."
    cubicleLine13 = "\nYeah, that's enough snooping around for now.\033[0;49m You didn't find any homework, " \
                    "but whatever.\033[0;49m You wouldn't want to go through the trouble of searching or printing out " \
                    "a whole new copy without anyone noticing, anyway.\n\n"
    cubicleLine14 = "You turn back around and leave the staff room, softly closing the door behind you."

    # call functions
    for line in cubicleOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(4)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(cubicleLine1, dialogueSpeed, pauseDialogue)
        time.sleep(pauseTransition)
        dialogue(cubicleLine2, dialogueSpeed, pauseDialogue)
        dialogue(cubicleLine3, dialogueSpeed, pauseTransition)
        hackOption()
    elif option == 2:
        calendar.play()
        dialogue(cubicleLine4, dialogueSpeed, pauseDialogue)
        dialogue(cubicleLine5, dialogueSpeed, pauseTransition)
        clear()
        cubicleOption()
    elif option == 3:
        paper.play()
        dialogue(cubicleLine6, dialogueSpeed, pauseDialogue)
        calendar.play()
        dialogue(cubicleLine7, dialogueSpeed, pauseDialogue)
        dialogue(cubicleLine8, endingSpeed, pauseTransition)
        dialogue(cubicleLine9, dialogueSpeed, pauseDialogue)
        dialogue(cubicleLine10, dialogueSpeed, pauseDialogue)
        dialogue(cubicleLine11, dialogueSpeed, pauseDialogue)
        paper.play()
        dialogue(cubicleLine12, dialogueSpeed, pauseTransition)
        clear()
        cubicleOption()
    elif option == 4:
        dialogue(cubicleLine13, dialogueSpeed, pauseDialogue)
        door_close.play()
        dialogue(cubicleLine14, dialogueSpeed, pauseTransition)
        clear()
        schoolScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        cubicleOption()

def hackOption():
    # dialogue
    hackOptions = ["   (1) Enter the password.\n",
                   "   (2) Forget it.\n"]
    hackLine1 = "\nPassword Hint:"
    hackLine2 = "\n..Got it!\033[0;49m Mr. W is really stingy, huh?\n\n"
    hackLine3 = "The computer unlocks before you as you celebrate internally.\033[0;49m However, before you can " \
                "navigate through it, an open tab catches your eye.\033[0;49m It seems to be a report of a missing " \
                "student at this school.\033[0;49m On a separate tab, a low quality depiction of a masked figure " \
                "wearing a red cloak nearly makes you jump out of your seat.\n\n"
    hackLine4 = "\nThat image is..\033[0;49m Very creepy.\n\n"
    hackLine5 = "It's rumored that the student's disappearance was due to a supernatural entity in one of the school " \
                "bathrooms.\033[0;49m You've heard claims of another student who survived the spirit by outsmarting " \
                "it.\033[0;49m You never really believed it, but concerning the amount of disappearances recently, " \
                "it might actually be real.\n\n"
    hackLine6 = "Was Mr. W investigating this, perhaps?\033[0;49m Could there actually be a serial killer hiding at " \
                "this school?\n\n"
    hackLine7 = "You're seriously unnerved.\033[0;49m Forgetting what you were originally searching for, you close " \
                "the laptop and set it aside with a newly instilled feeling of fear.\n"
    hackLine8 = "\n..Incorrect.\033[0;49m Maybe try again?\n\n"
    hackLine9 = "It might be a deciphering puzzle."
    hackLine10 = "\nThere's no way you're gonna spend the whole day trying to hack into your teacher's computer.\n\n"

    # call functions
    for line in hackOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(hackLine1, dialogueSpeed, pauseTransition)
        askPassword = "Password: \n"
        dialogue(askPassword, dialogueSpeed, 0)
        enteredPassword = input("   ")
        time.sleep(pauseTransition)
        if enteredPassword == "ihavenomouthandimustscream":
            success.play()
            dialogue(hackLine2, dialogueSpeed, pauseDialogue)
            dialogue(hackLine3, dialogueSpeed, pauseDialogue)
            time.sleep(pauseTransition)
            dialogue(hackLine4, dialogueSpeed, pauseDialogue)
            dialogue(hackLine5, dialogueSpeed, pauseDialogue)
            dialogue(hackLine6, dialogueSpeed, pauseDialogue)
            dialogue(hackLine7, dialogueSpeed, pauseTransition)
            global allowEscape
            allowEscape = True
            clear()
            cubicleOption()
        else:
            error.play()
            dialogue(hackLine8, dialogueSpeed, pauseDialogue)
            dialogue(hackLine9, dialogueSpeed, pauseTransition)
            clear()
            hackOption()
    elif option == 2:
        dialogue(hackLine10, dialogueSpeed, pauseTransition)
        clear()
        cubicleOption()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        hackOption()

################################################### LOCKER #############################################################
def lockerScene():
    # dialogue
    lockerLine1 = "It would make the most sense to search here.\033[0;49m The locker is locked with a combination " \
                  "padlock with four dials.\033[0;49m You could ask your friend for their passcode, but they're " \
                  "probably really busy at the moment.\n\n"
    lockerLine2 = "No need to search here anymore.\n\n"
    lockerLine3 = "You turn around and leave the locker alone.\n\n"

    # call functions
    if "itemHomework" not in inventory:
        dialogue(lockerLine1, dialogueSpeed, pauseTransition)
        clear()
        lockerOption()
    else:
        dialogue(lockerLine2, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(lockerLine3, dialogueSpeed, pauseTransition)
        clear()
        schoolScene()

def lockerOption():
    # dialogue
    lockerOptions = ["   (1) Try to unlock it.\n",
                     "   (2) Leave.\n"]
    lockerLine4 = "\n..Got it!\033[0;49m Wasn't too hard.\n\n"
    lockerLine5 = "The lock comes off, and you scan through the locker for..\n\n"
    lockerLine6 = "Homework!\033[0;49m Yes!\n\n"
    lockerLine7 = "\033[38;5;14mOBTAINED 'HOMEWORK'\033[0;49m\n\n"
    lockerLine8 = "You quickly snatch your friend's homework, and stuff it into your bag.\033[0;49m You turn around " \
                  "and..\n\n"
    lockerLine9 = "..Huh?\n\n"
    lockerLine10 = "Something falls out and clatters onto the floor.\033[0;49m You pick it up and examine it.\n\n"
    lockerLine11 = f'It is a small, antique-looking key, attached with a small tag with the name.. "{username}"?\033[' \
                   f'0;49m Is it addressed to you?\n\n'
    lockerLine12 = "They must've anticipated this.\033[0;49m You slip the small key carefully into your pocket, " \
                   "closing the locker before setting off once more.\n\n"
    lockerLine13 = "\033[38;5;14mOBTAINED 'SMALL KEY'\033[0;49m"
    lockerLine14 = "\n..Hmm, that's not it.\n\n"
    lockerLine15 = "Maybe their passcode has to do with an important date."
    lockerLine16 = "\nIt's going to take forever to guess their passcode.\033[0;49m Might as well just give up now."

    # call functions
    for line in lockerOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        askPasscode = "\nTurn dials to:   x|x|x|x\n"
        dialogue(askPasscode, dialogueSpeed, 0)
        enteredPasscode = input("   ")
        time.sleep(pauseTransition)
        if enteredPasscode == "0421":
            locker_open.play()
            dialogue(lockerLine4, dialogueSpeed, pauseDialogue)
            dialogue(lockerLine5, dialogueSpeed, pauseDialogue)
            dialogue(lockerLine6, dialogueSpeed, pauseDialogue)
            success.play()
            dialogue(lockerLine7, endingSpeed, pauseDialogue)
            dialogue(lockerLine8, dialogueSpeed, pauseTransition)
            dialogue(lockerLine9, dialogueSpeed, pauseTransition)
            dialogue(lockerLine10, dialogueSpeed, pauseDialogue)
            dialogue(lockerLine11, dialogueSpeed, pauseDialogue)
            locker_close.play()
            dialogue(lockerLine12, dialogueSpeed, pauseDialogue)
            success.play()
            dialogue(lockerLine13, endingSpeed, pauseTransition)
            inventory.append("itemHomework")
            inventory.append("itemSmallKey")
            clear()
            schoolScene()
        else:
            locker_locked.play()
            dialogue(lockerLine14, dialogueSpeed, pauseTransition)
            dialogue(lockerLine15, dialogueSpeed, pauseTransition)
            clear()
            lockerOption()
    elif option == 2:
        dialogue(lockerLine16, dialogueSpeed, pauseTransition)
        clear()
        schoolScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        lockerOption()

#################################################### YARD ##############################################################
def yardScene():
    # dialogue
    yardLine1 = "You recall how you and your friend were outside studying during lunchtime.\033[0;49m Maybe they just " \
                "forgot their homework here?\n\n"

    # call functions
    door_creak.play()
    dialogue(yardLine1, dialogueSpeed, pauseTransition)
    yardOption()

def yardOption():
    # dialogue
    yardOptions = ["   (1) Search inside the school.\n",
                   "   (2) Search near the fences.\n",
                   "   (3) Search that room at the very end of the school.\n",
                   "   (4) Go home.\n"]
    if "itemFreshCake" in inventory:
        yardOptions.append("   (5) ..What is that in the distance?\n")
    yardLine2 = "\nYou examine the fence for any loose papers.\n\n"
    yardLine3 = "Unfortunately, there doesn't seem to be anything except abandoned coffee cups and takeout boxes " \
                "littered around.\n\n"
    yardLine4 = "Hopefully it didn't fly away.."
    yardLine5 = "\nAt the highest point of the field, you spot a mysterious object.\033[0;49m Has that always been " \
                "there?\n\n"
    yardLine6 = "You decide to approach it out of curiosity."

    # call function
    for line in yardOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(len(yardOptions))
    time.sleep(pauseTransition)
    if option == 1:
        clear()
        schoolScene()
    elif option == 2:
        dialogue(yardLine2, dialogueSpeed, pauseDialogue)
        dialogue(yardLine3, dialogueSpeed, pauseDialogue)
        dialogue(yardLine4, dialogueSpeed, pauseTransition)
        clear()
        yardOption()
    elif option == 3:
        clear()
        hiddenScene()
    elif option == 4:
        clear()
        exitScene()
    elif option == 5 and "itemFreshCake" in inventory:
        dialogue(yardLine5, dialogueSpeed, pauseDialogue)
        pygame.mixer.music.pause()
        dialogue(yardLine6, dialogueSpeed, pauseTransition)
        clear()
        vergilScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        yardOption()

################################################### BATHROOM ###########################################################
def bathroomTimer():
    totalSeconds = 5
    while totalSeconds > 0 and timerRunning:
        time.sleep(1)
        totalSeconds -= 1
    if totalSeconds == 0 and timerRunning:
        clear()
        endingUrgent()

def bathroomScene():
    # dialogue
    bathroomLine1 = "You slowly open the door, and are immediately welcomed by a dimly lit room and a disgusting " \
                    "stench.\033[0;49m Repulsed, you quickly cover your nose with your shirt.\033[0;49m This place " \
                    "clearly hasn't been maintained recently.\n\n"
    bathroomLine2 = "Unsurprisingly, none of the stalls seem to be working, except for the one at the very end of the " \
                    "room.\n\n"
    bathroomLine3 = "..."
    bathroomLine4 = "\n\nYou feel a shiver run up your spine.\033[0;49m Is it the eeriness of the bathroom, or..\n\n"
    bathroomLine5 = "..the sudden strong urge to go relieve yourself.\033[0;49m You clearly don't remember drinking a " \
                    "ton of water beforehand, where did this come from?!\n\n"
    bathroomLine6 = "You need to use the stall immediately.\n\n"

    # call functions
    pygame.mixer.music.stop()
    door_creak.play()
    dialogue(bathroomLine1, dialogueSpeed, pauseDialogue)
    dialogue(bathroomLine2, dialogueSpeed, pauseDialogue)
    dialogue(bathroomLine3, dotSpeed, pauseTransition)
    dialogue(bathroomLine4, dialogueSpeed, pauseTransition)
    pygame.mixer.music.load(os.path.join(folder, 'silly_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(bathroomLine5, dialogueSpeed, pauseDialogue)
    dialogue(bathroomLine6, dialogueSpeed, pauseTransition)
    bathroomOption()

def bathroomOption():
    # dialogue
    bathroomOptions = ["   (1) Use the stall.\n",
                       "   (2) Leave.\n"]
    if "itemGrenade" in inventory:
        bathroomOptions.append("   (3) Destroy everything.\n")
    bathroomLine7 = "\nYou quickly rush over to the last bathroom stall, sitting down on the toilet and doing your " \
                    "business.\033[0;49m However, when you look down to grab some toilet paper..\n\n"
    bathroomLine8 = "..None.\033[0;49m There's nothing left.\n\n"
    bathroomLine9 = "Just then, you see a figure approaching.\n\n"
    bathroomLine10 = '"Red paper or blue paper?"\n\n'
    bathroomLine11 = "\nYou can't leave now!\033[0;49m You have to go,\033[0;49m like,\033[0;49m really bad!"

    # call functions
    for line in bathroomOptions:
        dialogue(line, optionSpeed, 0)

    global timerRunning
    timerRunning = True
    bathroomThread = threading.Thread(target=bathroomTimer)
    bathroomThread.start()

    # options
    option = chooseOption(len(bathroomOptions))
    time.sleep(pauseTransition)
    if option == 1:
        timerRunning = False
        pygame.mixer.music.stop()
        running.play()
        dialogue(bathroomLine7, dialogueSpeed, pauseTransition)
        dialogue(bathroomLine8, dialogueSpeed, pauseTransition)
        dialogue(bathroomLine9, dialogueSpeed, pauseTransition)
        dialogue(bathroomLine10, endingSpeed, pauseTransition)
        paperOption()
    elif option == 2:
        timerRunning = False
        dialogue(bathroomLine11, dialogueSpeed, pauseTransition)
        clear()
        timerRunning = True
        bathroomOption()
    elif option == 3 and "itemGrenade" in inventory:
        timerRunning = False
        pygame.mixer.music.stop()
        clear()
        endingCinema()
    else:
        timerRunning = False
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        timerRunning = True
        bathroomOption()

def paperOption():
    # dialogue
    paperOptions = ["   (1) Red paper.\n",
                    "   (2) Blue paper.\n"]
    if allowEscape:
        paperOptions.append("   (3) I don't want any paper.\n")

    # call functions
    for line in paperOptions:
        heartbeat.play(loops=3)
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(len(paperOptions))
    time.sleep(pauseTransition)
    if option == 1:
        clear()
        endingRed()
    elif option == 2:
        clear()
        endingBlue()
    elif option == 3 and allowEscape:
        clear()
        endingEscaped()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        paperOption()

#################################################### HIDDEN ############################################################
def hiddenScene():
    # dialogue
    hiddenLine1 = "You approach the room at the far corner of the school.\033[0;49m The entire door has been painted " \
                  "the same color as the walls, as if to hide itself.\033[0;49m Ominous!\n\n"
    hiddenLine2 = "No need to search here anymore.\n\n"
    hiddenLine3 = "You turn around and walk back to the yard.\n\n"

    # call functions
    if 'itemFreshCake' or 'itemGrenade' in inventory:
        dialogue(hiddenLine2, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(hiddenLine3, dialogueSpeed, pauseTransition)
        clear()
        yardScene()
    else:
        footsteps.play()
        dialogue(hiddenLine1, dialogueSpeed, pauseTransition)
        hiddenOption()

def hiddenOption():
    # dialogue
    hiddenOptions = ["   (1) Open the door.\n",
                     "   (2) Leave.\n"]
    hiddenLine4 = "..."
    hiddenLine5 = "\n\nLocked.\033[0;49m Looks like it can only be opened with a key.."
    hiddenLine6 = "\n\nYou fish for the key in your pocket and insert it into the keyhole, pulling the door " \
                  "open.\033[0;49m Immediately, dust starts flying everywhere.\033[0;49m Looks like no one has been " \
                  "in here in ages..\n\n"
    hiddenLine7 = "You turn on the lights, quickly scanning the room for your friend's homework.\033[0;49m Of course, " \
                  "you don't see it.\n\n"
    hiddenLine8 = "However, something else catches your attention.\033[0;49m A large open box, sitting at the very " \
                  "corner of the room.\033[0;49m It's filled up with tons of random objects.\033[0;49m Perhaps these " \
                  "are all confiscated items?\n\n"
    hiddenLine9 = "Well, it's not like your friend's homework is going to be in here anyway.\n\n"
    hiddenLine10 = "You turn around and walk back to the yard."

    # call functions
    for line in hiddenOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    print("")
    time.sleep(pauseTransition)
    if option == 1:
        if "itemSmallKey" in inventory:
            door_locked.play()
            dialogue(hiddenLine4, dotSpeed, pauseTransition)
            dialogue(hiddenLine5, dialogueSpeed, pauseTransition)
            dialogue(hiddenLine6, dialogueSpeed, pauseDialogue)
            door_open.play()
            dialogue(hiddenLine7, dialogueSpeed, pauseDialogue)
            dialogue(hiddenLine8, dialogueSpeed, pauseTransition)
            boxOption()
        else:
            door_locked.play()
            dialogue(hiddenLine4, dotSpeed, pauseTransition)
            dialogue(hiddenLine5, dialogueSpeed, pauseTransition)
            clear()
            hiddenOption()
    elif option == 2:
        dialogue(hiddenLine9, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(hiddenLine10, dialogueSpeed, pauseTransition)
        clear()
        yardScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        hiddenOption()

def boxOption():
    # dialogue
    boxOptions = ["   (1) Dig through the box.\n",
                  "   (2) Maybe you should leave it alone.\n"]
    boxLine1 = "\nYou dig through the box and pull out..\n\n"
    boxLine2 = "..A rubber duck!\n\n"
    boxLine3 = "Hello there!\033[0;49m Maybe you should bring it back home.\033[0;49m It would be nice to have a " \
               "bathtub friend."
    boxLine4 = "..Half-eaten homework!\n\n"
    boxLine5 = "Hey, you found homework!\033[0;49m It's pretty chewed up though, and you remember that your friend " \
               "does not have a dog."
    boxLine6 = "..A pastry box?\n\n"
    boxLine7 = "Upon closer inspection, you discover that there is a slice of cake inside.\033[0;49m Even though it " \
               "has been sitting here for so long, it seems to be in perfect condition.\n\n"
    boxLine8 = "For whatever reason, you can't seem to let it go, like it was meant for you specifically.\033[0;49m " \
               "You carefully bury the pastry box deep within your bag, as you sense a heavy feeling from deep " \
               "inside you.\n\n"
    boxLine9 = "\033[38;5;14mOBTAINED 'FRESH CAKE'\033[0;49m\n\n"
    boxLine10 = "Or you know,\033[0;49m maybe you're just hungry.\n\n"
    boxLine11 = "You leave the dusty room and go back into the yard."
    boxLine12 = "..A grenade?! What the heck?!\n\n"
    boxLine13 = "Should you take it?"
    boxLine14 = "\nIt would probably be best not to mess with it.\033[0;49m Who knows, maybe there's some spiders " \
                "hiding in there.\n\n"
    boxLine15 = "Well, looks like there's nothing else here.\033[0;49m You turn around and walk back to the yard."

    # call functions
    for line in boxOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        box.play()
        dialogue(boxLine1, dialogueSpeed, pauseTransition)
        retrievedItem = random.choices(largeBox, weights=weights, k=1)[0]
        if retrievedItem == "itemRubberDuck":
            dialogue(boxLine2, dialogueSpeed, pauseDialogue)
            dialogue(boxLine3, dialogueSpeed, pauseTransition)
            weights.remove(35)
            largeBox.remove("itemRubberDuck")
            clear()
            boxOption()
        elif retrievedItem == "itemChewedHomework":
            dialogue(boxLine4, dialogueSpeed, pauseDialogue)
            dialogue(boxLine5, dialogueSpeed, pauseTransition)
            weights.remove(35)
            largeBox.remove("itemChewedHomework")
            clear()
            boxOption()
        elif retrievedItem == "itemFreshCake":
            dialogue(boxLine6, dialogueSpeed, pauseDialogue)
            dialogue(boxLine7, dialogueSpeed, pauseDialogue)
            zip_up.play()
            dialogue(boxLine8, dialogueSpeed, pauseDialogue)
            success.play()
            dialogue(boxLine9, dialogueSpeed, pauseDialogue)
            dialogue(boxLine10, dialogueSpeed, pauseDialogue)
            footsteps.play()
            dialogue(boxLine11, dialogueSpeed, pauseTransition)
            inventory.append("itemFreshCake")
            clear()
            yardScene()
        else:
            dialogue(boxLine12, dialogueSpeed, pauseDialogue)
            dialogue(boxLine13, dialogueSpeed, pauseTransition)
            clear()
            grenadeOption()
    elif option == 2:
        dialogue(boxLine14, dialogueSpeed, pauseDialogue)
        door_close.play()
        dialogue(boxLine15, dialogueSpeed, pauseTransition)
        clear()
        yardScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        boxOption()

def grenadeOption():
    # dialogue
    grenadeOptions = ["   (1) Yes!\n",
                      "   (2) Absolutely not.\n"]
    grenadeLine1 = "\nWhoa, seriously?\033[0;49m No second thoughts..?\033[0;49m Uh, alright then.\033[0;49m You've " \
                   "acquired..\033[0;49m A grenade.\n\n"
    grenadeLine2 = "\033[38;5;14mOBTAINED 'GRENADE'\033[0;49m\n\n"
    grenadeLine3 = "You leave the dusty room and go back into the yard."
    grenadeLine4 = "\nThat's an extremely dangerous weapon!\033[0;49m Probably should report it once you leave.\033[" \
                   "0;49m You carefully set it back down into the box."

    # call functions
    for line in grenadeOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(grenadeLine1, dialogueSpeed, pauseDialogue)
        success.play()
        dialogue(grenadeLine2, endingSpeed, pauseDialogue)
        door_close.play()
        dialogue(grenadeLine3, dialogueSpeed, pauseTransition)
        inventory.append("itemGrenade")
        clear()
        yardScene()
    elif option == 2:
        dialogue(grenadeLine4, dialogueSpeed, pauseTransition)
        clear()
        weights.remove(20)
        largeBox.remove("itemGrenade")
        boxOption()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        grenadeOption()

#################################################### VERGIL ############################################################
def vergilScene():
    # dialogue
    vergilLine1 = "As you come closer to it, you slowly begin to make it out.\033[0;49m There stood a lone katana, " \
                  "leaning against a plastic white chair.\n\n"
    vergilLine2 = "It seems to be calling out to you.\n\n"

    # call functions
    dialogue(vergilLine1, dialogueSpeed, pauseDialogue)
    dialogue(vergilLine2, dialogueSpeed, pauseTransition)
    vergilOption()

def vergilOption():
    # dialogue
    vergilOptions = ["   (1) Sit down.\n", "   (2) Leave.\n"]
    vergilLine3 = "\nCryptic chairs that appear out of nowhere shall not be sat on!\033[0;49m Besides, you still have " \
                  "homework to find.\033[0;49m Better not waste any more time.\n\n"
    vergilLine4 = "You turn around and return to the yard."

    # call functions
    for line in vergilOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        clear()
        endingVergil()
    elif option == 2:
        dialogue(vergilLine3, dialogueSpeed, pauseDialogue)
        pygame.mixer.music.unpause()
        footsteps.play()
        dialogue(vergilLine4, dialogueSpeed, pauseTransition)
        clear()
        yardScene()
    else:
        clear()
        dialogue(optionError, dialogueSpeed, pauseTransition)
        vergilOption()

#################################################### ENDINGS ###########################################################
def exitScene():
    if "itemGrenade" in inventory:
        falseEnding = "You try to leave the school grounds, but you suddenly feel an otherworldly presence pulling " \
                      "you back.\033[0;49m Must be that weapon of yours, huh?\033[0;49m Invisible video game " \
                      "barriers!\033[0;49m Looks like you're gonna have to turn around.\n\n"
        clear()
        pygame.mixer.music.pause()
        dialogue(falseEnding, dialogueSpeed, pauseTransition)
        clear()
        pygame.mixer.music.unpause()
        entryScene()
    else:
        if "itemHomework" in inventory:
            endingFreed1 = "You've successfully retrieved your friend's homework,\033[0;49m and now it's time to " \
                           "leave.\n\n"
            endingFreed2 = "As you walk away from the school,\033[0;49m that tense feeling inside of you slowly fades " \
                           "away with every step,\033[0;49m as you quickly make your way to your friend's " \
                           "home.\n\n\033[1;49m"
            endingFreed3 = "ENDING:\033[1;49m Freedom\033[0;49m"
            pygame.mixer.music.load(os.path.join(folder, 'normal_ending.mp3'))
            pygame.mixer.music.play(-1)
            dialogue(endingFreed1, dialogueSpeed, pauseDialogue)
            footsteps.play()
            dialogue(endingFreed2, dialogueSpeed, pauseDialogue)
            dialogue(endingFreed3, endingSpeed, pauseTransition)
            if "endingFreed" not in endings:
                endings.append("endingFreed")
        else:
            endingLied1 = "..."
            endingLied2 = "\n\nFor whatever reason,\033[0;49m you feel deeply unsettled.\033[0;49m No matter how hard " \
                          "you try,\033[0;49m you can't shake that feeling off.\n\n"
            endingLied3 = "You slowly turn around and hurry back home,\033[0;49m carrying a heavy heart and regret " \
                          "for your false promise.\n\n\033[1;49m"
            endingLied4 = "ENDING:\033[1;49m Something is wrong.\033[0;49m"
            pygame.mixer.music.stop()
            dialogue(endingLied1, dotSpeed, pauseTransition)
            pygame.mixer.music.load(os.path.join(folder, 'off_ending.mp3'))
            pygame.mixer.music.play(-1)
            dialogue(endingLied2, dialogueSpeed, pauseDialogue)
            running.play()
            dialogue(endingLied3, dialogueSpeed, pauseDialogue)
            dialogue(endingLied4, endingSpeed, pauseTransition)
            if "endingLied" not in endings:
                endings.append("endingLied")

def endingUrgent():
    endingUrgent1 = "Before you could take another step,\033[0;49m you realize that it's too late.\n\n"
    endingUrgent2 = "You couldn't hold it in anymore,\033[0;49m and you feel your dignity stream down your leg.\033[" \
                    "0;49m Gross!\033[0;49m Go get yourself cleaned up!\n\n\033[1;49m"
    endingUrgent3 = "ENDING:\033[1;49m mom, i wet the bed again :(\033[0;49m"
    pygame.mixer.music.stop()
    dialogue(endingUrgent1, dialogueSpeed, pauseDialogue)
    dialogue(endingUrgent2, dialogueSpeed, pauseDialogue)
    dialogue(endingUrgent3, endingSpeed, pauseTransition)
    if "endingUrgent" not in endings:
        endings.append(endingUrgent)

def endingRed():
    endingRed1 = "The stall door slowly creaks open.\n\n"
    endingRed2 = "Suddenly,\033[0;49m flashes of red paint the walls surrounding you.\033[0;49m As you look down at " \
                 "your trembling hands,\033[0;49m you see various slashes cut deep into you,\033[0;49m so much so " \
                 "that you can no longer see your skin.\033[0;49m Your entire body weakens,\033[0;49m and you fall to " \
                 "the ground with a sickening thud.\n\n"
    endingRed3 = "With one final breath,\033[0;49m you see a masked figure wearing a red cloak towering over you," \
                 "\033[0;49m and everything fades to black.\n\n"
    endingRed4 = "You are dead.\n\n\033[1;49m"
    endingRed5 = "ENDING:\033[1;49m A Thousand Lacerations\033[0;49m"
    door_creak.play()
    dialogue(endingRed1, dialogueSpeed, pauseTransition)
    slash.play()
    pygame.mixer.music.load(os.path.join(folder, 'dead_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(endingRed2, dialogueSpeed, pauseTransition)
    dialogue(endingRed3, dialogueSpeed, pauseTransition)
    dialogue(endingRed4, dialogueSpeed, pauseTransition)
    dialogue(endingRed5, endingSpeed, pauseTransition)
    if "endingRed" not in endings:
        endings.append(endingRed)

def endingBlue():
    endingBlue1 = "The stall door slowly creaks open.\n\n"
    endingBlue2 = "Suddenly,\033[0;49m you feel the chest immediately compress.\033[0;49m You helplessly clutch at " \
                  "your neck,\033[0;49m desperately gasping for the air escaping from your lungs.\033[0;49m Your " \
                  "entire body weakens,\033[0;49m and you fall to the ground with a sickening thud.\n\n"
    endingBlue3 = "With one final breath,\033[0;49m you see a masked figure wearing a red cloak towering over you," \
                  "\033[0;49m and everything fades to black.\n\n"
    endingBlue4 = "You are dead.\n\n\033[1;49m"
    endingBlue5 = "ENDING:\033[1;49m Out of Breath?\033[0;49m"
    door_creak.play()
    dialogue(endingBlue1, dialogueSpeed, pauseTransition)
    gasp.play()
    pygame.mixer.music.load(os.path.join(folder, 'dead_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(endingBlue2, dialogueSpeed, pauseDialogue)
    dialogue(endingBlue3, dialogueSpeed, pauseDialogue)
    dialogue(endingBlue4, dialogueSpeed, pauseDialogue)
    dialogue(endingBlue5, endingSpeed, pauseTransition)
    if "endingBlue" not in endings:
        endings.append(endingBlue)

def endingEscaped():
    endingEscaped1 = "..."
    endingEscaped2 = "\n\nNothing happens.\n\n"
    endingEscaped3 = "You sneak over to the next stall and slide under the stall door,\033[0;49m seeing the figure " \
                     "peering over the last stall in your peripheral view.\n\n"
    endingEscaped4 = "You quickly rush out of the school with a racing heart,\033[0;49m never daring to look " \
                     "back.\033[1;49m\n\n"
    endingEscaped5 = "ENDING:\033[1;49m 赤マント\033[0;49m"
    pygame.mixer.music.stop()
    dialogue(endingEscaped1, dotSpeed, pauseTransition)
    dialogue(endingEscaped2, dialogueSpeed, pauseTransition)
    running.play()
    heartbeat.play(loops=3)
    dialogue(endingEscaped3, dialogueSpeed, pauseDialogue)
    dialogue(endingEscaped4, dialogueSpeed, pauseDialogue)
    dialogue(endingEscaped5, endingSpeed, pauseTransition)
    if "endingEscaped" not in endings:
        endings.append(endingEscaped)

def endingCinema():
    endingCinema1 = "You reach into your backpack and pull out the explosive from earlier.\033[0;49m It's time to " \
                    "destroy this place,\033[0;49m once and for all.\n\n"
    endingCinema2 = "With a sharp inhale,\033[0;49m you pull on the pin and immediately chuck it into the bathroom," \
                    "\033[0;49m closing the door behind you as you leave.\n\n"
    endingCinema3 = "The once terrorizing bathroom engulfed in flames,\033[0;49m pieces of debris flying past you as " \
                    "you walk away in slow motion.\033[0;49m In the threat of imminent danger,\033[0;49m you emerged " \
                    "victorious.\n\n"
    endingCinema4 = "No more missing students.\033[0;49m No more evil spirits.\033[0;49m No more urban legends.\n\n"
    endingCinema5 = "It all ends here.\n\n\033[1;49m"
    endingCinema6 = "ENDING:\033[1;49m Absolute Cinema.\033[0;49m"
    pygame.mixer.music.stop()
    dialogue(endingCinema1, dialogueSpeed, pauseDialogue)
    grenade.play()
    dialogue(endingCinema2, dialogueSpeed, pauseDialogue)
    pygame.mixer.music.load(os.path.join(folder, 'POWER.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(endingCinema3, dialogueSpeed, pauseDialogue)
    dialogue(endingCinema4, dialogueSpeed, pauseDialogue)
    dialogue(endingCinema5, dialogueSpeed, pauseDialogue)
    dialogue(endingCinema6, endingSpeed, pauseTransition)
    if "endingCinema" not in endings:
        endings.append(endingCinema)

def endingVergil():
    endingVergil1 = "You sit down on the chair,\033[0;49m letting go of all the tension built up inside of you.\033[" \
                    "0;49m You don't even realize that the sky has turned cloudy.\n\n"
    endingVergil2 = "A surge of \033[1;49mPOWER\033[0;49m washes over you,\033[0;49m as you sink deeper into the " \
                    "chair.\n\n"
    endingVergil3 = "\033[1;49mA storm is approaching,\033[1;49m provoking the black clouds in isolation.\033[1;49m " \
                    "Reclaim your name,\033[1;49m for you are blessed.\033[0;49m\n\n"
    endingVergil4 = "Maybe you should stay here for a while.\n\n\033[1;49m"
    endingVergil5 = "ENDING:\033[1;49m Berried Delight" + " \U0001F370" + " "
    dialogue(endingVergil1, dialogueSpeed, pauseDialogue)
    pygame.mixer.music.load(os.path.join(folder, 'POWER.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(endingVergil2, dialogueSpeed, pauseDialogue)
    dialogue(endingVergil3, dialogueSpeed, pauseDialogue)
    dialogue(endingVergil4, dialogueSpeed, pauseDialogue)
    dialogue(endingVergil5, endingSpeed, pauseTransition)
    if "endingVergil" not in endings:
        endings.append(endingVergil)

################################################# MAIN GAME LOOP #######################################################
while True:
    if gameRunning:
        pygame.mixer.music.stop()
        entryScene()
    else:
        keysThread = threading.Thread(target=keyEvents)
        keysThread.start()
        userInfo()
        gameRunning = True

    # dialogue
    replayLines = ["\n\n\n\033[0;49mPlay again? Y/N\n",
                   "Discovered Endings: " + str(len(endings)) + "/8"]
    replayError = "..I'm going to assume that's a no.\n"

    # call function
    for line in replayLines:
        dialogue(line, dialogueSpeed, 0)

    # reset
    inventory.clear()
    allowEscape = False
    largeBox = ["itemRubberDuck", "itemChewedHomework", "itemFreshCake", "itemGrenade"]

    # store as replay
    replay = input("\n   ")
    replay = replay.upper()
    time.sleep(pauseTransition)

    # jump scene
    if replay == "Y" or replay == "YES":
        clear()
        continue
    elif replay == "N" or replay == "NO":
        break
    else:
        clear()
        dialogue(replayError, dialogueSpeed, pauseTransition)
        break

#################################################### QUIT GAME #########################################################
# dialogue
clear()
quitLine1 = f"Thank you for playing, {username}!"
quitLine2 = "\nQuitting now.."

# call functions
dialogue(quitLine1, dialogueSpeed, pauseDialogue)
dialogue(quitLine2, dialogueSpeed, pauseTransition)

# quit
clear()
exit()
