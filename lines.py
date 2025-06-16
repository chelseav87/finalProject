import time


def ask_username():
    name = input("Enter your name.\n   ")
    if name.strip() == "":
        time.sleep(0.5)
        print("..Please enter something.\n\n")
        ask_username()
    else:
        time.sleep(0.5)
        return name


username = ask_username()
endings = []

# errors
option_error = "..Please select one of the options.\n\n"
skip_error = "..Please enter Y or N.\n\n"
replay_error = "..I'm going to assume that's a no.\n"

# skip_intro()
skip_line = "Skip introduction? Y/N"

# game_explanation()
expl_line_1 = "When you are a young child,\033[0;49m this world will seem strange and foreign.\n\n"
expl_line_2 = "In this world of abnormalities,\033[0;49m you must traverse with caution.\n\n"
expl_line_3 = "Whatever happens will be a result of your choices,\033[1;31m so choose carefully.\033[0;49m \n\n"

# intro_scene()
intro_line_1 = "It's a calm, sunny afternoon, and you decide to walk home with a friend after a long day of " \
               "school.\033[0;49m You both ponder about assignments and upcoming tests, while occasionally teasing " \
               "each other and such.\033[0;49m Just then, you remember the homework that is due soon.\033[0;49m You " \
               "ask your friend if they want to stop by a cafe and work on it with you.\n\n"
intro_line_2 = "Your friend hesitates for a moment, stopping in their tracks, before beginning to rummage through " \
               "their bag.\033[0;49m You see their face gradually become worried.\n\n"
intro_line_3 = '"Shoot.\033[0;49m Did I forget my homework at school?"\n\n'
intro_line_4 = "You can see them panicking a bit.\033[0;49m You aren't exactly in a rush, so you wouldn't really " \
               "mind going back.\033[0;49m How about walking back together?\n\n"
intro_line_5 = '"No,\033[0;49m I have an important family event today, I REALLY need to go."\n\n'
intro_line_6 = "I mean, it's just homework, right?\033[0;49m It's not that big of a deal.\033[0;49m Surely Mr. W " \
               "wouldn't mind it if you missed it by just one day.\033[0;49m But then again, it is worth 89.70% of " \
               "your final grade..\n\n"
intro_line_7 = "Since you don't have any other plans and you're practically almost finished with your homework, " \
               "you offer to go back and get their homework for them.\033[0;49m They thank you profusely before you " \
               "go both your separate ways."

# entry_scene()
entry_option = ["   (1) Search inside the school.\n",
                "   (2) Search the schoolyard.\n",
                "   (3) Go home.\n"]
entry_line_1 = "You're back standing in front of the school.\033[0;49m It's only been a little while since you've " \
               "left, but it seems that everyone has gone home already.\033[0;49m It's eerily quiet here.\n\n"
entry_line_2 = "\nNevertheless, you swallow back that off-feeling, knowing that your friend is depending on you."

# school_scene()
school_option = ["   (1) Search the homeroom class.\n",
                 "   (2) Search the staff room.\n",
                 "   (3) Search your friend's locker.\n",
                 "   (4) Search the schoolyard.\n",
                 "   (5) Leave the school.\n",
                 "   (6) Go to the bathroom?\n"]
school_line_1 = "The sounds of the creaking school door echoes through the empty hallways.\033[0;49m There doesn't " \
                "seem to be anyone as you look around, but all of the lights are still on.\033[0;49m Surely there " \
                "should be some lingering teachers or students around?\n\n"
school_line_2 = "\nAll the bathrooms are locked after school hours.\033[0;49m However, there's always an open one " \
                "at the very end of the campus, but none of the staff actually know about it.\n\n"
school_line_3 = "Maybe there’s a chance that your friend left it in there.."

# class_scene()
class_option = ["   (1) Search the student desks.\n",
                "   (2) Look at the floor.\n",
                "   (3) Leave the classroom.\n",
                "   (4) Search Mr. W's desk.\n"]
class_line_1 = "As you look around the classroom, you don't see anyone except for some leftover schoolbags.\033[" \
               "0;49m Strange.\n\n"
class_line_2 = "\nYou search through each of the student's desks until you find what seems to be your friend's " \
               "desk.\033[0;49m You dig through, pulling out random papers in search of the homework.\n\n"
