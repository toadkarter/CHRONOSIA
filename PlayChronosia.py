# Needed to clear the screen
import os

# Needed for char by char effect
import sys
import time

line1="[Welcome, Cadet! Glory to Admiral Radius!]"
line2="[Congratulations are in order. By reaching this point in your training you have shown impeccable physical prowess, mental discipline, and unflinching loyalty to Chronosia Industries and its values.] "
line3="[Unfortunately, duty prevents Admiral Radius from congratulating you on this significant achievement in person. He has, however, signed off on the text in this automated welcome message - you may view this as a communication by proxy if you so wish.]"
line4="[There are very few that make it to this point in the training program - no doubt many of your colleagues, some of whom you may even have called friends - have dropped out due to the intense stress and high demands placed upon your young shoulders.] "
line5="[This is a direct credit to you. We have culled the weak, and you remained. Allow yourself a moment to experience pride.]"
screen0=[line1,line2,line3,line4,line5]

line6="[But one thing yet eludes you - something that we test for rigorously before we allow a Cadet to become an official Chronosia Industries Enforcer.]"
line7="[You may have felt tremors of its call, dreams and visions of experiences seen through a dark mirror…]"
line8="[A whisper of things that yet may be.]"
screen1=[line6,line7,line8]

line9="[Yes, Cadet, we are of course talking of SightParsing. Your final step before you are able to walk the streets, doling out justice on behalf of our clients.]"
line10="[No doubt the mandatory surgery you undertook before becoming a Cadet has aided you in developing this talent… But sadly, despite decades of research, we have not been able to induce SightParsing through surgery and training alone.]"
line11="[We have discovered that SightParsing instead requires a singular, focal point of exertion on behalf of the test subject - a moment of acute stress that finally unveils the talent within the individual]"
line12="[In our experience, a field exam is the best way to generate such a moment.]"
screen2=[line9,line10,line11,line12]

line13="[Unfortunately, as you may be aware, our Legal Team has recommended that we suspend all field exams until the unfortunate incidents that took place during the last several tests have been fully investigated.]"
line14="[As such, the Chronosia Industries R&D Department has created this interactive experience as a final test for you.]"
line15="[It is based on real events experienced by one of our finest Enforcers, Ambrosia Monad. Some of you may have even met Enforcer Monad, and those individuals will no doubt attest to the strength of her character.]"
line16="[As you are no doubt aware, her recent death at the hands of the vile Shogunate has sent shockwaves across San Weyhoon - her murder, like the murder of Commander Emily Yu before her, will be avenged. Perhaps it will be you that dispenses justice at the hands of our enemies!]"
line17="[Please try to react to the events in this interactive experience as naturally as possible.]"
screen3=[line13,line14,line15,line16,line17]

line18="[One final point before we begin: any messages that you encounter that are surrounded by square brackets (much like this message) are NOT part of the experience. They are guidance notes to help you navigate the interface of this terminal.]"
line19="[Best of luck, Cadet! Glory to Admiral Radius!]"
line20="[NOTE: The Chronosia Industries Legal Department would like to stress that none of the views expressed in this interactive experience represent the views of Chronosia Industries or any of its parent and/or holding companies]"
screen4=[line18,line19,line20]

line21="<START>"
line22="Hello, Cadet, and welcome to this interactive experience - starring none other than me, Enforcer Monad! Glory to Admiral Radius! "
line23="Let me regale you of the story of what happened on that noble day when I was finally able to induce my SightParsing ability. "
line24="It all started when - "
screen5=[line21,line22,line23,line24]

line25="…"
line26="…"
line27="…"
screen6=[line25,line26,line27]

line28="<START>"
line29="Hey…  Is this thing on?"
line30="Yeah? "
line31="OK, fine. Yes. "
line32="…"
line33="Understood. Introduce myself?"
line34="Alright then. "
screen7=[line28,line29,line30,line31,line32,line33,line34]

line35="To whoever is reading this… hello. I’ve been asked to introduce myself, so here I am, I guess, doing just that."
line36="Although I gotta say, it feel pretty damn odd talking out loud like this. "
screen8=[line35,line36]

line37="My name is Ambrosia Monad. I am an Enforcer. "
line38="Enforcer… I’ve been calling myself that for a few weeks now, but saying it out still feels new to me. I suppose the person reading this will go through the same thing… Well. I hope so, at least. "
screen9=[line37,line38]

line39="Hey you, behind the glass - is any of this coming through? You guys getting the recording OK? "
line40="Good. Alright. "
line41="Ah, they’ve left now. I guess they did tell me they would do that. They said that it’s to give me some privacy, to make sure that I can give as subjective an account of what happened as possible, but who are they kidding. "
line42="We both know that as soon as I am done here, the guys in legal will be crawling all over this text to make sure that I didn’t hurt the feelings of any Chronodrones up on the top floor. "
line43="It’s not like I care, anyway. After what I saw… I know that I’m on my way out. Might as well be as honest as I can, while I still can. Maybe someone, somewhere will be able to read this unedited version, before it’s sanitised and mutilated beyond all recognition. "
screen10=[line39,line40,line41,line42,line43]

line44="Some background - they called me in a couple of days, put me under sedation and stuffed some kind of subdermal pad under my left ear. Hurt like hell but that’s par the course for this job. "
line45="They asked me to give my account of how exactly I induced my SightParsing ability. All I have to do is talk, and the pad will act as some sort of emotional translator, editing the transcript to match my feelings and emotions more accurately. "
line46="I don’t really know how the tech behind this works, nor do I particularly care."
line47="They said that this thing will be popped into a computer and used as training for future Cadets, which gave me a good chuckle. "
line48="No way in hell that typing commands at a computer could replicate what I went through on that day…"
screen11=[line44,line45,line46,line47,line48]

line49="No matter."
line50="I’ll do what they asked of me, and then I will face the consequences for following their instructions. It’s the only honorable thing to do given the circumstances. "
line51="If you are reading this, it’s very possible that I have been terminated for my actions. Hell, it’s entirely possible that recording will be deleted from existence, my memories lost forever. "
screen12=[line49,line50,line51]

line52="It’s possible. But there’s still a chance."
line53="And it’s a chance I’m going to take. "
line54="Are you ready, Cadet?"
line55="Let’s begin."
screen13=[line52,line53,line54,line55]

line56="[Date: 15 October 2115]"
line57="[Time: 03:02]"
line58="[Location: Chronosia Industries Cadet Barracks, Individual Quarters]"
screen14=[line56,line57,line58]

line59="I wake sharply to the godawful, stabbing sound of my commlink. "
line60="Christ almighty. "
line61="What time is it? "
screen15=[line59,line60,line61]

line62="Still half-asleep, muscles aching from yesterday’s fitness diagnostic, I fumble blindly in the dark at the source of that horrible noise. "
line63="Ah. There it is. "
line64="I stab at the ‘answer’ button groggily, and the noise, mercifully, cuts out."
screen16=[line62,line63,line64]

line65="-Cadet Monad speaking. How may I be of assistance? "
line66="-Get ready for deployment in 10 minutes, Cadet. Make sure you’re fully armed. Do not be late. "
line67="And then the comm goes silent. "
screen17=[line65,line66,line67]

line68="I could recognise that gravelly voice anywhere… "
line69="Commander Paulson has been my superior since my earliest days at Chronosia Industries. Shee reports directly to Admiral Radius, which means that she is also directly responsible for making sure that all Cadets within the company are worthy of their title. "
line70="She is extremely good at his job, mostly due to complete lack of squeamishness when it comes to discipline… I certainly have the bruises to prove it. "
screen18=[line68,line69,line70]

line71="There’s an awful feeling at the pit of my stomach as I fuss over my uniform. "
line72="Something doesn’t feel right. "
line73="Paulson is a hard-ass, sure, and she has woken us up in the middle of the night before, but never with this much short notice. "
line74="I check the display of my commlink and notice that the heart rate of all other Cadets is low… They are asleep. "
line75="I am the only one that has been summoned for… whatever this is. "
screen19=[line71,line72,line73,line74,line75]

line76="[Greetings once more, Cadet, and apologies for interrupting your interactive experience!]"
line77="[As mentioned previously, you can tell that this is a message from the program and is NOT part of the experience as the words are contained within square brackets.]"
screen20=[line76,line77]

line78="[You are about to engage with a navigation problem, the first of many, which simulates decisions that Enforcer Monad experienced during this time period.]"
line79="[Thankfully, the first problem is extremely simple, and as such you should take the opportunity to familiarise yourself with the commands available to you.] "
line80="[Future problems - which will be more challenging - will use the same controls and commands.]"
line81="[Would you like to read through the instructions?]"
line82="[You will be able to read the instructions later by typing 'tutorial' in a gameplay section even if you don't read them now.]"
screen21=[line78,line79,line80,line81,line82]

line83="[The text in the problem will feature certain objects that you can interact with. They will be surrounded by square brackets]"
line84="[To utilise the ‘Examine’ command, type ‘examine obj’, with the letters ‘obj’ replaced by the object you want to examine. For example - ‘examine key’. You will receive a short description of the object.]"
line85="[To utilise the ‘Pick’ command, type ‘pick obj’, with the letters ‘obj’ replaced by the object you want to pick up. For example - ‘pick key’. You will add the object to your inventory]"
line86="[To utilise the ‘inventory’ command, type ‘inventory’. You will be able to see the objects you have in your inventory.]"
screen22=[line83,line84,line85,line86]

line87="[To utilise the ‘Use’ command, type ‘use obj1’ or ‘use obj1 obj2’, with the letters obj1 and obj2 replaced by the objects that you want to use. The form ‘use obj1 obj2’ will result in obj1 being used on obj2, for example ‘use key door’ will result in the key being used on the door.]"
line88="[Please note that sometimes objects may be hidden inside other objects, and as such will not be immediately visible. Make sure to examine all object carefully, and choose the ‘use’ button on objects frequently to see what what can be done with them - it might not be obvious in the first instance]"
line89="[To view these instructions again, type ‘tutorial’ in the commands section.]"
line90="[Best of luck - and glory to Admiral Radius!]"
screen23=[line87,line88,line89,line90]

line91="[Congratulations Cadet - you have completed your first navigation problem!]"
line92="[Rest assured - going forward these will not be as easy.]"
line93="[Let us resume with the scheduled programming.]"
screen24=[line91,line92,line93]

line94="All traces of sleep are gone now, as I lock the door to my quarters behind me and make my way to the Briefing Room. "
line95="I am immediately drawn to the worst case scenario. Am I finally getting dropped from the programme? "
line96="My performance has been consistently above average for months, so it doesn’t seem likely that they’ll boot me for lack of progress. "
line97="There have been a few altercations with some of the instructors, but that’s par the course with Cadets. To be honest, I sometimes feel like Commander Paulson encourages it. "
line98="As Enforcers, it’s not likely that we will survive without being able to confront those who stand against us, whether it be through words or through violence. "
screen25=[line94,line95,line96,line97,line98]

line99="I turn the corner and finally see the door to the Briefing Room ahead of me. It’s a large, metal door, dented and scarred from generations of Cadets, Enforcers and Commanders cutting notches in it on their way in and out of meetings. "
line100="They say it’s good luck. "
line101="I never believed it, but as I open the door and walk into the large auditorium inside, the thought of making a little notch crosses my mind."
screen26=[line99,line100,line101]

line102="The smell of tobacco hits me immediately. It’s a large room, but Paulson’s legendary smoking habit has been at work here. I can barely make her out in the center, sitting behind a desk so large it’s almost funny.. "
line103="Paulson is a short woman, so all I can see of her behind that monstrosity of a table is her tiny head. "
line104="Her glasses glisten menacingly in the dark."
screen27=[line102,line103,line104]

line105="- Glory to Admiral Radius. Have a seat, Monad."
line106="I walk over to the chair opposite my commander, trying not to cough from all the smoke. "
line107="She looks at me for a while after I’ve sat down. Her glasses hide any sign of her motives for calling me in here. "
line108="I stay quiet, waiting for her to speak. "
screen28=[line105,line106,line107,line108]

line109="…"
line110="…"
line111="…"
line112="- Well, then. I guess I’ll get right down to it."
line113="The Commander picks up a glass of water and sips pensively. For a moment, I can see the water’s reflection in her glasses, and the reflection of the glasses in the water. "
line114="The effect is dizzying. "
line115="I feel unwell."
screen29=[line109,line110,line111,line112,line113,line114,line115]

line116="- We’ve caught On-Lam. "
line117="My heart stops. How?"
screen30=[line116,line117]

line118="The Commander pauses, clearly enjoying this shocking reveal, before continuing."
line119="- And we want you to interrogate him. I’m sure you have a lot of questions, Cadet. Be quick about it - we will need to get started soon."
screen31=[line118,line119]

line120="She takes off her glasses and rubs them with a handkerchief. "
line121="The thick smoke still makes it hard to see her eyes clearly, but I can tell that she’s tired."
screen32=[line120,line121]

line122="- I was sure you would be wondering why you’ve been tasked with interrogating a high-ranking member of one of the most feared gangs in this city. "
line123="The simple answer is - I think you’re ready. "
line124="I know we’ve had our differences over the years, but you are an exemplary Cadet. If this goes well… I’ll be personally recommending you for the position of Enforcer.’"
screen33=[line122,line123,line124]

line125="I knew this day would come, but I am still shocked. "
line126="It makes sense, I suppose - no-one stays a Cadet for over a decade, they either flunk out or get promoted - but it still doesn’t feel real. "
line127="I get the odd sensation of watching my own body from a distance, as if I am detached from what’s going on. "
screen34=[line125,line126,line127]

line128="Paulson’s glasses seem to sparkle, and I think I can see a hint of a smile. Or a smirk. "
line129="- This is a great honour for you, Cadet. But be aware that this will be a challenge unlike anything you have faced yet."
line130="On-Lam is not a happy woman right now, and she has not taken kindly to being captured. If I may make a suggestion…"
line131="You should probably start off with a verbal interrogation. See what she gives willingly. "
line132="After that, you can use the Melt."
screen35=[line128,line129,line130,line131,line132]

line133="I am suddenly grateful that I enrolled in extra Melt training a few years back. "
line134="The mental fortitude required for such a procedure is strenuous enough with a willing subject, let alone a criminal like On-Lam. "
screen36=[line133,line134]

line135="- The Melt will let you see - and feel - On-Lam’s experiences up until her capture as if you were On-Lam herself. "
line136="Be aware that she knows that our officers can use the Melt - she probably has psychic defenses up against such methods. She may have several cover stories concocted to throw you off course."
line137="Make sure that you explore her mind thoroughly, and try to make decisions that you think the true On-Lam will have made - that way you will find the true path through her mind. "
line138="The things you will see… they may be deeply unpleasant, to say the least. "
line139="Just be aware that they represent events the way On-Lam experienced them, not necessarily the way they happened. "
screen37=[line135,line136,line137,line138,line139]

line140="We know that right before her capture, On-Lam had in his possession four containers, which look like perfectly black cubes."
line141="She no longer had them on her when she was captured. "
line142="Your goal is to enter her mind and figure out where exactly she left them, so that we can retrieve them. "
line143="I cannot tell you what those containers contain… but what I can tell you is that their contents are of extreme importance to our client. "
line144="You *must* find out their location."
screen38=[line140,line141,line142,line143,line144]

line145="She leans back in her chair. "
line146="- My final piece of advice to you, Cadet."
line147="I know you and your peers have long awaited the gift of SightParsing - the final requirement you need to fulfil before you have all the skills you need to become an Enforcer. "
line148="This final test that I have set in front of you…"
line149="This is the exact set of stressful circumstances that you need to activate this gift. "
line150="You will be in great danger, and you will feel out of your depth - at times you may feel like you have failed, even - but just remember…"
screen39=[line145,line146,line147,line148,line149,line150]

line151="Failure is not the end - it’s a new beginning."
screen40=[line151]

line152="And then we both go quiet, sitting in the smoky room, waiting for… something. "
line153="- If you’re ready, Cadet?"
line154="I nod."
line155="“I’m ready, Commander.”"
screen41=[line152,line153,line154,line155]

line156="- Good. As I’m sure you’re aware, On-Lam’s location is highly classified, even to you. I will have to sedate you before transporting you over to her."
line157="Paulson walks over and I can see a syringe in her left hand. "
line158="I’m not scared of needles, but my skin crawls as she gently pokes the sedative into my neck and pushes the plunger. I barely feel a thing. "
line159="My vision blurs, and the only thing I can see is the Commander’s glasses, the only constant in a room full of smoke. "
screen42=[line156,line157,line158,line159]

line160="I think I hear her repeat the words, “failure is not the end” again, before my vision goes completely dark…"
line161="And then, just silence. "
screen43=[line160,line161]

line162="…"
line163="…"
line164="…"
line165="…"
line166="…"
screen44=[line162,line163,line164,line165,line166]

line167=" "
line168="I wake to harsh light and a low hum. "
line169="My body is numb, but as I try to move my extremities, I can sense the feeling slowly begin to return. "
line170="I am still in the chair where Commander Paulson sedated me, but the room is different."
line171="I recognise it from training. "
screen45=[line167,line168,line169,line170,line171]

line172="This is the interrogation chamber. I have questioned virtual recreations of all manner of human scum - war criminals and assassins, drug pushers and holo-pirates - over the course of my training…"
line173="But I have never practiced the Melt on a living human being. "
line174="I stand up out of the chair and feel a little dizzy. I vaguely wonder how long I have been unconscious. "
screen46=[line172,line173,line174]

line175="Ahead of me is a door behind which lies my target… and my victim. "
line176="I walk across the metal doorway and present my retina for scanning. "
line177="The sensor beeps lazily and the door swings open. "
line178="I walk in, trying to swallow, but my throat is far too dry for that."
screen47=[line175,line176,line177,line178]

line179="And then I see her - or, at least, what’s visible of her. "
line180="On-Lam is stood in the middle of the room, her arms and feet constrained with shackles that are of a material I can’t seem to place."
line181="Her body is suspended in the air by chains that are affixed to every corner of the loop - the effect is that of a floating coffin. "
line182="There is a helmet on her head, made of the same material as the shackles, which covers her eyes. "
line183="Her mouth is the only part of her body that is visible. Her lips are held together so tight that they look like some sort of wound, and I wonder if she is in pain."
line184="Something about her presence feels… familiar. "
screen48=[line179,line180,line181,line182,line183,line184]

line185="I catch myself almost immediately. "
line186="You can’t think of this scum as people. "
line187="As Commander Paulson said… it’s better to start with a verbal interrogation before conducting a Melt. "
line188="I take a deep breath… and begin. "
screen49=[line185,line186,line187,line188]

line189="‘You tell me, Chrono-scum.’"
line190="He smiles, but there’s no cruelty in it. "
line191="She’s almost sad. "
line192="‘I know you’re just itching to use that thing on your wrist."
line193="Well, if you’re going to poke around inside my head, I’d suggest you get on with it…"
line194="I don’t want to be stuck here all day.’"
line195="She’s right, of course. The thing that is about to happen is going to be deeply unpleasant - for both of us. "
line196="I fidget with the Melt config on my wrist display and point the device towards On-Lam. "
line197="The readings… they’re unbelievably high. "
line198="Definitely not just standard memories over there in her head… there’s something more. I can feel it."
line199="A trap for me, no doubt. "
line200="But as she herself has said - no use in putting it off. "
screen50=[line189,line190,line191,line192,line193,line194,line195,line196,line197,line198,line199,line200]

line201="‘Do it!’ I hear her yell as I press down on the execute command on my wrist…"
line202="…there’s a great, familiar whooshing, as my presence torpedoes in towards an abstraction of On-Lam’s mind. "
line203="Some of the other minor drug-pushers I’ve had to Melt during training with had tiny, insignificant minds. "
line204="In the Melt interface the content of their heads were represented by tiny, dirty shacks with almost nothing inside. "
line205="In comparison, On-Lam’s mind in front of me is a colossal palace, full of intricate rooms, stairs and doors, looping in and out of themselves. "
line206="It’s going to be extremely difficult to find what I’m looking for here. "
screen51=[line201,line202,line203,line204,line205,line206]

line207="I focus deeply on the building ahead and sense that behind one of the doors is what I am looking for. "
line208="A memory - or series of memories - that took place over the course of last night.  "
line209="I see a museum on fire."
line210="I see a figure in a gas mask look upon a room filled with unspeakable violence. "
line211="I see a memorial wreath for a young woman, its leaves yellowed and dying."
screen52=[line207,line208,line209,line210,line211]

line212="This seems…right. "
screen53=[line212]

line213="I feel closer and closer to On-Lam as I focus on her and her thoughts. "
line214="The experience is a bleed between our feelings - there’s a fear there, but also… an anticipation? "
line215="Something isn’t right. "
line216="There is no longer a me… or a her. "
line217="There is a… you? "
line218="Yes… you. It’s you, On-Lam."
screen54=[line213,line214,line215,line216,line217,line218]

line219="You. You are running down a street ablaze with riots." 
line10000000000="You feel a sick thrill at the violence about to unfurl, and underneath it all, a simmering hate towards Chronosia." 
line100000000001="You want to see them dead."
screen55=[line219, line10000000000, line100000000001]

line220="You know that Chronosia are after you, and that they will catch you soon… but not until you collect the four Boxes, scattered among the streets of San Weyhoon. It kills you that you will only be able to reach one of them tonight. "
screen56=[line220]

line221="Just one of three. "
line222="The first box lies with Rachel Monet, a deep cover operative posing as a director of the museum of Chronosia Industries."
line223="The second and third boxes were sadly captured by the Chrono-scum - they were being taken by convoy over to a nearby outpost, just past the Radius Bridge."
line224="The fourth box is located in [REDACTED]"
screen57=[line221,line222,line223,line224]

line225="There is a slight chill, and I can feel my mind separate from On-Lam’s a little."
line226="Redacted? How? It’s more of a feeling than a word… When I try to access that section of On-Lam’s memory, it’s like I’m being physically forced out. I will figure this out later - at least I have a grip on where the other boxes are for the time being."
line227="I feel myself merge back into On-Lam’s consciousness…"
screen58=[line225,line226,line227]

line228="This city is still recoiling from the death of Commander Emily Yu, a notoriously cruel Chronosia operative - the Shogunate were blamed on the murder as always… But you know that the Shogunate had nothing to do with it. It’s a set up, as always. It looks like the power vacuum has finally spilled over into total anarchy… It’s going to be tough trying to get anywhere in this city. "
screen59=[line228]

line229="[Note: This is the first of several decisions you will have to make - they will have an effect on how you progress through this experience.]"
line230="[You can skip to this decision point next time you start up this program by typing ‘skip’ followed by ‘Enter’ at the ‘Chronosia Industries’ introductory screen.] "
line231="Where will you search?"
screen60=[line229,line230,line231]

