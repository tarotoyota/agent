from dataclasses import dataclass, field
from typing import List, ClassVar
import state_inst

###########################################################################################################



###########################################################################################################
univ_modifier_job=["You're better than~", "You're as good as~", "You can be a~", "You can be the next~", "Top class~"]


@dataclass
class Grade:
  ALL_GRADE: ClassVar[List['Grade']] = []
  grade_name:str
  grade_genre:str
  grade_s:list # High grade.  Requires proper noun for person or group or award.
  grade_s_name:list
  grade_i:list # Low grade.  Requires proper noun for person or group or award.
  grade_i_name:list

  modifier:list
  def __post_init__(self):
      Grade.ALL_GRADE.append(self)
      if self.grade_genre == "job":
            self.modifier += univ_modifier_job


grade_singer            =Grade("singer"             ,"job",["singer"]                       ,["Beyonce"]            ,["idol", "rapper", "voice actor"],["Aquatimez", "Orange range", "Britney Spears"],[])
grade_classical_musician=Grade("classical musician" ,"job",["pianist", "violinist"]         ,["Bach"]               ,["cymbalist", "triangle player"] ,[],[])
grade_rock_musician     =Grade("rock musician"      ,"job",["guitarist", "vocal"]           ,["Beatles"]            ,["bassist"],[],[])
grade_comedian          =Grade("comedian"           ,"job",["comedian"]                     ,["Hitoshi Matsumoto"],["Vtuber", "idol", "tv talent", "voice actor", "clown"],["Tsuyoshi Muro"],[])
grade_novelist          =Grade("novelist"           ,"job",["novelist"]                     ,["the Nobel Prize in Literature", "J.K. Rowling"],["Narou novelist", "tabloid writer"],["Hiro Mizushima"],[])
grade_artist            =Grade("artist"             ,"job",["artist"]                       ,["Picasso", "Turner Prize"],["contemporary artist", "Hentai manga artist"],["Toru Mitsumune"], [])
grade_doctor            =Grade("doctor"             ,"job",["neurosurgeon", "cardiologist"] ,[]                     ,["dermatologist", "internal medicine doctor", "nurse"],[],[])
grade_researcher        =Grade("researcher"         ,"job",["mathematician"]                ,["Albert Einstein"]    ,["gender studies researcher"],["Chizuruko Ueno"], [])
grade_actor             =Grade("actor"              ,"job",["Hollywood star"]               ,["Academy Award", "Gary Oldman"],["TV drama actor", "Porn actor", "ASMR actor", "Karaoke background video actor"],["Stallone"], [])
grade_chef              =Grade("chef"               ,"job",["French chef"]                  ,["Michelin restaurant", "Imperial Hotel", "Gordon Ramsay"],["Fast food restaurant employee"]               ,["McDonalds", "Jiro inspires", "Kitchen of Karaoke", "Kitchen of hotpillow hotel"], [])
grade_athlete           =Grade("athlete"            ,"job",["baseball player"]              ,["Kyojin player"]      ,["Billiards player"],["DeNA player"],["Top class", "First team"])
grade_psycho_criminal   =Grade("psycho criminal"    ,"job",["murder", "terrorist"]          ,["Jeffrey Dahmer"]     ,["groper", "voyeurist"]                    ,["Jared Fogle"]        ,["Repeat offender"])
grade_progamer          =Grade("progamer"           ,"job",["pro gamer"]                    ,["Umehara"]            ,["medal game player", "water game player"] ,[]                     ,[])
grade_gambler           =Grade("gambler"            ,"job",["gambler"]                      ,[""]                   ,["medal game player", "lottery addicted"]  ,[]                     ,[])
grade_university        =Grade("university"         ,"job",["national University"]          ,["Tokyo Univ."]        ,["Private University"]                     ,["Tokyo MODE Gakuen"]  ,["A grade", "passed for active duty"])
grade_teacher           =Grade("teacher"            ,"job",["university professor"]         ,["Harvard", "MIT"]     ,["cram school teacher", "kindergarten teacher", "sewing class teacher"], ["Kumon"], ["Tenured"])
grade_craftsman         =Grade("craftsman"          ,"job",["potter", "blacksmith"]         ,["National Living Treasure"], ["fleshlight designer"], [], ["Highly skilled", "Renowned"])
grade_idol              =Grade("idol"               ,"job",["Akimoto's idol", "Johnny's idol"],["AKB48", "Arashi"]    ,["local idol", "underground idol", "image video idol"], ["Kamen Joshi"], ["Center position", "Ace"])


# Define grade_idol instance in English without any explanation. Start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

'''
grade_car             =Grade("car"              ,"",["Classic Cars", "4WD"],["57T Tourer", "Lamborghini"],["Light vehicle", " compact car"],["Nbox", "Prius"],["fully custom", "restored (year) type"])
grade_show_location   =Grade("show location"    ,"",["Dome", "Hall"],["Shibuya Kokaido"],["Community center", "Rental conference room", "Fast food restaurant", "Parking lot"],["Toshima Ward Community Center", "Chichibu Rental Conference Room", "McDonald's Takasaki No. 2 Store Parking Lot"],[])
grade_female_celebrity=Grade("Female celebrities whose Bob attends Ali","",["Idol", "Actress"],["Nogizaka 46"],["Female comedian"],["Ayaman Japan"],["Ex ~", "The most popular girl in ~", "Someone from ~"])
'''

###########################################################################################################
@dataclass
class Effort:
  ALL_EFFORT: ClassVar[List['Effort']] = []
  effort:list # Stereotypical effort in reality or fiction.
  def __post_init__(self):
      Effort.ALL_EFFORT.append(self)
      if self.effort:
          self.effort.append(["Seeking advice.", "Conflicts with others about the way one do things.", "Sacrificing family, friend and lover.", "Becoming estranged from a partner.", "Becoming ill and getting injured from overwork.", "Quitting college or work to pursue the dream.", "Selling personal belongings for Activity funds"])

univ_effort_creator=["Traveling for inspiration", "Abstinence", "Sublimating one's trauma into a work of art", "Use LSD", "Meditation", "Keeping a dream journal"]