class_line_3 = "To your dismay, you don’t find it, so you quickly shove all the papers back into the desk, " \
               "lazily picking up some loose papers and putting them back in with the others.\n\n "
class_line_4 = "\nYou look down at the pristine, white floor, scanning for any loose papers..\n\n"
class_line_5 = "Oh! It’s the birthday letter you wrote for your friend.\033[0;49m Ah, right! Their birthday is the " \
               "same day as the homework’s due date.\033[0;49m Haha, what a birthday gift!\n\n"
class_line_6 = "You carefully slip the letter back into their desk, subtly laughing to yourself."
class_line_7 = "..."
class_line_8 = "\n\nYou look at the floor harder..\n\n"
class_line_9 = "Uhm.\033[0;49m No homework here."
class_line_10 = "\nMaybe there's extra copies of the homework somewhere in here.\n\n"
class_line_11 = "You flip through the folders and rummage through his stuff.\033[0;49m Unfortunately, he doesn't " \
                "have any extras.\n\n"
class_line_12 = "However, as you search through Mr. W's bag, you do find a staff key card..\n\n"

key_card_option = ["   (1) Take it!\n",
                   "   (2) ..This is an invasion of privacy.\n"]
key_card_line_1 = "\nThis should be useful for later.\n\n"
key_card_line_2 = "Like the kleptomaniac you are, you psych yourself up before taking the key card and slipping it " \
                  "into your pocket.\n\n"
key_card_line_3 = "\033[38;5;14mOBTAINED 'STAFF KEY CARD'\033[0;49m"
key_card_line_4 = "\nOkay, coward.\n\n"
key_card_line_5 = "You zip up the bag, brushing it off before setting it back down onto the floor."

# staff_scene()
staff_option = ["   (1) Search inside the staff room.\n",
                "   (2) Leave.\n"]
staff_line_1 = "Well, since there seems to be no one around, you could probably search the staff room.\033[0;49m " \
               "Cautiously, you peek inside to see if there's anyone inside.\n\n"
staff_line_2 = "Of course, it's empty.\n\n"
staff_line_3 = "..."
staff_line_4 = "\n\nAh, of course.\033[0;49m The door can only be unlocked by staff.."
staff_line_5 = "\n\nYou fish for the key card in your pocket and swipe it through the door's sensor.\033[0;49m The " \
               "door opens with a click, slowly cracking open as you cautiously look around once more.\n\n"
staff_line_6 = "You quickly find Mr. W's cubicle.\033[0;49m Scanning through, there is a laptop, a calendar, " \
               "several piles of schoolwork, and several scattered pens.\n\n"
staff_line_7 = "You aren't supposed to be here, anyway."

cubicle_option = ["   (1) Use the laptop.\n",
                  "   (2) Examine the calendar.\n",
                  "   (3) Search the piles of schoolwork.\n",
                  "   (4) Leave.\n"]
cubicle_line_1 = "\nYYou open up the laptop, but it’s locked behind a four-digit PIN.\n\n"
cubicle_line_2 = "\nThe calendar is hung on the inner sidewall of the cubicle, skipped to April.\033[0;49m It has " \
                 "several markings with dates for meetings and assignment due dates, including the homework's due " \
                 "date next Monday.\n\n"
cubicle_line_3 = "There’s also a small yellow sticky note at the bottom of the calendar..\n\n"
cubicle_line_4 = "Other than that, nothing seems to be very significant."
cubicle_line_5 = "\nYou dig through the piles of schoolwork, pulling out several marked and unmarked assignments " \
                 "from students.\033[0;49m You catch a glimpse of your name in the sea of paper.\033[0;49m It's the " \
                 "unit test from last Friday!\n\n"
cubicle_line_6 = "You scan the top of your paper..\n\n"
cubicle_line_7 = f'   "{username},\033[0;49m Period: 1,\033[0;49m April 11.."\n\n'
cubicle_line_8 = "..Huh?\n\n"
cubicle_line_9 = "..Is that a 65%?\033[0;49m Here you thought you aced this test.\033[0;49m Wow, and it looks like " \
                 "everyone else did really well.\n\n"