line234="You decide to go after Monet’s box. Thankfully, the museum is relatively close - you turn a corner, and it stands in front of you. The riots have been burning here for weeks now, and the grand facade of the building is smashed to bits - windows in shards, walls pockmarked with bullet holes… A wonderful sight, you think, and smile to yourself. "
screen61=[line234]

line235="You feel a tinge of sadness as you consider that Monet may no longer be alive, given the state of the building - the inside is probably even worse. Nonetheless… the box must be retrieved. You go up to the front door… and enter."
screen62=[line235]

line236="You recall recent intel from Shogunate HQ saying that two of the boxes have been captured by the Chronoscum, and were being taken by convoy to an outpost full of those vermin. It’s an outpost near Radius Bridge, right on the border between the slums and the more affluent areas of the city."
line237="You start running towards the outpost, the cold night air filling your lungs, your head full of vengeance. "
screen63=[line236,line237]

line238="You start to hear the sounds of violence long before you ever see the bridge."
line239="There are screams like an animal’s wailing, punctuated by staccato gunfire. "
line240="The air reeks of smoke, and you are reminded of the ashen smells of the church you used to go to as a child, back when you still believed in the existence of a god."
screen64=[line238,line239,line240]

line241="You turn a corner and see the bridge ahead of you. The scene that unfolds before you is one of abject carnage - in the center of the bridge is an overturned NX999, one of Chronosia Industries’ flagship tanks, set ablaze by who knows what."
line242="You wonder for a moment what could have caused such damage to the colossal machine.  "
line243="In front of it are several crucifixes, to which people - bodies - are nailed. Some are missing limbs, eyes… You think you notice one of them twitch - just your imagination? Your stomach churns at the thought. "
screen65=[line241,line242,line243]

line244="You cross the bridge and walk into the central square… Where the violence just seems to escalate."
line245="The wailing, rioting crowd in the square encircling the Chronosia outpost in front of you all have ‘X’s carved into their foreheads… "
line246="You could have guessed from the display of violence, but this confirms it - this little slice of hell is the work of the Exers, a gang that has been wreaking havoc on the streets of San Weyhoon for the past several months."
screen66=[line244,line245,line246]

line247="It’s clear that regardless of what has happened here, the boxes couldn’t have gone far. "
line248="It’s possible that they have been taken by the Exers when they were butchering the Chronosia agents in the convoy. "
line249="Then again, it’s possible that some of the convoy have survived the attack - it’s possible that they still have the boxes holed up in the outpost ahead. "
line250="As much as you hate the Chronoscum, the boxes are the priority, and, let’s face it, it wouldn’t be the first time you pretended to be one of them to get what you wanted. "
line251="It’s time to make a choice - will you try to find a way into the outpost and deal with the surviving Chronosia agents? Or will you try to make a deal with the Exers? "
screen67=[line247,line248,line249,line250,line251]

line252="The three questions were answered correctly… The computer screen pushes inwards and slides up somewhere in the depths of the statue base. "
screen68=[line252]

line253="Underneath, there is a large recess, and inside - a pitch black box. It is of such a deep colour that it doesn’t feel like it’s of this Earth. This is what you came all this way for, what you risked your life for… and now it’s in your position. "
screen69=[line253]

line254="You take the box in your hands and it begins to hum - a low, even sound, soothing almost. "
line255="You touch it on the top surface, and it simply melts away. "
line256="You look inside…"
screen70=[line254,line255,line256]

line257="Whatever is contained inside the box doesn’t seem to be a physical object - it’s more like looking at the manifestation of a concept, an outward expression of an idea…"
line258="Your head hurts - it doesn’t feel like something that the human mind is meant to comprehend."
line259="You focus harder on the inside of the box, and it feels like something is scratching itself into your mind… "
screen71=[line257,line258,line259]

line260="THE SECOND DIGIT IS: 6"
line261="…"
line262="You have no idea what the thing inside the box is doing to you, but the more you focus, the more clear those words become…"
screen72=[line260,line261,line262]

line263="THE SECOND DIGIT IS: 6"
line264="…"
line265="Strange… This seems incredibly important, somehow. You feel like you should make a note of this…"
line266="If you had a pen and paper with you, or something to type on, you would certainly be writing this down."
screen73=[line263,line264,line265,line266]

line267="#####OUTPOST EXER ENDING#####"
screen74=[line267]

line268="You rush out of the outpost, cross the square, and down the street inside the shop, wincing at the carnage you must have unleashed. "
line269="Inside the shop, you walk up to the Duchess and explain what you have done. "
line270="‘Good, good,’ she says. ‘I think I know the passageway you’re talking about… We tried using brightsteel mines from the other side, but sadly we just weren’t able to drill through - we had to have someone open the lid on the other side. "
line271="Excellent work, On-Lam.’"
screen75=[line268,line269,line270,line271]

line272="What?.. "
line273="Did you just imagine it - or did she just call you by your name? "
line274="You have no time to think about the consequences of this, as your thoughts are interrupted by a thundering explosion."
line275="The Duchess walks over to the window… And now that it’s open, you are just in time to see the entirety of the Chronosia outpost collapse into total rubble. "
line276="‘Ah,’ she chuckles, ‘looks like my men made it in.’"
screen76=[line272,line273,line274,line275,line276]

line277="‘Well, a promise is a promise - here you go,’ she says, and takes a little black box out of her pocket, where it must have been the whole time."
line278="She does something to the glass… And the box seems to just melt through."
line279="You take the box in your hands and it begins to hum - a low, even sound, soothing almost. "
line280="You touch it on the top surface, and it simply melts away. "
line281="You look inside…"
screen77=[line277,line278,line279,line280,line281]

line282="Whatever is contained inside the box doesn’t seem to be a physical object - it’s more like looking at the manifestation of a concept, an outward expression of an idea…"
line283="Your head hurts - it doesn’t feel like something that the human mind is meant to comprehend."
line284="You focus harder on the inside of the box, and it feels like something is scratching itself into your mind… "
screen78=[line282,line283,line284]

line285="THE FIRST DIGIT IS: w"
line286="…"
line287="You have no idea what the thing inside the box is doing to you, but the more you focus, the more clear those words become…"
screen79=[line285,line286,line287]

line288="THE FIRST DIGIT IS: w"
line289="…"
line290="Strange… This seems incredibly important, somehow. You feel like you should make a note of this…"
line291="If you had a pen and paper with you, or something to type on, you would certainly be writing this down."
screen80=[line288,line289,line290,line291]

line292="#####OUTPOST CHRONO ENDING#####"
screen81=[line292]

line293="Your sense of relief lasts a mere moment… But then you realise that the Duchess is still moving."
line294="She looks at you, sprawled across the ground and bleeding, and shows you her fist - you remember seeing her holding something inside it earlier. "
line295="With her other hand she removes her gas mask, finally revealing her face - and to your surprise, it’s a face that you recognise…"
screen82=[line293,line294,line295]

line296="‘Emily Yu!?’"
screen83=[line296]

line297="Yes, there’s no mistaking it - in front of you is the former commander of the Chronosia outpost - the several-times decorated corporate officer, Emily Yu, allegedly murdered by the Shogunate several months ago. Her fist still remains outstretched, with something inside it. "
screen84=[line297]

line298="‘What’s the matter, On-Lam?’, she asks, coughing up blood. ‘Don’t tell me you’re surprised? I thought Shogunate intelligence was better than this. And yes, of course I know who you are - it doesn’t take a genius to see who would come into the middle of a warzone to nose around looking for random black boxes.’ "
screen85=[line298]

line299="‘Looks like you got me - or your cronies over on the other side did, anyway…’ She coughs again, and grimaces. "
line300="‘Might as well tell you the whole truth, then - not like anyone will believe you, anyway."
line301="This plan has been in the works ever since the Sakura Docks massacre, from back in the day. "
line302="You would have to be an idiot not to figure out that the whole thing was staged in order to place blame on the Shogunate. "
line303="I mean, surely you’ve seen that display that we have in the museum - does that seem like something that actually happened?  "
line304="But there were eyewitnesses that escaped - one of them works for you, I’m pretty sure. Operative that goes by the name of Monet?’"
screen86=[line299,line300,line301,line302,line303,line304]

line305="No matter. Chronosia needed a new way to exert control over San Weyhoon and to put down your sorry little cult. "
line306="We couldn’t just keep attacking the peasants in the slums and blaming it on you - we need something more unpredictable. "
line307="Something dangerous. "
screen87=[line305,line306,line307]

line308="It was Admiral Radius himself that gave me the assignment. "
line309="The people of this city… They need control. If they don’t have control, they will allow themselves to act like complete animals… Surely tonight is proof of that? You saw what they did to the convoy… To our men and women. "
line310="Their sacrifice will live on in the memory of Chronosia Industries. "
line311=" "
line312="For years we have been supplying arms to the more violent gangs within the city - the prototype for the Exers that you see today."
line313="Eventually, when it was time, my death was faked by the Admiral and a few from his close circle… Not too difficult to do, with a closed casket funeral. "
line314="There were a few conspiracy nuts - even in our outpost - that complained about not seeing the body, but they were either dismissed as crazy or silenced by some of our operatives. "
screen88=[line308,line309,line310,line311,line312,line313,line314]

line315="Over the course of the next months, I rose to power among those savages - now under the moniker of the Duchess. "
line316="These people are weak, On-Lam - the moment that you show them control, when you exert a bit of strength… They will fall under your heel. "
line317="Now Chronosia has its own agent of chaos in this city - whenever we need to place our troops somewhere, we can just direct the Exers there, and use that as justification to increase our military presence. "
screen89=[line315,line316,line317]

line318="The best part is… We can just keep blaming all the violence on you. "
line319="Do you think the general public cares about which gang burns down their house or kills their family? "
line320="They look at all of you as the animals that you are. As they should, might I add.’"
screen90=[line318,line319,line320]

line321="The Duchess gives a throaty chuckle at this, which quickly dissipates into a fit of painful, bloody coughing. "
line322="‘My death doesn’t change anything - I hope you realise that. "
line323="I am just one of many. For every Chronosia agent that you kill…"
line324="There are ten willing to take my place. You are fighting a losing battle, On-Lam.’"
screen91=[line321,line322,line323,line324]

line325="She smiles now, in a way that makes you nervous. "
line326="She shows you the closed fist again, and something about this whole situation starts to feel very wrong."
line327="‘Time to say your goodbyes, On-Lam. A shame, really - you’ll never find the box that I had here now.’ "
screen92=[line325,line326,line327]

line328="The Duchess unfurls her fist… And inside you see what she has been holding there the whole time - a deadman’s switch, connected to a bomb that you now see has been strapped to her stomach. "
screen93=[line328]

line329="The Duchess cackles as the bomb begins to tick, and you rush downstairs, away through the crowd of Exers that paid no attention to the murder of their leader…"
line330="And make it just in time - you are out on the street as the building behind you rocks with a thundering explosion, completely blowing out all the windows and doors within the structure. "
line331="The whole thing starts to creak and moan, and you can see some of the pipes and fixtures holding the building in place begin to collapse in on themselves. "
screen94=[line329,line330,line331]

line332="You keep running, further and further towards the outpost."
line333="As you look behind you, you can see that the building is now crumbling to the ground…"
line334="The Exers, completely enraptured by this new display of destruction, abandon their vandalism of the outpost and rush towards the freshly made ruins. "
line335="Just the time to help the trapped Chronosia agents escape… "
screen95=[line332,line333,line334,line335]

line336="The evacuation doesn’t take long - the men and women in the outpost are able to exit through the front door, killing the few stragglers left in the front square."
line337="You decide to keep the information about the Duchess and the true nature of the Exers to yourself - these operatives are so brainwashed that they probably don’t believe you anyway, and there’s probably a way that you will be able to leverage this information later. "
screen96=[line336,line337]

line338="The leader of the convoy begrudgingly fulfils his promise, and takes the box out of his pocket - where it has presumably been the whole time."
line339="You take it in your hands and it begins to hum - a low, even sound, soothing almost. "
line340="You touch it on the top surface, and it simply melts away. "
line341="You look inside…"
screen97=[line338,line339,line340,line341]

line342="Whatever is contained inside the box doesn’t seem to be a physical object - it’s more like looking at the manifestation of a concept, an outward expression of an idea…"
line343="Your head hurts - it doesn’t feel like something that the human mind is meant to comprehend."
line344="You focus harder on the inside of the box, and it feels like something is scratching itself into your mind… "
screen98=[line342,line343,line344]

line345="THE FOURTH DIGIT IS: u"
line346="…"
line347="You have no idea what the thing inside the box is doing to you, but the more you focus, the more clear those words become…"
screen99=[line345,line346,line347]

line348="THE FOURTH DIGIT IS: u"
line349="…"
line350="Strange… This seems incredibly important, somehow. You feel like you should make a note of this…"
line351="If you had a pen and paper with you, or something to type on, you would certainly be writing this down."
screen100=[line348,line349,line350,line351]

line352="#####PRE-BOMB PUZZLE TEXT#####"
screen101=[line352]

line353="Just as soon as this thought crosses your mind, you can feel an external… presence exert pressure on you."
line354="On you… or on me? "
line355="I can… feel my consciousness separate from On-Lam’s. "
line356="She is pushing me out of her mind…"
screen102=[line353,line354,line355,line356]

line357="And then I am back, safe inside my own head, my body in the interrogation chamber, standing in front of her - seconds have passed in real time, but it feels like I have been gone for hours. "
line358="The experience was just as uncomfortable as I imagined it would be - but now, thankfully, it is over…"
line359="For now."
screen103=[line357,line358,line359]

line360="I am about to speak when On-Lam floating body starts to heave and wretch. "
line361="A wave of panic crashes over me… Has the Melt had some kind of side-effect on my subject? "
line362="The retching continues, a hideous, rhythmic wet sound, until eventually it reaches a peak and some sort of object, covered in saliva, ejects itself from On-Lam’s mouth, and falls to the floor. "
line363="I can see On-Lam smile. "
screen104=[line360,line361,line362,line363]

line364="I walk over and inspect what my prisoner just produced out of her mouth…"
line365="…it’s a small metallic bomb. "
line366="Live and beeping."
line367="WIth a countdown set to thirty seconds."
line368="‘Well, now,’ On-Lam says, still smiling, ‘quite the turn of events, isn’t it?"
line369="Don’t bother calling for help, it won’t be any use - your boss was quite insistent that you handle this situation entirely on your own. "
line370="All the cameras are down, the doors are locked… You are completely alone in here with me."
line371="Whoopsie… And to think, they did such a good job of searching me.’"
screen105=[line364,line365,line366,line367,line368,line369,line370,line371]

line372="I refuse to let the taunting get to me - instead, I muster all the courage I have left, and pick up the bomb, trying not to let On-Lam see my hands shake. "
line373="You have seen these before - the Shogunate use these fairly often in their terrorist acts. "
line374="The bomb is small, but can completely decimate anything within a 25 meter radius - certainly enough to leave both me and On-Lam a pile of ash. "
screen106=[line372,line373,line374]

line375="On its front is a tiny keyboard - I recall from studying these types of electronics in the early Cadet classes that there is usually a four digit deactivation code on these types of bombs, which can consist of both numbers and letters. "
line376="…All time seems to freeze."
line377="There are two seconds left on the clock. "
line378="There is only one chance to get this right. "
screen107=[line375,line376,line377,line378]

line379="[This is a crucial juncture for Cadet Monad.]"
line380="[You can skip directly to this point when you are deciding whether to go to the museum or the outpost - Instead of pressing ‘1’ or ‘2’, type ‘bomb’ instead, and hit enter.]"
line381="[But for now... You need to find the password to diffuse the bomb.]"
screen108=[line379,line380,line381]

line383="#####BOMB FAILURE#####"
screen109=[line383]

line384="There is a long beep…"
line385="The password didn’t work. "
line386="I can hear On-Lam let out a sharp laugh before everything goes dark…"
screen110=[line384,line385,line386]

line387="…"
line388="…"
line389="…"
line390="But not completely dark."
screen111=[line387,line388,line389,line390]

line391="Somewhere in the distance I can see an amorphous shape…"
line392="A pair of glasses in the smoke. "
line393="Commander Paulson?"
screen112=[line391,line392,line393]

line394="Failure is not the end - it’s a new beginning."
screen113=[line394]

line395="It feels like I’m communicating with Commander Paulson somehow… But not verbally. "
line396="It’s more like she is another presence inside my head. "
line397="She brings up the memory of the bomb password inside my head…"
line398="A painful memory, but she waves away the negative emotions and makes me focus on the logic behind what happened. "
screen114=[line395,line396,line397,line398]

line399="Is there a way I could have figured out the password? "
line400="The boxes I was sent to collect… Do they have something to do with it? "
line401="Four boxes, four digits…"
line402="But what about the fourth box? "
screen115=[line399,line400,line401,line402]

line403="The glasses in the smoke shake in a motion that could be interpreted as laughing. "
line404="Ah, the fourth box. Well, of course, that is contained in [REDACTED]."
line405="Again, that strange feeling of being pushed out - whatever Paulson is trying to communicate to me is being censored somehow. I can feel her try again…"
screen116=[line403,line404,line405]

line406="Ah, the fourth box. Well, of course, that is contained in [/Chronosia/data_build/dialogue_diagram/box4/thirddigit.txt]."
line407="I can feel this string of numbers and symbols in my head… It’s somehow even more confusing. "
line408="What?..."
line409="I feel myself slip away… "
line410="But before I do, there’s that phrase again."
screen117=[line406,line407,line408,line409,line410]

line411="Failure is not the end - it’s a new beginning."
screen118=[line411]

line412="I feel disoriented, as if I am tumbling through my own consciousness - it’s a feeling of nausea, but somehow translated into a mental state as opposed to a physical one. "
line413="Somewhere, I can feel On-Lam’s presence - this has happened before…"
screen119=[line412,line413]

line414="There is no longer a me… or a her. "
line415="There is a… you? "
line416="Yes… you. It’s you, On-Lam."
screen120=[line414,line415,line416]

line417="Wait a second - no, this has definitely happened before - this is the experience you felt when Melting with On-Lam for the first time. "
line418="No time to consider why this is happening - it looks like someone - or something - has given you the chance to try again. "
line419="To maybe do things differently this time - and try and find a different box this time, perhaps. "
line420="Is it possible that this kind of loop will happen again… and if so, will I be able to eventually collect all four boxes?"
screen121=[line417,line418,line419,line420]

line421="#####BOMB SUCCESS AND TRUE ENDING#####"
screen122=[line421]

line422="There is a click after I type in the password… "
line423="And the beeping stops. "
line424="The bomb is deactivated and I breath a sigh of relief…"
screen123=[line422,line423,line424]

line425="In front of me, the chains holding On-Lam to the ceiling detach and the body is lowered to the ground, until the prisoner stands on her own two feet. "
line426="The sarcophagus releases itself and the shackles drop to the floor… "
line427="On-Lam reaches into her pocket and takes out a pair of familiar looking glasses. "
line428="She takes off her helmet, puts on the glasses, and lights up a cigarette. "
screen124=[line425,line426,line427,line428]

line429="This isn’t On-Lam at all. "
line430="The person hanging in front of me all this time wasn’t On-Lam…"
line431="…"
line432="…"
line433="…"
line434="It was Commander Paulson."
screen125=[line429,line430,line431,line432,line433,line434]

line435="‘Congratulations, Cadet,’ says Paulson, ‘or should I say, Enforcer. You passed. That fourth box was quite the doozy, wasn’t it?’ "
line436="I am still too stunned to speak, so the Commander keeps talking. "
line437="‘Apologies for my performance - I’m afraid I may have hammed it up a bit too much this time around. You no doubt have a lot of questions about what just happened here, so I’ll try to give you a brief explanation."
screen126=[line435,line436,line437]

line438="The first, and most obvious question - how was it that you were able to repeat the events of On-Lam’s night over and over again, until you were able to collect all four boxes? "
line439="Why did you not die when the bomb counted all the way down to zero? "
screen127=[line438,line439]

line440="The answer to that is simple - you finally induced SightParsing. "
line441="I knew you were close to being able to activate this ability - you were always an extremely talented cadet - but to fully induce it you needed to believe that you were in danger of death. "
line442="SightParsing is the ability to see the outcome of every decision you could make at any given time, which gives you an incredible tactical advantage over your enemies. "
line443="When you thought you were making decisions as On-Lam - to go to the museum or the outpost, to join Chronosia or the Exers - you weren’t actually physically making those decisions. "
line444="You were simply calculating what would happen if you did, to such an incredible accuracy that you were able to find out what was in the boxes that lay at the end of each respective decision path."
screen128=[line440,line441,line442,line443,line444]

line445="If you hadn’t activated SightParsing, you simply wouldn’t have known the password to the bomb, the timer would have ticked down to zero, and nothing would have happened - you would have to be kicked out of the academy of course, but you were never in any real danger, you just had to think that you were. "
line446="Fortunately this did not happen, and after each failed attempt you managed to boot yourself back to the first branching decision point to calculate another path."
line447="Ergo, you are still with us, and with a promotion, might I add."
screen129=[line445,line446,line447]

line448="The Commander walks over to the interrogation table and sits down, crossing her legs and taking another drag of her cigarette. "
line449="The room is beginning to fill with smoke, much like the auditorium where I was given my assignment… It really feels like that was years ago."
screen130=[line448,line449]

line450="‘Now for the tough part, Enforcer Monad. "
line451="You may have already figured out that On-Lam doesn’t exist. "
line452="She is a rumour that we spread among the Cadets, to make the SightParsing exam feel more real - do you really think we would send a cadet to interrogate a war criminal?"
line453="Now, with most cadets, I give them the sanitised version of the exam, where the Shogunate are shown as mass-murdering maniacs, ready to kill at the slightest provocation."
screen131=[line450,line451,line452,line453]

line454="With you… I’ve always sensed something different about you. "
line455="You don’t care for authority, Monad. You care about justice. So I wanted to show you the truth of what actually happens on the streets of San Weyhoon. "
line456="The memories you experienced may be fabrications, but the situations within them are entirely real. "
line457="The truth behind the massacre at Sakura Docks, the cover-up behind Emily Yu’s death, the corruption and rot at the upper levels of Chronosia Industries… It’s all real. "
line458="The Shogunate aren’t evil, Monad. They’re fighting for justice. "
line459="And you can fight for justice, too.’ "
screen132=[line454,line455,line456,line457,line458,line459]

