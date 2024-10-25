# Import Commands
# To use, select 'Emulate in Terminal' option in Run Settings.
import os
import sys
from os import system, name

# Use this line to restart code from beginning (Does not update output if code is changed)
# os.execl(sys.executable, sys.executable, *sys.argv)

# Notes
# Dynamic Water: Crest Lake, Halgeis
# Zenith Earth: Obsidian Canyon, Xhia
# Cosmic Wind: Aurora Grotto, Mu'karr
# Onyx Fire: Sundrop Valley, Mu'karr
# Electron Lightning: Trudawn Mountain, Altaria
# Permafrost Ice: Snowlink Glacier, Altaria

# To-Do List
# Keep lookout for Mimi's Canon Last Name & Species - Change when revealed
# Spell Descriptions & Purposes
# Add Secret Locations for Mythic Elemental Spots
# Add Mt. Moonlight to Eklyptil's City Description in Locations Command
# Quill's College (before Guardianship)
# Remove Mythical Elements from Sectional Sigils (Aren't User's Magic)
# Sigil Descriptions in Character Sheets
# Mythical Elemental Descriptions in Magic Core Command

# Long-Term Projects
# QoL Output Clear Commands (If Possible)
# Backstories for all main characters (those without tragedy, tell story of how they got magic)
# Add Side Character Option to Character Selection & Describe characters who don't get full pages
# Add Side Locations Options to Each Continent for Locations Not in Any Town
    # Nabuga's Garden, Halgeis
# Home Command that Clears Output Window & Restarts Program
# Make Different Paths Traversable (Go from One Magic Directly to Another)
# Leave for Every Pathway

# Current Update Notes
# Moved Large Text Blocks into Separate Files to Read From (Code Readability)

# Clear Command
os.putenv('TERM', 'xterm')

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Line Location Storage
info_loc = []

