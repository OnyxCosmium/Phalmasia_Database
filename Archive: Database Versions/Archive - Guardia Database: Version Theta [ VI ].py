
# Introduction
infoBarrier = input("IF YOU HAVE READ THIS PREVIOUSLY: Press enter twice to skip by this prompt and head to the beginning of the official code. Thanks!\n\nHey! If you are reading this, then you are here to test my code. Thanks for agreeing to do this by the way; error checking by someone else's eyes is a huge help.\n\nBy the way, I've set up the code in a way where if you press enter where the computer would look for an input from you, it should tell you that it's looking for an input. Just be sure to type an appropriate prompt in and the code will keep running as normal (I've tried to make the code as forgiving to as many forms of the input as I could. Hopefully that helps.).\n\nAnything that you change on this code cannot affect the final project, so if you do choose to delete anything or change the code in a way you can't rectify, simply recopy the code in the compiler to get back to the original version.\n\nIf you do find a place where the code stops working as intended or grammar or something is off, take a note of it. If the code breaks and leaves you stuck on the screen, press the red button on the far left of the output screen. This will reset the code and make it usable again.\n\nThe way I wrote this code may cause code to run off of the screen. To fix this, select the button directly under the down arrow (it should be on the left side of the screen). It will be called 'Soft Wrap'.\n\nIf this ever happens while you test, reload the page and the issue should fix itself. Sorry for the inconvienience.\n\nFinally, this is a database of characters, events, storylines and powers for which I have conceptualized based off of a webcomic I read. This entire thing is an AU passion project (and to be honest, quite embarrasing to be shared at all).\n\nWhat I'm saying is, please don't judge the work based on the idea, and don't share this code to anyone without my permission.\n\nThanks again for wanting to test this, and welcome to my world.\n")
while infoBarrier == "" or infoBarrier == "Return" or infoBarrier == "return":
    infoBarrier = input(
        "Phalmasia Info Database. Please use the interface to select information.\nChapters:\n| Characters\n| Locations\n| Magic\n| Races\n| History\n\nLeave the database by entering 'Leave'.\n")

    while infoBarrier == "":
        infoBarrier = input("Please Re-enter your database restriction.\n")
    while infoBarrier != "Characters" and infoBarrier != "characters" and infoBarrier != "Locations" and infoBarrier != "locations" and infoBarrier != "Magic" and infoBarrier != "magic" and infoBarrier != "Races" and infoBarrier != "races" and infoBarrier != "History" and infoBarrier != "history" and infoBarrier != "Leave" and infoBarrier != "leave":
        infoBarrier = input("Please Re-enter your database restriction.\n")

    # Character Input Commands
    while infoBarrier == "Characters" or infoBarrier == "characters":
        characterBarrier = input(
            "Characters:\n| Xaeyz Kai\n| Mirago Fynae\n| Yggdrasil (Yggdra) Aensyll\n| Cidelli (Cid) Reimora\n| Mimi Seiran\n| Kimiko Quintai\n| Aeiyou Drefael\n| Kinto Verali\n| Amiru Soaren\n| Turcobé Sentai\n| Yumeizu Artilux\n| Ryner Khabunago\n| Serena Fynae\n\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n")

        while characterBarrier == "":
            characterBarrier = input("Please Re-enter your database restriction.\n")
        while characterBarrier != "Xaeyz Kai" and characterBarrier != "Xaeyz" and characterBarrier != "xaeyz kai" and characterBarrier != "xaeyz" and characterBarrier != "Yggdrasil Aensyll" and characterBarrier != "Yggdra" and characterBarrier != "yggdrasil aensyll" and characterBarrier != "yggdra" and characterBarrier != "Yggdrasil" and characterBarrier != "yggdrasil" and characterBarrier != "Cidelli Reimora" and characterBarrier != "Cid" and characterBarrier != "cidelli reimora" and characterBarrier != "cid" and characterBarrier != "Cidelli" and characterBarrier != "cidelli" and characterBarrier != "Mimi" and characterBarrier != "mimi" and characterBarrier != "Kimiko Quintai" and characterBarrier != "Kimiko" and characterBarrier != "kimiko quintai" and characterBarrier != "kimiko" and characterBarrier != "Aeiyou Drefael" and characterBarrier != "Aeiyou" and characterBarrier != "aeiyou drefael" and characterBarrier != "aeiyou" and characterBarrier != "Kinto Verali" and characterBarrier != "Kinto" and characterBarrier != "kinto verali" and characterBarrier != "kinto" and characterBarrier != "Amiru Soaren" and characterBarrier != "Amiru" and characterBarrier != "amiru soaren" and characterBarrier != "amiru" and characterBarrier != "Turcobe Sentai" and characterBarrier != "Turcobe" and characterBarrier != "turcobe sentai" and characterBarrier != "turcobe" and characterBarrier != "Turcobé Sentai" and characterBarrier != "Turcobé" and characterBarrier != "turcobé sentai" and characterBarrier != "turcobé" and characterBarrier != "Yumeizu Artilux" and characterBarrier != "Yumeizu" and characterBarrier != "yumeizu artilux" and characterBarrier != "yumeizu" and characterBarrier != "Mirago Fynae" and characterBarrier != "Mirago" and characterBarrier != "mirago fynae" and characterBarrier != "mirago" and characterBarrier != "Ryner Khabunago" and characterBarrier != "Ryner" and characterBarrier != "ryner khabunago" and characterBarrier != "ryner" and characterBarrier != "Serena Fynae" and characterBarrier != "Serena" and characterBarrier != "serena fynae" and characterBarrier != "serena" and characterBarrier != "Leave" and characterBarrier != "leave" and characterBarrier != "Back" and characterBarrier != "back":
            characterBarrier = input("Please Re-enter your database restriction.\n")

        # Xaeyz Kai Bio
        while characterBarrier == "Xaeyz Kai" or characterBarrier == "Xaeyz" or characterBarrier == "xaeyz kai" or characterBarrier == "xaeyz":
            # Xaeyz Bio Prompts
            xaeyzProfile = "Xaeyz Kai\n\nHometown: Meteora\nRace: Argen (Black, Gray)\nBirthday: July 7th, 4023\nGender: Male\nPronunciation: Ex-AYZ KAI\nMagic Affinities\n| Wind\n| Gravity\n| Cosmic Wind\n\nItems\n| Aurora Staff\n| eMap\n| SoundCube\n| Gale Shard\n| PockUnity Orb\n| Psychal Library\n| Flyers License\n\nSigil: Sectional, Triagonal\n| Gravity, Bottom Section\n| Wind, Top Right Section\n| Cosmic Wind, Top Left Section\n\n"
            xaeyzWindSpells = "Spells: Wind\n| Cyclone Slice\n| Gale Vacuum\n| Pact: Aurora Scythe\n| Rising Wyrmwind\n* Rising Wyrmwind: Zephyr Flurry\n| Zephyr's Eye\n| Phoenix\n| Phoenix Hybrid\n* Phoenix Hybrid: Feather Control\n* Phoenix Hybrid: Feather Dance\n* Phoenix Hybrid: Gale Drive\n* Phoenix Hybrid: Wing Shield\n* Phoenix Hybrid: Tornado Wave\n| Phoenix Ethereal\n* Phoenix Ethereal: Feather Control\n* Phoenix Ethereal: Feather Dance\n* Phoenix Ethereal: Gale Drive\n* Phoenix Ethereal: Zephyr's Eye\n* Pheonix Ethereal: Draft Expanse\n* Phoenix Ethereal: Zephyr's Scream\n\nAurora Scythe: Magic Pact\n| Xaeyz's staff is made of a special meteor that could channel and amplify magical energy. He later learned to channel the energy through the staff more precisely, and formed a dual-bladed scythe; a weapon that represented his combat style perfectly. This scythe became his magic pact.\n\n"
            xaeyzGravitySpells = "Spells: Gravity\n| Levitation\n* Shift\n| Field\n| Quake\n| Lock\n| Shockwave\n| Impulse\n| Bounce\n| Combat\n\n"
            xaeyzCosmicWindSpells = "Spells: Cosmic Wind\n| Stardust Enhancement\n| Aurora's Grace\n| Meteor Crash\n| Luminous Aurora\n| Cosmic Seal\n| Constellar Ray\n\nAeon: Spirit of the Stars\n| Aeon is the spirit of Cosmic Wind, and the partner of Xaeyz. The only reason Xaeyz can use Cosmic Wind at all is because Aeon is with him. Similar to the other spirits of the mythical elementals, Aeon has no physical form and exists only in Xaeyz's psychal library. This, as a result, gives Xaeyz two active consciences. Aeon is a free soul and lives on trying to keep everyone around him safe while being as free as possible; values similar to Xaeyz's.\n\nPower Event: Aurora Borealis\nFriends: Yes\nAcceptance: Yes\nMagic Use: Permitted\n\n"

            # Xaeyz Backstory Prompts
            # Chapter 1
            xaeyzBackstory01 = "Xaeyz was born with wind magic, an oddity for Argens. As a result, " \
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
            xaeyzBackstory08 = "Xaeyz spent the next few days mourning his friend's loss, but knew he still " \
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
            xaeyzBackstory18 = "Here Xaeyz found a home in a tree he called the Heaven Tree. A wolf, " \
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
                               "Vacuum. This spell, unlike other wind spells, created an absense of air in its radius; a " \
                               "makeshift vacuum. Since fire relies and feeds on air, the flames went out quickly after " \
                               "being engulfed by the attack. Xaeyz had gotten stronger.\n\n"
            xaeyzBackstory21 = "Xaeyz had been keeping tabs on a town nearby the Enchanted Forest called Drəklife since " \
                               "he had arrived. There, he learned of the name the argens from Meteora began to call him: " \
                               "'The Boy of Cosmic Wind'. He preferred the Cosmic Wind User; a boy sounded less cool to " \
                               "him. He was also known as 'The Forest's Shadow' since he had stopped the forest fire. " \
                               "However, two years after the fire, Xaeyz encountered his final challenge: a fire user " \
                               "attaking the town.\n\nEnd of Chapter 3\n"
            # Chapter 4
            xaeyzBackstory22 = "The Avat attacking was known as Hozura the Flame, a man who was being " \
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
                xaeyzProfile + "\n" + xaeyzWindSpells + "\n" + xaeyzGravitySpells + "\n" + xaeyzCosmicWindSpells + "\nEnter 'Chapters' to view the chapters of Xaeyz's Backstory. Enter 'Back' to return to Character Selection.\n")
            while xaeyzChapterPrompt == "Chapters" or xaeyzChapterPrompt == "chapters":
                xaeyzChapterPrompt = input(
                    "Xaeyz's Backstory\nPlease enter the chapter number to see a chapter (Chapter 1)\n\n| Chapter 1: The Day of Black Sun\n| Chapter 2: The Aurora Scythe\n| Chapter 3: The Forest's Shadow\n| Chapter 4: Hozura the Flame\n\nEnter 'Bio' to return to Xaeyz's Biography.\n")

                if xaeyzChapterPrompt == "Bio" or xaeyzChapterPrompt == "bio":
                    break
                if xaeyzChapterPrompt == "":
                    xaeyzChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if xaeyzChapterPrompt != "Chapters" and xaeyzChapterPrompt != "chapters" and xaeyzChapterPrompt != "Chapter 1" and xaeyzChapterPrompt != "chapter 1" and xaeyzChapterPrompt != "Chapter One" and xaeyzChapterPrompt != "chapter One" and xaeyzChapterPrompt != "Chapter one" and xaeyzChapterPrompt != "chapter one" and xaeyzChapterPrompt != "Chapter 2" and xaeyzChapterPrompt != "chapter 2" and xaeyzChapterPrompt != "Chapter Two" and xaeyzChapterPrompt != "chapter Two" and xaeyzChapterPrompt != "Chapter two" and xaeyzChapterPrompt != "chapter two" and xaeyzChapterPrompt != "Chapter 3" and xaeyzChapterPrompt != "chapter 3" and xaeyzChapterPrompt != "Chapter Three" and xaeyzChapterPrompt != "chapter Three" and xaeyzChapterPrompt != "Chapter three" and xaeyzChapterPrompt != "chapter three" and xaeyzChapterPrompt != "Chapter 4" and xaeyzChapterPrompt != "chapter 4" and xaeyzChapterPrompt != "Chapter Four" and xaeyzChapterPrompt != "chapter Four" and xaeyzChapterPrompt != "Chapter four" and xaeyzChapterPrompt != "chapter four" and xaeyzChapterPrompt != "Back" and xaeyzChapterPrompt != "back" and xaeyzChapterPrompt != "":
                    xaeyzChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

                xaeyzChapterOne = ""
                xaeyzChapterTwo = ""
                xaeyzChapterThree = ""
                xaeyzChapterFour = ""
                if xaeyzChapterPrompt == "Chapter 1" or xaeyzChapterPrompt == "chapter 1" or xaeyzChapterPrompt == "Chapter One" or xaeyzChapterPrompt == "chapter One" or xaeyzChapterPrompt == "Chapter one" or xaeyzChapterPrompt == "chapter one":
                    xaeyzChapterOne = input(
                        "Chapter 1: The Day of Black Sun\n\n" + xaeyzBackstory01 + "\n" + xaeyzBackstory02 + "\n" + xaeyzBackstory03 + "\n" + xaeyzBackstory04 + "\n" + xaeyzBackstory05 + "\n" + xaeyzBackstory06 + "\n" + xaeyzBackstory07 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n")
                if xaeyzChapterPrompt == "Chapter 2" or xaeyzChapterPrompt == "chapter 2" or xaeyzChapterPrompt == "Chapter Two" or xaeyzChapterPrompt == "chapter Two" or xaeyzChapterPrompt == "Chapter two" or xaeyzChapterPrompt == "chapter two" or xaeyzChapterOne == "Next" or xaeyzChapterOne == "next":
                    xaeyzChapterTwo = input(
                        "Chapter 2: The Aurora Scythe\n\n" + xaeyzBackstory08 + "\n" + xaeyzBackstory09 + "\n" + xaeyzBackstory10 + "\n" + xaeyzBackstory11 + "\n" + xaeyzBackstory12 + "\n" + xaeyzBackstory13 + "\n" + xaeyzBackstory14 + "\n" + xaeyzBackstory15 + "\n" + xaeyzBackstory16 + "\n" + xaeyzBackstory17 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n")
                if xaeyzChapterPrompt == "Chapter 3" or xaeyzChapterPrompt == "chapter 3" or xaeyzChapterPrompt == "Chapter Three" or xaeyzChapterPrompt == "chapter Three" or xaeyzChapterPrompt == "Chapter three" or xaeyzChapterPrompt == "chapter three" or xaeyzChapterTwo == "Next" or xaeyzChapterTwo == "next":
                    xaeyzChapterThree = input(
                        "Chapter 3: The Forest's Shadow\n\n" + xaeyzBackstory18 + "\n" + xaeyzBackstory19 + "\n" + xaeyzBackstory20 + "\n" + xaeyzBackstory21 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n")
                if xaeyzChapterPrompt == "Chapter 4" or xaeyzChapterPrompt == "chapter 4" or xaeyzChapterPrompt == "Chapter Four" or xaeyzChapterPrompt == "chapter Four" or xaeyzChapterPrompt == "Chapter four" or xaeyzChapterPrompt == "chapter four" or xaeyzChapterThree == "Next" or xaeyzChapterThree == "next":
                    xaeyzChapterFour = input(
                        "Chapter 4: Hozura the Flame\n\n" + xaeyzBackstory22 + "\n" + xaeyzBackstory23 + "\n" + xaeyzBackstory24 + "\n" + xaeyzBackstory25 + "\n" + xaeyzBackstory26 + "\n" + xaeyzBackstory27 + "\n" + xaeyzBackstory28 + "\n" + xaeyzBackstory29 + "\n\nThis is the end of Xaeyz's Bio. Press 'Enter' to return to chapter selection.\n")
                if xaeyzChapterOne == "" or xaeyzChapterTwo == "" or xaeyzChapterThree == "" or xaeyzChapterFour == "":
                    xaeyzChapterPrompt = "Chapters"
                if xaeyzChapterOne != "Chapters" and xaeyzChapterOne != "chapters" and xaeyzChapterOne != "" and xaeyzChapterTwo != "Chapters" and xaeyzChapterTwo != "chapters" and xaeyzChapterTwo != "" and xaeyzChapterThree != "Chapters" and xaeyzChapterThree != "chapters" and xaeyzChapterThree != "" and xaeyzChapterFour != "Chapters" and xaeyzChapterFour != "chapters" and xaeyzChapterFour != "":
                    xaeyzChapterOne = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

            if xaeyzChapterPrompt == "Back" or xaeyzChapterPrompt == "back":
                break
            if xaeyzChapterPrompt == "":
                xaeyzChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if xaeyzChapterPrompt != "Chapters" and xaeyzChapterPrompt != "chapters" and xaeyzChapterPrompt != "Back" and xaeyzChapterPrompt != "back" and xaeyzChapterPrompt != "Bio" and xaeyzChapterPrompt != "bio" and xaeyzChapterPrompt != "":
                xaeyzChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Mirago Fynae Bio
        while characterBarrier == "Mirago Fynae" or characterBarrier == "Mirago" or characterBarrier == "mirago fynae" or characterBarrier == "mirago":
            # Mirago Bio Prompts
            miragoProfile = "Mirago Fynae\n\nHometown: Meteora\nRace: Argen (Blue, Black)\nBirthday: June 15, 4023\nGender: Male\nPronunciation: ME-rah-goh FAI-nay\nMagic Affinities\n| Fire\n| Onyx Fire\n| Life\n\nItems\n| Psychal Grotto\n| Cloak of Shadows\n| Rune Bracelet\n\nSigil: Sectional, Circle\n| Fire, Left Section\n| Onyx Fire, Right Section\n\n"
            miragoFireSpells = "Spells: Fire\n| Dragon Flame Bombs\n| Flash Palm\n| Flame Heatwave\n| Pact: Pyre Bow\n| Inferno\n* Inferno: Drive\n| Combustion Stars\n| Dracunity\n| Dracunity Halflife\n* Dracunity Halflife: Scale Shot\n* Dracunity Halflife: Dragon Rush\n* Dracunity Halflife: Combustion Chain\n* Dracunity Halflife: Scale Mines\n* Dragunity Halflife: Tail Embers\n* Dracunity Halflife: Eye of Ancients\n| Dracunity Possesion\n* Dracunity Possesion: Dragon Rush\n* Dracunity Possesion: Dragon Flame Bombs\n* Dracunity Possesion: Infernal Roar\n* Dracunity Possesion: Eye of Ancients\n* Dracunity Possesion: Tail Embers\n* Dracunity Possesion: Magestic Incineration\n\nPyre Bow: Magic Pact\n| Mirago's pact perfectly represents his calm, ambitious and shy nature. By extending his pinky and thumb on his hand, he can create elongated flame structures from his fingertips and bind them with a string made of flame. This allows him to conjure fire arrows and other flame projectiles with his magic and fire them at his enemies. He can give the flames different properties to increase their utility.\n\n"
            miragoLifeSpells = "Spells: Life\n| Eternal Life\n| Karma's Judgement\n| Absorbtion\n| Soul Reflux\n| Contact Drain\n\n"
            miragoOnyxFireSpells = "Spells: Onyx Fire\n| Midnight Combustion\n| Onyx Ignition\n| Compression Burst\n| Hellflame Pillars\n| Kindling Rend\n\nArc: Spirit of the Sun\n| Arc is the spirit of Onyx Fire, and the partner of Mirago. The only reason Mirago can use Onyx Fire at all is because Arc is with him. Like the other mythical elementals, Arc has no physical form and abides solely in Mirago's psychal grotto. Arc is an ambitious and dedicated soul who tries to keep to those he trusts close and always strives to become stronger with his friends; values nearly identical to Mirago's.\n\nPower Event: Solar Storm\nFriends: Yes\nAcceptance: Yes\nMagic Use: Permitted\n\n"

            # Mirago Backstory Prompts
            # Chapter 1
            miragoBackstory01 = "Mirago loved magic. His dad was a fire user, and though not a " \
                                "guardian, still did his best to protect those in Meteora. He never knew his mom; she " \
                                "died shortly after his sister was born. Mirago looked up to him and awaited the day " \
                                "that he could get his own magic, and he finally got it on his fifth birthday. " \
                                "However, something was strange about his magic when he first used it; instead of " \
                                "being reddish-orange, they were a deep black. He thought that this was incredible " \
                                "and showed his sister, Lea. She was amazed, too, and she frequently went to Duskfaze " \
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
                                "They learned that if Mirago used his flames and Xaeyz used his wind, " \
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
                miragoProfile + "\n" + miragoFireSpells + "\n" + miragoLifeSpells + "\n" + miragoOnyxFireSpells + "\nEnter 'Chapters' to view the chapters of Mirago's Backstory. Enter 'Back' to return to Character Selection.\n")
            while miragoChapterPrompt == "Chapters" or miragoChapterPrompt == "chapters":
                miragoChapterPrompt = input(
                    "Mirago's Backstory\nPlease enter the chapter number to see a chapter (Chapter 1)\n\n| Chapter 1: Onyx Fire\n| Chapter 2: Meeting Xaeyz\n| Chapter 3: A Final Stand\n| Chapter 4: Rebirth\n\nEnter 'Bio' to return to Mirago's Biography.\n")

                if miragoChapterPrompt == "Bio" or miragoChapterPrompt == "bio":
                    break
                if miragoChapterPrompt == "":
                    miragoChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if miragoChapterPrompt != "Chapters" and miragoChapterPrompt != "chapters" and miragoChapterPrompt != "Chapter 1" and miragoChapterPrompt != "chapter 1" and miragoChapterPrompt != "Chapter One" and miragoChapterPrompt != "chapter One" and miragoChapterPrompt != "Chapter one" and miragoChapterPrompt != "chapter one" and miragoChapterPrompt != "Chapter 2" and miragoChapterPrompt != "chapter 2" and miragoChapterPrompt != "Chapter Two" and miragoChapterPrompt != "chapter Two" and miragoChapterPrompt != "Chapter two" and miragoChapterPrompt != "chapter two" and miragoChapterPrompt != "Chapter 3" and miragoChapterPrompt != "chapter 3" and miragoChapterPrompt != "Chapter Three" and miragoChapterPrompt != "chapter Three" and miragoChapterPrompt != "Chapter three" and miragoChapterPrompt != "chapter three" and miragoChapterPrompt != "Chapter 4" and miragoChapterPrompt != "chapter 4" and miragoChapterPrompt != "Chapter Four" and miragoChapterPrompt != "chapter Four" and miragoChapterPrompt != "Chapter four" and miragoChapterPrompt != "chapter four" and miragoChapterPrompt != "Back" and miragoChapterPrompt != "back" and miragoChapterPrompt != "":
                    miragoChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

                miragoChapterOne = ""
                miragoChapterTwo = ""
                miragoChapterThree = ""
                miragoChapterFour = ""
                if miragoChapterPrompt == "Chapter 1" or miragoChapterPrompt == "chapter 1" or miragoChapterPrompt == "Chapter One" or miragoChapterPrompt == "chapter One" or miragoChapterPrompt == "Chapter one" or miragoChapterPrompt == "chapter one":
                    miragoChapterOne = input(
                        "Chapter 1: Onyx Fire\n\n" + miragoBackstory01 + "\n" + miragoBackstory02 + "\n" + miragoBackstory03 + "\n" + miragoBackstory04 + "\n" + miragoBackstory05 + "\n" + miragoBackstory06 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n")
                if miragoChapterPrompt == "Chapter 2" or miragoChapterPrompt == "chapter 2" or miragoChapterPrompt == "Chapter Two" or miragoChapterPrompt == "chapter Two" or miragoChapterPrompt == "Chapter two" or miragoChapterPrompt == "chapter two" or miragoChapterOne == "Next" or miragoChapterOne == "next":
                    miragoChapterTwo = input(
                        "Chapter 2: Meeting Xaeyz\n\n" + miragoBackstory07 + "\n" + miragoBackstory08 + "\n" + miragoBackstory09 + "\n" + miragoBackstory10 + "\n" + miragoBackstory11 + "\n" + miragoBackstory12 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n")
                if miragoChapterPrompt == "Chapter 3" or miragoChapterPrompt == "chapter 3" or miragoChapterPrompt == "Chapter Three" or miragoChapterPrompt == "chapter Three" or miragoChapterPrompt == "Chapter three" or miragoChapterPrompt == "chapter three" or miragoChapterTwo == "Next" or miragoChapterTwo == "next":
                    miragoChapterThree = input(
                        "Chapter 3: A Final Stand\n\n" + miragoBackstory13 + "\n" + miragoBackstory14 + "\n" + miragoBackstory15 + "\n" + miragoBackstory16 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n")
                if miragoChapterPrompt == "Chapter 4" or miragoChapterPrompt == "chapter 4" or miragoChapterPrompt == "Chapter Four" or miragoChapterPrompt == "chapter Four" or miragoChapterPrompt == "Chapter four" or miragoChapterPrompt == "chapter four" or miragoChapterThree == "Next" or miragoChapterThree == "next":
                    miragoChapterFour = input(
                        "Chapter 4: Rebirth\n\n" + miragoBackstory17 + "\n" + miragoBackstory18 + "\n" + miragoBackstory19 + "\n" + miragoBackstory20 + "\n" + miragoBackstory21 + "\n\nThis is the end of Mirago's Bio. Press 'Enter' to return to chapter selection.\n")
                if miragoChapterOne == "" or miragoChapterTwo == "" or miragoChapterThree == "" or miragoChapterFour == "":
                    miragoChapterPrompt = "Chapters"
                if miragoChapterOne != "Chapters" and miragoChapterOne != "chapters" and miragoChapterOne != "" and miragoChapterTwo != "Chapters" and miragoChapterTwo != "chapters" and miragoChapterTwo != "" and miragoChapterThree != "Chapters" and miragoChapterThree != "chapters" and miragoChapterThree != "" and miragoChapterFour != "Chapters" and miragoChapterFour != "chapters" and miragoChapterFour != "":
                    miragoChapterOne = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

            if miragoChapterPrompt == "Back" or miragoChapterPrompt == "back":
                break
            if miragoChapterPrompt == "":
                miragoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if miragoChapterPrompt != "Continue" and miragoChapterPrompt != "continue" and miragoChapterPrompt != "Bio" and miragoChapterPrompt != "bio" and miragoChapterPrompt != "Back" and miragoChapterPrompt != "back":
                miragoChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Yggdrasil Aensyll Bio
        while characterBarrier == "Yggdrasil Aensyll" or characterBarrier == "Yggdra" or characterBarrier == "yggdrasil aensyll" or characterBarrier == "yggdra" or characterBarrier == "Yggdrasil" or characterBarrier == "yggdrasil":
            # Yggdra Bio Prompts
            yggdraProfile = "Yggdrasil (Yggdra) Aensyll\n\nHometown: Ashford\nRace: Terrian (Fox)\nBirthday: December 17, 4023\nGender: Female\nPronunciation: EEG-dra-seel AYN-seel\nMagic Affinities\n| Wind\n\nItems\n| Gale Shard\n| PockUnity Orb\n| Frinrir's Hat\n| Frinrir's Jacket\n| Flyers License\n\n"
            yggdraWindSpells = "Spells: Wind\n| Gale Impact\n| Cutting Spiral\n| Pact: Zephyr\n* Zephyr: Shield\n* Zephyr: Barrier\n* Zephyr: Reflection\n* Zephyr: Tag-Team\n| Breeze Gems\n* Breeze Gems: Darts\n* Breeze Gems: Ring\n* Breeze Gems: Emblem\n\nZephyr: Spirit Pact\n| Zephyr is a spirit pact formed from her dead brother's (Frinrir) remaining mana and will. As her pact, Zephyr takes the form of a shield, symbolizing the will to protect Yggdra. He also takes his sprite form to assist Yggdra in casting unique spells. The bond that Yggdra and Zephyr share is deep, and that bond is what makes their duo so strong.\n\n"

            # Yggdra Backstory Prompts
            # Chapter 1
            yggdraBackstory01 = "Yggdra had always been fascinated by magic. Her mother waas once a " \
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
            yggdraBackstory09 = "Yggdra and Kiyo were outside throwing a ball around in Yggdra's yard when " \
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
            yggdraBackstory14 = "Alexis woke up a few hours later and saw Yggdra and Frinrir. Of course, " \
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
            yggdraBackstory18 = "Yggdra spent the next four years in her room thinking about what to do " \
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
                yggdraProfile + "\n" + yggdraWindSpells + "\nEnter 'Chapters' to view the chapters of Yggdra's Backstory. Enter 'Back' to return to Character Selection.\n")
            while yggdraChapterPrompt == "Chapters" or yggdraChapterPrompt == "chapters":
                yggdraChapterPrompt = input(
                    "Yggdra's Backstory\nPlease enter the chapter number to see a chapter (Chapter 1)\n\n| Chapter 1: A Time for Firsts & Lasts\n| Chapter 2: A Goodbye\n| Chapter 3: A Darkened Mind\n| Chapter 4: New Dreams\n\nEnter 'Bio' to return to yggdra's Biography.\n")

                if yggdraChapterPrompt == "Bio" or yggdraChapterPrompt == "bio":
                    break
                if yggdraChapterPrompt == "":
                    yggdraChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if yggdraChapterPrompt != "Chapters" and yggdraChapterPrompt != "chapters" and yggdraChapterPrompt != "Chapter 1" and yggdraChapterPrompt != "chapter 1" and yggdraChapterPrompt != "Chapter One" and yggdraChapterPrompt != "chapter One" and yggdraChapterPrompt != "Chapter one" and yggdraChapterPrompt != "chapter one" and yggdraChapterPrompt != "Chapter 2" and yggdraChapterPrompt != "chapter 2" and yggdraChapterPrompt != "Chapter Two" and yggdraChapterPrompt != "chapter Two" and yggdraChapterPrompt != "Chapter two" and yggdraChapterPrompt != "chapter two" and yggdraChapterPrompt != "Chapter 3" and yggdraChapterPrompt != "chapter 3" and yggdraChapterPrompt != "Chapter Three" and yggdraChapterPrompt != "chapter Three" and yggdraChapterPrompt != "Chapter three" and yggdraChapterPrompt != "chapter three" and yggdraChapterPrompt != "Chapter 4" and yggdraChapterPrompt != "chapter 4" and yggdraChapterPrompt != "Chapter Four" and yggdraChapterPrompt != "chapter Four" and yggdraChapterPrompt != "Chapter four" and yggdraChapterPrompt != "chapter four" and yggdraChapterPrompt != "Back" and yggdraChapterPrompt != "back" and yggdraChapterPrompt != "":
                    yggdraChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

                yggdraChapterOne = ""
                yggdraChapterTwo = ""
                yggdraChapterThree = ""
                yggdraChapterFour = ""
                if yggdraChapterPrompt == "Chapter 1" or yggdraChapterPrompt == "chapter 1" or yggdraChapterPrompt == "Chapter One" or yggdraChapterPrompt == "chapter One" or yggdraChapterPrompt == "Chapter one" or yggdraChapterPrompt == "chapter one":
                    yggdraChapterOne = input(
                        "Chapter 1: A Time for Firsts & Lasts\n\n" + yggdraBackstory01 + "\n" + yggdraBackstory02 + "\n" + yggdraBackstory03 + "\n" + yggdraBackstory04 + "\n" + yggdraBackstory05 + "\n" + yggdraBackstory06 + "\n" + yggdraBackstory07 + "\n" + yggdraBackstory08 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n")
                if yggdraChapterPrompt == "Chapter 2" or yggdraChapterPrompt == "chapter 2" or yggdraChapterPrompt == "Chapter Two" or yggdraChapterPrompt == "chapter Two" or yggdraChapterPrompt == "Chapter two" or yggdraChapterPrompt == "chapter two" or yggdraChapterOne == "Next" or yggdraChapterOne == "next":
                    yggdraChapterTwo = input(
                        "Chapter 2: A Goodbye\n\n" + yggdraBackstory09 + "\n" + yggdraBackstory10 + "\n" + yggdraBackstory11 + "\n" + yggdraBackstory12 + "\n" + yggdraBackstory13 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 3.\n")
                if yggdraChapterPrompt == "Chapter 3" or yggdraChapterPrompt == "chapter 3" or yggdraChapterPrompt == "Chapter Three" or yggdraChapterPrompt == "chapter Three" or yggdraChapterPrompt == "Chapter three" or yggdraChapterPrompt == "chapter three" or yggdraChapterTwo == "Next" or yggdraChapterTwo == "next":
                    yggdraChapterThree = input(
                        "Chapter 3: A Darkened Mind\n\n" + yggdraBackstory14 + "\n" + yggdraBackstory15 + "\n" + yggdraBackstory16 + "\n" + yggdraBackstory17 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 4.\n")
                if yggdraChapterPrompt == "Chapter 4" or yggdraChapterPrompt == "chapter 4" or yggdraChapterPrompt == "Chapter Four" or yggdraChapterPrompt == "chapter Four" or yggdraChapterPrompt == "Chapter four" or yggdraChapterPrompt == "chapter four" or yggdraChapterThree == "Next" or yggdraChapterThree == "next":
                    yggdraChapterFour = input(
                        "Chapter 4: New Dreams\n\n" + yggdraBackstory18 + "\n" + yggdraBackstory19 + "\n" + yggdraBackstory20 + "\n" + yggdraBackstory21 + "\n\nThis is the end of Yggdra's Bio. Press 'Enter' to return to chapter selection.\n")
                if yggdraChapterOne == "" or yggdraChapterTwo == "" or yggdraChapterThree == "" or yggdraChapterFour == "":
                    yggdraChapterPrompt = "Chapters"
                if yggdraChapterOne != "Chapters" and yggdraChapterOne != "chapters" and yggdraChapterOne != "" and yggdraChapterTwo != "Chapters" and yggdraChapterTwo != "chapters" and yggdraChapterTwo != "" and yggdraChapterThree != "Chapters" and yggdraChapterThree != "chapters" and yggdraChapterThree != "" and yggdraChapterFour != "Chapters" and yggdraChapterFour != "chapters" and yggdraChapterFour != "":
                    yggdraChapterOne = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

            if yggdraChapterPrompt == "Back" or yggdraChapterPrompt == "back":
                break
            if yggdraChapterPrompt == "":
                yggdraChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if yggdraChapterPrompt != "Continue" and yggdraChapterPrompt != "continue" and yggdraChapterPrompt != "Bio" and yggdraChapterPrompt != "bio" and yggdraChapterPrompt != "Back" and yggdraChapterPrompt != "back":
                yggdraChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Cidelli Reimora Bio
        while characterBarrier == "Cidelli Reimora" or characterBarrier == "Cid" or characterBarrier == "cidelli reimora" or characterBarrier == "cid" or characterBarrier == "Cidelli" or characterBarrier == "cidelli":
            # Cid Bio Prompts
            cidProfile = "Cidelli (Cid) Reimora\n\nHometown: Oshborne\nRace: Terrian, Sheep (Black Fur/Skin)\nBirthday: October 2, 4023\nGender: Female\nPronunciation: Cid-EL-ee Ray-MORE-ah\nMagic Affinities\n| Lightning\n\nItems\n| Bolt Shard\n| Mom's Pendant\n\n"
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
        while characterBarrier == "Mimi Seiran" or characterBarrier == "Mimi" or characterBarrier == "Mimi seiran" or characterBarrier == "mimi":
            # Mimi Bio Prompts
            mimiProfile = "Mimi Seiran\n\nHometown: Cilfier\nRace: Terrian, Tanuki(Light Brown with Brown Spots)\nBirthday: March 25, 4020\nGender: Female\nPronunciation: ME-me Say-ren\nMagic Affinities\n| Water\n\nItems\n| Aqua Shard\n| PockUnity Orb\n\n"
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
        while characterBarrier == "Kimiko Quintai" or characterBarrier == "Kimiko" or characterBarrier == "kimiko quintai" or characterBarrier == "kimiko":
            # Kimiko Bio Prompts
            kimikoProfile = "Kimiko Quintai\n\nHometown: Skykumo\nRace: Avat (Blue, Black)\nBirthday: June 16, 4023\nGender: Male\nPronunciation: KI-me-koh KWIN-tie\nMagic Affinities\n| Fire\n\nItems\n| Flame Shard\n| Featherband\n| PockUnity Orb\n\n"
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
        while characterBarrier == "Aeiyou Drefael" or characterBarrier == "Aeiyou" or characterBarrier == "aeiyou drefael" or characterBarrier == "aeiyou":
            # Aeiyou Bio Prompts
            aeiyouProfile = "Aeiyou Drefael\n\nHometown: Volquöla\nRace: Majuu (Ocean Blue)\nBirthday: March 9, 4023\nGender: Male\nPronunciation: AY-you DREE-fail\nMagic Affinities\n| Earth\n| Ice\n\nItems\n| Terra Shard\n| Trial Armband\n| Broadsword\n\nSigil: Unity, Diamond\n\n"
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
        while characterBarrier == "Kinto Verali" or characterBarrier == "Kinto" or characterBarrier == "kinto verali" or characterBarrier == "kinto":
            # Kinto Bio Prompts
            kintoProfile = "Kinto Verali\n\nHometown: Volquöla\nRace: Majuu (Gray)\nBirthday: January 19, 4017\nGender: Male\nPronunciation: KEEN-toe var-EL-ee\nMagic Affinities\n| Earth\n| Fire\n\nItems\n| Trial Armband\n| Terra Shard\n| PockUnity Orb\n\nSigil: Unity, Square\n\n"
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
        while characterBarrier == "Amiru Soaren" or characterBarrier == "Amiru" or characterBarrier == "amiru soaren" or characterBarrier == "amiru":
            # Amiru Bio Prompts
            amiruProfile = "Amiru Soaren\n\nHometown: Mezolune\nRace: Terrian, Rabbit (Light Yellow, White)\nBirthday: March 8, 4018\nGender: Female\nPronunciation: AM-i-roo soar-en\nMagic Affinities\n| Water\n\nItems\n| Promise Band\n| Aqua Shard\n| PockUnity Orb\n\n"
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
        while characterBarrier == "Turcobe Sentai" or characterBarrier == "Turcobe" or characterBarrier == "turcobe sentai" or characterBarrier == "turcobe" or characterBarrier == "Turcobé Sentai" or characterBarrier == "Turcobé" or characterBarrier == "turcobé sentai" or characterBarrier == "turcobé":
            # Turcobé Bio Prompts
            turcobeProfile = "Turcobé Sentai\n\nHometown: Piquaron\nRace: Avat (Black, White)\nBirthday: September 9, 4018\nGender: Male\nPronunciation: tur-CO-bay sen-tie\nMagic Affinities\n| Earth\n\nItems\n| Father's Runebook\n| PockUnity Orb\n| Terra Shard\n\n"
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
        while characterBarrier == "Yumeizu Artilux" or characterBarrier == "Yumeizu" or characterBarrier == "yumeizu artilux" or characterBarrier == "yumeizu":
            # Yumeizu Bio Prompts
            yumeizuProfile = "Yumeizu Artilux\n\nHometown: Elendraye\nRace: Terrian, Wolf (White, Sky Blue)\nBirthday: January 21, 4017\nGender: Female\nPronunciation: you-MAY-zoo ART-ill-ux\nMagic Affinities\n| Wind\n\nItems\n| PockUnity Orb\n\n"
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

        # Ryner Khabunago Bio
        while characterBarrier == "Ryner Khabunago" or characterBarrier == "Ryner" or characterBarrier == "ryner khabunago" or characterBarrier == "ryner":
            # Ryner Bio Prompts
            rynerProfile = "Ryner Khabunago\n\nHometown: ???\nRace: ???\nBirthday: October 13, 3442\nGender: ???\nPronunciation: RYE-ner ka-bun-AH-goh\nMagic Affinities\n| Lightning\n| Shadow\n| Electron Lightning\n\nItems\n| Pendant of the Gatekeeper's Shadow\n\nSigil: Unity, Square\n\n"
            rynerLightningSpells = "Spells: Lightning\n| Stun Clap\n| Electro Fence\n| Lightning Slice\n| Pact: Voltaic Falchion\n| Lightning Strike\n| Electro Dash\n| Raiju\n| Raijū Cloak\n* Raijū Cloak: Eye of the Mythics\n* Raijū Cloak: Tail Guard\n* Raijū Cloak: Storm Summon\n* Raijū Cloak: Thunderclap Strike\n* Raijū Cloak: Tail Concentration\n* Raijū Cloak: Polarize\n| Raijū Emergence\n* Raijū Emergence: Storm Summon\n* Raijū Emergence: Tail Guard\n* Raijū Emergence: Tail Concentration\n* Raijū Emergence: Eye of the Mythics\n* Raijū Emergence: Stunning Roar\n* Raijū Emergence: Zeus' Tail\n* Raijū Emergence: Nabuga's Squall\n\nVoltaic Falchion: Magic Pact\n| Ryner uses his lightning magic, as well as his fixation on power, to shape his lightning into a solid, sharpened mass called a falchion. Because of its composition of lightning magic, it has special properties. It is able to phase through defenses as well as perform instant strikes by using lightning magic. He can also section it by cutting the blade and binding it back together with a bolt of lightning. This allows it to act like a whip. By polarizing it with his Raijū Cloak, he can control it from a distance as a boomerang-like weapon, as well as constant rotation for improved offense and defense.\n\n"
            rynerShadowSpells = "Spells: Shadow\n| Shadow Sneak\n| Umbra Tendrils\n* Umbra Tendrils: Strike\n* Umbra Tendrils: Bind\n| Draining Silhouette\n| Shade Paralysis\n| Gloom Clones\n\n"
            rynerElectronLightningSpells = "Spells: Electron Lightning\n| Ashen Devastation\n| Atomic Emission\n| Electron Disassembly\n| Inferno Bolt\n| Augmented Reflex\n\nNova: Spirit of the Skies\n| Nova is the spirit of Electron Lightning, and Ryner's unwilling partner. The only reason Ryner can use Electron Lightning at all is because Nova is with him. Similar to the other mythical elementals, Nova doesn't have a physical form and resides solely in Nova's psychal graveyard. Nova is a timid and tranquil soul who will protect his friends at any cost. Nova acts only in self-defense, and violence is only a last resort; values that are stark opposites of Ryner's.\n\nPower Event: Charged Cumulonimbi\nFriends: No\nAcceptance: No\nMagic Use: Prohibited\n\n"

            # Ryner Backstory Prompts
            # Chapter 1
            rynerBackstory01 = "Ryner grew up a normal childhood as a Khabunago; a family of " \
                               "grave-watchers that oversaw graveyards across Phalmasia. The duty of the " \
                               "Khabunagos at these graveyards was to protect the bodies of the magic users kept " \
                               "there. They didn't watch over all graves; just the ones where the exceptionally " \
                               "powerful were buried so that anyone who wanted to try to take their strength weren't " \
                               "successful. They believed these powers are owned by those who grew, evolved, " \
                               "and originally wielded them, dead or alive.\n\n "
            rynerBackstory02 = "The head of the family is decided by a rare trait that only Khabunagos have access " \
                               "to: shadow magic. Throughout their time guarding the dead, their ancestors learned " \
                               "how to use the power of the dark to their advantage, and those who wield it are " \
                               "thought to have a stronger connection to them than others. Both Ryner's mother and " \
                               "father had the ability, and it was strongly believed that Ryner would posess the " \
                               "power as well. Ryner spent years practicing his lightning magic with his father when " \
                               "he had the time.\n\n "
            rynerBackstory03 = "Ryner grew up happy with his family. He trained day and night, honing his skill in " \
                               "his magic with other children in his family and awaiting the day that he could begin " \
                               "guarding the graves like his parents. He quickly became the strongest of his friends, " \
                               "and was respected throughout the family. When he was ten, a day came that turned his " \
                               "whole life upside down, and gave him the moment that ended up defining his future: " \
                               "the day the Guardians came.\n\n "
            rynerBackstory04 = "Ryner was out training with his dad, Larein, helping him master a spell he had been " \
                               "practicing. During this, guardians approached Ryner's father and asked if they could " \
                               "speak in private. He said it ws alright and send Ryner back to the house. But of " \
                               "course, Ryner wanted to know what they were talking about, so he hid out of sight and " \
                               "listened in. The guardians told his father that he was uder arrest for killing an " \
                               "intuder in the graveyard. Larein said that he didn't hurt anyone, and that no one had " \
                               "broken in recently, but the guardians didn't believe him.\n\n "
            rynerBackstory05 = "The guardians said that someone had died from injuries sustained after a Khabunago " \
                               "attacked them while they visited their grandparent's grave to pay them respects. " \
                               "Again, Larein denies that he or his wife have seen anyone intruding on the graveyard " \
                               "in the past month. The guardians became increasingly annoyed, and soon, they began to " \
                               "try to take him by force. Larein used his shadow magic to paralyze the guardians, " \
                               "insisting that he didn't want to fight. They didn't seem to care, though, " \
                               "and when Larein released them, they continued their attack.\n\n "
            rynerBackstory06 = "The ice magic user had whittled down his armor very quickly. The problem was that " \
                               "Larein couldn't fight back. He couldn't hurt the guardians since he knew he didn't " \
                               "hurt anyone, and didn't want to give them a reason to send him away from his family. " \
                               "He was dodging and blocking attacks well, but the lightning guardian landed a blow, " \
                               "stunning him and sending him to the ground. It wasn't a powerful blast, but the stun " \
                               "kept him on the ground long enough for the wind user to place a powerful slice " \
                               "through his neck.\n\n "
            rynerBackstory07 = "Ryner gasped, tears beginning to flow from his eyes, and ran back to his house to " \
                               "check on his mom. If they came after his dad, then his mom was in danger, " \
                               "too. He raced home using his magic and burst through the door. He found his mother on " \
                               "the floor, the light lost from her eyes. She was dead. The guardians who had killed " \
                               "her emerged and attacked him. Ryner exploded with a mana he had never felt before, " \
                               "and struck at his assailant so quickly it was as if he'd never moved. This is when " \
                               "Ryner gained Electron Lightning.\n\nEnd of Chapter 1\n "

            # Chapter 2
            rynerBackstory08 = "Ryner, seething with anger, went back to the guardians who had killed " \
                               "his father and as fast as he had the first time, took their lives. Once he had done " \
                               "it, he calmed down and realized what he had done. Ryner never meant to take their " \
                               "lives; he just wanted to scare them and make them feel what he felt. He was paralyzed " \
                               "for a few minutes. What would others think of him? What would they do to him once he " \
                               "found out? Deciding not to think about it for the time being, he solomnly collected " \
                               "his parents and buried them in the graveyard they once protected.\n\n "
            rynerBackstory09 = "That day became the darkest day of his life, and one that changed it forever. His " \
                               "deep emotion had not only sparked the awakening of Electron Wind, but another power " \
                               "as well: his shadow magic. But by this point, Ryner had decided to never use Electron " \
                               "Lightning ever again. It made him hurt people, not to mention everyone who had heard " \
                               "of his crime had shunned him and feared him. No one wante to be near a boy who " \
                               "couldn't control his own power, especially one who had killed because of it.\n\n "
            rynerBackstory10 = "Ryner decided that he had to leave town. He wanted to be sure he would remember his " \
                               "parents, so he went back to their graves one last time and took something that " \
                               "represented them from his father and a keepsake of the Khabunagos: The Pendent of the " \
                               "Gatekeeper's Shadow. It was said to increase the power of shadow magic, " \
                               "and was a gift from Nabuga herself to the family long ago. With it now in his hands, " \
                               "Ryner left town with nothing but his feelings to weigh him down.\n\n "
            rynerBackstory11 = "Ryner travelled for 15 years after that, constantly training his magic. He grew " \
                               "angrier and angrier at the world and its injustice. Guardians were meant to help " \
                               "people, but instead they took his family from him without so much as a viable reason. " \
                               "These thoughts corrupted him, and leaked into his magic. His spells became more " \
                               "powerful, and he was able to control more of it than he could before. Ryner realized " \
                               "that he was stronger than most everyone in Xhia, which led him to his grandest " \
                               "plan.\n\n "
            rynerBackstory12 = "Ryner decided to use his power to destroy the guardians. Not just the ones that " \
                               "wronged him, not even just the ones in Xhia. All of them, all across Phalmasia. He " \
                               "knew that this wouldn't be an easy task, so in need of more power, he tried to use " \
                               "electron lightning again, despite still despising Nova for being the cause of his " \
                               "problems in the first place. However, it turned out that he couldn't anymore; the " \
                               "spirit of Electron Lightning, Nova, wouldn't allow him to use his power if he was " \
                               "going to use it to hurt people. Ryner threatened him to reconsider, but Nova didn't " \
                               "budge. Ryner, as a result, locked Nova away in his mind, and stole his power.\n\n "
            rynerBackstory13 = "Using Electron Lightning hurt Nova, since he was fighting letting Ryner use it at " \
                               "all. As a result, the magic came out weaker than it would have, and it took more mana " \
                               "to cast any spell than normal. Despite these setbacks, it was still extremely " \
                               "powerful, and using this power along with his normal lightning and shadow magics, " \
                               "he travelled to Halgeis where the strongest guardians were known to live. . .\n\nEnd " \
                               "of Chapter 2\n "

            # Ryner Bio Search Commands
            rynerChapterPrompt = input(
                rynerProfile + "\n" + rynerLightningSpells + "\n" + rynerShadowSpells + "\n" + rynerElectronLightningSpells + "\nEnter 'Chapters' to view the chapters of Ryner's Backstory. Enter 'Back' to return to Character Selection.\n")
            while rynerChapterPrompt == "Chapters" or rynerChapterPrompt == "chapters":
                rynerChapterPrompt = input(
                    "Ryner's Backstory\nPlease enter the chapter number to see a chapter (Chapter 1)\n\n| Chapter 1: Corruption\n| Chapter 2: Anger Overtaking\n\nEnter 'Bio' to return to Ryner's Biography.\n")

                if rynerChapterPrompt == "Bio" or rynerChapterPrompt == "bio":
                    break
                if rynerChapterPrompt == "":
                    rynerChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
                if rynerChapterPrompt != "Chapters" and rynerChapterPrompt != "chapters" and rynerChapterPrompt != "Chapter 1" and rynerChapterPrompt != "chapter 1" and rynerChapterPrompt != "Chapter One" and rynerChapterPrompt != "chapter One" and rynerChapterPrompt != "Chapter one" and rynerChapterPrompt != "chapter one" and rynerChapterPrompt != "Chapter 2" and rynerChapterPrompt != "chapter 2" and rynerChapterPrompt != "Chapter Two" and rynerChapterPrompt != "chapter Two" and rynerChapterPrompt != "Chapter two" and rynerChapterPrompt != "chapter two" and rynerChapterPrompt != "Back" and rynerChapterPrompt != "back" and rynerChapterPrompt != "":
                    rynerChapterPrompt = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

                rynerChapterOne = ""
                rynerChapterTwo = ""
                if rynerChapterPrompt == "Chapter 1" or rynerChapterPrompt == "chapter 1" or rynerChapterPrompt == "Chapter One" or rynerChapterPrompt == "chapter One" or rynerChapterPrompt == "Chapter one" or rynerChapterPrompt == "chapter one":
                    rynerChapterOne = input(
                        "Chapter 1: Corruption\n" + rynerBackstory01 + "\n" + rynerBackstory02 + "\n" + rynerBackstory03 + "\n" + rynerBackstory04 + "\n" + rynerBackstory05 + "\n" + rynerBackstory06 + "\n" + rynerBackstory07 + "\n\nPress 'Enter' to return to chapter selection. Enter 'Next' to view Chapter 2.\n")
                if rynerChapterPrompt == "Chapter 2" or rynerChapterPrompt == "chapter 2" or rynerChapterPrompt == "Chapter Two" or rynerChapterPrompt == "chapter Two" or rynerChapterPrompt == "Chapter two" or rynerChapterPrompt == "chapter two" or rynerChapterOne == "Next" or rynerChapterOne == "next":
                    rynerChapterTwo = input(
                        "Chapter 1: Anger Overtaking\n" + rynerBackstory08 + "\n" + rynerBackstory09 + "\n" + rynerBackstory10 + "\n" + rynerBackstory11 + "\n" + rynerBackstory12 + "\n" + rynerBackstory13 + "\n\nThis is the end of Ryner's Bio. Press 'Enter' to return to chapter selection.\n")
                if rynerChapterOne == "" or rynerChapterTwo == "":
                    rynerChapterPrompt = "Chapters"
                if rynerChapterOne != "Chapters" and rynerChapterOne != "chapters" and rynerChapterOne != "" and rynerChapterTwo != "Chapters" and rynerChapterTwo != "chapters" and rynerChapterTwo != "":
                    rynerChapterOne = input(
                        "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

            if rynerChapterPrompt == "Back" or rynerChapterPrompt == "back":
                break
            if rynerChapterPrompt == "":
                rynerChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if rynerChapterPrompt != "Continue" and rynerChapterPrompt != "continue" and rynerChapterPrompt != "Bio" and rynerChapterPrompt != "bio" and rynerChapterPrompt != "Back" and rynerChapterPrompt != "back":
                rynerChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Serena Fynae Bio
        while characterBarrier == "Serena Fynae" or characterBarrier == "Serena" or characterBarrier == "serena fynae" or characterBarrier == "serena":
            # Serena Bio Prompts
            serenaProfile = "Serena Fynae\n\nHometown: Meteora\nRace: Argen (Blue, Light Gray)\nBirthday: April 2, 4007\nGender: Female\nPronunciation: Se-REEN-ah FAI-nay\nMagic Affinities\n| Fire\n| Gravity\n\nItems\n| Mother's Horn Rings\n\n"
            serenaFireSpells = "Spells: Fire\n| Stunning Flash\n| Pyre Ray\n| Ember Spirit\n* Ember Spirit: Combat\n* Ember Spirit: Heatwave\n| Fire Seal\n| Infernal Uprising\n| Ember Beads\n* Ember Beads: Control\n* Ember Beads: Enhancement Ring\n| Fire Outburst\n| Detonation Seeds\n* Detonation Seeds: Auto-Ignite\n\n"
            serenaGravitySpells = "Spells: Gravity\n| Augmented Gravity (Passive)\n| Placelock\n| Force Shield\n| Rift Palm\n| Control\n\n"

            # Serena Bio Search Commands
            serenaChapterPrompt = input(
                serenaProfile + "\n" + serenaFireSpells + "\n" + serenaGravitySpells + "\nEnter 'Back' to return to Character Selection. Backstory to be written at a later date.\n")
            if serenaChapterPrompt == "Back" or serenaChapterPrompt == "back":
                break
            if serenaChapterPrompt == "":
                serenaChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")
            if serenaChapterPrompt != "Continue" and serenaChapterPrompt != "continue" and serenaChapterPrompt != "Back" and serenaChapterPrompt != "back":
                serenaChapterPrompt = input(
                    "\nYou may have pressed enter on accident or misspelled your search. Please re-enter your search.")

        # Character Input Exit Command
        if characterBarrier == "Back" or characterBarrier == "back":
            infoBarrier = "Back"
            break
        if characterBarrier == "Leave" or characterBarrier == "leave":
            print("Database Search Completed. Please restart program to search again.")
            quit()

    # Location Input Commands
    while infoBarrier == "Locations" or infoBarrier == "locations":
        locationBarrier = input(
            "Continents of Phalmasia:\n| Halgeis\n| Mu'karr\n| Altaria\n| Xhia\n\nLeave the database by entering 'Leave'. Go back to the home prompt by endering 'Back'.\n")

        while locationBarrier == "":
            locationBarrier = input("Please Re-enter your database restriction.\n")
        while locationBarrier != "Halgeis" and locationBarrier != "halgeis" and locationBarrier != "Mu'karr" and locationBarrier != "mu'karr" and locationBarrier != "Mukarr" and locationBarrier != "mukarr" and locationBarrier != "Altaria" and locationBarrier != "altaria" and locationBarrier != "Xhia" and locationBarrier != "xhia" and locationBarrier != "Back" and locationBarrier != "back" and locationBarrier != "Leave" and locationBarrier != "leave":
            locationBarrier = input("Please Re-enter your database restriction.\n")

        # Halgeis Info & City Selection
        while locationBarrier == "Halgeis" or locationBarrier == "halgeis":
            halgeisLocations = input(
                "Halgeis is the first, and currently only, continent where humans inhabit. Terrians are the primary inhabitants of Halgeis, and are also the ones in power in the continent. The humans and the terrians came together in piece relatively quickly, but the argens, avians and majuu weren't so trustworthy. To help along their relations, the terrians and humans constructed the city capital, Grand Elise, the peace capital of the world. With time, all of the races now reside in Grand Elise, and though relations are not perfect, they are still in place.\n\nHalgeis Cities:\n| Volquöla\n| Ashford\n| Oshborne\n| Cilfier\n| Skykumo\n| Swalubu\n| Nulvali\n| Starkiepe\n| Grand Elise\n| Drəklife\n| Mezolune\n| Piquaron\n| Elendraye\n\nLeave the database by entering 'Leave'. Go back to the continent selection by entering 'Back'.\n")

            # Volquöla City Commands
            if halgeisLocations == "Volquola" or halgeisLocations == "volquola" or halgeisLocations == "Volquöla" or halgeisLocations == "volquöla":
                volquolaStats = "Volquöla, Halgeis\n\nPrimary Resident Race: Majuu\nPronunciation: vol-KWOH-lah\nLocation: Northwestern Halgeis\nVisitor Friendly: No\nTown Trade:\n| Weapons\n| Armor\nSub-Locations:\n| Voltoru Canyon\n| Pyrevault Ridge\nNotable Residents:\n| Aeiyou Drefael\n| Kinto Verali\n\n"
                volquolaDescription = "Volquöla is a peaceful town in Northwestern Halgeis and the home to many Majuu, including Aeiyou and Kinto. Volquöla is a town built on the side of Pyrevault Ridge, a volcano that has been inactive for decades. Despite this, it is still extremely hot there, and the average temperature is over 100 degrees Fahrenheit. It has a deep cavern down the side that runs around the northern and eastern side of the town facing towards Mu'Karr called Voltoru Cavern, which hosts a calm and steady flow of magma into the volcano's chamber.\n\nMost majuu from Volquöla are light colors. It hosts many skilled blacksmiths, and it is among some of the main providers of armor and weaponry in Halgeis, which makes it relatively respected in the country. However, most of the villagers prefer to keep to themselves and their community, so the town doesn't get many visitors.\n\n"
                halgeisLocation = input(
                    volquolaStats + volquolaDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Ashford City Commands
            if halgeisLocations == "Ashford" or halgeisLocations == "ashford":
                ashfordStats = "Ashford, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: ASH-ford\nLocation: Northern Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| Kytegrove Forest\n| Frinrir's Gravesite\nNotable Residents:\n| Yggdrasil Aensyll\n\n"
                ashfordDescription = "Ashford is a peaceful town on the northern side of Halgeis. The town itself is larger than other common villages in Halgeis because of the regions of Kytegrove Forest it covers, as well as many nearby open fields. The townspeople are very close-knit and mostly all the residents knows each other, and because of this the residents are very supportive and welcoming to others in the community and outsiders stopping by. Those born with magical capabilities venture to the open fields to spar with one another or find a peaceful, open place to train in solidarity. The town doesn't have any landmarks or produce any products they trade commonly, so Ashford is mostly a quiet settling place for terrians to live a peaceful life with their families.\n\n"
                halgeisLocation = input(
                    ashfordStats + ashfordDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Oshborne City Commands
            if halgeisLocations == "Oshborne" or halgeisLocations == "oshborne":
                oshborneStats = "Oshborne, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: OSH-born\nLocation: Western Halgeis\nVisitor Friendly: Yes\nNotable Residents:\n| Cidelli Reimora\n\n"
                oshborneDescription = "Oshborne is a small town in Western Halgeis and one of the many places in Halgeis that Terrians have made their home. This is also the location of the Reimora Family Bakery. It hosts a lot of open area that is used when the town commonly holds fairs for various occations like holidays, which are extravagant in their own right.\n\nThe town doesn't act as a tourist attraction since there aren't many things to do there, but the town will openly accept any travelers who happen to be passing through.\n\n"
                halgeisLocation = input(
                    oshborneStats + oshborneDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Cilfier City Commands
            if halgeisLocations == "Cilfier" or halgeisLocations == "cilfier":
                cilfierStats = "Cilfier, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: SIL-fire\nLocation: Eastern Halgeis\nVisitor Friendly: Yes\nTown Trade:\n| Fish\nSub-Locations:\n| Sapphire Lakes\nNotable Residents: Mimi Seiran\n\n"
                cilfierDescription = "Cilfier is a city centered around the Sapphire Lakes, and is also where the town name originated from. They got their name because of their deep blue water that makes them look like sapphire gems. Because of these lakes, Cilfier is colder than other cities most of the year, but they also provide the town with seafood, as well as enabled the town to trade fish to the rest of Halgeis.\n\nResidents who use water magic enjoy practicing with the water in the lakes. The lakes of Cilfier draw in travellers from across Halgeis to admire them. The citizens of Cilfier don't allow anyone to take water out of or polluting the lakes to both respect the lakes and nature.\n\n"
                halgeisLocation = input(
                    cilfierStats + cilfierDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Skykumo City Commands
            if halgeisLocations == "Skykumo" or halgeisLocations == "skykumo":
                skykumoStats = "Skykumo, Halgeis\n\nPrimary Resident Race: Avian\nPronunciation: SKY-coo-moh\nLocation: Northern Halgeis\nVisitor Friendly: No\nSub-Locations:\n| Tengou Mountain\nNotable Residents: Kimiko Quintai\n\n"
                skykumoDescription = "Skykumo is a mountainside village so high that it is near cloud height, which is how the town got its name. It is on Tengou Mountain, one of the tallest mountains in Halgeis. It is a village of avians, since only they can breathe clearly in such thin air. Despite avian's natural accpetance of all people, Skykumo is rather closed to visitors. It isn't the fact that avians do not welcome visitors, it is that many visitors simply do not come to Skykumo.\n\nIt is a simple town with the only attraction being its height and its proximity to the clouds. Most don't come to see this, however, because the thin air in Skykumo makes breathing extremely labor-intensive and is dangerous to most without protective gear or wind magic.\n\n"
                halgeisLocation = input(
                    skykumoStats + skykumoDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Swalubu City Commands
            if halgeisLocations == "Swalubu" or halgeisLocations == "swalubu":
                swalubuStats = "Swalubu, Halgeis\n\nPrimary Resident Race: Human\nPronunciation: swa-LOO-boo\nLocation: Northeastern Halgeis\nVisitor Friendly: Yes\nTown Trade:\n| Seafood\nSub-Locations:\n| Soshi Dojo\n| Borderline Beach\n\n"
                swalubuDescription = "Swalubu is a seaside city in Halgeis that borders Mu'karr. It hosts both a beach and a large tackle shop due to its proximity to the ocean. Many fishermen make their homes here due to this, though not many others live here due to its summertime business. Due to the beach, the town is also a tourist spot for both those that live in Halgeis and those visiting from other continents.\n\nSwalubu also houses Soshi Dojo, a combat training school that specializes in honing weaponry skills and fighting styles. It is extremely popular, and those without magic often come here seeking mentorship if they still wish to help defend or protect others (as guardians or not).\n\n"
                halgeisLocation = input(
                    swalubuStats + swalubuDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Nulvali City Commands
            if halgeisLocations == "Nulvali" or halgeisLocations == "nulvali":
                nulvaliStats = "Nulvali, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: null-VAH-lee\nLocation: Northern Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| Nulvali Marketplace\n| Kytegrove Forest\n| Halgeian Flyers Department (HFD)\n\n"
                nulvaliDescription = "Nulvali is a large town in northern Halgeis, and is the neighbor of Ashford. Nulvali is busy almost all days of they year, especially on weekends, due to the Nulvali marketplace; a bustling shopping center that hosts all types of stores. Many people from neighboring towns come to the market for produce and other wares. \n\nIt is also the location of several departmental businesses like the Halgeian Flyers Department, or HFD. They are responsible for testing potential wind users for legalized flight, and give out Flyers Licenses. Though there are other locations, due to Kytegrove Forest being in such a close vicinity, it is the largest center in Halgeis.\n\n"
                halgeisLocation = input(
                    nulvaliStats + nulvaliDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Starkiepe City Commands
            if halgeisLocations == "Starkiepe" or halgeisLocations == "starkiepe":
                starkiepeStats = "Starkiepe, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: STAR-keep\nLocation: Central Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| Steelpaige Mountains\n* Briarfield Cliffs\n| Starkiepe Battle Frontier\n\n"
                starkiepeDescription = "Starkiepe is a large city in the center of Halgeis. Starkiepe is a tourist attraction for all those in Halgeis. It is one of the core cities of the continent, and is filled with activities, food, and shopping centers that those from all over Halgeis come to use and enjoy. Just outside of the city, there is a small mountain range called Steelpaige Mountains which is also accessible to climb. If you reach the top, you will arrive at Briarfield Cliffs, a blooming plateau at the top of the highest mountain overlooking all of Starkiepe. It is very popular to tourists due to the photogeniety of the city.\n\nOne of the highlights of the city, however, is the arena for the Starkiepe Battle Frontier. This is a location where magic users from Halgeis can come to compete in competitive matches and challanges. Those who want to compete must pass a trial exam to portray their skill, as well as follow certain guidelines to ensure the health of those competing. These matches may be attempted alone, or with a team, in which case the team name and members must all be registered as such. It is a great place to go to watch some action.\n\n"
                halgeisLocation = input(
                    starkiepeStats + starkiepeDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Grand Elise City Commands
            if halgeisLocations == "Grand Elise" or halgeisLocations == "Grand elise" or halgeisLocations == "grand Elise" or halgeisLocations == "grand elise":
                grandEliseStats = "Grand Elise, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: Grand El-LEASE\nLocation: Central Halgeis\nVisitor Friendly: Yes\nSub-Locations:\n| St. Guardia's Academy\n| Enchanted Forest\n\n"
                grandEliseDescription = "Grand Elise is the capital city of Halgeis, but is one of the continent's younger cities. When humans first emerged on Phalmasia hundreds of years ago, they bonded strongly with the terrians in Halgeis. Their ultimate goal was to unite all of the races as equals, and built the city with this in mind, welcoming any race that wanted to live in Halgeis a home. Grand Elise became the symbol of peace in the world, and the first official result of progression towards interracial acceptance. After St. Guardia's Academy was destroyed during the Arduos War, they decided to rebuild it in the center of Grand Elise.\n\nThough it hosts the schooling grounds for Guardians, it is still open to visitors year-round. Every year St. Guardia's sets off fireworks in celebration of the day that Grand Elise had officially finished construction and became open to visitors and residents. The Enchanted Forest, the largest forest in Halgeis, is also present withing walking distance of the city's borders and is easily accessible to residents and visitors.\n\n"
                halgeisLocation = input(
                    grandEliseStats + grandEliseDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Drəklife City Commands
            if halgeisLocations == "Dreklife" or halgeisLocations == "dreklife":
                dreklifeStats = "Drəklife, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: DREEK-life\nLocation: Western Halgeis\nVisitor Friendly: No\nSub-Locations:\n| Enchanted Forest\n\n"
                dreklifeDescription = "Drəklife is a small village on the easternmost side of the Enchanted Forest. It has a small population, but the town acts more as a family than a village; everyone is close-knit, and though visitors are welcomed with open arms, many are unaware of its presence and don't stop by. Because of its seclusion, it is one of the few towns unprotected by a guardian post, which leaves it open to the attack from wrongdoers. But because it is so secluded, they rarely get attacked anyway. Drəklife harvests most of its resources from the nearby Enchanted Forest, but is still respectful enough to replant any trees it cuts down. Their work has done almost nothing to the health of the forest, but their care has actually improved it. Those who live in Drəklife have learned to care for the enironment and others.\n\n"
                halgeisLocation = input(
                    dreklifeStats + dreklifeDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Mezolune City Commands
            if halgeisLocations == "Mezolune" or halgeisLocations == "mezolune":
                mezoluneStats = "Mezolune, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: MEH-zo-loon\nLocation: Southeastern Halgeis\nVisitor Friendly: No\nTrade:\n| Produce/Crops\nNotable Residents:\n| Amiru Soaren\n\n"
                mezoluneDescription = "Mezolune is a village on the outskirts of Halgeis near the sea. The land there is very rich and good for growing basic produce like potatoes, carrots, and other common veggies. Though they don't have a large town, the area the village takes up is one of the largest in all of Halgeis due to the farmland. They distribute their crops all over Halgeis along with their neighboring towns, which provide the majority of the produce supply.\n\nDespite this, the town itself doesn't resemble typical farmland; it looks like a normal village. Small markets are found on most days, and many people call this place their home. Those who live here have a great affinity for life and plants alike.\n\n"
                halgeisLocation = input(
                    mezoluneStats + mezoluneDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Piquaron City Commands
            if halgeisLocations == "Piquaron" or halgeisLocations == "piquaron":
                piquaronStats = "Piquaron, Halgeis\n\nPrimary Resident Race: Avian\nPronunciation: Pick-CWUAIR-ron\nLocation: Southwestern Halgeis\nVisitor Friendly: Yes\nNotable Residents:\n| Turcobé Sentai\n\n"
                piquaronDescription = "Piquaron is a small village in Halgeis inhabited by avians. There are few avian towns that are built at ground level, and Piquaron is one of those few. Piquaron is an average town that takes great pride in its village's magic ability. Usually, avians are born with ice or wind magics suitable for their usual home heights, but because of the low altitude, most avians here actually have a greater affinity for earth magic than ice.\n\nMagic affinity is taken very seriously, and all citizens here view magic as an extention of themselves, giving them faster mana regeneration and larger mana reserves than most. Piquaron schools teach students in a rather unconventional way; instead of teaching them spells, they teach them mana control. This not only leaves the students to figure out spells on their own which increases their understanding of their magic, but it also teaches them to find ways to use them more efficiently and in a way that is comfortable for them.\n\n"
                halgeisLocation = input(
                    piquaronStats + piquaronDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            # Elendraye City Commands
            if halgeisLocations == "Elendraye" or halgeisLocations == "elendraye":
                elendrayeStats = "Elendraye, Halgeis\n\nPrimary Resident Race: Terrian\nPronunciation: ELL-en-dray\nLocation: Southwestern Halgeis\nVisitor Friendly: No\nNotable Residents:\n| Yumeizu Artilux\n\n"
                elendrayeDescription = "Elendraye is a large town that sits in a valley in Southwestern Halgeis. Though the town itself is a spectacle to see, not many visitors are welcomed here. Elendraye is a closed town, and many who were born there live there for their whole lives. A deep familial community is built in this town and has been that way for generations. The townfolk maintain the health of the valley by using earth and water magic, as well as planting trees and flowers to liven the area.\n\nDespite this, the people of elendraye arequote adapt to their surroundings and know a lot about the history of Halgeis. Many of them do not beleive in violence, so they use their magic like agrens are known to: defensively. This influences the magic styles of many magic users who live here. A common passtime for children is to practice their magics with and against each other.\n\n"
                halgeisLocation = input(
                    elendrayeStats + elendrayeDescription + "Go back to the other cities of Halgeis by pressing 'Enter'.\n")

            while halgeisLocations == "":
                halgeisLocations = input("Please Re-enter your database restriction.\n")
            while halgeisLocations != "Volquola" and halgeisLocations != "volquola" and halgeisLocations != "Ashford" and halgeisLocations != "ashford" and halgeisLocations != "Oshborne" and halgeisLocations != "oshborne" and halgeisLocations != "Cilfier" and halgeisLocations != "cilfier" and halgeisLocations != "Skykumo" and halgeisLocations != "skykumo" and halgeisLocations != "Swalubu" and halgeisLocations != "swalubu" and halgeisLocations != "Nulvali" and halgeisLocations != "nulvali" and halgeisLocations != "Starkiepe" and halgeisLocations != "starkiepe" and halgeisLocations != "Grand Elise" and halgeisLocations != "Grand elise" and halgeisLocations != "grand Elise" and halgeisLocations != "grand elise" and halgeisLocations != "Dreklife" and halgeisLocations != "dreklife" and halgeisLocations != "Mezolune" and halgeisLocations != "mezolune" and halgeisLocations != "Piquaron" and halgeisLocations != "piquaron" and halgeisLocations != "Elendraye" and halgeisLocations != "elendraye" and halgeisLocations != "Leave" and halgeisLocations != "leave" and halgeisLocations != "Back" and halgeisLocations != "back":
                halgeisLocations = input("Please Re-enter your database restriction.\n")

            # Halgeis Exit Command
            if halgeisLocations == "Back" or halgeisLocations == "back":
                break
            if halgeisLocations == "Leave" or halgeisLocations == "leave":
                print("Database Search Completed. Please restart program to search again.")
                quit()

        # Locations Exit Command
        if locationBarrier == "Back" or locationBarrier == "back":
            infoBarrier = "Back"
            break
        if locationBarrier == "Leave" or locationBarrier == "leave":
            print("Database Search Completed. Please restart program to search again.")
            quit()

    # Magic Input Commands
    while infoBarrier == "Magic" or infoBarrier == "magic":
        magicBarrier = input(
            "Elemental Magic:\n| Fire\n| Water\n| Lightning\n| Wind\n| Ice\n| Earth\n\nLost Magic:\n| Shadow\n| Nature\n| Life\n| Gravity\n\nSigils:\n| About Sigils\n| Unity Sigils\n| Sectional Sigils\n\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n")

        while magicBarrier == "":
            magicBarrier = input("Please Re-enter your database restriction.\n")
        while magicBarrier != "Fire" and magicBarrier != "fire" and magicBarrier != "Water" and magicBarrier != "water" and magicBarrier != "Lightning" and magicBarrier != "lightning" and magicBarrier != "Wind" and magicBarrier != "wind" and magicBarrier != "Ice" and magicBarrier != "ice" and magicBarrier != "Earth" and magicBarrier != "earth" and magicBarrier != "Shadow" and magicBarrier != "shadow" and magicBarrier != "Nature" and magicBarrier != "nature" and magicBarrier != "Life" and magicBarrier != "life" and magicBarrier != "Gravity" and magicBarrier != "gravity" and magicBarrier != "Unity Sigils" and magicBarrier != "Unity sigils" and magicBarrier != "unity Sigils" and magicBarrier != "unity sigils" and magicBarrier != "Sectional Sigils" and magicBarrier != "Sectional sigils" and magicBarrier != "sectional Sigils" and magicBarrier != "sectional sigils" and magicBarrier != "About Sigils" and magicBarrier != "About sigils" and magicBarrier != "about Sigils" and magicBarrier != "about sigils" and magicBarrier != "Sigils" and magicBarrier != "sigils" and magicBarrier != "Unity" and magicBarrier != "unity" and magicBarrier != "Sectional" and magicBarrier != "sectional" and magicBarrier != "Back" and magicBarrier != "back" and magicBarrier != "Leave" and magicBarrier != "leave":
            magicBarrier = input("Please Re-enter your database restriction.\n")

        # Elemental Magic
        # Fire Magic Commands
        if magicBarrier == "Fire" or magicBarrier == "fire":
            fireExplanation = "Passive Ability: Resistance to non-magic flames & heat\n\nFire magic is a magic geared more towards offense, and the only magic that continue to grow without the caster's maintenence or mana. This also makes the magic difficult to control for new fire users. This magic is commonly associated with the caster's emotions, since it sometimes grows in power in accordance to them. Fire users are known to be determined, motivated, or obnoxious when accomplishing their goals."
            fireSpells = "Basic Spells:\n| Ember Palm: The user covers their hands, and occasionally arms, in fire magic. This both adds extra power in close-range fights, and allows for basic ranged attacks.\n| Burst Step Spells: The user covers their feet, and occasionally legs, in fire magic. This both adds extra power in close-range fights. Additionally, it can be used to concentrate mana under the user's feet and create an explosion that boosts their jump height.\n| Combustion Spells: A ranged application of fire magic that allows the user to concentrate their mana at a distance and cause an explosion."
            fireUsers = "Notable Users:\n| Mirago Fynae\n| Kimiko Quintai\n| Kinto Vareli\n| Serena Fynae"
            fireMagic = input(
                "Fire, The Element of Ambition\nSigil Color Representation: Red\n" + fireExplanation + "\n\n" + fireSpells + "\n\n" + fireUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Water Magic Commands
        if magicBarrier == "Water" or magicBarrier == "water":
            waterExplanation = "Passive Ability: Using mana to walk on water\n\nWater magic is a magic geared towards defense. Using this magic takes tact and planning. Users of water magic are able to alter the temperature of water by freezing and boiling it. Users of water magic are known to be relaxed and in tune with their surroundings, and are passive about their thoughts and opinions."
            waterSpells = "Basic Spells:\n| Breath Spells: The user takes a large breath to increase their lung capacity so they can stay underwater for longer periods of time. They do this by surrounding their heads with an air bubble. The stronger the caster of the spell, the larger the air bubble is, and the more of the body it covers.\n| Glow Spells: This type of spell can only be used underwater. The caster uses mana to make the water around their hands glow to illuminate dark underwater areas. The brightness and proximity of the glow is determined by the caster's strength.\n| Moisture Spells: This spell is the basis of water magic. Users can't create their own element like many of the other magics, and aren't around it at all times, either. This spell allows them to take water from the air and plants in the surroundings to use."
            waterUsers = "Notable Users:\n| Mimi Seiran\n| Amiru Soaren"
            waterMagic = input(
                "Water, The Element of Flow\nSigil Color Representation: Blue\n" + waterExplanation + "\n\n" + waterSpells + "\n\n" + waterUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Lightning Magic Commands
        if magicBarrier == "Lightning" or magicBarrier == "lightning":
            lightningExplanation = "Passive Ability: Short distance teleportation\n\nLightning is a magic that specializes in quick, precise attacks. If dealt with enough power, these attacks may inflict extra shock damage or even temporary paralysis. Due to the concentration of lightning magic, it can easily be used to penetrate a target's armor. Though the magic's overall power isn't substantial, it more than makes up for it in speed. Users of lighting magic are known to be excitable and confident."
            lightningSpells = "Basic Spells:\n| Shock Step: The caster releases lightning from their feet, allowing for increased movement speed. High level casters will leave trails behind them as they move, which cause added shock damage and possible paralysis.\n| Dart Spells: The caster releases a quick bolt from their hands, dealing damage and possibly stunning the target."
            lightningUsers = "Notable Users:\n| Cidelli Reimora\n| Ryner Khabunago"
            lightningMagic = input(
                "Lightning, The Element of Precision\nSigil Color Representation: Yellow\n" + lightningExplanation + "\n\n" + lightningSpells + "\n\n" + lightningUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Wind Magic Commands
        if magicBarrier == "Wind" or magicBarrier == "wind":
            windExplanation = "Passive Ability: Slight flight & Gliding\n\nWind, when used in high concentrations, can be used to slice objects or opponents at high speeds. Defensively, however, it must deflect most magic attacks and projectiles. This magic is preferred by those who use speed and agility in their combat. Using their magic, they are also able to use streams of wind to push and pull objects from a distance. Users of wind magic are known to be lone wolves who travel their own path and fight for what they think is right."
            windSpells = "Basic Spells:\n| Lightfoot Spells: The caster channels mana into their feet which allows them to increase their speed and jump height, cushion their landings, and, along with the help of a glider, glide and even fly for a short period of time.\n| Breath Spells: The caster gathers mana in their lungs to increase their lung capacity to blow out winds of high speeds, increase their volume, and hold their breath for a prolonged period of time. The more experienced the caster, the more air can be brought into the lungs.\n| Sharp Spells: The caster presses mana together to create a sharp blade of wind with which they can throw as a projectile or attatch to their body as a sword-like extention. The size, speed, and cutting power of these blasts are dependent on the strength of the caster."
            windUsers = "Notable Users:\n| Xaeyz Kai\n| Yggdrasil Aensyll\n| Yumeizu Artilux"
            windMagic = input(
                "Wind, The Element of Free Paths\nSigil Color Representation: Teal\n" + windExplanation + "\n\n" + windSpells + "\n\n" + windUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Ice Magic Commands
        if magicBarrier == "Ice" or magicBarrier == "ice":
            iceExplanation = "Passive Ability: Resistance to non-magic based freezing temperatures.\n\nIce is a powerful magic for both offensive and defensive capabilities. This magic is extremely deadly to even the user at times, so using it with a pact for better control is highly recommended. This magic has the capability to penetrate a target's armor, but not with the level of proficiency of lightning. They can freeze the air, water or ground around them, which allows for an increased range of mobility on the battlefield and place-locking opponents. It is also the only magic with no distinguishing base shape, coming out in spikes if used in brute force. Th temperature of this flame scales with the user's strength."
            iceSpells = "Basic Spells:\n| Frost Fire: The user conjures a freezing flame that shocks armor, withering it away and making it easier to penetrate. This can cause serious damage if use directly on a person's vitals with extreme intensity.\n| Spike Bullet: The user creates multiple ice spikes that float behind the user's back until they call for them to be fired. These can be shaped into any object, but spikes are most commonly used as they deal a lot of piercing damage. The speed, durability, and size of these projectiles scale with the user's strength."
            iceUsers = "Notable Users:\n| Aeiyou Drefael"
            iceMagic = input(
                "Ice, The Element of Resistance\nSigil Color Representation: Light Blue\n" + iceExplanation + "\n\n" + iceSpells + "\n\n" + iceUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Earth Magic Commands
        if magicBarrier == "Earth" or magicBarrier == "earth":
            earthExplanation = "Passive Ability: Hardened resistance to magic based attacks.\n\nEarth is a magic that is both offensive and defensive. Earth magic relies on the ground beneath the user's feet, giving them free reign to control the battlefield at will. Being such a sturdy magic, earth can easiy use their defense as offense and vice versa. Due to this, it has a lot of ways to counter other elements. Though earth magic uses the most magic energy to cast spells of all other elemental magics as well as the shortest casting range, its combat capability more than makes up for it. This magic is preferred by those who fight up close."
            earthSpells = "Basic Spells:\n| Earth's Step: The user impacts the ground, creating a crack and sending a wave of earth in the direction of their target. It is a good move to narrow the opponent's line of sight, as well as throw them off their balance.The stronger the caster, the larger the wave.\n| Pillar Spells: The user creates pillars of earth from the ground, striking opponents or use as a defense. They can also be ripped from the ground and float in midair for a while. The stronger the caster is, the larger the pillars will be, and the faster they can create them.\n| Soft Sand Spells: The caster concentrates their mana on a certain area on the ground and softens it, creating a quicksand-like pit. This sinks the target down as far as their torso, and extremely strong casters can sink opponents down to their shoulders. It is impossible to use this spell to sink someone completely."
            earthUsers = "Notable Users:\n| Aeiyou Drefael\n| Kinto Vareli\n| Turcobé Sentai"
            earthMagic = input(
                "Earth, The Element of Nature\nSigil Color Representation: Brown\n" + earthExplanation + "\n\n" + earthSpells + "\n\n" + earthUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Lost Magic
        # Shadow Magic Commands
        if magicBarrier == "Shadow" or magicBarrier == "shadow":
            shadowExplanation = "Passive Ability: Creating shadow copies. The mana cost increases with the number of clones.\n\nShadow is a magic that only the Khabunago Family is capable of; a family of spirits that use Sprite Pacts to gain mortal & physical forms. They are the spiritual protectors of graveyards, guarding them from any who wish to disturb the graves of those who are buried there. Shadow magic allows the user to create and manipulate darkness. It is possible to create solid shadows using this magic, which can be used to cause extreme damage. Many classify this as a dark magic, and can be easily dispelled with fire magic."
            shadowSpells = "Basic Spells:\n| Cloak Spells: The caster hides their physical body in a nearby shadow, increasing their movement speed and travel capabilities. They are able to be damaged while in their shadow by attacking the shadow directly. The less mana you have remaining, the slower you move, and the more you are pushed out of the shadow.\n| Tendril Spells: The caster shapes the surrounding shadows into solid spike-like structures that can grab or damage opponents. The more proficient the caster, the more range and damage they can deal.\n| Dark Mana: The caster forms projectiles from the surrounding shadows and throws them at the target. It can also be used to lock the shadows of the target in place, restraining their movement. This, however, is an active ability, and no other spells can be cast while restraining a target. The stronger the caster, the longer the stun, and the stronger the projectile.\n| Banish Spells: The caster concentrates the shadows of the target to strangle themselves, cutting off the target's flow of mana and preventing them from casting spells for a short time."
            shadowUsers = "Notable Users:\n| Ryner Khabunago"
            shadowMagic = input(
                "Shadow, The Element of Reflection\nSigil Color Representation: Black\n" + shadowExplanation + "\n\n" + shadowSpells + "\n\n" + shadowUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Nature Magic Commands
        if magicBarrier == "Nature" or magicBarrier == "nature":
            natureExplanation = "Passive Ability: Immunity to non-magic based poison & paralysis from plants.\n\nNature is a magic that works similarly to Earth; the only difference is it utilizes the plants instead of the ground itself. It can cause plants to grow at and extremely quick pace, as well as change their capabilities by making them poisonous. All poison created by a user's spells do not affect the caster. This also allows the user to create and manipulate wood, which creates strong and versetile defenses. This magic has an advantage against wind magic."
            natureSpells = "Basic Spells:\n| Nurture Spells: The caster channels mana into wildlife around them and increases their growth speed. It is the core of nature magic and the basis of all its spells, as it also gives the caster control of all plants in the area. The more proficient the caster, the faster the rate of growth becomes, and the more precise the control gets.\n| Vine Spells: The user grows vines that can emerge from anywhere on the battlefield within the caster's reach. They are used to attack and grab targets. The stronger the caster, the faster and longer the vines can become.\n| Property Spells: The caster concentrates mana into the surrounding plants and changes their properties, allowing them to emit spores with effects of the caster's choice. The larger the plant, the larger the mana cost."
            natureUsers = "Notable Users: None"
            natureMagic = input(
                "Nature, The Element of Harvest\nSigil Color Representation: Purple\n" + natureExplanation + "\n\n" + natureSpells + "\n\n" + natureUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Life Magic Commands
        if magicBarrier == "Life" or magicBarrier == "life":
            lifeExplanation = "Passive Ability: Natural healing factor is enhanced.\n\nOf all magic, Life is the most risky and dangerous to use. It uses a visible stream of life energy to cast and use spells. Life magic can also heal targets, but at a high cost to the user."
            lifeSpells = "Basic Spells:\n| Give & Take Spells: The caster channels a stream of life that takes from one thing to give to another. This can be used to transfer resources from one place to another, like water or nutrients. If the caster takes something from one thing or person, it loses said status and the receiving end gains said status.\n| Sacrifice Spells: A sub-genre of Give & Take Spells that specicifically deals with human injury and basic healing. This revolves around the caster taking injuries from one target and giving them to another. This results in the healing of the initial target and the injury of the post target.\n| Absorb Spells: The caster wraps their hand in a mana stream that draws all mana-based attacks towards it and absorbs them. This replenishes the caster's mana supply proportional to the amount of mana the target used to cast the spell.\n| Mirror Spells: The caster surrounds both arms with streams of mana. This absorbs a mana-based spell targeted at the caster with one hand, then releases the spell through the opposite arm. This, however, takes mana, and the caster must expend mana equal to the amount of mana used to cast the original spell."
            lifeUsers = "Notable Users:\n| Mirago Fynae"
            lifeMagic = input(
                "Life, The Element of Sacrifice\nSigil Color Representation: Green\n" + lifeExplanation + "\n\n" + lifeSpells + "\n\n" + lifeUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Gravity Magic Commands
        if magicBarrier == "Gravity" or magicBarrier == "gravity":
            gravityExplanation = "Passive Ability: A psychic-like ability that allows the user to lift and manipulate opjects with their mana.\n\nGravity magic is the rarest of all magics. It can only be used by Argenian families who live in the mountainous regions of Mu'karr. Using this magic makes the controlling mana invisible to both the user and those around them, as well as the largest attack radius of all magics. It controls gravity in a spherical radius around the target of the spells, and works as a psychic ability would. Gravity can be used to move objects to the will of the user. However, due to its rarity, those who have it usually don't know how to control it. The user can choose whether or not the gravity they manipulate affects them or not."
            gravitySpells = "Basic Spells:\n| Barrier Spells: The user emits an arc radius towards the casting direction. This makes any target that enters that radius shoot towards the ground, physical or mana based, before it can deal damage to the caster. Though it has never been a recorded attempt, it may be possible to increase gravity to a degree that a magic-based spell that enters the barrier is immidiately dispelled.\n| Impulse Spells: The caster compresses their mana into a sphere and sends it at a target location. On either command or impact, the sphere disperses, releasing a powerful impulse that forcefully pushes everything in the sphere's radius away from the center of the sphere.\n| Push Spells: A melee based spell. The user concentrates mana in their palm and strikes the target. This causes a blow that deals increased damage and sends the target flying backward. This can also be used to create shockwaves when striking the air."
            gravityUsers = "Notable Users:\n| Xaeyz Kai\n| Serena Fynae"
            gravityMagic = input(
                "Gravity, The Element of Control\nSigil Color Representation: Gray\n" + gravityExplanation + "\n\n" + gravitySpells + "\n\n" + gravityUsers + "\n\nPress 'Enter' to return to magic selection.\n")

        # Sigils
        # About Sigils Commands
        if magicBarrier == "About Sigils" or magicBarrier == "About sigils" or magicBarrier == "about Sigils" or magicBarrier == "about sigils" or magicBarrier == "Sigils" or magicBarrier == "sigils":
            sigilExplanation = input(
                "About Sigils\n\nSigils are unique magic mechanics that are only available to those with two magics. Once a user masters both elements, a symbol shaped of either a circle, triangle, square, or diamond will manifest itself on the back of the user. This sigil begins passively storing the user's mana, increasing the maximum amount the user can hold at once. It can hold up to 30% of the maximum mana capacity of the user.\n\nThough the user can use this stored mana normally, when full, the user can tap into the power of the sigil, spreading the power across their body. This is shown by streams of mana extending over their limbs. This floods the body with the previously stored mana, increasing the damage of spells casted. However, this boost lasts proportionally long to the amount of mana stored, meaning those with higher base mana capacities can use sigil boosts for longer periods of time.\n\nIf the user has a mythical element, however, this time limit is doubled, as it drains from both the user and their mythical spirit, though it doesn't increase the power of mythical elements any. Though mythical elements do not get boosted by sigils, they do force them to function differently. Those with sectional sigils and mythical elements can use each section of the sigil as if it was a full one. That is to say, if you have an fire and water sigil, you would have the base 30% mana storage capacity, splitting it between the two elements. However, if you had fire, water, and onyx fire, you would have each section store 30% mana, leading to a 90% total mana storage.\n\nPress 'Enter' to return to magic selection.\n")

        # Unity Sigil Commands
        if magicBarrier == "Unity Sigils" or magicBarrier == "Unity sigils" or magicBarrier == "unity Sigils" or magicBarrier == "unity sigils" or magicBarrier == "Unity" or magicBarrier == "unity":
            unityExplanation = "Unity Sigils are base sigils, and the ones that awaken for all their users. Unity sigils blend the colors of the two magics the user controls, then uses that swirled color to make up the sigil. Utilizing this sigil, the user can use the entirity of the sigil's stored power for one magic, or a balance of the two. For instance, the user can use 100% of the stored energy for one of their magics or some balance of the stored energy on each of their two magics.\n\nIt gives the user added versitility as it acts as an extention of the user's magic pool. When activated completely, the streams that surround the user take on the swirled color of the sigil. When in this state, you can use both magic types freely and get the increased power from the sigil, and the time limit remains the same."
            unitySigil = input(
                "Unity Sigils\n\n" + unityExplanation + "\n\nPress 'Enter' to return to magic selection.\n")

        # Sectional Sigil Commands
        if magicBarrier == "Sectional Sigils" or magicBarrier == "Sectional sigils" or magicBarrier == "sectional Sigils" or magicBarrier == "sectional sigils" or magicBarrier == "Sectional" or magicBarrier == "sectional":
            sectionalExplanation = "Sectional Sigils, also known as Evolved Sigils, are attained by extreme mana control, and are completely up to the user's decision. A Unity Sigil will not evolve itself into a Sectional Sigil unless the user meets the requirements and wills the sigil to evolve. Once evolved into a Sectional Sigil, a user is completely unable to return to using a Unity Sigil.\n\nTo attain a Sectional Sigil, the user must force all of their mana into the sigil. This causes the sigil to destabilize and shuts down the user's mana flow for one month, leaving the user physically weakened. On the final day, the user regains their mana, and in a spiritual battle, must best the sigil's magic, which has been charged to hold over four times the user's maximum mana capacity, using their own. The user will be unable to activate or utilize their sigil in any way, and only one chance to best the sigil is given. If the user emerges victorious, the sigil will evolve into a Sectional Sigil.\n\nThe power of the Sectional Sigil is relatively similar in function to the Unity Sigil. However, instead of the blended color, the sigil sections the magic by evenly splitting itself, leaving each half of the sigil to reflect one of the user's magics. This means that the user is limited to using up to 50% of the sigil's stored energy for each magic.\n\nWhile activated completely, the user can choose to activate half of their sigil. When this is done, the streams that cover the user's body take on the color of the chosen magic. Because the user is only activating half of the sigil, the sigil only lasts half as long as it did before. But, because the mana is more controlled due to the Sectional Sigil, the sigil gives double the power boost it did before. However, this only lasts for the chosen magic, meaning that the magic not associated with the activated sigil will get the normal power boost. Additionally, if both sides of the Sectional Sigil are used simultaniously, then the streams take on a striped pattern made up of the two magic colors of the user, and the power boost given is quadrupled for both magics."
            sectionalSigil = input(
                "Sectional Sigils\n\n" + sectionalExplanation + "\n\nPress 'Enter' to return to magic selection.\n")

        # Magic Exit Command
        if magicBarrier == "Back" or magicBarrier == "back":
            infoBarrier = "Back"
            break
        if magicBarrier == "Leave" or magicBarrier == "leave":
            print("Database Search Completed. Please restart program to search again.")
            quit()

    # Races Input Commands
    while infoBarrier == "Races" or infoBarrier == "races":
        raceBarrier = input(
            "Besides humans, there are four different races that inhabit Phalmasia: Terrians, Argens, Avats, and Majuu. Each of them primarily inhabit one continent of Phalmasia, and have different ways of life, as well as unique characteristics and magic options. It is possible for some of these races to learn magic that isn't in their common subset, but it is very uncommon.\n\nRaces:\n| Terrians\n| Argens\n| Avats\n| Majuu\n\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n")

        while raceBarrier == "":
            raceBarrier = input("Please Re-enter your database restriction.\n")
        while raceBarrier != "Terrians" and raceBarrier != "terrians" and raceBarrier != "Terrian" and raceBarrier != "terrian" and raceBarrier != "Argens" and raceBarrier != "argens" and raceBarrier != "Argen" and raceBarrier != "argen" and raceBarrier != "Avats" and raceBarrier != "avats" and raceBarrier != "Avat" and raceBarrier != "avat" and raceBarrier != "Majuu" and raceBarrier != "majuu" and raceBarrier != "Back" and raceBarrier != "back" and raceBarrier != "Leave" and raceBarrier != "leave":
            raceBarrier = input("Please Re-enter your database restriction.\n")

        # Terrian Commands
        if raceBarrier == "Terrians" or raceBarrier == "terrians" or raceBarrier == "Terrian" or raceBarrier == "terrian":
            terrianRace = input(
                "Terrians\n\nCommon Magic Affinities: Fire, Water, Earth, Lightning, Wind, Ice\nNative Continent: Halgeis\n\nA peaceful race that highly populates the Halgeis Region. Many terrians work as farmers, and have a long standing relationship with other races. They can be found living almost everywhere and can easily adapt to new environments. They originally built the city of Grand Elise as a way to bring all races together to live in harmony and peace, and established the Divina Royal Family that ruled for many generations.\n\nIt is said that the terrians evolved from their domesticated ancestors during the old age of the world's birth, taking on forms to better serve the one place they call home. Terrians are very diverse and come in all shapes and sizes.\n\nPress 'Enter' to return to race selection.\n")

        # Argen Commands
        if raceBarrier == "Argens" or raceBarrier == "argens" or raceBarrier == "Argen" or raceBarrier == "argen":
            argenRace = input(
                "Argens\n\nRace Ability: Scales slightly resist magic-based attacks.\nCommon Magic Affinities: Fire, Lightning, Earth\nNative Continent: Mu'karr\n\nA highly intelligent and curious race, argens populate the mountainous, forest-covered region of Mu'karr. Very in tune with nature and mana, they are people who have a strong thirst for knowledge, many becoming researchers or professors in school. Their lifestyle is simple and homely, many preferring to stay in Mu'karr as the climate fits perfectly for their preferred environment high in the mountains.\n\nArgens were the first of the new races to appear after terrians, when humans discovered and explored Mu'karr. They come in a variety of colors and patterns. They are also the only race capable of having an affinity for gravity magic.\n\nPress 'Enter' to return to race selection.\n")

        # Avat Commands
        if raceBarrier == "Avats" or raceBarrier == "avats" or raceBarrier == "Avat" or raceBarrier == "avat":
            avatRace = input(
                "Avats\n\nCommon Magic Affinities: Wind, Lightning, Ice, Water\nNative Continent: Altaria\n\nAnother intelligent race, avats are theorists, and have just as much as a thirst for knowledge as argens do. They are highly respected philosophers. Along with other researchers, avats study the mysterious history of the world and the development and knowledge behind how magic is used, taking a careful look into each element. They've written many books on the subject, and are highly skilled in the use of magic due to their extensive knowledge.\n\nPress 'Enter' to return to race selection.\n")

        # Majuu Commands
        if raceBarrier == "Majuu" or raceBarrier == "majuu":
            majuuRace = input(
                "Majuu\n\nCommon Magic Affinities: Earth, Fire\nNative Continent: Xhia\n\nA race of large goat/bull like beasts that grow to a maximum of 9 to 10 feet tall, and originte from Xhia. Because of the Arduos War, the majuu people were divided amongst themsleves, some living in a higher society away from the others who live on the outskirts. The war they started ran they friendly and kind reputation into the ground. Though most majuu are gentle giants, some are hostile due to their trust issues. Some even move to Halgeis in hopes of giving a better life for their families, though the predjudice proves to make that difficult.\n\nThe color of a majuu's fur is dependent on their climate. Bright colored majuu are from warmer areas, while darker colored majuu are from colder areas. They are also known to be very skilled blacksmiths, and have created many fearsome weapons and tools in the past. Majuu are the longest living species on Phalmasia, averaging a lifespan of 200 years.\n\nPress 'Enter' to return to race selection.\n")

        # Races Exit Command
        if raceBarrier == "Back" or raceBarrier == "back":
            infoBarrier = "Back"
            break
        if raceBarrier == "Leave" or raceBarrier == "leave":
            print("Database Search Completed. Please restart program to search again.")
            quit()

    # History Input Commands
    while infoBarrier == "History" or infoBarrier == "history":
        historyBarrier = input(
            "Time Periods of Phalmasia:\n| Before Divine's Gift (BDG)\n| Post Divine's Gift (PDG)\n| The Gifter's War\n| Nabuga's Banishment\n| The Arduos War\n| Day of Black Sun\n\nLeave the database by entering 'Leave'. Go back to the home prompt by entering 'Back'.\n")

        while historyBarrier == "":
            historyBarrier = input("Please Re-enter your database restriction.\n")
        while historyBarrier != "Before Divine's Gift" and historyBarrier != "Before divine's Gift" and historyBarrier != "Before Divine's gift" and historyBarrier != "before Divine's Gift" and historyBarrier != "Before divine's gift" and historyBarrier != "before Divine's gift" and historyBarrier != "before divine's Gift" and historyBarrier != "before divine's gift" and historyBarrier != "BDG" and historyBarrier != "bdg" and historyBarrier != "Before Divines Gift" and historyBarrier != "Before divines Gift" and historyBarrier != "Before Divines gift" and historyBarrier != "before Divines Gift" and historyBarrier != "Before divines gift" and historyBarrier != "before Divines gift" and historyBarrier != "before divines Gift" and historyBarrier != "before divines gift" and historyBarrier != "Post Divine's Gift" and historyBarrier != "Post divine's Gift" and historyBarrier != "Post Divine's gift" and historyBarrier != "post Divine's Gift" and historyBarrier != "Post divine's gift" and historyBarrier != "post Divine's gift" and historyBarrier != "post divine's Gift" and historyBarrier != "post divine's gift" and historyBarrier != "PDG" and historyBarrier != "pdg" and historyBarrier != "Post Divines Gift" and historyBarrier != "Post divines Gift" and historyBarrier != "Post Divines gift" and historyBarrier != "post Divines Gift" and historyBarrier != "Post divines gift" and historyBarrier != "post Divines gift" and historyBarrier != "post divines Gift" and historyBarrier != "post divines gift" and historyBarrier != "The Gifter's War" and historyBarrier != "the Gifter's War" and historyBarrier != "The gifter's War" and historyBarrier != "The Gifter's war" and historyBarrier != "The gifter's war" and historyBarrier != "the Gifter's war" and historyBarrier != "the gifter's War" and historyBarrier != "the gifter's war" and historyBarrier != "The Gifters War" and historyBarrier != "the Gifters War" and historyBarrier != "The gifters War" and historyBarrier != "The Gifters war" and historyBarrier != "The gifters war" and historyBarrier != "the Gifters war" and historyBarrier != "the gifters War" and historyBarrier != "the gifters war" and historyBarrier != "Nabuga's Banishment" and historyBarrier != "Nabuga's banishment" and historyBarrier != "nabuga's Banishment" and historyBarrier != "nabuga's banishment" and historyBarrier != "Nabugas Banishment" and historyBarrier != "Nabugas banishment" and historyBarrier != "nabugas Banishment" and historyBarrier != "nabugas banishment" and historyBarrier != "The Arduos War" and historyBarrier != "the Arduos War" and historyBarrier != "The arduos War" and historyBarrier != "The Arduos war" and historyBarrier != "the arduos War" and historyBarrier != "the Arduos war" and historyBarrier != "The arduos war" and historyBarrier != "the arduos war" and historyBarrier != "Day of Black Sun" and historyBarrier != "day of Black Sun" and historyBarrier != "Day of black Sun" and historyBarrier != "Day of Black sun" and historyBarrier != "day of black Sun" and historyBarrier != "day of Black sun" and historyBarrier != "Day of black sun" and historyBarrier != "day of black sun" and historyBarrier != "Back" and historyBarrier != "back" and historyBarrier != "Leave" and historyBarrier != "leave":
            historyBarrier = input("Please Re-enter your database restriction.\n")

        # Before Divine's Gift
        if historyBarrier == "Before Divine's Gift" or historyBarrier == "Before divine's Gift" or historyBarrier == "Before Divine's gift" or historyBarrier == "before Divine's Gift" or historyBarrier == "Before divine's gift" or historyBarrier == "before Divine's gift" or historyBarrier == "before divine's Gift" or historyBarrier == "before divine's gift" or historyBarrier == "BDG" or historyBarrier == "bdg" or historyBarrier == "Before Divines Gift" or historyBarrier == "Before divines Gift" or historyBarrier == "Before Divines gift" or historyBarrier == "before Divines Gift" or historyBarrier == "Before divines gift" or historyBarrier == "before Divines gift" or historyBarrier == "before divines Gift" or historyBarrier == "before divines gift":
            bdgHistory1 = "Before Divine's Gift\n| 4557 BDG - 0 BDG\n\nWhen the terrians, argens, avats, and majuu first emerged on Phalmasia over 4500 years ago, the earth was barren and tough. With no way to scupt their terrain, the population found it difficult to survive. Shelters were constructed with much difficulty, but most could not withstand the strength of the weather. The races split themselves among the four main sections of land on the planet where they could live most comfortably.\n\n"
            bdgHistory2 = "Argens chose the natural forests and mountains of the east, naming it Mu'karr. The avats took the high cliffs of the island away from the mainland seeking peace and serenity. They called it Altaria, a powerful spirit of the sky and clouds. The majuu took the smaller section of the mainland towards the south with harsh and extreme climates, naming it Xhia, a word meaning perseverence & strength. The terrians then chose the flat plains of the north, naming it Halgeis, a portmanteau of the horizon.\n\n"
            bdgHistory3 = "Now in climates and locations they were more comfortable with, they began to shape their new homes. Avats took advantage of the cliffs and made homes out of caves on the side of their mountains. Majuu made their homes of volcanic rock and forged brick, providing insulation and cooling based on the natural weather. The terrians built large towns and cities, utilizing the flat land to farm the crops they could with their limited resources. The argens used the trees of the dense forests as their homes, giving them a deeper connection to the earth and protection from the outdoor weather.\n\n"
            bdgHistory4 = "Life like this continued for many centuries. However, in 78 BDG, the world began to change. Volcanic eruptions & avalances nearly consumed all living space in Xhia. The land ran dry in Halgeis and Mu'karr, making farming near impossible and starting wildfires in the argenian forests. Earthquakes ran through Altaria, making quick work of any structures the avats had built there. By 1 BDG, they had nothing of their developments. They had prospered for centuries, and soon every race was back to how they were eons ago. They were forced to start over.\n\n"
            bdgHistory = input(
                bdgHistory1 + bdgHistory2 + bdgHistory3 + bdgHistory4 + "\nPress 'Enter' to return to history selection.\n")

        # Post Divine's Gift
        if historyBarrier == "Post Divine's Gift" or historyBarrier == "Post divine's Gift" or historyBarrier == "Post Divine's gift" or historyBarrier == "post Divine's Gift" or historyBarrier == "Post divine's gift" or historyBarrier == "post Divine's gift" or historyBarrier == "post divine's Gift" or historyBarrier == "post divine's gift" or historyBarrier == "PDG" or historyBarrier == "pdg" or historyBarrier == "Post Divines Gift" or historyBarrier == "Post divines Gift" or historyBarrier == "Post Divines gift" or historyBarrier == "post Divines Gift" or historyBarrier == "Post divines gift" or historyBarrier == "post Divines gift" or historyBarrier == "post divines Gift" or historyBarrier == "post divines gift":
            pdgHistory1 = "Post Divine's Gift\n| 0 BDG - Present\n\nGhurrado the All-Giver, the one who gave life and being to Phalmasia and those who inhabit it, saw this and went to his children, the other gods of the land, and asked them to lend their help to those below, for they have suffered enough and need a way to lead a permanent life. So they did, and they offered their gifts to the people of Phalmasia to assist them in building their lives once again.\n\n"
            pdgHistory2 = "Aha'jitt, the Goddess of Arts, gifted her Element of Nature so that people could tame the land that stood against them, and work the land into their own image. Mahar'elles, Goddess of Ease, gifted her Element of Flow, so that people may soften the land and allow the plant life to flourish. These new gifts allowed people to soften and shape the land easily around them, but they stood still once more, unable to break the land without tools.\n\n"
            pdgHistory3 = "Yumaliyu the Forgiving saw this and gifted his Element of Ambition to the world. This allowed them to forge weapons and tools to craft the land around them. He also gave them the sun to give them light. But because of the use of the Element of Ambition and the sun being unmoving in the sky, heat ran across the world unchecked. So Teverail of the Finest gifted his Element of Free Paths and cooled the land. He rotated Phalmasia around the sun, giving the world seasons, and gave his Element of Resistance as well in order to cool the land during certain times.\n\n"
            pdgHistory4 = "Then, Nabuga, their wicked mother, advised not to make it too easy for those below, and created storms and other powerful disasters to test the will and ambition of the people, as well as gifting her Element of Precision to the world. Ghurrado deemed this fair, for if the people wanted to call this land their own, they would need to suffer hardships as well as generosities. He then passed on his Element of Control and Element of Reflection, hoping to aid them in learning about the land.\n\n"
            pdgHistory5 = "Mahar'elles then gifted her Element of Harvest, so that people may have plenty of food to eat after their hard work. Nabuga spoke again, deeming it appropriate to give the people something to fear, as to test the will of their spirits. She then plagued the world with her Element of Sacrifice, forging darkness and evil into the world. When it was over, they admired their work, and began to watch from afar.\n\n"
            pdgHistory = input(
                pdgHistory1 + pdgHistory2 + pdgHistory3 + pdgHistory4 + pdgHistory5 + "\nPress 'Enter' to return to history selection.\n")

        # The Gifter's War & The Establishment of the Keepers
        if historyBarrier == "The Gifter's War" or historyBarrier == "the Gifter's War" or historyBarrier == "The gifter's War" or historyBarrier == "The Gifter's war" or historyBarrier == "The gifter's war " or historyBarrier == "the Gifter's war" or historyBarrier == "the gifter's War" or historyBarrier == "the gifter's war" or historyBarrier == "The Gifters War" or historyBarrier == "the Gifters War" or historyBarrier == "The gifters War" or historyBarrier == "The Gifters war" or historyBarrier == "The gifters war " or historyBarrier == "the Gifters war" or historyBarrier == "the gifters War" or historyBarrier == "the gifters war":
            tgwHistory1 = "The Gifter's War & The Establishment of the Keepers\n| 1064 PDG - 1076 PDG\n\nAs the people were granted the gifts of their creators, they used all of the gifts together and made the land beautiful. They established life in large fieldw, high in the mountains, through the trees, and much more. They crafted buildings to live in; villages, towns, and cities rose from the ground up.\n\n"
            tgwHistory2 = "They built shrines and temples of worship to give thanks to the Creators as well, often giving them offerings so that they all may be pleased with their hard work, and to show appreciation for all that they had done for them during their time of suffering. However, the people soon came to realise that others had given more thanks to some of the gods than others. They began to question which of their creators had done more work out of the others and who deserved more thanks over the others.\n\n"
            tgwHistory3 = "As the thought dwelled and grew in silence, the people began to argue, trying to display which of the Creators deserved more of the praiseand which gifts had been more beneficial to their cause. Ghurrado stood and watched this great war. He was hurt, for they did not understand that they all eqully contributed to bring them their new beloved world. If it had not been for all of this children and wife, the people would not have been able to craft the world in the way they wanted.\n\n"
            tgwHistory4 = "The All-Giver then decided to show the world his displeasure and would end this unneeded fighting, for he didn't wish to see his people fight when there was so much good left to be observed. So he took earth, water, fire, ice, shadow, and iron, and built The Six Keepers.\n\n"
            tgwHistory5 = "Of earth came Guranjo the Puppet, who tried to sway the people away from unnecessary fighting.\n\nFrom ice came Achina the Ice Tower, who attempted to block arrows and weapons from clashing with each other.\n\nFrom fire came Opherius the Scorched, who burn the land and keep people away from one another.\n\nFrom water came Cerrus the Lake, who created large rivers and bodies of water to keep the people divided from one another.\n\nFrom shadow came Yulektia the Graveyard, who showed the people to respect the passing of others and to display the evil of the war.\n\nAnd of iron came Impervius the Iron Maiden, who would punish the corrupted and evil.\n\n"
            tgwHistory6 = "To give them life, he granted them the Life Stone, a rune sealed with unfathomable amounts of Life Energy & Magic, and sent them out to the world to carry on their missions. Several years had passed, and The Six Keepers ended the warring of the people. They then went their separate ways, each of them finding their own homes and going into a deep slumber until they were needed again...\n\n"
            tgwHistory = input(
                tgwHistory1 + tgwHistory2 + tgwHistory3 + tgwHistory4 + tgwHistory5 + tgwHistory6 + "\nPress 'Enter' to return to history selection.\n")

        # Nabuga's Banishment & The Creation of the After Palace
        if historyBarrier == "Nabuga's Banishment" or historyBarrier == "Nabuga's banishment" or historyBarrier == "nabuga's Banishment" or historyBarrier == "nabuga's banishment" or historyBarrier == "Nabugas Banishment" or historyBarrier == "Nabugas banishment" or historyBarrier == "nabugas Banishment" or historyBarrier == "nabugas banishment":
            nbapHistory1 = "Nabuga's Banishment & The Creation of the After Palace\n| 1077 - 1322 PDG\n\nAs more years passed Ghurrado became pleased wth how things had changed. After seeing the errors of their ways, people began to worship all creators eqully, and gave them all praise in respect to the elements they had been gifted with. Nabuga, however, was the only one who received no recognition of any kind, and began to feel bitter.\n\n"
            nbapHistory2 = "She had helped to build the world as well. If Ghurrado and her children were being praised for therir efforts, she believed that she should as well. Conflict was important, after all. Without it, how do people grow? How do they learn to adapt? As time passed, Nabuga's anger and jealousy grew, and out of malice, Nabuga plagued the world with a disease to enact on her displeasure. Ghurrado saw this, and quickly cleansed the world of it. Ghurrado then told her that her actions were unnecesary and cruel.\n\n"
            nbapHistory3 = "He was truly sorry that she didn't receive any of the praise she deserved, but with more time he promised that it would come to her. But this wasn't enough for her. Over time, her hatred for the people shifted to her family, and she planned to dispose of them directly instead. One day, Nabuga attacked her youngest son, Yumaliyu, and brought him to the brink of death. At the last moment, Ghurrado intervened and stopped Nabuga from finishing her attack.\n\n"
            nbapHistory4 = "Seeing Nabuga like this, Ghurrado became very sad. The two fought for three days and nights until Nabuga went into a horrible fit, attacking her husband with unrestrained force through her blinded rage. At this, Ghurrado had enough, and had no choice but to banish his wife from their home, stripping her of some of her power and placed her in the world's core. She then had The Six Keepers build her a home, so that she may live there on her own.\n\n"
            nbapHistory5 = "Then, Ghurrado had an idea. Nabuga threw this fit because she wanted praise, and so she would get it. He created an entire new world underneath his own, granting Nabuga the power to watch over it. Those who passed on were sent to this world where Nabuga was god and was to be worshipped. As time passed on, rumor spread in the overworld thata wicked queen had come to watch over the dead from that point on.\n\n"
            nbapHistory = input(
                nbapHistory1 + nbapHistory2 + nbapHistory3 + nbapHistory4 + nbapHistory5 + "\nPress 'Enter' to return to history selection.\n")

        # The Arduos War
        if historyBarrier == "The Arduos War" or historyBarrier == "the Arduos War" or historyBarrier == "The arduos War" or historyBarrier == "The Arduos war" or historyBarrier == "the arduos War" or historyBarrier == "the Arduos war" or historyBarrier == "The arduos war" or historyBarrier == "the arduos war":
            tawHistory1 = "The Arduos War\n| 3968 - 3971 PDG\n\nKing T'llas Arduos had been crowned as the ruler of Xhia. His family had peacefully ruled for hundreds of years up until he had been crowned. He was extremely powerful, wielding both earth and fire magics, but as a king he was tyrranical. He believed that the Majuu were the superior race due to them having the strongest magics, and the innate ability to smith powerful weapons. In 20 years, he had overtaken the entire continent, and ruled over it for another 30.\n\n"
            tawHistory2 = "Due to his extreme power, Arduos drove himself insane. Seeking more power, he wished to expand his land even further into the other continents. He waged war on the other continents and immidiately sent troops to overpower them. Innocent majuu who dissented against the war were put into slavery by their own kind; by soldiers of Arduos who believed that he was right. Altaria, Mu'karr and Halgeis quickly banded the little troops they had together to fight back.\n\n"
            tawHistory3 = "Arduos' troops first struck over the water, hoping to stop Altarian troops from reaching Mu'karr. However, majuu had no experience fighting on water, and they were easily defeated. Once the battle hit land, though, the tides changed. The allied army stood no chance against the majuu; their magic and weapon mastery was too great. The allies had to find a way to stop the majuu from advancing towards them. They only thought of one way.\n\n"
            tawHistory4 = "Xhia, before the war, hosted forests, though nowhere near as vast as their neighbor Mu'karr. During the war, however, the allies send all the pyromancers they could to the frontlines, and had them burn the forest that the majuu needed to pass through to get to Mu'karr. Arduos, understanding that the majuu had innate ability to withstand the flames and magic, ordered them to continue through the burning forest. Even with their abilities, the flames were too great.\n\n"
            tawHistory5 = "Arduos' general (still unknown and unnamed), refused to send more troops to their deaths in the wildfire. He knew that the flames were causing them to lose the war. Arduos was furious, and insisted that the war was for the people, therefore it was more important than the lives of the people. The war would bring them more land, more freedom, more peace! One final time, he ordered the general to send the troops through the flames.\n\n"
            tawHistory6 = "Throughout all of this, the general had always opposed the war. It was a burden, a strain on the lives of the people, and something many didn't want to be associated with. They thought long and hard with the general's back turned to him. He had finally had enough, and drew his sword, piercing it into Arduos and ending his live as well as the war. The general aimed to fix all of the damage the war had caused, and convinced the other continents to help in extinguishing the fire.\n\n"
            tawHistory7 = "After that, the majuu lost their reputation as a calm and peaceful race. The war bred contempt, and many still keep that hatred to this day.\n\n"
            tawHistory = input(
                tawHistory1 + tawHistory2 + tawHistory3 + tawHistory4 + tawHistory5 + tawHistory6 + tawHistory7 + "\nPress 'Enter' to return to history selection.\n")

        # The Day of Black Sun
        if historyBarrier == "Day of Black Sun" or historyBarrier == "day of Black Sun" or historyBarrier == "Day of black Sun" or historyBarrier == "Day of Black sun" or historyBarrier == "day of black Sun" or historyBarrier == "day of Black sun" or historyBarrier == "Day of black sun" or historyBarrier == "day of black sun":
            dbsHistory1 = "The Day of Black Sun\n| 4030 PDG\n\nThings in the world returned to somewhat normalcy after the resolution of the Arduos war, albeit some new stigmas and biases towards the populace of the majuu race. However, in 4022, those in the Mu'karr began reporting strange weather patterns. Summers were hotter than the years before, and winters colder. Thunderstorms were much more common, and blizzards brought much more snow than expected. Most strangely, the aurora borealis was in the sky nearly every week.\n\n"
            dbsHistory2 = "The argens of Mu'karr couldn't understand why the weather had changed so drastically over such a short time, but they assumed it would pass after a year or two. The weather wasn't causing any major damage or problems, so life continued on as normal. However, one day, a large object shifted in front of the sun, causing a makeshift solar eclipse. Confusion was spread all throughout Mu'karr and Halgeis (as both of them shared the same time in the sun). Unlike the weather anomalies, this issue was prominent.\n\n"
            dbsHistory3 = "How had something so large that it could block out the sun entirely get so close to Phalmasia without anyone noticing? After seeing this, it was determined that the strange celestial object, a large meteor made of some sort of black stone, was the cause behind the abnormal weather. Many people theorized that it could be the divines, angry at the Arduos War, and wanted to scare them for their wrongdoings. The meteor came and went after a few minutes, and with it went the strange weather.\n\n"
            dbsHistory4 = "People seemed to have forgotten about the meteor in everyday life for a few years. But they were promptly reminded of its existence when it returned. Instead of a solar eclipse blocking out the sun, it was not hurdling towards the ground with massive force towards a direct path with Entrype, a small village in Mu'karr. Many warriers were trying to do everything they could to stop it from reaching the surface with their magic, but it was ineffective.\n\n"
            dbsHistory5 = "Only a few were strong enough to make contact with the meteor while it was so far away, and even then the distance caused whatever spells they had to grow too weak to slow it down. The defenders of the village were forced to flee and evacuate everyone, though it was hopeless. If a meteor of that size and speed made contact, all of Phalmasia would likely be disrupted and even destroyed. Just then, however, a flash of light was seen from the village center, and a ray of black energy shot into the sky.\n\n"
            dbsHistory6 = "The ray was forceful enough to make contact with the meteor, and was even able to push back against it. It wasn't enough, though. It wouldn't slow down enough to matter when it hit the ground, and once again all hope was lost. But suddenly another flash was seen from the village center, this time eminating a light similar to that of the aurora in the sky. Shortly after, the ray became bright and colorful, growing far more forceful and large.\n\n"
            dbsHistory7 = "The meteor was effectively responding to the newfound ray, and slowing down much faster. It was enough to drop the meteor slowly onto the ground, saving not only the lives of the fleeing villagers, but of all of Phalmasia. Those who saw it quickly ran to the village center to thank the mysterious being who saved their lives. But they were suprised to meet a small boy who lived in the village at the center, covering someone else. Instead of thanking him as planned, the people grew fearful.\n\n"
            dbsHistory8 = "How could a young boy hold enough power to stop a force the entire defense system couldn't? The people stepped back, and the village defenders chased him out of the village. The boy brought the one he was protecting away with him, and was never seen or heard from again. That day went down in history as the Day of Black Sun, and the boy became a legend; some feared him for his power, some revered him for his actions. No one saw his face, so no one knew who he was, but they began to call him by his unique magic: The Boy of Cosmic Wind.\n\n"
            dbsHistory = input(
                dbsHistory1 + dbsHistory2 + dbsHistory3 + dbsHistory4 + dbsHistory5 + dbsHistory6 + dbsHistory7 + dbsHistory8 + "\nPress 'Enter' to return to history selection.\n")

        # History Exit Command
        if historyBarrier == "Back" or historyBarrier == "back":
            infoBarrier = "Back"
            break
        if historyBarrier == "Leave" or historyBarrier == "leave":
            print("Database Search Completed. Please restart program to search again.")
            quit()

    # Intro Exit Command
    if infoBarrier == "Leave" or infoBarrier == "leave":
        print("Database Search Completed. Please restart program to search again.")
        quit()
    if infoBarrier == "Back" or infoBarrier == "back":
        infoBarrier = "Return"
    else:
        input("The data you have requested has not yet been implemented. Check back in a future release version.")