cubicle_line_10 = "Other than that, there's no extra homework lying around.\n\n"
cubicle_line_11 = "Frustrated, you carefully stack up the papers back to its original state, as if no one touched it."
cubicle_line_12 = "\nYeah, that's enough snooping around for now.\033[0;49m You didn't find any homework, " \
                  "but whatever.\033[0;49m You wouldn't want to go through the trouble of searching or printing out " \
                  "a whole new copy without anyone noticing, anyway.\n\n"
cubicle_line_13 = "You turn back around and leave the staff room, softly closing the door behind you."

hack_option = ["   (1) Enter the password.\n",
               "   (2) Forget it.\n"]
hack_line_1 = "\nPassword Hint:"
hack_line_2 = "\n..Got it!\n\n"
hack_line_3 = "The laptop unlocks before you as you celebrate internally.\033[0;49m However, before you can navigate " \
              "through it, an open tab catches your eye.\033[0;49m It seems to be a report of a missing student at " \
              "this school.\033[0;49m On a separate tab, a low quality depiction of a masked figure wearing a red " \
              "cloak nearly makes you jump out of your seat.\n\n"
hack_line_4 = "\nThat image is..\033[0;49m Very creepy.\n\n"
hack_line_5 = "It's rumored that the student's disappearance was due to a supernatural entity in one of the school " \
              "bathrooms.\033[0;49m You've heard claims of another student who survived the spirit by outsmarting " \
              "it.\033[0;49m You never really believed it, but concerning the amount of disappearances recently, " \
              "it might actually be real.\n\n"
hack_line_6 = "Was Mr. W investigating this, perhaps?\033[0;49m Could there actually be a serial killer hiding at " \
              "this school?\n\n"
hack_line_7 = "You're seriously unnerved.\033[0;49m Forgetting what you were originally searching for, you close " \
              "the laptop and set it aside with a newly instilled feeling of fear.\n"
hack_line_8 = "\n..Incorrect. Maybe there is a clue around here somewhere?\n\n"
hack_line_9 = "\nThere's no way you're gonna spend the whole day trying to hack into your teacher's computer.\n\n"

# locker_scene()
locker_option = ["   (1) Try to unlock it.\n",
                 "   (2) Leave.\n"]
locker_line_1 = "It would make the most sense to search here.\033[0;49m The locker is locked with a combination " \
                "padlock with four dials.\033[0;49m You could ask your friend for their passcode, but they're " \
                "probably really busy at the moment.\n\n"
locker_line_2 = "No need to search here anymore.\n\n"
locker_line_3 = "You turn around and leave the locker alone.\n\n"
locker_line_4 = "\n..Got it!\033[0;49m Wasn't too hard.\n\n"
locker_line_5 = "The lock comes off, and you scan through the locker for..\n\n"
locker_line_6 = "Homework!\033[0;49m Yes!\n\n"
locker_line_7 = "\033[38;5;14mOBTAINED 'HOMEWORK'\033[0;49m\n\n"
locker_line_8 = "You quickly snatch your friend's homework, and stuff it into your bag.\033[0;49m You turn around " \
                "and..\n\n"
locker_line_9 = "..Huh?\n\n"
locker_line_10 = "Something falls out and clatters onto the floor.\033[0;49m You pick it up and examine it.\n\n"
locker_line_11 = f'It is a small, antique-looking key, attached with a small tag with the name.. "{username}"?\033[' \
                 f'0;49m Is it addressed to you?\n\n'
locker_line_12 = "They must've anticipated this.\033[0;49m You slip the small key carefully into your pocket, " \
                 "closing the locker before setting off once more.\n\n"
locker_line_13 = "\033[38;5;14mOBTAINED 'SMALL KEY'\033[0;49m"
locker_line_14 = "\n..Hmm, that's not it.\n\n"
locker_line_15 = "Maybe their passcode has to do with an important date."
locker_line_16 = "\nIt's going to take forever to guess their passcode.\033[0;49m Might as well just give up now."

# yard_scene()
yard_option = ["   (1) Search inside the school.\n",
               "   (2) Search near the fences.\n",
               "   (3) Search that room at the very end of the school.\n",
               "   (4) Go home.\n"]
