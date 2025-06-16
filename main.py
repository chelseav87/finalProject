# import modules/packages
import random
import sys
import os
import threading
import time
import pygame
import lines

# sound effects
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
folder = "media"
box = pygame.mixer.Sound(os.path.join(folder, "box.wav"))
calendar = pygame.mixer.Sound(os.path.join(folder, "calendar.wav"))
door_close = pygame.mixer.Sound(os.path.join(folder, "door_close.wav"))
door_creak = pygame.mixer.Sound(os.path.join(folder, "door_creak.wav"))
door_locked = pygame.mixer.Sound(os.path.join(folder, "door_locked.wav"))
door_open = pygame.mixer.Sound(os.path.join(folder, "door_open.wav"))
error = pygame.mixer.Sound(os.path.join(folder, "error.wav"))
footsteps = pygame.mixer.Sound(os.path.join(folder, "footsteps.wav"))
gasp = pygame.mixer.Sound(os.path.join(folder, "gasp.wav"))
grenade = pygame.mixer.Sound(os.path.join(folder, "grenade.wav"))
heartbeat = pygame.mixer.Sound(os.path.join(folder, "heartbeat.wav"))
key_clatter = pygame.mixer.Sound(os.path.join(folder, "key_clatter.wav"))
locker_close = pygame.mixer.Sound(os.path.join(folder, "locker_close.wav"))
locker_locked = pygame.mixer.Sound(os.path.join(folder, "locker_locked.wav"))
locker_open = pygame.mixer.Sound(os.path.join(folder, "locker_open.wav"))
paper = pygame.mixer.Sound(os.path.join(folder, "paper.wav"))
running = pygame.mixer.Sound(os.path.join(folder, "running.wav"))
slash = pygame.mixer.Sound(os.path.join(folder, "slash.wav"))
success = pygame.mixer.Sound(os.path.join(folder, "success.wav"))
zip_up = pygame.mixer.Sound(os.path.join(folder, "zip_up.wav"))

# some variables
weights = [35, 35, 10, 20]
dialogueSpeed = 0.04
endingSpeed = 0.06
dotSpeed = 0.6
optionSpeed = 0.01
pauseDialogue = 0.5
pauseTransition = 1
inventory = []
largeBox = ["itemRubberDuck", "itemChewedHomework", "itemFreshCake", "itemGrenade"]
gameRunning = False


# set text behaviour
def dialogue(line, parameterSpeed, parameterPause):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(parameterSpeed)
    time.sleep(parameterPause)


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

def gameExplanation():

    # call functions
    dialogue(lines.expl_line_1, dialogueSpeed, pauseDialogue)
    dialogue(lines.expl_line_2, dialogueSpeed, pauseDialogue)
    dialogue(lines.expl_line_3, dialogueSpeed, pauseDialogue)
    skipIntro()

def skipIntro():
    # call function
    dialogue(lines.skip_line, dialogueSpeed, 0)

    # store as skip
    skip = input("\n   ")
    skip = skip.upper()
    time.sleep(pauseTransition)

    # jump scene
    if skip == "N" or skip == "NO":
        introScene()
    elif skip == "Y" or skip == "YES":
        entryScene()
    else:
        dialogue(lines.skip_error, dialogueSpeed, pauseTransition)
        skipIntro()

def introScene():
    pygame.mixer.music.load(os.path.join(folder, 'intro_theme.mp3'))
    pygame.mixer.music.play(-1)

    # call functions
    footsteps.play()
    dialogue(lines.intro_line_1, dialogueSpeed, pauseDialogue)
    dialogue(lines.intro_line_2, dialogueSpeed, pauseDialogue)
    dialogue(lines.intro_line_3, dialogueSpeed, pauseDialogue)
    dialogue(lines.intro_line_4, dialogueSpeed, pauseDialogue)
    dialogue(lines.intro_line_5, dialogueSpeed, pauseDialogue)
    dialogue(lines.intro_line_6, dialogueSpeed, pauseDialogue)
    footsteps.play()
    dialogue(lines.intro_line_7, dialogueSpeed, pauseTransition)

    # jump scene
    entryScene()

