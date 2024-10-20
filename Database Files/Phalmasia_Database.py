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
                        "Locations\n| Magic\n| Races\n| History\n\nLeave the database by entering 'Leave'.\n").lower().strip()

    while infoBarrier == "":
        infoBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
    while infoBarrier != "characters" and infoBarrier != "locations" and infoBarrier != "magic" and infoBarrier != "races" and infoBarrier != "history" and infoBarrier != "leave":
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
            # Xaeyz Kai Bio
            info_loc = []
            for i in range(3, 84, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
                if xaeyzChapterPrompt == "chapter 1" or xaeyzChapterPrompt == "chapter one" or xaeyzChapterPrompt == "the day of black sun" or xaeyzChapterPrompt == "day of black sun":
                    # Xaeyz Kai Backstory Chapter 1
                    info_loc = []
                    for i in range(4, 21, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    xaeyzChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                if xaeyzChapterPrompt == "chapter 2" or xaeyzChapterPrompt == "chapter two" or xaeyzChapterPrompt == "the aurora scythe" or xaeyzChapterPrompt == "aurora scythe" or xaeyzChapterOne == "next":
                    # Xaeyz Kai Backstory Chapter 2
                    info_loc = []
                    for i in range(24, 47, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    xaeyzChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                if xaeyzChapterPrompt == "chapter 3" or xaeyzChapterPrompt == "chapter three" or xaeyzChapterPrompt == "the forest's shadow" or xaeyzChapterPrompt == "the forests shadow" or xaeyzChapterPrompt == "forest's shadow" or xaeyzChapterPrompt == "forests shadow" or xaeyzChapterTwo == "next":
                    # Xaeyz Kai Backstory Chapter 3
                    info_loc = []
                    for i in range(50, 61, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    xaeyzChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                if xaeyzChapterPrompt == "chapter 4" or xaeyzChapterPrompt == "chapter four" or xaeyzChapterPrompt == "hozura the flame" or xaeyzChapterThree == "next":
                    # Xaeyz Kai Backstory Chapter 4
                    info_loc = []
                    for i in range(64, 85, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
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
            # Mirago Bio
            info_loc = []
            for i in range(88, 160, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
                if miragoChapterPrompt == "chapter 1" or miragoChapterPrompt == "chapter one" or miragoChapterPrompt == "onyx fire":
                    # Mirago Backstory Chapter 1
                    info_loc = []
                    for i in range(90, 105, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    miragoChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                if miragoChapterPrompt == "chapter 2" or miragoChapterPrompt == "chapter two" or miragoChapterPrompt == "meeting xaeyz" or miragoChapterOne == "next":
                    # Mirago Backstory Chapter 2
                    info_loc = []
                    for i in range(108, 123, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    miragoChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                if miragoChapterPrompt == "chapter 3" or miragoChapterPrompt == "chapter three" or miragoChapterPrompt == "a final stand" or miragoChapterTwo == "next":
                    # Mirago Backstory Chapter 3
                    info_loc = []
                    for i in range(126, 137, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    miragoChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                if miragoChapterPrompt == "chapter 4" or miragoChapterPrompt == "chapter four" or miragoChapterPrompt == "rebirth & the sundrop valley" or miragoChapterPrompt == "rebirth and the sundrop valley" or miragoChapterThree == "next":
                    # Mirago Backstory Chapter 4
                    info_loc = []
                    for i in range(140, 155, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
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
            # Yggdra Bio
            info_loc = []
            for i in range(164, 197, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
                if yggdraChapterPrompt == "chapter 1" or yggdraChapterPrompt == "chapter one" or yggdraChapterPrompt == "a time for firsts and lasts":
                    # Yggdra Backstory Chapter 1
                    info_loc = []
                    for i in range(160, 179, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    yggdraChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                if yggdraChapterPrompt == "chapter 2" or yggdraChapterPrompt == "chapter two" or yggdraChapterPrompt == "a goodbye" or yggdraChapterOne == "next":
                    # Yggdra Backstory Chapter 2
                    info_loc = []
                    for i in range(182, 195, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    yggdraChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                if yggdraChapterPrompt == "chapter 3" or yggdraChapterPrompt == "chapter three" or yggdraChapterPrompt == "a darkened mind" or yggdraChapterTwo == "next":
                    # Yggdra Backstory Chapter 3
                    info_loc = []
                    for i in range(198, 209, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    yggdraChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                if yggdraChapterPrompt == "chapter 4" or yggdraChapterPrompt == "chapter four" or yggdraChapterPrompt == "new dreams" or yggdraChapterThree == "next":
                    # Yggdra Backstory Chapter 4
                    info_loc = []
                    for i in range(212, 225, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
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
            # Cid Bio
            info_loc = []
            for i in range(201, 231, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Mimi Bio
            info_loc = []
            for i in range(235, 258, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Kimiko Bio
            info_loc = []
            for i in range(262, 289, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Aeiyou Bio
            info_loc = []
            for i in range(293, 336, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Kinto Bio
            info_loc = []
            for i in range(340, 382, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Amiru Bio
            info_loc = []
            for i in range(386, 414, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Turcobé Bio
            info_loc = []
            for i in range(418, 447, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Yumeizu Bio
            info_loc = []
            for i in range(451, 477, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Ryner Bio
            info_loc = []
            for i in range(481, 551, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
                if rynerChapterPrompt == "chapter 1" or rynerChapterPrompt == "chapter one" or rynerChapterPrompt == "point of the quill" or rynerChapterPrompt == "the point of the quill":
                    # Ryner Backstory Chapter 1
                    info_loc = []
                    for i in range(230, 245, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    rynerChapterOne = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n").lower().strip()
                if rynerChapterPrompt == "chapter 2" or rynerChapterPrompt == "chapter two" or rynerChapterPrompt == "nabugas garden" or rynerChapterPrompt == "nabuga's garden" or rynerChapterOne == "next":
                    # Ryner Backstory Chapter 2
                    info_loc = []
                    for i in range(248, 261, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    rynerChapterTwo = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n").lower().strip()
                if rynerChapterPrompt == "chapter 3" or rynerChapterPrompt == "chapter three" or rynerChapterPrompt == "spirit once shared" or rynerChapterPrompt == "a spirit once shared" or rynerChapterTwo == "next":
                    # Ryner Backstory Chapter 3
                    info_loc = []
                    for i in range(264, 285, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
                        line_number = 1
                        for line in file:
                            if line_number in info_loc:
                                print(f"{line.strip()}")
                            line_number += 1

                    rynerChapterThree = input("\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n").lower().strip()
                if rynerChapterPrompt == "chapter 4" or rynerChapterPrompt == "chapter four" or rynerChapterPrompt == "spirit twice broken" or rynerChapterPrompt == "a spirit twice broken" or rynerChapterThree == "next":
                    # Ryner Backstory Chapter 4
                    info_loc = []
                    for i in range(288, 295, 1): info_loc.append(i)
                    with open('Characters+Races/Backstories.md', 'r') as file:
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
            # Sereina Bio
            info_loc = []
            for i in range(557, 592, 1): info_loc.append(i)
            with open('Characters+Races/Bios.md', 'r') as file:
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
            # Halgeis Overview
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

            # Volquöla City Commands
            if halgeisLocations == "volquola" or halgeisLocations == "volquöla":
                # Volquöla Overview
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

            # Ashford City Commands
            if halgeisLocations == "ashford":
                # Ashford Overview
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

            # Oshborne City Commands
            if halgeisLocations == "oshborne":
                # Oshborne Overview
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

            # Cilfier City Commands
            if halgeisLocations == "cilfier":
                # Cilfier Overview
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

            # Skykumo City Commands
            if halgeisLocations == "skykumo":
                # Skykumo Overview
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

            # Swalubu City Commands
            if halgeisLocations == "swalubu":
                # Swalubu Overview
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

            # Nulvali City Commands
            if halgeisLocations == "nulvali":
                # Nulvali Overview
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

            # Starkiepe City Commands
            if halgeisLocations == "starkiepe":
                # Starkiepe Overview
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

            # Grand Elise City Commands
            if halgeisLocations == "grand elise":
                # Grand Elise Overview
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

            # Drəklife City Commands
            if halgeisLocations == "dreklife":
                # Drəklife Overview
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

            # Mezolune City Commands
            if halgeisLocations == "mezolune":
                # Mezolune Overview
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

            # Piquaron City Commands
            if halgeisLocations == "piquaron":
                # Piquaron Overview
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

            # Elendraye City Commands
            if halgeisLocations == "elendraye":
                # Elendraye Overview
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
            # Mu'karr Overview
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

            # Trefaeli City Commands
            if mukarrLocations == "trefaeli":
                # Trefaeli Overview
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

            # Andromita City Commands
            if mukarrLocations == "andromita":
                # Andromita Overview
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

            # Dragolyne City Commands
            if mukarrLocations == "dragolyne":
                # Dragolyne Overview
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

            # Meteora City Commands
            if mukarrLocations == "meteora":
                # Meteora Overview
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

            # Forécyør City Commands
            if mukarrLocations == "forecyor":
                # Forécyør Overview
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

            # Dendraiye City Commands
            if mukarrLocations == "dendraiye":
                # Dendraiye Overview
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

            # Petalford City Commands
            if mukarrLocations == "petalford":
                # Petalford Overview
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

            # Mu'karr: Mythic Location Commands
            # Aurora Grotto Commands
            if mukarrLocations == "aurora grotto":
                # Aurora Grotto Overview
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

            # Sundrop Valley Commands
            if mukarrLocations == "sundrop valley":
                # Sundrop Valley Overview
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
            # Altaria Overview
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

            # Entrype City Commands
            if altariaLocations == "entrype":
                # Entrype Overview
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

            # Soraikai City Commands
            if altariaLocations == "soraikai":
                # Soraikai Overview
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

            # Cerulaine City Commands
            if altariaLocations == "cerulaine":
                # Cerulaine Overview
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

            # Luminour City Commands
            if altariaLocations == "luminour":
                # Luminour Overview
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

            # Keravine City Commands
            if altariaLocations == "keravine":
                # Keravine Overview
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

            # Thornhaven City Commands
            if altariaLocations == "thornhaven":
                # Thornhaven Overview
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

            # Manafield City Commands
            if altariaLocations == "manafield":
                # Manafield Overview
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
            # Xhia Overview
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

            # Puls City Commands
            if xhiaLocations == "puls":
                # Puls Overview
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

            # Glouden City Commands
            if xhiaLocations == "glouden":
                # Glouden Overview
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

            # Clorohfyll City Commands
            if xhiaLocations == "clorohfyll":
                # Clorohfyll Overview
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

            # Mengoro City Commands
            if xhiaLocations == "mengoro":
                # Mengoro Overview
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

            # Zenorah City Commands
            if xhiaLocations == "zenorah":
                # Zenorah Overview
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
            # Nohla Overview
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

            # Korfu Island Commands
            if nohlaLocations == "korfu":
                # Korfu Overview
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

            # Hartledge Island Commands
            if nohlaLocations == "hartledge":
                # Hartledge Overview
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

            # Eklyptil Island Commands
            if nohlaLocations == "eklyptil":
                # Eklyptil Overview
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

            # Dullus Island Commands
            if nohlaLocations == "dullus":
                # Dullus Overview
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

            # Cingrigh Island Commands
            if nohlaLocations == "cingrigh":
                # Cingrigh Overview
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

            # Talen Island Commands
            if nohlaLocations == "talen":
                # Talen Overview
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

            # Skyhaven Island Commands
            if nohlaLocations == "skyhaven":
                # Nohla Overview
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
        # Magic Overview
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

        # Elemental Magic Commands
        while magicBarrier == "elemental magic" or magicBarrier == "elemental":
            # Elemental Magic Overview
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

            # Fire Magic Commands
            if elementalBarrier == "fire":
                # Fire Overview
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

            # Water Magic Commands
            if elementalBarrier == "water":
                # Water Overview
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

            # Lightning Magic Commands
            if elementalBarrier == "lightning":
                # Lightning Overview
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

            # Wind Magic Commands
            if elementalBarrier == "wind":
                # Wind Overview
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

            # Ice Magic Commands
            if elementalBarrier == "ice":
                # Ice Overview
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

            # Earth Magic Commands
            if elementalBarrier == "earth":
                # Earth Overview
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
                elementalBarrier = "back"
                break
            if elementalBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Lost Magic Commands
        while magicBarrier == "lost magic" or magicBarrier == "lost":
            # Lost Magic Overview
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

            # Shadow Magic Commands
            if lostBarrier == "shadow":
                # Shadow Overview
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

            # Nature Magic Commands
            if lostBarrier == "nature":
                # Nature Overview
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

            # Life Magic Commands
            if lostBarrier == "life":
                # Life Overview
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

            # Gravity Magic Commands
            if lostBarrier == "gravity":
                # Gravity Overview
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
                lostBarrier = "back"
                break
            if lostBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Sigils Commands
        while magicBarrier == "sigils":
            # Sigils Overview
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

            # Unity Sigil Commands
            if sigilBarrier == "unity sigils" or sigilBarrier == "unity":
                # Unity Sigils Overview
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

            # Sectional Sigil Commands
            if sigilBarrier == "sectional sigils" or sigilBarrier == "sectional":
                # Sectional Sigils Overview
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
                sigilBarrier = "back"
                break
            if sigilBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Mythical Elemental Commands
        while magicBarrier == "mythical elements" or magicBarrier == "mythical element" or magicBarrier == "mythical" or magicBarrier == "mythic":
            # Mythical Elements Overview
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
                # About Mythical Elements
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

            # Dynamic Water Commands
            if mythicBarrier == "dynamic water":
                # Dynamic Water Overview
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

            # Zenith Earth Commands
            if mythicBarrier == "zenith earth":
                # Zenith Earth Overview
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

            # Cosmic Wind Commands
            if mythicBarrier == "cosmic wind":
                # Cosmic Wind Overview
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

            # Onyx Fire Commands
            if mythicBarrier == "Onyx Fire" or mythicBarrier == "Onyx fire" or mythicBarrier == "onyx Fire" or mythicBarrier == "onyx fire":
                # Onyx Fire Overview
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

            # Electron Lightning Commands
            if mythicBarrier == "electron lightning":
                # Electron Lightning Overview
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

            # Permafrost Ice Commands
            if mythicBarrier == "permafrost ice":
                # Permafrost Ice Overview
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

            # Mythical Beasts Commands
            if mythicBarrier == "mythical beasts":
                # Mythical Beasts Overview
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

            # Rebirth Commands
            if mythicBarrier == "rebirth":
                # Rebirth Overview
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
                mythicBarrier = "back"
                break
            if mythicBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Energy Elevage Commands
        if magicBarrier == "energy elevage" or magicBarrier == "elevage":
            # Sectional Sigils Overview
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
        # Races Overview
        info_loc = []
        for i in range(3, 10, 1): info_loc.append(i)
        with open('Characters+Races/Races.md', 'r') as file:
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

        # Terrian Commands
        if raceBarrier == "terrians" or raceBarrier == "terrian":
            # Terrian Overview
            info_loc = []
            for i in range(14, 24, 1): info_loc.append(i)
            with open('Characters+Races/Races.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            terrianRace = input("\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Argen Commands
        if raceBarrier == "argens" or raceBarrier == "argen":
            # Argen Overview
            info_loc = []
            for i in range(28, 38, 1): info_loc.append(i)
            with open('Characters+Races/Races.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            argenRace = input("\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Avat Commands
        if raceBarrier == "avats" or raceBarrier == "avat":
            # Avat Overview
            info_loc = []
            for i in range(42, 50, 1): info_loc.append(i)
            with open('Characters+Races/Races.md', 'r') as file:
                # Initialize a counter
                line_number = 1

                # Read and process each line
                for line in file:
                    if line_number in info_loc:
                        print(f"{line.strip()}")
                    line_number += 1

            avatRace = input("\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Majuu Commands
        if raceBarrier == "majuu":
            # Majuu Overview
            info_loc = []
            for i in range(54, 64, 1): info_loc.append(i)
            with open('Characters+Races/Races.md', 'r') as file:
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

    # History Input Commands
    while infoBarrier == "history":
        historyBarrier = input("Historical Events of Phalmasia:\n| Before Divine's Gift (BDG)\n| Post Divine's Gift ("
                               "PDG)\n| The Gifter's War\n| Nabuga's Banishment\n| The Arduos War\n| The "
                               "Establishment of St. Guardia's\n| The Day of Black Sun\n| The Battle of "
                               "Judgement\n\nLeave the database by entering 'Leave'. Go back to the home prompt by "
                               "entering 'Back'.\n").lower().strip()

        while historyBarrier == "":
            historyBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while historyBarrier != "before divine's gift" and historyBarrier != "bdg" and historyBarrier != "before divines gift" and historyBarrier != "post divine's gift" and historyBarrier != "pdg" and historyBarrier != "post divines gift" and historyBarrier != "the gifter's war" and historyBarrier != "the gifters war" and historyBarrier != "nabuga's banishment" and historyBarrier != "nabugas banishment" and historyBarrier != "the arduos war" and historyBarrier != "arduos war" and historyBarrier != "day of black sun" and historyBarrier != "the day of black sun" and historyBarrier != "establishment of st. guardias" and historyBarrier != "establishment of st. guardia's" and historyBarrier != "the establishment of st. guardia's" and historyBarrier != "the establishment of st. guardia's" and historyBarrier != "st. guardias" and historyBarrier != "st. guardia's" and historyBarrier != "battle of judgement" and historyBarrier != "the battle of judgement" and historyBarrier != "back" and historyBarrier != "leave":
            historyBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Initialization
        bdgHistory = ""
        pdgHistory = ""
        tgwHistory = ""
        nbapHistory = ""
        tawHistory = ""
        esgHistory = ""
        dbsHistory = ""
        bojHistory = ""

        # Before Divine's Gift
        if historyBarrier == "before divine's gift" or historyBarrier == "bdg" or historyBarrier == "before divines gift":
            bdgHistory1 = "\033[1m" + "Before Divine's Gift" + "\033[0m\n| 4557 BDG - 0 BDG\n\nWhen the terrians, argens, avats, and majuu " \
                                                               "first emerged on Phalmasia over 4500 years ago, the earth was barren and tough. With no " \
                                                               "way to sculpt their terrain, the population found it difficult to survive. Shelters were " \
                                                               "constructed with much difficulty, but most could not withstand the strength of the " \
                                                               "weather. The races split themselves among the four main sections of land on the planet " \
                                                               "where they could live most comfortably.\n\n"
            bdgHistory2 = "Argens chose the natural forests and mountains of the east, naming it Mu'karr. The avats " \
                          "took the high cliffs of the island away from the mainland seeking peace and serenity. They " \
                          "called it Altaria, a powerful spirit of the sky and clouds. The majuu took the smaller " \
                          "section of the mainland towards the south with harsh and extreme climates, naming it Xhia, " \
                          "a word meaning perseverance & strength. The terrians then chose the flat plains of the " \
                          "north, naming it Halgeis, a portmanteau of the horizon.\n\n"
            bdgHistory3 = "Now in climates and locations they were more comfortable with, they began to shape their " \
                          "new homes. Avats took advantage of the cliffs and made homes out of caves on the side of " \
                          "their mountains. Majuu made their homes of volcanic rock and forged brick, " \
                          "providing insulation and cooling based on the natural weather. The terrians built large " \
                          "towns and cities, utilizing the flat land to farm the crops they could with their limited " \
                          "resources. The argens used the trees of the dense forests as their homes, giving them a " \
                          "deeper connection to the earth and protection from the outdoor weather.\n\n"
            bdgHistory4 = "Life like this continued for many centuries. However, in 78 BDG, the world began to " \
                          "change. Volcanic eruptions & avalanches nearly consumed all living space in Xhia. The land " \
                          "ran dry in Halgeis and Mu'karr, making farming near impossible and starting wildfires in " \
                          "the argenian forests. Earthquakes ran through Altaria, making quick work of any structures " \
                          "the avats had built there. By 1 BDG, they had nothing of their developments. They had " \
                          "prospered for centuries, and soon every race was back to how they were eons ago. They were " \
                          "forced to start over.\n\n"
            bdgHistory = input(
                bdgHistory1 + bdgHistory2 + bdgHistory3 + bdgHistory4 + "\nPress 'Enter' to return to history selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Post Divine's Gift
        if historyBarrier == "post divine's gift" or historyBarrier == "pdg" or historyBarrier == "post divines gift" or bdgHistory == "next":
            pdgHistory1 = "\033[1m" + "Post Divine's Gift" + "\033[0m\n| 0 BDG - Present\n\nGhurrado the All-Giver, the one who gave life and " \
                                                             "being to Phalmasia and those who inhabit it, saw this and went to his children, " \
                                                             "the other gods of the land, and asked them to lend their help to those below, " \
                                                             "for they have suffered enough and need a way to lead a permanent life. So they did, " \
                                                             "and they offered their gifts to the people of Phalmasia to assist them in building their " \
                                                             "lives once again.\n\n"
            pdgHistory2 = "Aha'jitt, the Goddess of Arts, gifted her Element of Nature so that people could tame the " \
                          "land that stood against them, and work the land into their own image. Mahar'elles, " \
                          "Goddess of Ease, gifted her Element of Flow, so that people may soften the land and allow " \
                          "the plant life to flourish. These new gifts allowed people to soften and shape the land " \
                          "easily around them, but they stood still once more, unable to break the land without " \
                          "tools.\n\n"
            pdgHistory3 = "Yumaliyu the Forgiving saw this and gifted his Element of Ambition to the world. This " \
                          "allowed them to forge weapons and tools to craft the land around them. He also gave them " \
                          "the sun to give them light. But because of the use of the Element of Ambition and the sun " \
                          "being unmoving in the sky, heat ran across the world unchecked. So Teverail of the Finest " \
                          "gifted his Element of Free Paths and cooled the land. He rotated Phalmasia around the sun, " \
                          "giving the world seasons, and gave his Element of Resistance as well in order to cool the " \
                          "land during certain times.\n\n"
            pdgHistory4 = "Then, Nabuga, their wicked mother, advised not to make it too easy for those below, " \
                          "and created storms and other powerful disasters to test the will and ambition of the " \
                          "people, as well as gifting her Element of Precision to the world. Ghurrado deemed this " \
                          "fair, for if the people wanted to call this land their own, they would need to suffer " \
                          "hardships as well as generosities. He then passed on his Element of Control and Element of " \
                          "Sacrifice, hoping to aid them in learning about the land.\n\n"
            pdgHistory5 = "Mahar'elles then gifted her Element of Harvest, so that people may have plenty of food to " \
                          "eat after their hard work. Nabuga spoke again, deeming it appropriate to give the people " \
                          "something to fear, as to test the will of their spirits. She then plagued the world with " \
                          "her Element of Reflection, forging darkness and evil into the world. When it was over, " \
                          "they admired their work, and began to watch from afar.\n\n"
            pdgHistory = input(
                pdgHistory1 + pdgHistory2 + pdgHistory3 + pdgHistory4 + pdgHistory5 + "\nPress 'Enter' to return to history selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # The Gifter's War & The Establishment of the Keepers
        if historyBarrier == "the gifter's war" or historyBarrier == "the gifters war" or pdgHistory == "next":
            tgwHistory1 = "\033[1m" + "The Gifter's War & The Establishment of the Keepers" + "\033[0m\n| 1064 PDG - 1076 PDG\n\nAs the " \
                                                                                              "people were granted the gifts of their creators, they used all of the gifts together and " \
                                                                                              "made the land beautiful. They established life in large fields, high in the mountains, " \
                                                                                              "through the trees, and much more. They crafted buildings to live in; villages, towns, " \
                                                                                              "and cities rose from the ground up.\n\n"
            tgwHistory2 = "They built shrines and temples of worship to give thanks to the Creators as well, " \
                          "often giving them offerings so that they all may be pleased with their hard work, " \
                          "and to show appreciation for all that they had done for them during their time of " \
                          "suffering. However, the people soon came to realise that others had given more thanks to " \
                          "some of the gods than others. They began to question which of their creators had done more " \
                          "work out of the others and who deserved more thanks over the others.\n\n"
            tgwHistory3 = "As the thought sat and grew in silence, the people began to argue, trying to display which " \
                          "of the Creators deserved more of the praise and which gifts had been more beneficial to " \
                          "their cause. Ghurrado stood and watched this great war. He was hurt, for they did not " \
                          "understand that they all equally contributed to bring them their new beloved world. If it " \
                          "had not been for all of this children and wife, the people would not have been able to " \
                          "craft the world in the way they wanted.\n\n"
            tgwHistory4 = "The All-Giver then decided to show the world his displeasure and would end this unneeded " \
                          "fighting, for he didn't wish to see his people fight when there was so much good left to " \
                          "be observed. So he took earth, water, fire, ice, shadow, and iron, and built The Six " \
                          "Keepers.\n\n"
            tgwHistory5 = "Of earth came Guranjo the Puppet, who tried to sway the people away from unnecessary " \
                          "fighting.\n\nFrom ice came Achina the Ice Tower, who attempted to block arrows and weapons " \
                          "from clashing with each other.\n\nFrom fire came Opherius the Scorched, who burn the land " \
                          "and keep people away from one another.\n\nFrom water came Cerrus the Lake, who created " \
                          "large rivers and bodies of water to keep the people divided from one another.\n\nFrom " \
                          "shadow came Yulektia the Graveyard, who showed the people to respect the passing of others " \
                          "and to display the evil of the war.\n\nAnd of iron came Impervious the Iron Maiden, " \
                          "who would punish the corrupted and evil.\n\n"
            tgwHistory6 = "To give them life, he granted them the Life Stone, a rune sealed with unfathomable amounts " \
                          "of Life Energy & Magic, and sent them out to the world to carry on their missions. Several " \
                          "years had passed, and The Six Keepers ended the warring of the people. They then went " \
                          "their separate ways, each of them finding their own homes and going into a deep slumber " \
                          "until they were needed again...\n\n"
            tgwHistory = input(
                tgwHistory1 + tgwHistory2 + tgwHistory3 + tgwHistory4 + tgwHistory5 + tgwHistory6 + "\nPress 'Enter' to return to history selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Nabuga's Banishment & The Creation of the After Palace
        if historyBarrier == "nabuga's banishment" or historyBarrier == "nabugas banishment" or tgwHistory == "next":
            nbapHistory1 = "\033[1m" + "Nabuga's Banishment & The Creation of the After Palace" + "\033[0m\n| 1077 - 1322 PDG\n\nAs more " \
                                                                                                  "years passed Ghurrado became pleased wth how things had changed. After seeing the errors " \
                                                                                                  "of their ways, people began to worship all creators equally, and gave them all praise in " \
                                                                                                  "respect to the elements they had been gifted with. Nabuga, however, was the only one who " \
                                                                                                  "received no recognition of any kind, and began to feel bitter.\n\n"
            nbapHistory2 = "She had helped to build the world as well. If Ghurrado and her children were being " \
                           "praised for their efforts, she believed that she should as well. Conflict was important, " \
                           "after all. Without it, how do people grow? How do they learn to adapt? As time passed, " \
                           "Nabuga's anger and jealousy grew, and out of malice, Nabuga plagued the world with a " \
                           "disease to enact on her displeasure. Ghurrado saw this, and quickly cleansed the world of " \
                           "it. Ghurrado then told her that her actions were unnecessary and cruel.\n\n"
            nbapHistory3 = "He was truly sorry that she didn't receive any of the praise she deserved, but with more " \
                           "time he promised that it would come to her. But this wasn't enough for her. Over time, " \
                           "her hatred for the people shifted to her family, and she planned to dispose of them " \
                           "directly instead. One day, Nabuga attacked her youngest son, Yumaliyu, and brought him to " \
                           "the brink of death. At the last moment, Ghurrado intervened and stopped Nabuga from " \
                           "finishing her attack.\n\n"
            nbapHistory4 = "Seeing Nabuga like this, Ghurrado became very sad. The two fought for three days and " \
                           "nights until Nabuga went into a horrible fit, attacking her husband with unrestrained " \
                           "force through her blinded rage. At this, Ghurrado had enough, and had no choice but to " \
                           "banish his wife from their home, stripping her of some of her power and placed her in the " \
                           "world's core. She then had The Six Keepers build her a home, so that she may live there " \
                           "on her own.\n\n"
            nbapHistory5 = "Then, Ghurrado had an idea. Nabuga threw this fit because she wanted praise, and so she " \
                           "would get it. He created an entire new world underneath his own, granting Nabuga the " \
                           "power to watch over it. Those who passed on were sent to this world where Nabuga was god " \
                           "and was to be worshipped. As time passed on, rumor spread in the overworld that a wicked " \
                           "queen had come to watch over the dead from that point on.\n\n"
            nbapHistory = input(
                nbapHistory1 + nbapHistory2 + nbapHistory3 + nbapHistory4 + nbapHistory5 + "\nPress 'Enter' to return to history selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # The Arduos War
        if historyBarrier == "the arduos war" or historyBarrier == "arduos war" or nbapHistory == "next":
            tawHistory1 = "\033[1m" + "The Arduos War" + "\033[0m\n| 3958 - 3961 PDG\n\nKing T'llas Arduos had been crowned as the ruler of " \
                                                         "Xhia. His family had peacefully ruled for hundreds of years up until he had been crowned. " \
                                                         "He was extremely powerful, wielding both earth and fire magics, but as a king he was " \
                                                         "tyrannical. He believed that the Majuu were the superior race due to them having the " \
                                                         "strongest magics, and the innate ability to smith powerful weapons. In 20 years, " \
                                                         "he had overtaken the entire continent, and ruled over it for another 30.\n\n"
            tawHistory2 = "Due to his extreme power, Arduos drove himself insane. Seeking more power, he wished to " \
                          "expand his land even further into the other continents. He waged war on the other " \
                          "continents and immediately sent troops to overpower them. Innocent majuu who dissented " \
                          "against the war were put into slavery by their own kind; by soldiers of Arduos who " \
                          "believed that he was right. Altaria, Mu'karr and Halgeis quickly banded the little troops " \
                          "they had together to fight back.\n\n"
            tawHistory3 = "Arduos' troops first struck over the water, hoping to stop Altarian troops from reaching " \
                          "Mu'karr. However, majuu had no experience fighting on water, and they were easily " \
                          "defeated. Once the battle hit land, though, the tides changed. The allied army stood no " \
                          "chance against the majuu; their magic and weapon mastery was too great. The allies had to " \
                          "find a way to stop the majuu from advancing towards them. They only thought of one way.\n\n"
            tawHistory4 = "Xhia, before the war, hosted forests, though nowhere near as vast as their neighbor " \
                          "Mu'karr. During the war, however, the allies send all the pyromancers they could to the " \
                          "front lines, and had them burn the forest that the majuu needed to pass through to get to " \
                          "Mu'karr. Arduos, understanding that the majuu had innate ability to withstand the flames " \
                          "and magic, ordered them to continue through the burning forest. Even with their abilities, " \
                          "the flames were too great.\n\n"
            tawHistory5 = "Arduos' general (still unknown and unnamed), refused to send more troops to their deaths " \
                          "in the wildfire. He knew that the flames were causing them to lose the war. Arduos was " \
                          "furious, and insisted that the war was for the people, therefore it was more important " \
                          "than the lives of the people. The war would bring them more land, more freedom, " \
                          "more peace! One final time, he ordered the general to send the troops through the " \
                          "flames.\n\n"
            tawHistory6 = "Throughout all of this, the general had always opposed the war. It was a burden, a strain " \
                          "on the lives of the people, and something many didn't want to be associated with. They " \
                          "thought long and hard with the general's back turned to him. He had finally had enough, " \
                          "and drew his sword, piercing it into Arduos and ending his live as well as the war. The " \
                          "general aimed to fix all of the damage the war had caused, and convinced the other " \
                          "continents to help in extinguishing the fire.\n\n"
            tawHistory7 = "After that, the majuu lost their reputation as a calm and peaceful race. The war bred " \
                          "contempt, and many still keep that hatred to this day.\n\n"
            tawHistory = input(
                tawHistory1 + tawHistory2 + tawHistory3 + tawHistory4 + tawHistory5 + tawHistory6 + tawHistory7 + "\nPress 'Enter' to return to history selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Establishment of St. Guardia's
        if historyBarrier == "establishment of st. guardias" or historyBarrier == "establishment of st. guardia's" or historyBarrier == "the establishment of st. guardia's" or historyBarrier == "the establishment of st. guardias" or historyBarrier == "st. guardias" or historyBarrier == "st. guardia's" or tawHistory == "next":
            esgHistory1 = "\033[1m" + "The Establishment of St. Guardia's Academy" + "\033[0m\n| 3961 - 3963 PDG\n\nBecause of the Arduos " \
                                                                                     "War, the world began to understand the consequences of having only one person in a " \
                                                                                     "position of power. The impromptu king of Xhia (the general who ended the war) called a " \
                                                                                     "meeting with the king of the Terrians, the High Mage of the Argens, and the Head Crow of " \
                                                                                     "the Avats to have a talk about solutions that they could work together on to fix the past " \
                                                                                     "mistakes of his race, and to ensure it doesn't happen again.\n\n"
            esgHistory2 = "Though skeptical of the request, all three leaders accepted the request and met in Xhia. " \
                          "The general apologized on behalf of his people for the trouble that they had caused and " \
                          "asked that any prejudice held against the Majuu people be targeted towards him directly " \
                          "from that point on. This earned the respect of the king of the Terrians, and soon after " \
                          "the other leaders. This meeting was the start of the idea of guardianship. Over the next " \
                          "few years, the idea of guardians became more established.\n\n"
            esgHistory3 = "Guardians started out as a militia of skilled magic users that would be directly led by " \
                          "the leaders of the continent. However, they saw this as no different than an army and " \
                          "quickly scrapped the idea. It then evolved into a group of tested individuals who proved " \
                          "themselves to be skilled enough to protect others. However, this limited the guardians to " \
                          "people who were naturally skilled, and offered no training system for them either.\n\n"
            esgHistory4 = "The idea was fleshed out over many more meetings over the course of the next three years " \
                          "until the idea of guardians matches what it does today: graduates of a continent-funded " \
                          "school that teaches accepted students magic and other basic subjects. At this point, " \
                          "the four leaders had already picked the first hundred or so guardians for each continent; " \
                          "powerful people who would be teaching classes at their continent's branch of the new " \
                          "school.\n\n"
            esgHistory5 = "From there, many graduates of the school began to make changes to what being a Guardian " \
                          "meant. A guardian could be stationed at a town for basic protection against common " \
                          "threats, or it could be a team who took on bounty missions on criminals, or even a lone " \
                          "ranger who preferred to use their abilities for espionage. Guardianship wasn't just a " \
                          "protection against the leaders having too much power anymore; it was the life-blood of " \
                          "most continent's protection force, and a dream for many young people across Phalmasia.\n\n"
            esgHistory = input(
                esgHistory1 + esgHistory2 + esgHistory3 + esgHistory4 + esgHistory5 + "\nPress 'Enter' to return to history selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # The Day of Black Sun
        if historyBarrier == "day of black sun" or historyBarrier == "the day of black sun" or esgHistory == "next":
            dbsHistory1 = "\033[1m" + "The Day of Black Sun" + "\033[0m\n| 4030 PDG\n\nThings in the world returned to somewhat normalcy " \
                                                               "after the resolution of the Arduos war, albeit some new stigmas and biases towards the " \
                                                               "populace of the majuu race. However, in 4022, those in the Mu'karr began reporting strange " \
                                                               "weather patterns. Summers were hotter than the years before, and winters colder. " \
                                                               "Thunderstorms were much more common, and blizzards brought much more snow than expected. " \
                                                               "Most strangely, the aurora borealis was in the sky nearly every week.\n\n"
            dbsHistory2 = "The argens of Mu'karr couldn't understand why the weather had changed so drastically over " \
                          "such a short time, but they assumed it would pass after a year or two. The weather wasn't " \
                          "causing any major damage or problems, so life continued on as normal. However, one day, " \
                          "a large object shifted in front of the sun, causing a makeshift solar eclipse. Confusion " \
                          "was spread all throughout Mu'karr and Halgeis (as both of them shared the same time in the " \
                          "sun). Unlike the weather anomalies, this issue was prominent.\n\n"
            dbsHistory3 = "How had something so large that it could block out the sun entirely get so close to " \
                          "Phalmasia without anyone noticing? After seeing this, it was determined that the strange " \
                          "celestial object, a large meteor made of some sort of black stone, was the cause behind " \
                          "the abnormal weather. Many people theorized that it could be the divines, angry at the " \
                          "Arduos War, and wanted to scare them for their wrongdoings. The meteor came and went after " \
                          "a few minutes, and with it went the strange weather.\n\n"
            dbsHistory4 = "People seemed to have forgotten about the meteor in everyday life for a few years. But " \
                          "they were promptly reminded of its existence when it returned. Instead of a solar eclipse " \
                          "blocking out the sun, it was not hurdling towards the ground with massive force towards a " \
                          "direct path with Meteora, a small village in Mu'karr. Many warriors were trying to do " \
                          "everything they could to stop it from reaching the surface with their magic, but it was " \
                          "ineffective.\n\n"
            dbsHistory5 = "Only a few were strong enough to make contact with the meteor while it was so far away, " \
                          "and even then the distance caused whatever spells they had to grow too weak to slow it " \
                          "down. The defenders of the village were forced to flee and evacuate everyone, " \
                          "though it was hopeless. If a meteor of that size and speed made contact, all of Phalmasia " \
                          "would likely be disrupted and even destroyed. Just then, however, a flash of light was " \
                          "seen from the village center, and a ray of black energy shot into the sky.\n\n"
            dbsHistory6 = "The ray was forceful enough to make contact with the meteor, and was even able to push " \
                          "back against it. It wasn't enough, though. It wouldn't slow down enough to matter when it " \
                          "hit the ground, and once again all hope was lost. But suddenly another flash was seen from " \
                          "the village center, this time emanating a light similar to that of the aurora in the sky. " \
                          "Shortly after, the ray became bright and colorful, growing far more forceful and large.\n\n"
            dbsHistory7 = "The meteor was effectively responding to the newfound ray, and slowing down much faster. " \
                          "It was enough to drop the meteor slowly onto the ground, saving not only the lives of the " \
                          "fleeing villagers, but of all of Phalmasia. Those who saw it quickly ran to the village " \
                          "center to thank the mysterious being who saved their lives. But they were surprised to " \
                          "meet a small boy who lived in the village at the center, covering someone else. Instead of " \
                          "thanking him as planned, the people grew fearful.\n\n"
            dbsHistory8 = "How could a young boy hold enough power to stop a force the entire defense system " \
                          "couldn't? The people stepped back, and the village defenders chased him out of the " \
                          "village. The boy brought the one he was protecting away with him, and was never seen or " \
                          "heard from again. That day went down in history as the Day of Black Sun, and the boy " \
                          "became a legend; some feared him for his power, some revered him for his actions. No one " \
                          "saw his face, so no one knew who he was, but they began to call him by his unique magic: " \
                          "The Boy of Cosmic Wind.\n\n"
            dbsHistory = input(
                dbsHistory1 + dbsHistory2 + dbsHistory3 + dbsHistory4 + dbsHistory5 + dbsHistory6 + dbsHistory7 + dbsHistory8 + "\nPress 'Enter' to return to history selection. Enter 'Next' to view the next historical event.\n").lower().strip()

        # Battle of Judgement
        if historyBarrier == "battle of judgement" or historyBarrier == "the battle of judgement" or dbsHistory == "next":
            bojHistory1 = "\033[1m" + "The Battle of Judgement" + "\033[0m\n| 4042 PDG\n\nOn the graduation day of St. Guardia's in Halgeis, " \
                                                                  "the Electron Lightning user Ryner made his first appearance. He threatened to destroy the " \
                                                                  "guardians and everything they worked for, and promised to defeat anyone that got in his " \
                                                                  "path. All the guardians, of course, rose up to stop him and told the students to evacuate. " \
                                                                  "In response, Ryner put up a ring of lightning around all of the students, trapping them " \
                                                                  "inside. Many of the students tried to break the cage, but they could barely do anything " \
                                                                  "against it.\n\n"
            bojHistory2 = "Ryner then sped towards the guardians, ready to attack when he was stopped by The Forest's " \
                          "Shadow and repelled backwards. The shadow then used this strange force to destabilize the " \
                          "cage of lightning freeing the students. It dropped his hood to reveal Xaeyz, the boy who " \
                          "had dropped out of St. Guardia's the previous year. He revealed to the world then that he " \
                          "was the Cosmic Wind user, and would do everything he could to stop this threat.\n\n"
            bojHistory3 = "He had his friends Yggdra, Mimi, Cid, Aeiyou and Kimiko help to evacuate everyone with the " \
                          "help of the guardians. Ryner, again tried to stop them, but this time Xaeyz held him back " \
                          "with his wind magic. Turning to Ryner in rage, he quickly flew up to him, dodging his " \
                          "attacks and using a powerful push spell to send Ryner flying away from the academy to a " \
                          "battlefield where civilians wouldn't be in the way. It was here that Mirago appeared and " \
                          "joined the fight to stop this great threat once and for all.\n\n"
            bojHistory4 = "This battle lasted for two days and nights, as the terrain around them became more and " \
                          "more destroyed. Ryner's shadow magic proved to be difficult to dealing with, especially " \
                          "since it could shut off magic flow, but Xaeyz could counter it with gravity, and Mirago " \
                          "could absorb his attacks with his Life magic. Their battle eventually only consisted of an " \
                          "onslaught of Mythical Elements: Onyx Fire, Cosmic Wind, and Electron Lightning attacks " \
                          "were thrown at high speeds.\n\n"
            bojHistory5 = "Eventually, Ryner got the upper hand, and hit Mirago with a blast of lightning, taking him " \
                          "down. Xaeyz tries his best to defend Mirago until he can recover himself, but he fails and " \
                          "is hit himself. It was then that Xaeyz snapped. Magic exploded from his body in a torrent " \
                          "of rage, and as a result, his Cosmic Wind merged with his phoenix form. In response, " \
                          "Ryner summoned his kaijū, and the battle began anew. But this time, Xaeyz had the " \
                          "advantage.\n\n"
            bojHistory6 = "Xaeyz barraged Ryner with attacks from the sky where his kitsune could not reach, " \
                          "damaging him. The stardust from every wing flap of the phoenix landed on Mirago, " \
                          "and helped him to recover more quickly, enough so that he could fight for one last attack. " \
                          "Xaeyz and Mirago merged their beasts to create something entirely new: a Draconic Phoenix. " \
                          "Using the same attack they had used years ago to stop the Black Sun, they blasted Ryner " \
                          "with everything they had. It worked, and Ryner fell defeated to the ground.\n\n"
            bojHistory7 = "Realizing they had won, Xaeyz and Mirago used their magic to absorb Nova, the spirit of " \
                          "Electron Lightning, from Ryner's abusive control and store it in Xaeyz's body, " \
                          "leaving Ryner without the power of his *mythical element* forever. Returning to St. " \
                          "Guardia's, Xaeyz and Mirago announced their victory. However, because of Nova's presence, " \
                          "Xaeyz couldn't wield elemental magic without taking extreme recoil and was left with only " \
                          "gravity magic.\n\n"
            bojHistory8 = "The toll of carrying two *Mythic* Spirits also put a heavy stress on his body, " \
                          "and he realized he only had about a year left to live if he continued to hold on to Nova. " \
                          "Xaeyz said goodbye to his friends at St. Guardia's one last time, and went with Mirago to " \
                          "travel the world, looking for a worthy lightning user to be the new wielder of Electron " \
                          "Lightning.\n\n"
            bojHistory = input(
                bojHistory1 + bojHistory2 + bojHistory3 + bojHistory4 + bojHistory5 + bojHistory6 + bojHistory7 + bojHistory8 + "\nPress 'Enter' to return to history selection.\n").lower().strip()

        # History Exit Command
        if historyBarrier == "back":
            infoBarrier = "back"
            break
        if historyBarrier == "leave":
            print("Thank you for using the Phalmasia Info Database. Have a nice day.")
            quit()

    # Intro Exit Command
    if infoBarrier == "leave":
        print("Thank you for using the Phalmasia Info Database. Have a nice day.")
        quit()
    if infoBarrier == "back":
        infoBarrier = "return"
