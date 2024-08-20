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
# Revamp Sigil Functionality

# Long-Term Projects
# QoL Output Clear Commands (If Possible)
# Backstories [R] for all main characters (those without tragedy, tell story of how they got magic)
# Add Side Character Option to Character Selection & Describe characters who don't get full pages
# Add Side Locations Options to Each Continent for Locations Not in Any Town
# Nabuga's Garden, Halgeis
# Home Command that Clears Output Window & Restarts Program

# Current Update Notes
# Moved Large Text Blocks into Separate Files to Read From (Code Readability)
# Added Readability Files With User-Friendly Indentation


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
            with open('Character Info/Bios', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
                    with open('Character Info/Backstories', 'r') as file:
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
            with open('Character Info/Bios', 'r') as file:
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
            halgeisLocations = input("Halgeis is the first, and currently only, continent where humans inhabit. "
                                     "Terrians are the primary inhabitants of Halgeis, and are also the ones in power "
                                     "in the continent. The humans and the terrians came together in piece relatively "
                                     "quickly, but the argens, avats and majuu weren't so trustworthy. To help along "
                                     "their relations, the terrians and humans constructed the city capital, "
                                     "Grand Elise, the peace capital of the world. With time, all of the races now "
                                     "reside in Grand Elise, and though relations are not perfect, they are still in "
                                     "place.\n\nHalgeis Cities:\n| Volquöla\n| Ashford\n| Oshborne\n| Cilfier\n| "
                                     "Skykumo\n| Swalubu\n| Nulvali\n| Starkiepe\n| Grand Elise\n| Drəklife\n| "
                                     "Mezolune\n| Piquaron\n| Elendraye\n\nLeave the database by entering 'Leave'. Go "
                                     "back to the continent selection by entering 'Back'.\n").lower().strip()

            while halgeisLocations == "":
                halgeisLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while halgeisLocations != "volquola" and halgeisLocations != "ashford" and halgeisLocations != "oshborne" and halgeisLocations != "cilfier" and halgeisLocations != "skykumo" and halgeisLocations != "swalubu" and halgeisLocations != "nulvali" and halgeisLocations != "starkiepe" and halgeisLocations != "grand elise" and halgeisLocations != "dreklife" and halgeisLocations != "mezolune" and halgeisLocations != "piquaron" and halgeisLocations != "elendraye" and halgeisLocations != "leave" and halgeisLocations != "back":
                halgeisLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Volquöla City Commands
            if halgeisLocations == "volquola" or halgeisLocations == "volquöla":
                volquolaStats = "Primary Resident Race: Majuu\nPronunciation: " \
                                "vol-KWOH-lah\nLocation: Northwestern Halgeis\nVisitor Friendly: No\nTown Trade:\n| " \
                                "Weapons\n| Armor\nSub-Locations:\n| Voltoru Canyon\n| Pyrevault Ridge\nNotable " \
                                "Residents:\n| Aeiyou Drefael\n| Kinto Verali\n\n"
                volquolaDescription = "Volquöla is a peaceful town in Northwestern Halgeis and the home to many " \
                                      "Majuu, including Aeiyou and Kinto. Volquöla is a town built on the side of " \
                                      "Pyrevault Ridge, a volcano that has been inactive for decades. Despite this, " \
                                      "it is still extremely hot there, and the average temperature is over 100 " \
                                      "degrees Fahrenheit. It has a deep cavern down the side that runs around the " \
                                      "northern and eastern side of the town facing towards Mu'karr called Voltoru " \
                                      "Cavern, which hosts a calm and steady flow of magma into the volcano's " \
                                      "chamber.\n\nMost majuu from Volquöla are light colors. It hosts many skilled " \
                                      "blacksmiths, and it is among some of the main providers of armor and weaponry " \
                                      "in Halgeis, which makes it relatively respected in the country. However, " \
                                      "most of the villagers prefer to keep to themselves and their community, " \
                                      "so the town doesn't get many visitors.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Volquöla, Halgeis\n\n" + "\033[0m" + volquolaStats + volquolaDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Ashford City Commands
            if halgeisLocations == "ashford":
                ashfordStats = "Primary Resident Race: Terrian\nPronunciation: " \
                               "ASH-ford\nLocation: Northern Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                               "Kytegrove Forest\n| Frinrir's Grave\nNotable Residents:\n| Yggdrasil Aensyll\n\n"
                ashfordDescription = "Ashford is a peaceful town on the northern side of Halgeis. The town itself is " \
                                     "larger than other common villages in Halgeis because of the regions of " \
                                     "Kytegrove Forest it covers, as well as many nearby open fields. The townspeople " \
                                     "are very close-knit and mostly all the residents knows each other, and because " \
                                     "of this the residents are very supportive and welcoming to others in the " \
                                     "community and outsiders stopping by. Those born with magical capabilities " \
                                     "venture to the open fields to spar with one another or find a peaceful, " \
                                     "open place to train in solidarity. The town doesn't have any landmarks or " \
                                     "produce any products they trade commonly, so Ashford is mostly a quiet settling " \
                                     "place for terrians to live a peaceful life with their families.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Ashford, Halgeis\n\n" + "\033[0m" + ashfordStats + ashfordDescription + "Go "
                                                                                                         "back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Oshborne City Commands
            if halgeisLocations == "oshborne":
                oshborneStats = "Primary Resident Race: Terrian\nPronunciation: " \
                                "OSH-born\nLocation: Western Halgeis\nVisitor Friendly: Yes\nNotable Residents:\n| " \
                                "Cidelli Reimora\n\n"
                oshborneDescription = "Oshborne is a small town in Western Halgeis and one of the many places in " \
                                      "Halgeis that Terrians have made their home. This is also the location of the " \
                                      "Reimora Family Bakery. It hosts a lot of open area that is used when the town " \
                                      "commonly holds fairs for various occasions like holidays, which are " \
                                      "extravagant in their own right.\n\nThe town doesn't act as a tourist " \
                                      "attraction since there aren't many things to do there, but the town will " \
                                      "openly accept any travelers who happen to be passing through.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Oshborne, Halgeis\n\n" + "\033[0m" + oshborneStats + oshborneDescription + "Go "
                                                                                                            "back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Cilfier City Commands
            if halgeisLocations == "cilfier":
                cilfierStats = "Primary Resident Race: Terrian\nPronunciation: " \
                               "SIL-fire\nLocation: Eastern Halgeis\nVisitor Friendly: Yes\nTown Trade:\n| " \
                               "Fish\nSub-Locations:\n| Sapphire Lakes\nNotable Residents: Mimi Seiran\n\n"
                cilfierDescription = "Cilfier is a city centered around the Sapphire Lakes, and is also where the " \
                                     "town name originated from. They got their name because of their deep blue water " \
                                     "that makes them look like sapphire gems. Because of these lakes, Cilfier is " \
                                     "colder than other cities most of the year, but they also provide the town with " \
                                     "seafood, as well as enabled the town to trade fish to the rest of " \
                                     "Halgeis.\n\nResidents who use water magic enjoy practicing with the water in " \
                                     "the lakes. The lakes of Cilfier draw in travellers from across Halgeis to " \
                                     "admire them. The citizens of Cilfier don't allow anyone to take water out of or " \
                                     "polluting the lakes to both respect the lakes and nature.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Cilfier, Halgeis\n\n" + "\033[0m" + cilfierStats + cilfierDescription + "Go "
                                                                                                         "back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Skykumo City Commands
            if halgeisLocations == "skykumo":
                skykumoStats = "Primary Resident Race: Avat\nPronunciation: " \
                               "SKY-coo-moh\nLocation: Northern Halgeis\nVisitor Friendly: No\nSub-Locations:\n| " \
                               "Tengou Mountain\nNotable Residents: Kimiko Quintai\n\n"
                skykumoDescription = "Skykumo is a mountainside village so high that it is near cloud height, " \
                                     "which is how the town got its name. It is on Tengou Mountain, one of the " \
                                     "tallest mountains in Halgeis. It is a village of avats, since only they can " \
                                     "breathe clearly in such thin air. Despite avat's natural acceptance of all " \
                                     "people, Skykumo is rather closed to visitors. It isn't the fact that avats do " \
                                     "not welcome visitors, it is that many visitors simply do not come to " \
                                     "Skykumo.\n\nIt is a simple town with the only attraction being its height and " \
                                     "its proximity to the clouds. Most don't come to see this, however, because the " \
                                     "thin air in Skykumo makes breathing extremely labor-intensive and is dangerous " \
                                     "to most without protective gear or wind magic.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Skykumo, Halgeis\n\n" + "\033[0m" + skykumoStats + skykumoDescription + "Go "
                                                                                                         "back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Swalubu City Commands
            if halgeisLocations == "swalubu":
                swalubuStats = "Primary Resident Race: Human\nPronunciation: " \
                               "swa-LOO-boo\nLocation: Northeastern Halgeis\nVisitor Friendly: Yes\nTown Trade:\n| " \
                               "Seafood\nSub-Locations:\n| Soshi Dojo\n| Borderline Beach\n\n"
                swalubuDescription = "Swalubu is a seaside city in Halgeis that borders Mu'karr. It hosts both a " \
                                     "beach and a large tackle shop due to its proximity to the ocean. Many fishermen " \
                                     "make their homes here due to this, though not many others live here due to its " \
                                     "summertime business. Due to the beach, the town is also a tourist spot for both " \
                                     "those that live in Halgeis and those visiting from other continents.\n\nSwalubu " \
                                     "also houses Soshi Dojo, a combat training school that specializes in honing " \
                                     "weaponry skills and fighting styles. It is extremely popular, and those without " \
                                     "magic often come here seeking mentorship if they still wish to help defend or " \
                                     "protect others (as guardians or not).\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Swalubu, Halgeis\n\n" + "\033[0m" + swalubuStats + swalubuDescription + "Go "
                                                                                                         "back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Nulvali City Commands
            if halgeisLocations == "nulvali":
                nulvaliStats = "Primary Resident Race: Terrian\nPronunciation: " \
                               "null-VAH-lee\nLocation: Northern Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                               "Nulvali Marketplace\n| Kytegrove Forest\n| Halgeian Flyers Department (HFD)\n\n"
                nulvaliDescription = "Nulvali is a large town in northern Halgeis, and is the neighbor of Ashford. " \
                                     "Nulvali is busy almost all days of they year, especially on weekends, " \
                                     "due to the Nulvali marketplace; a bustling shopping center that hosts all types " \
                                     "of stores. Many people from neighboring towns come to the market for produce " \
                                     "and other wares. \n\nIt is also the location of several departmental businesses " \
                                     "like the Halgeian Flyers Department, or HFD. They are responsible for testing " \
                                     "potential wind users for legalized flight, and give out Flyers Licenses. Though " \
                                     "there are other locations, due to Kytegrove Forest being in such a close " \
                                     "vicinity, it is the largest center in Halgeis.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Nulvali, Halgeis\n\n" + "\033[0m" + nulvaliStats + nulvaliDescription +
                    "Go back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Starkiepe City Commands
            if halgeisLocations == "starkiepe":
                starkiepeStats = "Primary Resident Race: Terrian\nPronunciation: " \
                                 "STAR-keep\nLocation: Central Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                                 "Steelpaige Mountains\n  * Briarfield Cliffs\n| Starkiepe Battle Frontier\n| Celeste " \
                                 "Mall\n\n"
                starkiepeDescription = "Starkiepe is a large city in the center of Halgeis. Starkiepe is a tourist " \
                                       "attraction for all those in Halgeis. It is one of the core cities of the " \
                                       "continent, and is filled with activities, food, and shopping centers that " \
                                       "those from all over Halgeis come to use and enjoy. Just outside of the city, " \
                                       "there is a small mountain range called Steelpaige Mountains which is also " \
                                       "accessible to climb. If you reach the top, you will arrive at Briarfield " \
                                       "Cliffs, a blooming plateau at the top of the highest mountain overlooking all " \
                                       "of Starkiepe. It is very popular to tourists due to the photogenic nature of " \
                                       "the city.\n\nOne of the highlights of the city, however, is the arena for the " \
                                       "Starkiepe Battle Frontier. This is a location where magic users from Halgeis " \
                                       "can come to compete in competitive matches and challenges. Those who want to " \
                                       "compete must pass a trial exam to portray their skill, as well as follow " \
                                       "certain guidelines to ensure the health of those competing. These matches may " \
                                       "be attempted alone, or with a team, in which case the team name and members " \
                                       "must all be registered as such. It is a great place to go to watch some " \
                                       "action.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Starkiepe, Halgeis\n\n" + "\033[0m" + starkiepeStats + starkiepeDescription +
                    "Go back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Grand Elise City Commands
            if halgeisLocations == "grand elise":
                grandEliseStats = "Primary Resident Race: Terrian\nPronunciation: Grand " \
                                  "El-LEASE\nLocation: Central Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| St. " \
                                  "Guardia's Academy\n| Enchanted Forest\n\n"
                grandEliseDescription = "Grand Elise is the capital city of Halgeis, but is one of the continent's " \
                                        "younger cities. When humans first emerged on Phalmasia hundreds of years " \
                                        "ago, they bonded strongly with the terrians in Halgeis. Their ultimate goal " \
                                        "was to unite all of the races as equals, and built the city with this in " \
                                        "mind, welcoming any race that wanted to live in Halgeis a home. Grand Elise " \
                                        "became the symbol of peace in the world, and the first official result of " \
                                        "progression towards interracial acceptance. After St. Guardia's Academy was " \
                                        "destroyed during the Arduos War, they decided to rebuild it in the center of " \
                                        "Grand Elise.\n\nThough it hosts the schooling grounds for Guardians, " \
                                        "it is still open to visitors year-round. Every year St. Guardia's sets off " \
                                        "fireworks in celebration of the day that Grand Elise had officially finished " \
                                        "construction and became open to visitors and residents. The Enchanted " \
                                        "Forest, the largest forest in Halgeis, is also present withing walking " \
                                        "distance of the city's borders and is easily accessible to residents and " \
                                        "visitors.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Grand Elise, Halgeis\n\n" + "\033[0m" + grandEliseStats + grandEliseDescription +
                    "Go back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Drəklife City Commands
            if halgeisLocations == "dreklife":
                dreklifeStats = "Primary Resident Race: Terrian\nPronunciation: " \
                                "DREEK-life\nLocation: Western Halgeis\nVisitor Friendly: No\nSub-Locations:\n| " \
                                "Enchanted Forest\n\n"
                dreklifeDescription = "Drəklife is a small village on the easternmost side of the Enchanted Forest. " \
                                      "It has a small population, but the town acts more as a family than a village; " \
                                      "everyone is close-knit, and though visitors are welcomed with open arms, " \
                                      "many are unaware of its presence and don't stop by. Because of its seclusion, " \
                                      "it is one of the few towns unprotected by a guardian post, which leaves it " \
                                      "open to the attack from wrongdoers. But because it is so secluded, they rarely " \
                                      "get attacked anyway. Drəklife harvests most of its resources from the nearby " \
                                      "Enchanted Forest, but is still respectful enough to replant any trees it cuts " \
                                      "down. Their work has done almost nothing to the health of the forest, " \
                                      "but their care has actually improved it. Those who live in Drəklife have " \
                                      "learned to care for the environment and others.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Drəklife, Halgeis\n\n" + "\033[0m" + dreklifeStats + dreklifeDescription +
                    "Go back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Mezolune City Commands
            if halgeisLocations == "mezolune":
                mezoluneStats = "Primary Resident Race: Terrian\nPronunciation: " \
                                "MEH-zo-loon\nLocation: Southeastern Halgeis\nVisitor Friendly: No\nTrade:\n| " \
                                "Produce/Crops\nNotable Residents:\n| Amiru Soaren\n\n"
                mezoluneDescription = "Mezolune is a village on the outskirts of Halgeis near the sea. The land there " \
                                      "is very rich and good for growing basic produce like potatoes, carrots, " \
                                      "and other common veggies. Though they don't have a large town, the area the " \
                                      "village takes up is one of the largest in all of Halgeis due to the farmland. " \
                                      "They distribute their crops all over Halgeis along with their neighboring " \
                                      "towns, which provide the majority of the produce supply.\n\nDespite this, " \
                                      "the town itself doesn't resemble typical farmland; it looks like a normal " \
                                      "village. Small markets are found on most days, and many people call this place " \
                                      "their home. Those who live here have a great affinity for life and plants " \
                                      "alike.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Mezolune, Halgeis\n\n" + "\033[0m" + mezoluneStats + mezoluneDescription +
                    "Go back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Piquaron City Commands
            if halgeisLocations == "piquaron":
                piquaronStats = "Primary Resident Race: Avat\nPronunciation: " \
                                "Pick-CWUAIR-ron\nLocation: Southwestern Halgeis\nVisitor Friendly: Yes\nNotable " \
                                "Residents:\n| Turcobé Sentai\n\n"
                piquaronDescription = "Piquaron is a small village in Halgeis inhabited by avats. There are few " \
                                      "avat towns that are built at ground level, and Piquaron is one of those few. " \
                                      "Piquaron is an average town that takes great pride in its village's magic " \
                                      "ability. Usually, avats are born with ice or wind magics suitable for their " \
                                      "usual home heights, but because of the low altitude, most avats here actually " \
                                      "have a greater affinity for earth magic than ice.\n\nMagic affinity is taken " \
                                      "very seriously, and all citizens here view magic as an extension of " \
                                      "themselves, giving them faster mana regeneration and larger mana reserves than " \
                                      "most. Piquaron schools teach students in a rather unconventional way; instead " \
                                      "of teaching them spells, they teach them mana control. This not only leaves " \
                                      "the students to figure out spells on their own which increases their " \
                                      "understanding of their magic, but it also teaches them to find ways to use " \
                                      "them more efficiently and in a way that is comfortable for them.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Piquaron, Halgeis\n\n" + "\033[0m" + piquaronStats + piquaronDescription +
                    "Go back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Elendraye City Commands
            if halgeisLocations == "elendraye":
                elendrayeStats = "Primary Resident Race: Terrian\nPronunciation: " \
                                 "ELL-en-dray\nLocation: Southwestern Halgeis\nVisitor Friendly: No\nNotable " \
                                 "Residents:\n| Yumeizu Artilux\n\n"
                elendrayeDescription = "Elendraye is a large town that sits in a valley in Southwestern Halgeis. " \
                                       "Though the town itself is a spectacle to see, not many visitors are welcomed " \
                                       "here. Elendraye is a closed town, and many who were born there live there for " \
                                       "their whole lives. A deep familial community is built in this town and has " \
                                       "been that way for generations. The townsfolk maintain the health of the " \
                                       "valley by using earth and water magic, as well as planting trees and flowers " \
                                       "to liven the area.\n\nDespite this, the people of elendraye are quite adapt " \
                                       "to their surroundings and know a lot about the history of Halgeis. Many of " \
                                       "them do not believe in violence, so they use their magic like argens are " \
                                       "known to: defensively. This influences the magic styles of many magic users " \
                                       "who live here. A common pastime for children is to practice their magics with " \
                                       "and against each other.\n\n"
                halgeisLocation = input(
                    "\033[1m" + "Elendraye, Halgeis\n\n" + "\033[0m" + elendrayeStats + elendrayeDescription +
                    "Go back to the other cities of Halgeis by pressing 'Enter'.\n").lower().strip()

            # Halgeis Exit Command
            if halgeisLocations == "back":
                break
            if halgeisLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Mu'karr Info & City Selection
        while locationBarrier == "mu'karr" or locationBarrier == "mukarr":
            mukarrLocations = input("Mu'karr is the continent that rests in between Xhia and Halgeis. Mostly "
                                    "consisting of forests and mountains, Mu'karr is a natural continent that "
                                    "residents strive to preserve. The main race of Mu'karr are the Argens, "
                                    "a dragon-like species. They built their cities around the forests instead of "
                                    "cutting them down, leaving most of the large cities of Mu'karr with unusual "
                                    "houses, like those in tree trunks or caves. Forécyør, the first established city "
                                    "of Mu'karr, became the center of the continent and spurred its growth. Argens "
                                    "are extremely friendly towards most outsiders and other races, so many towns in "
                                    "Mu'karr are visitor-friendly. It is also home to the high majority of "
                                    "bioluminescent plant life that Phalmasia has to offer. The result is Mu'karr "
                                    "looking like something out of a fairy tale, which helps draw in tourists looking "
                                    "to gaze in the natural beauty of the continent.\n\nMu'karr has two hidden "
                                    "locations that can only be accessed by those who know their name. Hints have "
                                    "been littered throughout the database. May the stars show you the "
                                    "way.\n\nMu'karr Cities:\n| Trefaeli\n| Andromita\n| Dragolyne\n| Meteora\n| "
                                    "Forécyør\n| Dendraiye\n| Petalford\n\nLeave the database by entering 'Leave'. Go "
                                    "back to the continent selection by entering 'Back'.\n").lower().strip()

            while mukarrLocations == "":
                mukarrLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while mukarrLocations != "trefaeli" and mukarrLocations != "andromita" and mukarrLocations != "dragolyne" and mukarrLocations != "meteora" and mukarrLocations != "forecyor" and mukarrLocations != "dendraiye" and mukarrLocations != "petalford" and mukarrLocations != "aurora grotto" and mukarrLocations != "sundrop valley" and mukarrLocations != "leave" and mukarrLocations != "back":
                mukarrLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Trefaeli City Commands
            if mukarrLocations == "trefaeli":
                trefaeliStats = "Primary Resident Race: Argen\nPronunciation: " \
                                "tree-FAIL-ee\nLocation: Southwestern Mu'karr\nVisitor Friendly: Yes\nTown Trade:\n| " \
                                "Clothing\n\n"
                trefaeliDescription = "Trefaeli is a peaceful village in Southeastern Mu'karr. Due to the hilly " \
                                      "terrain of the city, the trees aren't able to grow their roots completely " \
                                      "underground, and many burst through to the surface. This causes the trees to " \
                                      "grow strangely sideways, creating many archways of trees throughout the town. " \
                                      "This adds a natural beauty to the village.\n\nThough there isn't much to do " \
                                      "here, it is a producer of high-quality argenian clothing, though it isn't a " \
                                      "major producer. They do sell their products to all of Mu'karr, but due to the " \
                                      "size of Trefaeli, they can't afford to create high supplies.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Trefaeli, Mu'karr\n\n" + "\033[0m" + trefaeliStats + trefaeliDescription +
                    "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Andromita City Commands
            if mukarrLocations == "andromita":
                andromitaStats = "Primary Resident Race: Argen\nPronunciation: " \
                                 "an-DROM-ita\nLocation: Western Mu'karr\nVisitor Friendly: Yes\n\n"
                andromitaDescription = "Andromita is one of the few villages in Mu'karr that is in a clearing with " \
                                       "very little forestry. Though forests do surround the clearing, " \
                                       "there are minimal trees in the town itself. This leaves Andromita as one of " \
                                       "the few towns with fully constructed houses that aren't integrated into the " \
                                       "forest.\n\nArgens who live here wish to lead a quiet life; most find " \
                                       "enjoyment in small activities like gardening or collecting. Magic is rarely " \
                                       "used in this town for combat since most people agree to keep the town " \
                                       "friendly. Since the town is very small (the population is around 400 due to " \
                                       "the small size of the grove), guardians don't need to have a post in the " \
                                       "town, and it rarely ever receives any problems. It is a nice place to visit, " \
                                       "even if you are just passing through.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Andromita, Mu'karr\n\n" + "\033[0m" + andromitaStats + andromitaDescription +
                    "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Dragolyne City Commands
            if mukarrLocations == "dragolyne":
                dragolyneStats = "Primary Resident Race: Argen\nPronunciation: " \
                                 "DRA-go-line\nLocation: Eastern Mu'karr\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                                 "St. Guardia's Academy\n\n"
                dragolyneDescription = "Dragolyne is one of the largest cities in Mu'karr. It is an integration of " \
                                       "both forestry and mountainous regions of Mu'karr, so the buildings and " \
                                       "architecture throughout the town are varied depending on which region they " \
                                       "reside in, adding a unique mix of personality into the town. This makes it a " \
                                       "good place for visitors to want to come and learn about argenian " \
                                       "culture.\n\nThis town also hosts the St. Guardia's Academy of Mu'karr, " \
                                       "a sister academy of the one in Halgeis. Though they are the same academy, " \
                                       "their curriculums are tailored to argens. The school has made Dragolyne a " \
                                       "more lively place for residents, visitors, and their incoming students.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Dragolyne, Mu'karr\n\n" + "\033[0m" + dragolyneStats + dragolyneDescription +
                    "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Meteora City Commands
            if mukarrLocations == "meteora":
                meteoraStats = "Primary Resident Race: Argen\nPronunciation: " \
                               "meet-ee-OR-ah\nLocation: Southeastern Mu'karr\nVisitor Friendly: Yes\nTown Trade:\n| " \
                               "Weapons\n| Armor\nSub-Locations:\n| Black Sun Impact Site\nNotable Residents:\n| " \
                               "Xaeyz Kai\n| Mirago Fynae\n\n"
                meteoraDescription = "Meteora is a peaceful town. The community of the town is very close-knit, " \
                                     "and most all residents know each other. This is also Xaeyz and Mirago's " \
                                     "hometown. The town is also responsible for hosting the greatest smith-shop in " \
                                     "the continent, which was originally run by Xaeyz's grandfather. They are well " \
                                     "known throughout all of Mu'karr for their weaponry and armor forging.\n\nIn " \
                                     "4030, the Black Sun emerged from the sky and came crashing towards Meteora, " \
                                     "but it was stopped by Xaeyz and Mirago before it made a huge amount of damage. " \
                                     "Though the impact of the meteor was cushioned, the Black Sun still caused a " \
                                     "large crater in the middle of the town. Many people visit the crater, " \
                                     "though the public isn't aware of whether or not the Cosmic Wind User existed.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Meteora, Mu'karr\n\n" + "\033[0m" + meteoraStats + meteoraDescription +
                    "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Forécyør City Commands
            if mukarrLocations == "forecyor":
                forecyorStats = "Primary Resident Race: Argen\nPronunciation: " \
                                "FOR-eh-CYORE\nLocation: Central Mu'karr\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                                "Eden's Library\n| Dawndew Mall\n\n"
                forecyorDescription = "Forécyør is the capitol city of Mu'karr, and happens to be the largest city in " \
                                      "the continent, as well as the first city established in the continent. It is " \
                                      "in the middle of the densest part of the forests in Mu'karr. It hosts Dawndew " \
                                      "Mall, the main shopping center of the city and of Central Mu'karr. It hosts a " \
                                      "large amount of stores, as well as a shipping hub that allows for large " \
                                      "shipments of essentials like produce and intercontinental goods.\n\nThe town's " \
                                      "houses are built into the several trees in and around the town, which creates " \
                                      "a mystical setting in the town around the dirt and stone-paved paths of the " \
                                      "city. Many of the trees grow a special type of fungus that produces random " \
                                      "bioluminescent colors, lighting up the city nights. It also hosts the " \
                                      "continents central library: Eden's Library. This is built into the largest " \
                                      "tree in the city, and even continues underground. Residents of Forécyør use " \
                                      "the library on a daily basis for a multitude of reasons, and everyone does " \
                                      "what they can to preserve the natural beauty of their city.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Forécyør, Mu'karr\n\n" + "\033[0m" + forecyorStats + forecyorDescription +
                    "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Dendraiye City Commands
            if mukarrLocations == "dendraiye":
                dendraiyeStats = "Primary Resident Race: Argen\nPronunciation: " \
                                 "DEN-dray\nLocation: Northern Mu'karr\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                                 "Cryonili Mountains\nNotable Residents:\n| Sereina Fynae\n\n"
                dendraiyeDescription = "Dendraiye is a small town in Northern Mu'karr. It rests directly outside the " \
                                       "Cryonili Mountains, the mountain range that spans as a border from Halgeis " \
                                       "and Mu'karr. It hosts the safest entrance into the mountains for hikers via a " \
                                       "series of magic-made paths over the years. This attracts many " \
                                       "adventure-hungry visitors looking to climb the mountains.\n\nThe mountains " \
                                       "are very cold, and the weather is extremely volatile. Snowstorms and " \
                                       "avalanches roll down the hillside to the town very often, and guardians that " \
                                       "have ice affinities are usually stationed there to protect the towns below. " \
                                       "Sereina Fynae has made her home deep into these mountains, using the dangerous " \
                                       "terrain as a training regimen for her own magic.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Dendraiye, Mu'karr\n\n" + "\033[0m" + dendraiyeStats + dendraiyeDescription +
                    "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Petalford City Commands
            if mukarrLocations == "petalford":
                dendraiyeStats = "Primary Resident Race: Argen\nPronunciation: " \
                                 "PE-tal-ford\nLocation: Eastern Mu'karr\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                                 "Fewl Institute\nTown Trade:\n| Produce\n\n"
                dendraiyeDescription = "Petalford is a large village in Eastern Mu'karr. It is mostly open fields " \
                                       "that the residents use for gardening, primarily fruits and vegetables. While " \
                                       "some residents here are farmers, there are still plenty of others who reside " \
                                       "here as normal townsfolk with other professions. The fields that are grown " \
                                       "here are extremely efficient due to the soil that they have nurtured with " \
                                       "magic. They are able to farm very quickly in this soil, producing crops in " \
                                       "less than half the time. The argens here have also figured out how to use " \
                                       "their wind magic to yield the crops invulnerable to the seasons by keeping " \
                                       "the climate standard.\n\nThe argens here are open to visitors, as most all " \
                                       "argenian towns are, but they would rather keep to themselves. It is also one " \
                                       "of the few villages that has an extremely good magic school. Though it " \
                                       "doesn't rival the size or outreach of St. Guardia's, the training that it " \
                                       "provides is on par with the school, and many argens who don't get accepted " \
                                       "into St. Guardia's choose to apply here instead.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Petalford, Mu'karr\n\n" + "\033[0m" + dendraiyeStats + dendraiyeDescription +
                    "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Mu'karr: Mythic Location Commands
            # Aurora Grotto Commands
            if mukarrLocations == "aurora grotto":
                auroraGrottoStats = "Location: Southeastern " \
                                    "Mu'karr\nVisitor Friendly: N/A\nMythic Elemental: Aeon\nEnhanced Natural Event: " \
                                    "Aurora Borealis\n\n"
                auroraGrottoDescription = "\"It's strange, being from the stars. Everyone down here looks so odd, " \
                                          "so weak, so different. You think that after living with one of them for " \
                                          "years I would have gotten used to the sight of them. I guess I just never " \
                                          "expected to see anyone but those two here. I don't know how you got here " \
                                          "or why you know of this place, but welcome, traveller, to Aurora Grotto. " \
                                          "Don't give me a reason to make you leave.\" - Aeon, Spirit of the Cosmic " \
                                          "Wind\n\nAurora Grotto is a special location that only Xaeyz and Mirago " \
                                          "know of. This is a grotto in the vast forests of Mu'karr near the sea. It " \
                                          "is extremely serene, with waterfalls running into a lake with an island " \
                                          "that Xaeyz and Mirago seem to have built a bridge to out of a fallen " \
                                          "tree.\n\nThere are several fruit trees lining the grotto, and a cliff on " \
                                          "the edge of the grotto hosts a beautiful view of the sea. Xaeyz and Mirago " \
                                          "met each other in this grotto, and trained here nearly every day for two " \
                                          "years before Mirago passed. It is also the location of Mirago's grave, " \
                                          "which rests under the tree on the island in the lake.\n\nThe most " \
                                          "important part of the grotto is the clear skies overhead. The grotto " \
                                          "actually experiences a higher rate of natural auroras that last longer " \
                                          "than the average. This makes it the ideal location for Xaeyz to train and " \
                                          "relax due to the boost that the auroras give to his Cosmic Wind.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Mythic Location: Aurora Grotto, Mu'karr\n\n" + "\033[0m" + auroraGrottoStats +
                    auroraGrottoDescription + "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Sundrop Valley Commands
            if mukarrLocations == "sundrop valley":
                sundropValleyStats = "Location: Northwestern " \
                                     "Mu'karr\nVisitor Friendly: N/A\nMythic Elemental: Arc\nEnhanced Natural Event: " \
                                     "Solar Storm\n\n"
                sundropValleyDescription = "\"The sun is such a simple place. Just elements fusing with each other to " \
                                           "extend the system's life. It's beautiful, in a way; the ultimate " \
                                           "precipice of teamwork. But this world is different. People fight each " \
                                           "other, steal from each other, hurt each other, kill each other. But even " \
                                           "in this world of wrong, there are still shining lights. Atoms that still " \
                                           "want to work together for the betterment of the system. I don't know how " \
                                           "you know of this place's existence, but welcome nonetheless. I hope that " \
                                           "you're a good atom, or we are going to have a bit of a problem.\" - Arc, " \
                                           "Spirit of the Onyx Fire\n\nSundrop Valley is a special location that " \
                                           "Mirago alone discovered and knows of. It lies in the Cryonili Mountain " \
                                           "range in a deep valley between the mountains. In this valley, there is a " \
                                           "vast lake with an island in the center. There is also a decently large " \
                                           "field in the valley, which Mirago uses to train. When Onyx Fire revived " \
                                           "Mirago, he left Xaeyz's Grotto and went out to find a new secret place " \
                                           "where he could be alone. In his search, he found this valley.\n\nThe " \
                                           "valley is deep enough that the surrounding mountains actually provide " \
                                           "decent shelter against the outside weather, so the valley is warm and " \
                                           "naturally climate controlled. Being surrounded by mountains and " \
                                           "undiscovered by people, the terrain is completely preserved from " \
                                           "interaction and has retained its natural beauty. It is also closed off " \
                                           "from the outside world, providing a peaceful and private environment for " \
                                           "Mirago to train freely.\n\nThis valley, to Mirago's great surprise and " \
                                           "pleasure, also rests above a natural small hole in the planet's " \
                                           "atmosphere. This allows radiation from the sun to burst through in higher " \
                                           "quantities, mimicking the properties of a solar storm during times of " \
                                           "intense violence on the sun's surface. This happens to be Mirago's power " \
                                           "event, and makes his Onyx Fire stronger.\n\n"
                mukarrLocation = input(
                    "\033[1m" + "Mythic Location: Sundrop Valley, Mu'karr\n\n" + "\033[0m" + sundropValleyStats +
                    sundropValleyDescription + "Go back to the other cities of Mu'karr by pressing 'Enter'.\n").lower().strip()

            # Mu'karr Exit Command
            if mukarrLocations == "back":
                break
            if mukarrLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Altaria Info & City Selection
        while locationBarrier == "altaria":
            altariaLocations = input("Altaria is a lone island continent that is mostly mountainous terrain with lush "
                                     "cliffs and deep caves. Many of the mountains exceed cloud height, which means "
                                     "that many inhabitants of Altaria, the Avats, live very high up. As a result, "
                                     "many of them learned wind magic to assist in their breathing. Because of the "
                                     "many high peaks of the continent, the views from the cities of Altaria are "
                                     "breathtaking, which attracts many tourists. The natural terrain is mostly rocky "
                                     "and steep which makes natural trees very rare, so Avats import saplings that "
                                     "can handle their climate from Mu'karr. Because of the steep terrain, "
                                     "many villages in Mu'karr are built with different architecture that brings "
                                     "stability on vertical surfaces, like the steep mountainside. Manafield, "
                                     "the capital city of Altaria, demonstrates this architecture since it has "
                                     "buildings built up and improved over the history of the continent. This adds a "
                                     "unique aesthetic that can't be found anywhere else in the world.\n\nAltaria "
                                     "Cities:\n| Entrype\n| Soraikai\n| Cerulaine\n| Luminour\n| Keravine\n| "
                                     "Thornhaven\n| Manafield\n\nLeave the database by entering 'Leave'. Go back to "
                                     "the continent selection by entering 'Back'.\n").lower().strip()

            while altariaLocations == "":
                altariaLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while altariaLocations != "entrype" and altariaLocations != "soraikai" and altariaLocations != "cerulaine" and altariaLocations != "luminour" and altariaLocations != "keravine" and altariaLocations != "thornhaven" and altariaLocations != "manafield" and altariaLocations != "leave" and altariaLocations != "back":
                altariaLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Entrype City Commands
            if altariaLocations == "entrype":
                entrypeStats = "Primary Resident Race: Avat\nPronunciation: EN-tripe\nLocation: " \
                               "Northern Altaria\nVisitor Friendly: No\nTown Trade: Technology & " \
                               "Research\nSub-Locations:\n| Boreal Crown\n| Moonlight Pond: Yin\nTown Trade:\n| " \
                               "Mana-based Technology\n\n"
                entrypeDescription = "Entrype is the northern pole of Phalmasia, called the Boreal Crown, and the " \
                                     "northernmost town of Altaria. The Boreal Crown, being a pole of Phalmasia, " \
                                     "has a concentrated amount of natural magical energy. The Altarian guardians " \
                                     "send those at the top of their class in combat skill to guard the crown, " \
                                     "as many who desire the natural mana will try to use it for their own needs. The " \
                                     "natural mana is only allowed to be used by the researchers of Altaria to " \
                                     "enhance magical capabilities and effects.\n\nAt the center of the Boreal Crown " \
                                     "is Moonlight Pond: Yin. It is a pond shaped as the yin half of the yin-yang, " \
                                     "but the dot is an island shaped of a crescent moon. The water in this pond has " \
                                     "special properties due to it being at the center of the Boreal Crown and is " \
                                     "used in the avat's research. Though the highlight of the town is the Boreal " \
                                     "Crown, Avats do live outside the pole. Because of the icy climate and flat " \
                                     "terrain, many homes are igloos insulated with mana from the crown, and others " \
                                     "are mountain homes in the cliffs of nearby mountains. Though visitation is " \
                                     "limited due to the crown's presence, Entrype is still a beautiful village to " \
                                     "live in.\n\n"
                altariaLocation = input(
                    "\033[1m" + "Entrype, Altaria\n\n" + "\033[0m" + entrypeStats + entrypeDescription +
                    "Go back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Soraikai City Commands
            if altariaLocations == "soraikai":
                soraikaiStats = "Primary Resident Race: Avat\nPronunciation: " \
                                "soar-EYE-KYE\nLocation: Western Altaria\nVisitor Friendly: Yes\nTown Trade:\n| " \
                                "Altaria Mail Service (AMS)\n\n"
                soraikaiDescription = "Soraikai is a mountaintop village that rests just below cloud level. Most " \
                                      "every resident here has wind magic to assist in their breathing, as the height " \
                                      "of the city doesn't provide much air. Buildings are outfitted with wind " \
                                      "magic-based tech that increased air amounts in the building. The terrain of " \
                                      "the town primarily consists of a plateau where some of the town sits, " \
                                      "and the mountainside homes that are built into and onto the mountain walls " \
                                      "surrounding the plateau.\n\nThe town is high enough off of the ground that at " \
                                      "some points, it is actually difficult to see the ground below. But, " \
                                      "at the lowest sections of the town, there are places that residents or " \
                                      "visitors can observe the ground down below. People who visit must be outfitted " \
                                      "with an air tank at all times unless they are proficient wind users for their " \
                                      "own safety. Somme come to savor the view of the world from up above, " \
                                      "while others drop by for skydiving, as the height of the village makes for an " \
                                      "ideal starting point. It is also the reason that Soraikai hosts Altaria's Mail " \
                                      "Service (AMS); since mail deliverers have such a high starting point, " \
                                      "they can use wind magic to glide to other towns without using much mana to " \
                                      "gain altitude.\n\n"
                altariaLocation = input(
                    "\033[1m" + "Entrype, Altaria\n\n" + "\033[0m" + soraikaiStats + soraikaiDescription +
                    "Go back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Cerulaine City Commands
            if altariaLocations == "cerulaine":
                cerulaineStats = "Primary Resident Race: Avat\nPronunciation: " \
                                 "SER-oo-lane\nLocation: Northeastern Altaria\nVisitor Friendly: Yes\n\n"
                cerulaineDescription = "Cerulaine is the only city in Altaria that is primarily at sea level. Because " \
                                       "of this, residents share a distribution of magic affinities of wind, water, " \
                                       "and ice. This also gives the town the freedom to use architecture that is " \
                                       "more common outside of Altaria. The houses can be larger than others in " \
                                       "Altaria, and can be more flat than normal as well. This is primarily a " \
                                       "city-town though, and many of the buildings are tall for both residential and " \
                                       "business needs.\n\nBecause the height isn't so high, it has a normal amount " \
                                       "of oxygen. This makes the city more feasible and comfortable for tourists " \
                                       "since they don't need to carry around air just to walk around the town while " \
                                       "still getting a good taste of the Altarian experience. This fact makes it one " \
                                       "of the most popular tourist towns of Altaria, second only to Manafield. It is " \
                                       "also popular due to the aquatic surroundings of the city. Because it is so " \
                                       "close to the ocean, it has the ability to host water-based events and " \
                                       "activities, which also adds to the tourist attraction of the city.\n\n"
                altariaLocation = input(
                    "\033[1m" + "Cerulaine, Altaria\n\n" + "\033[0m" + cerulaineStats + cerulaineDescription +
                    "Go back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Luminour City Commands
            if altariaLocations == "luminour":
                luminourStats = "Primary Resident Race: Avat\nPronunciation: " \
                                "LOOM-in-or\nLocation: Eastern Altaria\nVisitor Friendly: Yes\nSub-Locations:\n| True" \
                                " North Pole\n\n"
                luminourDescription = "Luminour is another mountain city that is in a very special place in terms of " \
                                      "its location. Though Entrype hosts the Boreal Crown, it doesn't host the True " \
                                      "North Pole. The crowns of Phalmasia only host the magnetic poles of the " \
                                      "planet, but the True North Poles are in a separate location that is in " \
                                      "reference to the terrain. Because it is on the True North Pole, it is one of " \
                                      "the few towns in Altaria that goes through the Yin Night & Yang Day, " \
                                      "a process in which the sun appears to stay up for half the year, and sets for " \
                                      "the other half.\n\nBecause of the uniqueness of the location and the Yin & " \
                                      "Yang Day & Night cycle, many people travel to Luminour to experience the " \
                                      "strange sun patterns. This actually ended up giving the town its name; " \
                                      "Luminour. 'Lumi' is based on the word 'Luminous' which means bright while " \
                                      "'Nour' is based on 'Noir' which means black. The residents are used to the " \
                                      "months of night and months of day at a time, and have based their entire way " \
                                      "of doing things on it. Because it is so hard to tell the time simply by " \
                                      "looking at where the sun is in the sky, they have a bell tower that rings on " \
                                      "the hour. They are also a big research town since the natural light hours are " \
                                      "so constant.\n\n"
                altariaLocation = input(
                    "\033[1m" + "Luminour, Altaria\n\n" + "\033[0m" + luminourStats + luminourDescription +
                    "Go back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Keravine City Commands
            if altariaLocations == "keravine":
                keravineStats = "Primary Resident Race: Avat\nPronunciation: " \
                                "CARE-ah-veen\nLocation: Northwestern Altaria\nVisitor Friendly: " \
                                "Yes\nSub-Locations:\n| Mountain's Green\n\n"
                keravineDescription = "Keravine is a mountain city like many others. However, it is special in the " \
                                      "fact that it is surrounded by a forest named 'Mountain's Green'. Natural trees " \
                                      "are rare in Altaria, so to have a forest surrounding the city is extremely " \
                                      "rare. Of course, due to the altitude of Keravine, normal trees cannot survive, " \
                                      "so the trees that grow there are trees that can't grow anywhere outside of " \
                                      "Altaria.\n\nThe trees have much lighter and larger leaves than normal to allow " \
                                      "for increased carbon dioxide sunlight intake. They also grow vines that grow " \
                                      "beautiful flowers, making the usual stony mountain scenery very vibrant and " \
                                      "open. Some species of birds only live in these trees, whether it be because of " \
                                      "the height, the colors, or the unique sap the tree produces. All of these " \
                                      "natural elements liven up the area and make it a popular place for Avats to " \
                                      "live and for people to visit.\n\n"
                altariaLocation = input(
                    "\033[1m" + "Keravine, Altaria\n\n" + "\033[0m" + keravineStats + keravineDescription +
                    "Go back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Thornhaven City Commands
            if altariaLocations == "thornhaven":
                thornhavenStats = "Primary Resident Race: Avat\nPronunciation: " \
                                  "THORN-hay-ven\nLocation: Central Altaria\nVisitor Friendly: Yes\nTown Trade: Fresh " \
                                  "Produce\nSub-Locations:\n| Cascade Gardens\n\n"
                thornhavenDescription = "Thornhaven is a town in the center of Altaria. It is in a valley in between " \
                                        "two mountains and is one of the few towns that has flat area within its " \
                                        "borders. However, unlike other towns that use the area to build on, " \
                                        "nearly no buildings are built on the flat ground. Thornhaven uses this space " \
                                        "to grow and maintain the Cascade Gardens, a plot of land that maintains " \
                                        "different types of plant life.\n\nThough this is open to the public, " \
                                        "there are some plots that are for private use only. These are used by " \
                                        "scientists and researchers who are studying plants to gather information " \
                                        "about them that could be used for medicine or nutrition. This is one of the " \
                                        "most intuitive and progressive research gardens in all of Phalmasia, " \
                                        "as well as a beautiful location for visitors to see. The gardens also help " \
                                        "support Thornhaven by growing fruits and vegetables that the locals are able " \
                                        "to help grow and pick for themselves.\n\n"
                altariaLocation = input(
                    "\033[1m" + "Thornhaven, Altaria\n\n" + "\033[0m" + thornhavenStats + thornhavenDescription +
                    "Go back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Manafield City Commands
            if altariaLocations == "manafield":
                manafieldStats = "Primary Resident Race: Avat\nPronunciation: " \
                                 "Mah-nah-field\nLocation: Southern Altaria\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                                 "Port of New Worlds\n| St. Guardia's Academy\n| 9th Cloud\n\n"
                manafieldDescription = "Manafield is the capital city of Altaria, and is the largest city in all of " \
                                       "Altaria by a wide margin, and in the world. It spans over the entire southern " \
                                       "mountain region of Altaria, and covers over 20 mountain bases. At the " \
                                       "southernmost point of Altaria, a port was built to interact with the mainland " \
                                       "of Phalmasia more easily, and was called the Port of New Worlds. Most of " \
                                       "Altaria's international imports and exports come through this port and are " \
                                       "then distributed to other cities in the continent.\n\nIt also has the largest " \
                                       "mall in Phalmasia called the 9th Cloud. It has many different activities and " \
                                       "shops that the citizens of Manafield commonly use. Finally, being the capital " \
                                       "of Altaria, it holds the Altarian branch of St. Guardia's Academy. The " \
                                       "academy is on the west side of the city and isn't surrounded by other " \
                                       "buildings. This is because the school needs a training ground for the " \
                                       "students to practice on. This is also a unique branch as it is the only one " \
                                       "built on a mountainside. Because of the large size of Manafield, the amount " \
                                       "of land that Altaria's St. Guardia's has is far greater than those of the " \
                                       "other branches.\n\n"
                altariaLocation = input(
                    "\033[1m" + "Manafield, Altaria\n\n" + "\033[0m" + manafieldStats + manafieldDescription +
                    "Go back to the other cities of Altaria by pressing 'Enter'.\n").lower().strip()

            # Altaria Exit Command
            if altariaLocations == "back":
                break
            if altariaLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Xhia Info & City Selection
        while locationBarrier == "xhia":
            xhiaLocations = input("Xhia is the smallest of the four continents, hosting a dry, barren terrain. The "
                                  "grass and trees of the forests that once covered the northern part of Xhia are now "
                                  "gone due to the Arduos War, leaving half of the continent in a dry grass, "
                                  "treeless wasteland. Though, despite all this, the southern half of Xhia retained "
                                  "its natural beauty. Mu'karr is known for its fast forests, but Xhia was known for "
                                  "its plethora of flora species, and in southern Xhia, these plants still grow and "
                                  "are cared for. The main residents of the continent, the Majuu, are a serene and "
                                  "peaceful race, caring for nature and protecting it as best they can. The capital "
                                  "of Xhia, Clorohfyll, is in the burned northern section, making it void of all of "
                                  "its pre-war beauty. However, despite the newfound lack of flora, the city itself "
                                  "is still a beautiful place to live.\n\nXhia Cities:\n| Puls\n| Glouden\n| "
                                  "Clorohfyll\n| Mengoro\n| Zenorah\n\nLeave the database by entering 'Leave'. Go "
                                  "back to the continent selection by entering 'Back'.\n").lower().strip()

            while xhiaLocations == "":
                xhiaLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while xhiaLocations != "puls" and xhiaLocations != "glouden" and xhiaLocations != "clorohfyll" and xhiaLocations != "mengoro" and xhiaLocations != "zenorah" and xhiaLocations != "leave" and xhiaLocations != "back":
                xhiaLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Puls City Commands
            if xhiaLocations == "puls":
                pulsStats = "Primary Resident Race: Majuu\nPronunciation: PULSE\nLocation: Northeastern " \
                            "Xhia\nVisitor Friendly: No\n\n"
                pulsDescription = "Puls is a town in the burned section of Xhia. It doesn't have many residents. " \
                                  "Because of the poor soil quality, plant life isn't that big of a factor in the " \
                                  "town, besides a few trees that help add color. The town has been trying to replace " \
                                  "the soil in their town to start replanting the flora that once covered their town. " \
                                  "Before the Arduos War, this town used to be home to a magic school. But after " \
                                  "seeing what the war did to both their reputation and the rest of the world, " \
                                  "they decided to close the school and have the students learn magic from " \
                                  "experimentation on their own. While they do not forbid the use of magic throughout " \
                                  "the town, it doesn't have a school for teaching magic any longer. Residents are " \
                                  "expected to either figure it out for themselves, or have their parents teach " \
                                  "them.\n\n"
                xhiaLocation = input("\033[1m" + "Puls, Xhia\n\n" + "\033[0m" + pulsStats + pulsDescription +
                                     "Go back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Glouden City Commands
            if xhiaLocations == "glouden":
                gloudenStats = "Primary Resident Race: Majuu\nPronunciation: GLOW-den\nLocation: " \
                               "Southern Xhia\nVisitor Friendly: Yes\nSub-Locations:\n| Luminous Vineyard\n| True " \
                               "South Pole\n\n"
                gloudenDescription = "Glouden is in Southern Xhia, so it wasn't affected by the great fire, " \
                                     "and because of this, the plants that are natural to the Xhia region are still " \
                                     "able to grow there. The central-southern region of Xhia is particularly dark " \
                                     "and cold as a result of being at the bottom of the southern-most continent in " \
                                     "Phalmasia. However, this special climate allows for unique types of plants to " \
                                     "grow, particularly bulbroot vines, a type of vine that grows glowing pods and " \
                                     "flowers. This rare type of bioluminescence covers the trees and rocky terrain " \
                                     "of the village, and makes the town and surrounding flora much more welcoming " \
                                     "and serene.\n\nThere is a small forest behind the town covered in bulbroot, " \
                                     "which the townspeople call the Luminous Vineyard. The True South Pole of " \
                                     "Phalmasia is located in the Luminous Vineyard, and the residents of Glouden " \
                                     "have placed a marker in the ground where it lies. This is one of the few towns " \
                                     "that welcome visitors from outside of Xhia, feeling as though this beauty " \
                                     "shouldn't be restricted to the eyes of only the Majuu, though some still avoid " \
                                     "the region altogether because of stigmas.\n\n"
                xhiaLocation = input("\033[1m" + "Glouden, Xhia\n\n" + "\033[0m" + gloudenStats + gloudenDescription +
                                     "Go back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Clorohfyll City Commands
            if xhiaLocations == "clorohfyll":
                clorohfyllStats = "Primary Resident Race: Majuu\nPronunciation: " \
                                  "CLO-ruh-fill\nLocation: Northern Xhia\nVisitor Friendly: Yes\nSub-Locations:\n| " \
                                  "St. Guardia's Academy\n\n"
                clorohfyllDescription = "Clorohfyll is the capital of Xhia. Being in the northern half of the " \
                                        "continent, it's been torched by the embers of the war, draining the city of " \
                                        "region exclusive flora, and of much of the natural beauty it once had. " \
                                        "Though it bears a mark of embers, its residents haven't lost their spark of " \
                                        "hope and friendliness. They still openly welcome non-majuu visitors, " \
                                        "and are trying to restore the forest and lush plant life surrounding their " \
                                        "city. They have rebuilt over half the city after the fire, which leads to a " \
                                        "contrast between ancient architecture and the new, modern-age designs. This " \
                                        "makes it a popular place to learn about architecture and construction in " \
                                        "Xhia, as well as across Phalmasia.\n\nClorohfyll got its name from the " \
                                        "several different species of flora it had throughout the city, but after the " \
                                        "great fire, it has since lost its significance. Clorohfyll is also one of " \
                                        "the only places in Xhia where combat can still be instructed. They have a " \
                                        "St. Guardia's Academy of their own, where many Majuu apply to every year, " \
                                        "hoping to get in. Because of the fact that it is one of the only schools in " \
                                        "the region that can teach combat, many more students apply every year, " \
                                        "resulting in the highest application rates of any St. Guardia's Academy, " \
                                        "and a far lower acceptance rate. However, this also leads to high dropout " \
                                        "rates, since many of those applying don't intend to become guardians and " \
                                        "simply want magic or combat training.\n\n"
                xhiaLocation = input(
                    "\033[1m" + "Clorohfyll, Xhia\n\n" + "\033[0m" + clorohfyllStats + clorohfyllDescription +
                    "Go back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Mengoro City Commands
            if xhiaLocations == "mengoro":
                mengoroStats = "Primary Resident Race: Majuu\nPronunciation: men-GO-row\nLocation: " \
                               "Western Xhia\nVisitor Friendly: No\nSub-Locations:\n| Echo's Chasm\n\n"
                mengoroDescription = "Mengoro is a small village on the western outskirts of Xhia. It was one of the " \
                                     "southernmost cities to be affected by the fire, but thanks to the fast-acting " \
                                     "earth magic users, the town and its surroundings were saved. The result was a " \
                                     "chasm that arched across the northern and western borders which became known as " \
                                     "Echo's Chasm. Many residents in this village are guardians or retired " \
                                     "guardians, which is why there were enough proficient earth magic users to stop " \
                                     "the flame's progression. However, because of the high volume of guardians, " \
                                     "many don't wish to travel to Mengoro, so it remains somewhat isolated. Majuu " \
                                     "from across the region have given it the name 'Guardian's Cove' due to the " \
                                     "Echo's Chasm, which separates the guardians in the town from the other towns in " \
                                     "Xhia.\n\n"
                xhiaLocation = input("\033[1m" + "Mengoro, Xhia\n\n" + "\033[0m" + mengoroStats + mengoroDescription +
                                     "Go back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Zenorah City Commands
            if xhiaLocations == "zenorah":
                zenorahStats = "Primary Resident Race: Majuu\nPronunciation: zen-OH-rah\nLocation: " \
                               "Southeastern Xhia\nVisitor Friendly: No\nSub-Locations:\n| Austreal Crown\n| " \
                               "Moonlight Pond: Yang\nTown Trade:\n| Weaponry\n\n"
                zenorahDescription = "Zenorah is a village on the southeastern coast of Xhia. The core of the city is " \
                                     "the Austreal Crown, where a large amount of natural magical energy is " \
                                     "concentrated. The majuu harness the immense source of energy in the crown to " \
                                     "create extremely powerful weapons which they provide to the other continents. " \
                                     "Many from outside Xhia did not want the Majuu to have complete autonomy around " \
                                     "the Austreal Crown because of bias and fear that they might use these weapons " \
                                     "to start another war, but it was decided to have the majuu watch over the crown " \
                                     "by the leaders of the continents. This shows trust to the majuu by giving them " \
                                     "space to continue their lives, as well as leaves them in charge of managing " \
                                     "magic flow in the crown.\n\nAt the center of the Austreal Crown, much like the " \
                                     "Boreal Crown in Entrype, is Moonlight Pond: Yang. This pond, unlike the yin " \
                                     "half in Altaria, bears a dot that resembles a flaring sun. The pond water has " \
                                     "been imbued with the excess amount of natural energy and has healing properties " \
                                     "that the Majuu use. It cannot be used outside of Zenorah, however; if the water " \
                                     "is to leave the village, it would lose its energy concentration and return to " \
                                     "being normal water.\n\n"
                xhiaLocation = input("\033[1m" + "Zenorah, Xhia\n\n" + "\033[0m" + zenorahStats + zenorahDescription +
                                     "Go back to the other cities of Xhia by pressing 'Enter'.\n").lower().strip()

            # Xhia Exit Command
            if xhiaLocations == "back":
                break
            if xhiaLocations == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Nohla Info & City Selection
        while locationBarrier == "nohla":
            nohlaLocations = input("Nohla is unique compared to other continents, because it is composed of large "
                                   "islands, each of which are home to all of the five races of the world. Because of the "
                                   "diversity of the continent, there isn't a official leader over everything, as residents "
                                   "think that would put one race above the other, something they strive to avoid. "
                                   "Because the people here are so kind and welcoming to everyone, it makes it a great "
                                   "place for people to visit and live in. Surrounded by ocean in all directions, Nohla "
                                   "is Phalmasia's largest seafood and ocean product exporters. Many original residents "
                                   "here usually originate from other continents and immigrate here.\n\nNohla Islands:\n|"
                                   " Korfu\n| Hartledge\n| Eklyptil\n| Dullus\n| Cingrigh\n| Talen\n| Skyhaven"
                                   "\n\nLeave the database by entering 'Leave'. Go back to the continent selection by "
                                   "entering 'Back'.\n").lower().strip()

            while nohlaLocations == "":
                nohlaLocations = input("Please Re-enter your database restriction.\n").lower().strip()
            while nohlaLocations != "korfu" and nohlaLocations != "hartledge" and nohlaLocations != "eklyptil" and nohlaLocations != "dullus" and nohlaLocations != "cingrigh" and nohlaLocations != "talen" and nohlaLocations != "skyhaven" and nohlaLocations != "leave" and nohlaLocations != "back":
                nohlaLocations = input("Please Re-enter your database restriction.\n").lower().strip()

            # Korfu Island Commands
            if nohlaLocations == "korfu":
                korfuStats = "Primary Resident Race: Terrian\nPronunciation: CORE-foo\nLocation: Western " \
                             "Nohla\nVisitor Friendly: Yes\nSub-Locations:\n| Tropics Grove\n\n"
                korfuDescription = "Korfu is a short island on the western side of Nohla that lies close to sea level. " \
                                   "This means that it is naturally surrounded by beaches, and has a very tropical climate. " \
                                   "The seawater is also very clear near the shores, and many resorts line the beaches " \
                                   "as travel locations to tourists and visiting people. Because of the summer-like " \
                                   "climate and resorts, Korfu has become one of the most popular islands people visit " \
                                   "when coming to Nohla.\n\nKorfu also houses Tropics Grove, a tropical valley that has " \
                                   "several pine trees and bushes growing different tropical fruit, like pyreapples and " \
                                   "cocomelons. Tropics Grove is open to the public on weekends, and a farmer's market " \
                                   "is opened every Saturday. Tropics Grove also allows Korfu to export large amounts of " \
                                   "fruit to the other islands of the continent, which gives it a steady source of income." \
                                   "Korfu is big on protecting its environment, so the island takes many steps to prevent " \
                                   "it's deterioration.\n\n"
                nohlaLocation = input("\033[1m" + "Korfu, Nohla\n\n" + "\033[0m" + korfuStats + korfuDescription +
                                      "Go back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Hartledge Island Commands
            if nohlaLocations == "hartledge":
                hartledgeStats = "Primary Resident Race: Argen\nPronunciation: HEART-ledge\nLocation: " \
                                 "Northern Nohla\nVisitor Friendly: No\nSub-Locations:\n| Hornscale Caves\n| Whispering Forest\n\n"
                hartledgeDescription = "Hartledge is an island covered in trees similar to Mu'karr, which is why its population " \
                                       "mainly consists of argens. Most of these argens, however, are archaeologists and " \
                                       "proficient scholars in history and magic. This is because Hartledge hosts the Hornscale" \
                                       "Caves, one of the oldest recorded cave systems in Phalmasia. Not much is known about " \
                                       "the caves, however the walls give off a strange magical signature that is difficult " \
                                       "to notice, but seems to have been there since its inception thousands of years ago. " \
                                       "The caves go deep into the heart of the islands, and the researchers believe that " \
                                       "discovering the secrets of the caves may lead to a deeper understanding of magic as " \
                                       "a whole.\n\nDue to the caves being actively under research, the island isn't open " \
                                       "for visitation. However, the Whispering Forest can be seen from other nearby islands " \
                                       "of Nohla, as their pink leaves and silver trunks are very vibrant. The island is high " \
                                       "enough that there is a breeze constantly flowing throughout the forest, and the trunks " \
                                       "of these hardened sakura trees whistle in the wind, which is why the forest has been " \
                                       "dubbed the 'Whispering Forest'.\n\n"
                nohlaLocation = input(
                    "\033[1m" + "Hartledge, Nohla\n\n" + "\033[0m" + hartledgeStats + hartledgeDescription +
                    "Go back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Eklyptil Island Commands
            if nohlaLocations == "eklyptil":
                eklyptilStats = "Primary Resident Race: None (Balanced)\nPronunciation: eh-KLIP-til\n" \
                                "Location: Central Nohla\nVisitor Friendly: Yes\nSub-Locations:\n| St. Guardia's Academy" \
                                "\n| Twilight Mall\n| Starrgem River\n\n"
                eklyptilDescription = "Eklyptil is the capital of Nohla, and the only island to be made up of more than " \
                                      "one island: Solaro and Lunaro, connected by sky bridges built at intervals " \
                                      "throughout the islands. The two islands resemble the sun and a crescent moon, " \
                                      "hence the name of the islands. The islands are aligned such that the sun is " \
                                      "placed into the curve of the crescent moon, creating a unique island structure. " \
                                      "The islands are separated by the Starrgem River. Because it is surrounded by the " \
                                      "other islands, it sees very concentrated amounts of moonlight during the night, " \
                                      "so the stones at the bottom of the river twinkle brightly causing the river to " \
                                      "sparkle, reflecting the night sky. On both Lunaro and Solaro, there are viewing " \
                                      "platforms and overhangs for people to sit and watch the river.\n\n"
                solaroDescription = "Solaro, Nohla\nSolaro, also known as Dawn Isle, is the sun-shaped island in Eklyptil. " \
                                    "St. Guardia's Academy is built on the edge of the island, and takes up almost a " \
                                    "third of the island's space. Because of the nature of Nohla, it is the most inclusive " \
                                    "branch of St. Guardia's since it doesn't lean towards tailoring its classes to one " \
                                    "specific race. This St. Guardia's is built around the edge of the island, and utilizes" \
                                    "the cliff side to build additional training ground terrains for students. The island " \
                                    "itself has lots of open space and is about 250 feet above sea level, so the weather " \
                                    "there is mostly warm, but very comfortable. A winding dirt road spirals the island " \
                                    "to give a safe way to get resources and people from arriving ships to and from the " \
                                    "city.\n\n"
                lunaroDescription = "Lunaro, Nohla\nLunaro, also known as Dusk Isle, is the moon-shaped island in Eklyptil. " \
                                    "It is the home of Twilight Mall, the biggest mall in the continent, and a hotspot " \
                                    "for tourists and visitors since it hosts a variety of popular foods, clothing, and " \
                                    "activities from different races. This gives visitors a true eye into other race's " \
                                    "cultures and customs. It's also a fun day trip because it has several indoor " \
                                    "activities, like an indoor theme park and movie theater. Bridges span across the " \
                                    "Starrgem River to Solaro, and a dirt path also spans across the inner curve of the " \
                                    "moon to sea level. It is much longer than the one in Solaro, however, due to Lunaro " \
                                    "being closer to 550 feet above sea level.\n\n"
                nohlaLocation = input(
                    "\033[1m" + "Eklyptil, Nohla\n\n" + "\033[0m" + eklyptilStats + eklyptilDescription +
                    solaroDescription + lunaroDescription + "Go back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Dullus Island Commands
            if nohlaLocations == "dullus":
                dullusStats = "Primary Resident Race: Majuu\nPronunciation: DULL-loos\nLocation: " \
                              "Southwestern Nohla\nVisitor Friendly: Yes\n\n"
                dullusDescription = "Dullus is a small island separated from the rest of Nohla. Though it is still part " \
                                    "of the continent, the island isn't part of the group of islands that make up the " \
                                    "rest of Nohla. The populace is mostly made up of majuu who have been thrown from " \
                                    "their homes in Xhia due to their crimes against their fellow majuu during The " \
                                    "Arduos War, as well as those who couldn't find their place in the world after leaving " \
                                    "Xhia because of prejudice. These majuu have grown kind due ot their time together, " \
                                    "and are very friendly towards outsiders who happen to visit their island. However, " \
                                    "due to who inhabits the island, many are afraid to go to Dullus, and have avoided " \
                                    "it altogether.\n\nThough the island doesn't import or export anything, the majuu are " \
                                    "able to sustain themselves through livestock and agriculture. Since they are so far " \
                                    "from the rest of Nohla, they used what little land they had to build themselves a " \
                                    "natural paradise. However, the population of Dullus drops nearly every generation " \
                                    "since the younger majuu often choose to leave for the mainland of Nohla or another " \
                                    "continent altogether. Because of this, the majuu have made a plan to be reliant on " \
                                    "nature, up to the point where if they all left, then the island would easily be reclaimed " \
                                    "by nature.\n\n"
                nohlaLocation = input("\033[1m" + "Dullus, Nohla\n\n" + "\033[0m" + dullusStats + dullusDescription +
                                      "Go back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Cingrigh Island Commands
            if nohlaLocations == "cingrigh":
                cingrighStats = "Primary Resident Race: Majuu\nPronunciation: CIN-gree\nLocation: " \
                                "Northeastern Nohla\nVisitor Friendly: Yes\n\nTown Trade:\n| Weapons\n| Armor\n" \
                                "Sub-Locations:\n| Magmatic Cavern\n  * Hellheat Forge\n\n"
                cingrighDescription = "Cingrigh is a mountainous island with a deep magmatic cavern in the center. " \
                                      "This, in addition to Nohla's tropical location, causes the climate to be " \
                                      "extremely hot nearly all the time. Majuu who originate from warmer climates " \
                                      "and therefore have lighter fur colors are more suited to live here. The island " \
                                      "itself isn't entirely hot, though, as the mountaintops are quite cool since " \
                                      "they are so high up. However, because of its altitude and low amounts of oxygen, " \
                                      "only avats make their homes that high up. Visitors to Cingrigh unless a majuu " \
                                      "or have a fire magic affinity must wear a form or heat resistance in order to " \
                                      "prevent overheating.\n\nInside the magmatic cavern lies the Hellheat Forge, the " \
                                      "largest forge in all of Phalmasia that's outside of Xhia. The natural flow of lava " \
                                      "throughout the cavern makes the weapons able to be forged and quenched at much " \
                                      "higher temperature differences, causing weapons and armor with increased durability. " \
                                      "This forge, however, is completely inaccessible to anyone but heat-resistant majuu " \
                                      "with fire affinities because of the insane temperatures within the forge. Only the " \
                                      "best blacksmiths may use it to prevent any fatal accidents, which serves to increase " \
                                      "the average quality of anything leaving the forge as well.\n\n"
                nohlaLocation = input(
                    "\033[1m" + "Cingrigh, Nohla\n\n" + "\033[0m" + cingrighStats + cingrighDescription +
                    "Go back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Talen Island Commands
            if nohlaLocations == "talen":
                talenStats = "Primary Resident Race: Avats\nPronunciation: TAL-en\nLocation: " \
                             "Eastern Nohla\nVisitor Friendly: Yes\n\nSub-Locations:\n| Eagle's Beach\n| Skyward " \
                             "Tower\n\n"
                talenDescription = "Talen is a flat island that somewhat resembles the talon of an eagle. The island rests " \
                                   "at sea level, and constantly has a cool sea breeze blowing across its landscape. " \
                                   "The resident avats love this because many of them have wind affinities that make them " \
                                   "feel more in tune with their magic. However, avats to generally like to live in high " \
                                   "places, and so they have build a tall tower on the tip of the island's talon. At the " \
                                   "top of the tower, there is a small grassy park that many avats with flyers license " \
                                   "jump off of it and glide down for a rush. Since the island is at sea level, it is " \
                                   "surrounded by a beach. The beach has naturally white sand because Talen makes an " \
                                   "effort to keep the beach clean. Eagle's Beach, as it is called, and the Skyward Tower " \
                                   "attract many tourists to Talen to spend time at the beautiful beaches and admire the " \
                                   "continent from above.\n\n"
                nohlaLocation = input("\033[1m" + "Talen, Nohla\n\n" + "\033[0m" + talenStats + talenDescription +
                                      "Go back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

            # Talen Island Commands
            if nohlaLocations == "skyhaven":
                skyhavenStats = "Primary Resident Race: Human\nPronunciation: SKY-hay-ven\nLocation: " \
                                "Southeastern Nohla\nVisitor Friendly: Yes\n\n"
                skyhavenDescription = "Skyhaven is the highest island in Nohla, but despite this, mostly humans made " \
                                      "their homes here. Despite not having magic and thereby not having any natural " \
                                      "resistances to the cold weather, they have made do by building heavily insulated " \
                                      "homes and having heat crystals littered throughout the town, being careful not to " \
                                      "have too many in one place in case they melted the snow to cause avalanches. " \
                                      "Humans here are commonly scientists and astronomers since they are closer to the " \
                                      "stars than anywhere else in Nohla. People who visit Skyhaven who don't have wind " \
                                      "affinities usually need an air pack because of the lack of oxygen due to the height. " \
                                      "Being so close to the stars makes for a beautiful view of the night sky, and " \
                                      "visitors commonly gather on the undeveloped edge of the island where light " \
                                      "pollution is lowest to view space.\n\n"
                nohlaLocation = input(
                    "\033[1m" + "Skyhaven, Nohla\n\n" + "\033[0m" + skyhavenStats + skyhavenDescription +
                    "Go back to the other islands of Nohla by pressing 'Enter'.\n").lower().strip()

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
        magicBarrier = input("There is one additional magic classification that can only be accessed by those who are "
                             "strong enough to wield them. Hints have been littered throughout the database. May the "
                             "stars guide your way.\n\nMagic:\n| Elemental Magic\n| Lost Magic\n| Sigils\n| Energy Elevage\n\nLeave the "
                             "database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n").lower().strip()

        while magicBarrier == "":
            magicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while magicBarrier != "elemental magic" and magicBarrier != "elemental" and magicBarrier != "lost magic" and magicBarrier != "lost" and magicBarrier != "sigils" and magicBarrier != "mythical elements" and magicBarrier != "mythical" and magicBarrier != "energy elevage" and magicBarrier != "elevage" and magicBarrier != "back" and magicBarrier != "leave":
            magicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Elemental Magic Commands
        while magicBarrier == "elemental magic" or magicBarrier == "elemental":
            elementalBarrier = input("Elemental Magic:\n| Fire\n| Water\n| Lightning\n| Wind\n| Ice\n| Earth\n\nLeave "
                                     "the database by entering 'Leave'. Go back to magic selection prompt by entering"
                                     " 'Back'.\n").lower().strip()

            while elementalBarrier == "":
                elementalBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while elementalBarrier != "fire" and elementalBarrier != "water" and elementalBarrier != "lightning" and elementalBarrier != "wind" and elementalBarrier != "ice" and elementalBarrier != "earth" and elementalBarrier != "back" and elementalBarrier != "leave":
                elementalBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # Fire Magic Commands
            if elementalBarrier == "fire":
                fireExplanation = "Passive Ability: Resistance to non-magic flames & heat\n\nFire magic is a magic " \
                                  "geared more towards offense, and the only magic that continue to grow without the " \
                                  "caster's maintenance or mana. This also makes the magic difficult to control for " \
                                  "new fire users. This magic is commonly associated with the caster's emotions, " \
                                  "since it sometimes grows in power in accordance to them. Fire users are known to " \
                                  "be determined, motivated, or obnoxious when accomplishing their goals."
                fireSpells = "Basic Spells:\n| Ember Palm: The user covers their hands, and occasionally arms, " \
                             "in fire magic. This both adds extra power in close-range fights, and allows for basic " \
                             "ranged attacks.\n| Burst Step Spells: The user covers their feet, and occasionally " \
                             "legs, in fire magic. This both adds extra power in close-range fights. Additionally, " \
                             "it can be used to concentrate mana under the user's feet and create an explosion that " \
                             "boosts their jump height.\n| Combustion Spells: A ranged application of fire magic that " \
                             "allows the user to concentrate their mana at a distance and cause an explosion."
                fireUsers = "Notable Users:\n| Mirago Fynae\n| Kimiko Quintai\n| Kinto Vareli\n| Sereina Fynae"
                fireMagic = input(
                    "\033[1m" + "Fire, the Element of Ambition" + "\033[0m\nSigil Color Representation: Red\n" + fireExplanation + "\n\n" + fireSpells + "\n\n" + fireUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Water Magic Commands
            if elementalBarrier == "water":
                waterExplanation = "Passive Ability: Using mana to walk on water\n\nWater magic is a magic geared " \
                                   "towards defense. Using this magic takes tact and planning. Users of water magic " \
                                   "are able to alter the temperature of water by freezing and boiling it. Users of " \
                                   "water magic are known to be relaxed and in tune with their surroundings, " \
                                   "and are passive about their thoughts and opinions."
                waterSpells = "Basic Spells:\n| Breath Spells: The user takes a large breath to increase their lung " \
                              "capacity so they can stay underwater for longer periods of time. They do this by " \
                              "surrounding their heads with an air bubble. The stronger the caster of the spell, " \
                              "the larger the air bubble is, and the more people can fit in it.\n| Glow Spells: This " \
                              "type of spell can only be used when the user's hands are covered in water. The caster " \
                              "uses mana to make the water " \
                              "around their hands glow to illuminate dark underwater areas. The brightness and " \
                              "proximity of the glow is determined by the caster's strength.\n| Moisture Spells: This " \
                              "spell is the basis of water magic. Users can't create their own element like many of " \
                              "the other magics, and aren't around it at all times, either. This spell allows them to " \
                              "take water from the air and plants in the surroundings to use."
                waterUsers = "Notable Users:\n| Mimi Seiran\n| Amiru Soaren"
                waterMagic = input(
                    "\033[1m" + "Water, the Element of Flow" + "\033[0m\nSigil Color Representation: Blue\n" + waterExplanation + "\n\n" + waterSpells + "\n\n" + waterUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Lightning Magic Commands
            if elementalBarrier == "lightning":
                lightningExplanation = "Passive Ability: Short distance teleportation\n\nLightning is a magic that " \
                                       "specializes in quick, precise attacks. If dealt with enough power, " \
                                       "these attacks may inflict extra shock damage or even temporary paralysis. Due " \
                                       "to the concentration of lightning magic, it can easily be used to penetrate a " \
                                       "target's armor. Though the magic's overall power isn't substantial, " \
                                       "it more than makes up for it in speed. Users of lighting magic are known to " \
                                       "be excitable and confident."
                lightningSpells = "Basic Spells:\n| Shock Step: The caster releases lightning from their feet, " \
                                  "allowing for increased movement speed. High level casters will leave trails behind " \
                                  "them as they move, which cause added shock damage and possible paralysis.\n| Dart " \
                                  "Spells: The caster releases a quick bolt from their hands, dealing damage and " \
                                  "possibly stunning the target."
                lightningUsers = "Notable Users:\n| Cidelli Reimora\n| Ryner Khabunago"
                lightningMagic = input(
                    "\033[1m" + "Lightning, the Element of Precision" + "\033[0m\nSigil Color Representation: Yellow\n" + lightningExplanation + "\n\n" + lightningSpells + "\n\n" + lightningUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Wind Magic Commands
            if elementalBarrier == "wind":
                windExplanation = "Passive Ability: Slight flight & Gliding\n\nWind, when used in high " \
                                  "concentrations, can be used to slice objects or opponents at high speeds. " \
                                  "Defensively, however, it must deflect most magic attacks and projectiles. This " \
                                  "magic is preferred by those who use speed and agility in their combat. Using their " \
                                  "magic, they are also able to use streams of wind to push and pull objects from a " \
                                  "distance. Users of wind magic are known to be lone wolves who travel their own " \
                                  "path and fight for what they think is right."
                windSpells = "Basic Spells:\n| Lightfoot Spells: The caster channels mana into their feet which " \
                             "allows them to increase their speed and jump height, cushion their landings, and, " \
                             "along with the help of a glider, glide and even fly for a short period of time.\n| " \
                             "Breath Spells: The caster gathers mana in their lungs to increase their lung capacity " \
                             "to blow out winds of high speeds, increase their volume, and hold their breath for a " \
                             "prolonged period of time. The more experienced the caster, the more air can be brought " \
                             "into the lungs.\n| Sharp Spells: The caster presses mana together to create a sharp " \
                             "blade of wind with which they can throw as a projectile or attach to their body as a " \
                             "sword-like extension. The size, speed, and cutting power of these blasts are dependent " \
                             "on the strength of the caster."
                windUsers = "Notable Users:\n| Xaeyz Kai\n| Yggdrasil Aensyll\n| Yumeizu Artilux"
                windMagic = input(
                    "\033[1m" + "Wind, the Element of Free Paths" + "\033[0m\nSigil Color Representation: Teal\n" + windExplanation + "\n\n" + windSpells + "\n\n" + windUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Ice Magic Commands
            if elementalBarrier == "ice":
                iceExplanation = "Passive Ability: Resistance to non-magic based freezing temperatures.\n\nIce is a " \
                                 "powerful magic for both offensive and defensive capabilities. This magic is " \
                                 "extremely deadly to even the user at times, so using it with a pact for better " \
                                 "control is highly recommended. This magic has the capability to penetrate a " \
                                 "target's armor, but not with the level of proficiency of lightning. They can freeze " \
                                 "the air, water or ground around them, which allows for an increased range of " \
                                 "mobility on the battlefield and place-locking opponents. It is also the only magic " \
                                 "with no distinguishing base shape, coming out in spikes if used in brute force."
                iceSpells = "Basic Spells:\n| Frost Fire: The user conjures a freezing flame that shocks armor, " \
                            "withering it away and making it easier to penetrate. This can cause serious damage if " \
                            "use directly on a person's vitals with extreme intensity.\n| Spike Bullet: The user " \
                            "creates multiple ice spikes that float behind the user's back until they call for them " \
                            "to be fired. These can be shaped into any object, but spikes are most commonly used as " \
                            "they deal a lot of piercing damage. The speed, durability, and size of these projectiles " \
                            "scale with the user's strength."
                iceUsers = "Notable Users:\n| Aeiyou Drefael"
                iceMagic = input(
                    "\033[1m" + "Ice, the Element of Resistance" + "\033[0m\nSigil Color Representation: Light Blue\n" + iceExplanation + "\n\n" + iceSpells + "\n\n" + iceUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Earth Magic Commands
            if elementalBarrier == "earth":
                earthExplanation = "Passive Ability: Hardened resistance to magic based attacks.\n\nEarth is a magic " \
                                   "that is both offensive and defensive. Earth magic relies on the ground beneath " \
                                   "the user's feet, giving them free reign to control the battlefield at will. Being " \
                                   "such a sturdy magic, earth can easily use their defense as offense and vice " \
                                   "versa. Due to this, it has a lot of ways to counter other elements. Though earth " \
                                   "magic uses the most magic energy to cast spells of all other elemental magics as " \
                                   "well as the shortest casting range, its combat capability more than makes up for " \
                                   "it. This magic is preferred by those who fight up close."
                earthSpells = "Basic Spells:\n| Earth's Step: The user impacts the ground, creating a crack and " \
                              "sending a wave of earth in the direction of their target. It is a good move to narrow " \
                              "the opponent's line of sight, as well as throw them off their balance.The stronger the " \
                              "caster, the larger the wave.\n| Pillar Spells: The user creates pillars of earth from " \
                              "the ground, striking opponents or use as a defense. They can also be ripped from the " \
                              "ground and float in midair for a while. The stronger the caster is, the larger the " \
                              "pillars will be, and the faster they can create them.\n| Soft Sand Spells: The caster " \
                              "concentrates their mana on a certain area on the ground and softens it, creating a " \
                              "quicksand-like pit. This sinks the target down as far as their torso, and extremely " \
                              "strong casters can sink opponents down to their shoulders. It is impossible to use " \
                              "this spell to sink someone completely."
                earthUsers = "Notable Users:\n| Aeiyou Drefael\n| Kinto Vareli\n| Turcobé Sentai"
                earthMagic = input(
                    "\033[1m" + "Earth, the Element of Nature" + "\033[0m\nSigil Color Representation: Brown\n" + earthExplanation + "\n\n" + earthSpells + "\n\n" + earthUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Elemental Magic Exit Command
            if elementalBarrier == "back":
                elementalBarrier = "back"
                break
            if elementalBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Lost Magic Commands
        while magicBarrier == "lost magic" or magicBarrier == "lost":
            lostBarrier = input("Lost Magic:\n| Shadow\n| Nature\n| Life\n| Gravity\n\nLeave the database by entering "
                                "'Leave'. Go back to magic selection prompt by entering 'Back'.\n").lower().strip()

            while lostBarrier == "":
                lostBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while lostBarrier != "shadow" and lostBarrier != "nature" and lostBarrier != "life" and lostBarrier != "gravity" and lostBarrier != "back" and lostBarrier != "leave":
                lostBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # Shadow Magic Commands
            if lostBarrier == "shadow":
                shadowExplanation = "Passive Ability: Creating shadow copies. The mana cost increases with the number " \
                                    "of clones.\n\nShadow is a magic that only the Khabunago Family is capable of; a " \
                                    "family of spirits that use Sprite Pacts to gain mortal & physical forms. They " \
                                    "are the spiritual protectors of graveyards, guarding them from any who wish to " \
                                    "disturb the graves of those who are buried there. Shadow magic allows the user " \
                                    "to create and manipulate darkness. It is possible to create solid shadows using " \
                                    "this magic, which can be used to cause extreme damage. Many classify this as a " \
                                    "dark magic, and can be easily dispelled with fire magic."
                shadowSpells = "Basic Spells:\n| Cloak Spells: The caster hides their physical body in a nearby " \
                               "shadow, increasing their movement speed and travel capabilities. They are able to be " \
                               "damaged while in their shadow by attacking the shadow directly. The less mana you " \
                               "have remaining, the slower you move, and the more you are pushed out of the " \
                               "shadow.\n| Tendril Spells: The caster shapes the surrounding shadows into solid " \
                               "spike-like structures that can grab or damage opponents. The more proficient the " \
                               "caster, the more range and damage they can deal.\n| Dark Mana: The caster forms " \
                               "projectiles from the surrounding shadows and throws them at the target. It can also " \
                               "be used to lock the shadows of the target in place, restraining their movement. This, " \
                               "however, is an active ability, and no other spells can be cast while restraining a " \
                               "target. The stronger the caster, the longer the stun, and the stronger the " \
                               "projectile.\n| Banish Spells: The caster concentrates the shadows of the target to " \
                               "strangle themselves, cutting off the target's flow of mana and preventing them from " \
                               "casting spells for a short time."
                shadowUsers = "Notable Users:\n| Ryner Khabunago"
                shadowMagic = input(
                    "\033[1m" + "Shadow, the Element of Reflection" + "\033[0m\nSigil Color Representation: Black\n" + shadowExplanation + "\n\n" + shadowSpells + "\n\n" + shadowUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Nature Magic Commands
            if lostBarrier == "nature":
                natureExplanation = "Passive Ability: Immunity to non-magic based poison & paralysis from " \
                                    "plants.\n\nNature is a magic that works similarly to Earth; the only difference " \
                                    "is it utilizes the plants instead of the ground itself. It can cause plants to " \
                                    "grow at and extremely quick pace, as well as change their capabilities by making " \
                                    "them poisonous. All poison created by a user's spells do not affect the caster. " \
                                    "This also allows the user to create and manipulate wood, which creates strong " \
                                    "and versatile defenses. This magic has an advantage against wind magic."
                natureSpells = "Basic Spells:\n| Nurture Spells: The caster channels mana into wildlife around them " \
                               "and increases their growth speed. It is the core of nature magic and the basis of all " \
                               "its spells, as it also gives the caster control of all plants in the area. The more " \
                               "proficient the caster, the faster the rate of growth becomes, and the more precise " \
                               "the control gets.\n| Vine Spells: The user grows vines that can emerge from anywhere " \
                               "on the battlefield within the caster's reach. They are used to attack and grab " \
                               "targets. The stronger the caster, the faster and longer the vines can become.\n| " \
                               "Property Spells: The caster concentrates mana into the surrounding plants and changes " \
                               "their properties, allowing them to emit spores with effects of the caster's choice. " \
                               "The larger the plant, the larger the mana cost."
                natureUsers = "Notable Users: None"
                natureMagic = input(
                    "\033[1m" + "Nature, the Element of Harvest" + "\033[0m\nSigil Color Representation: Dark Green\n" + natureExplanation + "\n\n" + natureSpells + "\n\n" + natureUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Life Magic Commands
            if lostBarrier == "life":
                lifeExplanation = "Passive Ability: Natural healing factor is enhanced.\n\nOf all magic, Life is the " \
                                  "most risky and dangerous to use. It uses a visible stream of life energy to cast " \
                                  "and use spells. Life magic can also heal targets, but at a high cost to the user."
                lifeSpells = "Basic Spells:\n| Give & Take Spells: The caster channels a stream of life that takes " \
                             "from one thing to give to another. This can be used to transfer resources from one " \
                             "place to another, like water or nutrients. If the caster takes something from one thing " \
                             "or person, it loses said status and the receiving end gains said status.\n| Sacrifice " \
                             "Spells: A sub-genre of Give & Take Spells that specifically deals with human injury and " \
                             "basic healing. This revolves around the caster taking injuries from one target and " \
                             "giving them to another. This results in the healing of the initial target and the " \
                             "injury of the post target, and requires both party's consent to work.\n| Absorb Spells: " \
                             "The caster wraps their hand in a mana " \
                             "stream that draws all mana-based attacks towards it and absorbs them. This replenishes " \
                             "the caster's mana supply proportional to the amount of mana the target used to cast the " \
                             "spell.\n| Mirror Spells: The caster surrounds both arms with streams of mana. This " \
                             "absorbs a mana-based spell targeted at the caster with one hand, then releases the " \
                             "spell through the opposite arm. This, however, takes mana, and the caster must expend " \
                             "mana equal to the amount of mana used to cast the original spell."
                lifeUsers = "Notable Users:\n| Mirago Fynae"
                lifeMagic = input(
                    "\033[1m" + "Life, the Element of Sacrifice" + "\033[0m\nSigil Color Representation: Green\n" + lifeExplanation + "\n\n" + lifeSpells + "\n\n" + lifeUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Gravity Magic Commands
            if lostBarrier == "gravity":
                gravityExplanation = "Passive Ability: A psychic-like ability that allows the user to lift and " \
                                     "manipulate objects with their mana.\n\nGravity magic is the rarest of all " \
                                     "magics. It can only be used by Argenian families who live in the mountainous " \
                                     "regions of Mu'karr. Using this magic makes the controlling mana invisible to " \
                                     "both the user and those around them, as well as the largest attack radius of " \
                                     "all magics. It controls gravity in a spherical radius around the target of the " \
                                     "spells, and works as a psychic ability would. Gravity can be used to move " \
                                     "objects to the will of the user. However, due to its rarity, those who have it " \
                                     "usually don't know how to control it. The user can choose whether or not the " \
                                     "gravity they manipulate affects them or not."
                gravitySpells = "Basic Spells:\n| Barrier Spells: The user emits an arc radius towards the casting " \
                                "direction. This makes any target that enters that radius shoot towards the ground, " \
                                "physical or mana based, before it can deal damage to the caster. Though it has never " \
                                "been a recorded attempt, it may be possible to increase gravity to a degree that a " \
                                "magic-based spell that enters the barrier is immediately dispelled.\n| Impulse " \
                                "Spells: The caster compresses their mana into a sphere and sends it at a target " \
                                "location. On either command or impact, the sphere disperses, releasing a powerful " \
                                "impulse that forcefully pushes everything in the sphere's radius away from the " \
                                "center of the sphere.\n| Push Spells: A melee based spell. The user concentrates " \
                                "mana in their palm and strikes the target. This causes a blow that deals devastating " \
                                "damage and sends the target flying backward. This can also be used to create " \
                                "shockwaves when striking the air."
                gravityUsers = "Notable Users:\n| Xaeyz Kai\n| Sereina Fynae"
                gravityMagic = input(
                    "\033[1m" + "Gravity, the Element of Control" + "\033[0m\nSigil Color Representation: Gray\n" + gravityExplanation + "\n\n" + gravitySpells + "\n\n" + gravityUsers + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Lost Magic Exit Command
            if lostBarrier == "back":
                lostBarrier = "back"
                break
            if lostBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Sigils Commands
        while magicBarrier == "sigils":
            sigilBarrier = input("Sigils:\n| About Sigils\n| Unity Sigils\n| Sectional Sigils\n\nLeave the database "
                                 "by entering 'Leave'. Go back to magic selection prompt by entering "
                                 "'Back'.\n").lower().strip()

            while sigilBarrier == "":
                sigilBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while sigilBarrier != "unity sigils" and sigilBarrier != "sectional sigils" and sigilBarrier != "about sigils" and sigilBarrier != "sigils" and sigilBarrier != "unity" and sigilBarrier != "sectional" and sigilBarrier != "back" and sigilBarrier != "leave":
                sigilBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # About Sigils Commands
            if sigilBarrier == "about sigils" or sigilBarrier == "sigils":
                sigilExplanation = "\033[1m" + "About Sigils" + "\033[0m\n\nSigils are unique magic mechanics that are only available to " \
                                                                "those with two magics. Once a user unlocks their second element, a symbol shaped of " \
                                                                "either a circle, triangle, square, or diamond will manifest itself on the back, " \
                                                                "neck, chest, or stomach of the user. This sigil begins passively storing the " \
                                                                "user's mana, increasing the maximum amount the user can hold at once. It can hold " \
                                                                "up to 25% of the maximum mana capacity of the user.\n\nThough the user can use " \
                                                                "this stored mana normally, the user can tap into the power of the " \
                                                                "sigil, spreading the power across their body. This is shown by streams of mana " \
                                                                "extending over their limbs. This floods the body with the previously stored mana, " \
                                                                "increasing the strength, speed, and overall effectiveness of spells casted. However, this boost lasts proportionally " \
                                                                "long to the amount of mana stored, meaning those with higher amounts of stored mana " \
                                                                "can use sigil boosts for longer periods of time.\n\nIf the user has a *mythical " \
                                                                "element*, however, this time limit is doubled, as they have heightened control over " \
                                                                "their mana, though it doesn't increase the power of *mythical " \
                                                                "elements* any."
                sigils = input(sigilExplanation + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()
            # Unity Sigil Commands
            if sigilBarrier == "unity sigils" or sigilBarrier == "unity":
                unityExplanation = (
                            "\033[1m" + "Unity Sigils" + "\033[0m\n\nUnity Sigils are base sigils, and the ones that awaken for all their users. "
                                                         "Unity sigils blend the colors of the two magics the user controls, then uses that "
                                                         "swirled color to make up the sigil. The user of the sigil can choose to use the "
                                                         "sigil's stored mana normally, or shoot the mana through the user all at once. If "
                                                         "the user decides to do this, in a process dubbed a Mana Surge, the streams of mana "
                                                         "that will cover the user's body will be composed of the two swirled colors of the "
                                                         "sigil. This will boost the mana output and, because of mana's connection to life "
                                                         "energy, the physical ability of the user by roughly 20%. ")
                unitySigil = input(
                    "Unity Sigils\n\n" + unityExplanation + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Sectional Sigil Commands
            if sigilBarrier == "sectional sigils" or sigilBarrier == "sectional":
                sectionalExplanation = (
                            "\033[1m" + "Sectional Sigils" + "\033[0m\n\nSectional Sigils, also known as Evolved Sigils, are attained by extreme mana "
                                                             "control, and are completely up to the user's decision. A Unity Sigil will not "
                                                             "evolve into a Sectional Sigil unless the user meets the requirements "
                                                             "and wills the sigil to evolve. Once evolved into a Sectional Sigil, "
                                                             "a user is completely unable to return to using a Unity Sigil.\n\nTo attain a "
                                                             "Sectional Sigil, the user must have mastered use of the Unity Sigil, "
                                                             "and have completed an Energy Elevage. Once both of these requirements is "
                                                             "met, the user must go through a unique version of Energy Elevage. Instead of "
                                                             "focusing their mana into their own core, they will be forcing it into the sigil. "
                                                             "This will cause it to destabilize and shut down, locking away sigil usage for one year. "
                                                             "Unlike a usual Energy Elevage, however, this does not remove the ability to cast "
                                                             "mana since it is taking place in the sigil and not the core. Once the year is up, "
                                                             "the sigil reactivates and floods the body with the stored mana in what is essentially "
                                                             "a forced Mana Surge that the user will not be able to turn off. After this is done, "
                                                             "the process is fully complete, and the user will have a Sectional Sigil.\n\nThe power of "
                                                             "the Sectional Sigil is relatively similar in function "
                                                             "to the Unity Sigil. However, instead of the blended color, the sigil sections "
                                                             "the magic by evenly splitting itself, leaving each half of the sigil to "
                                                             "reflect one of the user's magics. This means that the user is limited to "
                                                             "using up to 50% of the sigil's stored energy for each magic. Each section "
                                                             "stores 15% of the user's total mana capacity, for a total increased "
                                                             "storage of 30%. This is due to the second Energy Elevage. \n\nWhile "
                                                             "activated completely, the user can choose to activate half of their sigil. "
                                                             "When this is done, the streams that cover the user's body take on the color "
                                                             "of the chosen magic. Because the user is only activating half of the sigil, "
                                                             "the boost only lasts half as long as it did before. This only lasts for the chosen magic, "
                                                             "meaning that the magic not associated with the activated half of the sigil will not get the "
                                                             "power boost. Additionally, if both sides of the Sectional Sigil are "
                                                             "used simultaneously, then the streams take on either one magic color of "
                                                             "the two magic colors of the user, and the power boost given is raised to 50% for "
                                                             "both magics. This boost cannot be turned off unlike a typical Mana Surge, and only stops once either half of "
                                                             "the sigil runs out of magic. This boost is known as a Mana Baryon. Because the amount of mana flowing through the user "
                                                             "was so much greater than the body is used to for such a long period of time, any magic "
                                                             "that runs out of mana during a Mana Baryon cannot be used again until that magic's half "
                                                             "of the sigil is completely filled again. This also means that the sigil must regenerate "
                                                             "the lost mana on it's own over time; the user cannot simply refill the sigil manually. "
                                                             "This may take anywhere from a day to a week depending "
                                                             "on the mana capacity of the user's sigil.")
                sectionalSigil = input(
                    "Sectional Sigils\n\n" + sectionalExplanation + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Sigil Exit Command
            if sigilBarrier == "back":
                sigilBarrier = "back"
                break
            if sigilBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Mythical Elemental Commands
        while magicBarrier == "mythical elements" or magicBarrier == "mythical element" or magicBarrier == "mythical" or magicBarrier == "mythic":
            mythicBarrier = input("The secret powers of Phalmasia reveal themselves to you...\n\nMythical "
                                  "Elements:\n| Dynamic Water\n| Zenith Earth\n| Cosmic Wind\n| Onyx Fire\n| Electron "
                                  "Lightning\n| Permafrost Ice\n\nUnison Techniques:\n| Mythical Beasts\n| Rebirth"
                                  "\n\nLeave the database by entering 'Leave'. Go back to "
                                  "magic selection prompt by entering 'Back'.\n").lower().strip()

            while mythicBarrier == "":
                mythicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
            while mythicBarrier != "dynamic water" and mythicBarrier != "zenith earth" and mythicBarrier != "cosmic wind" and mythicBarrier != "onyx fire" and mythicBarrier != "electron lightning" and mythicBarrier != "permafrost ice" and mythicBarrier != "mythical beasts" and mythicBarrier != "rebirth" and mythicBarrier != "back" and mythicBarrier != "leave":
                mythicBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

            # Dynamic Water Commands
            if mythicBarrier == "dynamic water":
                mythicWaterStats = "\033[1m" + "Dynamic Water, the Mythical Element of the Sea" + "\033[0m\n\nMythical Spirit Name: " \
                                                                                                  "Lumen\nSigil Color Representation: Dark Blue\nMythical Enhancement: Increased " \
                                                                                                  "Water Pressure & Healing Factor\nMythical Beast: Sea Serpent\nPower Event: King " \
                                                                                                  "Tides"
                mythicWaterDescription = "Dynamic Water is the Mythical Element of the Sea, and Lumen is its spirit. " \
                                         "Lumen is a serene spirit; she rarely does anything to disturb others and " \
                                         "keeps to herself. She spends her time caring for the seas and its life. She " \
                                         "ensures that all sea creatures are being treated fairly, and uses her power " \
                                         "to stop them from bullying or hurting each other unjustly.\n\nDynamic Water " \
                                         "can heal diseases in the oceanic animals and purify the water from " \
                                         "pollution. It can also be used to heal injuries to a greater degree than " \
                                         "other mythical elements, but still doesn't hold a candle to the healing " \
                                         "abilities of Life. It also has a unique compression factor that makes it " \
                                         "possible to compress the water far more than ordinary water, which leads to " \
                                         "increased water pressure. This creates a large boost in its destructive " \
                                         "capabilities. Dynamic Water also has bioluminescent properties."
                mythicWater = input(
                    mythicWaterStats + "\n\n" + mythicWaterDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Zenith Earth Commands
            if mythicBarrier == "zenith earth":
                zenithEarthStats = "\033[1m" + "Zenith Earth, the Mythical Element of the Terrain" + "\033[0m\n\nMythical Spirit Name: " \
                                                                                                     "Chrono\nSigil Color Representation: Dark Gray\nMythical Enhancement: Increased " \
                                                                                                     "Earthen Nutrients & Lava Manipulation\nMythical Beast: Golem\nPower Event: " \
                                                                                                     "Volcanic Eruptions"
                zenithEarthDescription = "Zenith Earth is the Mythical Element of the Terrain, and Chrono is its " \
                                         "spirit. Chrono is an extremely determined and trustworthy spirit. He always " \
                                         "sticks up for those he cares about, as well as for the health of the " \
                                         "terrain. His steadfast nature is perfect for commanding the earth to his " \
                                         "bidding, and makes him a reliable friend. Zenith Earth provides a boosted " \
                                         "number of nutrients to the plant life in the area, increasing their life " \
                                         "force and allowing them to grow faster and into more beautiful plants, " \
                                         "acting as a pseudo-nature magic. It is, of course, inferior to the real " \
                                         "thing since it cannot manipulate the plants it grows, and cannot grow plants " \
                                         "as fast due to only providing nutrients and not direct magic.\n\nHowever, " \
                                         "his main strength lies in the ability to manipulate the phase of the earth " \
                                         "he uses, changing it into lava. He can then use this transmuted lava as if " \
                                         "it was earth and attack his target with it, making his attacks extremely " \
                                         "volatile."
                zenithEarth = input(
                    zenithEarthStats + "\n\n" + zenithEarthDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Cosmic Wind Commands
            if mythicBarrier == "cosmic wind":
                cosmicWindStats = "\033[1m" + "Cosmic Wind, the Mythical Element of the Stars" + "\033[0m\n\nMythical Spirit Name: " \
                                                                                                 "Aeon\nSigil Color Representation: Purple\nMythical Enhancement: Stardust " \
                                                                                                 "Manipulation & Vacuum Override\nMythical Beast: Phoenix\nPower Event: Aurora " \
                                                                                                 "Borealis"
                cosmicWindDescription = "Cosmic Wind is the Mythical Element of the Stars, and Aeon is its spirit. " \
                                        "Aeon is a free soul and lives on trying to keep everyone around him safe " \
                                        "while being as free as possible. He does as he pleases most of the time, " \
                                        "but he is also responsible for guiding starlight to Phalmasia, as well as " \
                                        "creating constellations. Essentially, he is responsible for all celestia " \
                                        "visible from Phalmasia.\n\nCosmic Wind isn't composed of Phalmasian air; " \
                                        "it's the manipulation of Solar Wind & Stardust. This gives cosmic wind " \
                                        "control over stardust, which it can use for an assortment of tasks. Stardust " \
                                        "can be used for the enhancement of attacks and revitalize the life force of " \
                                        "those it chooses, increasing the effected's healing factor. Additionally, " \
                                        "because Cosmic Wind is composed of Solar Wind, it has the versatility of " \
                                        "being used within a vacuum, or a place with no air, like space. This also " \
                                        "gives it the capability of producing artificial auroras by shooting large " \
                                        "quantities of magic into the atmosphere."
                cosmicWind = input(
                    cosmicWindStats + "\n\n" + cosmicWindDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Onyx Fire Commands
            if mythicBarrier == "Onyx Fire" or mythicBarrier == "Onyx fire" or mythicBarrier == "onyx Fire" or mythicBarrier == "onyx fire":
                onyxFireStats = "\033[1m" + "Onyx Fire, the Mythical Element of the Sun" + "\033[0m\n\nMythical Spirit Name: Arc\nSigil Color " \
                                                                                           "Representation: Pure Black\nMythical Enhancement: Heat Amplification & Eternal " \
                                                                                           "Flames\nMythical Beast: Dragon\nPower Event: Solar Storms"
                onyxFireDescription = "Onyx Fire is the Mythical Element of the Sun, and Arc is its spirit.  Arc is " \
                                      "an ambitious and dedicated soul who tries to keep to those he trusts close and " \
                                      "always strives to become stronger with his friends. He is consistently aiming " \
                                      "to get better at everything he does and is extremely competitive when with " \
                                      "those close to him. Arc is responsible for the maintenance of the sun. He " \
                                      "keeps the balance of its intense power from radiating too far from its core " \
                                      "and damaging the planets that orbit it (including Phalmasia).\n\nOnyx Fire " \
                                      "burns with a dark black flame that has special properties. Unlike other " \
                                      "flames, Onyx Fire can be eternal; it can't go out unless the user wants it to. " \
                                      "This is because it doesn't depend on air to burn, and it is unaffected by " \
                                      "physical interactions, like water or other fire extinguishers. It also has the " \
                                      "innate property to burn at a higher temperature than other flames, as well as " \
                                      "perfectly control flame temperature even on flames that have already been cast."
                onyxFire = input(
                    onyxFireStats + "\n\n" + onyxFireDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Electron Lightning Commands
            if mythicBarrier == "electron lightning":
                electronLightningStats = "\033[1m" + "Electron Lightning, the Mythical Element of the Skies" + "\033[0m\n\nMythical Spirit " \
                                                                                                               "Name: Nova\nSigil Color Representation: Dark Red\nMythical Enhancement: " \
                                                                                                               "Electron Destabilization & Silent Thunder\nMythical Beast: Raijū\nPower " \
                                                                                                               "Event: Supercell Thunderstorms"
                electronLightningDescription = "Electron Lightning is the Mythical Element of the Skies, and Nova is " \
                                               "its spirit. Nova is an rational and precise soul. He thinks about how " \
                                               "his actions affect everyone and everything around him, and that makes " \
                                               "him a valuable spirit when in times of turmoil. He is also an " \
                                               "energetic and excitable spirit who finds interest in magic, " \
                                               "which gives him an aptitude of control over Electron " \
                                               "Lightning.\n\nNova is responsible for maintaining the weather. He " \
                                               "keeps the weather from becoming too destructive & disruptive to " \
                                               "Phalmasia's life and terrain. He is also responsible for maintaining " \
                                               "the strength and effectiveness of the atmosphere, as well as " \
                                               "preventing its degradation.\n\nElectron Lightning has the ability of " \
                                               "electron destabilization. This lightning is compressed so thin that " \
                                               "the temperature increases far higher than that of normal lightning. " \
                                               "This, instead of compressing the air around it, destabilizes the " \
                                               "electrons of air and burns them. This creates a section of " \
                                               "unbreathable air around the impact area. As a result of not " \
                                               "compressing but burning the air, the lightning does not create a " \
                                               "thunder sound, causing silent attacks until the moment of impact."
                electronLightning = input(
                    electronLightningStats + "\n\n" + electronLightningDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Permafrost Ice Commands
            if mythicBarrier == "permafrost ice":
                permafrostIceStats = "\033[1m" + "Permafrost Ice, the Mythical Element of the Moon" + "\033[0m\n\nMythical Spirit Name: " \
                                                                                                      "Cryo\nSigil Color Representation: Light Purple\nMythical Enhancement: Dry Ice & " \
                                                                                                      "Contact Freeze\nMythical Beast: Kitsune\nPower Event: Whiteouts"
                permafrostIceDescription = "Permafrost Ice is the Mythical Element of the Moon, and Cryo is its " \
                                           "spirit. Cryo is a closeted soul, choosing to keep to herself for the most " \
                                           "part. She is also extremely organized and likes to keep her surroundings " \
                                           "clean. Cryo is responsible for the maintenance of the moon. She is " \
                                           "responsible for ensuring that the orbit of the moon is steady and " \
                                           "continuous, and that it doesn't interfere with the sunlight " \
                                           "often.\n\nPermafrost Ice is unlike normal ice in composition which is " \
                                           "composed of frozen water; it is frozen carbon dioxide. Because it is a " \
                                           "gas, as it is released it creates shrouds of the gas around it as the ice " \
                                           "melts. This also allows for it to freeze at much lower temperatures than " \
                                           "normal ice: absolute zero. Permafrost Ice also has the innate ability to " \
                                           "contact freeze. This means that if any amount of Permafrost Ice comes " \
                                           "into contact with water, it freezes it starting from the point of contact " \
                                           "of the Permafrost Ice."
                permafrostIce = input(
                    permafrostIceStats + "\n\n" + permafrostIceDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Mythical Beasts Commands
            if mythicBarrier == "mythical beasts":
                mythicalBeastStats = "\033[1m" + "Mythical Beast Manifestation" + "\033[0m\n\tMythical Tier Spell\n\n| Spell Style: " \
                                                                                  "Mode/Utility\n| Mastery: Extreme"
                mythicalBeastDescription = "A unique type of magic manipulation only capable by mythical element users. " \
                                           "The process of doing this is something that only the mythical elemental " \
                                           "know, and the casting of which something only their users can handle due " \
                                           "to their increased mana capacities and higher skill ceilings. The spell " \
                                           "revolves around summoning the spirit of the mythical element's mythical " \
                                           "beast around the user, giving the user the abilities of the beast, " \
                                           "additional magical power, and specialized spells only usable in the beast " \
                                           "form.\n\nThis spell has two forms. One is where the user transforms into a " \
                                           "hybrid being, keeping their size but gaining magic appendages that resemble " \
                                           "their mythical beasts, like wings, tails, and horns. The other is when the " \
                                           "user transforms completely into their beast, constructing the body of their " \
                                           "own mana and controlling them from within with their hybrid form. Both forms " \
                                           "increase magic utility and damage to an incredible degree, making it an " \
                                           "extremely useful part of any mythical elemental user's arsenal."
                mythicalBeast = input(
                    mythicalBeastStats + "\n\n" + mythicalBeastDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Rebirth Commands
            if mythicBarrier == "rebirth":
                rebirthStats = "\033[1m" + "Rebirth" + "\033[0m\n\tMythical Tier Spell\n\n| Spell Style: Conditional/Medicinal\n| " \
                                                       "Mastery: Impossible"
                rebirthDescription = "Rebirth is an extremely powerful spell that no one but the mythical elementals " \
                                     "themselves can cast. Being a conditional spell, there are several requirements " \
                                     "that must be met before activation. The mythical elemental must be bonded to " \
                                     "a living user for over a year, and the user must be on the brink of death or " \
                                     "have died less than 10 minutes prior. If the spell is not cast during this " \
                                     "time, the spell will fail. The mythical elemental must also want to revive " \
                                     "their user, meaning that the user cannot cast this spell on themselves, both " \
                                     "because they physically couldn't while on the brink of death, and the user " \
                                     "requires consent from their elemental before the spell can be casted at all. " \
                                     "Once Rebirth is casted, the end effect is that the " \
                                     "previously vitally harmed host will return to a perfectly healthy state.\n\n" \
                                     "This works by the mythical elemental using their own mana to pump energy " \
                                     "through the host. This essentially means that the user now has mana running " \
                                     "through their veins instead of blood, and their energy becomes more potent as " \
                                     "a result. Their magic skyrockets in power upon waking up from rebirth, as " \
                                     "well as changing the color of their fur, skin or scales (depending on the " \
                                     "race of the mythical element user) to a pure white, pitch-black sclera, and well " \
                                     "as giving their " \
                                     "eyes the color of their primary magic.\n\nThe drawbacks to this technique are " \
                                     "severe, however. By using their power to keep their user alive, the mythical " \
                                     "elemental is significantly weakened by the endeavor, causing the user to be " \
                                     "unable to call upon the force of their mythical element as strongly as they " \
                                     "could before. Because of the body's new reliance on mana, the user is also " \
                                     "extremely vulnerable to shadow attacks, as temporarily shutting off their mana " \
                                     "results in the user entering a severely weakened state similar to death."
                rebirth = input(
                    rebirthStats + "\n\n" + rebirthDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

            # Mythical Elements Exit Command
            if mythicBarrier == "back":
                mythicBarrier = "back"
                break
            if mythicBarrier == "leave":
                print("Thank you for using the Phalmasia Info Database. Have a nice day.")
                quit()

        # Energy Elevage Commands
        if magicBarrier == "energy elevage" or magicBarrier == "elevage":
            energyElevageDescription = (
                "Energy Elevage is a process that boosts the user's power output by roughly 10%, though it takes "
                "time, patience, and strength of will to complete successfully. In order to begin the process, "
                "the user must first find their core: the place where their mana comes from. It varies from "
                "person to person, but many common ones include the brain, the heart or the stomach. Once the "
                "user locates their core, they must force every drop of mana in their body into it and hold "
                "it there. This process normally takes a few minutes, and is very difficult, so many find it "
                "useful to meditate through it. The core isn't built to withstand this much mana at once, and doing this will cause "
                "it to shut itself off from the rest of your body to protect it from any forceful release of "
                "energy. As a result, this locks off the user from their magical abilities completely while "
                "the core gives itself time to adjust and heal, leaving the user physically weakened. "
                "This can take anywhere from one month to nine. During this time, the user's mana undergoes "
                "an evolution of sorts, and becomes more potent and pure.\n\nOnce the time is up, the user "
                "will be tasked with retaining this strengthened mana from their core. This is a test "
                "of mental and physical fortitude, as flooding the body with this much power can drive "
                "the user insane and even cause bodily harm. If the user can retain their mind and calm "
                "the flow of mana throughout their body, then the process is complete. Because of the "
                "year spent with no mana, the user's body will become accustomed to the new potency of "
                "the mana and begin producing mana at the new concentration from that point on.")
            energyElevage = input(
                "\033[1m" + "Energy Elevage" + "\033[0m\n\n" + energyElevageDescription + "\n\nPress 'Enter' to return to magic selection.\n").lower().strip()

        # Magic Exit Command
        if magicBarrier == "back":
            infoBarrier = "back"
            break
        if magicBarrier == "leave":
            print("Thank you for using the Phalmasia Info Database. Have a nice day.")
            quit()

    # Races Input Commands
    while infoBarrier == "races":
        raceBarrier = input("Besides humans, there are four different races that inhabit Phalmasia: Terrians, Argens, "
                            "Avats, and Majuu. Each of them primarily inhabit one continent of Phalmasia, "
                            "and have different ways of life, as well as unique characteristics and magic options. It "
                            "is possible for some of these races to learn magic that isn't in their common subset, "
                            "but it is very uncommon. Humans, unfortunately, cannot learn magic. \n\nRaces:\n| "
                            "Terrians\n| Argens\n| Avats\n| Majuu\n\nLeave the database by entering 'Leave'. Go back "
                            "to the home prompt by entering 'Back'.\n").lower().strip()

        while raceBarrier == "":
            raceBarrier = input("Please Re-enter your database restriction.\n").lower().strip()
        while raceBarrier != "terrians" and raceBarrier != "terrian" and raceBarrier != "argens" and raceBarrier != "argen" and raceBarrier != "avats" and raceBarrier != "avat" and raceBarrier != "majuu" and raceBarrier != "back" and raceBarrier != "leave":
            raceBarrier = input("Please Re-enter your database restriction.\n").lower().strip()

        # Terrian Commands
        if raceBarrier == "terrians" or raceBarrier == "terrian":
            terrianRace = input(
                "\033[1m" + "Terrians" + "\033[0m\n\nRace Ability: Increased stamina. \n\nCommon Magic Affinities: Fire, Water, "
                                         "Earth, Lightning, Wind, "
                                         "Ice\nNative Continent: Halgeis\n\nA peaceful race that highly populates the Halgeis "
                                         "Region. Many terrians work as farmers, and have a long standing relationship with "
                                         "other races. They can be found living almost everywhere and can easily adapt to new "
                                         "environments. They originally built the city of Grand Elise as a way to bring all "
                                         "races together to live in harmony and peace, and established the Divina Royal Family "
                                         "that ruled for many generations.\n\nIt is said that the terrians evolved from their "
                                         "domesticated ancestors during the old age of the world's birth, taking on forms to "
                                         "better serve the one place they call home. Terrians are very diverse and come in all "
                                         "shapes and sizes.\n\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Argen Commands
        if raceBarrier == "argens" or raceBarrier == "argen":
            argenRace = input(
                "\033[1m" + "Argens" + "\033[0m\n\nRace Ability: Magic Proficiency & Scales slightly resist "
                                       "Magic-Based Attacks\n\nCommon Magic "
                                       "Affinities: Fire, Lightning, Earth\nNative Continent: Mu'karr\n\nA highly intelligent "
                                       "and curious race, argens populate the mountainous, forest-covered region of Mu'karr. "
                                       "Very in tune with nature and mana, they are people who have a strong thirst for "
                                       "knowledge, many becoming researchers or professors in school. Their lifestyle is "
                                       "simple and homely, many preferring to stay in Mu'karr as the climate fits perfectly "
                                       "for their preferred environment high in the mountains.\n\nArgens were the first of the "
                                       "new races to appear after terrians, when humans discovered and explored Mu'karr. They "
                                       "come in a variety of colors and patterns. They are also the only race capable of "
                                       "having an affinity for gravity magic.\n\nPress 'Enter' to return to race "
                                       "selection.\n").lower().strip()

        # Avat Commands
        if raceBarrier == "avats" or raceBarrier == "avat":
            avatRace = input(
                "\033[1m" + "Avats" + "\033[0m\n\nRace Ability: Magic Proficiency & Increased speed\n\nCommon Magic Affinities: "
                                      "Wind, Lightning, Ice, Water\nNative Continent: Altaria\n\nAnother intelligent race, "
                                      "avats are theorists, and have just as much as a thirst for knowledge as argens do. They "
                                      "are highly respected philosophers. Along with other researchers, avats study the "
                                      "mysterious history of the world and the development and knowledge behind how magic is "
                                      "used, taking a careful look into each element. They've written many books on the "
                                      "subject, and are highly skilled in the use of magic due to their extensive "
                                      "knowledge.\n\nPress 'Enter' to return to race selection.\n").lower().strip()

        # Majuu Commands
        if raceBarrier == "majuu":
            majuuRace = input(
                "\033[1m" + "Majuu" + "\033[0m\n\nRace Ability: Increased resistance to physical attacks\n\nCommon Magic "
                                      "Affinities: Earth, Fire\nNative Continent: Xhia\n\nA race of large goat/bull like "
                                      "beasts that grow to a maximum of 9 to 10 feet tall, and originate from Xhia. Because "
                                      "of the Arduos War, the majuu people were divided amongst themselves, some living in a "
                                      "higher society away from the others who live on the outskirts. The war they started "
                                      "ran they friendly and kind reputation into the ground. Though most majuu are gentle "
                                      "giants, some are hostile due to their trust issues. Some even move to Halgeis in hopes "
                                      "of giving a better life for their families, though the prejudice proves to make that "
                                      "difficult.\n\nThe color of a majuu's fur is dependent on their climate. Bright colored "
                                      "majuu are from warmer areas, while darker colored majuu are from colder areas. They "
                                      "are also known to be very skilled blacksmiths, and have created many fearsome weapons "
                                      "and tools in the past. Majuu are the longest living species on Phalmasia, averaging a "
                                      "lifespan of 200 years.\n\nPress 'Enter' to return to race selection.\n").lower().strip()

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
                          "Xaeyz and Mirago merged their beasts to create something entirely new: a Dragonic Phoenix. " \
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
