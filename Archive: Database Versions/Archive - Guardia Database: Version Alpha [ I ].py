# To-Do List
# Change Test Release Volume per release cycle in introduction

# Tester Introduction
input(
    "IF YOU HAVE READ THIS PREVIOUSLY: Press enter 8 times to skip by this prompt and head to the beginning of the official code. Thanks!\n\nHey! If you are reading this, then you are here to test my code. Thanks for agreeing to do this by the way; error checking by someone else's eyes is a huge help.\n\nOh, and to continue after you are finished reading anything without a prompt, just press ENTER. Try it here!")
input(
    "Nice! By the way, I've set up the code in a way where if you press enter where the computer would look for an input from you, it should tell you that it's looking for an input. Just be sure to type an appropriate prompt in and the code will keep running as normal (I've tried to make the code as forgiving to as many forms of the input as I could. Hopefully that helps.).")
input(
    "This is more a warning than anything else. The code may sometimes stop working and display red text in the output area of this code. This, however, is an intended output, and I've left a message there so you know.")
input(
    "Anything that you change on this code cannot affect the final project, so if you do choose to delete anything or change the code in a way you can't rectify, simply reload the page or reopen the link I sent you to get back to the original version.")
input(
    "If you do find a place where the code stops working as intended or grammar or something is off, take a note of it. If the code breaks and leaves you stuck on the screen, press the green button directly under the RUN button titled RESET. This will reset the code and make it usable again.")
input(
    "Sometimes, this compiler breaks the code for no reason, and no matter what you enter the code will not progress and tell you that your input is incorrect despite it being fine. This error is, unfortunately, out of my control.\n\nIf this ever happens while you test, reload the page and the issue should fix itself. Sorry for the inconvienience.")
input(
    "Finally, this is a database of characters, events, storylines and powers for which I have conceptualized based off of a webcomic I read. This entire thing is an AU passion project (and to be honest, quite embarrasing to be shared at all).\n\nWhat I'm saying is, please don't judge the work based on the idea, and don't share the link for this code to anyone without my permission.")
input("Thanks again for wanting to test this, and welcome to my world.")

# Introduction
input("Version Release - ALPHA\n\nGuardia: Tales of Halgeis Info Database")
input("Please use the interface to select information.")
infoBarrier1 = input(
    "Current Implemented Options: Characters\n\nChapters:\n| Characters\n| Locations\n| Magics\n\nLeave the database by entering 'Leave'.")

# InfoBarrier1 Check
while infoBarrier1 == (""):
    infoBarrier1 = input(
        "Please Re-enter your database restriction. Current Implemented Options: Characters\n\nChapters:\n| Characters\n| Locations\n| Magics\n\nLeave the database by entering 'Leave'.")
while (
        infoBarrier1 != "Characters" and infoBarrier1 != "characters" and infoBarrier1 != "Locations" and infoBarrier1 != "locations" and infoBarrier1 != "Magics" and infoBarrier1 != "magics" and infoBarrier1 != "Leave" and infoBarrier1 != "leave"):
    infoBarrier1 = input(
        "Please Re-enter your database restriction. Current Implemented Options: Characters\n\nChapters:\n| Characters\n| Locations\n| Magics\n\nLeave the database by entering 'Leave'.")