yard_line_1 = "You recall how you and your friend were outside studying during lunchtime.\033[0;49m Maybe they just " \
              "forgot their homework here?\n\n"
yard_line_2 = "\nYou examine the fence for any loose papers.\n\n"
yard_line_3 = "Unfortunately, there doesn't seem to be anything except abandoned coffee cups and takeout boxes " \
              "littered around.\n\n"
yard_line_4 = "Hopefully it didn't fly away.."
yard_line_5 = "\nAt the highest point of the field, you spot a mysterious object.\033[0;49m Has that always been " \
              "there?\n\n"
yard_line_6 = "You decide to approach it out of curiosity."

# bathroom_scene()
bathroom_option = ["   (1) Use the stall.\n",
                   "   (2) Leave.\n"]
bathroom_line_1 = "You slowly open the door, and are immediately welcomed by a dimly lit room and a disgusting " \
                  "stench.\033[0;49m Repulsed, you quickly cover your nose with your shirt.\033[0;49m This place " \
                  "clearly hasn't been maintained recently.\n\n"
bathroom_line_2 = "Unsurprisingly, none of the stalls seem to be working, except for the one at the very end of the " \
                  "room.\n\n"
bathroom_line_3 = "..."
bathroom_line_4 = "\n\nYou feel a shiver run up your spine.\033[0;49m Is it the eeriness of the bathroom, or..\n\n"
bathroom_line_5 = "..the sudden strong urge to go relieve yourself.\033[0;49m You clearly don't remember drinking a " \
                  "ton of water beforehand, where did this come from?!\n\n"
bathroom_line_6 = "You need to use the stall immediately.\n\n"
bathroom_line_7 = "\nYou quickly rush over to the last bathroom stall, sitting down on the toilet and doing your " \
                  "business.\033[0;49m However, when you look down to grab some toilet paper..\n\n"
bathroom_line_8 = "..None.\033[0;49m There's nothing left.\n\n"
bathroom_line_9 = "Just then, you see a figure approaching.\n\n"
bathroom_line_10 = '"Red paper or blue paper?"\n\n'
bathroom_line_11 = "\nYou can't leave now!\033[0;49m You have to go,\033[0;49m like,\033[0;49m really bad!"

paper_option = ["   (1) Red paper.\n",
                "   (2) Blue paper.\n"]

# hidden_scene()
hidden_option = ["   (1) Open the door.\n",
                 "   (2) Leave.\n"]
hidden_line_1 = "You approach the room at the far corner of the school.\033[0;49m The entire door has been painted " \
                "the same color as the walls, as if to hide itself.\033[0;49m Ominous!\n\n"
hidden_line_2 = "No need to search here anymore.\n\n"
hidden_line_3 = "You turn around and walk back to the yard.\n\n"
hidden_line_4 = "..."
hidden_line_5 = "\n\nLocked.\033[0;49m Looks like it can only be opened with a key.."
hidden_line_6 = "\n\nYou fish for the key in your pocket and insert it into the keyhole, pulling the door " \
                "open.\033[0;49m Immediately, dust starts flying everywhere.\033[0;49m Seems like no one has been " \
                "here in ages..\n\n "
hidden_line_7 = "You turn on the lights, quickly scanning the room for your friend's homework.\033[0;49m Of course, " \
                "you don't see it.\n\n"
hidden_line_8 = "However, something else catches your attention.\033[0;49m A large open box, sitting at the very " \
                "corner of the room.\033[0;49m It's filled up with tons of random objects.\033[0;49m Perhaps these " \
                "are all confiscated items?\n\n"
hidden_line_9 = "Well, it's not like your friend's homework is going to be in here anyway.\n\n"
hidden_line_10 = "You turn around and walk back to the yard."

box_option = ["   (1) Dig through the box.\n",
              "   (2) Maybe you should leave it alone.\n"]
box_line_1 = "\nYou dig through the box and pull out..\n\n"
box_line_2 = "..A rubber duck!\n\n"
box_line_3 = "Hello there!\033[0;49m Maybe you should bring it back home.\033[0;49m It would be nice to have a " \
             "bathtub friend."
