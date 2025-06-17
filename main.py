# import modules/packages
import random
import sys
import os
import threading
import time
import pygame
import lines
import ascii

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

# game variables
DIALOGUE_SPEED = 0.03
ENDING_SPEED = 0.05
DOT_SPEED = 0.5
OPTION_SPEED = 0.01
PAUSE_DIALOGUE = 0.5
PAUSE_TRANSITION = 1
weights = [35, 35, 10, 20]
inventory = []
prompts = []
endings = []
large_box = ["item_rubber_duck", "item_chewed_homework", "item_fresh_cake", "item_grenade"]
game_running = False
stop_timer = threading.Event()
timeout_occurred = False


# set text behaviour
def dialogue(story_line, parameter_speed, parameter_pause):
    for char in story_line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(parameter_speed)
    time.sleep(parameter_pause)


# clear console
def clear():
    if os.name == 'nt':
        _ = os.system('cls')


# set up options
def choose_option(number_of_options):  # teacher supplied
    option = 0
    while option < 1 or option > number_of_options:
        ask_option = "\n   1 to " + str(number_of_options) + " -> "
        dialogue(ask_option, DIALOGUE_SPEED, 0)

        option = input()
        if option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6':
            option = 0
        if option == '1' or option == '2' or option == '3' or option == '4' or option == '5' or option == '6':
            option = int(option)
        return option