effort_singer               =Effort([univ_effort_creator, "Quit smoking"])
effort_instrumentalist      =Effort([univ_effort_creator, "Quit smoking"])
effort_comedian             =Effort(["Abstinence", "People-watching"])
effort_writer               =Effort([univ_effort_creator])
effort_artist               =Effort([univ_effort_creator, "Creating art in the dark"])
effort_doctor               =Effort(["Abstinence", "Use nootropics"])
effort_researcher           =Effort([univ_effort_creator])
effort_actor                =Effort([univ_effort_creator, "Method acting", "Physical transformation for roles", "Taking specialized classes (e.g., dance, martial arts)", "Performing own stunts","Extensive research for historical roles", "Learning new languages for international productions", "Undergoing extreme weight changes","Continues to play the role in his private life."])
effort_chef                 =Effort([])
effort_examinee             =Effort(["Use nootropics", "Study all night", "Making flashcards", "Memorizing"])
effort_athlete              =Effort(["Intense physical training", "Strict diet regimen", "Ice baths for recovery", "Altitude training", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"])
effort_progamer             =Effort(["Intense physical training", "Strict diet regimen", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"])
effort_gambler              =Effort(["Learning math", "Creating and checking statistical data"])
effort_teacher              =Effort(["Creating engaging lesson plans", "Mentoring students outside of class hours", "Pursuing advanced degrees", "physical punishment"])
effort_craftsman            =Effort(["Practicing techniques for hours daily", "Studying traditional methods", "Experimenting with new materials", "Apprenticeship under a master", "Perfecting a single skill for years", "Attending specialized workshops"])

# Define effort_craftsman in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



# Add new itmes in effort_actor instance in English without any explanation. start answer with ```python. I will run your reply through the eval function, so don't write anything unnecessary.



# Add new itmes in each instance in English without any explanation. start answer with ```python.
###########################################################################################################
@dataclass
class Suffer:
  ALL_SUFFER: ClassVar[List['Suffer']] = []
  suffer:list # Stereotypical suffer in reality or fiction.
  def __post_init__(self):
    Suffer.ALL_SUFFER.append(self)
    if self.suffer:
        self.suffer.append(["slump", "Children's school fees", "Loans for activities"])

univ_suffer_creator=["A lack of depth that comes from a lack of life experience.","Emotionless","Become a victim of plagiarism", "Conflict with producers", "Commercialism", "Creator's block", "Drug addiction", "alcohol addiction", "sex addiction", "Cannot surpass one's rival", "Cannot surpass one's past self", "Paparazzi", "Stalkers"]
l_suffer_script = ["Lacking hints","Lacking a clear message","Poor character development","Weak plot structure","Unrealistic dialogue","Lack of conflict","Cliché or predictable storylines","Poor world-building","Underdeveloped themes","Weak endings"]
l_suffer_game   = ["Luck-based", "Unbalanced ","Lack of content updates","Limited customization options","Pay-to-win elements or microtransactions","Lack of endgame content","Repetitive gameplay","Poor UI design","Lack of player agency","Buggy or glitchy performance","Limited replay value","Inconsistent difficulty levels","Weak or unengaging narrative"]

# Extend 10 new items in l_suffer_game in English. I will run your reply through the eval function, so don't write anything unnecessary.

suffer_singer               =Suffer([univ_suffer_creator, "Lack of stage presence","Lack of versatility","The song arrangements are lacking", "Uninspired Lyrics", "Repetitive Melodies"])
suffer_instrumentalist      =Suffer([univ_suffer_creator, "Emotionless","lacking a clear message","Inability to play in different styles","Poor improvisation skills","Lack of stage presence","Inability to tune instrument properly"])
suffer_comedian             =Suffer([univ_suffer_creator])
suffer_actor                =Suffer([univ_suffer_creator, "Physical injuries from stunts", "Pressure to maintain a certain physical appearance","The damage caused by method acting", "Unconvincing Performances", "Difficulty with Accents/Dialects","Overacts","lack of stage presence","Lack of character depth","Inability to improvise","Lack of chemistry with co-stars", l_suffer_script])

suffer_writer               =Suffer([univ_suffer_creator, "Deadline", l_suffer_script])
suffer_artist               =Suffer([univ_suffer_creator, "Emotionless","lack of creativity","unoriginal style","lack of craftsmanship", "Struggles with Proportions"  ,  "Weak anatomy knowledge"])
suffer_doctor               =Suffer(["The trauma of not being able to save a patient's life."])
suffer_researcher           =Suffer(["Plagiarism", "Not being able to get research funding", "Has white hair"])
suffer_progamer             =Suffer([l_suffer_game, "Repetitive Strain Injury", "Carpal Tunnel Syndrome", "Eye strain",   "Addiction to gaming"])
suffer_teacher              =Suffer(["punk", "Pressure from parents and administration",  "Lack of autonomy in curriculum decisions", "Testing pressure", "Large class sizes", "bullying"])
suffer_craftsman = Suffer(["Repetitive strain injuries", "Lack of successors", "Exposure to harmful materials", "Competition from mass-produced items", "Difficulty in finding apprentices", "Financial instability", "Long hours of solitary work", "burnout", "Struggles with modernization and technology"])


# Define suffer_craftsman in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.




suffer_chef                 =Suffer([])
suffer_examinee             =Suffer(["Exam pressure","Health issues due to long study hours","Intense competition","Balancing study and personal life","Fear that one failure will affect future","Pressure from parents and teachers","Self-loathing and loss of confidence","Deterioration of relationships with friends"])
suffer_athlete              =Suffer(["Career-ending injuries","Pressure from fans and media", "Doping scandals", "Burnout", "Post-retirement depression", "Eating disorders", "Chronic pain", "Concussions and long-term brain damage", "Stalker"])

suffer_gambler = Suffer(["Addiction to gambling", "Financial ruin", "Depression and anxiety", "Lying to cover losses", "Chasing losses", "Neglecting work or family responsibilities", "Legal troubles", "Substance abuse as a coping mechanism", "Suicidal thoughts"])






###########################################################################################################
@dataclass
class StereoAction:
  ALL_STEREOACTION: ClassVar[List['StereoAction']] = []
  stereoaction:list # Stereotypical action in reality or fiction.
  def __post_init__(self):
    StereoAction.ALL_STEREOACTION.append(self)

univ_stereoaction_creator=["Support the American Democratic Party.", "Being interested in environmental issues.", "Getting involved in the Scientology or SGI", "Being atheist or non-religious.", "Expressing support or opposition to abortion."]

stereoaction_singer                 =StereoAction([univ_stereoaction_creator, "Has suicidal thoughts"])
stereoaction_instrumentalist        =StereoAction([univ_stereoaction_creator, "Suddenly starts writing music on paper."])
stereoaction_classical_musician     =StereoAction([univ_stereoaction_creator, "Suddenly starts writing music on paper."])
stereoaction_rock_musician          =StereoAction([univ_stereoaction_creator, "Suddenly starts writing music on paper.", "Being an alcoholic", "Addicting drug and sex"])
stereoaction_comedian               =StereoAction([univ_stereoaction_creator])
stereoaction_writer                 =StereoAction([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
stereoaction_artist                 =StereoAction([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
stereoaction_doctor                 =StereoAction([])
stereoaction_researcher             =StereoAction(["Starting a religion after overthinking it", "Suddenly starts writing mathematical formulas on the wall.", "Unable to understand others' feelings."])
stereoaction_actor                  =StereoAction([univ_stereoaction_creator, "Looking down on lighting engineers and cinematographers.""Constantly practicing lines in public","Name-dropping famous directors or actors","Insisting on being called by their character's name","Refusing to break character even off-set","Demanding specific brands of bottled water on set","Throwing tantrums when not given enough screen time","Obsessing over their appearance and plastic surgery",])
stereoaction_chef                   =StereoAction(["Getting angry at customers for using condiments", "Yelling at kitchen staff",  "Striving for Michelin stars", "Taking pride in sourcing ingredients locally", "Focus on seasonal ingredients", "Focus on pesticide-free ingredients"])
stereoaction_psycho_criminal        =StereoAction(["Talking to imaginary friends", "Collecting trophies from victims", "Writing manifestos", "Obsessively stalking targets", "Creating elaborate traps or puzzles", "Claim responsibility", "Leaving cryptic clues at crime scenes", "Sending taunting messages to police", "Developing a signature kill method", "Keeping detailed journals of crimes", "Ritualistic behavior before or after crimes", "Creating alter egos or personas"])
stereoaction_athlete                =StereoAction(["Getting involved in a cult", "Splurge", "Bullying nerds", "Support the Republican Party", "Trash Talk", "meathead", "Partying excessively","Constantly flexing muscles","Overusing sports metaphors in conversation","Ignoring injuries to keep playing","Developing superstitious pre-game rituals",])
stereoaction_gambler                =StereoAction(["Constantly checking scores or results", "Borrowing money from friends and family",  "Lying about whereabouts or activities", "Skipping work or important events to gamble", "Celebrating wins extravagantly", "Becoming irritable when unable to gamble", "Hiding betting slips or casino receipts", "Making increasingly risky bets", "Talking excessively about past wins", "Chasing losses with bigger bets", "Steal money"])
stereoaction_progamer               =StereoAction(["Trash talking opponents", "Celebrating wins excessively", "Skipping meals to practice", "Neglecting personal hygiene", "Becoming irritable when unable to play", "Bragging about ranking or skills", "Forming rivalries with other players", "Rage quitting", "Streaming for hours", "Using gaming slang in everyday conversation"])
stereoaction_teacher                =StereoAction(["Constantly correcting others' grammar", "Carrying a red pen everywhere", "Assigning homework on weekends and holidays","Favoring certain students", "Talking in a condescending tone", "Struggling with technology in the classroom", "Drinking excessive amounts of coffee"])
stereoaction_craftsman = StereoAction(["Obsessing over tool organization", "Refusing to use modern technology", "Criticizing mass-produced items", "Wearing traditional work attire", "Collecting rare or antique tools", "Talking extensively about material quality", "Insisting on doing everything by hand", "Becoming irritated when rushed", "Hoarding materials and supplies", "Giving unsolicited advice on craftsmanship", "Throw the failed piece onto the floor."])

# Add new itmes in stereoaction_craftsman instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


# Define stereoaction_teacher in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.





# Define stereoaction_actor in English and out put only that instance. without any explanation. start answer with ```python.



# Add new itmes in each instance in English without any explanation. start answer with ```python.

###########################################################################################################

@dataclass
class StereoAppear:
  ALL_STEREOAPPEAR: ClassVar[List['StereoAppear']] = []
  stereoappear:list # Stereotypical appearance in reality or fiction.
  def __post_init__(self):
    StereoAppear.ALL_STEREOAPPEAR.append(self)

stereoappear_singer                 =StereoAppear(["Many piercings", "Many tattoos", "Colorful hair"])
stereoappear_classical_musician     =StereoAppear(["Formal black attire","Bow tie","Slicked-back hair","Round glasses","Pale complexion","Thin frame"])
stereoappear_rock_musician          =StereoAppear(["Many piercings", "Many tattoos", "Colorful hair"])
stereoappear_comedian               =StereoAppear([])
stereoappear_writer                 =StereoAppear(["Wears a samue", "Has a beard", "Thin and pale", "Has messy hair"])
stereoappear_artist                 =StereoAppear(["Many piercings", "Many tattoos", "Colorful hair"])
stereoappear_doctor                 =StereoAppear(["White coat", "Messy hair"])
stereoappear_researcher             =StereoAppear(["White coat", "Messy hair", "Has bags under one's eyes", "Carries around a clipboard", "using a wheelchair"])
stereoappear_actor                  =StereoAppear([])
stereoappear_chef                   =StereoAppear(["Kaiser moustache", "Being fat", "Wears a neckerchief", "Has a thick accent"])
stereoappear_psycho_criminal        =StereoAppear(["Unkempt appearance", "Wild eyes", "Scars or burn marks", "Twitchy movements", "Wears all black", "Clown-like makeup", "Disheveled hair", "Pale skin", "Bloodstained clothing", "Ritualistic tattoos", "Leather gloves", "Creepy mask"])
stereoappear_athlete                =StereoAppear(["Muscular build", "Athletic wear", "Sweatbands", "Sports gear", "Taped joints or limbs", "Shaved body", "Visible tan lines", "Team jersey or uniform", "Dreadlocks"])
stereoappear_gambler                =StereoAppear(["Disheveled appearance", "Dark circles under eyes", "Nervous twitches", "Flashy jewelry", "Expensive watch", "Rumpled suit", "Cigarette in hand", "Fidgeting with chips or cards", "Sunglasses indoors", "Sweaty brow", "Loosened tie", "Rolled-up sleeves", "Has a red pencil on his ear."])
stereoappear_progamer               =StereoAppear(["Headset", "Gaming chair", "Energy drinks", "Junk food", "Eyeglasses", "Acne", "Poor posture", "Headaches", "Back pain", "Wrist pain", "Messy hair", "Dark circles under eyes", "Skinny build", "Multiple monitors", "RGB lighting", "Wrist brace"])
stereoappear_teacher                =StereoAppear(["Glasses", "Cardigan sweater", "Sensible shoes", "Messy bun or ponytail", "Lanyard with ID badge", "Tote bag full of papers", "Elbow patches on jacket", "Chalk dust on clothes", "Coffee stains", "Comfortable, modest clothing", "Practical hairstyle", "Minimal makeup", "Wristwatch", "Reading glasses on a chain", "Colorful, quirky accessories"])
stereoappear_craftsman = StereoAppear(["Leather apron", "Calloused hands", "Rolled-up sleeves", "Safety goggles", "Work boots", "Tool belt", "Weathered skin", "Muscular forearms", "Sawdust or wood shavings on clothes", "Protective gloves", "Bandana or cap", "Rugged, worn clothing", "Pencil behind ear", "Measuring tape clipped to belt", "Beard or mustache"])


# Define stereoappear_craftsman in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.




# Add new itmes in stereoaciton_classical_musician instance in English without any explanation. start answer with ```python.


# Add new itmes in each instance in English without any explanation. start answer with ```python.

###########################################################################################################

@dataclass
class Press:
  ALL_PRESS: ClassVar[List['Press']] = []
  press:list # stereotypical emergency situations in which a person of that attribute plays an active role
  def __post_init__(self):
    Press.ALL_PRESS.append(self)

press_singer                =Press(["Sudden vacancy"])
press_instrumentalist       =Press(["Sudden vacancy"])
press_comedian              =Press(["Sudden vacancy"])
press_writer                =Press(["Sudden vacancy", "Ghost writer"])
press_artist                =Press([])
press_doctor                =Press(["Suddenly ill"])
press_researcher            =Press(["Bomb Defusal", "Death Game", "Zombie Pandemic"])
press_actor                 =Press(["Sudden vacancy"])
press_chef                  =Press(["Sudden vacancy"])
press_old                   =Press(["An old potter is urgently looking for a successor.", "A middle-aged person is urgently looking for a marriage partner."])
press_athlete               =Press(["Suddeen vacancy", "Death Game","Zombie Pandemic","Life saving scene"])
press_unhappy               =Press(["Ali guards a spiritual hot spot.", "Ali manufactures spiritual goods.","Ali sells spiritual goods door-to-door.", "Ali offers fortune telling.", "Ali lives near a spiritual hot spot."])
press_unhealthy             =Press(["Ali sales alternative medicine."])
press_illiteracy            =Press(["Ali sales nootropics."])
press_fat                   =Press(["A middle-aged person is urgently looking for a marriage partner."])
press_pedophilia            =Press(["Ali is job interviewed by a pediatric clinic."])
press_criminal              =Press(["Ali is job interviewed by a terrorists group."])
press_gambler               =Press(["death game", "underground casino tournament"])
press_progamer              =Press(["Sudden vacancy"])
press_teacher               =Press([])


# Add new items in press_craftsman in English without any explanation. start answer with ```python. I will run your reply through the eval function, so don't write anything unnecessary.

# Define press_gambler in English without any explanation. start answer with ```python. I will run your reply through the eval function, so don't write anything unnecessary.

###########################################################################################################

@dataclass
class Term:
    term:list # Terms that would be fulsome or posey if used by someone who is extremely bad at the job.

term_chef = Term(["season", "presentation", "appetizer", "main dish", "garnish", "emulsify"]) # If someone who only heats up TV dinners were to use this word as if they were a chef, that would be posey.
term_script = Term(["plot", "foreshadowing", "character arc", "subplot", "climax", "denouement", "exposition", "motif", "protagonist", "antagonist", "narrative", "dialogue", "theme", "flashback"])
term_athlete = Term(["tactics","endurance", "agility", "strategy", "conditioning", "aerobic", "anaerobic", "interval training", "cross-training", "recovery", "plyometrics", "core strength", "periodization", "technique"])
term_researcher = Term(["hypothesis", "methodology", "literature review", "data analysis", "peer review", "experimental design", "control group", "variable", "replication", "statistical significance", "qualitative research", "quantitative research", "citation", "abstract"])
term_actor = Term(["monologue", "improvisation", "character development", "stage presence", "blocking", "method acting", "scene study", "cold reading", "audition", "script analysis", "cue", "subtext", "emotional range", "projection"])
term_singer = Term(["vibrato", "falsetto", "pitch", "harmony", "breathing technique", "belting", "dynamics", "vocal range", "intonation", "resonance", "phrasing", "melisma", "head voice", "chest voice"])
term_instrumentalist = Term(["arpeggio", "legato", "staccato", "tremolo", "crescendo", "decrescendo", "octave", "pizzicato", "fingering", "bowing technique", "articulation", "tuning", "intonation", "sight-reading"])
term_gambler = Term(["bluff", "ante", "flop", "turn", "river", "pot odds", "bankroll", "tell", "all-in", "buy-in", "fold", "raise", "check", "dealer"])
term_progamer = Term([])
term_teacher = Term([])
term_craftsman = Term(["patina", "joinery", "dovetail", "inlay", "burnishing", "temper", "annealing", "forging", "casting", "glazing"])
# Add new 10 words in term_gambler and  term_actor in English, not Japanese. Start answer with ```python



###########################################################################################################

# Define b2scene_craftsman in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

# 'b2scene' means stereotypical conflict scenes. Each item should end with "is annoyed by Ali."
# for i in all_b2scene:
#  print(script : {i} Then Ali actually shows him her performance or achievements and tries to get him to acknowledge her.)

b2scene_univ = ["Ali's mind and body are exhausted from overwork. Ali's family is annoyed by Ali.", "Ali keeps asking his team member for advice. The team member is annoyed by Ali.", "Ali criticizes his team member for not being enthusiastic. The team member is annoyed by Ali.", "Ali, a unsuccessful poor, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.", "Ali, a unsuccessful poor, sticks to his career. Ali's wife is annoyed by Ali."]
b2scene_chef                = ["Ali trains cooks hard. The cook is annoyed by Ali.","Ali scolds a customer who asks for condiments. The customer is annoyed by Ali.","Ali urges the owner-chef who fired him to reconsider. The owner-chef is annoyed by Ali.","Ali changes the menu without consulting the restaurant manager. The manager is annoyed by Ali.","Ali insists on using expensive, out-of-season ingredients. The restaurant owner is annoyed by Ali."]
b2scene_actor               = ["After failing an audition, Ali goes to the director's house. The director is annoyed by Ali.","Ali's body and mind are exhausted through method acting. Ali's family is annoyed by Ali.","Ali is vocal with the director about the script and acting. The director is annoyed by Ali.","Ali constantly interrupts the rehearsal with his suggestions. The lead actor is annoyed by Ali.","Ali insists on multiple retakes for a minor scene. The crew is annoyed by Ali.","Ali stages a one-man protest outside a theater that rejected him. The theater owner is annoyed by Ali."]
b2scene_athlete             = ["After being dropped from the regular lineup, Ali goes to the manager's house and urges him to reconsider. The manager is annoyed by Ali.","Ali's body and mind are exhausted through over training. Ali's family is annoyed by Ali.","Ali, a poor athlete, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.","Ali, convinced he's the next big sports star, starts acting cocky and arrogant towards his teammates. The team is annoyed by Ali. ","Ali, a trainer, trains his teammates hard. The teammates is annoyed by Ali.","Ali, a renowned athlete, refuses to endorse a sponsor's product. The sponsor is annoyed by Ali. ","Ali's gambling addiction leads to financial problems and missed practices. The team captain is annoyed by Ali.","Ali's rivalry with a player from another team escalates into a physical altercation. The league commissioner is annoyed by Ali.","Ali shows up uninvited to a rival team's practice session to challenge their star player. The rival coach is annoyed by Ali.","Ali, a chef, refuses to accommodate a gourmet's detailed orders. The gourmet is annoyed by Ali. ","Ali, a chef, constantly makes changes to the menu without consulting the owner. The owner is annoyed by Ali."]
b2scene_novelist            = ["Ali's perfectionism is causing him to miss deadlines. The editor is annoyed by Ali.","Ali's body and mind are exhausted through over working. Ali's family is annoyed by Ali.","Ali, a successful novelist, refuses to make revisions requested by his editor. The editor is annoyed by Ali.","Ali, a novelist, constantly changes the plot of his book, frustrating his agent. The agent is annoyed by Ali..","Ali's plagiarism accusations against a fellow writer are causing a stir in the literary community. The literary agent is annoyed by Ali.","Ali's refusal to compromise on his artistic vision is hindering the book's commercial success. The publisher is annoyed by Ali.","Ali's public criticism of the judges' decision in a literary award is damaging his reputation. The literary award committee is annoyed by Ali..","Ali insists on rewriting the entire manuscript just days before the printing deadline. The publishing house CEO is annoyed by Ali.","Ali starts a heated debate with a literary critic who gave his book a negative review at a literary festival. The festival organizer is annoyed by Ali."]
b2scene_doctor              = ["Ali is in despair due to the trauma of not being able to cure his patients. His (family, coworker) is annoyed by Ali."]
b2scene_classical_musician  = ["Ali insists on playing a piece in a different style than what the conductor requested. The conductor is annoyed by Ali.","Ali constantly interrupts rehearsals with his suggestions and modifications. The orchestra members are annoyed by Ali.","Ali refuses to participate in a promotional event for the orchestra, citing artistic integrity. The orchestra manager is annoyed by Ali.","Ali starts a public argument with a music critic who gave him a negative review after a concert. The concert organizer is annoyed by Ali.","Ali's rivalry with another musician leads to tension and conflict during performances. The concertmaster is annoyed by Ali."]
b2scene_rock_musician       = ["Ali insists on changing the setlist at the last minute without consulting the band. The band members are annoyed by Ali.","Ali's constant partying and late-night habits are affecting his performance. The band manager is annoyed by Ali.","Ali refuses to play a fan-favorite song during concerts, citing artistic reasons. The fans are annoyed by Ali.","Ali's destructive behavior on stage leads to damage to the venue. The venue owner is annoyed by Ali.","Ali's insistence on using outdated equipment causes technical issues during performances. The sound engineer is annoyed by Ali.","Ali publicly criticizes the band's record label, causing tension and potential legal issues. The record label executive is annoyed by Ali.","Ali's refusal to participate in promotional activities hinders the band's publicity efforts. The publicist is annoyed by Ali.","Ali's rivalry with a member of another band leads to a public altercation. The music festival organizer is annoyed by Ali.","Ali's unpredictable behavior and mood swings cause delays in recording sessions. The producer is annoyed by Ali."]
b2scene_singer              = ["Ali insists on singing songs in a different style than what the producer requested. The producer is annoyed by Ali.","Ali's constant vocal exercises at home are disturbing the neighbors. The neighbors are annoyed by Ali.","Ali refuses to perform a popular song during concerts, citing artistic reasons. The fans are annoyed by Ali.","Ali's late-night partying is affecting his voice and performance quality. The tour manager is annoyed by Ali.","Ali insists on making last-minute changes to the setlist during live performances. The band members are annoyed by Ali.","Ali's public feud with another singer is causing negative publicity. The record label executive is annoyed by Ali.","Ali's refusal to promote his new album on social media hinders its success. The marketing team is annoyed by Ali.","Ali's insistence on using a specific microphone that frequently malfunctions causes delays. The sound technician is annoyed by Ali.","Ali's unpredictable behavior during interviews creates awkward situations. The publicist is annoyed by Ali.","Ali's rivalry with another singer leads to tension and conflicts during collaborative projects. The collaboration manager is annoyed by Ali."]
b2scene_progamer            = ["Ali insists on using unconventional strategies during team matches. The team captain is annoyed by Ali.","Ali's constant trash-talking during streams is damaging the team's reputation. The team manager is annoyed by Ali.","Ali refuses to practice with the team, claiming he performs better solo. The coach is annoyed by Ali.","Ali's rage-quitting during an important tournament match costs the team a victory. The tournament organizer is annoyed by Ali.","Ali's addiction to gaming leads to neglect of his physical health and missed team meetings. The team doctor is annoyed by Ali.","Ali publicly criticizes the game developers for balance issues after a loss. The esports league commissioner is annoyed by Ali.","Ali's rivalry with a player from another team escalates into a real-life confrontation. The event security is annoyed by Ali.","Ali refuses to practice with the team, claiming he's already skilled enough. His teammates are annoyed by Ali.","Ali's overly competitive nature leads him to sabotage his teammates during scrimmages. His teammates are annoyed by Ali.",]
b2scene_teacher             = ["Ali insists on teaching the curriculum in his own unconventional way. The principal is annoyed by Ali.","Ali's constant changes to the lesson plan confuse the students. The students are annoyed by Ali.","Ali refuses to participate in standardized testing preparations, citing educational philosophy. The school board is annoyed by Ali.","Ali's insistence on assigning unconventional homework frustrates parents. The parents are annoyed by Ali.","Ali's insistence on grading students based on non-traditional criteria causes complaints. The school counselor is annoyed by Ali.","Ali's overly strict discipline methods lead to student protests. The student council is annoyed by Ali."]
b2scene_craftsman = ["Ali insists on using only traditional methods, slowing down production. The workshop manager is annoyed by Ali.", "Ali refuses to compromise on material quality, increasing costs. The client is annoyed by Ali.", "Ali takes too long perfecting details, missing deadlines. The project coordinator is annoyed by Ali.", "Ali criticizes mass-produced items in front of potential buyers. The sales representative is annoyed by Ali.", "Ali refuses to use modern tools, affecting efficiency. The business owner is annoyed by Ali.", "Ali's perfectionism leads to constant rework, frustrating collaborators. The team leader is annoyed by Ali.", "Ali insists on sourcing rare materials, delaying projects. The supplier is annoyed by Ali.", "Ali's lengthy explanations about craftsmanship bore customers. The store owner is annoyed by Ali.", "Ali's stubborn adherence to outdated techniques causes conflicts. The master craftsman is annoyed by Ali.", "Ali's criticism of other craftsmen's work creates tension. The guild leader is annoyed by Ali."]






###########################################################################################################
revealer_chef               = ["the restaurant sign", "his uniform", "his cuisine"] # Ali acts like a chef, but he's acturally a McDonald's employee
revealer_actor              = ["his lines", "his costume", "his prop", "his video", "the poster"] # Ali acts like an actor, but he's actually a porn star
revealer_comedian           = ["his lines", "his costume", "his prop", "his video"] # Ali acts like a comedian, but he's actually a Vtuber
revealer_instrumentalist    = ["his instrument", "his video"] # Ali acts like an instrumentalist, but he's actually a cymbalist
revealer_researcher         = ["his book", "the school sign"] # Ali acts like a researcher, but he's actually a gender studies researcher
revealer_athlete            = ["his sports gear", "his video"] # Ali acts like a baseball player, but he's actually a darts player
revealer_doctor             = ["the hospital sign"] # Ali acts like a surgeon, but he's actually a dermatologist
revealer_criminal           = ["a newspaper article about him", "he re-enact the crime."] # Ali acts like a assassin, but he's actually a groper
revealer_singer             = ["his song", "his CD", "his music video", "the poster"]
revealer_novelist           = ["the sound of him reading his manuscript aloud", "his book"] # Ali acts like a novelist, but he's actually a My Little Pony secondary creator
revealer_gambler            = ["his gambling paraphernalia"] # Ali acts like a poker player, but he's actually a lottery addicted.
revealer_progamer           = ["his game screen", "his game gear"]
revealer_teacher            = ["his blackboard", "his textbook"]
revealer_craftsman          = ["his works"]
###########################################################################################################

# s_rephrase lists depend on the hypo_i

comedy_script_chef = "Ali, a McDonald's employee, feels inferior to chefs at fine dining restaurants, so he speaks like a fine dining chef. Ali calls {a} {b}."
rephrase_chef=[
    ["French fry", "French"], ["Patty", "Steak"], ["Teriyaki Burger", "Japanese food"], ["Happy Meal", "full course meal"], ["McDonald's employee", "chef"], ["McDonald's", "restaurant"], ["cashier", "maître d' station"], ["part-time worker", "apprentice"]
]

comedy_script_progamer = "Ali, a rock paper scissors player, feels inferior to progamers, so he speaks like a progamers. Ali calls {a} {b}."
rephrase_progamer=[
    ["rock paper scissors", "PvP game"], ["rock paper scissors", "luck based"], ["hand", "input commands"], ["win", "kill"], ["player", "casual player"], ["win rate", "K/D"], ["rock can beat paper", "rock is meta of paper"],["Rock loses to paper, paper loses to scissors, and scissors loses to rock", "metagame"], ["luck", "RNG"], ["losing", "feeding"], ["throw", "input"], ["Hand shape", "UI"]
]

comedy_script_actor = "Ali, a porn star, feels inferior to Hollywood stars, so he speaks like a Hollywood star. Ali calls {a} {b}."
rephrase_actor=[
    ["porn", "romance"], ["having sex", "love scene"], ["undercover", "suspense movie"],["BDSM", "violence action"],["BDSM", "psycho thriller"],["porn star", "actor"],["porn", "PG-rated movie"],["adult film", "indie film"],["porn star", "co-actor"],["money shot", "climactic scene"],["fluffer", "production assistant"],["squirter", "side character"],["squirter", "extra"],["solo tease", "monodrama"],["medieval", "epic drama"],["nurse", "medical dramas"]
]

comedy_script_novelist = "Ali, a tabloid writer, feels inferior to novelists, so he speaks like a novelist. Ali calls {a} {b}."
rephrase_novelist=[
    ["lying", "creation"],["gossip", "character development"],["clickbait", "hook"],["expose", "revealing chapter"],["tabloid", "literary work"],["lie", "fiction"],["lie", "fantasy"],["fabrication","dramatization"], ["tabloid writer", "novelist"], ["tabloid writer", "creator"]
]





# Add new pairs in rephrase_athlete in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

comedy_script_billiards_player = "Ali, a billiards player, feels inferior to athletes, so he speaks like an athlete. Ali calls {a} {b}."
rephrase_athlete=[
    ["billiards", "indoor sports"], ["billiards players", "athletes"], ["table", "field"], ["pool hall", "arena"],
]

comedy_script_comedian = "Ali, a hospital clown, feels inferior to comedians, so he speaks like a comedian. Ali calls {a} {b}."
rephrase_comedian=[
    ["clown makeup", "hook"], ["magic tricks", "misdirection"],["hospital clown", "comedian"],["funny faces", "punch line"],["stage", "hospital"],["病院", "ハコ"]
]


comedy_script_instrumentalist = "Ali, a cymbalist, feels inferior to normal instrumentalists, such as pianists and violinists. so he speaks like an instrumentalist. Ali calls {a} {b}."
rephrase_instrumentalist=[
    ["crash", "crescendo"],["hitting cymbals", "performing"],["cymbal stand", "instrument stand"],["cymbal bag", "instrument case"],["cymbal polish", "instrument maintenance"],
]

comedy_script_criminal = "Ali, a petty criminal, feels inferior to famous criminals, so he speaks like a famous criminal. Ali calls {a} {b}."
rephrase_criminal=[
    ["shoplifting", "looting"], ["County Sheriff", "State power"],["arrest", "capture"],["parole", "clemency"],["forced to wear a GPS ankle strap.", "monitored by satellite."]
]
###########################################################################################################

# Listed below are some examples of how negative concepts have been elegantly rephrased in the media.

# for i in rephrase_rock_musician:
#  print(f"comedy script : Successful person's {i[0]} is {i[1]}; unsuccessful person's {i[0]} is just {i[0]}.")

# Define rephrase_novelist list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.

rephrase_rock_musician=[
 ["drug addiction, crime, arrest, dispute", "rock'n'-roll, scandal, inspiration, rebellion, charisma"]
,["drug addiction", "chemical muse"]
,["unemployment", "retirement, career transition"]
,["illiteracy", "rock'n'-roll"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
,["mental illness, authism", "rock'n'-roll, charisma"]
,["infidelity", "passionate love, romantic scandal"]
,["mental illness", "artistic temperament"]
]

rephrase_athlete=[
 ["injury", "badge, medal"]
,["doping", "performance enhancement"]
,["unemployment", "retirement, career transition"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
,["exercise", "sport"]
]

rephrase_researcher=[
 ["scholarship", "debt"]
,["unemployment", "retirement, career transition"]
,["failure, mistake", "learning experience, growth opportunity"]
]



rephrase_novelist=[
 ["depression, anxiety", "writer's block, slump"]
,["mental illness", "artistic temperament, charisma"]
,["unemployment", "retirement, career transition"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
]

# ,["obsession", "dedication"],["recklessness", "fearless approach"]

# ["Scholarship", "debt"]


# Extend 10 new items to rephrase_researcher list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.



rephrase_soldier=[
    ["injury", "badge"], ["casualty", "fallen hero"],
]


###########################################################################################################

univ_slump=["Trying to be the one who explains.", "Start a restaurant.", "Trying to be the one who teaches.", "Appearing in advertisements for online casinos and marijuana.", "Run for local council elections.", "Suddenly start talking about environmental protection and feminism."]

@dataclass
class Slump:
    slump:list # Typical actions when the slump.

slump_singer    = Slump([univ_slump, "playing country music and rapping.", "Starts singing sexual songs with revealing clothes.","Making a rockabilly arrangement of one's past hits.","Releasing a Christmas album","Collaborating with a DJ on EDM tracks","Starring in a reality TV show about their family",])
slump_chef      = Slump(["Start serving curry with superficial knowledge", "Serve trendy food with superficial knowledge","Opening a food truck","Starting a catering business",])
slump_actor     = Slump([univ_slump, "Starring in a low-budget movie with sharks", "Appearing on a TV shopping show"])
slump_athlete   = Slump([univ_slump, "Endorsing questionable health products or fad diets", "Appearing on reality TV shows", "Becoming a motivational speaker for corporate events","Trying to switch to another sport."])
slump_comedian  = Slump([univ_slump, "Doing magic tricks", "Performing at retirement homes", "Attempting to become a motivational speaker"])
slump_novelist  = Slump([univ_slump, "Writing fan fiction", "Writing erotic novels", "Writing self-help books","Ghostwriting celebrity autobiographies"])
slump_artist    = Slump([univ_slump, "Use excrement and genital as motifs.", "Presenting a blank canvas or just trash as a work of art."])
slump_researcher= Slump(["Focusing on quantity over quality of publications","Engaging in pseudoscience or fringe theories","Becoming a paid consultant for industries related to their field","Writing popular science books that oversimplify complex topics","Appearing on sensationalist documentaries or TV shows",])


# Add new items in slump_singer in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

# Define slump_researcher in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

# パチンコ屋で営業

# もうスランプ入った
###########################################################################################################
'''
@dataclass
class Binary:
    mental_physical_other:str
    art_not:str


    def post(self): # 流れ作業についていけない黒夢のファン
        if   self.mental_physical_other:
            self.kuroyume.append(["プライドの高い", "話を聞かない", "敬語を使えない", "千葉の", "自分に自信がある"])
        if   self.mental_physical_other == "o":
            self.kuroyume.append([""])
        elif self.mental_physical_other == "p":
            self.kuroyume.append(["健康な", "ガタイがいい", "痩せた", "太った", "背が高い", "色黒な", "ストリート系の"])
        elif self.mental_physical_other == "m":
            self.kuroyume.append(["目の悪い", "ニッコマの", "Fランの", "学士の", "大卒の"])
        if self.art_not:
            self.kuroyume.append(["物憂げな", "繊細な"])



binary_singer = Binary("o", "y")
binary_athlete = Binary("p", "" )
binary_novelist = Binary("m", "y")

'''

# agent_output
# a = f"{self.just_a}"
# b = [f"{hypo_i}","McJob worker","NEET","low wage worker","unemployed"]


###########################################################################################################
@dataclass
class Agent:
  ALL_AGENT: ClassVar[List['Agent']] = []
  agent_name: str
  job_or_not: str
  s_Grade: Grade
  s_Effort: Effort
  s_Suffer: Suffer
  s_StereoAction: StereoAction
  s_StereoAppear: StereoAppear
  s_Press: Press
  s_Term: Term
  s_b2scene : list
  s_revealer: list
  s_rephrase: list
  s_State: List[str]


  def __post_init__(self):
    Agent.ALL_AGENT.append(self)

agent_singer                =Agent("singer"             ,"y", [grade_singer]            , effort_singer         , suffer_singer         , stereoaction_singer               , stereoappear_singer               , press_singer          , [term_singer]             ,b2scene_singer + b2scene_rock_musician             , revealer_singer           ,None ,[])
agent_classical_musician    =Agent("classical musician" ,"y", [grade_classical_musician], effort_instrumentalist, suffer_instrumentalist, stereoaction_classical_musician   , stereoappear_classical_musician   , press_instrumentalist , [term_instrumentalist]    ,b2scene_classical_musician + b2scene_rock_musician , revealer_instrumentalist  ,rephrase_instrumentalist ,[])
agent_rock_musician         =Agent("rock musician"      ,"y", [grade_rock_musician]     , effort_instrumentalist, suffer_instrumentalist, stereoaction_rock_musician        , stereoappear_rock_musician        , press_instrumentalist , [term_instrumentalist]    ,b2scene_classical_musician + b2scene_rock_musician , revealer_instrumentalist  ,None ,[])
agent_comedian              =Agent("comedian"           ,"y", [grade_comedian]          , effort_comedian       , suffer_comedian       , stereoaction_comedian             , stereoappear_comedian             , press_comedian        , []                        ,None                                               , revealer_comedian         ,None ,[state_inst.state_unfunny])
agent_writer                =Agent("novelist"           ,"y", [grade_novelist]          , effort_writer         , suffer_writer         , stereoaction_writer               , stereoappear_writer               , press_writer          , [term_script]             ,b2scene_novelist                                   , revealer_novelist         ,rephrase_novelist ,[state_inst.state_illiteracy])
agent_artist                =Agent("artist"             ,"y", [grade_artist]            , effort_artist         , suffer_artist         , stereoaction_artist               , stereoappear_artist               , press_artist          , []                        ,None                                               , None                      ,None ,[])
agent_doctor                =Agent("doctor"             ,"y", [grade_doctor]            , effort_doctor         , suffer_doctor         , stereoaction_doctor               , stereoappear_doctor               , press_doctor          , []                        ,b2scene_doctor                                     , revealer_doctor           ,None ,[state_inst.state_illiteracy])
agent_researcher            =Agent("researcher"         ,"y", [grade_researcher]        , effort_researcher     , suffer_researcher     , stereoaction_researcher           , stereoappear_researcher           , press_researcher      , [term_researcher]         ,None                                               , revealer_researcher       ,None ,[state_inst.state_illiteracy])
agent_actor                 =Agent("actor"              ,"y", [grade_actor]             , effort_actor          , suffer_actor          , stereoaction_actor                , stereoappear_actor                , press_actor           , [term_actor, term_script] ,b2scene_actor                                      , revealer_actor            ,rephrase_actor ,[])
agent_chef                  =Agent("chef"               ,"y", [grade_chef]              , effort_chef           , suffer_chef           , stereoaction_chef                 , stereoappear_chef                 , press_chef            , [term_chef]               ,b2scene_chef                                       , revealer_chef             ,rephrase_chef ,[])
agent_athlete               =Agent("athlete"            ,"y", [grade_athlete]           , effort_athlete        , suffer_athlete        , stereoaction_athlete              , stereoappear_athlete              , press_athlete         , [term_athlete]            ,b2scene_athlete                                    , revealer_athlete          ,None ,[])
agent_psycho_criminal       =Agent("psycho criminal"    ,"y", [grade_psycho_criminal]   , None                  , None                  , stereoaction_psycho_criminal      , stereoappear_psycho_criminal      , None                  , []                        ,None                                               , revealer_criminal         ,rephrase_criminal ,[state_inst.state_criminal])
agent_examinee              =Agent("examinee"           ,"y", [grade_university]        , effort_examinee       , suffer_examinee       , None                              , None                              , None                  , []                        ,None                                               , None                      ,None ,[state_inst.state_illiteracy])
agent_gambler               =Agent("gambler"            ,"y", [grade_gambler]           , effort_gambler        , suffer_gambler        , stereoaction_gambler              , stereoappear_gambler              , press_gambler         , [term_gambler]            ,None                                               , revealer_gambler          ,None ,[])
agent_progamer              =Agent("progamer"           ,"y", [grade_progamer]          , effort_progamer       , suffer_progamer       , stereoaction_progamer             , stereoappear_progamer             , press_progamer        , [term_progamer]           ,b2scene_progamer                                   , revealer_progamer         ,rephrase_progamer, [])
agent_teacher               =Agent("teacher"            ,"y", [grade_teacher]           , effort_teacher        , suffer_teacher        , stereoaction_teacher              , stereoappear_teacher              , press_teacher         , [term_teacher]            ,b2scene_teacher                                    , revealer_teacher          ,None,[])


agent_old                   =Agent("old"        ,"", [], None, None, None, None, press_old         ,None, None, None, None, [state_inst.state_old])
agent_unhappy               =Agent("unhappy"    ,"", [], None, None, None, None, press_unhappy     ,None, None, None, None, [state_inst.state_poor, state_inst.state_unlucky])
agent_unhealthy             =Agent("unhealthy"  ,"", [], None, None, None, None, press_unhealthy   ,None, None, None, None, [state_inst.state_unhealthy])
agent_illiteracy            =Agent("illiteracy" ,"", [], None, None, None, None, press_illiteracy  ,None, None, None, None, [state_inst.state_illiteracy])
agent_fat                   =Agent("fat"        ,"", [], None, None, None, None, press_fat         ,None, None, None, None, [state_inst.state_fat])
agent_pedophilia            =Agent("pedophilia" ,"", [], None, None, None, None, press_pedophilia  ,None, None, None, None, [state_inst.state_pedophilia])
###########################################################################################################



