class Item():
    def __init__(self, name, descr, pick, item_use):
        self.name=name
        self.descr=descr
        self.pick=pick
        self.item_use=item_use
        self.item_used_alone=False
        self.item_used_with_otherItem=False


class Inventory():
    def __init__(self):
        self.inventory= []
    
    def addItem(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
        else:
            return

    def removeItem(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return

# General thought: Add a condition for not being able to pick up an item

inventory=Inventory()

room1_blaster_use={"self":"I really don’t want to discharge this weapon indoors. In any event, I need to save up the charge for whatever’s coming."}
room1_blaster=Item("blaster","My standard issue blaster. It’s charged from the night before, but I check it again just in case. Who knows what trouble I’ll be getting into this morning. The weight of the weapon feels reassuring in my hands.",True,room1_blaster_use)

room1_knife_use={"self":"I don’t want to use this weapon unless I really have to."}
room1_knife=Item("knife","A knife I’ve had since my days in the slums of San Weyhoon. Looking at it brings back bad memories.",True,room1_knife_use)

room1_diploma_use={"self":"I can't use this"}
room1_diploma=Item("diploma","A crisp, moderately-sized piece of paper that started it all. I remember feeling so happy when I was presented with it… A lifetime ago.",False,room1_diploma_use)

room1_photograph_use={"self":"I can't use this"}
room1_photograph=Item("photograph","This is the standard-issue photograph of the Admiral, which every member of Chronosia Industries is required to have in their possession. I never liked the way the Admiral looked in it - it’s heavily edited, to the point where I don’t feel like I get a sense of the person depicted in it.",False,room1_photograph_use)

room1_keycard_use={"self":"I can't use a key on its own... I have to use this with something.","door":"I've unlocked the door... I guess I can go now, and see what Commander Paulson wants from me."}
room1_keycard=Item("keycard","A small plastic keycard with my name on it. It locks the door to my quarters - nothing special about it.",True,room1_keycard_use)

room1_door_use={"self":"It won't open... I need to unlock it first. Do I have something I can use?","key":"Good thinking, but I need to use the key on the door, not the other way around."}
room1_door=Item("door","It's the door that leads out of my quarters, to the rest of the compound. I should probably get out of here and see what the Commander wants from me.",False,room1_door_use)

room1_article_use={"self":"It's the latest issue of the cadet newspaper. Some conspiracy theory about the death of Commander Yu, who was murdered by the Shogunate a few months ago... Absolute nonsense."}
room1_article=Item("article","It's the latest issue of the cadet newspaper. Some conspiracy theory about the death of Commander Yu, who was murdered by the Shogunate a few months ago... Absolute nonsense.",False,room1_article_use)

room1_advert_use={"self":"It's an advert for the Chronosia Industries museum, a couple of blocks from here... I remember visiting it as a child. Some of the exhibits were a little corny, to be honest."}
room1_advert=Item("advert","It's an advert for the Chronosia Industries museum, a couple of blocks from here... I remember visiting it as a child. Some of the exhibits were a little corny, to be honest.",False,room1_advert_use)

room1_items=[room1_blaster,room1_knife,room1_diploma,room1_photograph,room1_keycard,room1_door, room1_advert, room1_article]

puzzle1="The phosphorescent light in my quarters is easy on the eyes, even this early in the morning. I should arm myself before I go." 
puzzle2=f"I look around the room and see my [{room1_blaster.name}] sitting in its charging dock on the far side of the wall. After some rummaging under my pillow, I am glad to feel the comforting shape of my old [{room1_knife.name}] still lying there. "
puzzle3=f"I feel a tinge of sadness, looking at my barren surroundings. Compared to some of the other Cadets, who decorate their walls with posters of famous holostars and virtu-divas, my living space looks like I had only just moved in. The only object of note is my entrance [{room1_diploma.name}], which hangs just beside the door, and a framed [{room1_photograph.name}] of Admiral Radius, which stands on my bedrest. Under the door are a newspaper [{room1_article.name}] and an [{room1_advert.name}] that someone slipped in... I guess I can have a look, but I should probably leave them here."

room1=[puzzle1,puzzle2,puzzle3]

puzzle4="I have my weapons on me now, and I feel a little safer - though not by much. It's time to get out of here."
puzzle5=f"I open the drawer by my bedside table - inside is my [{room1_keycard.name}], which opens the main [{room1_door.name}] opposite my bed."

room1_changed=[puzzle4,puzzle5]

dialogue1_1_option="[1] ‘I don’t get it. Is this so important that I had to be woken up at three in the morning?’"
dialogue1_1_2="The Commander frowns."
dialogue1_1_3="‘Cadet, I do not need to tell you the importance that San Weyhoon Municipality have as our client. We have been serving them since our company’s incorporation, and their fees are directly responsible for the clothes on your back."
dialogue1_1_4="For years they have been asking us to get rid of The Shogunate - and their leaders - off the streets of San Weyhoon. And now - with their chief lieutenant captured - we might finally have a shot to do just that."
dialogue1_1_5="So, in short - yes, I do think it’s that important.’ "
dialogue1_1=[dialogue1_1_option,dialogue1_1_2,dialogue1_1_3,dialogue1_1_4, dialogue1_1_5]

dialogue1_2_option="[2] ‘Who are the Shogunate again?’"
dialogue1_2_1="‘I’m going to assume that that was an attempt at a joke."
dialogue1_2_2="We’ve been trying to drive The Shogunate out of the city for years."
dialogue1_2_3="It’s one of the most feared - and deadly - gangs in the entire city."
dialogue1_2_4="If you don’t know who they are, I’m going to send you to medical so that they can check you for brain tumours.’"
dialogue1_2=[dialogue1_2_option,dialogue1_2_1,dialogue1_2_3,dialogue1_2_4]

dialogue1_3_option="[3] ‘You might need to jog my memory about On-Lam. He’s the designated chef for the Cadet meals, right?’"
dialogue1_3_1="‘You’re a soldier, not a comedian, Cadet. But if, for whatever reason, you need me to jog your memory - On-Lam is the chief lieutenant of The Shogunate, famous for her unflinching brutality."
dialogue1_3_2="She was personally responsible for the massacre at Sakura Docks, and we have been trying to capture her for several years."
dialogue1_3_3="In the gang, she is second only to In-Ran, the head chief."
dialogue1_3=[dialogue1_3_option, dialogue1_3_1, dialogue1_3_2, dialogue1_3_3]

dialogue1_4_option="[4] ‘Which Enforcer ended up capturing On-Lam?’"
dialogue1_4_1="‘Classified. Next question.’"
dialogue1_4=[dialogue1_4_option,dialogue1_4_1]

dialogue1_5_option="[5] ‘How did the Shogunate get so sloppy?’"
dialogue1_5_1="The Commander shrugs."
dialogue1_5_2="‘Everyone gets sloppy one day, Cadet."
dialogue1_5_3="Let’s hope that today is not that day for you.’"
dialogue1_5=[dialogue1_5_option,dialogue1_5_1,dialogue1_5_2,dialogue1_5_3]

dialogue1_exit_option="[0] ‘Why me?’"

dialogue1=[dialogue1_1,dialogue1_2,dialogue1_3,dialogue1_4,dialogue1_5,dialogue1_exit_option]

dialogue2_1_option="[1] ‘For the record, I would like you to state your name.’"
dialogue2_1_1="The floating body convulses slightly and I realise that On-Lam must be laughing." 
dialogue2_1_2="‘My name, Chrono-scum?"
dialogue2_1_3="You would like to know my name?"
dialogue2_1_4="You know my name." 
dialogue2_1_5="It haunts the dreams of all who toil at your palace of rot."
dialogue2_1_6="Chronosia Industries will fall, alongside all who take its side.’" 
dialogue2_1_7="…"
dialogue2_1_8="Big words, I think to myself, for a woman in chains."
dialogue2_1=[dialogue2_1_option,dialogue2_1_2,dialogue2_1_3,dialogue2_1_4, dialogue2_1_5, dialogue2_1_6, dialogue2_1_7, dialogue2_1_8]

dialogue2_2_option="[2] ‘Where are the boxes, On-Lam?’"
dialogue2_2_1="‘Boxes?’"
dialogue2_2_2="I can see that horrid gash on her face curl upwards."
dialogue2_2_3="‘I know nothing of boxes. Are you sure you don’t have me mixed up with someone else?’"
dialogue2_2=[dialogue2_2_option,dialogue2_2_1,dialogue2_2_2,dialogue2_2_3]

dialogue2_3_option="[3] ‘Why do you hate the people of this city so much?’"
dialogue2_3_1="I can’t see her eyes but I can sense that she is looking at me with a sense of pity."
dialogue2_3_2="‘The very fact that you ask this question tells me you have not been outside in a very long time.’"
dialogue2_3_3="She is quiet for a moment, and then continues, softly."
dialogue2_3_4="‘I don’t hate the people of this city at all. I love them."
dialogue2_3_5="And I don’t know which would be worse - if you didn’t understand that, or if you didn’t care."
dialogue2_3=[dialogue2_3_option,dialogue2_3_1,dialogue2_3_2,dialogue2_3_3,dialogue2_3_4,dialogue2_3_5]

dialogue2_4_option="[4] ‘You know we’re eventually going to catch you and your people, right? You are just the first in a long line of upcoming arrests.’"
dialogue2_4_1="‘That’s what you think, Chrono-scum."
dialogue2_4_2="I think you might change your mind on that before the day is done.’"
dialogue2_4_3="Something about the way she says that makes me incredibly uneasy."
dialogue2_4=[dialogue2_4_option,dialogue2_4_1,dialogue2_4_2,dialogue2_4_3]

dialogue2_5_option="[5] ‘How can you live with yourself, having killed that many people?’"
dialogue2_5_1="‘Have you ever had to kill a cockroach, Chrono-scum?"
dialogue2_5_2="They are worthless beings, which cause havoc and displeasure to honest, hard-working citizens."
dialogue2_5_3="That’s what you are - vermin, to be exterminated."
dialogue2_5_4="No regrets’"
dialogue2_5=[dialogue2_5_option,dialogue2_5_1,dialogue2_5_2,dialogue2_5_3,dialogue2_5_4]

dialogue2_exit_option="[0] ‘You and I both know that words won’t get us anywhere. Why are we wasting our time here?’"

dialogue2=[dialogue2_1,dialogue2_2,dialogue2_3,dialogue2_4,dialogue2_5,dialogue2_exit_option]