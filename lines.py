optionError = "..Please select one of the options.\n\n"

# user_info()
ask_username = "Enter your name.\n"
user_error = "..Please enter something.\n\n"

# skip_intro()
skip_line = "Skip introduction? Y/N"
skip_error = "..Please enter Y or N.\n\n"

# game_explanation()
expl_line1 = "When you are a young child,\033[0;49m this world will seem strange and foreign.\n\n"
expl_line2 = "In this world of abnormalities,\033[0;49m you must traverse with caution.\n\n"
expl_line3 = "Whatever happens will be a result of your choices,\033[1;31m so choose carefully.\033[0;49m \n\n"

# intro_scene()
intro_line1 = "It's a calm, sunny afternoon, and you decide to walk home with a friend after a long day of " \
             "school.\033[0;49m You both ponder about assignments and upcoming tests, while occasionally teasing " \
             "each other and such.\033[0;49m Just then, you remember the homework that is due soon.\033[0;49m You " \
             "ask your friend if they want to stop by a cafe and work on it with you.\n\n"
intro_line2 = "Your friend hesitates for a moment, stopping in their tracks, before beginning to rummage through " \
             "their bag.\033[0;49m You see their face gradually become worried.\n\n"
intro_line3 = '"Shoot.\033[0;49m Did I forget my homework at school?"\n\n'
intro_line4 = "You can see them panicking a bit.\033[0;49m You aren't exactly in a rush, so you wouldn't really " \
             "mind going back.\033[0;49m How about walking back together?\n\n"
intro_line5 = '"No,\033[0;49m I have an important family event today, I REALLY need to go."\n\n'
intro_line6 = "I mean, it's just homework, right?\033[0;49m It's not that big of a deal.\033[0;49m Surely Mr. W " \
             "wouldn't mind it if you missed it by just one day.\033[0;49m But then again, it is worth 90% of " \
             "your final grade..\n\n"
intro_line7 = "Since you don't have any other plans and you're practically almost finished with your homework, " \
             "you offer to go back and get their homework for them.\033[0;49m They thank you profusely before you " \
             "go both your separate ways."

# entry_scene()
entryOptions = ["   (1) Search inside the school.\n",
                "   (2) Search the schoolyard.\n",
                "   (3) Go home.\n"]
entryLine1 = "You're back standing in front of the school.\033[0;49m It's only been a little while since you've " \
             "left, but it seems that everyone has gone home already.\033[0;49m It's eerily quiet here.\n\n"
entryLine2 = "\nNevertheless, you swallow back that off-feeling, knowing that your friend is depending on you."

# school_scene()
schoolOptions = ["   (1) Search the homeroom class.\n",
                 "   (2) Search the staff room.\n",
                 "   (3) Search your friend's locker.\n",
                 "   (4) Search the schoolyard.\n",
                 "   (5) Leave the school.\n",
                 "   (6) Go to the bathroom?\n"]
schoolLine1 = "The sounds of the creaking school door echoes through the empty hallways.\033[0;49m There doesn't " \
                  "seem to be anyone as you look around, but all of the lights are still on.\033[0;49m Surely there " \
                  "should be some lingering teachers or students around?\n\n"
schoolLine2 = "\nAll the bathrooms are locked after school hours.\033[0;49m However, there's always an open one " \
              "at the very end of the campus, but none of the staff actually know about it.\n\n"
schoolLine3 = "You're positive your friend wouldn't leave their homework in there, yet you really wanted to go " \
              "for some reason."

# class_scene()
classOptions = ["   (1) Search the student desks.\n",
                "   (2) Look at the floor.\n",
                "   (3) Leave the classroom.\n",
                "   (4) Search Mr. W's desk.\n"]
classLine1 = "As you look around the classroom, you don't see anyone except for some leftover schoolbags.\033[" \
             "0;49m Strange.\n\n"
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

key_cardOptions = ["   (1) Take it!\n",
                   "   (2) ..This is an invasion of privacy.\n"]
key_cardLine1 = "\nThis should be useful for later.\n\n"
key_cardLine2 = "Like the kleptomaniac you are, you psych yourself up before taking the keycard and slipping it " \
               "into your pocket.\n\n"
key_cardLine3 = "\033[38;5;14mOBTAINED 'STAFF KEYCARD'\033[0;49m"
key_cardLine4 = "\nOkay, scaredy-cat.\n\n"
key_cardLine5 = "You zip up the bag, brushing it off before setting it back down onto the floor."

# staff_scene()
staffOptions = ["   (1) Search inside the staff room.\n",
                "   (2) Leave.\n"]
staffLine1 = "Well, since there seems to be no one around, you could probably search the staff room.\033[0;49m " \
             "Cautiously, you peek inside to see if there's anyone inside.\n\n"
staffLine2 = "Of course, it's empty.\n\n"
staffLine3 = "..."
staffLine4 = "\n\nAh, of course.\033[0;49m The door can only be unlocked by staff.."
staffLine5 = "\n\nYou fish for the keycard in your pocket and swipe it through the door's sensor.\033[0;49m The " \
             "door opens with a click, slowly cracking open as you cautiously look around once more.\n\n"
staffLine6 = "You quickly find Mr. W's cubicle.\033[0;49m Scanning through, there is a laptop, a calendar, " \
             "several piles of schoolwork, and several scattered pens.\n\n"
staffLine7 = "You aren't supposed to be here, anyway."

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

# locker_scene()


# yard_scene()


# bathroom_scene()


# hidden_scene()


# vergil_scene()


# exit_scene()


# quit