def game_explanation():
    clear()
    dialogue(lines.expl_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.expl_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.expl_line_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    skip_intro()


def skip_intro():
    dialogue(lines.skip_line, DIALOGUE_SPEED, 0)

    skip = input("\n   ")
    time.sleep(PAUSE_TRANSITION)

    if skip.upper() == "N" or skip.upper() == "NO":
        clear()
        intro_scene()
    elif skip.upper() == "Y" or skip.upper() == "YES":
        clear()
        entry_scene()
    else:
        clear()
        dialogue(lines.skip_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        skip_intro()


def intro_scene():
    pygame.mixer.music.load(os.path.join(folder, 'intro_theme.mp3'))
    pygame.mixer.music.play(-1)

    footsteps.play()
    dialogue(lines.intro_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.intro_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.intro_line_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.intro_line_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.intro_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.intro_line_6, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    footsteps.play()
    dialogue(lines.intro_line_7, DIALOGUE_SPEED, PAUSE_TRANSITION)

    clear()
    entry_scene()


def entry_scene():
    pygame.mixer.music.load(os.path.join(folder, 'main_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(lines.entry_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
    entry_option()


def entry_option():
    for story_line in lines.entry_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(3)
    time.sleep(PAUSE_TRANSITION)
    # (1) Search inside the school.
    if option == 1:
        footsteps.play()
        dialogue(lines.entry_line_2, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        school_scene()
    # (2) Search the schoolyard.
    elif option == 2:
        footsteps.play()
        dialogue(lines.entry_line_2, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        yard_scene()
    # (3) Go home.
    elif option == 3:
        clear()
        exit_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        entry_option()


def school_scene():
    door_creak.play()
    dialogue(lines.school_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
    school_option()


def school_option():
    for story_line in lines.school_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(6)
    time.sleep(PAUSE_TRANSITION)
    # (1) Search the homeroom class.
    if option == 1:
        clear()
        class_scene()
    # (2) Search the staff room.
    elif option == 2:
        clear()
        staff_scene()
    # (3) Search your friend's locker.
    elif option == 3:
        clear()
        locker_scene()
    # (4) Search the schoolyard.
    elif option == 4:
        clear()
        yard_scene()
    # (5) Leave the school.
    elif option == 5:
        clear()
        entry_scene()
    # (6) Go to the bathroom?
    elif option == 6:
        dialogue(lines.school_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        footsteps.play()
        dialogue(lines.school_line_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        bathroom_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        school_option()


def class_scene():
    door_open.play()
    dialogue(lines.class_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
    class_option()


def class_option():
    for story_line in lines.class_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(4)
    time.sleep(PAUSE_TRANSITION)
    # (1) Search the student desks.
    if option == 1:
        paper.play()
        dialogue(lines.class_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        paper.play()
        dialogue(lines.class_line_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
        prompts.append("prompt_birthday")
        clear()
        class_option()
    # (2) Look at the floor.
    elif option == 2:
        if "prompt_important_date" in prompts:
            dialogue(lines.class_line_10, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.class_line_11, DIALOGUE_SPEED, PAUSE_TRANSITION)
        else:
            dialogue(lines.class_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
            if "prompt_birthday" in prompts:
                dialogue(lines.class_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
                calendar.play()
                dialogue(lines.class_line_6, DIALOGUE_SPEED, PAUSE_TRANSITION)
                prompts.append("prompt_important_date")
            else:
                dialogue(lines.class_line_7, DOT_SPEED, PAUSE_TRANSITION)
                dialogue(lines.class_line_8, DIALOGUE_SPEED, 2)
                dialogue(lines.class_line_9, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        class_option()
    # (3) Search. Mr. W's desk.
    elif option == 3:
        if "item_staff_key_card" not in inventory:
            dialogue(lines.class_line_12, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            paper.play()
            dialogue(lines.class_line_13, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            box.play()
            dialogue(lines.class_line_14, DIALOGUE_SPEED, PAUSE_TRANSITION)
            key_card_option()
        else:
            dialogue(lines.class_line_15, DIALOGUE_SPEED, PAUSE_TRANSITION)
            clear()
            class_option()
    # (4) Leave the classroom.
    elif option == 4:
        clear()
        school_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        class_option()


def key_card_option():
    for story_line in lines.key_card_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    time.sleep(PAUSE_TRANSITION)
    # (1) Take it!
    if option == 1:
        dialogue(lines.key_card_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        zip_up.play()
        dialogue(lines.key_card_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        success.play()
        dialogue(lines.key_card_line_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
        inventory.append("item_staff_key_card")
        clear()
        class_option()
    # (2) ..This is an invasion of privacy.
    elif option == 2:
        dialogue(lines.key_card_line_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        zip_up.play()
        dialogue(lines.key_card_line_5, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        class_option()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        key_card_option()


def staff_scene():
    dialogue(lines.staff_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.staff_line_2, DIALOGUE_SPEED, PAUSE_TRANSITION)
    staff_option()


def staff_option():
    for story_line in lines.staff_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    print("")
    time.sleep(PAUSE_TRANSITION)
    # (1) Search inside the staff room.
    if option == 1:
        if "item_staff_key_card" in inventory:
            door_locked.play()
            dialogue(lines.staff_line_3, DOT_SPEED, PAUSE_TRANSITION)
            dialogue(lines.staff_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
            door_open.play()
            dialogue(lines.staff_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.staff_line_6, DIALOGUE_SPEED, PAUSE_TRANSITION)
            cubicle_option()
        else:
            door_locked.play()
            dialogue(lines.staff_line_3, DOT_SPEED, PAUSE_TRANSITION)
            dialogue(lines.staff_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
            clear()
            staff_option()
    # (2) Leave.
    elif option == 2:
        footsteps.play()
        dialogue(lines.staff_line_7, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        school_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        staff_option()


def cubicle_option():
    for story_line in lines.cubicle_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(4)
    time.sleep(PAUSE_TRANSITION)
    # (1) Use the laptop.
    if option == 1:
        dialogue(lines.cubicle_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
        hack_option()
    # (2) Examine the calendar.
    elif option == 2:
        calendar.play()
        dialogue(lines.cubicle_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        dialogue(lines.cubicle_line_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        print(ascii.ASCII_HINT)
        print(input("   > Press enter to continue"))
        time.sleep(PAUSE_TRANSITION)
        dialogue(lines.cubicle_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        cubicle_option()
    # (3) Search the piles of schoolwork.
    elif option == 3:
        paper.play()
        dialogue(lines.cubicle_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        calendar.play()
        dialogue(lines.cubicle_line_6, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        dialogue(lines.cubicle_line_7, ENDING_SPEED, PAUSE_TRANSITION)
        dialogue(lines.cubicle_line_8, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        dialogue(lines.cubicle_line_9, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        dialogue(lines.cubicle_line_10, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        paper.play()
        dialogue(lines.cubicle_line_11, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        cubicle_option()
    # (4) Leave.
    elif option == 4:
        dialogue(lines.cubicle_line_12, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        door_close.play()
        dialogue(lines.cubicle_line_13, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        school_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        cubicle_option()


def hack_option():
    for story_line in lines.hack_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    time.sleep(PAUSE_TRANSITION)
    # (1) Enter the password.
    if option == 1:
        ask_pin = "\nPIN: \n"
        dialogue(ask_pin, DIALOGUE_SPEED, 0)
        entered_pin = input("   ")
        time.sleep(PAUSE_TRANSITION)
        if entered_pin == "8970":
            success.play()
            dialogue(lines.hack_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.hack_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            print(ascii.ASCII_AKAMANTO)
            print(input("   > Press enter to continue"))
            time.sleep(PAUSE_TRANSITION)
            dialogue(lines.hack_line_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.hack_line_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.hack_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.hack_line_6, DIALOGUE_SPEED, PAUSE_TRANSITION)
            prompts.append("prompt_escape")
            clear()
            cubicle_option()
        else:
            error.play()
            dialogue(lines.hack_line_7, DIALOGUE_SPEED, PAUSE_TRANSITION)
            clear()
            hack_option()
    # (2) Forget it.
    elif option == 2:
        dialogue(lines.hack_line_8, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        cubicle_option()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        hack_option()


def locker_scene():
    if "item_homework" not in inventory:
        dialogue(lines.locker_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        locker_option()
    else:
        dialogue(lines.locker_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        footsteps.play()
        dialogue(lines.locker_line_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        school_scene()


def locker_option():
    for story_line in lines.locker_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    time.sleep(PAUSE_TRANSITION)
    # (1) Try to unlock it.
    if option == 1:
        ask_passcode = "\nTurn dials to:   x|x|x|x\n"
        dialogue(ask_passcode, DIALOGUE_SPEED, 0)
        entered_passcode = input("   ")
        time.sleep(PAUSE_TRANSITION)
        if entered_passcode == "0421":
            locker_open.play()
            dialogue(lines.locker_line_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.locker_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.locker_line_6, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            success.play()
            dialogue(lines.locker_line_7, ENDING_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.locker_line_8, DIALOGUE_SPEED, PAUSE_TRANSITION)
            dialogue(lines.locker_line_9, DIALOGUE_SPEED, PAUSE_TRANSITION)
            dialogue(lines.locker_line_10, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.locker_line_11, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            locker_close.play()
            dialogue(lines.locker_line_12, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            success.play()
            dialogue(lines.locker_line_13, ENDING_SPEED, PAUSE_TRANSITION)
            inventory.append("item_homework")
            inventory.append("item_small_key")
            clear()
            school_scene()
        else:
            locker_locked.play()
            dialogue(lines.locker_line_14, DIALOGUE_SPEED, PAUSE_TRANSITION)
            dialogue(lines.locker_line_15, DIALOGUE_SPEED, PAUSE_TRANSITION)
            clear()
            locker_option()
    # (2) Leave.
    elif option == 2:
        dialogue(lines.locker_line_16, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        school_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        locker_option()


def yard_scene():
    door_creak.play()
    dialogue(lines.yard_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
    yard_option()


def yard_option():
    if "ite_fresh_cake" in inventory:
        lines.yard_option.append("   (5) ..What is that in the distance?\n")

    for story_line in lines.yard_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(len(lines.yard_option))
    time.sleep(PAUSE_TRANSITION)
    # (1) Search inside the school.
    if option == 1:
        clear()
        school_scene()
    # (2) Search near the fences.
    elif option == 2:
        dialogue(lines.yard_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        dialogue(lines.yard_line_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        dialogue(lines.yard_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        yard_option()
    # (3) Search that room at the very end of the school.
    elif option == 3:
        clear()
        hidden_scene()
    # (4) Go home.
    elif option == 4:
        clear()
        exit_scene()
    # (5) ..What is that in the distance?
    elif option == 5 and "item_fresh_cake" in inventory:
        dialogue(lines.yard_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        pygame.mixer.music.pause()
        dialogue(lines.yard_line_6, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        vergil_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        yard_option()


def bathroom_timer():
    total_seconds = 5
    while total_seconds > 0 and not stop_timer.is_set():
        time.sleep(1)
        total_seconds -= 1
    if total_seconds == 0 and not stop_timer.is_set():
        clear()
        ending_urgent()


def bathroom_scene():
    pygame.mixer.music.stop()
    door_creak.play()
    dialogue(lines.bathroom_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.bathroom_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.bathroom_line_3, DOT_SPEED, PAUSE_TRANSITION)
    dialogue(lines.bathroom_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
    pygame.mixer.music.load(os.path.join(folder, 'silly_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(lines.bathroom_line_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.bathroom_line_6, DIALOGUE_SPEED, PAUSE_TRANSITION)
    bathroom_option()


def bathroom_option():
    global timeout_occurred
    timeout_occurred = False

    if "item_grenade" in inventory:
        lines.bathroom_option.append("   (3) Destroy everything.\n")

    for story_line in lines.bathroom_option:
        dialogue(story_line, OPTION_SPEED, 0)

    stop_timer.clear()
    bathroom_thread = threading.Thread(target=bathroom_timer)
    bathroom_thread.start()

    option = choose_option(len(lines.bathroom_option))
    stop_timer.set()
    if bathroom_thread is not None:
        bathroom_thread.join()
    if timeout_occurred:
        return

    # (1) Use the stall.
    if option == 1:
        pygame.mixer.music.stop()
        running.play()
        dialogue(lines.bathroom_line_7, DIALOGUE_SPEED, PAUSE_TRANSITION)
        dialogue(lines.bathroom_line_8, DIALOGUE_SPEED, PAUSE_TRANSITION)
        dialogue(lines.bathroom_line_9, DIALOGUE_SPEED, PAUSE_TRANSITION)
        dialogue(lines.bathroom_line_10, ENDING_SPEED, PAUSE_TRANSITION)
        paper_option()
    # (2) Leave.
    elif option == 2:
        dialogue(lines.bathroom_line_11, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        bathroom_option()
    # (3) Destroy everything.
    elif option == 3 and "item_grenade" in inventory:
        pygame.mixer.music.stop()
        clear()
        ending_cinema()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        bathroom_option()


def paper_option():
    if "prompt_escape" in prompts:
        lines.paper_option.append("   (3) I don't want any paper.\n")

    for story_line in lines.paper_option:
        heartbeat.play()
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(len(lines.paper_option))
    time.sleep(PAUSE_TRANSITION)
    # (1) Red paper.
    if option == 1:
        clear()
        ending_red()
    # (2) Blue paper.
    elif option == 2:
        clear()
        ending_blue()
    # (3) I don't want any paper.
    elif option == 3 and "prompt_escape" in prompts:
        clear()
        ending_escaped()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        paper_option()


def hidden_scene():
    if 'item_fresh_cake' or 'item_grenade' in inventory:
        dialogue(lines.hidden_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        footsteps.play()
        dialogue(lines.hidden_line_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        yard_scene()
    else:
        footsteps.play()
        dialogue(lines.hidden_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
        hidden_option()


def hidden_option():
    for story_line in lines.hidden_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    print("")
    time.sleep(PAUSE_TRANSITION)
    # (1) Open the door.
    if option == 1:
        if "item_small_key" in inventory:
            door_locked.play()
            dialogue(lines.hidden_line_4, DOT_SPEED, PAUSE_TRANSITION)
            dialogue(lines.hidden_line_5, DIALOGUE_SPEED, PAUSE_TRANSITION)
            dialogue(lines.hidden_line_6, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            door_open.play()
            dialogue(lines.hidden_line_7, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.hidden_line_8, DIALOGUE_SPEED, PAUSE_TRANSITION)
            box_option()
        else:
            door_locked.play()
            dialogue(lines.hidden_line_4, DOT_SPEED, PAUSE_TRANSITION)
            dialogue(lines.hidden_line_5, DIALOGUE_SPEED, PAUSE_TRANSITION)
            clear()
            hidden_option()
    # (2) Leave.
    elif option == 2:
        dialogue(lines.hidden_line_9, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        footsteps.play()
        dialogue(lines.hidden_line_10, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        yard_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        hidden_option()


def box_option():
    for story_line in lines.box_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    time.sleep(PAUSE_TRANSITION)
    # (1) Dig through the box.
    if option == 1:
        box.play()
        dialogue(lines.box_line_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
        retrieved_item = random.choices(large_box, weights=weights, k=1)[0]
        if retrieved_item == "item_rubber_duck":
            dialogue(lines.box_line_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.box_line_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
            weights.remove(35)
            large_box.remove("item_rubber_duck")
            clear()
            box_option()
        elif retrieved_item == "item_chewed_homework":
            dialogue(lines.box_line_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.box_line_5, DIALOGUE_SPEED, PAUSE_TRANSITION)
            weights.remove(35)
            large_box.remove("item_chewed_homework")
            clear()
            box_option()
        elif retrieved_item == "item_fresh_cake":
            dialogue(lines.box_line_6, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.box_line_7, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            zip_up.play()
            dialogue(lines.box_line_8, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            success.play()
            dialogue(lines.box_line_9, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.box_line_10, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            footsteps.play()
            dialogue(lines.box_line_11, DIALOGUE_SPEED, PAUSE_TRANSITION)
            inventory.append("item_fresh_cake")
            clear()
            yard_scene()
        else:
            dialogue(lines.box_line_12, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.box_line_13, DIALOGUE_SPEED, PAUSE_TRANSITION)
            clear()
            grenade_option()
    # (2) Maybe you should leave it alone.
    elif option == 2:
        dialogue(lines.box_line_14, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        door_close.play()
        dialogue(lines.box_line_15, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        yard_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        box_option()


def grenade_option():
    for story_line in lines.grenade_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    time.sleep(PAUSE_TRANSITION)
    # (1) Yes!
    if option == 1:
        dialogue(lines.grenade_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        success.play()
        dialogue(lines.grenade_line_2, ENDING_SPEED, PAUSE_DIALOGUE)
        door_close.play()
        dialogue(lines.grenade_line_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
        inventory.append("item_grenade")
        clear()
        yard_scene()
    # (2) Absolutely not.
    elif option == 2:
        dialogue(lines.grenade_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        weights.remove(20)
        large_box.remove("item_grenade")
        box_option()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        grenade_option()


def vergil_scene():
    dialogue(lines.vergil_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.vergil_line_2, DIALOGUE_SPEED, PAUSE_TRANSITION)
    vergil_option()


def vergil_option():
    for story_line in lines.vergil_option:
        dialogue(story_line, OPTION_SPEED, 0)

    option = choose_option(2)
    time.sleep(PAUSE_TRANSITION)
    # (1) Sit down.
    if option == 1:
        clear()
        ending_vergil()
    # (2) Leave.
    elif option == 2:
        dialogue(lines.vergil_line_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
        pygame.mixer.music.unpause()
        footsteps.play()
        dialogue(lines.vergil_line_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        yard_scene()
    else:
        clear()
        dialogue(lines.option_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        vergil_option()


def exit_scene():
    if "item_grenade" in inventory:
        clear()
        pygame.mixer.music.pause()
        dialogue(lines.ending_false, DIALOGUE_SPEED, PAUSE_TRANSITION)
        clear()
        pygame.mixer.music.unpause()
        entry_scene()
    else:
        if "item_homework" in inventory:
            pygame.mixer.music.load(os.path.join(folder, 'normal_ending.mp3'))
            pygame.mixer.music.play(-1)
            dialogue(lines.ending_freed_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            footsteps.play()
            dialogue(lines.ending_freed_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.ending_freed_3, ENDING_SPEED, PAUSE_TRANSITION)
            if "ending_freed" not in endings:
                endings.append("ending_freed")
        else:
            pygame.mixer.music.stop()
            dialogue(lines.ending_lied_1, DOT_SPEED, PAUSE_TRANSITION)
            pygame.mixer.music.load(os.path.join(folder, 'off_ending.mp3'))
            pygame.mixer.music.play(-1)
            dialogue(lines.ending_lied_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            running.play()
            dialogue(lines.ending_lied_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
            dialogue(lines.ending_lied_4, ENDING_SPEED, PAUSE_TRANSITION)
            if "ending_lied" not in endings:
                endings.append("ending_lied")


def ending_urgent():
    global timeout_occurred
    timeout_occurred = True
    pygame.mixer.music.stop()
    dialogue(lines.ending_urgent_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_urgent_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_urgent_3, ENDING_SPEED, PAUSE_TRANSITION)
    if "ending_urgent" not in endings:
        endings.append("ending_urgent")


def ending_red():
    door_creak.play()
    dialogue(lines.ending_red_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
    slash.play()
    pygame.mixer.music.load(os.path.join(folder, 'dead_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(lines.ending_red_2, DIALOGUE_SPEED, PAUSE_TRANSITION)
    dialogue(lines.ending_red_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
    dialogue(lines.ending_red_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
    dialogue(lines.ending_red_5, ENDING_SPEED, PAUSE_TRANSITION)
    if "ending_red" not in endings:
        endings.append("ending_red")


def ending_blue():
    door_creak.play()
    dialogue(lines.ending_blue_1, DIALOGUE_SPEED, PAUSE_TRANSITION)
    gasp.play()
    pygame.mixer.music.load(os.path.join(folder, 'dead_theme.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(lines.ending_blue_2, DIALOGUE_SPEED, PAUSE_TRANSITION)
    dialogue(lines.ending_blue_3, DIALOGUE_SPEED, PAUSE_TRANSITION)
    dialogue(lines.ending_blue_4, DIALOGUE_SPEED, PAUSE_TRANSITION)
    dialogue(lines.ending_blue_5, ENDING_SPEED, PAUSE_TRANSITION)
    if "ending_blue" not in endings:
        endings.append("ending_blue")


def ending_escaped():
    pygame.mixer.music.stop()
    dialogue(lines.ending_escaped_1, DOT_SPEED, PAUSE_TRANSITION)
    dialogue(lines.ending_escaped_2, DIALOGUE_SPEED, PAUSE_TRANSITION)
    running.play()
    heartbeat.play()
    dialogue(lines.ending_escaped_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_escaped_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_escaped_5, ENDING_SPEED, PAUSE_TRANSITION)
    if "ending_escaped" not in endings:
        endings.append("ending_escaped")


def ending_cinema():
    pygame.mixer.music.stop()
    dialogue(lines.ending_cinema_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    grenade.play()
    dialogue(lines.ending_cinema_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    pygame.mixer.music.load(os.path.join(folder, 'POWER.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(lines.ending_cinema_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_cinema_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_cinema_5, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_cinema_6, ENDING_SPEED, PAUSE_TRANSITION)
    if "ending_cinema" not in endings:
        endings.append("ending_cinema")


def ending_vergil():
    dialogue(lines.ending_vergil_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    pygame.mixer.music.load(os.path.join(folder, 'POWER.mp3'))
    pygame.mixer.music.play(-1)
    dialogue(lines.ending_vergil_2, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_vergil_3, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_vergil_4, DIALOGUE_SPEED, PAUSE_DIALOGUE)
    dialogue(lines.ending_vergil_5, ENDING_SPEED, PAUSE_TRANSITION)
    if "ending_vergil" not in endings:
        endings.append("ending_vergil")


while True:
    if game_running:
        pygame.mixer.music.stop()
        entry_scene()
    else:
        cubicle_option()
        game_running = True

    # reset
    inventory.clear()
    prompts.clear()
    weights = [35, 35, 10, 20]
    large_box = ["item_rubber_duck", "item_chewed_homework", "item_fresh_cake", "item_grenade"]

    replay_line = ["\n\n\n\033[0;49mPlay again? Y/N\n",
                   "Discovered Endings: " + str(len(endings)) + "/8"]

    dialogue(replay_line, DIALOGUE_SPEED, 0)
    replay = input("\n   ")
    time.sleep(PAUSE_TRANSITION)

    if replay.upper() == "Y" or replay.upper() == "YES":
        clear()
        continue
    elif replay.upper() == "N" or replay.upper() == "NO":
        break
    else:
        clear()
        dialogue(lines.replay_error, DIALOGUE_SPEED, PAUSE_TRANSITION)
        break

clear()
pygame.mixer.music.stop()
dialogue(lines.quit_line_1, DIALOGUE_SPEED, PAUSE_DIALOGUE)
dialogue(lines.quit_line_2, DIALOGUE_SPEED, PAUSE_TRANSITION)

clear()
exit()