# Character Input Lists
if (infoBarrier1 == "Characters" or infoBarrier1 == "characters"):
    infoBarrier2 = input(
        "Current Implemented Options: Xaeyz Kai, Yggdra Aensyll\n\nCharacters:\n| Xaeyz Kai\n| Yggdrasil Aensyll\n| Cidelli Reimora\n| Mimi\n| Kimiko Quintai\n| Aeiyou Dreanew\n| Kinto Genjudo\n| Amiru Soaren\n| Turcobé Sentai\n| Yumeizu Artilux\n| Mirago Fynae\n\nLeave the database by entering 'Leave'.")

    while infoBarrier2 == (""):
        infoBarrier2 = input(
            "Please Re-enter your database restriction.\n\nCharacters:\n| Xaeyz Kai\n| Yggdrasil Aensyll\n| Cidelli Reimora\n| Mimi\n| Kimiko\n| Aeiyou\n| Kinto\n| Amiru\n| Turcobé\n| Yumeizu\n| Mirago Fynae")
    while (
            infoBarrier2 != "Xaeyz Kai" and infoBarrier2 != "Xaeyz" and infoBarrier2 != "xaeyz kai" and infoBarrier2 != "xaeyz" and infoBarrier2 != "Yggdrasil Aensyll" and infoBarrier2 != "Yggdra" and infoBarrier2 != "yggdrasil aensyll" and infoBarrier2 != "yggdra" and infoBarrier2 != "Yggdrasil" and infoBarrier2 != "yggdrasil" and infoBarrier2 != "Cidelli Reimora" and infoBarrier2 != "Cid" and infoBarrier2 != "cidelli reimora" and infoBarrier2 != "cid" and infoBarrier2 != "Cidelli" and infoBarrier2 != "cidelli" and infoBarrier2 != "Mimi" and infoBarrier2 != "mimi" and infoBarrier2 != "Kimiko Quintai" and infoBarrier2 != "Kimiko" and infoBarrier2 != "kimiko quintai" and infoBarrier2 != "kimiko" and infoBarrier2 != "Aeiyou Dreanew" and infoBarrier2 != "Aeiyou" and infoBarrier2 != "aeiyou dreanew" and infoBarrier2 != "aeiyou" and infoBarrier2 != "Kinto Genjudo" and infoBarrier2 != "Kinto" and infoBarrier2 != "kinto genjudo" and infoBarrier2 != "kinto" and infoBarrier2 != "Amiru Soaren" and infoBarrier2 != "Amiru" and infoBarrier2 != "amiru soaren" and infoBarrier2 != "amiru" and infoBarrier2 != "Turcobe Sentai" and infoBarrier2 != "Turcobe" and infoBarrier2 != "turcobe sentai" and infoBarrier2 != "turcobe" and infoBarrier2 != "Turcobé Sentai" and infoBarrier2 != "Turcobé" and infoBarrier2 != "turcobé sentai" and infoBarrier2 != "turcobé" and infoBarrier2 != "Yumeizu Artilux" and infoBarrier2 != "Yumeizu" and infoBarrier2 != "yumeizu artilux" and infoBarrier2 != "yumeizu" and infoBarrier2 != "Mirago Fynae" and infoBarrier2 != "Mirago" and infoBarrier2 != "mirago fynae" and infoBarrier2 != "mirago" and infoBarrier2 != "Leave" and infoBarrier2 != "leave"):
        infoBarrier2 = input(
            "Please Re-enter your database restriction.\n\nCharacters:\n| Xaeyz Kai\n| Yggdrasil Aensyll\n| Cidelli Reimora\n| Mimi\n| Kimiko\n| Aeiyou\n| Kinto\n| Amiru\n| Turcobé\n| Yumeizu\n| Mirago Fynae")

    # Xaeyz Kai Bio
    if (
            infoBarrier2 == "Xaeyz Kai" or infoBarrier2 == "Xaeyz" or infoBarrier2 == "xaeyz kai" or infoBarrier2 == "xaeyz"):
        # Xaeyz Bio Prompts
        xaeyzProfile = "Xaeyz Kai\n\nHometown: Meteora\nRace: Argen (Black, Gray)\nBirthday: July 7th, 4023\nMagic Affinities\n| Wind\n| Gravity\n| Cosmic Wind\n\nItems\n| Aurora Staff\n| eMap\n| SoundCube\n| Gale Shard\n| PockUnity Orb\n\n| Wind Spells | Gravity Spells | Cosmic Wind | Backstory | Leave |"
        xaeyzProfilePrompt = "Xaeyz Kai\n\nHometown: Meteora\nRace: Argen (Black, Gray)\nBirthday: July 7th, 4023\nMagic Affinities\n| Wind\n| Gravity\n| Cosmic Wind\n\nItems\n| Aurora Staff\n| eMap\n| SoundCube\n| Gale Shard\n| PockUnity Orb\n| Psychal Library\n\nPlease select an option below\n| Wind Spells | Gravity Spells | Cosmic Wind | Backstory | Leave |"
        xaeyzWindSpells = "Xaeyz Kai\n\nSpells: Wind\n| Cyclone Slice\n| Gale Vaccuum\n| Aurora Scythe\n| Rising Wyrmwind\n* Rising Wyrmwind: Zephyr Flurry\n| Zephyr's Eye\n| Phoenix\n| Phoenix Hybrid\n* Phoenix Hybrid: Feather Control\n* Phoenix Hybrid: Feather Dance\n* Phoenix Hybrid: Gale Drive\n| Phoenix Ethereal\n* Phoenix Ethereal: Feather Control\n* Phoenix Ethereal: Feather Dance\n* Phoenix Ethereal: Gale Drive\n* Phoenix Ethereal: Zephyr's Eye\n* Phoenix Ethereal: Zephyr's Wrath\n\n| Profile | Gravity Spells | Cosmic Wind | Backstory | Leave |"
        xaeyzGravitySpells = "Xaeyz Kai\n\nSpells: Gravity\n| Levitation\n* Shift\n| Field\n| Quake\n| Lock\n\n| Profile | Wind Spells | Cosmic Wind | Backstory | Leave |"
        xaeyzCosmicWindSpells = "Xaeyz Kai\n\nSpells: Cosmic Wind\n| Stardust Enhancement\n| Aurora's Grace\n| Meteor Crash\n| Luminous Aurora\n| Cosmic Seal\n| Constellar Ray\n\nAeon: Spirit of the Stars\n| Aeon is the spirit of Cosmic Wind, and the partner of Xaeyz. The only reason Xaeyz can use Cosmic Wind at all is because Aeon is with him. Similar to the other spirits of the mythical elementals, Aeon has no physical form and exists only in Xaeyz's psychal library. This, as a result, gives Xaeyz two active consciences. Aeon is a free soul and lives on trying to keep everyone around him safe while being as free as possible; values similar to Xaeyz's.\n\nFriends: Yes\nAcceptance: Yes\nMagic Use: Permitted\n\n| Profile | Wind Spells | Gravity Spells | Backstory | Leave |"

        # Xaeyz Backstory Prompts
        # Chapter 1
        xaeyzBackstory01 = "Chapter 01\n\nXaeyz was born with wind magic, an oddity for Argens. As a result, no one could teach him, and was made fun of often. He did not let this stop him, however, and dropped out of school to train himself at age five. During his training, Xaeyz met another young argen named Mirago, who also dropped out of school due to a hatred of magic. Xaeyz helps Mirago overcome this hatred, and they train together for the next two years, dreaming of applying to St. Guardias and becoming guardians."
        xaeyzBackstory02 = "In 4030, a great black meteor that the world came to know as the Black Sun, came crashing down on Meteora. Mirago, being the Onyx Fire User, helps Xaeyz to try to slow it down, though the many strong magic users of the village could not. Their power is not enough to stop the catastrophe. Suddenly, Xaeyz gains a new power, the affinity for Cosmic Wind, and with this power and Mirago's Onyx Fire, the meteor was stopped."
        xaeyzBackstory03 = "However, when fighting this interstellar threat, they discovered something incredible: the meteor was absorbing their magic. No other metal or rock on Phalmasia had the ability, so it was certainly unique. Unfortunately, this victory and information came with a great cost. Mirago had nearly exhausted his mana trying to stop the meteor, and collapsed. Mirago understood the power this meteor had, and realized what could happen if it fell into the wrong hands."
        xaeyzBackstory04 = "Using what was left of his mana, he used Xaeyz's new wind and his own to build a Divine Spell; one that would seal out any magic but the ones that made up the seal. Though it would be weak, it would be enough to protect the meteor from those that would abuse its power. Mirago and Xaeyz were the only ones who knew about the properties of the meteor, so to keep the power safe, they mutually decided to keep the secret safe. This promise ended up being Mirago's final words."
        xaeyzBackstory05 = "However, this was not the end of Xaeyz's problems. A lightning bolt hit Xaeyz in the back, and a fireball in the side. The villagers of Meteora were attacking him. They were scared of him. Who wouldn't be, after a seven-year-old boy stopped a threat the entire village's best couldn't stand a chance against? But Xaeyz didn't understand. He and Mirago had saved the lives of everyone. Why were they attacking him?"
        xaeyzBackstory06 = "He used his magic to defend himself and Mirago's body, but he was fighting an losing battle. He refused to fight back. He couldn't hurt his fellow argens; his family. So he merely defended. He couldn't last forever, though, and soon he was overwhelmed by the force of the townspeople. Then someone (something?) whispered to him. It told him not to fight the villagers. That he needed to get away to the place where he met Mirago. And so Xaeyz grabbed Mirago and took off into Duskfaze Forest."
        xaeyzBackstory07 = "Xaeyz didn't know why he was listening to this ominous voice. But he does know who was talking to him: the cosmic wind. Whatever this new power was, it was sentient. But he trusted it, and he had to keep going to the place he met his best friend: Aurora Grotto. It was his and Mirago's favorite place. Xaeyz knew that Mirago had a favorite tree in the grotto; it was the biggest one in the field, at the very center of an island in a small lake. Under this flowering tree, Xaeyz gave Mirago his final resting place."
        # Chapter 2
        xaeyzBackstory08 = "Chapter 02\n\nXaeyz spent the next few days mourning his friend's loss, but knew he still had more work to do: he had to seal the meteor's powers away as soon as possible. He couldn't do it himself; the only way to condense the meteor into a smaller object without cutting any of it off was with earth magic, and a lot of experience with weapon forging. Xaeyz knew someone who could do the job in Meteora: his grandfather, the town's blacksmith."
        xaeyzBackstory09 = "The next day, Xaeyz snuck back into Meteora to see his grandfather, Armedies. When he found him in his workshop, he explained everything about what really happened and what needed to be done. Xaeyz apologized after he was done for coming in the first place, and started to leave in case his grandfather was scared of him like the rest of the town. Armedies, however, stops him and says he's willing to help him."
        xaeyzBackstory10 = "Armedies also mentions that the village was oblivious to the help, and power, of Mirago. This was a great relief to Xaeyz because he figured that if there was a spell to render magic useless on an opject, then there might be one to steal magic from others, too. If anyone would be able to steal Mirago's powerful magic, it wouldn't be good. Xaeyz decided to keep Mirago and the existance of Aurora Grotto secret to anyone else."
        xaeyzBackstory11 = "Getting the meteor was the easy part: Armedies was supposed to remove it that day so he could use it for a fuel source in his shop. Now, Xaeyz explained his designs for the meteor: a staff. Xaeyz wanted to turn the whole meteor into a staff that had built-in wings so he wouldn't need a glider. He also wanted to add a storage compartment somewhere that would require an input of magic to open."
        xaeyzBackstory12 = "His grandfather condensed the entirity of the meteor into a staff, which ended up, for some reason, to be no heavier than an ordinary wooden one. He added the wings and a storage compartment to the staff. Once it was finished, Xaeyz needed to add the most important part. He took out the Divine Rune and cast the spell on the staff. But something unexpected happened. The spell summoned a blinding light that engulfed the workshop, and alerted everyone outside."
        xaeyzBackstory13 = "Knowing people would come inside to check if everything is alright, his grandfather told him to go back to his house and talk to his parents one last time before running off. Xaeyz grabbed his new staff, now branded with the Divine Mark of the Phoenix (the symbol created when the divine spell was cast with fire and wind magic), and ran to his old home. When he got there, his parents were waiting for him."
        xaeyzBackstory14 = "They embraced him, explaining that they were not afraid, and gave him some money, a black cloak with a hood, and a goodbye. Xaeyz blasted off back into the forest where he lived in Aurora Grotto for another week, surviving off of the fruit trees surrounding the grotto. It was rough and scary for him since he had never lived on his own before. Why would he; he was only seven after all. But much worse was to come; another tragedy."
        xaeyzBackstory15 = "The next week, Xaeyz heard yelling coming from the direction of Metera, so he hopped into the trees and went to check it out. What he found horrified him. His mom, dad, and grandfather were on the ground in a field, beaten, shocked, and burned. They were shouting at them, asking where Xaeyz had gone. They did not say a word. They weren't going to give up family to an angry mob. For this secrecy, the townspeople gathered their magic and killed all three while Xaeyz watched."
        xaeyzBackstory16 = "Xaeyz eyes widened. Tears streamed down his face as he looked at the burned corpses of his family. And he lost control. He crashed down into the field with cosmic wind rushing out of him. His eyes were aglow with this power, and the sight brought fear to the townspeople. Xaeyz screamed in anger at his former friends. Throughts raced through his head, and all he could do was scream. His magic was more relentless and powerful than it had ever been, and it sent everyone flying backwards."
        xaeyzBackstory17 = "Xaeyz finally came to his senses and the cosmic wind died down. He looked back at the people of his former home cower and beg for forgiveness. All Xaeyz did was whisper an apology and rush away before he could get so much as a response. He ran farther than he ever had before, miles and miles farther away from Meteora than he had ever been. He kept going until he had gotten somewhere new: the Enchanted Forest of Grand Elise, the center of Halgeis."
        # Chapter 3
        xaeyzBackstory18 = "Chapter 03\n\nHere Xaeyz found a home in a tree he called the Heaven Tree. A wolf, sheep and crow had been living together in the tree before he had arrived, and he befriended them. In remembrance of his best friend, he named the wolf Mirago, and trained here for the remainder of our story. Xaeyz was going to train hard to become a guardian. He had a mission to carry on his friend's dream; and to make sure no one hurt the way he did."
        xaeyzBackstory19 = "Two years afterward, a fire was burning in the Tree of Souls at the very center of the forest. Xaeyz had grown very used to living in the wild and loved the forest, so he had to do something about it. Wind magic was notorious against fire, however. Water or earth users were most effective wih dealing with natural flames since wind usually just spread them. But now was Xaeyz's time to show off the results of his two years of training, and rushed to the tree."
        xaeyzBackstory20 = "Putting up his hood, jumping above the trees with a magic gust and grabbing his Aurora Staff from his back, Xaeyz launched himself high above the tree. Xaeyz then spun his staff rapidly and launched magic out of it. The result was his first wind spell: Gale Vaccuum. This spell, unlike other wind spells, created an absense of air in its radius; a makeshift vaccuum. Since fire relies and feeds on air, the flames went out quickly after being engulfed by the attack. Xaeyz had gotten stronger."
        xaeyzBackstory21 = "Xaeyz had been keeping tabs on a town nearby the Enchanted Forest called Drəklife since he had arrived. There, he learned of the name the argens from Meteora began to call him: 'The Boy of Cosmic Wind'. He preferred the Cosmic Wind User; a boy sounded less cool to him. He was also known as 'The Forest's Shadow' since he had stopped the forest fire. However, two years after the fire, Xaeyz encountered his final challenge: a fire user attaking the town."
        # Chapter 4
        xaeyzBackstory22 = "Chapter04\n\nThe avian attacking was known as Hozura the Flame, a man who was being hunted by the guardians for about 3 weeks. He wasn't particularly strong, but was extremely smart and always attacked places without guardians and places that were far away from them. Xaeyz put on his cloak and jumped into the town to protect the townspeople and try to stop Hozura. Hozura had gathered all the townspeople together and had a magic attack poised at them. He fired when they didn't give him access to the bank."
        xaeyzBackstory23 = "Xaeyz landed in front of them and used his own wind magic to stop the flames from hurting anyone. This upset Hozura, and he drew his sword, threatening to kill him if he kept getting in his way. The townspeople began to murmur behind him about being in the presence of the Forest's Shadow as Xaeyz took out his staff. The battle began. Hozura and Xaeyz clashed with their weapons for several minutes, and Xaeyz was on par with him despite being much younger than him."
        xaeyzBackstory24 = "Xaeyz asked him during their fight why Hozura was doing this, and he responded by throwing a fireball at his head. Xaeyz promptl dodged and swung with his staff, landing a clean blow. Xaeyz gathered magic in his lungs and blew a blast of air at Hozura, pushing him backwards. However, Hozura had a plan of his own. He had concentrated magic beneath Xaeyz and began to trigger it. Xaeyz noticed and hopped out of the way just before the ground below him exploded."
        xaeyzBackstory25 = "Hozura used an explosion beneath himself to get up to Xaeyz and swung his sword, throwing three fireballs along the arc of his swing. Xaeyz channelled mana into his staff and knocked them both away, all the while keeping damage to Drəklife as minimal as he could. Xaeyz threw slashes of wind at Hozura while parrying fireballs and explosions from Hozura. After a while of fighting him, he knew that this couldn't continue."
        xaeyzBackstory26 = "Xaeyz needed to leave before the guardians got here, which means he needed to defeat Hozura before he left. Xaeyz needed to trap him, and Xaeyz had just the thing to do it. Xaeyz opened up the bottom of his glider on the staff and swung, releasing a wave of intense wind at Hozura, which he couldn't counter and sent him flying backwards. Xaeyz then inhaled and blew another gust at him, pinning him to the ground. Finally, he poised for his final blow."
        xaeyzBackstory27 = "Xaeyz channelled as much mana as he could spare into his staff and let loose with a blast of air from his staff. The amount of air that Hozura was dealin with caused so much pressure, the ground beneath him began to crack and he passed out. As Xaeyz slowl floated to the ground, he knew that he had won. Xaeyz checked the town: barely any damage besides the cracks in the ground and a few buildings that were scorched. Not bad for his first actual battle."
        xaeyzBackstory28 = "Xaeyz rushed back to the towns people to make sure they were ok. When he told them that Hozura had been knocked out, they celebrated. Xaeyz had Hozura cuffed and restrained so he couldn't move until the guardians got here. Xaeyz had also gained Hozura's bounty. In order to claim it, he had to stay afterwards and show his face to the guardians, which were two things he couldn't do. So he gave a note to the mayor that gave the bounty back to the town for repairs as a gift before leaving Drəklife once again."
        xaeyzBackstory29 = "Xaeyz had defeated his first villain at age 11. For the next three years, Xaeyz trained as hard as he could.\n\nAfter those three years, he took the entry exam to St. Guardias, and at age 14, he passed, and the rest is history..."

        # Xaeyz Bio Search Commands
        xaeyzShift = input(xaeyzProfile)
        xaeyzStore = xaeyzProfile

        while xaeyzShift == (""):
            xaeyzShift = input(xaeyzProfilePrompt)
        while (xaeyzShift != "Leave" and xaeyzShift != "leave"):
            if (xaeyzShift == "Profile" or xaeyzShift == "profile"):
                xaeyzStore = xaeyzProfile
                xaeyzShift = input(xaeyzProfile)
            if (
                    xaeyzShift == "Wind Spells" or xaeyzShift == "Wind spells" or xaeyzShift == "wind Spells" or xaeyzShift == "wind spells"):
                xaeyzStore = xaeyzWindSpells
                xaeyzShift = input(xaeyzWindSpells)
            if (
                    xaeyzShift == "Gravity Spells" or xaeyzShift == "Gravity spells" or xaeyzShift == "gravity Spells" or xaeyzShift == "gravity spells"):
                xaeyzStore = xaeyzGravitySpells
                xaeyzShift = input(xaeyzGravitySpells)
            if (
                    xaeyzShift == "Cosmic Wind" or xaeyzShift == "Cosmic wind" or xaeyzShift == "cosmic Wind" or xaeyzShift == "cosmic wind"):
                xaeyzStore = xaeyzCosmicWindSpells
                xaeyzShift = input(xaeyzCosmicWindSpells)
            if xaeyzShift == (""):
                xaeyzShift = input(
                    xaeyzStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if (
                    xaeyzShift != "Wind Spells" and xaeyzShift != "Wind spells" and xaeyzShift != "wind Spells" and xaeyzShift != "wind spells" and xaeyzShift != "Gravity Spells" and xaeyzShift != "Gravity spells" and xaeyzShift != "gravity Spells" and xaeyzShift != "gravity spells" and xaeyzShift != "Backstory" and xaeyzShift != "backstory" and xaeyzShift != "Profile" and xaeyzShift != "profile" and xaeyzShift != "Cosmic Wind" and xaeyzShift != "Cosmic wind" and xaeyzShift != "cosmic Wind" and xaeyzShift != "cosmic wind" and xaeyzShift != "Back" and xaeyzShift != "back" and xaeyzShift != "Leave" and xaeyzShift != "leave"):
                xaeyzStore = xaeyzProfilePrompt
                xaeyzShift = input(
                    xaeyzStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

            # Xaeyz Backstory System
            if (xaeyzShift == "Backstory" or xaeyzShift == "backstory"):
                xaeyzStore = "Table of Contents. Please enter the chapter you wish to view. Enter 'Back' to return to Xaeyz's Bio.\n\nChapter 1\n\nChapter 2\n\nChapter 3\n\nChapter 4"
                xaeyzShift = input(
                    "Table of Contents. Please enter the chapter you wish to view. Enter 'Back' to return to Xaeyz's Bio.\n\nChapter 1\n\nChapter 2\n\nChapter 3\n\nChapter 4")
                if xaeyzShift == (""):
                    xaeyzShift = input(
                        xaeyzStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if (
                        xaeyzShift != "Chapter 1" and xaeyzShift != "chapter 1" and xaeyzShift != "Chapter One" and xaeyzShift != "chapter one" and xaeyzShift != "Chapter 2" and xaeyzShift != "chapter 2" and xaeyzShift != "Chapter Two" and xaeyzShift != "chapter two" and xaeyzShift != "Chapter 3" and xaeyzShift != "chapter 3" and xaeyzShift != "Chapter Three" and xaeyzShift != "chapter Three" and xaeyzShift != "Chapter 4" and xaeyzShift != "chapter 4" and xaeyzShift != "Chapter Four" and xaeyzShift != "chapter four" and xaeyzShift != "Back" and xaeyzShift != "back"):
                    xaeyzShift = input(
                        xaeyzStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    quit("\nCommands entered inconsistantly. Please restart program. Sorry for the inconvienience.")
                if (xaeyzShift == "Back" or xaeyzShift == "back"):
                    input(
                        "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                    xaeyzShift = "Chapter 1 "
                    xaeyzStore = "Please Wait. . ."

                while (xaeyzShift != "Back" and xaeyzShift != "back"):
                    # Xaeyz Chapter 1 Backstory System
                    if (
                            xaeyzShift == "Chapter 1" or xaeyzShift == "chapter 1" or xaeyzShift == "Chapter One" or xaeyzShift == "chapter one"):
                        xaeyzShift = input(xaeyzBackstory01)
                        xaeyzShift = input(xaeyzBackstory02)
                        xaeyzShift = input(xaeyzBackstory03)
                        xaeyzShift = input(xaeyzBackstory04)
                        xaeyzShift = input(xaeyzBackstory05)
                        xaeyzShift = input(xaeyzBackstory06)
                        xaeyzShift = input(xaeyzBackstory07 + "\n\nEnd of Chapter 01")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        xaeyzStore = "Please Wait. . ."
                        break
                    # Xaeyz Chapter 2 Backstory System
                    if (
                            xaeyzShift == "Chapter 2" or xaeyzShift == "chapter 2" or xaeyzShift == "Chapter Two" or xaeyzShift == "chapter two"):
                        xaeyzShift = input(xaeyzBackstory08)
                        xaeyzShift = input(xaeyzBackstory09)
                        xaeyzShift = input(xaeyzBackstory10)
                        xaeyzShift = input(xaeyzBackstory11)
                        xaeyzShift = input(xaeyzBackstory12)
                        xaeyzShift = input(xaeyzBackstory13)
                        xaeyzShift = input(xaeyzBackstory14)
                        xaeyzShift = input(xaeyzBackstory15)
                        xaeyzShift = input(xaeyzBackstory16)
                        xaeyzShift = input(xaeyzBackstory17 + "\n\nEnd of Chapter 02")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        xaeyzStore = "Please Wait. . ."
                        break
                    # Xaeyz Chapter 3 Backstory System
                    if (
                            xaeyzShift == "Chapter 3" or xaeyzShift == "chapter 3" or xaeyzShift == "Chapter Three" or xaeyzShift == "chapter three"):
                        xaeyzShift = input(xaeyzBackstory18)
                        xaeyzShift = input(xaeyzBackstory19)
                        xaeyzShift = input(xaeyzBackstory20)
                        xaeyzShift = input(xaeyzBackstory21 + "\n\nEnd of Chapter 03")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        xaeyzStore = "Please Wait. . ."
                        break
                    # Xaeyz Chapter 4 Backstory System
                    if (
                            xaeyzShift == "Chapter 4" or xaeyzShift == "chapter 4" or xaeyzShift == "Chapter Four" or xaeyzShift == "chapter four"):
                        xaeyzShift = input(xaeyzBackstory22)
                        xaeyzShift = input(xaeyzBackstory23)
                        xaeyzShift = input(xaeyzBackstory24)
                        xaeyzShift = input(xaeyzBackstory25)
                        xaeyzShift = input(xaeyzBackstory26)
                        xaeyzShift = input(xaeyzBackstory27)
                        xaeyzShift = input(xaeyzBackstory28)
                        xaeyzShift = input(xaeyzBackstory29 + "\n\nEnd of Chapter 04")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        xaeyzStore = "Please Wait. . ."
                        break
                    else:
                        input("Please Wait. . .")
                        break

        # Xaeyz Exit Command
        input("Database Search Completed. Please restart program to search again.")
        quit("\nProgram Completed Successfully. This is not an error.")

    # Yggdra Bio Search Commands
    if (
            infoBarrier2 == "Yggdrasil Aensyll" or infoBarrier2 == "Yggdra" or infoBarrier2 == "yggdrasil aensyll" or infoBarrier2 == "yggdra" or infoBarrier2 == "Yggdrasil" or infoBarrier2 == "yggdrasil"):
        # Yggdra Bio Prompts
        yggdraProfile = "Yggdrasil (Yggdra) Aensyll\n\nHometown: Ashford\nRace: Terrian (Fox)\nBirthday: December 17, 4023\nMagic Affinities\n| Wind\n\nItems\n| Gale Shard\n| PockUnity Orb\n\n| Wind Spells | Backstory | Leave |"
        yggdraProfilePrompt = "Yggdrasil (Yggdra) Aensyll\n\nHometown: Ashford\nRace: Terrian (Fox)\nBirthday: December 17, 4023\nMagic Affinities\n| Wind\n\nItems\n| Gale Shard\n| PockUnity Orb\n\nPlease select an option below\n| Wind Spells | Backstory | Leave |"
        yggdraWindSpells = "Yggdrasil (Yggdra) Aensyll\n\nSpells: Wind\n| Gale Impact\n| Cutting Spiral\n| Pact: Zephyr\n* Zephyr: Shield\n* Zephyr: Barrier\n* Zephyr: Reflection\n* Zephyr: Tag-Team\n| Breeze Gems\n* Breeze Gems: Darts\n* Breeze Gems: Ring\n* Breeze Gems: Emblem\n\nZephyr: Sprite Pact\n| Zephyr is a sprite pact formed from her dead brother's (Frinrir) remaining mana and will. As her pact, Zephyr takes the form of a shield, symbolizing the will to protect Yggdra. He also takes his sprite form to assist Yggdra in casting unique spells. The bond that Yggdra and Zephyr share is deep, and that bond is what makes their duo so strong.\n\n| Profile | Backstory | Leave |"

        # Yggdra Backstory Prompts
        # Chapter 1
        yggdraBackstory01 = "Chapter 01\n\nYggdra had always been fascinated by magic. Her mother waas once a guardian who had retired to live a more quiet and peaceful life. Frinrir, her older brother and who Yggdra called Frinny, was finishing up his final year at St. Guardia's Academy. Frinrir was Yggdra's idol. He was the main reason she was so excited to find out if she had magic. On her fifth birthday, she unlocked her magic and discovered her affinity for wind, just like her brother."
        yggdraBackstory02 = "She was ecstatic, and wanted to show her brother when he came home a few days later. She was too eager about using her magic, however. She had just unlocked it; her control wasn't near average yet. Despite this, one day she practiced near a neighbor's house and her mana lost control and broke their window. When Yggdra's mom found out about it, she forbade her use of magic for a month, which means she wouldn't be able to show Frinrir her new magic."
        yggdraBackstory03 = "Yggdra begged for her to rescind the ban, but her mother wouldn't budge. She had plenty of schoolwork to catch up on, so practicing her magic wasn't the most efficient use of her time, either. But of course this meant nothing to a five year old girl with new magical abilities. The very next day, Yggdra left the house telling her mom that she was going to study with her friend Kiyo. However, what she was really doing was meeting up with Kiyo to practice some more of her magic."
        yggdraBackstory04 = "Kiyo didn't understand why she was still using her magic even when her mom told her it wasn't allowed, and Yggdra said that it was because magic waits for no one. She only wanted to get better at magic as fast as possible, and the first step to doing that was using lightfoot spells. Lightfoot spells were hard for beginners, and especially difficult for beginners who didn't have teachers guiding them through it. But after an argument with Kiyo saying she should stop and stomping the floor, Yggdra had accidentally figured it out."
        yggdraBackstory05 = "Kiyo knew where this was going as soon as Yggdra fell over from the force of her spell, and told her not to do anything drastic. But Yggdra was past that. She gathered all the mana she could into her feet and jumped. The jump launched her a hundred feet in the air, and the sight was unlike anything she had ever seen before. She could see the above the trees of the forest a mile away from her, the town a few miles behind her house, and a great, clear view of the sky. She was awestruck."
        yggdraBackstory06 = "But what she didn't expect to see was smoke billowing out of Kytegrove Forest. Something was clearly wrong; Yggdra could feel it, and she knew she had to tell someone. But she had a bigger problem on her hands: she was falling out of the sky. Thankfully, Kiyo was there to catch her before she hit the ground. Yggdra explained frantically to Kiyo what she saw, and they both returned to Yggdra's house  to tell the one person they knew could do something: Frinrir."
        yggdraBackstory07 = "When they got to the house, a girl was in the living room with Yggdra's parents and Frinrir. The girl's name was Alexis, and was apparently Frinrir's friend from Guardia's and his assigned partner. Yggdra told Frinrir what she saw (and brushed off her mom when she asked how she knew), but it turns out Alexis was here to take him to go and investigate it. Frinrir was going to leave again, and he'd just come home. She hadn't even shown him her new magic yet."
        yggdraBackstory08 = "Yggdra then turned to Alexis and asked her why she had to take him away. Alexis apologised and promised to get him back as soon as possible. Yggdra didn't want him to go, but Frinrir told her it was just a quick job. He'd come home after a few hours and after that, she could show him her new magic. This put Yggdra at ease, and Frinrir and Alexis took off towards Kytegrove Forest. Yggdra waited for a while with Kiyo and played tag for a bit. That's when she felt something horribly wrong."
        # Chapter 2
        yggdraBackstory09 = "Chapter 02\n\nYggdra and Kiyo were outside throwing a ball around in Yggdra's yard when she got the feeling. A burning feeling of dread and pain washed over her, and she was paralyzed in place. Something was wrong with Frinrir. She could feel it. At this point, Kiyo had noticed Yggdra's paralysis and was frantically trying to bring her back. Seconds later, Yggdra awoke, told Kiyo what she felt and where she was going, and ran off towards the forest to Frinrir."
        yggdraBackstory10 = "When Yggdra finally reached the forest, she ran through the trees to where she was being led by her vision. There, leaning on a tree, exhausted, lay Frinrir with a hole blasted in his chest. Yggdra froze as tears began to stream down her face. By this point, Frinrir noticed Yggdra's presence, and his eyes widened. He begged Yggdra weakly to get out of here, and that it was dangerous to stay here. Yggdra couldn't hear him though; all she could ask was how she could help him."
        yggdraBackstory11 = "This continued for about a minute until Alexis was blasted by her and landed hard against the tree, knocking her out. This was the thing that finally got Yggdra's attention, and she began to turn around in fear, and looked at whatever was attacking her brother. What she saw didn't stick with her, but what she felt did: a cold, fierce, murderous, uncontrollable force was looming over her. This feeling is what Yggdra would remember and how she would shape the monterous feeling."
        yggdraBackstory12 = "The thing poised for attack, reaching its hand out to grab Yggdra's head. Yggdra didn't move; she couldn't move. She was petrified by the thing's aura and bloodlust. She accepted the fact, then and there, that she was going to die. Just then, she felt a hand on her shoulder, and the thing went flying backwards. Yggdra looked up to see Frinrir standing arm outstretched with magic eminating from his hand. He created a ball of magic and threw it at a stone that the attacker had dropped, shattering it."
        yggdraBackstory13 = "Just as suddenly as he stood up, he fell to the ground. Yggdra lifted him up, begging for him to be ok, but he only managed to say one thing: 'As long as you are alive, I'll be there to protect you. So don't worry.'. After saying this, the light left his eyes, and his body went limp. Within a week of him being a guardian, Frinrir lost his life. Yggdra lost all emotion in that moment. She couldn't move and sat still, tears streaming from her eyes, staring at her brother."
        # Chapter 3
        yggdraBackstory14 = "Chapter 03\n\nAlexis woke up a few hours later and saw Yggdra and Frinrir. Of course, she was crushed by the news, but as a guardian and friend of Frinrir's, her job was to protect Yggdra. But when she reached out to her to ask her to follow her out of the forest, Yggdra swatted her hand away. She turned toward Alexis slowly and showed her her lightless eyes before getting up and walking back to her house. Alexis couldn't do anything but follow her."
        yddgraBackstory15 = "Kiyo was waiting back at Yggdra's house with her mom for Yggdra to come back. Of course, when Mrs. Aensyll found out about Yggdra using her magic, she was angry. But all of that fizzled out the minute Yggdra stepped into the door. She didn't say a word, looked down at the floor, and walked past everyone to her room upstairs. No one understood until a bit later when Alexis came in the door and dropped the news. Yggdra's parents were crushed, and Kiyo ran up to Yggdra's room to talk. Her door was already locked."
        yggdraBackstory16 = "Kiyo knocked on the door, asking Yggdra to open the door and that he only wanted to talk. She murmured something that Kiyo couldn't hear. When he asked again, a thundering voice that could only be the result of Yggdra enhancing her volume with wind magic screamed 'NO!' shook the entire house. Kiyo faltered backwards a bit, said that he could talk anytime she wanted and to let him know, and went home heavy hearted from the encounter. Yggdra didn't speak to anyone for quite a while after that."
        yggdraBackstory17 = "Yggdra cursed her own lack of strength as a result of Frinrir's death. She, as a result, began to hate magic as a concept and chose to never use hers for the rest of her life. She couldn't leave her room, so she dropped out of school to try and deal with her own feelings. One day, she had the dream of showing her brother her magic. The next day, she had the dream of seeing him again. All she had left of him now was his guardian jacket, tattered and torn from his final battle."
        # Chapter 4
        yggdraBackstory18 = "Chapter 04\n\nYggdra spent the next four years in her room thinking about what to do with herself. She took a long time to get over the death, and even more time to get herself out of the mindset it had put her in. When she turned nine, she finally asked for Kiyo to come over, wanting to talk and apologise for shutting him out for so long. When he got there, he scooped her up into a hug and thanked the divines over and over that she was okay. They spend the next few days catching up."
        yggdraBackstory19 = "Kiyo helped Yggdra get over her hatred of magic and decide that she was going to go to St. Guardia's to become a guardian like Frinrir was. She wanted to become strong enough that no one would ever have to go through the pain she did. Yggdra had, of course, missed many years of coursework and topics so she was very behind in school. Thankfully, Kiyo was willing to tutor her in whatever she missed. Yggdra never fuly understood all of the topics, but she had an idea of them."
        yggdraBackstory20 = "Eventually, Yggdra had to start practicing her magic again, but she was essentially starting from scratch since she hadn't used it in so long. At first, she didn't like using it; it reminded her too much of Frinrir. But she pushed through it and after a few weeks ended up finding magic fun again. From the age of eleven, Yggdra practiced her magic and making it her own in preparation for the Guardia's Entrance Exam. When she was old enough, she went to Grand Elise to take the exam."
        yggdraBackstory21 = "On her way to the exam, Yggdra met her first friend, Cid, and they took the exam together. Yggdra found the written portion of the exam easy, and fought her way to victory in the physical as well.\n\nA month later, her acceptance letter came in the mail, and from there, the rest is history..."

        # Yggdra Bio Search Commands
        yggdraShift = input(yggdraProfile)
        yggdraStore = yggdraProfile

        while yggdraShift == (""):
            yggdraShift = input(yggdraProfilePrompt)
        while (yggdraShift != "Leave" and yggdraShift != "leave"):
            if (yggdraShift == "Profile" or yggdraShift == "profile"):
                yggdraStore = yggdraProfile
                yggdraShift = input(yggdraProfile)
            if (
                    yggdraShift == "Wind Spells" or yggdraShift == "Wind spells" or yggdraShift == "wind Spells" or yggdraShift == "wind spells"):
                yggdraStore = yggdraWindSpells
                yggdraShift = input(yggdraWindSpells)
            if yggdraShift == (""):
                yggdraShift = input(
                    yggdraStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if (
                    yggdraShift != "Wind Spells" and yggdraShift != "Wind spells" and yggdraShift != "wind Spells" and yggdraShift != "wind spells" and yggdraShift != "Gravity Spells" and yggdraShift != "Gravity spells" and yggdraShift != "gravity Spells" and yggdraShift != "gravity spells" and yggdraShift != "Backstory" and yggdraShift != "backstory" and yggdraShift != "Profile" and yggdraShift != "profile" and yggdraShift != "Leave" and yggdraShift != "leave"):
                yggdraStore = yggdraProfilePrompt
                yggdraShift = input(
                    yggdraStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

            # Yggdra Backstory System
            if (yggdraShift == "Backstory" or yggdraShift == "backstory"):
                yggdraStore = "Table of Contents. Please enter the chapter you wish to view. Enter 'Back' to return to Yggdra's Bio.\n\nChapter 1\n\nChapter 2\n\nChapter 3\n\nChapter 4"
                yggdraShift = input(
                    "Table of Contents. Please enter the chapter you wish to view. Enter 'Back' to return to Yggdra's Bio.\n\nChapter 1\n\nChapter 2\n\nChapter 3\n\nChapter 4")
                if yggdraShift == (""):
                    yggdraShift = input(
                        yggdraStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if (
                        yggdraShift != "Chapter 1" and yggdraShift != "chapter 1" and yggdraShift != "Chapter One" and yggdraShift != "chapter one" and yggdraShift != "Chapter 2" and yggdraShift != "chapter 2" and yggdraShift != "Chapter Two" and yggdraShift != "chapter two" and yggdraShift != "Chapter 3" and yggdraShift != "chapter 3" and yggdraShift != "Chapter Three" and yggdraShift != "chapter Three" and yggdraShift != "Chapter 4" and yggdraShift != "chapter 4" and yggdraShift != "Chapter Four" and yggdraShift != "chapter four" and yggdraShift != "Back" and yggdraShift != "back"):
                    yggdraShift = input(
                        yggdraStore + "\n\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    quit("\nCommands entered inconsistantly. Please restart program. Sorry for the inconvienience.")
                if (yggdraShift == "Back" or yggdraShift == "back"):
                    input(
                        "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                    yggdraShift = "Chapter 1 "
                    yggdraStore = "Please Wait. . ."

                while (yggdraShift != "Back" and yggdraShift != "back"):
                    # Yggdra Chapter 1 Backstory System
                    if (
                            yggdraShift == "Chapter 1" or yggdraShift == "chapter 1" or yggdraShift == "Chapter One" or yggdraShift == "chapter one"):
                        yggdraShift = input(yggdraBackstory01)
                        yggdraShift = input(yggdraBackstory02)
                        yggdraShift = input(yggdraBackstory03)
                        yggdraShift = input(yggdraBackstory04)
                        yggdraShift = input(yggdraBackstory05)
                        yggdraShift = input(yggdraBackstory06)
                        yggdraShift = input(yggdraBackstory07)
                        yggdraShift = input(yggdraBackstory08 + "\n\nEnd of Chapter 01")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        yggdraStore = "Please Wait. . ."
                        break
                    # Yggdra Chapter 2 Backstory System
                    if (
                            yggdraShift == "Chapter 2" or yggdraShift == "chapter 2" or yggdraShift == "Chapter Two" or yggdraShift == "chapter two"):
                        yggdraShift = input(yggdraBackstory09)
                        yggdraShift = input(yggdraBackstory10)
                        yggdraShift = input(yggdraBackstory11)
                        yggdraShift = input(yggdraBackstory12)
                        yggdraShift = input(yggdraBackstory13 + "\n\nEnd of Chapter 02")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        yggdraStore = "Please Wait. . ."
                        break
                    # Yggdra Chapter 3 Backstory System
                    if (
                            yggdraShift == "Chapter 3" or yggdraShift == "chapter 3" or yggdraShift == "Chapter Three" or yggdraShift == "chapter three"):
                        xaeyzShift = input(yggdraBackstory14)
                        xaeyzShift = input(yggdraBackstory15)
                        xaeyzShift = input(yggdraBackstory16)
                        xaeyzShift = input(yggdraBackstory17 + "\n\nEnd of Chapter 03")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        yggdraStore = "Please Wait. . ."
                        break
                    # Yggdra Chapter 4 Backstory System
                    if (
                            yggdraShift == "Chapter 4" or yggdraShift == "chapter 4" or yggdraShift == "Chapter Four" or yggdraShift == "chapter four"):
                        yggdraShift = input(yggdraBackstory18)
                        yggdraShift = input(yggdraBackstory19)
                        yggdraShift = input(yggdraBackstory20)
                        yggdraShift = input(yggdraBackstory21 + "\n\nEnd of Chapter 04")
                        input(
                            "You will now be sent back to the profile. Please re-select 'backstory' if you wish to continue reading.")
                        yggdraStore = "Please Wait. . ."
                        break
                    else:
                        input("Please Wait. . .")
                        break

        # Yggdra Exit Command
        input("Database Search Completed. Please restart program to search again.")
        quit("\nProgram Completed Successfully. This is not an error.")

    else:
        input("The user data you have requested has not yet been implemented. Check back in a future release version.")
        quit("\nProgram Completed Successfully. This is not an error.")

else:
    input("The data you have requested has not yet been implemented. Check back in a future release version.")
    quit("\nProgram Completed Successfully. This is not an error.")

    # Exit Commands
    input("Database Search Completed. Please restart program to search again.")
    quit("\nProgram Completed Successfully. This is not an error.")
input("Database Search Completed. Please restart program to search again.")