# Introduction
infoBarrier = input("\033[1m" + "Phalmasia Info Database" + "\033[0m. Press 'Enter' to continue.").lower().strip()
while infoBarrier == "" or infoBarrier == "return":
    infoBarrier = input("To Enter a Content Chapter, Enter Its Name When Prompted.\nContents:\n| Characters\n| "
                        "Locations\n| Magic\n| Races\n| Chronicles\n\nLeave the database by entering 'Leave'.\n").lower().strip()

    while infoBarrier == "":
        infoBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
    while infoBarrier != "characters" and infoBarrier != "locations" and infoBarrier != "magic" and infoBarrier != "races" and infoBarrier != "chronicles" and infoBarrier != "leave":
        infoBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

    # Character Input Commands
    while infoBarrier == "characters":
        characterBarrier = input("Characters:\n| Xaeyz Kai\n| Mirago Fynae\n| Yggdrasil (Yggdra) Aensyll\n| Cidelli ("
                                 "Cid) Reimora\n| Mimi Seiran\n| Kimiko Quintai\n| Aeiyou Drefael\n| Kinto Verali\n| "
                                 "Amiru Soaren\n| Turcobé Sentai\n| Yumeizu Artilux\n| Ryner Khabunago\n| Sereina "
                                 "Fynae\n\nLeave the database by entering 'Leave'. Go back to the home prompt by "
                                 "entering 'Back'.\n").lower().strip()

        while characterBarrier == "":
            characterBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while characterBarrier != "xaeyz kai" and characterBarrier != "xaeyz" and characterBarrier != "yggdrasil aensyll" and characterBarrier != "yggdra" and characterBarrier != "yggdrasil" and characterBarrier != "cidelli reimora" and characterBarrier != "cid" and characterBarrier != "cidelli" and characterBarrier != "mimi seiran" and characterBarrier != "mimi" and characterBarrier != "kimiko quintai" and characterBarrier != "kimiko" and characterBarrier != "aeiyou drefael" and characterBarrier != "aeiyou" and characterBarrier != "kinto verali" and characterBarrier != "kinto" and characterBarrier != "amiru soaren" and characterBarrier != "amiru" and characterBarrier != "turcobe sentai" and characterBarrier != "turcobe" and characterBarrier != "turcobé sentai" and characterBarrier != "turcobé" and characterBarrier != "yumeizu artilux" and characterBarrier != "yumeizu" and characterBarrier != "mirago fynae" and characterBarrier != "mirago" and characterBarrier != "ryner khabunago" and characterBarrier != "ryner" and characterBarrier != "sereina fynae" and characterBarrier != "sereina" and characterBarrier != "leave" and characterBarrier != "back":
            characterBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Xaeyz Kai
        while characterBarrier == "xaeyz kai" or characterBarrier == "xaeyz":
            info_loc = []
            for i in range(3, 84, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            xaeyzChapterPrompt = input(
                "\nEnter 'Chapters' to view the chapters of Xaeyz's Backstory. Enter 'Back' to return to Character Selection.\n").lower().strip()
            while xaeyzChapterPrompt == "chapters":
                xaeyzChapterPrompt = input("Xaeyz's Backstory\n\n| Chapter 1: The Day of Black Sun\n| Chapter 2: The "
                                           "Aurora Scythe\n| Chapter 3: The Forest's Shadow\n| Chapter 4: Hozura the "
                                           "Flame\n\nPress 'Enter' to return to Xaeyz's Biography.\n").lower().strip()

                if xaeyzChapterPrompt == "":
                    break
                if xaeyzChapterPrompt != "chapters" and xaeyzChapterPrompt != "chapter 1" and xaeyzChapterPrompt != "chapter one" and xaeyzChapterPrompt != "the day of black sun" and xaeyzChapterPrompt != "day of the black sun" and xaeyzChapterPrompt != "chapter 2" and xaeyzChapterPrompt != "chapter two" and xaeyzChapterPrompt != "the aurora scythe" and xaeyzChapterPrompt != "aurora scythe" and xaeyzChapterPrompt != "chapter 3" and xaeyzChapterPrompt != "chapter three" and xaeyzChapterPrompt != "the forest's shadow" or xaeyzChapterPrompt == "the forests shadow" or xaeyzChapterPrompt == "the forests shadow" and xaeyzChapterPrompt != "forests shadow" and xaeyzChapterPrompt != "chapter 4" and xaeyzChapterPrompt != "chapter four" and xaeyzChapterPrompt != "hozura the flame" and xaeyzChapterPrompt != "":
                    xaeyzChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. "
                                               "Please re-enter your search.").lower().strip()

                xaeyzChapterOne, xaeyzChapterTwo, xaeyzChapterThree, xaeyzChapterFour = "", "", "", ""
                # Xaeyz Kai Backstory Chapter 1
                if xaeyzChapterPrompt == "chapter 1" or xaeyzChapterPrompt == "chapter one" or xaeyzChapterPrompt == "the day of black sun" or xaeyzChapterPrompt == "day of black sun":
                    info_loc = []
                    for i in range(4, 21, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    xaeyzChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                # Xaeyz Kai Backstory Chapter 2
                if xaeyzChapterPrompt == "chapter 2" or xaeyzChapterPrompt == "chapter two" or xaeyzChapterPrompt == "the aurora scythe" or xaeyzChapterPrompt == "aurora scythe" or xaeyzChapterOne == "next":
                    info_loc = []
                    for i in range(24, 47, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    xaeyzChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                # Xaeyz Kai Backstory Chapter 3
                if xaeyzChapterPrompt == "chapter 3" or xaeyzChapterPrompt == "chapter three" or xaeyzChapterPrompt == "the forest's shadow" or xaeyzChapterPrompt == "the forests shadow" or xaeyzChapterPrompt == "forest's shadow" or xaeyzChapterPrompt == "forests shadow" or xaeyzChapterTwo == "next":
                    info_loc = []
                    for i in range(50, 61, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    xaeyzChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                # Xaeyz Kai Backstory Chapter 4
                if xaeyzChapterPrompt == "chapter 4" or xaeyzChapterPrompt == "chapter four" or xaeyzChapterPrompt == "hozura the flame" or xaeyzChapterThree == "next":
                    info_loc = []
                    for i in range(64, 85, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    xaeyzChapterFour = input("\nThis is the end of Xaeyz's Bio. Press 'Enter' to return to chapter selection.\n").lower().strip()

                if xaeyzChapterOne == "" or xaeyzChapterTwo == "" or xaeyzChapterThree == "" or xaeyzChapterFour == "":
                    xaeyzChapterPrompt = "chapters"
                if xaeyzChapterOne != "chapters" and xaeyzChapterOne != "" and xaeyzChapterTwo != "chapters" and xaeyzChapterTwo != "" and xaeyzChapterThree != "chapters" and xaeyzChapterThree != "" and xaeyzChapterFour != "chapters" and xaeyzChapterFour != "":
                    xaeyzChapterOne = input("\nYou may have pressed enter on accident or misspelled your search. "
                                            "Please re-enter your search.").lower().strip()

            if xaeyzChapterPrompt == "back":
                break
            if xaeyzChapterPrompt != "chapters" and xaeyzChapterPrompt != "back" and xaeyzChapterPrompt != "":
                xaeyzChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. "
                                           "Please re-enter your search.").lower().strip()

        # Mirago Fynae
        while characterBarrier == "mirago fynae" or characterBarrier == "mirago":
            info_loc = []
            for i in range(88, 160, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            miragoChapterPrompt = input("\nEnter 'Chapters' to view the chapters of Mirago's Backstory. Enter 'Back' to return to Character Selection.\n").lower().strip()
            while miragoChapterPrompt == "chapters":
                miragoChapterPrompt = input("Mirago's Backstory\n\n| Chapter 1: Onyx Fire\n| Chapter 2: Meeting "
                                            "Xaeyz\n| Chapter 3: A Final Stand\n| Chapter 4: Rebirth & The *Sundrop "
                                            "Valley*\n\nPress 'Enter' to return to Mirago's Biography.\n").lower().strip()

                if miragoChapterPrompt == "":
                    break
                if miragoChapterPrompt != "chapters" and miragoChapterPrompt != "chapter 1" and miragoChapterPrompt != "chapter one" and miragoChapterPrompt != "onyx fire" and miragoChapterPrompt != "chapter 2" and miragoChapterPrompt != "chapter two" and miragoChapterPrompt != "meeting xaeyz" and miragoChapterPrompt != "chapter 3" and miragoChapterPrompt != "chapter three" and miragoChapterPrompt != "a final stand" and miragoChapterPrompt != "chapter 4" and miragoChapterPrompt != "chapter four" and miragoChapterPrompt != "rebirth & the sundrop valley" and miragoChapterPrompt != "rebirth and the sundrop valley" and miragoChapterPrompt != "":
                    miragoChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. "
                                                "Please re-enter your search.").lower().strip()

                miragoChapterOne, miragoChapterTwo, miragoChapterThree, miragoChapterFour = "", "", "", ""
                # Mirago Backstory Chapter 1
                if miragoChapterPrompt == "chapter 1" or miragoChapterPrompt == "chapter one" or miragoChapterPrompt == "onyx fire":
                    info_loc = []
                    for i in range(90, 105, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    miragoChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                # Mirago Backstory Chapter 2
                if miragoChapterPrompt == "chapter 2" or miragoChapterPrompt == "chapter two" or miragoChapterPrompt == "meeting xaeyz" or miragoChapterOne == "next":
                    info_loc = []
                    for i in range(108, 123, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    miragoChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                # Mirago Backstory Chapter 3
                if miragoChapterPrompt == "chapter 3" or miragoChapterPrompt == "chapter three" or miragoChapterPrompt == "a final stand" or miragoChapterTwo == "next":
                    info_loc = []
                    for i in range(126, 137, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    miragoChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                # Mirago Backstory Chapter 4
                if miragoChapterPrompt == "chapter 4" or miragoChapterPrompt == "chapter four" or miragoChapterPrompt == "rebirth & the sundrop valley" or miragoChapterPrompt == "rebirth and the sundrop valley" or miragoChapterThree == "next":
                    info_loc = []
                    for i in range(140, 155, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    miragoChapterFour = input("\nThis is the end of Mirago's Bio. Press 'Enter' to return to chapter selection.\n").lower().strip()

                if miragoChapterOne == "" or miragoChapterTwo == "" or miragoChapterThree == "" or miragoChapterFour == "":
                    miragoChapterPrompt = "chapters"
                if miragoChapterOne != "chapters" and miragoChapterOne != "" and miragoChapterTwo != "chapters" and miragoChapterTwo != "" and miragoChapterThree != "chapters" and miragoChapterThree != "" and miragoChapterFour != "chapters" and miragoChapterFour != "":
                    miragoChapterOne = input("\nYou may have pressed enter on accident or misspelled your search. "
                                             "Please re-enter your search.").lower().strip()

            if miragoChapterPrompt == "back":
                break
            if miragoChapterPrompt != "chapters" and miragoChapterPrompt != "back" and miragoChapterPrompt != "":
                miragoChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. "
                                            "Please re-enter your search.").lower().strip()

        # Yggdrasil Aensyll Bio
        while characterBarrier == "yggdrasil aensyll" or characterBarrier == "yggdra" or characterBarrier == "yggdrasil":
            info_loc = []
            for i in range(164, 197, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            yggdraChapterPrompt = input("\nEnter 'Chapters' to view the chapters of Yggdra's Backstory. Enter 'Back' to return to Character Selection.\n").lower().strip()
            while yggdraChapterPrompt == "chapters":
                yggdraChapterPrompt = input("Yggdra's Backstory\nPlease enter the chapter number to see a chapter ("
                                            "Chapter 1)\n\n| Chapter 1: A Time for Firsts & Lasts\n| Chapter 2: A "
                                            "Goodbye\n| Chapter 3: A Darkened Mind\n| Chapter 4: New Dreams\n\nPress "
                                            "'Enter' to return to Yggdra's Biography.\n").lower().strip()

                if yggdraChapterPrompt == "":
                    break
                if yggdraChapterPrompt != "chapters" and yggdraChapterPrompt != "chapter 1" and yggdraChapterPrompt != "chapter one" and yggdraChapterPrompt != "a time for firsts and lasts" and yggdraChapterPrompt != "chapter 2" and yggdraChapterPrompt != "chapter two" and yggdraChapterPrompt != "a goodbye" and yggdraChapterPrompt != "chapter 3" and yggdraChapterPrompt != "chapter three" and yggdraChapterPrompt != "a darkened mind" and yggdraChapterPrompt != "chapter 4" and yggdraChapterPrompt != "chapter four" and yggdraChapterPrompt != "new dreams" and yggdraChapterPrompt != "":
                    yggdraChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. "
                                                "Please re-enter your search.").lower().strip()

                yggdraChapterOne, yggdraChapterTwo, yggdraChapterThree, yggdraChapterFour = "", "", "", ""
                # Yggdra Backstory Chapter 1
                if yggdraChapterPrompt == "chapter 1" or yggdraChapterPrompt == "chapter one" or yggdraChapterPrompt == "a time for firsts and lasts":
                    info_loc = []
                    for i in range(160, 179, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    yggdraChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                # Yggdra Backstory Chapter 2
                if yggdraChapterPrompt == "chapter 2" or yggdraChapterPrompt == "chapter two" or yggdraChapterPrompt == "a goodbye" or yggdraChapterOne == "next":
                    info_loc = []
                    for i in range(182, 195, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    yggdraChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                # Yggdra Backstory Chapter 3
                if yggdraChapterPrompt == "chapter 3" or yggdraChapterPrompt == "chapter three" or yggdraChapterPrompt == "a darkened mind" or yggdraChapterTwo == "next":
                    info_loc = []
                    for i in range(198, 209, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    yggdraChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                # Yggdra Backstory Chapter 4
                if yggdraChapterPrompt == "chapter 4" or yggdraChapterPrompt == "chapter four" or yggdraChapterPrompt == "new dreams" or yggdraChapterThree == "next":
                    info_loc = []
                    for i in range(212, 225, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    yggdraChapterFour = input("\nThis is the end of Yggdra's Bio. Press 'Enter' to return to chapter selection.\n").lower().strip()

                if yggdraChapterOne == "" or yggdraChapterTwo == "" or yggdraChapterThree == "" or yggdraChapterFour == "":
                    yggdraChapterPrompt = "chapters"
                if yggdraChapterOne != "chapters" and yggdraChapterOne != "" and yggdraChapterTwo != "chapters" and yggdraChapterTwo != "" and yggdraChapterThree != "chapters" and yggdraChapterThree != "" and yggdraChapterFour != "chapters" and yggdraChapterFour != "":
                    yggdraChapterOne = input("\nYou may have pressed enter on accident or misspelled your search. "
                                             "Please re-enter your search.").lower().strip()

            if yggdraChapterPrompt == "back":
                break
            if yggdraChapterPrompt != "chapters" and yggdraChapterPrompt != "back" and yggdraChapterPrompt != "":
                yggdraChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. "
                                            "Please re-enter your search.").lower().strip()

        # Cidelli Reimora Bio
        while characterBarrier == "cidelli reimora" or characterBarrier == "cid" or characterBarrier == "cidelli":
            info_loc = []
            for i in range(201, 231, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            cidChapterPrompt = input("\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n").lower().strip()
            if cidChapterPrompt == "back":
                break
            if cidChapterPrompt == "":
                cidChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if cidChapterPrompt != "continue" and cidChapterPrompt != "back":
                cidChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Mimi Seiran Bio
        while characterBarrier == "mimi seiran" or characterBarrier == "mimi":
            info_loc = []
            for i in range(235, 258, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            mimiChapterPrompt = input("\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n").lower().strip()
            if mimiChapterPrompt == "back":
                break
            if mimiChapterPrompt == "":
                mimiChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if mimiChapterPrompt != "continue" and mimiChapterPrompt != "back":
                mimiChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Kimiko Quintai Bio
        while characterBarrier == "kimiko quintai" or characterBarrier == "kimiko":
            info_loc = []
            for i in range(262, 289, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            kimikoChapterPrompt = input("\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n").lower().strip()
            if kimikoChapterPrompt == "back":
                break
            if kimikoChapterPrompt == "":
                kimikoChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if kimikoChapterPrompt != "continue" and kimikoChapterPrompt != "back":
                kimikoChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Aeiyou Drefael Bio
        while characterBarrier == "aeiyou drefael" or characterBarrier == "aeiyou":
            info_loc = []
            for i in range(293, 336, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            aeiyouChapterPrompt = input("\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n").lower().strip()
            if aeiyouChapterPrompt == "back":
                break
            if aeiyouChapterPrompt == "":
                aeiyouChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if aeiyouChapterPrompt != "continue" and aeiyouChapterPrompt != "back":
                aeiyouChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Kinto Vareli Bio
        while characterBarrier == "kinto verali" or characterBarrier == "kinto":
            info_loc = []
            for i in range(340, 382, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            kintoChapterPrompt = input("\nEnter 'Back' to return to Character Selection.\n").lower().strip()
            if kintoChapterPrompt == "back":
                break
            if kintoChapterPrompt == "":
                kintoChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if kintoChapterPrompt != "continue" and kintoChapterPrompt != "back":
                kintoChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Amiru Soaren Bio
        while characterBarrier == "amiru soaren" or characterBarrier == "amiru":
            info_loc = []
            for i in range(386, 414, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            amiruChapterPrompt = input("\nEnter 'Back' to return to Character Selection.\n").lower().strip()
            if amiruChapterPrompt == "back":
                break
            if amiruChapterPrompt == "":
                amiruChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if amiruChapterPrompt != "continue" and amiruChapterPrompt != "back":
                amiruChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Turcobé Sentai Bio
        while characterBarrier == "turcobe sentai" or characterBarrier == "turcobe" or characterBarrier == "turcobé sentai" or characterBarrier == "turcobé":
            info_loc = []
            for i in range(418, 447, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            turcobeChapterPrompt = input("\nEnter 'Back' to return to Character Selection.\n").lower().strip()
            if turcobeChapterPrompt == "back":
                break
            if turcobeChapterPrompt == "":
                turcobeChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if turcobeChapterPrompt != "continue" and turcobeChapterPrompt != "back":
                turcobeChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Yumeizu Artilux Bio
        while characterBarrier == "yumeizu artilux" or characterBarrier == "yumeizu":
            info_loc = []
            for i in range(451, 477, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            yumeizuChapterPrompt = input("\nEnter 'Back' to return to Character Selection.\n").lower().strip()
            if yumeizuChapterPrompt == "back":
                break
            if yumeizuChapterPrompt == "":
                yumeizuChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if yumeizuChapterPrompt != "continue" and yumeizuChapterPrompt != "back":
                yumeizuChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Ryner Khabunago Bio
        while characterBarrier == "ryner khabunago" or characterBarrier == "ryner":
            info_loc = []
            for i in range(481, 551, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            rynerChapterPrompt = input("\nEnter 'Chapters' to view the chapters of Ryner's Backstory. Enter 'Back' to return to Character Selection.\n").lower().strip()
            while rynerChapterPrompt == "chapters":
                rynerChapterPrompt = input("Ryner's Backstory\nPlease enter the chapter number to see a chapter ("
                                           "Chapter 1)\n\n| Chapter 1: The Point of the Quill\n| Chapter 2: Nabuga's Garden"
                                           "\n| Chapter 3: A Spirit Once Shared\n| Chapter 4: A Soul Twice Broken\n\nPress 'Enter' to return to Ryner's Biography.\n").lower().strip()

                if rynerChapterPrompt == "":
                    break
                if rynerChapterPrompt != "chapters" and rynerChapterPrompt != "chapter 1" and rynerChapterPrompt != "chapter one" and rynerChapterPrompt != "point of the quill" and rynerChapterPrompt != "the point of the quill" and rynerChapterPrompt != "chapter 2" and rynerChapterPrompt != "chapter two" and rynerChapterPrompt != "nabugas garden" and rynerChapterPrompt != "nabuga's garden" and rynerChapterPrompt != "chapter 3" and rynerChapterPrompt != "chapter three" and rynerChapterPrompt != "spirit once shared" and rynerChapterPrompt != "a spirit once shared" and rynerChapterPrompt != "chapter 4" and rynerChapterPrompt != "chapter four" and rynerChapterPrompt != "spirit twice broken" and rynerChapterPrompt != "a spirit twice broken" and rynerChapterPrompt != "":
                    rynerChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

                rynerChapterOne, rynerChapterTwo, rynerChapterThree, rynerChapterFour = "", "", "", ""
                # Ryner Backstory Chapter 1
                if rynerChapterPrompt == "chapter 1" or rynerChapterPrompt == "chapter one" or rynerChapterPrompt == "point of the quill" or rynerChapterPrompt == "the point of the quill":
                    info_loc = []
                    for i in range(230, 245, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    rynerChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                # Ryner Backstory Chapter 2
                if rynerChapterPrompt == "chapter 2" or rynerChapterPrompt == "chapter two" or rynerChapterPrompt == "nabugas garden" or rynerChapterPrompt == "nabuga's garden" or rynerChapterOne == "next":
                    info_loc = []
                    for i in range(248, 261, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    rynerChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                # Ryner Backstory Chapter 3
                if rynerChapterPrompt == "chapter 3" or rynerChapterPrompt == "chapter three" or rynerChapterPrompt == "spirit once shared" or rynerChapterPrompt == "a spirit once shared" or rynerChapterTwo == "next":
                    info_loc = []
                    for i in range(264, 285, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    rynerChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                # Ryner Backstory Chapter 4
                if rynerChapterPrompt == "chapter 4" or rynerChapterPrompt == "chapter four" or rynerChapterPrompt == "spirit twice broken" or rynerChapterPrompt == "a spirit twice broken" or rynerChapterThree == "next":
                    info_loc = []
                    for i in range(288, 295, 1): info_loc.append(i)
                    with open('Characters/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    rynerChapterFour = input("\nThis is the end of Ryner's Bio. Press 'Enter' to return to chapter selection.\n").lower().strip()

                if rynerChapterOne == "" or rynerChapterTwo == "" or rynerChapterThree == "" or rynerChapterFour == "":
                    rynerChapterPrompt = "chapters"
                if rynerChapterOne != "chapters" and rynerChapterOne != "" and rynerChapterTwo != "chapters" and rynerChapterTwo != "" and rynerChapterThree != "chapters" and rynerChapterThree != "" and rynerChapterFour != "chapters" and rynerChapterFour != "":
                    rynerChapterOne = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

            if rynerChapterPrompt == "back":
                break
            if rynerChapterPrompt != "continue" and rynerChapterPrompt != "bio" and rynerChapterPrompt != "back" and rynerChapterPrompt != "":
                rynerChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Sereina Fynae Bio
        while characterBarrier == "sereina fynae" or characterBarrier == "sereina":
            info_loc = []
            for i in range(557, 592, 1): info_loc.append(i)
            with open('Characters/Bios.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            sereinaChapterPrompt = input("\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n").lower().strip()
            if sereinaChapterPrompt == "back":
                break
            if sereinaChapterPrompt == "":
                sereinaChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()
            if sereinaChapterPrompt != "continue" and sereinaChapterPrompt != "back":
                sereinaChapterPrompt = input("\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.").lower().strip()

        # Character Input Exit Command
        if characterBarrier == "back":
            infoBarrier = "back"
            break
        if characterBarrier == "leave":
            print("Thank you for using the Phalmasia Info Database. Have a nice day.")
            quit()

    # Location Input Commands
    while infoBarrier == "locations":
        locationBarrier = input("Continents of Phalmasia:\n| Halgeis\n| Mu'karr\n| Altaria\n| Xhia\n| Nohla\n\nLeave "
                                "the database by entering 'Leave'. Go back to the home prompt by entering "
                                "'Back'.\n").lower().strip()

        while locationBarrier == "":
            locationBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while locationBarrier != "halgeis" and locationBarrier != "mu'karr" and locationBarrier != "mukarr" and locationBarrier != "altaria" and locationBarrier != "xhia" and locationBarrier != "nohla" and locationBarrier != "back" and locationBarrier != "leave":
            locationBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Halgeis Info & City Selection
        while locationBarrier == "halgeis":
            info_loc = []
            for i in range(3, 19, 1): info_loc.append(i)
            with open('Locations/Halgeis.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            halgeisLocations = input("\nLeave the database by entering 'Leave'. Go back to the continent selection by entering 'Back'.\n").lower().strip()

            while halgeisLocations == "":
                halgeisLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while halgeisLocations != "volquola" and halgeisLocations != "ashford" and halgeisLocations != "oshborne" and halgeisLocations != "cilfier" and halgeisLocations != "skykumo" and halgeisLocations != "swalubu" and halgeisLocations != "nulvali" and halgeisLocations != "starkiepe" and halgeisLocations != "grand elise" and halgeisLocations != "dreklife" and halgeisLocations != "mezolune" and halgeisLocations != "piquaron" and halgeisLocations != "elendraye" and halgeisLocations != "leave" and halgeisLocations != "back":
                halgeisLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Volquöla City
            if halgeisLocations == "volquola" or halgeisLocations == "volquöla":
                info_loc = []
                for i in range(23, 42, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Ashford City
            if halgeisLocations == "ashford":
                info_loc = []
                for i in range(46, 59, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Oshborne City
            if halgeisLocations == "oshborne":
                info_loc = []
                for i in range(63, 75, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Cilfier City
            if halgeisLocations == "cilfier":
                info_loc = []
                for i in range(79, 94, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Skykumo City
            if halgeisLocations == "skykumo":
                info_loc = []
                for i in range(98, 111, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Swalubu City
            if halgeisLocations == "swalubu":
                info_loc = []
                for i in range(115, 128, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Nulvali City
            if halgeisLocations == "nulvali":
                info_loc = []
                for i in range(132, 146, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Starkiepe City
            if halgeisLocations == "starkiepe":
                info_loc = []
                for i in range(150, 165, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Grand Elise City
            if halgeisLocations == "grand elise":
                info_loc = []
                for i in range(169, 182, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Drəklife City
            if halgeisLocations == "dreklife":
                info_loc = []
                for i in range(186, 196, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Mezolune City
            if halgeisLocations == "mezolune":
                info_loc = []
                for i in range(200, 214, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Piquaron City
            if halgeisLocations == "piquaron":
                info_loc = []
                for i in range(218, 228, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Elendraye City
            if halgeisLocations == "elendraye":
                info_loc = []
                for i in range(232, 244, 1): info_loc.append(i)
                with open('Locations/Halgeis.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                halgeisLocation = input("\nGo back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Halgeis Exit Command
            if halgeisLocations == "back":
                break
            if halgeisLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Mu'karr Info & City Selection
        while locationBarrier == "mu'karr" or locationBarrier == "mukarr":
            info_loc = []
            for i in range(3, 15, 1): info_loc.append(i)
            with open('Locations/Mu\'karr.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            mukarrLocations = input("\nLeave the database by entering 'Leave'. Go back to the continent selection by entering 'Back'.\n").lower().strip()

            while mukarrLocations == "":
                mukarrLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while mukarrLocations != "trefaeli" and mukarrLocations != "andromita" and mukarrLocations != "dragolyne" and mukarrLocations != "meteora" and mukarrLocations != "forecyor" and mukarrLocations != "dendraiye" and mukarrLocations != "petalford" and mukarrLocations != "aurora grotto" and mukarrLocations != "sundrop valley" and mukarrLocations != "leave" and mukarrLocations != "back":
                mukarrLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Trefaeli City
            if mukarrLocations == "trefaeli":
                info_loc = []
                for i in range(19, 31, 1): info_loc.append(i)
                with open('Locations/Mu\'karr.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Andromita City
            if mukarrLocations == "andromita":
                info_loc = []
                for i in range(35, 45, 1): info_loc.append(i)
                with open('Locations/Mu\'karr.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Dragolyne City
            if mukarrLocations == "dragolyne":
                info_loc = []
                for i in range(49, 61, 1): info_loc.append(i)
                with open('Locations/Mu\'karr.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Meteora City
            if mukarrLocations == "meteora":
                info_loc = []
                for i in range(65, 83, 1): info_loc.append(i)
                with open('Locations/Mu\'karr.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Forécyør City
            if mukarrLocations == "forecyor":
                info_loc = []
                for i in range(87, 100, 1): info_loc.append(i)
                with open('Locations/Mu\'karr.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Dendraiye City
            if mukarrLocations == "dendraiye":
                info_loc = []
                for i in range(104, 118, 1): info_loc.append(i)
                with open('Locations/Mu\'karr.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Petalford City
            if mukarrLocations == "petalford":
                info_loc = []
                for i in range(122, 136, 1): info_loc.append(i)
                with open('Locations/Mu\'karr.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Mu'karr: Mythic Locations
            # Aurora Grotto
            if mukarrLocations == "aurora grotto":
                info_loc = []
                for i in range(4, 18, 1): info_loc.append(i)
                with open('Locations/Mythics.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Sundrop Valley
            if mukarrLocations == "sundrop valley":
                info_loc = []
                for i in range(21, 35, 1): info_loc.append(i)
                with open('Locations/Mythics.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mukarrLocation = input("\nGo back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Mu'karr Exit Command
            if mukarrLocations == "back":
                break
            if mukarrLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Altaria Info & City Selection
        while locationBarrier == "altaria":
            info_loc = []
            for i in range(3, 13, 1): info_loc.append(i)
            with open('Locations/Altaria.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            altariaLocations = input("\nLeave the database by entering 'Leave'. Go back to the continent selection by entering 'Back'.\n").lower().strip()

            while altariaLocations == "":
                altariaLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while altariaLocations != "entrype" and altariaLocations != "soraikai" and altariaLocations != "cerulaine" and altariaLocations != "luminour" and altariaLocations != "keravine" and altariaLocations != "thornhaven" and altariaLocations != "manafield" and altariaLocations != "leave" and altariaLocations != "back":
                altariaLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Entrype City
            if altariaLocations == "entrype":
                info_loc = []
                for i in range(17, 33, 1): info_loc.append(i)
                with open('Locations/Altaria.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                altariaLocation = input("\nGo back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Soraikai City
            if altariaLocations == "soraikai":
                info_loc = []
                for i in range(37, 49, 1): info_loc.append(i)
                with open('Locations/Altaria.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                altariaLocation = input("\nGo back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Cerulaine City
            if altariaLocations == "cerulaine":
                info_loc = []
                for i in range(53, 63, 1): info_loc.append(i)
                with open('Locations/Altaria.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                altariaLocation = input("\nGo back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Luminour City
            if altariaLocations == "luminour":
                info_loc = []
                for i in range(67, 79, 1): info_loc.append(i)
                with open('Locations/Altaria.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                altariaLocation = input("\nGo back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Keravine City
            if altariaLocations == "keravine":
                info_loc = []
                for i in range(83, 95, 1): info_loc.append(i)
                with open('Locations/Altaria.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                altariaLocation = input("\nGo back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Thornhaven City
            if altariaLocations == "thornhaven":
                info_loc = []
                for i in range(99, 112, 1): info_loc.append(i)
                with open('Locations/Altaria.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                altariaLocation = input("\nGo back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Manafield City
            if altariaLocations == "manafield":
                info_loc = []
                for i in range(116, 130, 1): info_loc.append(i)
                with open('Locations/Altaria.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                altariaLocation = input("\nGo back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Altaria Exit Command
            if altariaLocations == "back":
                break
            if altariaLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Xhia Info & City Selection
        while locationBarrier == "xhia":
            info_loc = []
            for i in range(3, 11, 1): info_loc.append(i)
            with open('Locations/Xhia.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            xhiaLocations = input("\nLeave the database by entering 'Leave'. Go back to the continent selection by entering 'Back'.\n").lower().strip()

            while xhiaLocations == "":
                xhiaLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while xhiaLocations != "puls" and xhiaLocations != "glouden" and xhiaLocations != "clorohfyll" and xhiaLocations != "mengoro" and xhiaLocations != "zenorah" and xhiaLocations != "leave" and xhiaLocations != "back":
                xhiaLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Puls City
            if xhiaLocations == "puls":
                info_loc = []
                for i in range(15, 23, 1): info_loc.append(i)
                with open('Locations/Xhia.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                xhiaLocation = input("\nGo back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Glouden City
            if xhiaLocations == "glouden":
                info_loc = []
                for i in range(27, 40, 1): info_loc.append(i)
                with open('Locations/Xhia.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                xhiaLocation = input("\nGo back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Clorohfyll City
            if xhiaLocations == "clorohfyll":
                info_loc = []
                for i in range(44, 56, 1): info_loc.append(i)
                with open('Locations/Xhia.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                xhiaLocation = input("\nGo back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Mengoro City
            if xhiaLocations == "mengoro":
                info_loc = []
                for i in range(60, 70, 1): info_loc.append(i)
                with open('Locations/Xhia.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                xhiaLocation = input("\nGo back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Zenorah City
            if xhiaLocations == "zenorah":
                info_loc = []
                for i in range(74, 89, 1): info_loc.append(i)
                with open('Locations/Xhia.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                xhiaLocation = input("\nGo back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Xhia Exit Command
            if xhiaLocations == "back":
                break
            if xhiaLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Nohla Info & City Selection
        while locationBarrier == "nohla":
            info_loc = []
            for i in range(3, 13, 1): info_loc.append(i)
            with open('Locations/Nohla.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            nohlaLocations = input("\nLeave the database by entering 'Leave'. Go back to the continent selection by "
                                   "entering 'Back'.\n").lower().strip()

            while nohlaLocations == "":
                nohlaLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while nohlaLocations != "korfu" and nohlaLocations != "hartledge" and nohlaLocations != "eklyptil" and nohlaLocations != "dullus" and nohlaLocations != "cingrigh" and nohlaLocations != "talen" and nohlaLocations != "skyhaven" and nohlaLocations != "leave" and nohlaLocations != "back":
                nohlaLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Korfu Island
            if nohlaLocations == "korfu":
                info_loc = []
                for i in range(17, 29, 1): info_loc.append(i)
                with open('Locations/Nohla.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                nohlaLocation = input("\nGo back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Hartledge Island
            if nohlaLocations == "hartledge":
                info_loc = []
                for i in range(33, 46, 1): info_loc.append(i)
                with open('Locations/Nohla.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                nohlaLocation = input("\nGo back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Eklyptil Island
            if nohlaLocations == "eklyptil":
                info_loc = []
                for i in range(50, 68, 1): info_loc.append(i)
                with open('Locations/Nohla.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                nohlaLocation = input("\nGo back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Dullus Island
            if nohlaLocations == "dullus":
                info_loc = []
                for i in range(72, 82, 1): info_loc.append(i)
                with open('Locations/Nohla.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                nohlaLocation = input("\nGo back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Cingrigh Island
            if nohlaLocations == "cingrigh":
                info_loc = []
                for i in range(86, 103, 1): info_loc.append(i)
                with open('Locations/Nohla.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                nohlaLocation = input("\nGo back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Talen Island
            if nohlaLocations == "talen":
                info_loc = []
                for i in range(107, 119, 1): info_loc.append(i)
                with open('Locations/Nohla.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                nohlaLocation = input("\nGo back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Skyhaven Island
            if nohlaLocations == "skyhaven":
                info_loc = []
                for i in range(123, 131, 1): info_loc.append(i)
                with open('Locations/Nohla.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                nohlaLocation = input("\nGo back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Nohla Exit Command
            if nohlaLocations == "back":
                break
            if nohlaLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Locations Exit Command
        if locationBarrier == "back":
            infoBarrier = "back"
            break
        if locationBarrier == "leave":
            print("Thank you for using the Phalmasia Info Database. Have a nice day.")
            quit()

    # Magic Input Commands
    while infoBarrier == "magic":
        info_loc = []
        for i in range(3, 12, 1): info_loc.append(i)
        with open('Magic/Elemental.md', 'r') as file:
            # Initialize a counter
            line_number = 1

            # Read and process each line
            for line in file:
                if line_number in info_loc:
                    print(f"{line.strip()}")
                line_number += 1

        magicBarrier = input("\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n").lower().strip()

        while magicBarrier == "":
            magicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while magicBarrier != "elemental magic" and magicBarrier != "elemental" and magicBarrier != "lost magic" and magicBarrier != "lost" and magicBarrier != "sigils" and magicBarrier != "mythical elements" and magicBarrier != "mythical" and magicBarrier != "energy elevage" and magicBarrier != "elevage" and magicBarrier != "back" and magicBarrier != "leave":
            magicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Elemental Magic
        while magicBarrier == "elemental magic" or magicBarrier == "elemental":
            info_loc = []
            for i in range(16, 25, 1): info_loc.append(i)
            with open('Magic/Elemental.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            elementalBarrier = input("\nLeave the database by entering 'Leave'. Go back to magic selection prompt by entering 'Back'.\n").lower().strip()

            while elementalBarrier == "":
                elementalBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while elementalBarrier != "fire" and elementalBarrier != "water" and elementalBarrier != "lightning" and elementalBarrier != "wind" and elementalBarrier != "ice" and elementalBarrier != "earth" and elementalBarrier != "back" and elementalBarrier != "leave":
                elementalBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # Fire Magic
            if elementalBarrier == "fire":
                info_loc = []
                for i in range(29, 45, 1): info_loc.append(i)
                with open('Magic/Elemental.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                fireMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Water Magic
            if elementalBarrier == "water":
                info_loc = []
                for i in range(49, 63, 1): info_loc.append(i)
                with open('Magic/Elemental.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                waterMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Lightning Magic
            if elementalBarrier == "lightning":
                info_loc = []
                for i in range(67, 80, 1): info_loc.append(i)
                with open('Magic/Elemental.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                lightningMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Wind Magic
            if elementalBarrier == "wind":
                info_loc = []
                for i in range(84, 99, 1): info_loc.append(i)
                with open('Magic/Elemental.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                windMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Ice Magic
            if elementalBarrier == "ice":
                info_loc = []
                for i in range(103, 115, 1): info_loc.append(i)
                with open('Magic/Elemental.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                iceMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Earth Magic
            if elementalBarrier == "earth":
                info_loc = []
                for i in range(119, 134, 1): info_loc.append(i)
                with open('Magic/Elemental.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                earthMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Elemental Magic Exit Command
            if elementalBarrier == "back":
                break
            if elementalBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Lost Magic
        while magicBarrier == "lost magic" or magicBarrier == "lost":
            info_loc = []
            for i in range(3, 10, 1): info_loc.append(i)
            with open('Magic/Lost.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            lostBarrier = input("\nLeave the database by entering 'Leave'. Go back to magic selection prompt by entering 'Back'.\n").lower().strip()

            while lostBarrier == "":
                lostBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while lostBarrier != "shadow" and lostBarrier != "nature" and lostBarrier != "life" and lostBarrier != "gravity" and lostBarrier != "back" and lostBarrier != "leave":
                lostBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # Shadow Magic
            if lostBarrier == "shadow":
                info_loc = []
                for i in range(14, 28, 1): info_loc.append(i)
                with open('Magic/Lost.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                shadowMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Nature Magic
            if lostBarrier == "nature":
                info_loc = []
                for i in range(32, 44, 1): info_loc.append(i)
                with open('Magic/Lost.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                natureMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Life Magic
            if lostBarrier == "life":
                info_loc = []
                for i in range(48, 62, 1): info_loc.append(i)
                with open('Magic/Lost.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                lifeMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Gravity Magic
            if lostBarrier == "gravity":
                info_loc = []
                for i in range(66, 80, 1): info_loc.append(i)
                with open('Magic/Lost.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                gravityMagic = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Lost Magic Exit Command
            if lostBarrier == "back":
                break
            if lostBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Sigils
        while magicBarrier == "sigils":
            info_loc = []
            for i in range(3, 12, 1): info_loc.append(i)
            with open('Magic/Sigils.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            sigilBarrier = input("\nLeave the database by entering 'Leave'. Go back to magic selection prompt by entering 'Back'.\n").lower().strip()

            while sigilBarrier == "":
                sigilBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while sigilBarrier != "unity sigils" and sigilBarrier != "sectional sigils" and sigilBarrier != "unity" and sigilBarrier != "sectional" and sigilBarrier != "back" and sigilBarrier != "leave":
                sigilBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # Unity Sigil
            if sigilBarrier == "unity sigils" or sigilBarrier == "unity":
                info_loc = []
                for i in range(16, 19, 1): info_loc.append(i)
                with open('Magic/Sigils.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                unitySigil = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Sectional Sigil
            if sigilBarrier == "sectional sigils" or sigilBarrier == "sectional":
                info_loc = []
                for i in range(23, 32, 1): info_loc.append(i)
                with open('Magic/Sigils.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                sectionalSigil = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Sigil Exit Command
            if sigilBarrier == "back":
                break
            if sigilBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Mythical Elementals
        while magicBarrier == "mythical elements" or magicBarrier == "mythical element" or magicBarrier == "mythical" or magicBarrier == "mythic":
            info_loc = []
            for i in range(3, 18, 1): info_loc.append(i)
            with open('Magic/Mythical.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            mythicBarrier = input("\nLeave the database by entering 'Leave'. Go back to magic selection prompt by entering 'Back'.\n").lower().strip()

            while mythicBarrier == "":
                mythicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while mythicBarrier != "dynamic water" and mythicBarrier != "zenith earth" and mythicBarrier != "cosmic wind" and mythicBarrier != "onyx fire" and mythicBarrier != "electron lightning" and mythicBarrier != "permafrost ice" and mythicBarrier != "mythical beasts" and mythicBarrier != "rebirth" and mythicBarrier != "mythical elements" and mythicBarrier != "about mythical elements" and mythicBarrier != "about" and mythicBarrier != "back" and mythicBarrier != "leave":
                mythicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # About Mythical Elements
            if mythicBarrier == "about mythical elements" or mythicBarrier == "mythical elements" or mythicBarrier == "about":
                info_loc = []
                for i in range(22, 29, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mythicElements = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Dynamic Water
            if mythicBarrier == "dynamic water":
                info_loc = []
                for i in range(33, 44, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mythicWater = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Zenith Earth
            if mythicBarrier == "zenith earth":
                info_loc = []
                for i in range(48, 59, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                zenithEarth = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Cosmic Wind
            if mythicBarrier == "cosmic wind":
                info_loc = []
                for i in range(63, 74, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                cosmicWind = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Onyx Fire
            if mythicBarrier == "Onyx Fire" or mythicBarrier == "Onyx fire" or mythicBarrier == "onyx Fire" or mythicBarrier == "onyx fire":
                info_loc = []
                for i in range(78, 89, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                onyxFire = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Electron Lightning
            if mythicBarrier == "electron lightning":
                info_loc = []
                for i in range(93, 106, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                electronLightning = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Permafrost Ice
            if mythicBarrier == "permafrost ice":
                info_loc = []
                for i in range(110, 121, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                permafrostIce = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Mythical Beasts
            if mythicBarrier == "mythical beasts":
                info_loc = []
                for i in range(125, 134, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                mythicalBeast = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Rebirth
            if mythicBarrier == "rebirth":
                info_loc = []
                for i in range(138, 149, 1): info_loc.append(i)
                with open('Magic/Mythical.md', 'r') as file:
                    # Initialize a counter
                    line_number = 1

                    # Read and process each line
                    for line in file:
                        if line_number in info_loc:
                            print(f"{line.strip()}")
                        line_number += 1

                rebirth = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Mythical Elements Exit Command
            if mythicBarrier == "back":
                break
            if mythicBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Energy Elevage Commands
        if magicBarrier == "energy elevage" or magicBarrier == "elevage":
            info_loc = []
            for i in range(36, 41, 1): info_loc.append(i)
            with open('Magic/Sigils.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            energyElevage = input("\nPress 'Enter' to return to magic selection.\n").lower().strip()

        # Magic Exit Command
        if magicBarrier == "back":
            infoBarrier = "back"
            break
        if magicBarrier == "leave":
            print("Thank you for using the Phalmasia Info Database. Have a nice day.")
            quit()

    # Races Input Commands
    while infoBarrier == "races":
        info_loc = []
        for i in range(3, 10, 1): info_loc.append(i)
        with open('Races.md', 'r') as file:
            # Initialize a counter
            line_number = 1

            # Read and process each line
            for line in file:
                if line_number in info_loc:
                    print(f"{line.strip()}")
                line_number += 1

        raceBarrier = input("\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n").lower().strip()

        while raceBarrier == "":
            raceBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while raceBarrier != "terrians" and raceBarrier != "terrian" and raceBarrier != "argens" and raceBarrier != "argen" and raceBarrier != "avats" and raceBarrier != "avat" and raceBarrier != "majuu" and raceBarrier != "back" and raceBarrier != "leave":
            raceBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Terrian
        if raceBarrier == "terrians" or raceBarrier == "terrian":
            info_loc = []
            for i in range(14, 24, 1): info_loc.append(i)
            with open('Races.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            terrianRace = input("\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Argen
        if raceBarrier == "argens" or raceBarrier == "argen":
            info_loc = []
            for i in range(28, 38, 1): info_loc.append(i)
            with open('Races.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            argenRace = input("\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Avat
        if raceBarrier == "avats" or raceBarrier == "avat":
            info_loc = []
            for i in range(42, 50, 1): info_loc.append(i)
            with open('Races.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            avatRace = input("\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Majuu
        if raceBarrier == "majuu":
            info_loc = []
            for i in range(54, 64, 1): info_loc.append(i)
            with open('Races.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            majuuRace = input("\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Races Exit Command
        if raceBarrier == "back":
            infoBarrier = "back"
            break
        if raceBarrier == "leave":
            print("Thank you for using the Phalmasia Info Database. Have a nice day.")
            quit()

    # Chronicles Input Commands
    while infoBarrier == "chronicles":
        info_loc = []
        for i in range(3, 14, 1): info_loc.append(i)
        with open('Chronicles.md', 'r') as file:
            # Initialize a counter
            line_number = 1

            # Read and process each line
            for line in file:
                if line_number in info_loc:
                    print(f"{line.strip()}")
                line_number += 1

        chronicleBarrier = input("\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n").lower().strip()

        while chronicleBarrier == "":
            chronicleBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while chronicleBarrier != "before divine's gift" and chronicleBarrier != "bdg" and chronicleBarrier != "before divines gift" and chronicleBarrier != "post divine's gift" and chronicleBarrier != "pdg" and chronicleBarrier != "post divines gift" and chronicleBarrier != "the gifter's war" and chronicleBarrier != "the gifters war" and chronicleBarrier != "nabuga's banishment" and chronicleBarrier != "nabugas banishment" and chronicleBarrier != "the arduos war" and chronicleBarrier != "arduos war" and chronicleBarrier != "day of black sun" and chronicleBarrier != "the day of black sun" and chronicleBarrier != "establishment of st. guardias" and chronicleBarrier != "establishment of st. guardia's" and chronicleBarrier != "the establishment of st. guardia's" and chronicleBarrier != "the establishment of st. guardia's" and chronicleBarrier != "st. guardias" and chronicleBarrier != "st. guardia's" and chronicleBarrier != "battle of judgement" and chronicleBarrier != "the battle of judgement" and chronicleBarrier != "back" and chronicleBarrier != "leave":
            chronicleBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Initialization
        bdgChronicle = ""
        pdgChronicle = ""
        tgwChronicle = ""
        nbapChronicle = ""
        tawChronicle = ""
        esgChronicle = ""
        dbsChronicle = ""
        bojChronicle = ""

        # Before Divine's Gift
        if chronicleBarrier == "before divine's gift" or chronicleBarrier == "bdg" or chronicleBarrier == "before divines gift":
            info_loc = []
            for i in range(18, 28, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            bdgChronicle = input("\nPress 'Enter' to return to chronicle selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Post Divine's Gift
        if chronicleBarrier == "post divine's gift" or chronicleBarrier == "pdg" or chronicleBarrier == "post divines gift" or bdgChronicle == "next":
            info_loc = []
            for i in range(32, 44, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            pdgChronicle = input("\nPress 'Enter' to return to chronicle selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # The Gifter's War & The Establishment of the Keepers
        if chronicleBarrier == "the gifter's war" or chronicleBarrier == "the gifters war" or pdgChronicle == "next":
            info_loc = []
            for i in range(48, 72, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            tgwChronicle = input("\nPress 'Enter' to return to chronicle selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Nabuga's Banishment & The Creation of the After Palace
        if chronicleBarrier == "nabuga's banishment" or chronicleBarrier == "nabugas banishment" or tgwChronicle == "next":
            info_loc = []
            for i in range(76, 88, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            nbapChronicle = input("\nPress 'Enter' to return to chronicle selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # The Arduos War
        if chronicleBarrier == "the arduos war" or chronicleBarrier == "arduos war" or nbapChronicle == "next":
            info_loc = []
            for i in range(92, 108, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            tawChronicle = input("\nPress 'Enter' to return to chronicle selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Establishment of St. Guardia's
        if chronicleBarrier == "establishment of st. guardias" or chronicleBarrier == "establishment of st. guardia's" or chronicleBarrier == "the establishment of st. guardia's" or chronicleBarrier == "the establishment of st. guardias" or chronicleBarrier == "st. guardias" or chronicleBarrier == "st. guardia's" or tawChronicle == "next":
            info_loc = []
            for i in range(112, 124, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            esgChronicle = input("\nPress 'Enter' to return to chronicle selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # The Day of Black Sun
        if chronicleBarrier == "day of black sun" or chronicleBarrier == "the day of black sun" or esgChronicle == "next":
            info_loc = []
            for i in range(128, 146, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            dbsChronicle = input("\nPress 'Enter' to return to chronicle selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Battle of Judgement
        if chronicleBarrier == "battle of judgement" or chronicleBarrier == "the battle of judgement" or dbsChronicle == "next":
            info_loc = []
            for i in range(150, 168, 1): info_loc.append(i)
            with open('Chronicles.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            bojChronicle = input("\nPress 'Enter' to return to chronicle selection.\n").lower().strip()

        # Chronicle Exit Command
        if chronicleBarrier == "back":
            infoBarrier = "back"
            break
        if chronicleBarrier == "leave":
            print("Thank you for using the Phalmasia Info Database. Have a nice day.")
            quit()

    # Intro Exit Command
    if infoBarrier == "leave":
        print("Thank you for using the Phalmasia Info Database. Have a nice day.")
        quit()
    if infoBarrier == "back":
        infoBarrier = "return"
