
# Import Commands
# import os
# clear = lambda: os.system('cls')

# Introduction
infoBarrier1 = input("IF YOU HAVE READ THIS PREVIOUSLY: Press enter twice to skip by this prompt and head to the beginning of the official code. Thanks!\n\nHey! If you are reading this, then you are here to test my code. Thanks for agreeing to do this by the way; error checking by someone else's eyes is a huge help.\n\nBy the way, I've set up the code in a way where if you press enter where the computer would look for an input from you, it should tell you that it's looking for an input. Just be sure to type an appropriate prompt in and the code will keep running as normal (I've tried to make the code as forgiving to as many forms of the input as I could. Hopefully that helps.).\n\nAnything that you change on this code cannot affect the final project, so if you do choose to delete anything or change the code in a way you can't rectify, simply reopen the page to get back to the original version.\n\nIf you do find a place where the code stops working as intended or grammar or something is off, take a note of it. If the code breaks and leaves you stuck on the screen, press the red button on the far left of the output screen. This will reset the code and make it usable again.\n\nThe way I wrote this code may cause code to run off of the screen. To fix this, select the button directly under the down arrow (it should be on the left side of the screen). It will be called 'Soft Wrap'.\n\nIf this ever happens while you test, reload the page and the issue should fix itself. Sorry for the inconvienience.\n\nFinally, this is a database of characters, events, storylines and powers for which I have conceptualized based off of a webcomic I read. This entire thing is an AU passion project (and to be honest, quite embarrasing to be shared at all).\n\nWhat I'm saying is, please don't judge the work based on the idea, and don't share this code to anyone without my permission.\n\nThanks again for wanting to test this, and welcome to my world.\n")
while infoBarrier1 == "" or infoBarrier1 == "Return" or infoBarrier1 == "return":
    infoBarrier1 = input(
        "Guardia: Tales of Halgeis Info Database. Please use the interface to select information.\nChapters:\n| Characters\n| Locations\n| Magics\n\nLeave the database by entering 'Leave'.\n")

    while infoBarrier1 == "":
        infoBarrier1 = input("Please Re-enter your database restriction.\n")
    while infoBarrier1 != "Characters" and infoBarrier1 != "characters" and infoBarrier1 != "Locations" and infoBarrier1 != "locations" and infoBarrier1 != "Magics" and infoBarrier1 != "magics" and infoBarrier1 != "Leave" and infoBarrier1 != "leave":
        infoBarrier1 = input("Please Re-enter your database restriction.\n")

    # Character Input Lists
    while infoBarrier1 == "Characters" or infoBarrier1 == "characters":
        infoBarrier2 = input(
            "Characters:\n| Xaeyz Kai\n| Mirago Fynae\n| Yggdrasil Aensyll\n| Cidelli Reimora\n| Mimi Seiran\n| Kimiko Quintai\n| Aeiyou Drefael\n| Kinto Verali\n| Amiru Soaren\n| Turcobé Sentai\n| Yumeizu Artilux\n\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n")

        while infoBarrier2 == "":
            infoBarrier2 = input("Please Re-enter your database restriction.\n")
        while infoBarrier2 != "Xaeyz Kai" and infoBarrier2 != "Xaeyz" and infoBarrier2 != "xaeyz kai" and infoBarrier2 != "xaeyz" and infoBarrier2 != "Yggdrasil Aensyll" and infoBarrier2 != "Yggdra" and infoBarrier2 != "yggdrasil aensyll" and infoBarrier2 != "yggdra" and infoBarrier2 != "Yggdrasil" and infoBarrier2 != "yggdrasil" and infoBarrier2 != "Cidelli Reimora" and infoBarrier2 != "Cid" and infoBarrier2 != "cidelli reimora" and infoBarrier2 != "cid" and infoBarrier2 != "Cidelli" and infoBarrier2 != "cidelli" and infoBarrier2 != "Mimi" and infoBarrier2 != "mimi" and infoBarrier2 != "Kimiko Quintai" and infoBarrier2 != "Kimiko" and infoBarrier2 != "kimiko quintai" and infoBarrier2 != "kimiko" and infoBarrier2 != "Aeiyou Drefael" and infoBarrier2 != "Aeiyou" and infoBarrier2 != "aeiyou drefael" and infoBarrier2 != "aeiyou" and infoBarrier2 != "Kinto Verali" and infoBarrier2 != "Kinto" and infoBarrier2 != "kinto verali" and infoBarrier2 != "kinto" and infoBarrier2 != "Amiru Soaren" and infoBarrier2 != "Amiru" and infoBarrier2 != "amiru soaren" and infoBarrier2 != "amiru" and infoBarrier2 != "Turcobe Sentai" and infoBarrier2 != "Turcobe" and infoBarrier2 != "turcobe sentai" and infoBarrier2 != "turcobe" and infoBarrier2 != "Turcobé Sentai" and infoBarrier2 != "Turcobé" and infoBarrier2 != "turcobé sentai" and infoBarrier2 != "turcobé" and infoBarrier2 != "Yumeizu Artilux" and infoBarrier2 != "Yumeizu" and infoBarrier2 != "yumeizu artilux" and infoBarrier2 != "yumeizu" and infoBarrier2 != "Mirago Fynae" and infoBarrier2 != "Mirago" and infoBarrier2 != "mirago fynae" and infoBarrier2 != "mirago" and infoBarrier2 != "Leave" and infoBarrier2 != "leave" and infoBarrier2 != "Back" and infoBarrier2 != "back":
            infoBarrier2 = input("Please Re-enter your database restriction.\n")

        # Xaeyz Kai Bio
        while infoBarrier2 == "Xaeyz Kai" or infoBarrier2 == "Xaeyz" or infoBarrier2 == "xaeyz kai" or infoBarrier2 == "xaeyz":
            # Xaeyz Bio Prompts
            xaeyzProfile = "Xaeyz Kai\n\nHometown: Meteora\nRace: Argen (Black, Gray)\nBirthday: July 7th, 4023\nGender: Male\nMagic Affinities\n| Wind\n| Gravity\n| Cosmic Wind\n\nItems\n| Aurora Staff\n| eMap\n| SoundCube\n| Gale Shard\n| PockUnity Orb\n| Psychal Library\n\n"
            xaeyzWindSpells = "Spells: Wind\n| Cyclone Slice\n| Gale Vaccuum\n| Aurora Scythe\n| Rising Wyrmwind\n* Rising Wyrmwind: Zephyr Flurry\n| Zephyr's Eye\n| Phoenix\n| Phoenix Hybrid\n* Phoenix Hybrid: Feather Control\n* Phoenix Hybrid: Feather Dance\n* Phoenix Hybrid: Gale Drive\n| Phoenix Ethereal\n* Phoenix Ethereal: Feather Control\n* Phoenix Ethereal: Feather Dance\n* Phoenix Ethereal: Gale Drive\n* Phoenix Ethereal: Zephyr's Eye\n* Phoenix Ethereal: Zephyr's Scream\n\nAurora Scythe: Magic Pact\n| Xaeyz's staff is made of a special meteor that could channel and amplify magical energy. He later learned to channel the energy through the staff more precisely, and formed a dual-bladed scythe; a weapon that represented his combat style perfectly. This scythe became his magic pact.\n\n"
            xaeyzGravitySpells = "Spells: Gravity\n| Levitation\n* Shift\n| Field\n| Quake\n| Lock\n\n"
            xaeyzCosmicWindSpells = "Spells: Cosmic Wind\n| Stardust Enhancement\n| Aurora's Grace\n| Meteor Crash\n| Luminous Aurora\n| Cosmic Seal\n| Constellar Ray\n\nAeon: Spirit of the Stars\n| Aeon is the spirit of Cosmic Wind, and the partner of Xaeyz. The only reason Xaeyz can use Cosmic Wind at all is because Aeon is with him. Similar to the other spirits of the mythical elementals, Aeon has no physical form and exists only in Xaeyz's psychal library. This, as a result, gives Xaeyz two active consciences. Aeon is a free soul and lives on trying to keep everyone around him safe while being as free as possible; values similar to Xaeyz's.\n\nFriends: Yes\nAcceptance: Yes\nMagic Use: Permitted\n\n"

            # Xaeyz Backstory Prompts
            # Chapter 1
            xaeyzBackstory01 = "Chapter 01\n\nXaeyz was born with wind magic, an oddity for Argens. As a result, " \
                               "no one could teach him, and was made fun of often. He did not let this stop him, however, " \
                               "and dropped out of school to train himself at age five. During his training, " \
                               "Xaeyz met another young argen named Mirago, who also dropped out of school due to a " \
                               "hatred of magic. Xaeyz helps Mirago overcome this hatred, and they train together for the " \
                               "next two years, dreaming of applying to St. Guardia's and becoming guardians.\n\n"
            xaeyzBackstory02 = "In 4030, a great black meteor that the world came to know as the Black Sun, came crashing " \
                               "down on Meteora. Mirago, being the Onyx Fire User, helps Xaeyz to try to slow it down, " \
                               "though the many strong magic users of the village could not. Their power is not enough to " \
                               "stop the catastrophe. Suddenly, Xaeyz gains a new power, the affinity for Cosmic Wind, " \
                               "and with this power and Mirago's Onyx Fire, the meteor was stopped.\n\n"
            xaeyzBackstory03 = "However, when fighting this interstellar threat, they discovered something incredible: " \
                               "the meteor was absorbing their magic. No other metal or rock on Phalmasia had the " \
                               "ability, so it was certainly unique. Unfortunately, this victory and information came " \
                               "with a great cost. Mirago had nearly exhausted his mana trying to stop the meteor, " \
                               "and collapsed. Mirago understood the power this meteor had, and realized what could " \
                               "happen if it fell into the wrong hands.\n\n"
            xaeyzBackstory04 = "Using what was left of his mana, he used Xaeyz's new wind and his own to build a Divine " \
                               "Spell; one that would seal out any magic but the ones that made up the seal. Though it " \
                               "would be weak, it would be enough to protect the meteor from those that would abuse its " \
                               "power. Mirago and Xaeyz were the only ones who knew about the properties of the meteor, " \
                               "so to keep the power safe, they mutually decided to keep the secret safe. This promise " \
                               "ended up being Mirago's final words.\n\n"
            xaeyzBackstory05 = "However, this was not the end of Xaeyz's problems. A lightning bolt hit Xaeyz in the " \
                               "back, and a fireball in the side. The villagers of Meteora were attacking him. They were " \
                               "scared of him. Who wouldn't be, after a seven-year-old boy stopped a threat the entire " \
                               "village's best couldn't stand a chance against? But Xaeyz didn't understand. He and " \
                               "Mirago had saved the lives of everyone. Why were they attacking him?\n\n"
            xaeyzBackstory06 = "He used his magic to defend himself and Mirago's body, but he was fighting an losing " \
                               "battle. He refused to fight back. He couldn't hurt his fellow argens; his family. So he " \
                               "merely defended. He couldn't last forever, though, and soon he was overwhelmed by the " \
                               "force of the townspeople. Then someone (something?) whispered to him. It told him not to " \
                               "fight the villagers. That he needed to get away to the place where he met Mirago. And so " \
                               "Xaeyz grabbed Mirago and took off into Duskfaze Forest.\n\n"
            xaeyzBackstory07 = "Xaeyz didn't know why he was listening to this ominous voice. But he does know who was " \
                               "talking to him: the cosmic wind. Whatever this new power was, it was sentient. But he " \
                               "trusted it, and he had to keep going to the place he met his best friend: Aurora Grotto. " \
                               "It was his and Mirago's favorite place. Xaeyz knew that Mirago had a favorite tree in the " \
                               "grotto; it was the biggest one in the field, at the very center of an island in a small " \
                               "lake. Under this flowering tree, Xaeyz gave Mirago his final resting place.\n\nEnd of Chapter 1\n"
            # Chapter 2
            xaeyzBackstory08 = "Chapter 02\n\nXaeyz spent the next few days mourning his friend's loss, but knew he still " \
                               "had more work to do: he had to seal the meteor's powers away as soon as possible. He " \
                               "couldn't do it himself; the only way to condense the meteor into a smaller object without " \
                               "cutting any of it off was with earth magic, and a lot of experience with weapon forging. " \
                               "Xaeyz knew someone who could do the job in Meteora: his grandfather, the town's " \
                               "blacksmith.\n\n"
            xaeyzBackstory09 = "The next day, Xaeyz snuck back into Meteora to see his grandfather, Armedies. When he " \
                               "found him in his workshop, he explained everything about what really happened and what " \
                               "needed to be done. Xaeyz apologized after he was done for coming in the first place, " \
                               "and started to leave in case his grandfather was scared of him like the rest of the town. " \
                               "Armedies, however, stops him and says he's willing to help him.\n\n"
            xaeyzBackstory10 = "Armedies also mentions that the village was oblivious to the help, and power, of Mirago. " \
                               "This was a great relief to Xaeyz because he figured that if there was a spell to render " \
                               "magic useless on an opject, then there might be one to steal magic from others, " \
                               "too. If anyone would be able to steal Mirago's powerful magic, it wouldn't be good. Xaeyz " \
                               "decided to keep Mirago and the existance of Aurora Grotto secret to anyone else.\n\n"
            xaeyzBackstory11 = "Getting the meteor was the easy part: Armedies was supposed to remove it that day so he " \
                               "could use it for a fuel source in his shop. Now, Xaeyz explained his designs for the " \
                               "meteor: a staff. Xaeyz wanted to turn the whole meteor into a staff that had built-in " \
                               "wings so he wouldn't need a glider. He also wanted to add a storage compartment somewhere " \
                               "that would require an input of magic to open.\n\n"
            xaeyzBackstory12 = "His grandfather condensed the entirity of the meteor into a staff, which ended up, " \
                               "for some reason, to be no heavier than an ordinary wooden one. He added the wings and a " \
                               "storage compartment to the staff. Once it was finished, Xaeyz needed to add the most " \
                               "important part. He took out the Divine Rune and cast the spell on the staff. But " \
                               "something unexpected happened. The spell summoned a blinding light that engulfed the " \
                               "workshop, and alerted everyone outside.\n\n"
            xaeyzBackstory13 = "Knowing people would come inside to check if everything is alright, his grandfather told " \
                               "him to go back to his house and talk to his parents one last time before running off. " \
                               "Xaeyz grabbed his new staff, now branded with the Divine Mark of the Phoenix (the symbol " \
                               "created when the divine spell was cast with fire and wind magic), and ran to his old " \
                               "home. When he got there, his parents were waiting for him.\n\n"
            xaeyzBackstory14 = "They embraced him, explaining that they were not afraid, and gave him some money, " \
                               "a black cloak with a hood, and a goodbye. Xaeyz blasted off back into the forest where he " \
                               "lived in Aurora Grotto for another week, surviving off of the fruit trees surrounding the " \
                               "grotto. It was rough and scary for him since he had never lived on his own before. Why " \
                               "would he; he was only seven after all. But much worse was to come; another tragedy.\n\n"
            xaeyzBackstory15 = "The next week, Xaeyz heard yelling coming from the direction of Metera, so he hopped into " \
                               "the trees and went to check it out. What he found horrified him. His mom, dad, " \
                               "and grandfather were on the ground in a field, beaten, shocked, and burned. They were " \
                               "shouting at them, asking where Xaeyz had gone. They did not say a word. They weren't " \
                               "going to give up family to an angry mob. For this secrecy, the townspeople gathered their " \
                               "magic and killed all three while Xaeyz watched.\n\n"
            xaeyzBackstory16 = "Xaeyz eyes widened. Tears streamed down his face as he looked at the burned corpses of " \
                               "his family. And he lost control. He crashed down into the field with cosmic wind rushing " \
                               "out of him. His eyes were aglow with this power, and the sight brought fear to the " \
                               "townspeople. Xaeyz screamed in anger at his former friends. Throughts raced through his " \
                               "head, and all he could do was scream. His magic was more relentless and powerful than it " \
                               "had ever been, and it sent everyone flying backwards.\n\n"
            xaeyzBackstory17 = "Xaeyz finally came to his senses and the cosmic wind died down. He looked back at the " \
                               "people of his former home cower and beg for forgiveness. All Xaeyz did was whisper an " \
                               "apology and rush away before he could get so much as a response. He ran farther than he " \
                               "ever had before, miles and miles farther away from Meteora than he had ever been. He kept " \
                               "going until he had gotten somewhere new: the Enchanted Forest of Grand Elise, the center " \
                               "of Halgeis.\n\nEnd of Chapter 2\n"
            # Chapter 3
            xaeyzBackstory18 = "Chapter 03\n\nHere Xaeyz found a home in a tree he called the Heaven Tree. A wolf, " \
                               "sheep and crow had been living together in the tree before he had arrived, " \
                               "and he befriended them. In remembrance of his best friend, he named the wolf Mirago, " \
                               "and trained here for the remainder of our story. Xaeyz was going to train hard to become " \
                               "a guardian. He had a mission to carry on his friend's dream; and to make sure no one hurt " \
                               "the way he did.\n\n"
            xaeyzBackstory19 = "Two years afterward, a fire was burning in the Tree of Souls at the very center of the " \
                               "forest. Xaeyz had grown very used to living in the wild and loved the forest, " \
                               "so he had to do something about it. Wind magic was notorious against fire, however. Water " \
                               "or earth users were most effective wih dealing with natural flames since wind usually " \
                               "just spread them. But now was Xaeyz's time to show off the results of his two years of " \
                               "training, and rushed to the tree.\n\n"
            xaeyzBackstory20 = "Putting up his hood, jumping above the trees with a magic gust and grabbing his Aurora " \
                               "Staff from his back, Xaeyz launched himself high above the tree. Xaeyz then spun his " \
                               "staff rapidly and launched magic out of it. The result was his first wind spell: Gale " \
                               "Vaccuum. This spell, unlike other wind spells, created an absense of air in its radius; a " \
                               "makeshift vaccuum. Since fire relies and feeds on air, the flames went out quickly after " \
                               "being engulfed by the attack. Xaeyz had gotten stronger.\n\n"
            xaeyzBackstory21 = "Xaeyz had been keeping tabs on a town nearby the Enchanted Forest called Drəklife since " \
                               "he had arrived. There, he learned of the name the argens from Meteora began to call him: " \
                               "'The Boy of Cosmic Wind'. He preferred the Cosmic Wind User; a boy sounded less cool to " \
                               "him. He was also known as 'The Forest's Shadow' since he had stopped the forest fire. " \
                               "However, two years after the fire, Xaeyz encountered his final challenge: a fire user " \
                               "attaking the town.\n\nEnd of Chapter 3\n"
            # Chapter 4
            xaeyzBackstory22 = "Chapter 04\n\nThe avian attacking was known as Hozura the Flame, a man who was being " \
                               "hunted by the guardians for about 3 weeks. He wasn't particularly strong, " \
                               "but was extremely smart and always attacked places without guardians and places that were " \
                               "far away from them. Xaeyz put on his cloak and jumped into the town to protect the " \
                               "townspeople and try to stop Hozura. Hozura had gathered all the townspeople together and " \
                               "had a magic attack poised at them. He fired when they didn't give him access to the bank.\n\n"
            xaeyzBackstory23 = "Xaeyz landed in front of them and used his own wind magic to stop the flames from hurting " \
                               "anyone. This upset Hozura, and he drew his sword, threatening to kill him if he kept " \
                               "getting in his way. The townspeople began to murmur behind him about being in the " \
                               "presence of the Forest's Shadow as Xaeyz took out his staff. The battle began. Hozura and " \
                               "Xaeyz clashed with their weapons for several minutes, and Xaeyz was on par with him " \
                               "despite being much younger than him.\n\n"
            xaeyzBackstory24 = "Xaeyz asked him during their fight why Hozura was doing this, and he responded by " \
                               "throwing a fireball at his head. Xaeyz promptl dodged and swung with his staff, " \
                               "landing a clean blow. Xaeyz gathered magic in his lungs and blew a blast of air at " \
                               "Hozura, pushing him backwards. However, Hozura had a plan of his own. He had concentrated " \
                               "magic beneath Xaeyz and began to trigger it. Xaeyz noticed and hopped out of the way just " \
                               "before the ground below him exploded.\n\n"
            xaeyzBackstory25 = "Hozura used an explosion beneath himself to get up to Xaeyz and swung his sword, " \
                               "throwing three fireballs along the arc of his swing. Xaeyz channelled mana into his staff " \
                               "and knocked them both away, all the while keeping damage to Drəklife as minimal as he " \
                               "could. Xaeyz threw slashes of wind at Hozura while parrying fireballs and explosions from " \
                               "Hozura. After a while of fighting him, he knew that this couldn't continue.\n\n"
            xaeyzBackstory26 = "Xaeyz needed to leave before the guardians got here, which means he needed to defeat " \
                               "Hozura before he left. Xaeyz needed to trap him, and Xaeyz had just the thing to do it. " \
                               "Xaeyz opened up the bottom of his glider on the staff and swung, releasing a wave of " \
                               "intense wind at Hozura, which he couldn't counter and sent him flying backwards. Xaeyz " \
                               "then inhaled and blew another gust at him, pinning him to the ground. Finally, " \
                               "he poised for his final blow.\n\n"
            xaeyzBackstory27 = "Xaeyz channelled as much mana as he could spare into his staff and let loose with a blast " \
                               "of air from his staff. The amount of air that Hozura was dealin with caused so much " \
                               "pressure, the ground beneath him began to crack and he passed out. As Xaeyz slowl floated " \
                               "to the ground, he knew that he had won. Xaeyz checked the town: barely any damage besides " \
                               "the cracks in the ground and a few buildings that were scorched. Not bad for his first " \
                               "actual battle.\n\n"
            xaeyzBackstory28 = "Xaeyz rushed back to the towns people to make sure they were ok. When he told them that " \
                               "Hozura had been knocked out, they celebrated. Xaeyz had Hozura cuffed and restrained so " \
                               "he couldn't move until the guardians got here. Xaeyz had also gained Hozura's bounty. In " \
                               "order to claim it, he had to stay afterwards and show his face to the guardians, " \
                               "which were two things he couldn't do. So he gave a note to the mayor that gave the bounty " \
                               "back to the town for repairs as a gift before leaving Drəklife once again.\n\n"
            xaeyzBackstory29 = "Xaeyz had defeated his first villain at age 11. For the next three years, Xaeyz trained " \
                               "as hard as he could.\n\nAfter those three years, he took the entry exam to St. Guardias, " \
                               "and at age 14, he passed, and the rest is history...\n\nEnd of Chapter 4\n"

            # Xaeyz Bio Output Commands
            xaeyzChapterPrompt = input(
                xaeyzProfile + "\n" + xaeyzWindSpells + "\n" + xaeyzGravitySpells + "\n" + xaeyzCosmicWindSpells + "\nEnter 'Continue' to view Chapter One. Enter 'Back' to return to Character Selection.\n")
            if xaeyzChapterPrompt == "Continue" or xaeyzChapterPrompt == "continue":
                xaeyzChapterPrompt = input(
                    xaeyzBackstory01 + "\n" + xaeyzBackstory02 + "\n" + xaeyzBackstory03 + "\n" + xaeyzBackstory04 + "\n" + xaeyzBackstory05 + "\n" + xaeyzBackstory06 + "\n" + xaeyzBackstory07 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                if xaeyzChapterPrompt == "":
                    xaeyzChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if xaeyzChapterPrompt != "Continue" and xaeyzChapterPrompt != "continue" and xaeyzChapterPrompt != "Back" and xaeyzChapterPrompt != "back":
                    xaeyzChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if xaeyzChapterPrompt == "Continue" or xaeyzChapterPrompt == "continue":
                    xaeyzChapterPrompt = input(
                        xaeyzBackstory08 + "\n" + xaeyzBackstory09 + "\n" + xaeyzBackstory10 + "\n" + xaeyzBackstory11 + "\n" + xaeyzBackstory12 + "\n" + xaeyzBackstory13 + "\n" + xaeyzBackstory14 + "\n" + xaeyzBackstory15 + "\n" + xaeyzBackstory16 + "\n" + xaeyzBackstory17 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                    if xaeyzChapterPrompt == "":
                        xaeyzChapterPrompt = input(
                            "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    if xaeyzChapterPrompt != "Continue" and xaeyzChapterPrompt != "continue" and xaeyzChapterPrompt != "Back" and xaeyzChapterPrompt != "back":
                        xaeyzChapterPrompt = input(
                            "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    if xaeyzChapterPrompt == "Continue" or xaeyzChapterPrompt == "continue":
                        xaeyzChapterPrompt = input(
                            xaeyzBackstory18 + "\n" + xaeyzBackstory19 + "\n" + xaeyzBackstory20 + "\n" + xaeyzBackstory21 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                        if xaeyzChapterPrompt == "":
                            xaeyzChapterPrompt = input(
                                "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                        if xaeyzChapterPrompt != "Continue" and xaeyzChapterPrompt != "continue" and xaeyzChapterPrompt != "Back" and xaeyzChapterPrompt != "back":
                            xaeyzChapterPrompt = input(
                                "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                        if xaeyzChapterPrompt == "Continue" or xaeyzChapterPrompt == "continue":
                            xaeyzChapterPrompt = input(
                                xaeyzBackstory22 + "\n" + xaeyzBackstory23 + "\n" + xaeyzBackstory24 + "\n" + xaeyzBackstory25 + "\n" + xaeyzBackstory26 + "\n" + xaeyzBackstory27 + "\n" + xaeyzBackstory28 + "\n" + xaeyzBackstory29 + "\n\nThis is the end of Xaeyz's Bio. Please press 'Enter' to choose another character when you are ready.\n")
                            break
            if xaeyzChapterPrompt == "Back" or xaeyzChapterPrompt == "back":
                break
            if xaeyzChapterPrompt == "":
                xaeyzChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if xaeyzChapterPrompt != "Continue" and xaeyzChapterPrompt != "continue" and xaeyzChapterPrompt != "Back" and xaeyzChapterPrompt != "back":
                xaeyzChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Mirago Fynae Bio
        while infoBarrier2 == "Mirago Fynae" or infoBarrier2 == "Mirago" or infoBarrier2 == "mirago fynae" or infoBarrier2 == "mirago":
            # Mirago Bio Prompts
            miragoProfile = "Mirago Fynae\n\nHometown: Meteora\nRace: Argen (Blue, Black)\nBirthday: June 15, 4023\nGender: Male\nMagic Affinities\n| Fire\n| Onyx Fire\n| Life\n\nItems\n| Psychal Grotto\n| Cloak of Shadows\n| Rune Bracelet\n\n"
            miragoFireSpells = "Spells: Fire\n| Dragon Flame Bombs\n| Flash Palm\n| Flame Heatwave\n| Pact: Pyre Bow\n| Inferno\n* Inferno: Drive\n| Combustion Stars\n| Dracunity\n| Dracunity Halflife\n* Dracunity Halflife: Scale Shot\n* Dracunity Halflife: Dragon Rush\n* Dracunity Halflife: Combustion Chain\n* Dracunity Halflife: Scale Mines\n* Dragunity Halflife: Tail Embers\n* Dracunity Halflife: Eye of Ancients\n| Dracunity Possesion\n* Dracunity Possesion: Dragon Rush\n* Dracunity Possesion: Dragon Flame Bombs\n* Dracunity Possesion: Infernal Roar\n* Dracunity Possesion: Eye of Ancients\n* Dracunity Possesion: Tail Embers\n* Dracunity Possesion: Magestic Incineration\n\nPyre Bow: Magic Pact\n| Mirago's pact perfectly represents his calm, ambitious and shy nature. By extending his pinky and thumb on his hand, he can create elongated flame structures from his fingertips and bind them with a string made of flame. This allows him to conjure fire arrows and other flame projectiles with his magic and fire them at his enemies. He can give the flames different properties to increase their utility.\n\n"
            miragoLifeSpells = "Spells: Life\n| Eternal Life\n| Karma's Judgement\n| Absorbtion\n| Soul's Reflection\n\n"
            miragoOnyxFireSpells = "Spells: Onyx Fire\n| Midnight Combustion\n| Onyx Ignition\n| Compression Burst\n| Hellflame Pillars\n| Kindling Rend\n\nArc: Spirit of the Sun\n| Arc is the spirit of Onyx Fire, and the partner of Mirago. The only reason Mirago can use Onyx Fire at all is because Arc is with him. Like the other mythical elementals, Arc has no physical form and abides solely in Mirago's psychal grotto. Arc is an ambitious and dedicated soul who tries to keep to those he trusts close and always strives to become stronger with his friends; values nearly identical to Mirago's.\n\nFriends: Yes\nAcceptance: Yes\nMagic Use: Permitted\n\n"

            # Mirago Backstory Prompts
            # Chapter 1
            miragoBackstory01 = "Chapter 01\n\nMirago loved magic. His dad was a fire user, and though not a " \
                                "guardian, still did his best to protect those in Meteora. He never knew his mom; she " \
                                "died shortly after his sister was born. Mirago looked up to him and awaited the day " \
                                "that he could get his own magic, and he finally got it on his fifth birthday. " \
                                "However, something was strange about his magic when he first used it; instead of " \
                                "being reddish-orange, they were a deep black. He thought that this was incredible " \
                                "and showed his sister, Lea. She was amazed, too, and she frequently went to Duckfaze " \
                                "Forest to watch him practice. \n\n"
            miragoBackstory02 = "However, these happy times didn't last. One day, Mirago wanted to try out a spell " \
                                "more advanced than he was ready for. Since his fire was black, he figured that meant " \
                                "he could do it anyway and tried it out. It didn't go as he expected it to. He wanted " \
                                "to make a flamethrower spell like his dad used. Instead, the fire burst out with a " \
                                "heavy force in every direction, searing trees around him and evaporating water in " \
                                "the creek nearby. Mirago was disoriented a bit, but otherwise unharmed. The same " \
                                "couldn't be said for Lea. \n\n"
            miragoBackstory03 = "Immediately, Mirago went to go and comfort her. She had a burn on her right arm and " \
                                "was crying. She was alright and understood that this was a mistake, but Mirago was " \
                                "still crying and apologizing over and over. He lifted her up (despite her being " \
                                "close to his own weight) and carried her back to their house. Once Mirago's father " \
                                "saw them approaching, he raced towards them and hurried them inside. He put a " \
                                "soothing remedy over Lea's arm and took her to the village doctor. Mirago didn't " \
                                "decide to come. \n\n"
            miragoBackstory04 = "Mirago sat at home for the two days that his dad and sister were gone and had a long " \
                                "talk to himself. He had hurt someone he cared about because of his magic. His father " \
                                "had lost trust in him because o his magic. These black flames weren't a blessing, " \
                                "they were a curse. That day, only two weeks after receiving his gift, " \
                                "decided solomnly to never bring the flames out again. His father and sister returned " \
                                "home later that day. His sister was fine, and his father understood that he was only " \
                                "practicing his magic, but told him to be more careful in the future. He was sure he " \
                                "would be careful; he wouldn't be using his magic anymore. \n\n"
            miragoBackstory05 = "Mirago fell into a depression for a while after that. He was scared and angry with " \
                                "himself and this strange power that had cursed him. His father noticed he rarely " \
                                "ever left the house since the incident, and more concerningly, hadn't seen him use " \
                                "his magic at all. Mirago dropped out of school later when he discovered that he " \
                                "would be forced to learn how to use his magic in his classes and began being " \
                                "homeschooled by his father. After a month of this, Mirago decided to get a breath of " \
                                "fresh air and go for his first walk through the forest since the incident. \n\n"
            miragoBackstory06 = "Mirago knew his dad and sister began to worry for him. They were both being " \
                                "supportive of Mirago's magic use and insisted that no one wished him ill after what " \
                                "happened, but he never responded and never showed any signs of having any interest " \
                                "in magic. Mirago had never told them about his promise to never use magic again, " \
                                "and for as long as he could, he intended to keep it a secret. He didn't want his dad " \
                                "to feel sorry for him, or his sister to feel responsible.\n\nEnd of Chapter 1\n "
            # Chapter 2
            miragoBackstory07 = "During his walk through the woods, he had seen the trees that he had scorched and " \
                                "sped up his walking pace to pass it faster. Just then, he heard a strong whoosh " \
                                "brustle through the leaves, which was odd since there was no wind at all a moment " \
                                "before. He decided to investigate the sound. After a few minutes of walking toward " \
                                "the origin of the wind (which was getting stronger and stronger as he got closer) " \
                                "and soon found himself in a field surrounded by trees with a waterfall that cascaded " \
                                "into a river and over a cliff into the ocean hundreds of feet below. \n\n"
            miragoBackstory08 = "The two boys didn't move for a few seconds, just staring at each other. The boy " \
                                "walks over to Mirago to which he explains how he got here and hurriedly apologizes, " \
                                "throwing his arms up in defense. The boy, however, noticed that something was wrong " \
                                "and asked if Mirago was okay. Mirago didn't understand this at first until he " \
                                "realised he had started crying. So he told the boy everything: who he was, " \
                                "what he'd done and about his magic. The boy listened intently and after he finished " \
                                "retelling he stated a simple response: 'Then they know it's not your fault.' \n\n"
            miragoBackstory09 = "Hearing this response from a total stranger, Mirago smiled and thanked the boy. He " \
                                "introduced himself and the boy said his name was Xaeyz. Xaeyz helped Mirago up to " \
                                "his feet and showed him around his secret grotto. Xaeyz told Mirago his story, " \
                                "and it turned out they both dropped out of school. It was getting dark at this " \
                                "point, and Mirago had to start heading home, but before Xaeyz stopped him and " \
                                "offered him a proposition. If he was interested, Mirago could meet him back here " \
                                "tomorrow to start to learn to love his magic again. \n\n"
            miragoBackstory10 = "Mirago didn't know how to respond, so he simply offered a maybe, said goodbye, " \
                                "and returned home. He sat on his bed that night thinking over Xaeyz's proposition. " \
                                "It's not like he didn't want to use his magic again, he was just afraid of hurting " \
                                "people with it. But if Xaeyz could somehow help him control this power any better " \
                                "than he could on his own, then at leas trying it out couldn't hurt. Tomorrow, " \
                                "he would go back into the woods to meet up with Xaeyz again and ask for his help " \
                                "with his magic comfortability. Tomorrow was going to be the first step back into " \
                                "magic. \n\n"
            miragoBackstory11 = "When Mirago arrived the next day, Xaeyz was already there training, throwing wind " \
                                "blasts in ever direction. When Xaeyz turned to see Mirago, his face shifted into a " \
                                "smile and greeted him. Xaeyz said that since Mirago was only afraid of hurting " \
                                "people with his magic, all he needed to do was learn to trust it again by learning " \
                                "to control it better. Xaeyz couldn't help him control his magic since he didn't know " \
                                "how fire magic felt, but he would be here to help stop anything that could go wrong; " \
                                "that and mental support. Over the next three months, Mirago began to slowly overcome " \
                                "his fears. \n\n"
            miragoBackstory12 = "Mirago and Xaeyz continued to train together for another two years, sparring which " \
                                "each other and learning new spells. They became each other's rivals, striving to " \
                                "apply to St. Guardia's Academy and become guardians. One day when they were " \
                                "sparring, a tragedy brought itself onto Meteora: a large black meteor hurling " \
                                "towards the town. It shook the ground as it made its descent. Mirago and Xaeyz " \
                                "looked at each other and knew what they had to do: they rushed back to the village " \
                                "to do what they could to stop it.\n\nEnd of Chapter 2\n "
            # Chapter 3
            miragoBackstory13 = "When they got to the village, Mirago and Xaeyz saw the defender argens running away, " \
                                "too. They had tried to stop it, and had no effect on it whatsoever. They couldn't " \
                                "stop it so they were running away. Xaeyz and Mirago didn't know what do. If the " \
                                "village defenders couldn't stop this thing, how could two seven year olds? But " \
                                "something changed Mirago's mind: among them was Mirago's dad. He was running away, " \
                                "too. Mirago immidiately jumped down into the fray and towards the meteor. Xaeyz " \
                                "tried to stop him, but followed him in. As they stood and stared at the meteor, " \
                                "they readied attacks to fire at it. \n\n"
            miragoBackstory14 = "In the woods, Xaeyz and Mirago had practiced their teamwork and combination spells. " \
                                "They learned that is Mirago used his flames and Xaeyz used his wind, " \
                                "he could amplify the power of the fire. So they launched everything they had at the " \
                                "meteor. However, nothing happened; the meteor wasn't slowing down. Just then, " \
                                "something had begun surrounding Xaeyz; a glistering light swirling around him. Xaeyz " \
                                "opened his eyes and forced more energy than he ever had out of himself. Instead of " \
                                "his greenish-blue gusts of wind, it came out in blues and purples. It looked like an " \
                                "aurora. \n\n"
            miragoBackstory15 = "This power engulfs Mirago's flames and amplifies them to a degree that wasn't " \
                                "comparable to their boosts before. With this new power, Mirago decided to put in " \
                                "everything, too. He poured more and more energy into his flames, making them burn " \
                                "hotter and hotter. This new power that Xaeyz had aquired was doing the trick; the " \
                                "meteor was finally slowing down! But Mirago knew that something was wrong. This much " \
                                "power should be slowing it down far more than it was. In fact, the defenders earlier " \
                                "should have had some effect on it. Was the meteor nullifying, no, absorbing their " \
                                "magics? \n\n"
            miragoBackstory16 = "Mirago notices himself growing weaker and weaker the more he puts his energy into " \
                                "his flames, but he has just enough strength to help Xaeyz lower the meteor safely to " \
                                "the ground. Afterward, Mirago collapses to the ground in a daze. He knows that he " \
                                "doesn't have long until his magic burns out, so he tells Xaeyz what he discovers. He " \
                                "asks Xaeyz to seal away the meteor before anyone else realizes what it can do, " \
                                "and gives him what is left of his magic to cast his final spell: a Divine Seal that " \
                                "could lock away the power of the meteor for only Xaeyz's use. After sealing this in " \
                                "a rune, Mirago begins his sleep.\n\nEnd of Chapter 3\n "
            # Chapter 4
            miragoBackstory17 = "'Get up.' A black ember ignites itself in Mirago's body and continues to burn hotter " \
                                "and hotter. The power grows and emerges as a large burst, pushing away the dirt " \
                                "prison around him and throwing him out of his grave. Where was he? He tries to open " \
                                "his eyes, but a scar over his right eye forces it closed. He uses his left eye to " \
                                "look around his surroundings and immidiately identiies where he is: Xaeyz's Grotto. " \
                                "Xaeyz must have brought him here and buried him, but why? He seems to hav forgotten " \
                                "everything. Mirago walks back to Meteora to find Xaeyz. But seeing the meteor in the " \
                                "center of town brings back everything. He rushes back to the grotto searching for " \
                                "Xaeyz. \n\n"
            miragoBackstory18 = "Mirago screams out for Xaeyz, but he's nowhere to be found. Tears well in his eyes " \
                                "and he crumples to the floor in a scream of agony, and releases his black flames, " \
                                "which touch the cut on his right eye. He winces in pain and covers his eyes. But " \
                                "when he releases the eye, he finds he can open it a small amount. His fire must have " \
                                "helped heal his eye. He quickly covers his eye with his hand and throws flames into " \
                                "the cut. He screams in pain, but after the pain passes, he's able to open his eye " \
                                "fully. Mirago realized something just then: Xaeyz and everyone he knew thought that " \
                                "he was dead. He was not. \n\n"
            miragoBackstory19 = "Mirago turned back to the grave and filled in the hole as best he could so Xaeyz " \
                                "wouldn't know he was alive. Soon after, Mirago met the spirit of the black flames " \
                                "who called himself 'Arc'. Arc explains that his magic is called Onyx Fire, " \
                                "and that he was its sole user. Mirago asked why he only appeared now, " \
                                "and he responded with he only needed to see him now since he lived in his " \
                                "subconscious. Arc said that if he didn't want to use his flames, he had his own and " \
                                "that if he ever wanted to talk again to simply come and see him. Mirago was left " \
                                "confused at his words. He had his own fire? Wasn't Onyx Fire his flames? After a few " \
                                "minutes, he finally got it. Arc was saying he could use normal fire, too. \n\n"
            miragoBackstory20 = "Mirago didn't understand how to use the normal fire, though; he'd never done it " \
                                "before. He decided to ask Arc for what to do, and he advised that his magic would " \
                                "feel different than onyx flames, and that he should try to put his own feelings and " \
                                "strength into it. It took a week or two, but Mirago had finally found a way to " \
                                "reliably use his own fire. It was the most connected he'd ever felt to his magic " \
                                "since using it. Mirago decided that he would train himself instead of going to St. " \
                                "Guardia's with Xaeyz. \n\n"
            miragoBackstory21 = "Mirago didn't have a way to seal away the meteor without the rune he and Xaeyz had " \
                                "made and didn't want to risk Xaeyz coming back and seeing him, so he knew he had to " \
                                "leave to keep himself a secret. So he did. He left the grotto for northern Mu'karr " \
                                "under the cover of the forests that grew all over the continent. Ever since then, " \
                                "he's been training his magic, honing his skills wth Arc's guidance and friendship, " \
                                "and waiting for the perfect moment to re-emerge. . .\n\nEnd of Chapter 4\n "

            # Mirago Bio Search Commands
            miragoChapterPrompt = input(
                miragoProfile + "\n" + miragoFireSpells + "\n" + miragoLifeSpells + "\n" + miragoOnyxFireSpells + "\nEnter 'Continue' to view Chapter One. Enter 'Back' to return to Character Selection.\n")
            if miragoChapterPrompt == "Continue" or miragoChapterPrompt == "continue":
                miragoChapterPrompt = input(
                    miragoBackstory01 + "\n" + miragoBackstory02 + "\n" + miragoBackstory03 + "\n" + miragoBackstory04 + "\n" + miragoBackstory05 + "\n" + miragoBackstory06 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                if miragoChapterPrompt == "":
                    miragoChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if miragoChapterPrompt != "Continue" and miragoChapterPrompt != "continue" and miragoChapterPrompt != "Back" and miragoChapterPrompt != "back":
                    miragoChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if miragoChapterPrompt == "Continue" or miragoChapterPrompt == "continue":
                    miragoChapterPrompt = input(
                        miragoBackstory07 + "\n" + miragoBackstory08 + "\n" + miragoBackstory09 + "\n" + miragoBackstory10 + "\n" + miragoBackstory11 + "\n" + miragoBackstory12 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                    if miragoChapterPrompt == "":
                        miragoChapterPrompt = input(
                            "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    if miragoChapterPrompt != "Continue" and miragoChapterPrompt != "continue" and miragoChapterPrompt != "Back" and miragoChapterPrompt != "back":
                        miragoChapterPrompt = input(
                            "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    if miragoChapterPrompt == "Continue" or miragoChapterPrompt == "continue":
                        miragoChapterPrompt = input(
                            miragoBackstory13 + "\n" + miragoBackstory14 + "\n" + miragoBackstory15 + "\n" + miragoBackstory16 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                        if miragoChapterPrompt == "":
                            miragoChapterPrompt = input(
                                "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                        if miragoChapterPrompt != "Continue" and miragoChapterPrompt != "continue" and miragoChapterPrompt != "Back" and miragoChapterPrompt != "back":
                            miragoChapterPrompt = input(
                                "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                        if miragoChapterPrompt == "Continue" or miragoChapterPrompt == "continue":
                            miragoChapterPrompt = input(
                                miragoBackstory17 + "\n" + miragoBackstory18 + "\n" + miragoBackstory19 + "\n" + miragoBackstory20 + "\n" + miragoBackstory21 + "\n\nThis is the end of Mirago's Bio. Please press 'Enter' to choose another character when you are ready.\n")
                            break
            if miragoChapterPrompt == "Back" or miragoChapterPrompt == "back":
                break
            if miragoChapterPrompt == "":
                miragoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if miragoChapterPrompt != "Continue" and miragoChapterPrompt != "continue" and miragoChapterPrompt != "Back" and miragoChapterPrompt != "back":
                miragoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Yggdrasil Aensyll Bio
        while infoBarrier2 == "Yggdrasil Aensyll" or infoBarrier2 == "Yggdra" or infoBarrier2 == "yggdrasil aensyll" or infoBarrier2 == "yggdra" or infoBarrier2 == "Yggdrasil" or infoBarrier2 == "yggdrasil":
            # Yggdra Bio Prompts
            yggdraProfile = "Yggdrasil (Yggdra) Aensyll\n\nHometown: Ashford\nRace: Terrian (Fox)\nBirthday: December 17, 4023\nGender: Female\nMagic Affinities\n| Wind\n\nItems\n| Gale Shard\n| PockUnity Orb\n| Frinrir's Hat\n| Frinrir's Jacket\n\n"
            yggdraWindSpells = "Spells: Wind\n| Gale Impact\n| Cutting Spiral\n| Pact: Zephyr\n* Zephyr: Shield\n* Zephyr: Barrier\n* Zephyr: Reflection\n* Zephyr: Tag-Team\n| Breeze Gems\n* Breeze Gems: Darts\n* Breeze Gems: Ring\n* Breeze Gems: Emblem\n\nZephyr: Spirit Pact\n| Zephyr is a spirit pact formed from her dead brother's (Frinrir) remaining mana and will. As her pact, Zephyr takes the form of a shield, symbolizing the will to protect Yggdra. He also takes his sprite form to assist Yggdra in casting unique spells. The bond that Yggdra and Zephyr share is deep, and that bond is what makes their duo so strong.\n\n"

            # Yggdra Backstory Prompts
            # Chapter 1
            yggdraBackstory01 = "Chapter 01\n\nYggdra had always been fascinated by magic. Her mother waas once a " \
                                "guardian who had retired to live a more quiet and peaceful life. Frinrir, " \
                                "her older brother and who Yggdra called Frinny, was finishing up his final year at St. " \
                                "Guardia's Academy. Frinrir was Yggdra's idol. He was the main reason she was so excited " \
                                "to find out if she had magic. On her fifth birthday, she unlocked her magic and " \
                                "discovered her affinity for wind, just like her brother.\n\n"
            yggdraBackstory02 = "She was ecstatic, and wanted to show her brother when he came home a few days later. She " \
                                "was too eager about using her magic, however. She had just unlocked it; her control " \
                                "wasn't near average yet. Despite this, one day she practiced near a neighbor's house and " \
                                "her mana lost control and broke their window. When Yggdra's mom found out about it, " \
                                "she forbade her use of magic for a month, which means she wouldn't be able to show " \
                                "Frinrir her new magic.\n\n"
            yggdraBackstory03 = "Yggdra begged for her to rescind the ban, but her mother wouldn't budge. She had plenty " \
                                "of schoolwork to catch up on, so practicing her magic wasn't the most efficient use of " \
                                "her time, either. But of course this meant nothing to a five year old girl with new " \
                                "magical abilities. The very next day, Yggdra left the house telling her mom that she was " \
                                "going to study with her friend Kiyo. However, what she was really doing was meeting up " \
                                "with Kiyo to practice some more of her magic.\n\n"
            yggdraBackstory04 = "Kiyo didn't understand why she was still using her magic even when her mom told her it " \
                                "wasn't allowed, and Yggdra said that it was because magic waits for no one. She only " \
                                "wanted to get better at magic as fast as possible, and the first step to doing that was " \
                                "using lightfoot spells. Lightfoot spells were hard for beginners, and especially " \
                                "difficult for beginners who didn't have teachers guiding them through it. But after an " \
                                "argument with Kiyo saying she should stop and stomping the floor, Yggdra had " \
                                "accidentally figured it out.\n\n"
            yggdraBackstory05 = "Kiyo knew where this was going as soon as Yggdra fell over from the force of her spell, " \
                                "and told her not to do anything drastic. But Yggdra was past that. She gathered all the " \
                                "mana she could into her feet and jumped. The jump launched her a hundred feet in the " \
                                "air, and the sight was unlike anything she had ever seen before. She could see the above " \
                                "the trees of the forest a mile away from her, the town a few miles behind her house, " \
                                "and a great, clear view of the sky. She was awestruck. \n\n"
            yggdraBackstory06 = "But what she didn't expect to see was smoke billowing out of Kytegrove Forest. Something " \
                                "was clearly wrong; Yggdra could feel it, and she knew she had to tell someone. But she " \
                                "had a bigger problem on her hands: she was falling out of the sky. Thankfully, " \
                                "Kiyo was there to catch her before she hit the ground. Yggdra explained frantically to " \
                                "Kiyo what she saw, and they both returned to Yggdra's house  to tell the one person they " \
                                "knew could do something: Frinrir. \n\n"
            yggdraBackstory07 = "When they got to the house, a girl was in the living room with Yggdra's parents and " \
                                "Frinrir. The girl's name was Alexis, and was apparently Frinrir's friend from Guardia's " \
                                "and his assigned partner. Yggdra told Frinrir what she saw (and brushed off her mom when " \
                                "she asked how she knew), but it turns out Alexis was here to take him to go and " \
                                "investigate it. Frinrir was going to leave again, and he'd just come home. She hadn't " \
                                "even shown him her new magic yet. \n\n"
            yggdraBackstory08 = "Yggdra then turned to Alexis and asked her why she had to take him away. Alexis " \
                                "apologised and promised to get him back as soon as possible. Yggdra didn't want him to " \
                                "go, but Frinrir told her it was just a quick job. He'd come home after a few hours and " \
                                "after that, she could show him her new magic. This put Yggdra at ease, and Frinrir and " \
                                "Alexis took off towards Kytegrove Forest. Yggdra waited for a while with Kiyo and played " \
                                "tag for a bit. That's when she felt something horribly wrong. \n\nEnd of Chapter 1\n"

            # Chapter 2
            yggdraBackstory09 = "Chapter 02\n\nYggdra and Kiyo were outside throwing a ball around in Yggdra's yard when " \
                                "she got the feeling. A burning feeling of dread and pain washed over her, and she was " \
                                "paralyzed in place. Something was wrong with Frinrir. She could feel it. At this point, " \
                                "Kiyo had noticed Yggdra's paralysis and was frantically trying to bring her back. " \
                                "Seconds later, Yggdra awoke, told Kiyo what she felt and where she was going, " \
                                "and ran off towards the forest to Frinrir. \n\n"
            yggdraBackstory10 = "When Yggdra finally reached the forest, she ran through the trees to where she was being " \
                                "led by her vision. There, leaning on a tree, exhausted, lay Frinrir with a hole blasted " \
                                "in his chest. Yggdra froze as tears began to stream down her face. By this point, " \
                                "Frinrir noticed Yggdra's presence, and his eyes widened. He begged Yggdra weakly to get " \
                                "out of here, and that it was dangerous to stay here. Yggdra couldn't hear him though; " \
                                "all she could ask was how she could help him. \n\n"
            yggdraBackstory11 = "This continued for about a minute until Alexis was blasted by her and landed hard " \
                                "against the tree, knocking her out. This was the thing that finally got Yggdra's " \
                                "attention, and she began to turn around in fear, and looked at whatever was attacking " \
                                "her brother. What she saw didn't stick with her, but what she felt did: a cold, fierce, " \
                                "murderous, uncontrollable force was looming over her. This feeling is what Yggdra would " \
                                "remember and how she would shape the monterous feeling. \n\n"
            yggdraBackstory12 = "The thing poised for attack, reaching its hand out to grab Yggdra's head. Yggdra didn't " \
                                "move; she couldn't move. She was petrified by the thing's aura and bloodlust. She " \
                                "accepted the fact, then and there, that she was going to die. Just then, she felt a hand " \
                                "on her shoulder, and the thing went flying backwards. Yggdra looked up to see Frinrir " \
                                "standing arm outstretched with magic eminating from his hand. He created a ball of magic " \
                                "and threw it at a stone that the attacker had dropped, shattering it. \n\n"
            yggdraBackstory13 = "Just as suddenly as he stood up, he fell to the ground. Yggdra lifted him up, begging " \
                                "for him to be ok, but he only managed to say one thing: 'As long as you are alive, " \
                                "I'll be there to protect you. So don't worry.'. After saying this, the light left his " \
                                "eyes, and his body went limp. Within a week of him being a guardian, Frinrir lost his " \
                                "life. Yggdra lost all emotion in that moment. She couldn't move and sat still, " \
                                "tears streaming from her eyes, staring at her brother. \n\nEnd of Chapter 2\n"

            # Chapter 3
            yggdraBackstory14 = "Chapter 03\n\nAlexis woke up a few hours later and saw Yggdra and Frinrir. Of course, " \
                                "she was crushed by the news, but as a guardian and friend of Frinrir's, her job was to " \
                                "protect Yggdra. But when she reached out to her to ask her to follow her out of the " \
                                "forest, Yggdra swatted her hand away. She turned toward Alexis slowly and showed her her " \
                                "lightless eyes before getting up and walking back to her house. Alexis couldn't do " \
                                "anything but follow her. \n\n"
            yggdraBackstory15 = "Kiyo was waiting back at Yggdra's house with her mom for Yggdra to come back. Of course, " \
                                "when Mrs. Aensyll found out about Yggdra using her magic, she was angry. But all of that " \
                                "fizzled out the minute Yggdra stepped into the door. She didn't say a word, looked down " \
                                "at the floor, and walked past everyone to her room upstairs. No one understood until a " \
                                "bit later when Alexis came in the door and dropped the news. Yggdra's parents were " \
                                "crushed, and Kiyo ran up to Yggdra's room to talk. Her door was already locked. \n\n"
            yggdraBackstory16 = "Kiyo knocked on the door, asking Yggdra to open the door and that he only wanted to " \
                                "talk. She murmured something that Kiyo couldn't hear. When he asked again, a thundering " \
                                "voice that could only be the result of Yggdra enhancing her volume with wind magic " \
                                "screamed 'NO!' shook the entire house. Kiyo faltered backwards a bit, said that he could " \
                                "talk anytime she wanted and to let him know, and went home heavy hearted from the " \
                                "encounter. Yggdra didn't speak to anyone for quite a while after that. \n\n"
            yggdraBackstory17 = "Yggdra cursed her own lack of strength as a result of Frinrir's death. She, as a result, " \
                                "began to hate magic as a concept and chose to never use hers for the rest of her life. " \
                                "She couldn't leave her room, so she dropped out of school to try and deal with her own " \
                                "feelings. One day, she had the dream of showing her brother her magic. The next day, " \
                                "she had the dream of seeing him again. All she had left of him now was his guardian " \
                                "jacket, tattered and torn from his final battle. \n\nEnd of Chapter 3\n"

            # Chapter 4
            yggdraBackstory18 = "Chapter 04\n\nYggdra spent the next four years in her room thinking about what to do " \
                                "with herself. She took a long time to get over the death, and even more time to get " \
                                "herself out of the mindset it had put her in. When she turned nine, she finally asked " \
                                "for Kiyo to come over, wanting to talk and apologise for shutting him out for so long. " \
                                "When he got there, he scooped her up into a hug and thanked the divines over and over " \
                                "that she was okay. They spend the next few days catching up. \n\n"
            yggdraBackstory19 = "Kiyo helped Yggdra get over her hatred of magic and decide that she was going to go to " \
                                "St. Guardia's to become a guardian like Frinrir was. She wanted to become strong enough " \
                                "that no one would ever have to go through the pain she did. Yggdra had, of course, " \
                                "missed many years of coursework and topics so she was very behind in school. Thankfully, " \
                                "Kiyo was willing to tutor her in whatever she missed. Yggdra never fuly understood all " \
                                "of the topics, but she had an idea of them. \n\n"
            yggdraBackstory20 = "Eventually, Yggdra had to start practicing her magic again, but she was essentially " \
                                "starting from scratch since she hadn't used it in so long. At first, she didn't like " \
                                "using it; it reminded her too much of Frinrir. But she pushed through it and after a few " \
                                "weeks ended up finding magic fun again. From the age of eleven, Yggdra practiced her " \
                                "magic and making it her own in preparation for the Guardia's Entrance Exam. When she was " \
                                "old enough, she went to Grand Elise to take the exam. \n\n"
            yggdraBackstory21 = "On her way to the exam, Yggdra met her first friend, Cid, and they took the exam " \
                                "together. Yggdra found the written portion of the exam easy, and fought her way to " \
                                "victory in the physical as well.\n\nA month later, her acceptance letter came in the " \
                                "mail, and from there, the rest is history... \n\nEnd of Chapter 4\n"

            # Yggdra Bio Search Commands
            yggdraChapterPrompt = input(
                yggdraProfile + "\n" + yggdraWindSpells + "\nEnter 'Continue' to view Chapter One. Enter 'Back' to return to Character Selection.\n")
            if yggdraChapterPrompt == "Continue" or yggdraChapterPrompt == "continue":
                yggdraChapterPrompt = input(
                    yggdraBackstory01 + "\n" + yggdraBackstory02 + "\n" + yggdraBackstory03 + "\n" + yggdraBackstory04 + "\n" + yggdraBackstory05 + "\n" + yggdraBackstory06 + "\n" + yggdraBackstory07 + "\n" + yggdraBackstory08 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                if yggdraChapterPrompt == "":
                    yggdraChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if yggdraChapterPrompt != "Continue" and yggdraChapterPrompt != "continue" and yggdraChapterPrompt != "Back" and yggdraChapterPrompt != "back":
                    yggdraChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if yggdraChapterPrompt == "Continue" or yggdraChapterPrompt == "continue":
                    yggdraChapterPrompt = input(
                        yggdraBackstory09 + "\n" + yggdraBackstory10 + "\n" + yggdraBackstory11 + "\n" + yggdraBackstory12 + "\n" + yggdraBackstory13 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                    if yggdraChapterPrompt == "":
                        yggdraChapterPrompt = input(
                            "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    if yggdraChapterPrompt != "Continue" and yggdraChapterPrompt != "continue" and yggdraChapterPrompt != "Back" and yggdraChapterPrompt != "back":
                        yggdraChapterPrompt = input(
                            "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                    if yggdraChapterPrompt == "Continue" or yggdraChapterPrompt == "continue":
                        yggdraChapterPrompt = input(
                            yggdraBackstory14 + "\n" + yggdraBackstory15 + "\n" + yggdraBackstory16 + "\n" + yggdraBackstory17 + "\n\nEnter 'Continue' to view the next chapter. Enter 'Back' to return to Character Selection.\n")
                        if yggdraChapterPrompt == "":
                            yggdraChapterPrompt = input(
                                "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                        if yggdraChapterPrompt != "Continue" and yggdraChapterPrompt != "continue" and yggdraChapterPrompt != "Back" and yggdraChapterPrompt != "back":
                            yggdraChapterPrompt = input(
                                "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                        if yggdraChapterPrompt == "Continue" or yggdraChapterPrompt == "continue":
                            yggdraChapterPrompt = input(
                                yggdraBackstory18 + "\n" + yggdraBackstory19 + "\n" + yggdraBackstory20 + "\n" + yggdraBackstory21 + "\n\nThis is the end of Yggdra's Bio. Please press 'Enter' to choose another character when you are ready.\n")
                            break
            if yggdraChapterPrompt == "Back" or yggdraChapterPrompt == "back":
                break
            if yggdraChapterPrompt == "":
                yggdraChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if yggdraChapterPrompt != "Continue" and yggdraChapterPrompt != "continue" and yggdraChapterPrompt != "Back" and yggdraChapterPrompt != "back":
                yggdraChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Cidelli Reimora Bio
        while infoBarrier2 == "Cidelli Reimora" or infoBarrier2 == "Cid" or infoBarrier2 == "cidelli reimora" or infoBarrier2 == "cid" or infoBarrier2 == "Cidelli" or infoBarrier2 == "cidelli":
            # Cid Bio Prompts
            cidProfile = "Cidelli (Cid) Reimora\n\nHometown: Oshborne\nRace: Terrian, Sheep (Black Fur/Skin)\nBirthday: October 2, 4023\nGender: Female\nMagic Affinities\n| Lightning\n\nItems\n| Bolt Shard\n| Mom's Pendant\n\n"
            cidLightningSpells = "Spells: Lightning\n| Shock Orbs\n| Shock Step\n* Shock Step: Trail\n* Shock Step: Dash\n| Bolt Strike\n| Thunder's Arrow\n| Bolt Charge\n| Lightning Discharge\n| Storm Cloak\n* Storm Cloak: Teleport\n* Storm Cloak: Orb Control\n* Storm Cloak: Reflux\n| Magnetize\n| Precision Bolt\n\n"

            # Cid Bio Search Commands
            cidChapterPrompt = input(
                cidProfile + "\n" + cidLightningSpells + "\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n")
            if cidChapterPrompt == "Back" or cidChapterPrompt == "back":
                break
            if cidChapterPrompt == "":
                cidChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if cidChapterPrompt != "Continue" and cidChapterPrompt != "continue" and cidChapterPrompt != "Back" and cidChapterPrompt != "back":
                cidChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Mimi Serian Bio
        while infoBarrier2 == "Mimi Seiran" or infoBarrier2 == "Mimi" or infoBarrier2 == "Mimi seiran" or infoBarrier2 == "mimi":
            # Mimi Bio Prompts
            mimiProfile = "Mimi Seiran\n\nHometown: Cilfier\nRace: Terrian, Tanuki(Light Brown with Brown Spots)\nBirthday: March 25, 4020\nGender: Female\nMagic Affinities\n| Water\n\nItems\n| Aqua Shard\n| PockUnity Orb\n\n"
            mimiWaterSpells = "Spells: Water\n| Swamp Trap\n| Morning Dew\n| Water Wave\n| Aqua Ring\n| Flood Jet\n| Water Tentacles\n| Ocean's Seal\n\n"

            # Mimi Bio Search Commands
            mimiChapterPrompt = input(
                mimiProfile + "\n" + mimiWaterSpells + "\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n")
            if mimiChapterPrompt == "Back" or mimiChapterPrompt == "back":
                break
            if mimiChapterPrompt == "":
                mimiChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if mimiChapterPrompt != "Continue" and mimiChapterPrompt != "continue" and mimiChapterPrompt != "Back" and mimiChapterPrompt != "back":
                mimiChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Kimiko Quintai Bio
        while infoBarrier2 == "Kimiko Quintai" or infoBarrier2 == "Kimiko" or infoBarrier2 == "kimiko quintai" or infoBarrier2 == "kimiko":
            # Kimiko Bio Prompts
            kimikoProfile = "Kimiko Quintai\n\nHometown: Skykumo\nRace: Avian (Blue, Black)\nBirthday: June 16, 4023\nGender: Male\nMagic Affinities\n| Fire\n\nItems\n| Flame Shard\n| Featherband\n| PockUnity Orb\n\n"
            kimikoFireSpells = "Spells: Fire\n| Fire Bolt\n| Flame Bakudan\n| Ryuuken\n* Ryuuken: Combat\n* Ryuuken: Embers\n* Ryuuken: Combust\n| Flashfire Stars\n| Burning Pillar\n| Fire Burst\n| Ember Mines\n\n"

            # Kimiko Backstory Prompts
            kimikoBackstory01 = ""

            # Kimiko Bio Search Commands
            kimikoChapterPrompt = input(
                kimikoProfile + "\n" + kimikoFireSpells + "\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n")
            if kimikoChapterPrompt == "Back" or kimikoChapterPrompt == "back":
                break
            if kimikoChapterPrompt == "":
                kimikoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if kimikoChapterPrompt != "Continue" and kimikoChapterPrompt != "continue" and kimikoChapterPrompt != "Back" and kimikoChapterPrompt != "back":
                kimikoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Aeiyou Drefael Bio
        while infoBarrier2 == "Aeiyou Drefael" or infoBarrier2 == "Aeiyou" or infoBarrier2 == "aeiyou drefael" or infoBarrier2 == "aeiyou":
            # Aeiyou Bio Prompts
            aeiyouProfile = "Aeiyou Drefael\n\nHometown: Volquola\nRace: Majuu (Ocean Blue)\nBirthday: March 9, 4023\nGender: Male\nMagic Affinities\n| Earth\n| Ice\n\nItems\n| Terra Shard\n| Trial Armband\n| Broadsword\n\n"
            aeiyouEarthSpells = "Spells: Earth\n| Earth Wave\n| Stone Barrier\n| Terra Pillar\n| Pact: Terra Sabre\n* Terra Sabre: Omni-Wave\n* Terra Sabre: Mountain Chain\n* Terra Sabre: Combat\n* Terra Sabre: Strike Charge\n| Earth Sink\n\nTerra Sabre: Magic Pact\n| Using his broadsword as a base, Aeiyou can plunge it into the earth to wrap the blade in stone. This makes attacking slower, but he can counter this with more accurate strikes and a far sharper blade. While he uses his pact, he can control his blade without touching it by using magic on the earth on his blade, allowing for both utility and enhanced combat.\n\n"
            aeiyouIceSpells = "Spells: Ice\n| Freeze Field\n| Ice Shards\n| Frost Fire\n| Glacier Seal\n| Ice Slide \n\nPact Combo: Terra-Frost Sabre\n| Aeiyou had the idea of using the withering effect of Frost Fire in conjunction with his pact. By freezing over his blade, he can cause the same withering effect ice magic has on armor with every hit. Though the cold temperature makes the blade even harder, it also makes it more brittle and succeptable to cracks and damage. This isn't imbuing his pact with ice magic, rather adding it to its base effects, which is why it is still considered his pact after using two magic types in tandem.\n\n"

            # Aeiyou Backstory Prompts
            aeiyouBackstory01 = ""

            # Aeiyou Bio Search Commands
            aeiyouChapterPrompt = input(
                aeiyouProfile + "\n" + aeiyouEarthSpells + "\n" + aeiyouIceSpells + "\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n")
            if aeiyouChapterPrompt == "Back" or aeiyouChapterPrompt == "back":
                break
            if aeiyouChapterPrompt == "":
                aeiyouChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if aeiyouChapterPrompt != "Continue" and aeiyouChapterPrompt != "continue" and aeiyouChapterPrompt != "Back" and aeiyouChapterPrompt != "back":
                aeiyouChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Kinto Vareli Bio
        while infoBarrier2 == "Kinto Verali" or infoBarrier2 == "Kinto" or infoBarrier2 == "kinto verali" or infoBarrier2 == "kinto":
            # Kinto Bio Prompts
            kintoProfile = "Kinto Verali\n\nHometown: Volquola\nRace: Majuu (Gray)\nBirthday: January 19, 4017\nGender: Male\nMagic Affinities\n| Earth\n| Fire\n\nItems\n| Trial Armband\n| Terra Shard\n| PockUnity Orb\n\n"
            kintoEarthSpells = "Spells: Earth\n| Quicksand Pit\n| Stalactite Forest\n| Precision Spike\n| Terra Rocket\n| Pact: Earth Hammer\n* Earth Hammer: Quake\n* Earth Hammer: Field Control\n* Earth Hammer: Combat\n* Earth Hammer: Mountain\n* Earth Hammer: Fist Combat\n| Terra Shield\n| Stone Prison\n\nEarth Hammer: Magic Pact\n| Kinto can use his mana to condense the earth into a hammer that he can wield. This hammer carries extreme power, and causes immense damage even without a spell. However, wielding the hammer is incredibly difficult; even for Kinto. Because it is so dense, the hammer is very heavy, and the only way Kinto can use it is to cast his hands and feet in stone as well. This gives him enough power to brace himself while using the weapon and enough strength to swing it.\n\n"
            kintoFireSpells = "Spells: Fire\n| Flame Explosion\n| Ember Shower\n| Fire Emission\n\nPact Combo: Hellflame Hammer\n| Because setting his hammer on fire wasn't sustainable, Kinto made an alternative combination. Because the hammer served as an extention of himself (as near all pacts are), he was able to use the hammer in a very unique way. When he slams it on the ground, he can use the point of impact as an ignition of a chain of explosions that combust in a straight line over a short distance. Fire magic is an extremely useful aspect to Kinto; Earth magic has a very short casting range and limited Kinto to close-range combat. Fire magic combats this and gives him ranged capabilities.\n\n"

            # Kinto Bio Search Commands
            kintoChapterPrompt = input(
                kintoProfile + "\n" + kintoEarthSpells + "\n" + kintoFireSpells + "\nEnter 'Back' to return to Character Selection.\n")
            if kintoChapterPrompt == "Back" or kintoChapterPrompt == "back":
                break
            if kintoChapterPrompt == "":
                kintoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if kintoChapterPrompt != "Continue" and kintoChapterPrompt != "continue" and kintoChapterPrompt != "Back" and kintoChapterPrompt != "back":
                kintoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Amiru Soaren Bio
        while infoBarrier2 == "Amiru Soaren" or infoBarrier2 == "Amiru" or infoBarrier2 == "amiru soaren" or infoBarrier2 == "amiru":
            # Amiru Bio Prompts
            amiruProfile = "Amiru Soaren\n\nHometown: Mezolune\nRace: Terrian, Rabbit (Light Yellow, White)\nBirthday: March 8, 4018\nGender: Female\nMagic Affinities\n| Water\n\nItems\n| Promise Band\n| Aqua Shard\n| PockUnity Orb\n\n"
            amiruWaterSpells = "Spells: Water\n| Aqua Wave\n| Rainwater's Grace\n| Pressure Bolt\n| Water Dragon\n| Rising Geyser\n| Ocean's Flow\n* Ocean's Flow: Rising Geyser\n* Ocean's Flow: Tentacles\n* Ocean's Flow: Twin Dragons\n* Ocean's Flow: Whirlpool\n| Ocean Orbs\n\n"

            # Amiru Bio Search Commands
            amiruChapterPrompt = input(
                amiruProfile + "\n" + amiruWaterSpells + "\nEnter 'Back' to return to Character Selection.\n")
            if amiruChapterPrompt == "Back" or amiruChapterPrompt == "back":
                break
            if amiruChapterPrompt == "":
                amiruChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if amiruChapterPrompt != "Continue" and amiruChapterPrompt != "continue" and amiruChapterPrompt != "Back" and amiruChapterPrompt != "back":
                amiruChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Turcobé Sentai Bio
        while infoBarrier2 == "Turcobe Sentai" or infoBarrier2 == "Turcobe" or infoBarrier2 == "turcobe sentai" or infoBarrier2 == "turcobe" or infoBarrier2 == "Turcobé Sentai" or infoBarrier2 == "Turcobé" or infoBarrier2 == "turcobé sentai" or infoBarrier2 == "turcobé":
            # Turcobé Bio Prompts
            turcobeProfile = "Turcobé Sentai\n\nHometown: Piquaron\nRace: Avian (Black, White)\nBirthday: September 9, 4018\nGender: Male\nMagic Affinities\n| Earth\n\nItems\n| Father's Runebook\n| PockUnity Orb\n| Terra Shard\n\n"
            turcobeEarthSpells = "Spells: Earth\n| Soft Sand\n| Terra Gauntlets\n* Terra Gauntlets: Force Palm\n* Terra Gauntlets: Combat\n| Earth Control\n* Earth Control: Sky Island\n* Earth Control: Pillar\n* Earth Control: Gauntlet Control\n| Terra Dome\n\nTurcobé's Runebook\n| When he first discovered he had magic at the age of 10, Turcobé's father gave him his old runebook that he used to use when he still used magic. This book allows Turcobé to add his own runes to the pages and use them in tandem with his spells. This doesn't count as a pact, however, since it doesn't require any magic to maintain. Because he specializes in Earth Control, a sort of spell style that requires making earth float, his mana runs out exceptionally quickly. Holding up earth has a high mana cost, and by using runes from his book he can circumvent the mana cost.\n\n"

            # Turcobé Bio Search Commands
            turcobeChapterPrompt = input(
                turcobeProfile + "\n" + turcobeEarthSpells + "\nEnter 'Back' to return to Character Selection.\n")
            if turcobeChapterPrompt == "Back" or turcobeChapterPrompt == "back":
                break
            if turcobeChapterPrompt == "":
                turcobeChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if turcobeChapterPrompt != "Continue" and turcobeChapterPrompt != "continue" and turcobeChapterPrompt != "Back" and turcobeChapterPrompt != "back":
                turcobeChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Yumeizu Artilux Bio
        while infoBarrier2 == "Yumeizu Artilux" or infoBarrier2 == "Yumeizu" or infoBarrier2 == "yumeizu artilux" or infoBarrier2 == "yumeizu":
            # Yumeizu Bio Prompts
            yumeizuProfile = "Yumeizu Artilux\n\nHometown: Elendraye\nRace: Terrian, Wolf (White, Sky Blue)\nBirthday: January 21, 4017\nGender: Female\nMagic Affinities\n| Wind\n\nItems\n| PockUnity Orb\n\n"
            yumeizuWindSpells = "Spells: Wind\n| Gale Palm\n| Updraft\n| Scissor Ring\n| Air Body\n* Air Body: Lift\n* Air Body: Pressure Counter\n* Air Body: Shockwave\n* Air Body: Lightfist Combat\n| Zephyr Mines\n| Wind Spear\n| Gale Pretense\n\n"

            # Yumeizu Bio Search Commands
            yumeizuChapterPrompt = input(
                yumeizuProfile + "\n" + yumeizuWindSpells + "\nEnter 'Back' to return to Character Selection.\n")
            if yumeizuChapterPrompt == "Back" or yumeizuChapterPrompt == "back":
                break
            if yumeizuChapterPrompt == "":
                yumeizuChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if yumeizuChapterPrompt != "Continue" and yumeizuChapterPrompt != "continue" and yumeizuChapterPrompt != "Back" and yumeizuChapterPrompt != "back":
                yumeizuChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Character Input Exit Command
        if infoBarrier2 == "Back" or infoBarrier2 == "back":
            infoBarrier1 = "Back"
            break
        if infoBarrier2 == "Leave" or infoBarrier2 == "leave":
            input("Database Search Completed. Please restart program to search again.")
            quit()

    # Intro Exit Command
    if infoBarrier1 == "Leave" or infoBarrier1 == "leave":
        input("Database Search Completed. Please restart program to search again.")
        quit()
    if infoBarrier1 == "Back" or infoBarrier1 == "back":
        infoBarrier1 = "Return"
    else:
        input("The data you have requested has not yet been implemented. Check back in a future release version.")