box_line_4 = "..Half-eaten homework!\n\n"
box_line_5 = "Hey, you found homework!\033[0;49m It's pretty chewed up though, and you remember that your friend " \
             "does not have a dog."
box_line_6 = "..A pastry box?\n\n"
box_line_7 = "Upon closer inspection, you discover that there is a slice of cake inside.\033[0;49m Even though it " \
             "has been sitting here for so long, it seems to be in perfect condition.\n\n"
box_line_8 = "For whatever reason, you can't seem to let it go, like it was meant for you specifically.\033[0;49m " \
             "You carefully bury the pastry box deep within your bag, as you sense a heavy feeling from deep " \
             "inside you.\n\n"
box_line_9 = "\033[38;5;14mOBTAINED 'FRESH CAKE'\033[0;49m\n\n"
box_line_10 = "Or you know,\033[0;49m maybe you're just hungry.\n\n"
box_line_11 = "You leave the dusty room and go back into the yard."
box_line_12 = "..A grenade?! What the heck?!\n\n"
box_line_13 = "Should you take it?"
box_line_14 = "\nIt would probably be best not to mess with it.\033[0;49m Who knows, maybe there's some spiders " \
              "hiding in there.\n\n"
box_line_15 = "Well, looks like there's nothing else here.\033[0;49m You turn around and walk back to the yard."

grenade_option = ["   (1) Yes!\n",
                  "   (2) Absolutely not.\n"]
grenade_line_1 = "\nWhoa, seriously?\033[0;49m No second thoughts..?\033[0;49m Uh, alright then.\033[0;49m You've " \
                 "acquired..\033[0;49m A grenade.\n\n"
grenade_line_2 = "\033[38;5;14mOBTAINED 'GRENADE'\033[0;49m\n\n"
grenade_line_3 = "You leave the dusty room and go back into the yard."
grenade_line_4 = "\nThat's an extremely dangerous weapon!\033[0;49m Probably should report it once you leave.\033[" \
                 "0;49m You carefully set it back down into the box."

# vergil_scene()
vergil_option = ["   (1) Sit down.\n",
                 "   (2) Leave.\n"]
vergil_line_1 = "As you come closer to it, you slowly begin to make it out.\033[0;49m There stood a lone katana, " \
                "leaning against a plastic white chair.\n\n"
vergil_line_2 = "It seems to be calling out to you.\n\n"
vergil_line_3 = "\nCryptic chairs that appear out of nowhere shall not be sat on!\033[0;49m Besides, you still have " \
                "homework to find.\033[0;49m Better not waste any more time.\n\n"
vergil_line_4 = "You turn around and return to the yard."

# exit_scene()
ending_false = "You try to leave the school grounds, but you suddenly feel an otherworldly presence pulling " \
               "you back.\033[0;49m Must be that weapon of yours, huh?\033[0;49m Invisible video game " \
               "barriers!\033[0;49m Looks like you're gonna have to turn around.\n\n"
ending_freed_1 = "You've successfully retrieved your friend's homework,\033[0;49m and now it's time to " \
                 "leave.\n\n"
ending_freed_2 = "As you walk away from the school,\033[0;49m that tense feeling inside of you slowly fades " \
                 "away with every step,\033[0;49m as you quickly make your way to your friend's " \
                 "home.\n\n\033[1;49m"
ending_freed_3 = "ENDING:\033[1;49m Freedom\033[0;49m"
ending_lied_1 = "..."
ending_lied_2 = "\n\nFor whatever reason,\033[0;49m you feel deeply unsettled.\033[0;49m No matter how hard " \
                "you try,\033[0;49m you can't shake that feeling off.\n\n"
ending_lied_3 = "You slowly turn around and hurry back home,\033[0;49m carrying a heavy heart and regret " \
                "for your false promise.\n\n\033[1;49m"
ending_lied_4 = "ENDING:\033[1;49m Something is wrong.\033[0;49m"
ending_urgent_1 = "Before you could take another step,\033[0;49m you realize that it's too late.\n\n"
ending_urgent_2 = "You couldn't hold it in anymore,\033[0;49m and you feel your dignity stream down your leg.\033[" \
                  "0;49m Gross!\033[0;49m Go get yourself cleaned up!\n\n\033[1;49m"