line460="Commander Paulson goes quiet for a moment and then leans forward in her chair. "
line461="‘I know it’s a tough decision… But it’s one that I’m giving you, because I think you deserve it. This city is rotting, and only the Shogunate can truly enact change."
line462="We have eyes everywhere, and we have people within every station of government."
line463="It’s only a matter of time before this regime is toppled. "
screen133=[line460,line461,line462,line463]

line464="Will you join me?’"
screen134=[line464]

line465="After what I have seen, there is only one way I can answer. "
line466="I don’t bother with the SightParsing - I know that this is the right thing to do. "
screen135=[line465,line466]

line467="‘Yes,’ I reply."
screen136=[line467]

line468="[Congratulations on completing your interactive experience, Cadet!]"
line469="[Please don’t forget to log your thoughts and musings in the official training log, which will be reviewed by a superior before being logged in the official Chronosia Industries database.]"
line470="[Glory to Admiral Radius!] "
screen137=[line468,line469,line470]

line471="BROADCAST COMPLETE"
screen138=[line471]

line472="[Thank you for playing!]"
line473="[CHRONOSIA is a game by Vlad ‘toadkarter’ Rakhmanin]"
line474="[You can find more of my projects at my GitHub: https://github.com/toadkarter]"
screen139=[line472,line473,line474]

totalScreenList=[screen0,screen1,screen2,screen3,screen4,screen5,screen6,screen7,screen8,screen9,screen10,screen11,screen12,screen13,screen14,screen15,screen16,screen17,screen18,screen19,screen20,screen21,screen22,screen23,screen24,screen25,screen26,screen27,screen28,screen29,screen30,screen31,screen32,screen33,screen34,screen35,screen36,screen37,screen38,screen39,screen40,screen41,screen42,screen43,screen44,screen45,screen46,screen47,screen48,screen49,screen50,screen51,screen52,screen53,screen54,screen55,screen56,screen57,screen58,screen59,screen60,screen61,screen62,screen63,screen64,screen65,screen66,screen67,screen68,screen69,screen70,screen71,screen72,screen73,screen74,screen75,screen76,screen77,screen78,screen79,screen80,screen81,screen82,screen83,screen84,screen85,screen86,screen87,screen88,screen89,screen90,screen91,screen92,screen93,screen94,screen95,screen96,screen97,screen98,screen99,screen100,screen101,screen102,screen103,screen104,screen105,screen106,screen107,screen108,screen109,screen110,screen111,screen112,screen113,screen114,screen115,screen116,screen117,screen118,screen119,screen120,screen121,screen122,screen123,screen124,screen125,screen126,screen127,screen128,screen129,screen130,screen131,screen132,screen133,screen134,screen135,screen136,screen137,screen138,screen139]

def ClearScreen():
    """Clears the console screen"""
    command="clear"
    if os.name in ("nt", "dos"):
        command="cls"   
    os.system(command)

def header2():
    print(R"////////////////////////Chronosia Industries Cadet Training Server _ Program v0.5\\\\\\\\\\\\\\\\\\\\\\\\")

def lineDecoration():
    print()
    print("****************************************************************************")
    print()


def display(lines):
    """Generates an individual screen for the visual novel section. Allows user to access options"""
    """TO DO - show user list of options if they accidentally type something wrong?"""
    """TO DO - generally, add an options screen"""
    header2()
    print()
    for i in lines:
        print(i)
        input()
    ClearScreen()