def entryScene():
    pygame.mixer.music.load(os.path.join(folder, 'main_theme.mp3'))
    pygame.mixer.music.play(-1)

    # call functions
    dialogue(lines.entry_line_1, dialogueSpeed, pauseTransition)
    entryOption()

def entryOption():
    # call functions
    for line in lines.entry_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(3)
    time.sleep(pauseTransition)
    if option == 1:
        footsteps.play()
        dialogue(lines.entry_line_2, dialogueSpeed, pauseTransition)
        schoolScene()
    elif option == 2:
        footsteps.play()
        dialogue(lines.entry_line_2, dialogueSpeed, pauseTransition)
        yardScene()
    elif option == 3:
        exitScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        entryOption()

def schoolScene():
    # call functions
    door_creak.play()
    dialogue(lines.school_line_1, dialogueSpeed, pauseTransition)
    schoolOption()

def schoolOption():
    # call functions
    for line in lines.school_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(6)
    time.sleep(pauseTransition)
    if option == 1:
        classScene()
    elif option == 2:
        staffScene()
    elif option == 3:
        lockerScene()
    elif option == 4:
        yardScene()
    elif option == 5:
        entryScene()
    elif option == 6:
        dialogue(lines.school_line_2, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(lines.school_line_3, dialogueSpeed, pauseTransition)
        bathroomScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        schoolOption()

################################################### CLASS ##############################################################
def classScene():
    # call functions
    door_open.play()
    dialogue(lines.class_line_1, dialogueSpeed, pauseTransition)
    classOption()

def classOption():
    if "itemStaffKeycard" in inventory:
        lines.class_option.pop()

    # call function
    for line in lines.class_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(len(lines.class_option))
    time.sleep(pauseTransition)
    if option == 1:
        paper.play()
        dialogue(lines.class_line_2, dialogueSpeed, pauseDialogue)
        dialogue(lines.class_line_3, dialogueSpeed, pauseDialogue)
        calendar.play()
        dialogue(lines.class_line_4, dialogueSpeed, pauseTransition)
        classOption()
    elif option == 2:
        dialogue(lines.class_line_5, dialogueSpeed, pauseTransition)
        dialogue(lines.class_line_6, dotSpeed, pauseTransition)
        dialogue(lines.class_line_7, dialogueSpeed, 3)
        dialogue(lines.class_line_8, dialogueSpeed, pauseTransition)
        classOption()
    elif option == 3:
        schoolScene()
    elif option == 4:
        dialogue(lines.class_line_9, dialogueSpeed, pauseDialogue)
        paper.play()
        dialogue(lines.class_line_10, dialogueSpeed, pauseDialogue)
        box.play()
        dialogue(lines.class_line_11, dialogueSpeed, pauseTransition)
        keycardOption()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        classOption()

def keycardOption():
    # call function
    for line in lines.key_card_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(lines.key_card_line_1, dialogueSpeed, pauseDialogue)
        zip_up.play()
        dialogue(lines.key_card_line_2, dialogueSpeed, pauseDialogue)
        success.play()
        dialogue(lines.key_card_line_3, dialogueSpeed, pauseTransition)
        inventory.append("itemStaffKeycard")
        classOption()
    elif option == 2:
        dialogue(lines.key_card_line_4, dialogueSpeed, pauseDialogue)
        zip_up.play()
        dialogue(lines.key_card_line_5, dialogueSpeed, pauseTransition)
        classOption()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        keycardOption()

################################################### STAFF ##############################################################
def staffScene():
    # call functions
    dialogue(lines.staff_line_1, dialogueSpeed, pauseDialogue)
    dialogue(lines.staff_line_2, dialogueSpeed, pauseTransition)
    staffOption()

def staffOption():
    # call functions
    for line in lines.staff_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    print("")
    time.sleep(pauseTransition)
    if option == 1:
        if "itemStaffKeycard" in inventory:
            door_locked.play()
            dialogue(lines.staff_line_3, dotSpeed, pauseTransition)
            dialogue(lines.staff_line_4, dialogueSpeed, pauseTransition)
            door_open.play()
            dialogue(lines.staff_line_5, dialogueSpeed, pauseDialogue)
            dialogue(lines.staff_line_6, dialogueSpeed, pauseTransition)
            cubicleOption()
        else:
            door_locked.play()
            dialogue(lines.staff_line_3, dotSpeed, pauseTransition)
            dialogue(lines.staff_line_4, dialogueSpeed, pauseTransition)
            staffOption()
    elif option == 2:
        footsteps.play()
        dialogue(lines.staff_line_7, dialogueSpeed, pauseTransition)
        schoolScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        staffOption()

def cubicleOption():
    # call functions
    for line in lines.cubicle_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(4)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(lines.cubicle_line_1, dialogueSpeed, pauseDialogue)
        time.sleep(pauseTransition)
        dialogue(lines.cubicle_line_2, dialogueSpeed, pauseDialogue)
        dialogue(lines.cubicle_line_3, dialogueSpeed, pauseTransition)
        hackOption()
    elif option == 2:
        calendar.play()
        dialogue(lines.cubicle_line_4, dialogueSpeed, pauseDialogue)
        dialogue(lines.cubicle_line_5, dialogueSpeed, pauseTransition)
        cubicleOption()
    elif option == 3:
        paper.play()
        dialogue(lines.cubicle_line_6, dialogueSpeed, pauseDialogue)
        calendar.play()
        dialogue(lines.cubicle_line_7, dialogueSpeed, pauseDialogue)
        dialogue(lines.cubicle_line_8, endingSpeed, pauseTransition)
        dialogue(lines.cubicle_line_9, dialogueSpeed, pauseDialogue)
        dialogue(lines.cubicle_line_10, dialogueSpeed, pauseDialogue)
        dialogue(lines.cubicle_line_11, dialogueSpeed, pauseDialogue)
        paper.play()
        dialogue(lines.cubicle_line_12, dialogueSpeed, pauseTransition)
        cubicleOption()
    elif option == 4:
        dialogue(lines.cubicle_line_13, dialogueSpeed, pauseDialogue)
        door_close.play()
        dialogue(lines.cubicle_line_14, dialogueSpeed, pauseTransition)
        schoolScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        cubicleOption()

def hackOption():
    # call functions
    for line in lines.hack_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(lines.hack_line_1, dialogueSpeed, pauseTransition)
        askPassword = "Password: \n"
        dialogue(askPassword, dialogueSpeed, 0)
        enteredPassword = input("   ")
        time.sleep(pauseTransition)
        if enteredPassword == "8970":
            success.play()
            dialogue(lines.hack_line_2, dialogueSpeed, pauseDialogue)
            dialogue(lines.hack_line_3, dialogueSpeed, pauseDialogue)
            time.sleep(pauseTransition)
            dialogue(lines.hack_line_4, dialogueSpeed, pauseDialogue)
            dialogue(lines.hack_line_5, dialogueSpeed, pauseDialogue)
            dialogue(lines.hack_line_6, dialogueSpeed, pauseDialogue)
            dialogue(lines.hack_line_7, dialogueSpeed, pauseTransition)
            global allowEscape
            allowEscape = True
            cubicleOption()
        else:
            error.play()
            dialogue(lines.hack_line_8, dialogueSpeed, pauseDialogue)
            dialogue(lines.hack_line_9, dialogueSpeed, pauseTransition)
            hackOption()
    elif option == 2:
        dialogue(lines.hack_line_10, dialogueSpeed, pauseTransition)
        cubicleOption()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        hackOption()

################################################### LOCKER #############################################################
def lockerScene():

    # call functions
    if "itemHomework" not in inventory:
        dialogue(lines.locker_line_1, dialogueSpeed, pauseTransition)
        lockerOption()
    else:
        dialogue(lines.locker_line_2, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(lines.locker_line_3, dialogueSpeed, pauseTransition)
        schoolScene()

def lockerOption():
    # call functions
    for line in lines.locker_option:
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
            dialogue(lines.locker_line_4, dialogueSpeed, pauseDialogue)
            dialogue(lines.locker_line_5, dialogueSpeed, pauseDialogue)
            dialogue(lines.locker_line_6, dialogueSpeed, pauseDialogue)
            success.play()
            dialogue(lines.locker_line_7, endingSpeed, pauseDialogue)
            dialogue(lines.locker_line_8, dialogueSpeed, pauseTransition)
            dialogue(lines.locker_line_9, dialogueSpeed, pauseTransition)
            dialogue(lines.locker_line_10, dialogueSpeed, pauseDialogue)
            dialogue(lines.locker_line_11, dialogueSpeed, pauseDialogue)
            locker_close.play()
            dialogue(lines.locker_line_12, dialogueSpeed, pauseDialogue)
            success.play()
            dialogue(lines.locker_line_13, endingSpeed, pauseTransition)
            inventory.append("itemHomework")
            inventory.append("itemSmallKey")
            schoolScene()
        else:
            locker_locked.play()
            dialogue(lines.locker_line_14, dialogueSpeed, pauseTransition)
            dialogue(lines.locker_line_15, dialogueSpeed, pauseTransition)
            lockerOption()
    elif option == 2:
        dialogue(lines.locker_line_16, dialogueSpeed, pauseTransition)
        schoolScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        lockerOption()

#################################################### YARD ##############################################################
def yardScene():

    # call functions
    door_creak.play()
    dialogue(lines.yard_line_1, dialogueSpeed, pauseTransition)
    yardOption()

def yardOption():
    if "itemFreshCake" in inventory:
        lines.yard_option.append("   (5) ..What is that in the distance?\n")

    # call function
    for line in lines.yard_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(len(lines.yard_option))
    time.sleep(pauseTransition)
    if option == 1:
        schoolScene()
    elif option == 2:
        dialogue(lines.yard_line_2, dialogueSpeed, pauseDialogue)
        dialogue(lines.yard_line_3, dialogueSpeed, pauseDialogue)
        dialogue(lines.yard_line_4, dialogueSpeed, pauseTransition)
        yardOption()
    elif option == 3:
        hiddenScene()
    elif option == 4:
        exitScene()
    elif option == 5 and "itemFreshCake" in inventory:
        dialogue(lines.yard_line_5, dialogueSpeed, pauseDialogue)
        pygame.mixer.music.pause()
        dialogue(lines.yard_line_6, dialogueSpeed, pauseTransition)
        vergilScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        yardOption()

################################################### BATHROOM ###########################################################
def bathroomTimer():
    totalSeconds = 5
    while totalSeconds > 0 and timerRunning:
        time.sleep(1)
        totalSeconds -= 1
    if totalSeconds == 0 and timerRunning:
        endingUrgent()

def bathroomScene():

    # call functions
    pygame.mixer.music.stop()
    door_creak.play()
    dialogue(lines.bathroom_line_1, dialogueSpeed, pauseDialogue)
    dialogue(lines.bathroom_line_2, dialogueSpeed, pauseDialogue)
    dialogue(lines.bathroom_line_3, dotSpeed, pauseTransition)
    dialogue(lines.bathroom_line_4, dialogueSpeed, pauseTransition)
    pygame.mixer.music.load(os.path.join(folder, 'silly_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(lines.bathroom_line_5, dialogueSpeed, pauseDialogue)
    dialogue(lines.bathroom_line_6, dialogueSpeed, pauseTransition)
    bathroomOption()

def bathroomOption():
    # dialogue
    if "itemGrenade" in inventory:
        lines.bathroom_option.append("   (3) Destroy everything.\n")

    # call functions
    for line in lines.bathroom_option:
        dialogue(line, optionSpeed, 0)

    global timerRunning
    timerRunning = True
    bathroomThread = threading.Thread(target=bathroomTimer)
    bathroomThread.start()

    # options
    option = chooseOption(len(lines.bathroom_option))
    time.sleep(pauseTransition)
    if option == 1:
        timerRunning = False
        pygame.mixer.music.stop()
        running.play()
        dialogue(lines.bathroom_line_7, dialogueSpeed, pauseTransition)
        dialogue(lines.bathroom_line_8, dialogueSpeed, pauseTransition)
        dialogue(lines.bathroom_line_9, dialogueSpeed, pauseTransition)
        dialogue(lines.bathroom_line_10, endingSpeed, pauseTransition)
        paperOption()
    elif option == 2:
        timerRunning = False
        dialogue(lines.bathroom_line_11, dialogueSpeed, pauseTransition)
        timerRunning = True
        bathroomOption()
    elif option == 3 and "itemGrenade" in inventory:
        timerRunning = False
        pygame.mixer.music.stop()
        endingCinema()
    else:
        timerRunning = False
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        timerRunning = True
        bathroomOption()

def paperOption():
    if allowEscape:
        lines.paper_option.append("   (3) I don't want any paper.\n")

    # call functions
    for line in lines.paper_option:
        heartbeat.play(loops=3)
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(len(lines.paper_option))
    time.sleep(pauseTransition)
    if option == 1:
        endingRed()
    elif option == 2:
        endingBlue()
    elif option == 3 and allowEscape:
        endingEscaped()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        paperOption()

#################################################### HIDDEN ############################################################
def hiddenScene():
    # call functions
    if 'itemFreshCake' or 'itemGrenade' in inventory:
        dialogue(lines.hidden_line_2, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(lines.hidden_line_3, dialogueSpeed, pauseTransition)
        yardScene()
    else:
        footsteps.play()
        dialogue(lines.hidden_line_1, dialogueSpeed, pauseTransition)
        hiddenOption()

def hiddenOption():
    # call functions
    for line in lines.hidden_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    print("")
    time.sleep(pauseTransition)
    if option == 1:
        if "itemSmallKey" in inventory:
            door_locked.play()
            dialogue(lines.hidden_line_4, dotSpeed, pauseTransition)
            dialogue(lines.hidden_line_5, dialogueSpeed, pauseTransition)
            dialogue(lines.hidden_line_6, dialogueSpeed, pauseDialogue)
            door_open.play()
            dialogue(lines.hidden_line_7, dialogueSpeed, pauseDialogue)
            dialogue(lines.hidden_line_8, dialogueSpeed, pauseTransition)
            boxOption()
        else:
            door_locked.play()
            dialogue(lines.hidden_line_4, dotSpeed, pauseTransition)
            dialogue(lines.hidden_line_5, dialogueSpeed, pauseTransition)
            hiddenOption()
    elif option == 2:
        dialogue(lines.hidden_line_9, dialogueSpeed, pauseDialogue)
        footsteps.play()
        dialogue(lines.hidden_line_10, dialogueSpeed, pauseTransition)
        yardScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        hiddenOption()

def boxOption():
    # call functions
    for line in lines.box_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        box.play()
        dialogue(lines.box_line_1, dialogueSpeed, pauseTransition)
        retrievedItem = random.choices(largeBox, weights=weights, k=1)[0]
        if retrievedItem == "itemRubberDuck":
            dialogue(lines.box_line_2, dialogueSpeed, pauseDialogue)
            dialogue(lines.box_line_3, dialogueSpeed, pauseTransition)
            weights.remove(35)
            largeBox.remove("itemRubberDuck")
            boxOption()
        elif retrievedItem == "itemChewedHomework":
            dialogue(lines.box_line_4, dialogueSpeed, pauseDialogue)
            dialogue(lines.box_line_5, dialogueSpeed, pauseTransition)
            weights.remove(35)
            largeBox.remove("itemChewedHomework")
            boxOption()
        elif retrievedItem == "itemFreshCake":
            dialogue(lines.box_line_6, dialogueSpeed, pauseDialogue)
            dialogue(lines.box_line_7, dialogueSpeed, pauseDialogue)
            zip_up.play()
            dialogue(lines.box_line_8, dialogueSpeed, pauseDialogue)
            success.play()
            dialogue(lines.box_line_9, dialogueSpeed, pauseDialogue)
            dialogue(lines.box_line_10, dialogueSpeed, pauseDialogue)
            footsteps.play()
            dialogue(lines.box_line_11, dialogueSpeed, pauseTransition)
            inventory.append("itemFreshCake")
            yardScene()
        else:
            dialogue(lines.box_line_12, dialogueSpeed, pauseDialogue)
            dialogue(lines.box_line_13, dialogueSpeed, pauseTransition)
            grenadeOption()
    elif option == 2:
        dialogue(lines.box_line_14, dialogueSpeed, pauseDialogue)
        door_close.play()
        dialogue(lines.box_line_15, dialogueSpeed, pauseTransition)
        yardScene()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        boxOption()

def grenadeOption():

    # call functions
    for line in lines.grenade_option:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        dialogue(lines.grenade_line_1, dialogueSpeed, pauseDialogue)
        success.play()
        dialogue(lines.grenade_line_2, endingSpeed, pauseDialogue)
        door_close.play()
        dialogue(lines.grenade_line_3, dialogueSpeed, pauseTransition)
        inventory.append("itemGrenade")
        yardScene()
    elif option == 2:
        dialogue(lines.grenade_line_4, dialogueSpeed, pauseTransition)
        weights.remove(20)
        largeBox.remove("itemGrenade")
        boxOption()
    else:
        dialogue(lines.option_error, dialogueSpeed, pauseTransition)
        grenadeOption()

#################################################### VERGIL ############################################################
def vergilScene():
    # call functions
    dialogue(vergilLine1, dialogueSpeed, pauseDialogue)
    dialogue(vergilLine2, dialogueSpeed, pauseTransition)
    vergilOption()

def vergilOption():
    # call functions
    for line in vergilOptions:
        dialogue(line, optionSpeed, 0)

    # options
    option = chooseOption(2)
    time.sleep(pauseTransition)
    if option == 1:
        endingVergil()
    elif option == 2:
        dialogue(vergilLine3, dialogueSpeed, pauseDialogue)
        pygame.mixer.music.unpause()
        footsteps.play()
        dialogue(vergilLine4, dialogueSpeed, pauseTransition)
        yardScene()
    else:
        dialogue(optionError, dialogueSpeed, pauseTransition)
        vergilOption()

#################################################### ENDINGS ###########################################################
def exitScene():
    if "itemGrenade" in inventory:
        pygame.mixer.music.pause()
        dialogue(falseEnding, dialogueSpeed, pauseTransition)
        pygame.mixer.music.unpause()
        entryScene()
    else:
        if "itemHomework" in inventory:
            pygame.mixer.music.load(os.path.join(folder, 'normal_ending.mp3'))
            pygame.mixer.music.play(-1)
            dialogue(endingFreed1, dialogueSpeed, pauseDialogue)
            footsteps.play()
            dialogue(endingFreed2, dialogueSpeed, pauseDialogue)
            dialogue(endingFreed3, endingSpeed, pauseTransition)
            if "endingFreed" not in endings:
                endings.append("endingFreed")
        else:
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
    pygame.mixer.music.stop()
    dialogue(endingUrgent1, dialogueSpeed, pauseDialogue)
    dialogue(endingUrgent2, dialogueSpeed, pauseDialogue)
    dialogue(endingUrgent3, endingSpeed, pauseTransition)
    if "endingUrgent" not in endings:
        endings.append(endingUrgent)

def endingRed():
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
        gameExplanation()
        gameRunning = True

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
        continue
    elif replay == "N" or replay == "NO":
        break
    else:
        dialogue(replayError, dialogueSpeed, pauseTransition)
        break

#################################################### QUIT GAME #########################################################
# call functions
dialogue(quitLine1, dialogueSpeed, pauseDialogue)
dialogue(quitLine2, dialogueSpeed, pauseTransition)

# quit
exit()