ending_urgent_3 = "ENDING:\033[1;49m mom, i wet the bed again :(\033[0;49m"
ending_red_1 = "The stall door slowly creaks open.\n\n"
ending_red_2 = "Suddenly,\033[0;49m flashes of red paint the walls surrounding you.\033[0;49m As you look down at " \
               "your trembling hands,\033[0;49m you see various slashes cut deep into you,\033[0;49m so much so " \
               "that you can no longer see your skin.\033[0;49m Your entire body weakens,\033[0;49m and you fall to " \
               "the ground with a sickening thud.\n\n"
ending_red_3 = "With one final breath,\033[0;49m you see a masked figure wearing a red cloak towering over you," \
               "\033[0;49m and everything fades to black.\n\n"
ending_red_4 = "You are dead.\n\n\033[1;49m"
ending_red_5 = "ENDING:\033[1;49m A Thousand Lacerations\033[0;49m"
ending_blue_1 = "The stall door slowly creaks open.\n\n"
ending_blue_2 = "Suddenly,\033[0;49m you feel the chest immediately compress.\033[0;49m You helplessly clutch at " \
                "your neck,\033[0;49m desperately gasping for the air escaping from your lungs.\033[0;49m Your " \
                "entire body weakens,\033[0;49m and you fall to the ground with a sickening thud.\n\n"
ending_blue_3 = "With one final breath,\033[0;49m you see a masked figure wearing a red cloak towering over you," \
                "\033[0;49m and everything fades to black.\n\n"
ending_blue_4 = "You are dead.\n\n\033[1;49m"
ending_blue_5 = "ENDING:\033[1;49m Out of Breath?\033[0;49m"
ending_escaped_1 = "..."
ending_escaped_2 = "\n\nNothing happens.\n\n"
ending_escaped_3 = "You sneak over to the next stall and slide under the stall door,\033[0;49m seeing the figure " \
                   "peering over the last stall in your peripheral view.\n\n"
ending_escaped_4 = "You quickly rush out of the school with a racing heart,\033[0;49m never daring to look " \
                   "back.\033[1;49m\n\n"
ending_escaped_5 = "ENDING:\033[1;49m 赤マント\033[0;49m"
ending_cinema_1 = "You reach into your backpack and pull out the explosive from earlier.\033[0;49m It's time to " \
                  "destroy this place,\033[0;49m once and for all.\n\n"
ending_cinema_2 = "With a sharp inhale,\033[0;49m you pull on the pin and immediately chuck it into the bathroom," \
                  "\033[0;49m closing the door behind you as you leave.\n\n"
ending_cinema_3 = "The once terrorizing bathroom engulfed in flames,\033[0;49m pieces of debris flying past you as " \
                  "you walk away in slow motion.\033[0;49m In the threat of imminent danger,\033[0;49m you emerged " \
                  "victorious.\n\n"
ending_cinema_4 = "No more missing students.\033[0;49m No more evil spirits.\033[0;49m No more urban legends.\n\n"
ending_cinema_5 = "It all ends here.\n\n\033[1;49m"
ending_cinema_6 = "ENDING:\033[1;49m Absolute Cinema.\033[0;49m"
ending_vergil_1 = "You sit down on the chair,\033[0;49m letting go of all the tension built up inside of you.\033[" \
                  "0;49m You don't even realize that the sky has turned cloudy.\n\n"
ending_vergil_2 = "A surge of \033[1;49mPOWER\033[0;49m washes over you,\033[0;49m as you sink deeper into the " \
                  "chair.\n\n"
ending_vergil_3 = "\033[1;49mA storm is approaching,\033[1;49m provoking the black clouds in isolation.\033[1;49m " \
                  "Reclaim your name,\033[1;49m for you are blessed.\033[0;49m\n\n"
ending_vergil_4 = "Maybe you should stay here for a while.\n\n\033[1;49m"
ending_vergil_5 = "ENDING:\033[1;49m Berried Delight" + " \U0001F370" + " "

# quit
replay_line = ["\n\n\n\033[0;49mPlay again? Y/N\n",
               "Discovered Endings: " + str(len(endings)) + "/8"]
quit_line_1 = f"Thank you for playing, {username}!"
quit_line_2 = "\nQuitting now.."