def charByChar(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("...Press Enter.")
    input()

def chronosiaLogo():
    print(R"   ____ _                               _         ___           _           _        _           ")
    print(R"  / ___| |__  _ __ ___  _ __   ___  ___(_) __ _  |_ _|_ __   __| |_   _ ___| |_ _ __(_) ___  ___ ")
    print(R" | |   | '_ \| '__/ _ \| '_ \ / _ \/ __| |/ _` |  | || '_ \ / _` | | | / __| __| '__| |/ _ \/ __|")
    print(R" | |___| | | | | | (_) | | | | (_) \__ \ | (_| |  | || | | | (_| | |_| \__ \ |_| |  | |  __/\__ \\")
    print(R"  \____|_| |_|_|  \___/|_| |_|\___/|___/_|\__,_| |___|_| |_|\__,_|\__,_|___/\__|_|  |_|\___||___/")

def intro():
    charByChar("Chronosia Industries main port located…")
    charByChar("Disabling anti-breach protection…OK")
    charByChar("Breaching firewall…OK")
    charByChar("Accessing main server…OK")
    ClearScreen()
    chronosiaLogo()
    print()
    print('{:^90}'.format('Cadet Training Server'))
    print('{:^90}'.format('Say Hello To The Future You!'))
    print()
    print("[Access Date: 23 December 2117]")
    print("[Access Time: 00:15]")
    print()
    print("IMPORTANT NOTE")
    print("Please don’t forget to note all details of your practice session to your designated Chronosia Industries training log. ")
    print("Any unauthorised distribution of contents of any training log will be met with strict disciplinary action, up to and including summary dismissal. ")
    print("Remember - a good cadet takes care of their training log! Glory to Admiral Radius!")
    print()
    print("Press Enter to begin your training")
    print("Hold Enter to fast forward through text")
    print("Type Quit to log off")

def hacking():
    ClearScreen()
    header2()
    print()
    charByChar("Error: Program on display has been tampered with by Chronosia Industries R&D Department.")
    charByChar("Similarity to original program written by Enforcer Monad: 2%")
    charByChar("Attempting to roll back to original version…")
    charByChar("Rolling back…")
    charByChar("Rolling back…")
    charByChar("OK.")
    charByChar("Booting initial version of program without modification from the Chronosia Industries R&D Department.")

    ClearScreen()


def outro():
    ClearScreen()
    header2()
    print()
    charByChar("<Unauthorised user actions detected>")
    charByChar("<Compressing archive containing Enforcer Monad’s unaltered testimony on Chronosia Industries crimes>… OK.")
    charByChar("<Transferring to Shogunate encrypted archives>… OK. ")
    charByChar("<Broadcasting to San Weyhoon media outlets>…")
    input("...")
    input("...")
    input("...")
    ClearScreen()


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


lineA="[Welcome to the tutorial. The text in each gameplay section will feature certain objects that you can interact with. They will be surrounded by square brackets]"
lineB="[To utilise the ‘Examine’ command, type ‘examine obj’, with the letters ‘obj’ replaced by the object you want to examine. For example - ‘examine key’. You will receive a short description of the object.]"
lineC="[To utilise the ‘Pick’ command, type ‘pick obj’, with the letters ‘obj’ replaced by the object you want to pick up. For example - ‘pick key’. You will add the object to your inventory]"
lineD="[To utilise the ‘inventory’ command, type ‘inventory’. You will be able to see the objects you have in your inventory.]"
screenTut1=[lineA,lineB,lineC,lineD]

lineE="[To utilise the ‘Use’ command, type ‘use obj1’ or ‘use obj1 obj2’, with the letters obj1 and obj2 replaced by the objects that you want to use. The form ‘use obj1 obj2’ will result in obj1 being used on obj2, for example ‘use key door’ will result in the key being used on the door.]"
lineF="[Please note that sometimes objects may be hidden inside other objects, and as such will not be immediately visible. Make sure to examine all object carefully, and choose the ‘use’ button on objects frequently to see what what can be done with them - it might not be obvious in the first instance]"
lineG="[To view these instructions again, type ‘tutorial’ in the commands section.]"
lineH="[Best of luck - and glory to Admiral Radius!]"
screenTut2=[lineE,lineF,lineG,lineH]

def displayPuzzleText(room):
    for i in room:
        print(i)
        print()

def initialHeader():
    ClearScreen()
    header2()
    print()

def exit_command():
    print("Press Enter to return")
    input()

def display_commands():
    print("What do you do?")
    print("[Commands: examine, pick, use, inventory, tutorial, quit]")

def examine_command(command,room_items):
    command=command.split(" ")
    if len(command)==1:
        initialHeader()
        print("Sorry, you have to follow up the examine command with a noun.")
        print("For example: examine key")
        print()
        exit_command()
    else:
        itemSelected=Item
        correctInput=False
        for i in room_items:
            if i.name==command[1]:
                itemSelected=i
                correctInput=True
        if correctInput:
            initialHeader()
            print(f"Chosen Item: {itemSelected.name}")
            print()
            print(itemSelected.descr)
            print()
            exit_command()
        else:
            initialHeader()
            print("Sorry, we don't recognise an item with that name.")
            print()
            exit_command()

def pick_command(command,room_items):
    command=command.split(" ")
    if len(command)==1:
        initialHeader()
        print("Sorry, you have to follow up the examine command with a noun.")
        print("For example: pick key")
        exit_command()
    else:
        itemSelected=Item
        correctInput=False
        for i in room_items:
            if i.name==command[1]:
                itemSelected=i
                correctInput=True
        if correctInput:
            initialHeader()
            print(f"You are trying to get: {itemSelected.name}")
            if itemSelected.pick==True:
                inventory.addItem(itemSelected)
                print()
                print("You have successfully picked up this item.")
                print()
                exit_command()
            else:
                print("Sorry, you can't pick that up.")
                print()
                exit_command()
        else:
            initialHeader()
            print("Sorry, we don't recognise an item with that name.")
            print()
            exit_command()

def inventory_command():
    inventory_looping=True
    while inventory_looping:
        initialHeader()
        print("INVENTORY CONTENTS")
        print()
        if not inventory.inventory:
            print("Your inventory is currently empty.")
            print()
            exit_command()
            inventory_looping=False
        else: 
            print("You currently have the following items in your inventory:")
            for i in inventory.inventory:
                print(f"{i.name}")
            print()
            print("Type name of item to get its description, or press Enter to continue")
            descr=input().lower()
            for i in inventory.inventory:
                if descr==i.name:
                    initialHeader()
                    print(f"Chosen Item: {i.name}")
                    print()
                    print(f"Item Description: {i.descr}")
                    print()
                    exit_command()
                else:
                    inventory_looping=False

# BUG_REPORT: Currently allows you to use item not in inventory
# BUG_REPORT: No error handling for situation where user selects more than two items
def use_command(command,room_items):
    command=command.split(" ")
    if len(command)==1:
        initialHeader()
        print("Sorry, you have to follow up the use command with one or two nouns.")
        print()
        print("For example: use candle")
        print("For example: use key door")
        print()
        exit_command()
    else:
        itemSelected=Item
        item2Selected=Item
        correctInput=False
        correctInput2=False

        if len(command)==2:
            for i in room_items:
                if i.name==command[1]:
                    itemSelected=i
                    correctInput=True
            if correctInput:
                initialHeader()
                print(f"You are trying to use: {itemSelected.name}")
                print()
                print(itemSelected.item_use["self"])
                if itemSelected.item_used_alone==False:
                    itemSelected.item_used_alone=True
                print()
                exit_command()
                
        elif len(command)==3:
            for i in room_items:
                if i.name==command[1]:
                    itemSelected=i
                    correctInput=True
                        
                if i.name==command[2]:
                    item2Selected=i
                    correctInput2=True
                    
            if correctInput==True and correctInput2==True:
                key_value=-1
                initialHeader()
                print(f"You are trying to use {itemSelected.name} with {item2Selected.name}")
                print()
                for key in itemSelected.item_use.keys():
                    if key==item2Selected.name:
                        key_value=key
                if key_value != -1:
                    print(itemSelected.item_use[key_value])
                    if itemSelected.item_used_with_otherItem==False:
                        itemSelected.item_used_with_otherItem=True
                    if item2Selected.item_used_with_otherItem==False:
                        item2Selected.item_used_with_otherItem=True
                    print()
                    exit_command()
            else:
                print("Sorry, one of these items does not exist!")
                print()
                exit_command()

def dunno_command():
    initialHeader()
    print("Sorry, I don't recognise that command!")
    print()
    print("Please try 'examine','pick','inventory', 'use' 'tutorial' or 'quit'")
    print()
    exit_command()

# Note: Exit condition should always be at the end.
# TO DO: Add a tutorial option
def puzzle_room(room,room_items):
    looping=True
    while looping:
        initialHeader()
        displayPuzzleText(room)
        print()
        display_commands()
        command=input().lower()
        if "examine" in command:
            examine_command(command,room_items)
        elif "pick" in command:
            pick_command(command,room_items)
        elif command=="inventory":
            inventory_command()
        elif "use" in command:
            use_command(command,room_items)
        else:
            dunno_command()

def dialogueChoices(dialogue):
    looping=True
    while looping:
        selectedIndex=0
        ClearScreen()
        initialHeader()
        for i in range(0,len(dialogue)-1):
            print(dialogue[i][0])
        print(dialogue[len(dialogue)-1])
        print()

        # Note: Add error checking here for ints
        option=intChecker("Please select your dialogue option: ")
        if option<=len(dialogue)-1:
            if option==0:
                ClearScreen()
                initialHeader()
                looping=False
                break
            else:
                ClearScreen()
                initialHeader()
                for i in range(0,len(dialogue)):
                    if option==i:
                        selectedIndex=i-1
                        break
                print(dialogue[selectedIndex][0])
                print()
                for i in range(1,len(dialogue[selectedIndex])):
                    print(dialogue[selectedIndex][i])
                    input()
        else:
            print("Sorry, the number must be within the range of options provided.")
            print("Please press Enter and try again.")
            input()

def intChecker(message):
    while True:
        try:
            userInput=int(input(message))
        except ValueError:
            ClearScreen()
            initialHeader()
            print("Sorry, you have to type in a number.")
            print()
            continue
        else:
            return userInput
            break


def removeFromScene(object, location):
    if object in location:
        location.remove(object)


def addToScene(object, location):
    if object not in location:
        location.append(object)  


def puzzleNavigation(puzzle_text, puzzle_items):
    initialHeader()
    displayPuzzleText(puzzle_text)
    print()
    display_commands()
    command=input().lower()
    if "examine" in command:
        examine_command(command,puzzle_items)
    elif "pick" in command:
        pick_command(command,puzzle_items)
    elif command=="inventory":
        inventory_command()
    elif "use" in command:
        use_command(command,puzzle_items)
    elif command=="tutorial":
        ClearScreen()
        display(screenTut1)
        display(screenTut2)
        ClearScreen()
    elif command=="quit":
        ClearScreen()
        initialHeader()
        print()
        print("[Thank you for participating in the Chronosia Industries Cadet Interactive Experience.]")
        input("Please press Enter again to quit.")
        quit()
    else:
        dunno_command()

def addItemEverywhere(item, location_items):
    addToScene(item, inventory.inventory)
    for i in location_items:
        addToScene(item, i)

def removeItemEverywhere(item, location_items):
    removeFromScene(item, inventory.inventory)
    for i in location_items:
        removeFromScene(item, i)

def screensInRange(totalScreenList, low, high):
    for i in range(low, high+1):
        display(totalScreenList[i])

intro()

entry=input()
if entry.lower()=="quit":
    quit()

elif entry.lower()!="skip":
    ClearScreen()

    screensInRange(totalScreenList, 0, 6)
    hacking()
    screensInRange(totalScreenList, 7, 21)

    tutorialLoop=True
    while tutorialLoop:
        ClearScreen()
        header2()
        print()
        print("[Enter 1, followed by ‘enter’, to read, enter 2, followed by ‘enter’, to proceed directly to the exercise]")
        tutorialInput=str(input(""))

        if tutorialInput=="1" or tutorialInput=="2":
            tutorialLoop=False
            break
        else:
            input("Sorry, invalid input. Press Enter and try again.")

    if tutorialInput=="0":
        screensInRange(totalScreenList, 22, 23)

    # This is where the first puzzle room should start
    looping_puzzleroom1=True
    while looping_puzzleroom1:
        initialHeader()
        if room1_blaster in inventory.inventory and room1_knife in inventory.inventory and room1_items[4].item_used_with_otherItem==True:
            ClearScreen()
            looping_puzzleroom1=False
            break
        elif room1_blaster in inventory.inventory and room1_knife in inventory.inventory:
            displayPuzzleText(room1_changed)
            print()
        else:
            displayPuzzleText(room1)
        print()
        display_commands()
        command=input().lower()
        if "examine" in command:
            examine_command(command,room1_items)
        elif "pick" in command:
            pick_command(command,room1_items)
        elif command=="inventory":
            inventory_command()
        elif "use" in command:
            use_command(command,room1_items)

    screensInRange(totalScreenList, 24, 31)
    dialogueChoices(dialogue1)
    ClearScreen()
    screensInRange(totalScreenList, 32, 49)
    dialogueChoices(dialogue2)
    ClearScreen()
    screensInRange(totalScreenList, 50, 60)

# We will repeat from here each time the player fails a bomb loop
playingabranchingpath=True

while playingabranchingpath:

    branchingPathLoop=True

    while branchingPathLoop:
        # DEFINE ALL THE DATA HERE - IT WILL GET RESET WITH EVERY LOOP
        """
        ITEMS FOR PATH 1, MAIN ROOM
        """
        # Door
        path1main_door_use={"self":"The door opens easily and you head upstairs."}
        path1main_door=Item("door","The door is marked with the word 'Administrative'. It looks like it leads upstairs.",False,path1main_door_use)

        # Cube
        path1main_cube_use={"self":"You press the little button underneath the plaque. The light inside the cube sputters, and then begins to form into human shapes. What follows is an incredibly display of human slaughter - men in Shogunate uniforms, with almost comically evil sneers on their faces, cut down women and children that beg for mercy. A booming voiceover narrates the massacre: 'Witness the evil Shogunate murder innocent civilians on the streets of Sakura Docks. A sad day for Chronosia Industries - but one that also heralded a new beginning. Admiral Radius (glory to his name) has vowed on that day to increase the presence of armed forces in San Weyhoon. Since then, we have seen crime rates drop to an all-time low, bringing record-breaking dividends into the pockets of our shareholders! We honour the victims of the massacre with this memorial display - may they rest in peace.'"}
        path1main_cube=Item("cube","It's a holographic display, usually used to re-enact famous historical events. The plaque underneath it reads 'The Massacre at Sakura Docks (2102)'... A sad day.",False,path1main_cube_use)

        # Model
        path1main_model_use={"self":"It seems that the model is controlled by the display nearby."}
        path1main_model=Item("model","It's a model of the NX999, one of the automated vehicles that Chronosia Industries send into neighbourhoods suspected of harbouring Shogunate insurgents. It is, in effect, a tank, with two submachine guns on each side which have the capability to auto-lock onto moving targets. The most famous feature of the NX999 is its horizontal opening of spiked gears, known as The Maw, at the very front of the vehicle, which are so powerful that they can crush small structures in the slums where they are usually deployed. The surface of this machine is made of a material called blackened adamantium, which is notoriously difficult to destroy. Rather perversely, this model seems to be being used to create souvenir coins - after putting in a token, this token is transported by a mini-treadmill into the model's Maw, where it is flattened and then dispensed in a slot nearby. Looking into the model's display case, you can spot something glinting right beside the model's Maw.",False,path1main_model_use)

        # Token
        path1main_token_use={"self":"You don't think you can do anything with this on its own... It needs to be used with the model.","model":"The model seems to be switched off. I have to figure out a way to restore power to it first."}
        path1main_token=Item("token","A small token made of cheap metal... You're really glad you didn't waste any credits on this thing. It's supposed to be put into the little opening in the model, where it will then start the mechanism to flatten the token and print it with some kind of design",True,path1main_token_use)

        # Dispenser
        path1main_dispenser_use={"self":"Let's face it... You're not about to give any credits to this machine. You smash your fist into the cartoon drawing of the NX999 - the dispenser whines gently, rattles, and spits out a token. You add it to your inventory."}
        path1main_dispenser=Item("dispenser","A large cabinet. On it you can see a cartoon drawing of the NX999 vehicle - it's been given a humanoid face, and it seems to be winking provocatively in your direction. The text underneath the drawing reads: 'Get yourself a fond memory of your visit to the Chronosia Industries Historical Museum with a commemorative coin! A token costs only 10 credits - and for that price you will have a fun souvenir with an imprint of the NX999, the protector of San Weyhoon!'",False,path1main_dispenser_use)

        # Hololog 2

        # Keycard1 (downstairs)
        path1main_keycard1_use={"self":"It's a red keycard, a little soggy from the puddle you collected it from. It has the Chronosia Industries logo on it, but someone has scratched a vague approximation of the Shogunate insignia on top of it."}
        path1main_keycard1=Item("keycard1","It's a red keycard, a little soggy from the puddle you collected it from. It has the Chronosia Industries logo on it, but someone has scratched a vague approximation of the Shogunate insignia on top of it.",True,path1main_keycard1_use)

        path1main_keycard2_use={"self":"It's a blue keycard, a little dented at the bottom from where it almost got crushed in the model vehicle's Maw. It has the Chronosia Industries logo on it, but someone has scratched a vague approximation of the Shogunate insignia on top of it."}
        path1main_keycard2=Item("keycard2","It's a blue keycard, a little dented at the bottom from where it almost got crushed in the model vehicle's Maw. It has the Chronosia Industries logo on it, but someone has scratched a vague approximation of the Shogunate insignia on top of it.",True,path1main_keycard1_use)

        # Dripping
        path1main_dripping_use={"self": "The ceiling is too high - you can't reach the source of the dripping."}
        path1main_dripping=Item("dripping","Looking up at the ceiling, you see that one of the sections seems to be a slightly different colour - it looks like it was recently replaced. From its center, a drop of dirty water falls every couple of seconds onto the floor below. It's possible that there's some sort of crack in the new panel that is causing the leak.",False,path1main_dripping_use)

        # Holotool
        holotool_use={"self":"You place your finger on the lockslot and the device comes to live with a sickly green glow. Well, it seems to work... But you have to use this on something.", "knife":"Sadly, your knife is a non-electrical object - you can't hack it.", "sensor":"Sadly, the system is a little too complex to hack. You'll have to find another way of getting items out of this room.","cube":"You point the holotool at the cube and make a few adjustments. The readings show that there is another display file hidden at a different frequency. You switch it on, and the light within begins to flash into existence. Within the cube, a familiar scene of the Sakura Docks massacre appears... But this time, the men and women doing the killing are wearing Chronosia Industries uniforms. A woman's voice begins to speak: 'Do not believe the lies of the Chrono-drones. In 2102, it was one of Chronosia Industries' own commanders - Commander Turner - that instigated the slaughter of over 300 civilians, blaming it all on the Shogunate. They used this incident to justify taking their death machines into any neighbourhoods suspected of harbouring Shogunate agents... and lining their pockets with protection fees from the San Weyhoon Municipality. Stay viligant, agents. Monet out.'","dispenser":"This dispenser looks like it's not using any sophisticated software that would require hacking - just using it directly, without the use of implements, should do the trick.","display":"This thing is powered off... You have to restore power before trying to hack it.","glowingdisplay":"You point the holotool at the garbled words on the display and check the output. There is an 'on' button to power on the mechanism, and a toggle switch to change direction of the mini-treadmill used for the NX999's Maw. You reverse the treadmill and click the power button. The machine starts up, and you see the small piece of plastic that was stuck just outside the Maw slowly travel backwards and out into the slot where you were supposed to place your token. You reach inside... And see that it is a keycard. You pick it up and place it into your inventory."}
        holotool=Item("holotool","A small, portable hacking device. While it won't work with complex security systems, it is quite handy for breaking into minor electrical systems and vehicles. Standard issue for all Shogunate operatives.", True, holotool_use)

        # Knife
        knife_use={"self":"You should be using this with something... You are angry, but not angry enough to be lashing out at thin air.", "holotool":"You really don't want to break open your holotool - it seems to be working fine for now.","crack":"You poke the knife into the crack - the material seems to be worn, and quite malleable. After a short while, you have widened it enough to push a small, thin object through.", "dripping":"You don't think you could throw your knife hard enough to do any real damage to the source of the dripping.","cube":"Tired of seeing yet another piece of disgusting propoganda, you stab angrily at the cube. You manage to make a small scratch but the structure remains intact... No wonder this thing survived the riots.","dispenser":"You consider using your knife to pry open the machine... But it looks pretty frail. You can probably just try and use it directly, without the use of implements.","baton":"You saw away with your knife at the baton and, eventually, it comes loose. You add the tip to your inventory.","panel":"It's too sharp - you might damage it.","crucifixes":"It makes you feel ill to do this... But if you are going to infiltrate the Exers, you are going to have provide them with some evidence of your own brutality. You take your knife and saw at the loosely hanging finger of one of the corpses - it falls off and you put with the rest of your belongings. It is now added to your inventory."}
        knife=Item("knife","The Chrono-drones outnumber you, and have better equipment... but a knife in the right place can close such gaps. There are markings on its handle for every citizen you failed to save. It's only right that you remember them - noone else will.",True,knife_use)

        # Baton
        path1main_baton_use={"self":"The tip is barely hanging on, but you probably won't be able to pry it off with just your bare hands."}
        path1main_baton=Item("baton","The tip of the baton is extraordinarily sharp - you feel like it could be used as a tool. It's barely hanging on the end of the figurine.",False,path1main_baton_use)

        # Boots
        path1main_boots_use={"self":"You put the boots on. You feel absolutely ridiculous and start to wonder why you decided to put these on in the first place."}
        path1main_boots=Item("boots","Indescribably ugly boots - the design is plastered with an anthropomorphic version of the Chronosia Industries NX999 combat vehicle. They seem to be made from some kind of rubber. You could probably 'use' them if you wanted to.",False,path1main_boots_use)

        # Baton Used
        path1main_tip_use={"self":"You can't use this on its own - it has to be used with something else.","panel":"You could probably use this tip as a makeshift screwdriver to fix the panel, but you can't do that with all this water around you - you'll be electrocuted. You have to figure out a way to do this safely.","safepanel":"Now that you are wearing the boots, the rubber in them will protect you from the electricity. You tinker with the wiring, using the tip as a screwdriver, and eventually manage to see the issue. Something inside the panel whirrs to life and the sound mellows out to a steady hum. You should check downstairs to see if this has had an effect on any machinery there."}
        path1main_tip=Item("tip","It's the tip of the baton that you sawed off from one of the statues downstairs. It's incredibly thin - you think you could probably use it as some sort of tool.",False,path1main_tip_use)

        path1main_displaydummy_use={"self":"It's deactivated - you have to restore the power somehow."}
        path1main_displaydummy=Item("display","It looks like a control panel of some sort for the NX999 model, but it seems to be deactivated. You have to figure out a way to restore the power if you're going to use it.",False,path1main_displaydummy_use)

        path1main_display_use={"self":"The software on this machine is slightly garbled - you're going to want to hack into it in order to operate it."}
        path1main_display=Item("glowingdisplay","The display has come to life, and is giving on a greenish glow. The options on the screen seem a little garbled... You're probably going to need to hack into this machine in order to operate it.",False,path1main_display_use)

        path1main_hololog2_use={"self":"It's a standard hololog for corporate and domestic use. You power it on - there is a message here that was sent to an external address. It reads as follows: 'Sister, I’m becoming more and more dissatisfied with the way things are run around here. You have always been aware of my sympathies for The Shogunate - I don’t think it’s possible not to have sympathies, after what happened to our parents - but things are reaching a critical point and I don’t think I can sit idly by. I have hidden the Box belonging to our Cell here in this building, right after their noses. The entry is protected by two keycards, both of which are secure, and three passquestions. I will send these to you in separate holomessages for safety - if anything is to happen to me, I would like the Box to be safe. Question 1 is as follows: In what year did the Sakura Docks massacre occur? Yours always, Monet.'"}
        path1main_hololog2=Item("hololog2","It's a standard hololog for corporate and domestic use. You power it on - there is a message here that was sent to an external address. It reads as follows: 'Sister, I’m becoming more and more dissatisfied with the way things are run around here. You have always been aware of my sympathies for The Shogunate - I don’t think it’s possible not to have sympathies, after what happened to our parents - but things are reaching a critical point and I don’t think I can sit idly by. I have hidden the Box belonging to our Cell here in this building, right after their noses. The entry is protected by two keycards, both of which are secure, and three passquestions. I will send these to you in separate holomessages for safety - if anything is to happen to me, I would like the Box to be safe. Question 1 is as follows: In what year did the Sakura Docks massacre occur? Yours always, Monet.'",False,path1main_hololog2_use)

        path1main_statue_use={"self":"The statue is large and pompous - it looks impressive from a distance, but up close, it feels almost like a caricature… Much like most of the other art in this building. You spot a little speaker at the base, and you press the button beside it. A large, booming voice emerges: ‘Greetings, visitor, and welcome! Welcome to the museum of Chronosia Industries, the greatest corporation in the city state of San Weyhoon! My name is Admiral Radius, CEO, and I would like to perosnalldqqyy…’ The voice becomes scrambled and dies off. The speaker begins to steam… Until the metallic cover of the apparatus falls off altogether. Underneath, you can see a little display, with two keycard slots. You will probably be able to use it once you have two keycards in your inventory"}
        path1main_statue=Item("statue","A massive, ugly statue of Admiral Radius. At the base of this thing you can see a little speaker with a button next to it.",False,path1main_statue_use)

        path1main_computer_use={"self":"You press the enter key, and the questions begin to appear on the screen."}
        path1main_computer=Item("computer","Now that you have inserted the relevant keycards... The computer is on.",False,path1main_computer_use)


        path1main_items=[path1main_door, path1main_dripping,path1main_cube,path1main_model, path1main_dispenser,path1main_baton,path1main_boots,path1main_displaydummy,path1main_hololog2,path1main_statue, knife, holotool]



        """
        TEXT FOR PATH 1, MAIN ROOM
        """
        # Text
        path1main1=f"The main hall of the museum has seen better days, but despite the damage done it still retains some of its severe magnificence. It is a tall, towering room, and its brutalist architecture makes you feel small."
        path1main2=f"Rubble from the recent riots covers the floor, exhibits and art collapsed and shattered, and a lazy [{path1main_dripping.name}] can be heard from somewhere. A part of you is glad - one day San Weyhoon will be rid of all this propaganda."
        path1main3=f"Two exhibits remain that have not been completely destroyed. On your left is a large, transparent [{path1main_cube.name}], which you vaguely recognise as a holographic display. Scattered on the ground beside is a [{path1main_hololog2.name}]."

        path1main4=f"On your right is a large [{path1main_model.name}] of the NX999… A vehicle that you sadly know too well. It is encased in a kind of display case and affixed to a peculiar mechanism, which has a [{path1main_displaydummy.name}] on the back."

        path1main11=f"Having switched on the power, there is now a [{path1main_display.name}] beside the large [{path1main_model.name}] of the NX999."

        path1main5=f"Beside the NX999 exhibit stands a machine that looks like a [{path1main_dispenser.name}] of some sort - it looks like it’s somehow related to the model."

        path1main6=f"Directly ahead is a colossal [{path1main_statue.name}] of Admiral Radius, which stretches to the ceiling, and behind it as a [{path1main_door.name}]." 

        path1main9=f"Flanking each side of the statue is a slightly smaller, but equally imposing figure of a Chronosia Enforcer holding a riot baton with a sharpened tip. The [{path1main_baton.name}] of the figure on the left seems to be a little crooked."

        path1main7=f"You now spot something in the puddle directly underneath the source of the dripping you heard earlier."

        path1main8=f"In the pool of water, you can spot a [{path1main_keycard1.name}]."

        path1main10=f"Right beside the entrance where you are standing, there are some truly hideous [{path1main_boots.name}]."

        path1main12=f"Now that you have both keycards in your inventory, your were able to insert them in the slots at the base of the statue. Behind it is the [door] that leads upstairs. The [computer] screen begins to glow green. It's time to finish this."

        path1main=[path1main1,path1main2,path1main3,path1main4,path1main5,path1main6,path1main9,path1main10]

        """
        ITEMS FOR PATH 1, UPSTAIRS OFFICE
        """
        # Door
        path1office_door_use={"self":"You open the door and go back downstairs."}
        path1office_door=Item("door","It's the door you just came out of - it leads back into the main museum room.",False,path1office_door_use)

        # Boxes
        path1office_boxes_use={"self":"It takes you a bit of time, but you manage to move the boxes out of the way and reveal what is underneath."}
        path1office_boxes=Item("boxes","A set of cardboard boxes stacked on top of each other - the ones at the bottom are soaked from the flooding. They seem to contain various ledgers and accounting documents. At a glance, the boxes seem quite light - you could probably move them out of the way without much difficulty.",False,path1office_boxes_use)

        # Sensor
        path1office_sensor_use={"self":"The sensor is turned on - you can't switch it off without the relevant keyphrases... You don't think I'll find them here."}
        path1office_sensor=Item("sensor","It's a standard security sensor to protect the items in this room. Whenever someone tries to take a metallic object out of here, the door will automatically lock. It looks like you'll have to find some other way of getting items out of here.",False,path1office_sensor_use)

        # Crack
        path1office_crackdummy_use={"self":"It seems to be just a hairline crack for now - but the material is flimsy. You could probably widen it with something."}
        path1office_crackdummy=Item("crack","It seems to be just a hairline crack for now - but the material is flimsy. You could probably widen it with something.",False,path1office_crackdummy_use)

        # Desk (closed)
        path1office_deskdummy_use={"self":"You're certain there are probably some useful items in here, but you don't want to open it until you can get objects out of here."}
        path1office_deskdummy=Item("desk","It's a fancy looking desk. It looks like it belongs to someone who is - or was - in charge around here.",False,path1office_deskdummy_use)

        # Desk (open)
        path1office_desk_use={"self":"You have opened the desk."}
        path1office_desk=Item("desk","It's a fancy looking desk. It looks like it belongs to someone who is - or was - in charge around here.",False,path1office_desk_use)

        # Keycard1 (upstairs)
        path1office_keycard1_use={"self":"You take the keycard and shove it through the newly created gap in the floor. There is a moment of silence, followed by a splash."}
        path1office_keycard1=Item("keycard1","It's a red keycard. It has the Chronosia Industries logo on it, but someone has scratched a vague approximation of the Shogunate insignia on top of it.",False,path1office_keycard1_use)

        # Hololog1 (upstairs)
        path1office_hololog1_use={"self":"It's a standard hololog for corporate and domestic use. You power it on - there is a message here that was sent to an external address. It reads as follows: 'My sister, they are coming for me. These riots that are starting two streets over… They are a front, as per usual, and no doubt instigated by the Chrono-scum yet again - all they need is a convenient excuse to destroy what we have started to build here. I know they will direct the riots into the museum soon enough. I do not know if I have much time left, or if I will be able to get out of here alive. I have tried to destroy one of the keycards guarding our Box in that hideous model downstairs, but I do not know if I succeeded. The other keycard will have to be left here. I pray that that another operative comes to collect it - and that the Chrono-scum do not figure out where to look. I leave you with the last Question - I’m sure you know the answer. I love you, sister. Yours always, Monet.' Scrawled with what seems to be a knife at the bottom of the screen are the following words: 'Question 3: What entity is responsible for the Sakura Docks massacre?'"}
        path1office_hololog1=Item("hololog1","It's a standard hololog for corporate and domestic use. You power it on - there is a message here that was sent to an external address.It reads as follows: 'My sister, they are coming for me. These riots that are starting two streets over… They are a front, as per usual, and no doubt instigated by the Chrono-scum yet again - all they need is a convenient excuse to destroy what we have started to build here. I know they will direct the riots into the museum soon enough. I do not know if I have much time left, or if I will be able to get out of here alive. I have tried to destroy one of the keycards guarding our Box in that hideous model downstairs, but I do not know if I succeeded. The other keycard will have to be left here. I pray that that another operative comes to collect it - and that the Chrono-scum do not figure out where to look. I leave you with the last Question - I’m sure you know the answer. I love you, sister. Yours always, Monet.' Scrawled with what seems to be a knife at the bottom of the screen are the following words: 'Question 3: What entity is responsible for the Sakura Docks massacre?'",False,path1office_hololog1_use)

        # Panel
        path1office_panel_use={"self":"You can't do anything with this while you're ankle deep in water - you might get electrocuted. You have to figure out a way to fix it safely."}
        path1office_panel=Item("panel","It's an electrical panel. It doesn't seem to be connected to the sensor nearby but instead has wires that seem to lead out the door and back downstairs. It seems to be broken and you think you can see the issue with the wiring, but to fix it you probably need a screwdriver, or failing that, some sort of thin, flat object.",False,path1office_panel_use)

        # Panel Safe
        path1office_panel2_use={"self":"The rubber in the boots can act as an insulator for the electricity - now that you are wearing them, you can work on the panel safely. What you need now is to use some sort of thin, flat object on it."}
        path1office_panel2=Item("safepanel","It's an electrical panel. It doesn't seem to be connected to the sensor nearby but instead has wires that seem to lead out the door and back downstairs. It seems to be broken and you think you can see the issue with the wiring, but to fix it you probably need a screwdriver, or failing that, some sort of thin, flat object.",False,path1office_panel2_use)

        path1office_holodisplay_use={"self":"It's a standard hololodisplay, clearly belonging to someone that used to work here. The tag beside it reads 'Rachel Monet, Museum Director'. You power the holodisplay on - there is a message here that was sent to an external address.It reads as follows: 'Sister, I am making great progress here. It is truly rewarding being able to recruit people for the Shogunate cause right under the noses of the Chrono-scum. I have reprogrammed their propaganda display downstairs to show the real truth of what happened that fateful day - the new recording is set to a different frequency, so you have to use a holotool on it to get it to work. I’m sending you Question 2 that guards our Box, just in case something were to happen to me: Which individual specifically is responsible for the Sakura Docks massacre? Yours always, Monet.'"}

        path1office_holodisplay=Item("holodisplay","It's a standard hololodisplay, clearly belonging to someone that used to work here. The tag beside it reads 'Rachel Monet, Museum Director'. You power the holodisplay on - there is a message here that was sent to an external address.It reads as follows: 'Sister, I am making great progress here. It is truly rewarding being able to recruit people for the Shogunate cause right under the noses of the Chrono-scum. I have reprogrammed their propaganda display downstairs to show the real truth of what happened that fateful day - the new recording is set to a different frequency, so you have to use a holotool on it to get it to work. I’m sending you Question 2 that guards our Box, just in case something were to happen to me: Which individual specifically is responsible for the Sakura Docks massacre? Yours always, Monet.'",False,path1office_holodisplay_use)


        # Array of items
        path1office_items=[path1office_door, path1office_boxes,path1office_sensor,path1office_deskdummy,path1office_crackdummy,path1office_panel,path1office_holodisplay,knife,holotool]


        """
        TEXT FOR PATH 1, OFFICE
        """
        # Default text
        path1office1=f"The smell of dirty water is the first thing that hits you. The dripping from the ceiling below suddenly makes sense - this office, a sad little collection of desks of holodisplays, is ankle deep in water. Even before the riots, this place must not have been in great shape."

        path1office2="There are some posters of Admiral Radius on the walls, now partially peeling off - the humidity in here must be making the adhesive dissolve. You can't help but feel amused... It's an apt metaphor for what's happening to the stifling bureaucracy of Chronosia."

        path1office3=f"Near the [{path1office_door.name}] that leads back downstairs is a [{path1office_sensor.name}]... You've seen this kind of apparatus before - it's a patented Chronosia piece of engineering to prevent theft. You should take a look at it later." 

        path1office10=f"Right by the sensor near the door, there is some sort of electricity [{path1office_panel.name}]."

        path1office11=f"Right by the sensor near the door, there is some sort of electricity [{path1office_panel2.name}]."

        path1office4=f"Also of interest is the desk at the very back wall - it's slightly larger than all the others, so it's possible that it belonged to whoever was in charge of this department. On top of it stands a [{path1office_holodisplay.name}]."

        path1office5=f"Beside the desk and the holodisplay there are also some [{path1office_boxes.name}]. The [{path1office_deskdummy.name}] looks like it could have some useful things in it but you don't want to search it until you figure out a way to get objects out of this room."

        path1office6=f"With the boxes out of the way, you can now see that one of the floor tiles is made of a slightly different when compared to the others."

        path1office7=f"The makeshift tile is flimsy, and there seems to be a tiny [{path1office_crackdummy.name}] in the center. Come to think of it, this is probably the source of the ceiling leak on the main floor below."

        path1office8=f"With the crack in the floor now sufficiently wide, you should probably open the [desk] now."

        path1office9=f"The desk is now open. Inside are a [{path1office_keycard1.name}] and a [{path1office_hololog1.name}]. The keycard looks like it could squeeze through the crack if you 'use' it - you can then pick it up downstairs. There's probably no need to bring the hololog down to the main floor - you can just read it here."

        path1office12=f"The open desk near the wall at the back holds a single [{path1office_hololog1.name}]"

        # Array of default text items
        path1office=[path1office1, path1office2, path1office3,path1office10, path1office4, path1office5]




        """
        DEFAULT ITEMS FOR PATH 2
        """

        # Holotool
        path2_holotool_use={"self":"You place your finger on the lockslot and the device comes to live with a sickly green glow. Well, it seems to work... But you have to use this on something.", "knife":"Sadly, your knife is a non-electrical object - you can't hack it.", "terminal":"You can't use this yet - you don't have the right frequency.", "artwork":"You connect your holotool to the small metal sphere... It takes you a bit of time, but eventually you rewire the sensors to detect any nearby brightsteel. If you want, you can pick up this artwork now and use it in a particular area to see if there is any brightsteel around.", "tank":"You can't hack into the terminal located inside the tank - the tech here is too secure. You need to find the password."}
        path2_holotool=Item("holotool","A small, portable hacking device. While it won't work with complex security systems, it is quite handy for breaking into minor electrical systems and vehicles. Standard issue for all Shogunate operatives.", True, path2_holotool_use)

        # Knife
        path2_knife_use={"self":"You briefly consider carving a cross into your forehead, maybe this will allow you to masquerade as one of the Exers and gain accesse to their base? But know - this seems a little drastic. There has to be an easier way inside, one that doesn't involve self-mutilation.", "holotool":"You really don't want to break open your holotool - it seems to be working fine for now.","crucifixes":"It makes you feel ill to do this... But if you are going to infiltrate the Exers, you are going to have provide them with some evidence of your own brutality. You take your knife and saw at the loosely hanging finger of one of the corpses - it falls off and you put with the rest of your belongings. It is now added to your inventory.", "panel":"You know from experience that this isn't going to help - the glass is too strong to be cut. You need to find a different way around."}
        path2_knife=Item("knife","The Chrono-drones outnumber you, and have better equipment... but a knife in the right place can close such gaps. There are markings on its handle for every citizen you failed to save. It's only right that you remember them - noone else will.",True,path2_knife_use)


        """
        ITEMS FOR PATH 2, BATTLEFIELD
        """
        # Bridge
        path2battlefield_bridge_use={"self":"You turn around and walk back towards the bridge."}
        path2battlefield_bridge=Item("bridge","It's the path by which you arrived here - it leads back to the bridge.",False,path2battlefield_bridge_use)

        # Gate
        path2battlefield_gate_use={"self":"You push your way through the crowd, who thankfully don't seem to take much notice of you, and go through the gate."}
        path2battlefield_gate=Item("gate","It's a small gate that leads to some sort of alleyway - you wonder if you could get to a side entrance of the outpost this way.",False,path2battlefield_gate_use)

        # Street
        path2battlefield_street_use={"self":"You decide to avoid the riot and walk down the street to where the large shop is located."}
        path2battlefield_street=Item("street","It's a street the leads to the left, away from the riots - in the distance, you can see a large shop with an X drawn on it.",False,path2battlefield_street_use)

        # Pile
        path2battlefield_pile_use={"self":"You pry open the hand of the corpse holding the long pole... And are startled as the body convulses, coughing. It's still alive... At the moment, it's none of your concern. You add the pole to your inventory - it should come in handy later."}
        path2battlefield_pile=Item("pile","It's a grotesque pile of Exer corpses. You guess that there are maybe 10 or 12 bodies there already, but at the rate things are going you expect there to be a lot more by the time the night is through. This gang clearly does not discriminate - all ages and genders are among the bodies. At the very top is someone that doesn't look a day over 16 years. He is holding an almost comically long pole in his hands - it's almost twice his height. You could probably pick it up if you 'use' this pile.",False,path2battlefield_pile_use)

        # Pole
        path2battlefield_pole_use={"self":"You are sure that you will find a use for this pole over the course of this night... but you have to use it on something.", "sign":"You use the pole to try and hook the Chronosia jacket off the sign... It takes a bit of wrangling but eventually you manage to get it down. You add the uniform to your inventory - you can try wearing it by using the 'use uniform' command."}
        path2battlefield_pole=Item("pole","It's a long pole with a hook at the end. You vaguely recognise it as a tool the residents of the slums would use to pass items between different floors of their 'scraper shacks. It's so long that you have no idea how that poor kid was going to try to use this thing as a weapon... And now he never will.",False,path2battlefield_pole_use)

        # Door
        path2battlefield_door_use={"self":"While you do not fear death, trying to enter the outpost through this door would be suicidal. There seems to be a sniper on the roof of the building that is picking off those that get too close... You have to find another way in."}
        path2battlefield_door=Item("door","It's a door that leads to the main outpost... Where the Chrono-scum and, most likely at least one of the boxes, are holed up.",False,path2battlefield_door_use)

        # Array of items
        path2battlefield_items=[path2battlefield_bridge, path2battlefield_gate, path2battlefield_street, path2battlefield_pile, path2battlefield_door, knife, holotool]

        """
        TEXT FOR PATH 2, BATTLEFIELD
        """

        path2battlefield1=f"The wailing riot continues to throw garbage at the outpost [{path2battlefield_door.name}] ahead. Thankfully, they don't seem to be paying much attention to you."
        path2battlefield2=f"Every once in a while, an Exer runs forward to the outpost - a shot rings out, and the gang member crumples to the ground, upon which a few others scramble forwards and drag the fresh corpse into an ever growing [{path2battlefield_pile.name} of bodies."
        path2battlefield3=f"Behind you lies the way back to the [{path2battlefield_bridge.name}]."
        path2battlefield4=f"To the right, you can spot a small [{path2battlefield_gate.name}] - it looks like it could possibly lead to the back of the outpost..."
        path2battlefield5=f"Just down the [{path2battlefield_street.name}], on your left, you can see a large shop of some kind. It's unclear what the shop sells but even from this distance you can see that there's a massive X painted on the front of it - looks like it has been co-opted by the Exers as a makeshift headquarters."

        path2battlefield=[path2battlefield1, path2battlefield2, path2battlefield3, path2battlefield4, path2battlefield5]


        """
        ITEMS FOR PATH 2, TANK
        """
        # Bridge
        path2tank_path_use={"self":"You turn around and walk back towards the bridge."}
        path2tank_path=Item("path","It's the path by which you arrived here - it leads back to the bridge.",False,path2tank_path_use)

        # Crucifixes
        path2tank_crucifixes_use={"self":"It's disgusting. You don't want to be around here unless you have a specific reason."}
        path2tank_crucifixes=Item("crucifixes","Beside the tank stands a ghastly display of the Exers' brutality. There are seven crucifixes here, to which (now former) Chronosia agents are nailed, each in a different state of mutilation. The hand of a body nearest to you only has a single finger remaining, barely hanging on by a loose tendon. You feel a retch build up in your throat.", False, path2tank_crucifixes_use)

        # Finger
        path2tank_finger_use={"self":"It's the severed finger of a Chronosia agent. You really don't want to think about how you got this.", "man":"Gingerly, you pull the severed finger out of your belongings and show it to the man at the door. 'This, uh, wouldn't happen to be a good fit for your necklace, would it?' The man's face lights up immediately. His eyes, filled with ecstasy, are made even more demented when backlit by the burning bonfires on the street. 'Give!', he yells. He grabs the severed appendage and cradles it lovingly in his hands. 'I... I need to put this on right away,' he says, and disappears indoors. Looks like the way inside is clear - you are free to go in."}
        path2tank_finger=Item("finger","It's the severed finger of a Chronosia agent. You really don't want to think about how you got this.",False,path2tank_finger_use)

        path2tank_tank_use={"self":"One of the internal terminals inside the burning tank is still glowing... You can't believe that it's still working. You reach in, being careful to avoid the flames. You remember from earlier intelligence reports that the NX999 tank software system holds the most up-to-date frequency for Chronosia terminals - having this information might come in handy. To get at the frequency, you first need to log into this terminal somehow... The tech is too secure to hack into with your holotool. A prompt flashes onto the screen..."}
        path2tank_tank=Item("tank","It's the wreck of the NX999 tank that must have been part of the ill-fated convoy. You have absolutely no idea how the Exers managed to overturn this thing - must have been a hell of a job... You know from experience how tough it is to destroy blackened adamantium, which is what this machine's outer layer is made of. You should ask someone in charge about what happened here. The tank is burning, but inside you can see the faint glow of an internal terminal... You think you can probably reach it without burning yourself.",False,path2tank_tank_use)

        path2tank_mine_use={"self":"You need to be really careful about where to use this - this is not the place for that.", "lid": "This mine will definitely be able to melt through this lid... But doing this will no doubt unleash a swarm of Exers, who will destroy everything in this outpost. Even if this is something that you want to do, you need to leverage this information somehow - maybe it's time to have a little discussion with the Exers first."}
        path2tank_mine=Item("mine","It's a brightsteel mine, used by the Exers to destroy the NX999 tank. While ineffective against pretty much any kind of material, it works wonders to shred blackened adamantium. You need to be really careful with where you place this - you only have one shot to use it.",False,path2tank_mine_use)

        # Array of items
        path2tank_items=[path2tank_path, path2tank_crucifixes, path2tank_tank, knife, holotool]

        """
        TEXT FOR PATH 2, TANK
        """

        path2tank1=f"In a different time, this bridge could have been called beautiful. Now, it's a monument to everything wrong with this city - a living manifestation of the gap between the stupidly rich and the dirt poor."
        path2tank2=f"The smouldering wreck of the NX999 [{path2tank_tank.name}] still lies in the center of it, the flames making it difficult to approach."
        path2tank3=f"The [{path2tank_crucifixes.name}] are just nearby... You are used to violence, but the scene is difficult to look at, even for you."
        path2tank4=f"Behind you lies the [{path2tank_path.name}] back to the outpost."


        path2tank=[path2tank1, path2tank2, path2tank3, path2tank4]


        """
        ITEMS FOR PATH 2, OUTPOST ALLEY
        """

        # Gate
        path2alley_gate_use={"self":"You turn around and walk back through the gate, towards the main street."}
        path2alley_gate=Item("gate","It's the through which you came - it leads back to the main street, where the riot is taking place.",False,path2alley_gate_use)

        # Slit
        path2alley_slit_use={"self":"You bang on the door, and the small metal slit slides open. Behind it you can see a pair of nervous, young eyes - this kid is young, and on the verge of panic, by the looks of it. 'W-w-w-ho's there?' he asks."}
        path2alley_slit=Item("slit","It's a solid, metal door - you can tell from the design that the locks are built in such a way that it can only be opened from the inside... There's no breaking this one down. There's a closed slit in the door at around eye height, and you can hear some sort of shuffling behind it - looks like there's someone guarding the door. You're going to have to convince however is behind it to let you in if you're going to enter.",False,path2alley_slit_use)

        # Uniform
        path2alley_uniform_use={"self":"It's quiet here, and there are no Exers about. You put on the the Chronosia jacket - it doesn't fit particularly well, and the smell coming off it borders on the obscene. There is no need to take it off manually when you go back outside - you will remember to do so automatically.", "slit.":"You can't use the uniform with the door - if you want to wear the uniform, try the 'use uniform' command... This looks like a good place to put this on, in any event - there don't seem to be any Exers about."}
        path2alley_uniform=Item("uniform","It's a standard issue Chronosia Industries uniform jacket. The fabric contains particles of reinforced titanium to protect from laser blasts - but not blades, apparently, as this clothing item seems to be full of holes caused by them. There are some stains around the stomach area... The blood hasn't fully dried yet. To put it on, you have to type the 'use uniform' command.",False,path2alley_uniform_use)

        # Door
        path2alley_door_use={"self":"The guard spots you through the slit in the door and nods - the locks open and you push your way inside the outpost."}
        path2alley_door=Item("door","It's the large metal door that leads into Chronosia outpost - you are now free to come and go as you please.",False,path2alley_door_use)

        path2alley_items=[path2alley_gate, path2alley_slit, knife, holotool]

        """
        TEXT FOR PATH 2, OUTPOST ALLEY
        """
        path2alley1=f"The little alleyway that leads to the back of the outpost brings a small amount of relief from the violence outside."
        path2alley2=f"It is dark and cool, although you can see the odd flicker from the flames on the main street outside."
        path2alley3=f"Just ahead is a large steel door with a small [{path2alley_slit.name}] in it that looks like it might lead to the inside of the outpost."
        path2alley4=f"Behind you is the [{path2alley_gate.name}] through which you came." 
        path2alley5=f"In front of you is the [{path2alley_door.name}] that leads into the outpost. You can walk in and out of it freely now."

        path2alley=[path2alley1,path2alley2,path2alley3,path2alley4]


        """
        DIALOGUE FOR PATH 2, OUTPOST ALLEY
        """

        # THE GUARD

        dialogue2guard_1_option="[1] ‘Look, kid - I'm not with those thugs outside. I can help you get out of here but I need to speak to your boss - can you let me in?’"
        dialogue2guard_1_2="The guard somehow looks even more nervous."
        dialogue2guard_1_3="'I-I-I-I can't let you do that.' he says. 'I mean, I can't let you do that, sir'. He puts an undue amount of emphasis on the 'sir'."
        dialogue2guard_1_4="'Only Chronosia employees are permitted inside the outpost. I'm going to have to ask you respectfully to back away from the door.'"
        dialogue2guard_1_5="The threat rings hollow - you doubt he's capable of causing you any harm, but it's clear that he is following his instructions by the letter, and will not let you in unless you are a Chronosia employee."
        dialogue2guard_1=[dialogue2guard_1_option, dialogue2guard_1_2, dialogue2guard_1_3, dialogue2guard_1_4, dialogue2guard_1_5]

        dialogue2guard_2_option="[2] ‘What happened out there - how did those guys even manage to overturn your tank like that?’"
        dialogue2guard_2_2="There's a flash of pain in the guard's eyes, and then he manages to compose himself. He speaks in a quiet, reserved tone..."
        dialogue2guard_2_3="'I... don't know. We were transferring some items by convoy into this outpost from the southern district when the explosion hit.'"
        dialogue2guard_2_4="'I managed to escape, together with some of the others, when they started butchering the rest of my comrades.'"
        dialogue2guard_2_5="'Those people, they... They're not human.'"
        dialogue2guard_2_6="He trails off and goes quiet."
        dialogue2guard_2_7="The kid is completely shaken... Whatever it is that he has seen tonight, he will remember until his dying day."
        dialogue2guard_2=[dialogue2guard_2_option, dialogue2guard_2_2, dialogue2guard_2_3, dialogue2guard_2_4, dialogue2guard_2_5, dialogue2guard_2_6, dialogue2guard_2_7]

        dialogue2guard_3_option="[3] ‘I'm looking for two black boxes and I think they might be inside this outpost. You wouldn't happen to know if they are there, would you?’"
        dialogue2guard_3_2="There's a sudden recognition in the guard's eyes, as if he's shocked that you brought this up."
        dialogue2guard_3_3="'I, uh, have no idea what you're talking about.'"
        dialogue2guard_3_4="Something's not right here... It's clear that someone inside this outpost knows something about the boxes. You really need to find a way in."
        dialogue2guard_3=[dialogue2guard_3_option, dialogue2guard_3_2, dialogue2guard_3_3, dialogue2guard_3_4]

        dialogue2guard_4_option="[4] ‘You do know that it's not the Shogunate that are responsible for this, right? It's the Exers that are causing havoc in the city. No doubt the Shogunate will be blamed for this incident too.’"
        dialogue2guard_4_2="'That is lies and propoganda. The Shogunate are a menace to San Weyhoon and will be eradicated.'"
        dialogue2guard_4_3="The tone is unusually confident, coming from this kid. He's been totally brainwashed."
        dialogue2guard_4_4="You're not going to get anywhere trying to debate ideology with him - you need to find a way inside.."
        dialogue2guard_4=[dialogue2guard_4_option, dialogue2guard_4_2, dialogue2guard_4_3, dialogue2guard_4_4]

        dialogue2guard_exit_option="[0] ‘I need to step away for a while - hope the mob outside doesn't get you by the time I come back.’"

        dialogue2guard=[dialogue2guard_1, dialogue2guard_2, dialogue2guard_3, dialogue2guard_4, dialogue2guard_exit_option]

        # THE GUARD, AFTER JOINING EXERS

        lineguard1="Before you can ask your questions, there's a sudden flash of recognition in the guard's eyes."
        lineguard2="'Wait a second... Our sniper on the roof saw a man of your description walk into the base of those brutes just down the street."
        lineguard3="I'm afraid I can't let you in here, sir. You're going to have to back away from the door immediately.'"
        lineguard4="It looks like you've been made... You're going to need some really convincing proof you're not an enemy in order to get through this door now - something as simple as throwing on a Chronosia uniform just won't cut it."
        screenguard=[lineguard1,lineguard2,lineguard3, lineguard4]

        # THE GUARD, AFTER WEARING UNIFORM

        lineguard2_1="Before you can ask your questions, the guard spots your makeshift Chronosia uniform. His eyes light up."
        lineguard2_2="'Ah, a Chronosia man! Why didn't you says so in the first place? Come right in!'"
        lineguard2_3="What a gullible idiot. It's a good thing those maniacs outside are even dumber than him, otherwise this whole outpost would have been eradicated in minutes."
        lineguard2_4="Doesn't matter, at the end of the day - at least now you have free access in and out of this door. You hear the locks inside turn and tumble, and you push your way in."

        screenguard2=[lineguard2_1, lineguard2_2, lineguard2_3, lineguard2_4]

        """
        ITEMS FOR PATH 2, STREET 
        """

        # Man
        path2street_man_use={"self":"You walk up to the door... You are not a short person by any stretch of the imagination, but the size of the man in front of you causes an almost animal reaction of fear to bubble up inside you. If you are going to negotiate with the Exers, you are going to have to get past him, somehow - maybe it's time to ask a few questions."}
        path2street_man=Item("man","In front of the shop door is a massive, hulking brute of a man. The most noticable thing about him is the colossal metal exo plate that seems to take up over half of his head... The injury that led his head to such a state must have been severe indeed. He is wearing tattered, raggedy leather pants, and, much to your disgust, around his neck seems to be a necklace made of nine human fingers. They are still bleeding...",False,path2street_man_use)

        # Sign
        path2street_sign_use={"self":"You try and reach for the Chronosia jacket that's hanging off the sign, but you can't reach it from here - it's pretty high up."}
        path2street_sign=Item("sign","It's a flickering neon sign that says 'Featherdrum Fine Art Emporium' - it's in pretty bad shape. The letters are cracked and flickering, and staring at the erratic flashing lights gives you a bit of a headache. You seem to recall from an intelligence report that the higher-ups in Chronosia Industries had a significant shareholding in this outfit - they won't be too pleased by tonight's events... Draped over the last letter 'm' is a jacket from the standard issue Chronosia uniform. You struggle to imagine how it could have got there - the sign is pretty high up.",False,path2street_sign_use)

        # Uniform
        path2street_uniform_use={"self":"You are not wearing the uniform right now, but you don't want to put this on here. You think you can maybe take one Exer on in hand-to-hand combat, but if you start wearing the Chronosia colours in here they will swarm you and tear you apart. You should probably only wear this in a place where you won't be seen by any of the gang members."}
        path2street_uniform=Item("uniform","It's a standard issue Chronosia Industries uniform jacket. The fabric contains particles of reinforced titanium to protect from laser blasts - but not blades, apparently, as this clothing item seems to be full of holes caused by them. There are some stains around the stomach area... The blood hasn't fully dried yet. To put it on, you have to type the 'use uniform' command.",False,path2street_uniform_use)

        # Street
        path2street_street_use={"self":"You turn around and walk back to the main square."}
        path2street_street=Item("street","It's the street by which you came here - it leads back to the main street, where the riot is taking place.",False,path2street_street_use)

        # Door
        path2street_door_use={"self":"You take a deep breath and enter into the shop... into this den of violent sin. As you walk inside the shop... The thumping bass only gets louder. The sounds barely register as music - underneath the racket, you can barely make out staccato grunts that sound almost animal. It looks like the main floor is up the stairs, so you head up."}
        path2street_door=Item("door","It's the door that leads inside the shop... You can hear loud, thumping music coming from inside.",False,path2street_door_use)

        path2street_items=[path2street_street, path2street_man, path2street_sign, knife, holotool]

        """
        TEXT FOR PATH 2, STREET
        """
        path2street1=f"It is not entirely clear what the shop ahead of you sold originally - the neon [{path2street_sign.name}] above the front door, its letters smashed and distorted, seem to say 'Featherdrum Fine Art Emporium'."
        path2street2=f"Whatever this shop was before, it serves a different purpose now. The street is ablaze with makeshift bonfires, and there is a group of Exers scuttling from building to building, smashing the nearby windows with tools of different description."
        path2street3=f"The shop itself has a colossal X drawn on it - in front of it stands a massive, hulking brute of a [{path2street_man.name}] with an exo metal plate lodged in his head. There is no sign of any kind of intelligence in his eyes."
        path2street4=f"He seems to be acting as the muscle for this place - every once in a while you can see him let an Exer through the front door. It looks to be a place of importance for this gang - if you are going to try to negotiate with them, you are going to need to get through that door."
        path2street5=f"With the guard gone, you are now free to enter the shop via the [door] as you please. You can hear loud, thumping music coming from inside."
        path2street6=f"Behind you lies the [{path2street_street.name}] that leads back into the main square."

        path2street=[path2street1,path2street2,path2street3,path2street4,path2street6]


        """
        DIALOGUE FOR PATH 2, STREET
        """

        # THE BRUTE

        dialogue2man_1_option="[1] ‘What's inside this building?’"
        dialogue2man_1_2="The man looks at your forehead and narrows his eyes."
        dialogue2man_1_3="'It's not a place for you, outsider. If you're not an Exer, you're not welcome. Run along back to where you came from.'"
        dialogue2man_1_4="With those words, he taps a large metal crowbar across his hands menacingly."
        dialogue2man_1=[dialogue2man_1_option, dialogue2man_1_2, dialogue2man_1_3, dialogue2man_1_4]

        dialogue2man_2_option="[2] ‘How did the riots break out? I saw an overturned NX999 on the way in...’"
        dialogue2man_2_2="The man smiles, but his smile doesn't reach his eyes."
        dialogue2man_2_3="'It doesn't matter how, outsider. That scum got what they deserve."
        dialogue2man_2_4="They think we're too stupid to do any real damage, but look at us now. The Duchess will lead us to victory, and blood will flood the streets of San Weyhoon.'"
        dialogue2man_2_5="As the words leave his mouth, you can see him avert his gaze, as if he has said too much."
        dialogue2man_2_6="The Duchess... It's not a name you've heard before. Might be something to look into later."
        dialogue2man_2=[dialogue2man_2_option, dialogue2man_2_2, dialogue2man_2_3, dialogue2man_2_4, dialogue2man_2_5, dialogue2man_2_6]

        dialogue2man_3_option="[3] ‘I'm looking for two black boxes... You wouldn't happen to have seen any, would you?’"
        dialogue2man_3_2="'All property of the Chronoscum is now forfeit and belongs to the Exers. Those attempting to retrieve it shall pay with their blood.'"
        dialogue2man_3_3="The man rattles these words off like he has them memorised... Somethings not right here."
        dialogue2man_3_4="This level of chaos, it's not something that the Exers are capable of on their own. Someone is pulling the strings, in the background. But who?"
        dialogue2man_3=[dialogue2man_3_option, dialogue2man_3_2, dialogue2man_3_3, dialogue2man_3_4]

        dialogue2man_4_option="[4] ‘That's a nice, uh, necklace you have there...’"
        dialogue2man_4_2="The man looks down at his chest and an almost child-like glee spreads across his face."
        dialogue2man_4_3="He looks at the necklace lovingly - it is composed of nine human fingers, clearly freshly retrieved given the amount of bleeding."
        dialogue2man_4_4="'You like it? Just a little something I made from one of those rats in the convoy. His screams were exquisite.'"
        dialogue2man_4_5="His face darkens suddenly."
        dialogue2man_4_6="'I wanted all ten, but before I could finish it, they told me I had to come here and guard the damn door.'"
        dialogue2man_4_7="He looks almost on the verge of tears, like he's about to throw a tantrum. Clearly, this touched a nerve."
        dialogue2man_4=[dialogue2man_4_option, dialogue2man_4_2, dialogue2man_4_3, dialogue2man_4_4, dialogue2man_4_5, dialogue2man_4_6, dialogue2man_4_7]

        dialogue2man_exit_option="[0] ‘I'll be off now... We might speak again later.’"

        dialogue2man=[dialogue2man_1, dialogue2man_2, dialogue2man_3, dialogue2man_4, dialogue2man_exit_option]

        # THE BRUTE, AFTER JOINING CHRONOSIA

        lineman1="Before you can ask your questions, the man leans towards you and takes a deep breath... As he exhales you can smell the raw meat on his breath."
        lineman2="'I can smell the Chrono-scum on you... You've been inside their outpost, haven't you?'"
        lineman3="He looks enraged... You have no idea how he managed to figure out that you've been inside the Chronosia outpost, but it looks like you're not getting past him unless you really show him that you're on the side of the Exers... Trying to bribe him may have worked previously, but that won't cut it anymore - you are going to have to do something really drastic."

        screenman=[lineman1, lineman2, lineman3]


        """
        ITEMS FOR PATH 2, SHOP
        """

        # Door
        path2shop_door_use={"self":"The hypnotic, thumping bass, together with the incessant howling coming from the Exers, are making your head hurt. You go back downstairs and head outside."}
        path2shop_door=Item("door","It's the door that leads back downstairs and outside, onto the burning streets...",False,path2shop_door_use)

        # Panel
        path2shop_panel_use={"self":"There's no way that you're going to break through this... You're going to either have to find another way around, or talk to the woman inside from behind the glass."}
        path2shop_panel=Item("panel","It's a transparent panel made of sub-atomic quartz... The same kind of tech that is used in interrogation chambers by Chronosia. It makes sense for this shop to have this tech, given the amount of Chrono-scum laundering their money through this outfit... At any rate, you know from experience that virtually nothing - knives, bombs or guns - are going to help you get past this. You're going to have to find another way around.",False,path2shop_panel_use)

        # Terminal
        path2shop_terminal_use={"self":"You can't use it from behind the glass - your best shot is to track down the right frequency and use your holotool."}
        path2shop_terminal=Item("terminal","It looks like a standard issue Chronosia terminal. It glows with a sickly green light... If you had the right frequency, you could probably use your holotool to manipulate it. It sits right beside the window.",False,path2shop_terminal_use)

        # Window
        path2shop_window_use={"self":"You can't do anything with it standing outside the glass - if you're going to open it, you're going to have to find the mechanism to do so."}
        path2shop_window=Item("window","It's a large, shuttered window. You can see the flames from outside flicker through the tiny gaps and cast strange shadows on the room inside. The terminal sits right beside it.",False,path2shop_window_use)

        # Woman
        path2shop_woman_use={"self":"You walk up as close to the glass as possible. The woman looks at you - you can't tell the expression behind those dead, gas-mask eyes, but her  posture is one of menace. 'And who are you supposed to be?' she asks, the voice muffled through the mask's air filters. 'Look - I know that at least one of the black boxes that convoy was carrying is in this building,' you say, 'I can help you destroy the Chrono-scum holed up in that outpost - in exchange for one of the boxes.' The woman tilts her head to the side. 'A brash way to talk to the Duchess,' she says, 'but I respect directness. Yes, you are right - we do have one of the boxes here. I can let you have a peek inside... In exchange for a little job.' She lets out a raspy chuckle. 'Nothing a woman of your stature can't handle.'"}
        path2shop_woman=Item("woman","A large, hulking woman squats on top of a chair overseeing the carnage on the main floor. Her gas mask is tattered and frayed, and from it hang an assortment of cables and wires. The bulbous eye openings in the mask give her a bug-like appearance. Her left fist is tightly closed - she is holding something, but you can't tell what from this distance.",False,path2shop_woman_use)

        # Card
        path2shop_card_use={"self":"It's a small identification card used by Chronosia agents. The card says 'Commander Emily Yu'. The smiling face in the photograph looks nothing like you, but you have your scarf wrapped around your face to protect from the ashes of the burning streets - it's possible that this might trick one of the lower-ranking officers in Chronosia.", "man":"You decide to walk over to the man. He looks you up and down suspiciously,and mutters, 'And who in the hell are you supposed to be?' You hand him the identification card given to you by the Duchess. He looks at it... and is not impressed. 'Do you take me for an idiot, woman? This may have fooled poor Flynn outside, but I knew the woman who this belonged to personally. Now, I don't know who you are, but you better go on back to wherever it is that you came from.", "slit":"You hand the identification card through the slit... The eyes of the young guard light up. You don't think he has even processed what the name on the card is - he's just excited to see proof that more of his kind are live. What an idiot. 'Come right through, Commander Yu!' he says happily, and unlocks the door. You push your way in.", "leader":"You decide to walk over to the man. He looks you up and down suspiciously,and mutters, 'And who in the hell are you supposed to be?' You hand him the identification card given to you by the Duchess. He looks at it... and is not impressed. 'Do you take me for an idiot, woman? This may have fooled poor Flynn outside, but I knew the woman who this belonged to personally. Now, I don't know who you are, but you better go on back to wherever it is that you came from."}
        path2shop_card=Item("card","It's a small identification card used by Chronosia agents. The card says 'Commander Emily Yu'. The smiling face in the photograph looks nothing like you, but you have your scarf wrapped around your face to protect from the ashes of the burning streets - it's possible that this might trick one of the lower-ranking officers in Chronosia.",False,path2shop_card_use)

        # Podiums
        path2shop_podiums_use={"self":"You can't do anything with it standing outside the glass - if you're going to open it, you're going to have to find the mechanism to do so."}
        path2shop_podiums=Item("podiums","There are podiums placed all over this cramped room - they look like they once displayed art pieces, which now lie scattered on the floor. The one closest to you reads: 'A Flower Broken: A Memorial Piece in Honor of the Great Commander Yu, Gone Too Soon. Shogunate Scum Will Pay Tenfold For This Vicious Murder'. Underneath it, someone has scratched in the words, 'Year of Rebirth: 2114'.",False,path2shop_podiums_use)

        # Artwork
        path2shop_artwork_use={"self":"The piece of artwork that looks like a sphere seems to be quite promising. Maybe you should examine the artwork more closely."}
        path2shop_artwork=Item("artwork","There is artwork scattered all over the floor of this room... A symbol of the classist excess that cramps this city. You know that this so-called artwork was not created for personal expression - these objects are thrown together by the ultra-rich, who sell them to each other in order to write off their taxes and launder money coming from illicit activities. Disgusting. One of the object looks to be of use, however. It's a sphere that has several circuit-boards and sensors connected to it. You think you could probably use your holotool to re-wire them in such a way that it would be able to act as a makeshift brightsteel detector.",False,path2shop_artwork_use)

        # Button
        path2shop_button_use={"self":"You press the button... And the deep, thumping music in the room completely cuts out. There's a brief silence, and then the Exers turn toward you in unison and start howling in your direction. You press the button and the music starts up again... The Exers go back to what they were doing. That was a dumb idea, you think - why would you go around poking in random electronics in a base full of maniacal warlords?"}
        path2shop_button=Item("button","It's an unassuming button that sits inside this ancient electronics box. Only one way to find out what it does...",False,path2shop_button_use)

        # Switch
        path2shop_switch_use={"self":"You flick the switch... And the light in the room completely switches off, leaving you in complete darkness. The howling of the Exers somehow becomes even louder, and you can feel something brush up against your leg... You press the button and the lights switch back on. The Exers go back to what they were doing. That was a dumb idea, you think - why would you go around poking in random electronics in a base full of maniacal warlords?."}
        path2shop_switch=Item("switch","It's an unassuming switch that sits inside this ancient electronics box. Only one way to find out what it does....",False,path2shop_switch_use)

        # Slider
        path2shop_slider_use={"self":"You move the slider to the right... And the shuttered window inside the office of the woman in the gas mask begins to open. The woman glances at the opening window but doesn't seem to pay much attention to it - she just continues to sit there and look at the chaos in front of her through the glass. The window is now wide open."}
        path2shop_slider=Item("slider","It's an unassuming slider that sits inside this ancient electronics box. Only one way to find out what it does...",False,path2shop_slider_use)

        path2shop_items=[path2shop_door, path2shop_panel, path2shop_terminal, path2shop_window, path2shop_woman, path2shop_podiums, path2shop_artwork, path2shop_button, path2shop_switch, path2shop_slider]

        """
        TEXT FOR PATH 2, SHOP
        """

        path2shop1=f"Once you make your way to the top, the chaos here differs slightly from what is happening outside - in a way, it's almost sad. The Exers are packed in to this admittedly small room, once full of light and colour... Some are writhing against each other in a motion that could resemble dancing - or fighting."
        path2shop2=f"Above one of the walls is a large banner that reads 'Emily Yu Memorial Exhibition' - there are small [{path2shop_podiums.name}] placed around the room, on top of which originally stood glass cases full of artwork." 
        path2shop3=f"The cases are smashed to bits, and the [{path2shop_artwork.name}] now lies scattered on the ground."
        path2shop4=f"In the corner you see an Exer lounge beside a corpse wearing a Chronosia uniform. He is frantically plunging a knife in and out of the body. The Chronosia agent is long dead, obviously, and disfigured beyond recognition... He - it - now resembles nothing more than a pile of meat. Beside this sordid display is some kind of an ancient electronics box that contains a [{path2shop_button.name}], a [{path2shop_switch.name}] and a [{path2shop_slider.name}]."
        path2shop5=f"To the side is a small corridor that leads to an antechamber, of sorts - it's protected by a glass [{path2shop_panel.name}]."
        path2shop6=f"Inside it, a large [{path2shop_woman.name}] squats on top of a ceremonial chair, overseeing the carnage. She is wearing an ancient 20th century gas mask that is clearly no longer functioning... It looks like it's just for decoration."
        path2shop7=f"Behind her, close to the [{path2shop_window.name}] sits a standard [{path2shop_terminal.name}], which glows with a sickly green light."
        path2shop8=f"At the very back of this room is the [{path2shop_door.name}] from which you came - it leads back downstairs, to the outside."

        path2shop=[path2shop1, path2shop2, path2shop3, path2shop4, path2shop5, path2shop6, path2shop7, path2shop8]

        """
        DIALOGUE FOR PATH 2, SHOP  
        """


        # THE LEADER, BASIC VERSION

        womanBasic_1_option="[1] ‘Who are you?’"
        womanBasic_1_2="The Duchess lets out a dry, raspy chuckle." 
        womanBasic_1_3="'Child, I am the god of these pathetic beings."
        womanBasic_1_4="I am the terror of San Weyhoon, and the scourge of Chronosia, the Shogunate, and whoever else walks the streets of this pathetic city."
        womanBasic_1_5="I am the Duchess - and those that cross me shall fear my wrath.'"

        womanBasic_1=[womanBasic_1_option,womanBasic_1_2,womanBasic_1_3,womanBasic_1_4,womanBasic_1_5]

        womanBasic_2_option="[2] ‘What is it that you want me to do, exactly?’"
        womanBasic_2_2="'I want the men and women in that outpost dead... And I want them to die experiencing utter despair." 
        womanBasic_2_3="Chronosia is riddled with traitors, and each outpost has secret passageways that lead insurgents in and out - I want you to find this passageway and convince the people inside the outpost to escape through it."
        womanBasic_2_4="I want them to feel a speck of hope as they try to escape... A speck that will be taken away as my man slaughter them all on the way out.'"

        womanBasic_2=[womanBasic_2_option,womanBasic_2_2,womanBasic_2_3,womanBasic_2_4]

        womanBasic_3_option="[3] ‘I saw a flipped tank on the way in. How did you even manage to do that?’"
        womanBasic_3_2="'If you believe in the Duchess, anything is possible, child." 
        womanBasic_3_3="But if you want a more prosaic answer, we had intelligence reports confirming the route of the convoy. All it took was a few well-placed brightsteel technomines on the bridge... They never saw it coming."
        womanBasic_3_4="It was quite the breakthrough when we realised the havoc those mines, and the brighsteel that they're made of, could wreak on blackened adamantium... The shell of that tank dissolved in seconds."
        womanBasic_3_5="We probably went a bit over the top with the mines to be honest - some of them might still be left out on the bridge.'"

        womanBasic_3=[womanBasic_3_option,womanBasic_3_2,womanBasic_3_3,womanBasic_1_4,womanBasic_1_5]

        womanBasic_4_option="[4] ‘Why are you doing this? You're giving the rebellion a bad name, surely you know that the Shogunate are going to be blamed for this yet again.’"
        womanBasic_4_2="Something strange happens with the posture of the Duchess... What is that expression? Surely not fear?" 
        womanBasic_4_3="It only lasts a split-second - and then she relaxes, and continues with the same tone as before."
        womanBasic_4_4="'I couldn't care less about the inner working of your politics, child."
        womanBasic_4_5="I am an agent of chaos, and I will not rest until this city burns to the ground.'"
        womanBasic_4_6="Something about this exchange leaves you feeling extremely uneasy. What was that brief pause earlier? This whole set-up feels... wrong somehow. Someone is being played - but you're not sure who."

        womanBasic_4=[womanBasic_4_option,womanBasic_4_2,womanBasic_4_3,womanBasic_4_4, womanBasic_4_5,womanBasic_4_6]

        womanBasic_exit_option="[0] ‘Right, then - I'm going to go. I'll come back if I make any progress.’"

        womanBasic=[womanBasic_1, womanBasic_2, womanBasic_3, womanBasic_4, womanBasic_exit_option]


        # THE DUCHESS, AFTER PERMANENTLY JOINING EXERS

        lineWomanJoin1="'Very good', the Duchess says. 'You're going to need this.'"
        lineWomanJoin2="She takes out a small card and hands it to you - you add it to your inventory."
        lineWomanJoin3="'This should help you get inside the outpost - the person this card belonged to... Well, let's just say, she's not going to need it anymore.'"
        lineWomanJoin4="There's a hint of malice in her voice as she says this."
        lineWomanJoin5="'Now then. Any questions?'"
        screenWomanJoin=[lineWomanJoin1,lineWomanJoin2,lineWomanJoin3,lineWomanJoin4,lineWomanJoin5]

        # THE DUCHESS, AFTER ASKING FOR MORE TIME

        lineWomanThink1="'Fair enough', she says. 'You have to be careful about who you side with these days.'"
        lineWomanThink2="You can't see her facial expression through the mask but you can almost hear the smile through the garbled voice."
        lineWomanThink3="Something's not right... She's acting like she knows more than she lets on. Who is this woman?"
        lineWomanThink4="One thing's for sure - in order to get at the boxes, you are going to have to either ally with the Exers or with Chronosia. Both seem like bad choices at the moment... But you can't afford to be picky."
        screenWomanThink=[lineWomanThink1,lineWomanThink2,lineWomanThink3, lineWomanThink4]

        # THE DUCHESS, AFTER DOUBLE CROSSING

        lineWomanCross1="The woman tilts her head to the side."
        lineWomanCross2="'Ah, now this is something interesting, for once... A betrayal among the Crono-scum... How absolutely delicious."
        lineWomanCross3="There is nothing more that I like to see than my enemies betrayed, their last thoughts buried in misplaced trust."
        lineWomanCross4="For that alone, I would be willing to make a deal with you, yes. I don't know how you found this out, but we do indeed have one of the boxes here - I would be willing to let you have a peek at it... Provided that you do a little something for me.'"
        screenWomanCross=[lineWomanCross1,lineWomanCross2,lineWomanCross3,lineWomanCross4]


        """
        ITEMS FOR PATH 2, OUTPOST
        """

        # Door
        path2outpost_door_use={"self":"You hate the Chrono-scum... but the atmosphere here is depressing even for you. You turn arounds and head back outside."}
        path2outpost_door=Item("door","It's the door that leads back outside, into the alleyway...",False,path2outpost_door_use)

        path2outpost_leader_use={"self":"You decide to walk over to the man. He looks you up and down suspiciously, and mutters, 'And where the hell have you been? Go bring another box of ammo to Flynn upstairs - I think he's running short'. You compose yourself, and say: 'I've come here to help... I think my skills may be of use to you. All I want in exchange is some information about the black boxes that you have stashed in this outpost'. It's a gamble to be so brazen in front of this man who you have never met... But this is no time for subtlety, and these people are clearly desperate. The man looks at you again... He seems surprised that you are aware of the boxes. 'Well, we won't need the boxes if we're dead, now would we. Yeah, you look like a woman that can handle herself. Tell you what - you do a little job for us... And maybe we can let you have a peek inside the box for a while. We lost one, so you'll have to make do with the one that we do have. What do you say?"}
        path2outpost_leader=Item("leader","It's a short man, maybe in his mid 40s - he's badly shaven and looks like he has unresolved anger issues that he is taken out on the recruits around him. Given his current position... You don't blame him. He seems to be in charge here - if anyone knows anything about the boxes here, then it's him.",False,path2outpost_leader_use)

        path2outpost_wreath_use={"self":"Looking at this wreath fills you with a sense of gloom. You don't want to disturb this memorial."}
        path2outpost_wreath=Item("wreath","It's a large wreath made out of white flowers. The leaves have begun to yellow and fall a while ago. In the center of the wreath is a photo of a smiling young woman, wearing full ceremonial Chronosia uniform. The plaque underneath it reads, 'In Memoriam: Emily Yu (2088-2114) - Your service will never be forgotten'. Under the text is a stamped version of Admiral Radius' signature.",False,path2outpost_wreath_use)

        path2outpost_shelf_use={"self":"You have a look at the holologs on the shelf that seem slightly displaced... These could have some interesting information if someone was trying to access these recently. You decide to add them to your inventory - you can have a look at them later."}
        path2outpost_shelf=Item("shelf","It's a medium-size datapad shelf - not unusual to see it in a military installation like this one. Most of the data is in a pretty neat order, but you can see that there are three holologs that are slightly displaced... Someone has been reading these recently. You can probably add them to your inventory by choosing the 'use shelf' command.",False,path2outpost_shelf_use)

        path2outpost_hololog1_use={"self":"This hololog dates a few weeks back... It's sent from one of the Chronosia employees to Emily Yu, the former leader of this oupost. It talks about the fact that the Shogunate have managed to develop a new type of weapon called the technomines, made out of brightsteel - it completely dissolves blackened adamantium if it comes in contact with it. Interesting - you recall that the underside of the NX9 tank is made of blackened adamantium... Was this how the Exers outside managed to destroy the tank so easily? What's even more intriguing is the fact that you know for a fact that the Shogunate have never had access to such a weapon. You note that Emily Yu did not respond to this log.."}
        path2outpost_hololog1=Item("hololog1","This hololog dates a few weeks back... It's sent from one of the Chronosia employees to Emily Yu, the former leader of this oupost. It talks about the fact that the Shogunate have managed to develop a new type of weapon called the technomines, made out of brightsteel - it completely dissolves blackened adamantium if it comes in contact with it. Interesting - you recall that the underside of the NX999 tank is made of blackened adamantium... Was this how the Exers outside managed to destroy the tank so easily? What's even more intriguing is the fact that you know for a fact that the Shogunate have never had access to such a weapon. You note that Emily Yu did not respond to this log.",False,path2outpost_hololog1_use)

        path2outpost_hololog2_use={"self":"This hololog is of a slightly different format that all the others that you found on the shelf... It looks like it was made for personal use, and was accidentally left here, for whatever reason. The contents are of delusional ramblings that are barely coherent... Several of the pages just contains the sentence 'WE NEVER SAW HER BODY' typed over and over again. The sentence sends a chill down your spine... There's something important about this. But in the midst of this nonsense, you see that the author has taken the time to write down some key addresses and passwords. You don't recognise most of them, but there is one interesting entry that reads 'Chronosia Outpost Desk Computer Password = Year of Rebirth'."}
        path2outpost_hololog2=Item("hololog2","This hololog is of a slightly different format that all the others that you found on the shelf... It looks like it was made for personal use, and was accidentally left here, for whatever reason. The contents are of delusional ramblings that are barely coherent... But in the midst of this nonsense, you see that the author has taken the time to write down some key addresses and passwords. You don't recognise most of them, but there is one interesting entry that reads 'Chronosia Outpost Desk Computer Password = Year of Rebirth'.",False,path2outpost_hololog2_use)

        path2outpost_hololog3_use={"self":""}
        path2outpost_hololog3=Item("hololog3","This datapad looks like someone's research into the life of Commander Emily Yu, the former commander of this outpost, before her murder (allegedly at the hands of the Shogunate). It talks about her bright start as a Chronosia Industries cadet - it looks like she carried out a lot of work in engineering, particularly in connection with using blackened adamantium as the protective shell for the NX999 tank. It seems that she also designed the software system that allows the tanks to communicate with both each other and with the various Chronosia outposts. The only negative comment about her from anyone, really, can be seen in a mail communication from one of her superiors, where she is berated for constantly using her birth year as the root password for the NX999 tank software system. You note with some interest that her psychological profile reads that she has a fanatical devotion to Chronosia Industries, and will not hesitate to do anything to see it come to power. You chuckle to yourself as you read that this statement is listed as a 'positive' in Yu's psychological evaluation.",False,path2outpost_hololog3_use)

        path2outpost_shop_use={"self":"It's not entirely clear how you are planning to do anything to the shop from a roof of a building a street away, but it doesn't stop you from thinking about it. After a brief consideration, you realise that you cannot, in fact do anything from up here - maybe you should talk to the sniper specialist instead."}
        path2outpost_shop=Item("shop","It's the shop where the Exers are located. Being up at this height gives you a good overview of the carnage in the streets - you don't believe in a hell, but if it existed, it would look something like this. Of particular interest is a large window on the front-facing wall of the shop - it looks significant, somehow.",False,path2outpost_shop_use)

        path2outpost_officer_use={"self":"The man doesn't take his eyes off the scope of the sniper rifle as you approach him. Before you have the chance to say anything, he starts to speak, in a voice that's a little more high-pitched than you imagined... 'Don't know how you are, don't care. But I'm not speaking to you until the Commander has given the ok."}
        path2outpost_officer=Item("officer","It's a middle-aged, bearded man. He is holding an enormous sniper rifle, with which he takes remarkably accurate pot-shots at the Exers below. He seems to be getting a visible satisfaction from inflicting this level of violence. In his position... you don't blame him.",False,path2outpost_officer_use)

        path2outpost_desk_use={"self":"The built-in desk computer has a suspicious file located in one of the sub-directories... You decide to try your luck at entering the right password."}
        path2outpost_desk=Item("desk","Just a regular reception desk. It has a built-in screen - you take a quick scroll through the various files and directories. It seems to be just a normal administrative work computer... Except for one hidden, encrypted sub-directory. To be honest, you probably wouldn't have even spotted it were it not for your experience with digital espionage. Something isn't right with this file - it's password-protected. You maybe able to open it by typing in the right password.",False,path2outpost_desk_use)

        path2outpost_desk_use={"self":"The built-in desk computer has a suspicious file located in one of the sub-directories... You decide to try your luck at entering the right password."}
        path2outpost_desk=Item("desk","Just a regular reception desk. It has a built-in screen - you take a quick scroll through the various files and directories. It seems to be just a normal administrative work computer... Except for one hidden, encrypted sub-directory. To be honest, you probably wouldn't have even spotted it were it not for your experience with digital espionage. Something isn't right with this file - it's password-protected. You maybe able to open it by typing in the right password.",False,path2outpost_desk_use)

        path2outpost_lid_use={"self":"You can't open it - it's tightly shut. You have no idea how however it was that built this thing managed to seal it like this."}
        path2outpost_lid=Item("lid","It's a lid that appeared when you entered the password into the computer. It's completely smooth, and made out of a material that you recognise as blackened adamantium - the same material that the Chronosia Industries NX999 tanks are made of... Well, if the tank outside can be destroyed, then so can this lid.",False,path2outpost_lid_use)


        path2outpost_items=[path2outpost_door, path2outpost_leader, path2outpost_wreath, path2outpost_shelf, path2outpost_shop, path2outpost_officer, path2outpost_desk]

        """
        TEXT FOR PATH 2, OUTPOST
        """

        path2outpost1=f"The inside of the outpost is a large, open plan room with lavish decor. It suggests a time of opulence long gone - now, the room is filled with young men and women in Chronosia uniforms that look like they have seen too much. Some are sitting beside the wall with their knees brought up to their faces - their vacant stares suggest that they're not taking in what's happening around them."
        path2outpost2=f"A man that seems to be the [{path2outpost_leader.name}] of the outpost is barking orders at the ragtag recruits, who are carrying ammunition back and forth across the hallways."
        path2outpost3=f"Some of the recruits strap boxes to their backs and climb a ladder, which seems to lead to the roof."
        path2outpost4=f"In the area that looks like the main reception stands a [{path2outpost_desk.name}] - it's one of the more modern admin models, with a terminal built into it."
        path2outpost5=f"Also near the reception desk is a datapad [{path2outpost_shelf.name}] - it's full of all sorts of logs and records."
        path2outpost6=f"Behind you is the [{path2outpost_door.name}] from which you came - it leads back outside. Beside it sits a large memorial [{path2outpost_wreath.name}]."
        path2outpost7=f"If you climb up the ladder that the recruits are using, you end up on a wide space on the roof - here, a bearded Chronosia [officer] is picking off Exers that rush the main door below with an enormous sniper rifle."
        path2outpost8=f"Towards the right, you can see the [{path2outpost_shop.name}] where the Exers have made their base - it's a lot closer than you initially thought."
        path2outpost9=f"The tile beside the desk is now slid open - underneath is a [{path2outpost_lid.name}] made out of a black material."

        path2outpost=[path2outpost1, path2outpost2, path2outpost3, path2outpost4, path2outpost5, path2outpost6, path2outpost7, path2outpost8]

        # THE LEADER, CORE DIALOGUE

        leaderCore_1_option="[1] ‘What the hell is wrong with you? Was that really necessary?’"
        leaderCore_1_2="'Yes, yes, apologies for the inconvenince, and so on,' says the man dismissively."
        leaderCore_1_3="Surely you have seen that those savages outside have that mark on their foreheads as well..."
        leaderCore_1_4="We need someone to go infiltrate their base, and they won't let anyone in without that mark."
        leaderCore_1_5="And do stop complaining. If we get out of this alive I will personally pay for your surgery to have that mark removed.'"

        leaderCore_1=[leaderCore_1_option,leaderCore_1_2,leaderCore_1_3,leaderCore_1_4,leaderCore_1_5]

        leaderCore_2_option="[2] ‘So what is this job that you need me to do?’"
        leaderCore_2_2="'Yes, of course, by all means let's get right down to it."
        leaderCore_2_3="You are probably at this stage aware that the brutes that ambushed us clearly could not have had the organisational skills to launch such an attack. I'm sure most of them can barely read, let alone set explosives."
        leaderCore_2_4="Our sources tell us that their leader is someone called the Duchess, and that she is educated and deadly. She is located in the shop down the street, where the gang have set up their headquarters."
        leaderCore_2_5="Put simply... we want you to kill her. Once the Duchess is dead, I am sure that the mob outside will dissapate into random chaos, allowing us to escape. She is like a god to them, and we want you to destroy her."

        leaderCore_2=[leaderCore_2_option,leaderCore_2_2,leaderCore_2_3,leaderCore_2_4,leaderCore_2_5]

        leaderCore_3_option="[3] ‘How did you even get into this situation? That mob outside flipped your tank, I didn't even know that was possible.’"
        leaderCore_3_2="'Simply put, a combination of new leadership on the part of the gangs, and a lack of resources on the part of Chronosia."
        leaderCore_3_3="You have probably heard of the brutal murder of Emily Yu several months ago. She was the Commander who used to run this outpost... The Shogunate scum will pay for that crime one day."
        leaderCore_3_4="Commander Yu was a magnificent leader, and this outpost flourished under her command. Ever since her death, we simply have not had the resources to check all possible traps being laid by insurgents in this area."
        leaderCore_3_5="There's also the fact that this Duchess, the boss of the mob outside, seems to be doing a hell of a job riling those maniacs up. It was probably her idea to plant the bombs on the bridge... We never saw it coming.'"

        leaderCore_3=[leaderCore_3_option,leaderCore_3_2,leaderCore_3_3,leaderCore_3_4,leaderCore_3_5]

        leaderCore_4_option="[4] ‘They're going to blame this on the Shogunate again, aren't they? Isn't it clear that this is the work of a totally different gang?"
        leaderCore_4_2="There's a tiredness in the man's posture as he speaks... It sounds like he has heard this all before."
        leaderCore_4_3="'Lady, I don't care about the politics of whatever is happening here."
        leaderCore_4_4="Shogunate, Exers, whoever else... The only thing I know that we are under siege, and I'm just trying to survive tonight."
        leaderCore_4_5="By any means necessary.'"

        leaderCore_4=[leaderCore_4_option,leaderCore_4_2,leaderCore_4_3,leaderCore_4_4,leaderCore_4_5]

        leaderCore_5_option="[5] ‘Any tips on where to get started?'"
        leaderCore_5_2="The man sighs."
        leaderCore_5_3="'Go over to the base of those maniacs and see what's going over there. We're sure that their leader is holed up somewhere."
        leaderCore_5_4="Maybe check in with Kim upstairs... He's been monitoring the situation from the roof. He might be able to give you some more info."
        leaderCore_5_5="Remember, lady - the Duchess must die. By any means necessary.'"

        leaderCore_5=[leaderCore_5_option,leaderCore_5_2,leaderCore_5_3,leaderCore_5_4,leaderCore_5_5]

        leaderCore_exit_option="[0] ‘Right, then - I'm going to go. I'll come back if I make any progress.’"

        leaderCore=[leaderCore_1,leaderCore_2, leaderCore_3, leaderCore_4, leaderCore_5,  leaderCore_exit_option]


        # THE LEADER, BASIC VERSION

        leaderBasic_1_option="[1] ‘So what is this job that you need me to do?’"
        leaderBasic_1_2="'Have I not explained this to you before? Never mind, I guess I'll repeat myself."
        leaderBasic_1_3="You are probably at this stage aware that the brutes that ambushed us clearly could not have had the organisational skills to launch such an attack. I'm sure most of them can barely read, let alone set explosives."
        leaderBasic_1_4="Our sources tell us that their leader is someone called the Duchess, and that she is educated and deadly. She is located in the shop down the street, where the gang have set up their headquarters."
        leaderBasic_1_5="Put simply... we want you to kill her. Once the Duchess is dead, I am sure that the mob outside will dissapate into random chaos, allowing us to escape. She is like a god to them, and we want you to destroy her."

        leaderBasic_1=[leaderBasic_1_option,leaderBasic_1_2,leaderBasic_1_3,leaderBasic_1_4,leaderBasic_1_5]

        leaderBasic_2_option="[2] ‘How did you even get into this situation? That mob outside flipped your tank, I didn't even know that was possible.’"
        leaderBasic_2_2="'Simply put, a combination of new leadership on the part of the gangs, and a lack of resources on the part of Chronosia."
        leaderBasic_2_3="You have probably heard of the brutal murder of Emily Yu several months ago. She was the Commander who used to run this outpost... The Shogunate scum will pay for that crime one day."
        leaderBasic_2_4="Commander Yu was an incredible leader, and this outpost flourished under her command. Ever since her death, we simply have not had the resources to check all possible traps being laid by insurgents in this area."
        leaderBasic_2_5="There's also the fact that this Duchess, the boss of the mob outside, seems to be doing a hell of a job riling those maniacs up. It was probably her idea to plant the bombs on the bridge... We never saw it coming.'"

        leaderBasic_2=[leaderBasic_2_option,leaderBasic_2_2,leaderBasic_2_3,leaderBasic_2_4,leaderBasic_2_5]

        leaderBasic_3_option="[3] ‘They're going to blame this on the Shogunate again, aren't they? Isn't it clear that this is the work of a totally different gang?"
        leaderBasic_3_2="There's a tiredness in the man's posture as he speaks... It sounds like he has heard this all before."
        leaderBasic_3_3="'Lady, I don't care about the politics of whatever is happening here."
        leaderBasic_3_4="Shogunate, Exers, whoever else... The only thing I know that we are under siege, and I'm just trying to survive tonight."
        leaderBasic_3_5="By any means necessary.'"

        leaderBasic_3=[leaderBasic_3_option,leaderBasic_3_2,leaderBasic_3_3,leaderBasic_3_4,leaderBasic_3_5]

        leaderBasic_4_option="[4] ‘Any tips on where to get started?'"
        leaderBasic_4_2="The man sighs."
        leaderBasic_4_3="'Go over to the base of those maniacs and see what's going over there. We're sure that their leader is holed up somewhere."
        leaderBasic_4_4="Maybe check in with Kim upstairs... He's been monitoring the situation from the roof. He might be able to give you some more info."
        leaderBasic_4_5="Remember, lady - the Duchess must die. By any means necessary.'"

        leaderBasic_4=[leaderBasic_4_option,leaderBasic_4_2,leaderBasic_4_3,leaderBasic_4_4,leaderBasic_4_5]

        leaderBasic_exit_option="[0] ‘Right, then - I'm going to go. I'll come back if I make any progress.’"

        leaderBasic=[leaderBasic_1,leaderBasic_2, leaderBasic_3, leaderBasic_4,  leaderBasic_exit_option]

        # THE LEADER, AFTER PERMANENTLY JOINING CHRONO

        lineLeaderJoin1="The old man chuckles. 'Good. Flynn? Kim? As discussed'."
        lineLeaderJoin2="The tone is awfully casual, and makes you nervous for some reason."
        lineLeaderJoin3="Out of nowhere, two men, one of whom you recognise as the guard from the door, grab you and force you to the ground - you're too slow to react, and you are pinned down almost immediately."
        lineLeaderJoin4="'I'm sorry,' whispers the guard, his eyes almost on the verge of tears, as he grabs a knife from his belt and begins to cut."
        lineLeaderJoin5="You can feel the blade trace a searing hot line across your head, first one, then another... And then it's done, an 'X' branded across your forehead, and you are released."
        screenLeaderJoin=[lineLeaderJoin1,lineLeaderJoin2,lineLeaderJoin3, lineLeaderJoin4, lineLeaderJoin5]

        # THE LEADER, AFTER ASKING FOR MORE TIME

        lineLeaderThink1="'Don't take too long to decide, now,' the man says, with a wry chuckle."
        lineLeaderThink2="'By the time you come back, this building might no longer be standing."
        lineLeaderThink3="And you know what those savages are like... they're raze this whole thing to the ground. You won't find your box after they're through.'"
        lineLeaderThink4="He's right... You need to make up your mind - you're going to need to ally yourself with the Exers or the Chronosia troops to track down at least one of the boxes."
        screenLeaderThink=[lineLeaderThink1,lineLeaderThink2,lineLeaderThink3, lineLeaderThink4]

        # THE LEADER, AFTER DOUBLE CROSSING

        lineLeaderCross1="The man furrows his brow."
        lineLeaderCross2="'Yes, well, that sounds like something that the Duchess would try to cook up..."
        lineLeaderCross3="I think I would be willing to make a deal, yes. It would be helpful to have someone with an in with the Duchess on our side. We would be willing to let you have a peek at one of the boxes - provided that you do a job for us.'"
        screenLeaderCross=[lineLeaderCross1,lineLeaderCross2,lineLeaderCross3]



        """
        LOCATION ARRAY FOR PATH 2
        """

        path2location_items=[path2battlefield_items, path2alley_items, path2street_items, path2shop_items, path2outpost_items, path2tank_items]















        ClearScreen()
        header2()
        print()
        print("Where will you search?")
        print("[1] The museum (Box 1)")
        print("[2] The outpost (Box 2 and Box 3)")
        branchingpath=str(input("Please make your choice: "))

        if branchingpath=="1" or branchingpath=="2" or branchingpath.lower()=="bomb":
            branchingPathLoop==False
            break
        else:
            input("Sorry, invalid input. Press Enter and try again.")

    if branchingpath.lower()!="bomb":

        # MUSEUM
        if branchingpath=="1":
            ClearScreen()

            screensInRange(totalScreenList, 61, 62);

            # PUZZLES FOR THE FIRST PATH

            # My word this is scaldy, find a way to refactor later        
            bool1,bool2,bool3,bool5 = False,False,False,False
            # Setting looping for the entire path
            looping_path1=True
            museumEnding=False

            # Clear inventory if user has gone down other paths
            inventory.inventory.clear()

            # Add standard items to inventory
            inventory.inventory.append(knife)
            inventory.inventory.append(holotool)

            path1office_door.item_used_alone=True

            while looping_path1:

                if path1office_door.item_used_alone:

                    # User goes to main room
                    looping_path1main=True

                    # Closes the door from second floor
                    path1office_door.item_used_alone=False

                    while looping_path1main:

                        # If main door has been used, break out of loop and go to second floor
                        if path1main_door.item_used_alone:
                            looping_path1main=False
                        else:
                            if path1main_computer.item_used_alone:
                                ClearScreen()
                                header2()
                                print()
                                q1=input("Please type your answer to question 1: ")
                                if q1=="2102":
                                    print()
                                    q2=input("Please type your answer to question 2: ")
                                    if "turner" in q2.lower():
                                        print()
                                        q3=input("Please type your answer to question 3: ")
                                        if "chronosia" in q3.lower():
                                            museumEnding=True
                                            looping_path1main=False
                                            path1main_door.item_used_alone=False
                                        else:
                                            ClearScreen()
                                            header2()
                                            print()
                                            print("Sorry that is not correct...")
                                            print("Please press enter to return")
                                            path1main_computer.item_used_alone=False
                                    else:
                                        ClearScreen()
                                        header2()
                                        print()
                                        print("Sorry that is not correct...")
                                        print("Please press enter to return")
                                        path1main_computer.item_used_alone=False
                                else:
                                    ClearScreen()
                                    header2()
                                    print()
                                    print("Sorry that is not correct...")
                                    input("Please press enter to return")
                                    path1main_computer.item_used_alone=False

                            if path1main_statue.item_used_alone and path1main_keycard1 in inventory.inventory and path1main_keycard2 in inventory.inventory:
                                removeFromScene(path1main6, path1main)
                                addToScene(path1main12, path1main)
                                addToScene(path1main_computer, path1main_items)
                                removeFromScene(path1main_statue,path1main_items)

                            if path1main_keycard1 in inventory.inventory:
                                removeFromScene(path1main7, path1main)
                                removeFromScene(path1main8, path1main)

                            if path1main_boots.item_used_alone:
                                removeFromScene(path1main10, path1main)
                                removeFromScene(path1office10, path1office)
                                addToScene(path1office11, path1office)
                                removeFromScene(path1office_panel, path1office_items)
                                addToScene(path1office_panel2, path1office_items)


                            if path1main_display.item_used_with_otherItem:
                                addToScene(path1main_keycard2, path1main_items)
                                addToScene(path1main_keycard2, inventory.inventory)
                                removeFromScene(path1main4, path1main)
                                removeFromScene(path1main11, path1main)

                            if path1main_baton.item_used_with_otherItem:
                                addToScene(path1main_tip, inventory.inventory)
                                addToScene(path1main_tip, path1office_items)
                                removeFromScene(path1main_baton, path1main_items)
                                removeFromScene(path1main9, path1main)

                            if path1main_dispenser.item_used_alone:
                                if path1main_token not in inventory.inventory:
                                    inventory.inventory.append(path1main_token)
                                    if path1main_token not in path1main_items:
                                        path1main_items.append(path1main_token)
                                if path1main5 in path1main:
                                    path1main.remove(path1main5)
                                    if path1main_dispenser in path1main_items:
                                        path1main_items.remove(path1main_dispenser)

                            if looping_path1main:
                                puzzleNavigation(path1main, path1main_items)

                elif path1main_door.item_used_alone:

                    # User goes to second floor
                    looping_path1office=True

                    # Closes the door from the main floor
                    path1main_door.item_used_alone=False

                    # If second floor door has been used, break out of loop and go back to main floor
                    while looping_path1office:
                        if path1office_door.item_used_alone:
                            looping_path1office=False
                        else:
                            if path1office_keycard1.item_used_alone:
                                if path1main1 in path1main and path1main2 in path1main:
                                    path1main.remove(path1main1)
                                    path1main.remove(path1main2)
                                    path1main.append(path1main7)
                                if path1office_keycard1.item_used_alone:
                                    if path1main8 not in path1main:
                                        path1main.append(path1main8)
                                        if path1main_keycard1 not in path1main_items:
                                            path1main_items.append(path1main_keycard1)
                                        if path1office_keycard1 not in path1office_items:
                                            path1main_items.append(path1office_keycard1)
                                        if path1office12 not in path1office:
                                            path1office.append(path1office12)
                                        if path1office9 in path1office:
                                            path1office.remove(path1office9)

                            if path1main_keycard1 in inventory.inventory:
                                if path1main8 in path1main:
                                    path1main.remove(path1main8)
                            
                            if path1office_panel2.item_used_with_otherItem:
                                if path1main4 in path1main:
                                    path1main.remove(path1main4)
                                if path1main11 not in path1main:
                                    path1main.append(path1main11)
                                if path1main_display not in path1main_items:
                                    path1main_items.append(path1main_display)

                            if path1office_boxes.item_used_alone and bool1==False:
                                if path1office6 not in path1office and path1office8 not in path1office:
                                    path1office.append(path1office6)
                                    path1office.append(path1office7)
                                    path1office.remove(path1office5)
                                    path1office_items.remove(path1office_boxes)
                                    path1office_items.append(path1office_crackdummy)
                                    bool1=True

                            if path1office_crackdummy.item_used_with_otherItem and bool2==False:
                                if path1office8 not in path1office:
                                    path1office.append(path1office8)
                                    path1office.remove(path1office6)
                                    path1office.remove(path1office7)
                                    path1office_items.remove(path1office_crackdummy)
                                    path1office_items.append(path1office_desk)
                                    bool2=True

                            if path1office_desk.item_used_alone and bool3==False:
                                if path1office9 not in path1office:
                                    path1office.append(path1office9)
                                    path1office.remove(path1office8)
                                    path1office_items.remove(path1office_desk)
                                    path1office_items.append(path1office_keycard1)
                                    path1office_items.append(path1office_hololog1)
                                    bool3=True

                            initialHeader()
                            displayPuzzleText(path1office)
                            print()
                            display_commands()
                            command=input().lower()
                            if "examine" in command:
                                examine_command(command,path1office_items)
                            elif "pick" in command:
                                pick_command(command,path1office_items)
                            elif command=="inventory":
                                inventory_command()
                            elif "use" in command:
                                use_command(command,path1office_items)

                elif museumEnding:
                    museumEnding=False
                    looping_path1=False
                    ClearScreen()
                    screensInRange(totalScreenList, 68, 73)                

        # STANDOFF
        elif branchingpath=="2":

            ClearScreen()
            screensInRange(totalScreenList, 63, 67);

            # PUZZLES FOR THE SECOND PATH

            # Setting looping for the entire path
            looping_path2=True

            # Clear inventory if user has gone down other paths
            inventory.inventory.clear()

            # Add standard items to inventory
            addItemEverywhere(path2_holotool, path2location_items)
            addItemEverywhere(path2_knife, path2location_items)

            # Setting the first room in the bridge
            path2tank_path.item_used_alone=True

            joinedExers=False
            permExers=False

            joinedChrono=False
            permChrono=False

            chronoCross=False
            exerCross=False

            exerEnding=False
            chronoEnding=False

            talkedToSniper=False
            gotFrequency=False

            while looping_path2:

                # Check if any paths were used to go into the main street
                if path2tank_path.item_used_alone or path2alley_gate.item_used_alone or path2street_street.item_used_alone:

                    # Don't forget to switch off all the other guys
                    path2tank_path.item_used_alone=False
                    path2alley_gate.item_used_alone=False
                    path2street_street.item_used_alone=False

                    # Entering the battlefield
                    looping_path2battlefield=True
                    while looping_path2battlefield:

                        # Check if player is going to another map
                        if path2battlefield_bridge.item_used_alone or path2battlefield_gate.item_used_alone or path2battlefield_street.item_used_alone:
                            looping_path2battlefield=False

                        # General gameplay
                        else:

                            if path2battlefield_pile.item_used_alone:
                                addItemEverywhere(path2battlefield_pole, path2location_items)
                                removeFromScene(path2battlefield_door, path2battlefield)

                            puzzleNavigation(path2battlefield, path2battlefield_items)

                # Entering bridge
                elif path2battlefield_bridge.item_used_alone:
                    
                    looping_path2bridge=True
                    path2battlefield_bridge.item_used_alone=False

                    if path2shop_artwork in inventory.inventory:
                        path2shop_artwork.item_used_alone=False
                        path2shop_artwork_use["self"]="You switch on the sensor on the makeshift sphere... and hear a high-pitched beeping. Looks like there is some brightsteel around. You look around the bridge as the beeping increases - the tone becomes continuous as you approach one of the railings. You look behind it... And spot a brighsteel technomine. Looks like this is how the Exers managed to flip the tank - these mines are lethal against the blackaned adamantium the underside of the NX9999 is made of. You gingerly pick at the small item and place it in your inventory - this is sure to come in handy."

                    
                    while looping_path2bridge:
                        if path2tank_path.item_used_alone:
                            looping_path2bridge=False
                            if path2shop_artwork in inventory.inventory:
                                path2shop_artwork_use["self"]="You switch on the sensor on the makeshift sphere... There is no noise being emitted. You are certain there is no brightsteel in this area."
                        else:
                            
                            if path2tank_tank.item_used_alone:
                                path2tank_tank.item_used_alone=False
                                ClearScreen()
                                header2()
                                print()
                                tank_pw=str(input("Please type in the root password: "))
                                if tank_pw=="2088":
                                    
                                    gotFrequency=True
                                    removeFromScene(path2tank2, path2tank)
                                    removeFromScene(path2tank_tank, path2tank_items)
                                    path2_holotool_use["terminal"]="Now that you have sourced the correct frequency to the Chronosia terminals, you are able to 'ping' the one behind the glass. You discreetly press the appropriate commands on your holotool... And you can see the terminal in the back come to life. It beeps rapidly - the Duchess turns around to check the disturbance, and walks over to the terminal. She seems a little confused about where the sound has come from - you can see her try to type something into the terminal angrily."


                                    print()
                                    print("The screen reads: 'Authentication... Successful.'")
                                    print("'Welcome back, Commander Emily Yu.'")
                                    print()
                                    print("The output on the screen is pretty garbled, but you think that you can spot the 64-bit frequency key that is used to communicate with other Chronosia terminals.")
                                    print("Realistically, the only thing you will be able to do with this is ping the various terminals, causing them to beep - you won't be able to access any of their files unless you're very close to them.")
                                    print()
                                    print("Still, this is better than nothing - you copy the frequency to your holotool.") 
                                    print("Next time that you 'use' your holotool in the vicinity of a Chronosia terminal, it will ping.")
                                    print()
                                    input("Press Enter to continue.")
                                else:
                                    print()
                                    print("Sorry, password is incorrect. Please try again later.")
                                    input("Press Enter to continue.")

                            if path2shop_artwork.item_used_alone:
                                addItemEverywhere(path2tank_mine, path2location_items)
                                removeItemEverywhere(path2shop_artwork, path2location_items)

                            if path2tank_crucifixes.item_used_with_otherItem:
                                path2tank_crucifixes.item_used_with_otherItem=False
                                addItemEverywhere(path2tank_finger, path2location_items)
                                                    
                                removeFromScene(path2tank_crucifixes, path2tank_items)
                                removeFromScene(path2tank3, path2tank)
                            
                            puzzleNavigation(path2tank, path2tank_items)

                # Entering alleyway
                elif path2battlefield_gate.item_used_alone or path2outpost_door.item_used_alone:

                    looping_path2gate=True
                    path2battlefield_gate.item_used_alone=False
                    path2outpost_door.item_used_alone=False

                    while looping_path2gate:
                        if path2alley_gate.item_used_alone:
                            looping_path2gate=False
                        elif path2alley_door.item_used_alone:
                            looping_path2gate=False
                        else:

                            # Someone is 100% going to try and use the uniform with the door, which is fair enough to be honest. Switching this off if someone does try this in case I need this functionality later.

                            if path2alley_slit.item_used_with_otherItem and path2shop_card.item_used_with_otherItem:
                                path2alley_slit.item_used_with_otherItem=False
                                path2shop_card.item_used_with_otherItem=False
                                removeFromScene(path2alley3, path2alley)
                                removeFromScene(path2alley_slit, path2alley)
                                addToScene(path2alley5, path2alley)
                                addToScene(path2alley_door, path2alley_items)
                                looping_path2gate=False
                                path2alley_door.item_used_alone=True

                            # Trying to open the main door
                            if path2alley_slit.item_used_alone:
                                
                                # Switch off the door for subsequent attempts
                                path2alley_slit.item_used_alone=False

                                # Showing text if you joined the Exers first
                                if joinedExers:
                                    ClearScreen()
                                    display(screenguard)

                                # If haven't joined Exers and wearing uniform, door is now open and we shift around the text appropriately
                                elif path2alley_uniform.item_used_alone:
                                    path2alley_uniform.item_used_alone=False
                                    ClearScreen()
                                    display(screenguard2)
                                    removeFromScene(path2alley3, path2alley)
                                    removeFromScene(path2alley_slit, path2alley)
                                    addToScene(path2alley5, path2alley)
                                    addToScene(path2alley_door, path2alley_items)
                                    joinedChrono=True

                                    # Delete the uniform from everywhere and add flavour text to give the impression that the item is still being used
                                    removeItemEverywhere(path2street_uniform, path2location_items)
                                    removeFromScene(path2alley_uniform, path2alley_items)
                                    path2battlefield_gate_use["self"]="You push your way through the crowd, who thankfully don't seem to take much notice of you, and go through the gate. You change into your Chronosia uniform as you walk through."
                                    path2alley_gate_use["self"]="You turn around and walk back through the gate, towards the main street. You make sure to take off your Chronosia uniform as you walk through."

                                    # Flavour text for what happens when you try to give the Exer guard the severed finger
                                    path2tank_finger_use["man"]="Gingerly, you pull the severed finger out of your belongings and show it to the man at the door. 'This, uh, wouldn't happen to be a good fit for your necklace, would it?' The man's face lights up immediately... But suddenly, his eyes dim, and he looks at you a little closer. He takes a deep breath, and as he exhales you can smell the raw meat on his breath. 'I can smell the Chrono-scum on you... You've been inside their outpost, haven't you?' He grabs the finger from your hands. 'The only reason I am letting you live is because of this gift... You better not show your face here again.' It looks like he means it - you have no idea how he managed to tell that you've been inside the outpost, but one thing is certain now. To get inside this shop, you're now going to really have to try and show this man that you're on the side of the Exers."

                                    looping_path2gate=False
                                    path2alley_door.item_used_alone=True


                                # Otherwise, display world-building flavour text and various hints
                                else:
                                    dialogueChoices(dialogue2guard)
                            if looping_path2gate:
                                # General gameplay
                                puzzleNavigation(path2alley, path2alley_items)

                # Entering street
                elif path2battlefield_street.item_used_alone or path2shop_door.item_used_alone:
                    
                    looping_path2street=True
                    path2battlefield_street.item_used_alone=False
                    path2shop_door.item_used_alone = False

                    while looping_path2street:
                        if path2street_street.item_used_alone or path2street_door.item_used_alone:
                            looping_path2street=False
                        else:

                            if path2street_man.item_used_alone:
                                path2street_man.item_used_alone=False

                                # This is what happens once you get the carving on your forehead
                                if permChrono:
                                    addToScene(path2street5, path2street)
                                    addToScene(path2street_door, path2street_items)
                                    removeFromScene(path2street3, path2street)
                                    removeFromScene(path2street4, path2street)
                                    removeFromScene(path2street_man, path2street_items)
                                    path2street_door.item_used_alone=True
                                    looping_path2street=False

                                elif joinedChrono:
                                    ClearScreen()
                                    display(screenman)
                                else:
                                    dialogueChoices(dialogue2man)

                            if path2street_sign.item_used_with_otherItem:
                                addItemEverywhere(path2street_uniform, path2location_items)
                                removeFromScene(path2street_uniform, path2alley_items)
                                addToScene(path2alley_uniform, path2alley_items)
                                removeFromScene(path2street1, path2street)

                            if path2street_man.item_used_with_otherItem: 
                                
                                path2street_man.item_used_with_otherItem=False

                                if joinedChrono==False or permChrono==True:
                                    if permChrono==False:
                                        joinedExers=True
                                    addToScene(path2street5, path2street)
                                    addToScene(path2street_door, path2street_items)
                                    removeFromScene(path2street3, path2street)
                                    removeFromScene(path2street4, path2street)
                                    removeFromScene(path2street_man, path2street_items)
                                    path2street_door.item_used_alone=True
                                    looping_path2street=False

                                removeItemEverywhere(path2tank_finger, path2location_items)
                            
                            # What a hideous fix lol
                            if looping_path2street:
                                puzzleNavigation(path2street, path2street_items)

                # Entering the shop from the street door
                elif path2street_door.item_used_alone:

                    # Switching on looping for the shop room
                    looping_path2shop=True

                    # Closing door behind us
                    path2street_door.item_used_alone=False

                    while looping_path2shop:

                        # If using the door, quit loopiong
                        if path2shop_door.item_used_alone:
                            looping_path2shop=False
                        else:

                            if path2shop_terminal.item_used_with_otherItem==True:
                                path2shop_terminal.item_used_with_otherItem=False

                                if gotFrequency:
                                    if talkedToSniper:
                                        if path2shop_slider not in path2shop_items:
                                            chronoEnding=True
                                            looping_path2shop=False
                                            ClearScreen()
                                            header2()
                                            print()
                                            print("While the Duchess types, you suddenly hear a loud wooshing noise... And a bullet pierces her right in the chest, knocking her down on the ground like a rag-doll.")
                                            print("Looks like that Chronosia officer wasn't kidding about his marksmanship skills.")
                                            print()
                                            input("Press Enter to continue.")
                                        else:
                                            ClearScreen()
                                            header2()
                                            print()
                                            print("It looks like you have figured out a way to lure the Duchess over to the terminal by the shuttered window... But for the Chronosia officer to have a decent shot at her from the nearby outpost rooftop, the window still needs to be opened.")
                                            print()
                                            print("The Duchess, confused by what caused the beeping on her monitor, squats back down onto her chair.")
                                            print()
                                            input("Press Enter to continue.")
                                    else:
                                        if path2shop_slider not in path2shop_items:
                                            ClearScreen()
                                            header2()
                                            print()
                                            print("It looks like you have figured out a way to get the Duchess to stand by the terminal near the opened window... Maybe you should head over to the Chronosia outpost - someone over there might know what to do with this information.")
                                            print()
                                            print("The Duchess, confused by what caused the beeping on her monitor, squats back down onto her chair.")
                                            print()
                                            input("Press Enter to continue.")
                                        else:
                                            ClearScreen()
                                            header2()
                                            print()
                                            print("The Duchess, confused by what caused the beeping on her monitor, squats back down onto her chair.")
                                            print()
                                            input("Press Enter to continue.")


                            if path2shop_slider.item_used_alone:
                                removeFromScene(path2shop_slider, path2shop_items)
                                removeFromScene(path2shop4, path2shop)
                                path2shop_window.descr="It's a large window, now wide open, that looks out onto the streets below. You think that you can see the Chronosia outpost in the distance through it. The terminal sits right beside it."
                                path2shop_window_use["self"]="You have already opened this window using the electronics box in this room - you don't need to do anything else with it."

                            if path2shop_artwork.item_used_with_otherItem:
                                path2shop_artwork.pick=True
                                path2shop_artwork_use["self"]="You could try to use the sphere while it's lying here on this floor... But you're probably better off using 'pick' and putting it in your inventory first."
                                path2shop_artwork.descr="It's the sphere that you rewired with your holotool - it can now detect traces of brightsteel in the area. You can 'use' it in a particular area to turn it on."
                                

                            if path2shop_artwork in inventory.inventory:
                                removeFromScene(path2shop3, path2shop)
                                addItemEverywhere(path2shop_artwork, path2location_items)
                                path2shop_artwork_use["self"]="You switch on the sensor on the makeshift sphere... There is no noise being emitted. You are certain there is no brightsteel in this area."
                        
                            # Trying to talk to the Duchess
                            if path2shop_woman.item_used_alone:

                                # Switch off to allow several discussions
                                path2shop_woman.item_used_alone=False

                                if exerCross==True:
                                    dialogueChoices(womanBasic)

                                # If you've permanently allied with Chronosia, you get a chance to double cross them
                                elif permChrono==True:
                                    initialHeader()
                                    print("How will you answer?")
                                    print("[1] 'Fine then... I'm leaving.'")
                                    print("[2] 'The leader of the Chronosia outpost has personally recruited me to assassinate you - I am willing to change sides, if you let me have one of those boxes that I know you have stashed in here.'")
                                    branchingLoopExerCross=True
                                    while branchingLoopExerCross:
                                        option=0
                                        try:
                                            option=int(input("Please select your dialogue option: "))  
                                        except ValueError:
                                            initialHeader()  
                                        if option==1 or option==2:
                                            break
                                        else:
                                            initialHeader()
                                            print("Sorry, you have to either select 1 or 2.")
                                            input("Please press Enter, then try again.")
                                    if option==2:
                                        exerCross=True
                                        path2shop_woman_use["self"]="You walk over to the woman. 'Well, then?' she asks. 'Is it time?'"
                                        path2tank_mine_use["lid"]="You place the mine on the blackened adamantium lid... It fizzles quitely and the surface of the material melts like butter, leading into a chasm below. The whole process is mercifully quiet - you don't think anyone in the outpost has noticed. You really need to be careful now - it's only a matter of time before the Exers find out that the way through is open. You better get out of here fast."
                                        ClearScreen()
                                        display(screenWomanCross)
                                        dialogueChoices(womanBasic)

                                # If you've permanently allied with Exers, this dialogue plays
                                elif permExers==True:
                                    dialogueChoices(womanBasic)

                                # Prompt decision for whether or not to join Chronosia
                                else:
                                    initialHeader()
                                    print("How will you answer?")
                                    print("[1] 'Yes, I'll help.'")
                                    print("[2] 'Give me some time to think about it... I'll be back later.'")
                                    branchingLoopExers=True
                                    while branchingLoopExers:
                                        option=0
                                        try:
                                            option=int(input("Please select your dialogue option: "))  
                                        except ValueError:
                                            initialHeader()  
                                        if option==1 or option==2:
                                            break
                                        else:
                                            initialHeader()
                                            print("Sorry, you have to either select 1 or 2.")
                                            input("Please press Enter, then try again.")
                                    if option==1:
                                        permExers=True
                                        addItemEverywhere(path2shop_card, path2location_items)

                                        path2outpost_leader_use["self"]="You decide to walk over to the man. He looks you up and down suspiciously,and mutters, 'And who in the hell are you supposed to be?' You hand him the identification card given to you by the Duchess. He looks at it... and is not impressed. 'Do you take me for an idiot, woman? This may have fooled poor Flynn outside, but I knew the woman who this belonged to personally. Now, I don't know who you are, but you better go on back to wherever it is that you came from."

                                        path2shop_woman_use["self"]="You walk over to the woman. 'Well, then?' she asks. 'Is it time?'"

                                        path2tank_mine_use["lid"]="You place the mine on the blackened adamantium lid... It fizzles quitely and the surface of the material melts like butter, leading into a chasm below. The whole process is mercifully quiet - you don't think anyone in the outpost has noticed. You really need to be careful now - it's only a matter of time before the Exers find out that the way through is open. You better get out of here fast."

                                        path2shop_woman_use["self"]="You walk over to the woman. 'Well, then?' she asks. 'Is it time?'"
                                        
                                        ClearScreen()
                                        display(screenWomanJoin)
                                        dialogueChoices(womanBasic)
                                    elif option==2:
                                        ClearScreen()
                                        display(screenWomanThink)

                            if looping_path2shop==True:
                                # Regular gameplay
                                puzzleNavigation(path2shop, path2shop_items)

                # Entering the outpost from the alley door
                elif path2alley_door.item_used_alone:
                    
                    # Switching on looping for the outpost room
                    looping_path2outpost=True

                    # Closing the door behind us
                    path2alley_door.item_used_alone=False

                    while looping_path2outpost:

                        # If using door outside, quit looping
                        if path2outpost_door.item_used_alone:
                            looping_path2outpost=False
                        else:

                            if path2outpost_officer.item_used_alone:
                                path2outpost_officer.item_used_alone=False
                                if permChrono or chronoCross:
                                    talkedToSniper=True

                            if path2outpost_lid.item_used_with_otherItem:
                                path2outpost_lid.item_used_with_otherItem=False
                                if permExers or exerCross:
                                    exerEnding=True
                                    looping_path2outpost=False

                            if path2outpost_desk.item_used_alone:
                                path2outpost_desk.item_used_alone=False
                                ClearScreen()
                                header2()
                                print()
                                outpost_pw=str(input("Please type in your password: "))
                                if outpost_pw=="2114":

                                    removeFromScene(path2outpost4, path2outpost)
                                    addToScene(path2outpost9, path2outpost)
                                    addToScene(path2outpost_lid, path2outpost_items)

                                    print()
                                    print("The screen reads: 'Long live the year of rebirth... All praise the Duchess!'")
                                    print("'The path to your fellow comrades is now open - proceed with glory!'")
                                    print()
                                    print("There's a slight click in the floor beside you and one of the tiles slides open. You can see a lid that seems to lead underground... but you can't get it open.")
                                    print()
                                    print("None of this makes sense... Based on the output of the computer, it looks like that this passageway leads to another Exer base of some kind. Why is this here? And how did this gang manage to build it under the noses of the Chronosia operatives? Not even the Shogunate have such deep-seeded espionage capabilities.")
                                    print()
                                    print("If you open this lid, you are certain that the gang members on the other side will overrun and slaughter everything in this outpost.")

                                    input("Press Enter to continue.")
                                else:
                                    print()
                                    print("Sorry, password is incorrect. Please try again later.")
                                    input("Press Enter to continue.")

                            if path2outpost_shelf.item_used_alone:
                                addItemEverywhere(path2outpost_hololog1, path2location_items)
                                addItemEverywhere(path2outpost_hololog2, path2location_items)
                                addItemEverywhere(path2outpost_hololog3, path2location_items)
                                removeFromScene(path2outpost5, path2outpost)

                            if path2outpost_leader.item_used_with_otherItem and permExers:
                                path2outpost_leader.item_used_with_otherItem=False
                                initialHeader()
                                print("How will you answer?")
                                print("[1] 'Fine then... I'm leaving.'")
                                print("[2] 'The Exers have personally recruited me to assassinate the prople in this station - I am willing to change sides, if you let me have one of those boxes that I know you have stashed in here.'")
                                branchingLoopChronoCross=True
                                while branchingLoopChronoCross:
                                    option=0
                                    try:
                                        option=int(input("Please select your dialogue option: "))  
                                    except ValueError:
                                        initialHeader()  
                                    if option==1 or option==2:
                                        break
                                    else:
                                        initialHeader()
                                        print("Sorry, you have to either select 1 or 2.")
                                        input("Please press Enter, then try again.")
                                if option==2:
                                    chronoCross=True
                                    path2outpost_leader_use["self"]="You walk over to the man. 'Yes, yes,' he says, 'is it done? Is the Duchess dead? Or have you come to ask more questions?'"
                                    path2outpost_officer_use["self"]="The man doesn't take his eyes off the scope of the sniper rifle as you approach him. Before you have the chance to say anything, he starts to speak, in a voice that's a little more high-pitched than you imagined... 'Ah,' he says, 'little bird tells me you're working for us now. Well, let me tell you what's going on here. You're probably aware that the leader of that disgusting slime in the streets is hiding like a coward over in that shop yonder. I've used my infared scope to check, and it seems to be that her quarters are right behind that big window. Now, I'm no slouch with a rifle, as you can probably tell... but I'm not magic. To kill the Duchess, we need to do two things. First, you're going to need to find a way to open that big window - but that's just the first part. You're also going to need to lure the Duchess over to the window somehow. I'm keeping an eye at the shop at all times, so no need to call me or nothing - once the Duchess is at the open window... this here rifle is putting a hole right inside her sorry little head.'"
                                    ClearScreen()
                                    display(screenLeaderCross)
                                    dialogueChoices(leaderBasic)

                            # Trying to talk to the leader
                            if path2outpost_leader.item_used_alone:

                                # Switch off to allow several discussions
                                path2outpost_leader.item_used_alone=False

                                if chronoCross==True:
                                    dialogueChoices(leaderBasic)

                                # If you've permanently allied with Exers, you get a chance to double cross them
                                elif permExers==True:
                                    initialHeader()
                                    print("How will you answer?")
                                    print("[1] 'Fine then... I'm leaving.'")
                                    print("[2] 'The Exers have personally recruited me to assassinate the prople in this station - I am willing to change sides, if you let me have one of those boxes that I know you have stashed in here.'")
                                    branchingLoopChronoCross=True
                                    while branchingLoopChronoCross:
                                        option=0
                                        try:
                                            option=int(input("Please select your dialogue option: "))  
                                        except ValueError:
                                            initialHeader()  
                                        if option==1 or option==2:
                                            break
                                        else:
                                            initialHeader()
                                            print("Sorry, you have to either select 1 or 2.")
                                            input("Please press Enter, then try again.")
                                    if option==2:
                                        chronoCross=True
                                        path2outpost_leader_use["self"]="You walk over to the man. 'Yes, yes,' he says, 'is it done? Is the Duchess dead? Or have you come to ask more questions?'"
                                        path2outpost_officer_use["self"]="The man doesn't take his eyes off the scope of the sniper rifle as you approach him. Before you have the chance to say anything, he starts to speak, in a voice that's a little more high-pitched than you imagined... 'Ah,' he says, 'little bird tells me you're working for us now. Well, let me give you the low down. You're probably aware that the leader of that disgusting slime in the streets is hiding like a coward over in that shop yonder. I've used my infared scope to check, and it seems to be that her quarters are right behind that big window. Now, I'm no slouch with a rifle, as you can probably tell... but I'm not magic. To kill the Duchess, we need to do two things. First, you're going to need to find a way to open that big window - but that's just the first part. You're also going to need to lure the Duchess over to the window somehow. I'm keeping an eye at the shop at all times, so no need to call me or nothing - once the Duchess is at the open window... this here rifle is putting a hole right inside her sorry little head.'"

                                        ClearScreen()
                                        display(screenLeaderCross)
                                        dialogueChoices(leaderBasic)


                                # If you've permanently allied with Chronosia, this dialogue plays
                                elif permChrono==True:
                                    dialogueChoices(leaderBasic)


                                # Prompt decision for whether or not to join Chronosia
                                else:
                                    initialHeader()
                                    print("How will you answer?")
                                    print("[1] 'Yes, I'll help.'")
                                    print("[2] 'Give me some time to think about it... I'll be back later.'")
                                    branchingLoopChrono=True
                                    while branchingLoopChrono:
                                        option=0
                                        try:
                                            option=int(input("Please select your dialogue option: "))  
                                        except ValueError:
                                            initialHeader()  
                                        if option==1 or option==2:
                                            break
                                        else:
                                            initialHeader()
                                            print("Sorry, you have to either select 1 or 2.")
                                            input("Please press Enter, then try again.")
                                    if option==1:
                                        permChrono=True
                                        path2outpost_leader_use["self"]="You walk over to the man. 'Yes, yes,' he says, 'is it done? Is the Duchess dead? Or have you come to ask more questions?'"
                                        path2shop_woman_use["self"]="You walk up as close to the glass as possible. The woman looks at you - you can't tell the expression behind those dead, gas-mask eyes, but her  posture is one of menace. 'And who are you supposed to be?' she asks, the voice muffled through the mask's air filters. 'Ahh... that cross on your forehead. Hmm... I know all my subjects, but I don't know you. Any person that tries to pose as one of my subjects cannot be trusted - get out of my sight.'"
                                        path2street_man_use["self"]="You approach the man - he takes a brief look at the carved cross on your forehead with those dead, insect eyes, shrugs, and opens the door for you. That was easier than you expected - maybe you should have carved that cross on your forehead yourself and saved yourself some time. The man disappears indoors before you - it looks like you're not going to have a problem getting in and out of here anymore."
                                        path2tank_finger_use["man"]="You approach the man, but before you can even hand him the sever finger, he takes a brief look at the carved cross on your forehead with those dead, insect eyes, shrugs, and opens the door for you. That was easier than you expected - maybe you should have carved that cross on your forehead yourself and saved yourself some time. The man disappears indoors before you - it looks like you're not going to have a problem getting in and out of here anymore."
                                        path2outpost_officer_use["self"]="The man doesn't take his eyes off the scope of the sniper rifle as you approach him. Before you have the chance to say anything, he starts to speak, in a voice that's a little more high-pitched than you imagined... 'Ah,' he says, 'little bird tells me you're working for us now. Well, let me give you the low down. You're probably aware that the leader of that disgusting slime in the streets is hiding like a coward over in that shop yonder. I've used my infared scope to check, and it seems to be that her quarters are right behind that big window. Now, I'm no slouch with a rifle, as you can probably tell... but I'm not magic. To kill the Duchess, we need to do two things. First, you're going to need to find a way to open that big window - but that's just the first part. You're also going to need to lure the Duchess over to the window somehow. I'm keeping an eye at the shop at all times, so no need to call me or nothing - once the Duchess is at the open window... this here rifle is putting a hole right inside her sorry little head.'"

                                        ClearScreen()
                                        display(screenLeaderJoin)
                                        dialogueChoices(leaderCore)
                                    elif option==2:
                                        ClearScreen()
                                        display(screenLeaderThink)

                            if looping_path2outpost:
                                # Regular gameplay
                                puzzleNavigation(path2outpost, path2outpost_items)

                elif exerEnding:
                    exerEnding=False
                    looping_path2=False
                    ClearScreen()
                    screensInRange(totalScreenList, 75, 80)

                elif chronoEnding:
                    chronoEnding=False
                    looping_path2=False
                    ClearScreen()
                    screensInRange(totalScreenList, 82, 100)

        screensInRange(totalScreenList, 102, 108)
        

    ClearScreen()
    initialHeader()
    print()
    print("You need to type in the correct password and defuse the bomb...")
    passwordAttempt=str(input("Enter the password: "))

    if passwordAttempt=="w62u":
        playingabranchingpath=False
        break
    elif passwordAttempt!="w62u":
        ClearScreen()
        screensInRange(totalScreenList, 110, 121)

ClearScreen()
screensInRange(totalScreenList, 123, 137)
outro()
screensInRange(totalScreenList, 138, 139)
quit()