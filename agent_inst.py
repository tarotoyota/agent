from dataclasses import dataclass, field
from typing import List, ClassVar
###########################################################################################################
univ_modifier_job=["You're better than~", "You're as good as~", "You can be a~", "You can be the next~", "Top class~"] # unused


@dataclass
class Grade:
  ALL_GRADE: ClassVar[List['Grade']] = []
  grade_name:str

  hypo_s    :list# superior hyponym of the grade_name.
  hypo_s_pn :list# superior hyponym (proper noun) of the grade_name.
  hypo_i    :list# inferior hyponym of the grade_name. For example, bassist is an inferior hypoonym of rock musician. Darts player is an inferior hyponym of athlete.
  hypo_i_pn :list# inferior hyponym (proper noun) of the grade_name.

  modifier:list
  def __post_init__(self):
      Grade.ALL_GRADE.append(self)

grade_singer            =Grade("singer"             ,["singer"]                         ,["Beyonce"]            ,["idol", "rapper", "voice actor"]              ,["Aquatimez", "Orange range", "Britney Spears"],[])
grade_classical_musician=Grade("classical musician" ,["pianist", "violinist"]           ,["Bach"]               ,["cymbalist", "trianglist"]                    ,[]                                             ,[])
grade_rock_musician     =Grade("rock musician"      ,["guitarist", "vocalist"]          ,["Beatles"]            ,["bassist"]                                    ,[]                                             ,[])
grade_comedian          =Grade("comedian"           ,["comedian"]                       ,["Hitoshi Matsumoto"]  ,["Vtuber", "tv talent", "voice actor", "clown", "猿回し"],["Tsuyoshi Muro"]              ,[])
grade_novelist          =Grade("novelist"           ,["novelist"]                       ,["Stephen King"]       ,["Narou novelist", "tabloid writer"]           ,["Hiro Mizushima"],[])
grade_artist            =Grade("artist"             ,["artist"]                         ,["Picasso"]            ,["contemporary artist", "Hentai manga artist"] ,["Toru Mitsumune"], [])
grade_doctor            =Grade("doctor"             ,["neurosurgeon", "cardiologist"]   ,[]                     ,["dermatologist", "internist", "nurse"]        ,[],[])
grade_researcher        =Grade("researcher"         ,["mathematician"]                  ,["Albert Einstein"]    ,["gender studies researcher"]                  ,["Chizuruko Ueno"], [])
grade_actor             =Grade("actor"              ,["Hollywood star"]                 ,["Gary Oldman"]        ,["TV drama actor", "Porn actor", "ASMR actor", "Karaoke background video actor","extra", "commercial actor", "stuntman"],["Stallone"], [])
grade_chef              =Grade("chef"               ,["French chef"]                    ,["Michelin restaurant"],["Fast food restaurant employee"]              ,["McDonalds", "Jiro inspires", "Kitchen of Karaoke", "Kitchen of hotpillow hotel"], [])
grade_athlete           =Grade("athlete"            ,["baseball player"]                ,["Kyojin player"]      ,["billiards player", "darts player", "race walker"],["DeNA player"],["Top class", "First team"])
grade_psycho_criminal   =Grade("psycho criminal"    ,["murder", "terrorist"]            ,["Jeffrey Dahmer"]     ,["groper", "voyeurist", "shoplifter"]          ,["Jared Fogle"]        ,["Repeat offender"])
grade_progamer          =Grade("progamer"           ,["pro gamer"]                      ,["Umehara"]            ,["coin pusher player", "water game player"]    ,[]                     ,[])
grade_gambler           =Grade("gambler"            ,["gambler"]                        ,[""]                   ,["coin pusher player", "lottery addicted"]     ,[]                     ,[])
grade_university        =Grade("university"         ,["national University"]            ,["Tokyo Univ."]        ,["Private University"]                         ,["Tokyo MODE Gakuen"]  ,["A grade", "passed for active duty"])
grade_teacher           =Grade("teacher"            ,["university professor"]           ,["Harvard", "MIT"]     ,["cram school teacher", "kindergarten teacher", "sewing class teacher", "special education teacher", "elective teacher", "driving instructor"], ["Kumon"], ["Tenured"])
grade_craftsman         =Grade("craftsman"          ,["potter", "blacksmith"]           ,[]                     ,["fleshlight designer", "line worker"]         ,[], ["Highly skilled", "Renowned"])
grade_farmer            =Grade("farmer"             ,["vineyard farmer", "apple farmer"],["Napa Valley"]        ,["Parsley Farmer", "Farmer growing grapes for gummy"], [], ["Award-winning", "Sustainable", "organic"])
grade_director          =Grade("director"           ,["director"]                       ,["Steven Spielberg"]   ,["commercial director", "porn film director"]  ,["Toru Muranishi"], [])
grade_model             =Grade("model"              ,["fashion model"]                  ,["Gisele Bundchen"]    ,["hand model", "parts model"], [], ["High-end", "Runway"])
grade_guard             =Grade("guard"              ,["cop", "bodyguard"]               ,["Secret Service"]     ,["mall security", "nightclub bouncer", "school crossing guard", "lifeguard"], [], ["Armed", "Certified"])


# Define grade_guard instance in English without any explanation. Start answer with ```python. I'll run your response through the eval function so don't include unnecessary characters in your response.



# Extend new ones in grade_farmer in English without any explanation. Start answer with ```python. I'll run your response through the eval function so don't include unnecessary characters in your response.


grade_idol              =Grade("idol"               ,["Akimoto's idol", "Johnny's idol"],["AKB48", "Arashi"]    ,["local idol", "underground idol", "image video idol"], ["Kamen Joshi"], ["Center position", "Ace"])



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
effort_classical_musician   =Effort([])
effort_rock_musician        =Effort([])
effort_instrumentalist      =Effort([univ_effort_creator, "Quit smoking"])
effort_comedian             =Effort(["Abstinence", "People-watching"])
effort_writer               =Effort([univ_effort_creator])
effort_artist               =Effort([univ_effort_creator, "Creating art in the dark"])
effort_doctor               =Effort(["Abstinence", "Use nootropics"])
effort_researcher           =Effort([univ_effort_creator])
effort_actor                =Effort([univ_effort_creator, "Method acting", "Physical transformation for roles", "Taking specialized classes (e.g., dance, martial arts)", "Performing own stunts","Extensive research for historical roles", "Learning new languages for international productions", "Undergoing extreme weight changes","Continues to play the role in his private life."])
effort_chef                 =Effort([])
effort_athlete              =Effort(["Intense physical training", "Strict diet regimen", "Ice baths for recovery", "Altitude training", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"])
effort_progamer             =Effort(["Intense physical training", "Strict diet regimen", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"])
effort_gambler              =Effort(["Learning math", "Creating and checking statistical data"])
effort_examinee             =Effort(["Use nootropics", "Study all night", "Making flashcards", "Memorizing"])
effort_teacher              =Effort(["Creating engaging lesson plans", "Mentoring students outside of class hours", "Pursuing advanced degrees", "physical punishment"])
effort_craftsman            =Effort(["Practicing techniques for hours daily", "Studying traditional methods", "Experimenting with new materials", "Apprenticeship under a master", "Perfecting a single skill for years", "Attending specialized workshops"])

# Define effort_guard in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

effort_farmer               =Effort(["Waking up before dawn", "Implement organic farming.", "Working long hours in all weather conditions", "Continuous learning about crop science and animal husbandry", "Maintaining and repairing equipment", "Soil management and conservation practices", "Implementing sustainable farming techniques", "Adapting to changing climate patterns", "Market research and business planning"])
effort_director             =Effort([univ_effort_creator, "Storyboarding extensively", "Scouting locations", "Studying others' films and classic films", "Experimenting with new filming techniques", "Collaborating closely with actors and crew", "Fundraising for independent projects", "Attending film festivals", "Repeatedly does retakes"])
effort_model                =Effort(["Networking with industry professionals", "Maintaining a strict diet and fitness regimen", "Practicing poses and walks", "Attending casting calls and auditions regularly"])
effort_guard                =Effort(["Physical fitness training", "Self-defense classes", "Surveillance skills development", "Conflict resolution training", "First aid certification", "Night shifts", "Continuous situational awareness"])

effort_idol                 =Effort([])


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
suffer_singer               =Suffer([univ_suffer_creator, "Lack of stage presence","Lack of versatility","The song arrangements are lacking", "Uninspired Lyrics", "Repetitive Melodies"])


suffer_classical_musician   =Suffer([])
suffer_rock_musician        =Suffer([])
suffer_instrumentalist      =Suffer([univ_suffer_creator, "Emotionless","lacking a clear message","Inability to play in different styles","Poor improvisation skills","Lack of stage presence","Inability to tune instrument properly"])
suffer_comedian             =Suffer([univ_suffer_creator])
suffer_writer               =Suffer([univ_suffer_creator, "Deadline", l_suffer_script])
suffer_artist               =Suffer([univ_suffer_creator, "Emotionless","lack of creativity","unoriginal style","lack of craftsmanship", "Struggles with Proportions"  ,  "Weak anatomy knowledge"])
suffer_doctor               =Suffer(["The trauma of not being able to save a patient's life."])
suffer_researcher           =Suffer(["Plagiarism", "Not being able to get research funding", "Has white hair"])
suffer_actor                =Suffer([univ_suffer_creator, "Physical injuries from stunts", "Pressure to maintain a certain physical appearance","The damage caused by method acting", "Unconvincing Performances", "Difficulty with Accents/Dialects","Overacts","lack of stage presence","Lack of character depth","Inability to improvise","Lack of chemistry with co-stars", l_suffer_script])






# Define suffer_guard  in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.




# Extend 10 new items in l_suffer_game in English. I will run your reply through the eval function, so don't write anything unnecessary.

suffer_chef                 =Suffer([])

suffer_athlete              =Suffer(["Career-ending injuries","Pressure from fans and media", "Doping scandals", "Burnout", "Post-retirement depression", "Eating disorders", "Chronic pain", "Concussions and long-term brain damage", "Stalker"])
suffer_progamer             =Suffer([l_suffer_game, "Repetitive Strain Injury", "Carpal Tunnel Syndrome", "Eye strain",   "Addiction to gaming"])
suffer_gambler              =Suffer(["Addiction to gambling", "Financial ruin", "Depression and anxiety", "Lying to cover losses", "Chasing losses", "Neglecting work or family responsibilities", "Legal troubles", "Substance abuse as a coping mechanism", "Suicidal thoughts"])
suffer_examinee             =Suffer(["Exam pressure","Health issues due to long study hours","Intense competition","Balancing study and personal life","Fear that one failure will affect future","Pressure from parents and teachers","Self-loathing and loss of confidence","Deterioration of relationships with friends"])
suffer_teacher              =Suffer(["punk", "Pressure from parents and administration",  "Lack of autonomy in curriculum decisions", "Testing pressure", "Large class sizes", "bullying"])
suffer_craftsman            =Suffer(["Repetitive strain injuries", "Lack of successors", "Exposure to harmful materials", "Competition from mass-produced items", "Difficulty in finding apprentices", "Financial instability", "Long hours of solitary work", "burnout", "Struggles with modernization and technology"])

suffer_farmer               =Suffer(["Crop failures due to weather", "Market price fluctuations", "Equipment breakdowns", "Debt from loans", "Physical strain and injuries", "Eviction request", "Isolation in rural areas", "Pressure to adopt new technologies", "Regulatory challenges", "Competition from large agribusinesses", "Succession planning difficulties"])
suffer_director             =Suffer([univ_suffer_creator, "Budget constraints", "Creative differences with producers", "Pressure to meet box office expectations", "Negative critical reviews", "Challenges with difficult actors", "Technical issues during filming", "Post-production problems", "Distribution hurdles", "Balancing artistic vision with commercial viability", l_suffer_script])
suffer_model                =Suffer(["Body image issues", "Pressure to maintain unrealistic beauty standards", "Casting couch", "Constant scrutiny of physical appearance", "Age-related career decline", "Eating disorders", "Social media harassment"])
suffer_guard                =Suffer(["Monotonous work", "Long hours and night shifts", "Lack of recognition", "Stress from constant vigilance", "Physical strain from standing for long periods", "Dealing with aggressive individuals", "Post-traumatic stress from violent incidents", "Social isolation due to irregular work hours"])


suffer_idol                 =Suffer([])






###########################################################################################################

@dataclass
class Appear:
  ALL_APPEAR: ClassVar[List['Appear']] = []
  appear:list # Stereotypical appearance in reality or fiction.
  def __post_init__(self):
    Appear.ALL_APPEAR.append(self)

appear_singer                 =Appear(["Many piercings", "Many tattoos", "Colorful hair", "split tongue"])
appear_classical_musician     =Appear(["Formal black attire","Bow tie","Slicked-back hair","Round glasses","Pale complexion","Thin frame"])
appear_rock_musician          =Appear(["Many piercings", "Many tattoos", "Colorful hair", "split tongue"])
appear_comedian               =Appear([])
appear_writer                 =Appear(["Wears a samue", "Has a beard", "Thin and pale", "Has messy hair"])
appear_artist                 =Appear(["Many piercings", "Many tattoos", "Colorful hair"])
appear_doctor                 =Appear(["White coat", "Messy hair"])
appear_researcher             =Appear(["White coat", "Messy hair", "Has bags under one's eyes", "Carries around a clipboard", "using a wheelchair"])
appear_actor                  =Appear([])
appear_chef                   =Appear(["Kaiser moustache", "Being fat", "Wears a neckerchief", "Has a thick accent"])
appear_psycho_criminal        =Appear(["Unkempt appearance", "Wild eyes", "Scars or burn marks", "Twitchy movements", "Wears all black", "Clown-like makeup", "Disheveled hair", "Pale skin", "Bloodstained clothing", "Ritualistic tattoos", "Leather gloves", "Creepy mask"])
appear_athlete                =Appear(["Muscular build", "Athletic wear", "Sweatbands", "Sports gear", "Taped joints or limbs", "Shaved body", "Visible tan lines", "Team jersey or uniform", "Dreadlocks"])
appear_gambler                =Appear(["Disheveled appearance", "Dark circles under eyes", "Nervous twitches", "Flashy jewelry", "Expensive watch", "Rumpled suit", "Cigarette in hand", "Fidgeting with chips or cards", "Sunglasses indoors", "Sweaty brow", "Loosened tie", "Rolled-up sleeves", "Has a red pencil on his ear."])
appear_progamer               =Appear(["Headset", "Gaming chair", "Energy drinks", "Junk food", "Eyeglasses", "Acne", "Poor posture", "Headaches", "Back pain", "Wrist pain", "Messy hair", "Dark circles under eyes", "Skinny build", "Multiple monitors", "RGB lighting", "Wrist brace"])
appear_teacher                =Appear(["Glasses", "Cardigan sweater", "Sensible shoes", "Messy bun or ponytail", "Lanyard with ID badge", "Tote bag full of papers", "Elbow patches on jacket", "Chalk dust on clothes", "Coffee stains", "Comfortable, modest clothing", "Practical hairstyle", "Minimal makeup", "Wristwatch", "Reading glasses on a chain", "Colorful, quirky accessories"])
appear_craftsman              =Appear(["Leather apron", "Calloused hands", "Rolled-up sleeves", "Safety goggles", "Work boots", "Tool belt", "Weathered skin", "Muscular forearms", "Sawdust or wood shavings on clothes", "Protective gloves", "Bandana or cap", "Rugged, worn clothing", "Pencil behind ear", "Measuring tape clipped to belt", "Beard or mustache"])
# Define appear_guard in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


appear_farmer                 =Appear(["Overalls", "Plaid shirt", "Straw hat", "Work boots", "Sunburned skin", "Calloused hands", "Weathered face", "Farmer's tan", "Dirt under fingernails", "Faded jeans", "Bandana", "Belt buckle", "Leather work gloves", "Seed company cap"])
appear_director               =Appear(["Beret or flat cap", "Thick-rimmed glasses", "Scarf", "Black turtleneck", "Blazer with elbow patches", "Cargo vest with many pockets", "Comfortable, worn-in shoes", "Stubble or well-groomed beard", "Vintage watch", "Messenger bag or satchel", "Sunglasses (even indoors)", "Quirky, statement jewelry", "Fashionable, yet practical clothing", "Artsy, unconventional hairstyle", "Director's chair with name on it", "Viewfinder around neck"])
appear_model                  =Appear(["Tall and slender figure", "High cheekbones", "Long legs", "Perfect skin", "Symmetrical facial features", "Styled hair", "Designer clothing", "High heels", "Minimal makeup", "Manicured nails", "Confident posture", "Sunglasses", "Statement jewelry", "Visible collarbones", "Toned physique"])
appear_guard                  =Appear(["Uniform with badge", "Utility belt", "Earpiece", "Sunglasses", "Crew cut or short hair", "Muscular build", "Stern facial expression", "Combat boots", "Visible tattoos", "Clean-shaven face", "Bulletproof vest", "Name tag", "Flashlight", "Walkie-talkie", "Neatly pressed clothes", "Military-style posture", "Blood type tattoo", "scar"])


appear_idol                   =Appear([])


# Define stereoappear_farmer in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.




# Add new itmes in stereoaciton_classical_musician instance in English without any explanation. start answer with ```python.


# Add new itmes in each instance in English without any explanation. start answer with ```python.

###########################################################################################################
@dataclass
class Action:
  ALL_ACTION: ClassVar[List['Action']] = []
  action:list # Stereotypical action in reality or fiction.
  def __post_init__(self):
    Action.ALL_ACTION.append(self)

univ_stereoaction_creator=["Support the American Democratic Party.", "Being interested in environmental issues.", "Getting involved in the Scientology or SGI", "Being atheist or non-religious.", "Expressing support or opposition to abortion."]

action_singer                 =Action([univ_stereoaction_creator, "Has suicidal thoughts"])
action_classical_musician     =Action([univ_stereoaction_creator, "Suddenly starts writing music on paper."])
action_rock_musician          =Action([univ_stereoaction_creator, "Suddenly starts writing music on paper.", "Being an alcoholic", "Addicting drug and sex"])
action_comedian               =Action([univ_stereoaction_creator])
action_writer                 =Action([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
action_artist                 =Action([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
action_doctor                 =Action([])
action_researcher             =Action(["Starting a religion after overthinking it", "Suddenly starts writing mathematical formulas on the wall.", "Unable to understand others' feelings.", "Forgetting to eat or sleep while working on a problem", "Wearing mismatched or stained clothing", "Carrying around stacks of papers and books everywhere", "Muttering to themselves while pacing"])
action_actor                  =Action([univ_stereoaction_creator, "Looking down on lighting engineers and cinematographers.""Constantly practicing lines in public","Name-dropping famous directors or actors","Insisting on being called by their character's name","Refusing to break character even off-set","Demanding specific brands of bottled water on set","Throwing tantrums when not given enough screen time","Obsessing over their appearance and plastic surgery",])


# Add new itmes in stereo_guard instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


action_chef                   =Action(["Getting angry at customers for using condiments", "Yelling at kitchen staff",  "Striving for Michelin stars", "Taking pride in sourcing ingredients locally", "Focus on seasonal ingredients", "Focus on pesticide-free ingredients"])
action_psycho_criminal        =Action(["Talking to imaginary friends", "Collecting trophies from victims", "Writing manifestos", "Obsessively stalking targets", "Creating elaborate traps or puzzles", "Claim responsibility", "Leaving cryptic clues at crime scenes", "Sending taunting messages to police", "Developing a signature kill method", "Keeping detailed journals of crimes", "Ritualistic behavior before or after crimes", "Creating alter egos or personas"])
action_athlete                =Action(["Getting involved in a cult", "Splurge", "Bullying nerds", "Support the Republican Party", "Trash Talk", "meathead", "Partying excessively","Constantly flexing muscles","Overusing sports metaphors in conversation","Ignoring injuries to keep playing","Developing superstitious pre-game rituals",])
action_gambler                =Action(["Constantly checking scores or results", "Borrowing money from friends and family",  "Lying about whereabouts or activities", "Skipping work or important events to gamble", "Celebrating wins extravagantly", "Becoming irritable when unable to gamble", "Hiding betting slips or casino receipts", "Making increasingly risky bets", "Talking excessively about past wins", "Chasing losses with bigger bets", "Steal money"])
action_progamer               =Action(["Trash talking opponents", "Celebrating wins excessively", "Skipping meals to practice", "Neglecting personal hygiene", "Becoming irritable when unable to play", "Bragging about ranking or skills", "Forming rivalries with other players", "Rage quitting", "Streaming for hours", "Using gaming slang in everyday conversation"])
action_teacher                =Action(["Constantly correcting others' grammar", "Carrying a red pen everywhere", "Assigning homework on weekends and holidays","Favoring certain students", "Talking in a condescending tone", "Struggling with technology in the classroom", "Drinking excessive amounts of coffee"])
action_craftsman              =Action(["Obsessing over tool organization", "Refusing to use modern technology", "Criticizing mass-produced items", "Wearing traditional work attire", "Collecting rare or antique tools", "Talking extensively about material quality", "Insisting on doing everything by hand", "Becoming irritated when rushed", "Hoarding materials and supplies", "Giving unsolicited advice on craftsmanship", "Throw the failed piece onto the floor."])
action_farmer                 =Action(["Complaining about weather", "Waking up at dawn", "Wearing overalls and a straw hat", "Chewing on a piece of straw", "Talking about crop prices", "Distrusting city folk", "Attending county fairs", "Participating in farmers' markets", "Driving a tractor on public roads", "Using farming metaphors in conversation"])
action_director               =Action([univ_stereoaction_creator, "Constantly wearing a beret or scarf", "Using a megaphone unnecessarily", "Obsessively rewatching their own films", "Making grandiose statements about the power of cinema", "Insisting on unnecessary multiple takes", "Dramatically yelling 'cut!' and 'action!'", "Refusing to compromise on artistic vision", "Micromanaging every aspect of production", "Giving long, pretentious interviews about their craft", "Carrying a viewfinder everywhere"])
action_model                  =Action(["Walking with exaggerated hip movements", "Constantly checking appearance in mirrors", "Posing for selfies frequently", "Dieting excessively", "Attending fashion shows and parties", "Networking aggressively with industry professionals", "Practicing facial expressions and poses", "Complaining about uncomfortable high heels", "Discussing latest beauty treatments", "Maintaining a strict skincare routine", "Doing yoga or pilates regularly", "Endorsing products on social media", "Comparing themselves to other models", "Rushing to castings and photo shoots", "Meticulously planning outfits for events"])
action_guard                  =Action(["Has military experience", "Speaks in code over radio", "Wears sunglasses at night", "Constantly scans surroundings", "Stands with hands clasped in front", "Touches earpiece frequently", "Uses excessive force when provoked", "Drinks coffee excessively during night shifts", "Develops paranoia over time", "Has a tough, stoic demeanor"])
action_idol                   =Action([])


# Define stereoaction_model in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


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

# b2sceneのプロンプトに"こだわりが強い{agent}が", "プレッシャーに弱い{agent}が"という

# Define b2scene_craftsman in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

# 'b2scene' means stereotypical conflict scenes. Each item should end with "is annoyed by Ali."
# for i in all_b2scene:
#  print(script : {i} Then Ali actually shows him her performance or achievements and tries to get him to acknowledge her.)

# Ali is

b2scene_univ                = ["Ali's mind and body are exhausted from overwork. Ali's family is annoyed by Ali.", "Ali keeps asking his team member for advice. The team member is annoyed by Ali.", "Ali criticizes his team member for not being enthusiastic. The team member is annoyed by Ali.", "Ali, a unsuccessful poor, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.", "Ali, a unsuccessful poor, sticks to his career. Ali's wife is annoyed by Ali."]
b2scene_chef                = ["Ali trains cooks hard. The cook is annoyed by Ali.","Ali scolds a customer who asks for condiments. The customer is annoyed by Ali.","Ali urges the owner-chef who fired him to reconsider. The owner-chef is annoyed by Ali.","Ali changes the menu without consulting the restaurant manager. The manager is annoyed by Ali.","Ali insists on using expensive, out-of-season ingredients. The restaurant owner is annoyed by Ali."]
b2scene_actor               = ["After failing an audition, Ali goes to the director's house. The director is annoyed by Ali.","Ali's body and mind are exhausted through method acting. Ali's family is annoyed by Ali.","Ali is vocal with the director about the script and acting. The director is annoyed by Ali.","Ali constantly interrupts the rehearsal with his suggestions. The lead actor is annoyed by Ali.","Ali insists on multiple retakes for a minor scene. The crew is annoyed by Ali.","Ali stages a one-man protest outside a theater that rejected him. The theater owner is annoyed by Ali."]
b2scene_athlete             = ["After being dropped from the regular lineup, Ali goes to the manager's house and urges him to reconsider. The manager is annoyed by Ali.","Ali's body and mind are exhausted through over training. Ali's family is annoyed by Ali.","Ali, a poor athlete, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.","Ali, convinced he's the next big sports star, starts acting cocky and arrogant towards his teammates. The team is annoyed by Ali. ","Ali, a trainer, trains his teammates hard. The teammates is annoyed by Ali.","Ali, a renowned athlete, refuses to endorse a sponsor's product. The sponsor is annoyed by Ali. ","Ali's gambling addiction leads to financial problems and missed practices. The team captain is annoyed by Ali.","Ali's rivalry with a player from another team escalates into a physical altercation. The league commissioner is annoyed by Ali.","Ali shows up uninvited to a rival team's practice session to challenge their star player. The rival coach is annoyed by Ali.","Ali, a chef, refuses to accommodate a gourmet's detailed orders. The gourmet is annoyed by Ali. ","Ali, a chef, constantly makes changes to the menu without consulting the owner. The owner is annoyed by Ali."]
b2scene_novelist            = ["Ali's perfectionism is causing him to miss deadlines. The editor is annoyed by Ali.","Ali's body and mind are exhausted through over working. Ali's family is annoyed by Ali.","Ali, a successful novelist, refuses to make revisions requested by his editor. The editor is annoyed by Ali.","Ali, a novelist, constantly changes the plot of his book, frustrating his agent. The agent is annoyed by Ali..","Ali's plagiarism accusations against a fellow writer are causing a stir in the literary community. The literary agent is annoyed by Ali.","Ali's refusal to compromise on his artistic vision is hindering the book's commercial success. The publisher is annoyed by Ali.","Ali's public criticism of the judges' decision in a literary award is damaging his reputation. The literary award committee is annoyed by Ali..","Ali insists on rewriting the entire manuscript just days before the printing deadline. The publishing house CEO is annoyed by Ali.","Ali starts a heated debate with a literary critic who gave his book a negative review at a literary festival. The festival organizer is annoyed by Ali."]
b2scene_doctor              = ["Ali is in despair due to the trauma of not being able to cure his patients. His (family, coworker) is annoyed by Ali."]

b2scene_comedian            = ["Ali's controversial jokes offend audience members. The club owner is annoyed by Ali.","Ali refuses to adapt his material for different audiences. His manager is annoyed by Ali.","Ali's dark humor makes sponsors uncomfortable. The comedy festival director is annoyed by Ali.","Ali insists on performing longer than his allotted time slot. The headlining comedian is annoyed by Ali.","Ali's social media rants about other comedians create industry drama. His agent is annoyed by Ali.","Ali's refusal to censor his act for a TV appearance causes problems. The network executive is annoyed by Ali."]


# Define b2scene_guard in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



b2scene_classical_musician  = ["Ali insists on playing a piece in a different style than what the conductor requested. The conductor is annoyed by Ali.","Ali constantly interrupts rehearsals with his suggestions and modifications. The orchestra members are annoyed by Ali.","Ali refuses to participate in a promotional event for the orchestra, citing artistic integrity. The orchestra manager is annoyed by Ali.","Ali starts a public argument with a music critic who gave him a negative review after a concert. The concert organizer is annoyed by Ali.","Ali's rivalry with another musician leads to tension and conflict during performances. The concertmaster is annoyed by Ali."]
b2scene_rock_musician       = ["Ali insists on changing the setlist at the last minute without consulting the band. The band members are annoyed by Ali.","Ali's constant partying and late-night habits are affecting his performance. The band manager is annoyed by Ali.","Ali refuses to play a fan-favorite song during concerts, citing artistic reasons. The fans are annoyed by Ali.","Ali's destructive behavior on stage leads to damage to the venue. The venue owner is annoyed by Ali.","Ali's insistence on using outdated equipment causes technical issues during performances. The sound engineer is annoyed by Ali.","Ali publicly criticizes the band's record label, causing tension and potential legal issues. The record label executive is annoyed by Ali.","Ali's refusal to participate in promotional activities hinders the band's publicity efforts. The publicist is annoyed by Ali.","Ali's rivalry with a member of another band leads to a public altercation. The music festival organizer is annoyed by Ali.","Ali's unpredictable behavior and mood swings cause delays in recording sessions. The producer is annoyed by Ali."]
b2scene_singer              = ["Ali insists on singing songs in a different style than what the producer requested. The producer is annoyed by Ali.","Ali's constant vocal exercises at home are disturbing the neighbors. The neighbors are annoyed by Ali.","Ali refuses to perform a popular song during concerts, citing artistic reasons. The fans are annoyed by Ali.","Ali's late-night partying is affecting his voice and performance quality. The tour manager is annoyed by Ali.","Ali insists on making last-minute changes to the setlist during live performances. The band members are annoyed by Ali.","Ali's public feud with another singer is causing negative publicity. The record label executive is annoyed by Ali.","Ali's refusal to promote his new album on social media hinders its success. The marketing team is annoyed by Ali.","Ali's insistence on using a specific microphone that frequently malfunctions causes delays. The sound technician is annoyed by Ali.","Ali's unpredictable behavior during interviews creates awkward situations. The publicist is annoyed by Ali.","Ali's rivalry with another singer leads to tension and conflicts during collaborative projects. The collaboration manager is annoyed by Ali."]
b2scene_progamer            = ["Ali insists on using unconventional strategies during team matches. The team captain is annoyed by Ali.","Ali's constant trash-talking during streams is damaging the team's reputation. The team manager is annoyed by Ali.","Ali refuses to practice with the team, claiming he performs better solo. The coach is annoyed by Ali.","Ali's rage-quitting during an important tournament match costs the team a victory. The tournament organizer is annoyed by Ali.","Ali's addiction to gaming leads to neglect of his physical health and missed team meetings. The team doctor is annoyed by Ali.","Ali publicly criticizes the game developers for balance issues after a loss. The esports league commissioner is annoyed by Ali.","Ali's rivalry with a player from another team escalates into a real-life confrontation. The event security is annoyed by Ali.","Ali refuses to practice with the team, claiming he's already skilled enough. His teammates are annoyed by Ali.","Ali's overly competitive nature leads him to sabotage his teammates during scrimmages. His teammates are annoyed by Ali.",]
b2scene_teacher             = ["Ali insists on teaching the curriculum in his own unconventional way. The principal is annoyed by Ali.","Ali's constant changes to the lesson plan confuse the students. The students are annoyed by Ali.","Ali refuses to participate in standardized testing preparations, citing educational philosophy. The school board is annoyed by Ali.","Ali's insistence on assigning unconventional homework frustrates parents. The parents are annoyed by Ali.","Ali's insistence on grading students based on non-traditional criteria causes complaints. The school counselor is annoyed by Ali.","Ali's overly strict discipline methods lead to student protests. The student council is annoyed by Ali."]
b2scene_craftsman           = ["Ali insists on using only traditional methods, slowing down production. The workshop manager is annoyed by Ali.", "Ali refuses to compromise on material quality, increasing costs. The client is annoyed by Ali.", "Ali takes too long perfecting details, missing deadlines. The project coordinator is annoyed by Ali.", "Ali criticizes mass-produced items in front of potential buyers. The sales representative is annoyed by Ali.", "Ali refuses to use modern tools, affecting efficiency. The business owner is annoyed by Ali.", "Ali's perfectionism leads to constant rework, frustrating collaborators. The team leader is annoyed by Ali.", "Ali insists on sourcing rare materials, delaying projects. The supplier is annoyed by Ali.", "Ali's lengthy explanations about craftsmanship bore customers. The store owner is annoyed by Ali.", "Ali's stubborn adherence to outdated techniques causes conflicts. The master craftsman is annoyed by Ali.", "Ali's criticism of other craftsmen's work creates tension. The guild leader is annoyed by Ali."]

b2scene_farmer              = ["Ali insists on using organic methods despite lower yields. The farm owner is annoyed by Ali.","Ali refuses to use pesticides, leading to increased pest damage. The neighboring farmers are annoyed by Ali.","Ali's stubborn adherence to traditional farming methods slows down production. The farm workers are annoyed by Ali.","Ali's push for sustainable practices increases short-term costs. The farm's financial advisor is annoyed by Ali.","Ali's refusal to sell to large supermarket chains affects the farm's profits. The sales manager is annoyed by Ali.",]
b2scene_director            = ["Ali's perfectionism leads to constant reshoots, causing the production to go over budget. The producer is annoyed by Ali.", "Ali refuses to compromise on his artistic vision, jeopardizing the film's commercial viability. The studio executive is annoyed by Ali.", "Ali's micromanagement of actors' performances is causing tension on set. The lead actor is annoyed by Ali.", "Ali's last-minute script changes are causing chaos in the production schedule. The production manager is annoyed by Ali.", "Ali's insistence on filming in a dangerous location is raising safety concerns. The stunt coordinator is annoyed by Ali.", "Ali's constant arguments with the editor about the final cut are delaying the film's release. The distributor is annoyed by Ali.", "Ali's public criticism of the film's marketing strategy is creating negative publicity. The marketing team is annoyed by Ali.", "Ali's refusal to work within the agreed budget is straining relationships with investors. The film's financier is annoyed by Ali."]
b2scene_model               = ["Ali, a model, constantly criticizes the photographer's vision during a photoshoot. The photographer is annoyed by Ali.", "Ali shows up late to a major fashion show, causing delays. The show director is annoyed by Ali.", "Ali refuses to wear an outfit chosen by the stylist, insisting on their own selection. The stylist is annoyed by Ali.", "Ali's demanding behavior and excessive requests are frustrating the makeup artist. The makeup artist is annoyed by Ali.", "Ali's insistence on specific lighting is causing delays on set. The lighting technician is annoyed by Ali.", "Ali's constant diet talk and food restrictions are irritating other models during a group shoot. The other models are annoyed by Ali.", "Ali's refusal to walk in shoes provided for the runway show is causing last-minute changes. The shoe designer is annoyed by Ali.", "Ali's public criticism of a fashion brand they're contracted with is causing tension. The brand's PR team is annoyed by Ali.", "Ali's excessive social media use during a closed set shoot is disrupting the work flow. The production manager is annoyed by Ali.", "Ali's demands for retouching on already published photos are causing extra work. The retouching artist is annoyed by Ali."]
b2scene_guard               = ["Ali insists on following security protocols to the letter, causing delays at the entrance. The event organizer is annoyed by Ali.", "Ali boasts about his combat skills and challenges a trained martial artist to a sparring match. The gym owner is annoyed by Ali.", "Ali dismisses the need for backup when confronting multiple suspects. The police chief is annoyed by Ali.", "Ali takes on additional shifts without rest, claiming he doesn't need sleep. The security company owner is annoyed by Ali.", "Ali refuses to take breaks during a 12-hour shift, pushing himself to the limit. The manager is annoyed by Ali.", "Ali maintains his post during extreme weather conditions, ignoring calls to seek shelter. The manager is annoyed by Ali.", "Ali continues working despite a minor injury, refusing medical attention. The first aid team is annoyed by Ali." ]


b2scene_idol                = []

###########################################################################################################

# 養育費でタトゥー入れる奴爆弾解除できねーだろ

b3scene_default             = ["Sudden vacancy"]

b3scene_singer              = ["Sudden vacancy"]
b3scene_instrumentalist     = ["Sudden vacancy"]
b3scene_comedian            = ["Sudden vacancy"]
b3scene_writer              = ["Sudden vacancy", "Ghost writer"]
b3scene_artist              = []
b3scene_doctor              = ["Suddenly ill"]
b3scene_researcher          = ["Bomb Defusal", "Death Game", "Zombie Pandemic"]
b3scene_actor               = ["Sudden vacancy"]
b3scene_chef                = ["Sudden vacancy"]
b3scene_athlete             = ["Sudden vacancy", "Death Game","Zombie Pandemic","Life saving scene"]
b3scene_criminal            = ["Ali is job interviewed by a terrorists group."]
b3scene_gambler             = ["death game", "underground casino tournament"]
b3scene_progamer            = ["Sudden vacancy"]
b3scene_teacher             = []

# Define b3scene_guard

b3scene_farmer              = []
b3scene_guard = ["Hostage situation", "Terrorist attack", "High-profile asset protection", "Prison riot", "Undercover operation"]
b3scene_idol                = []

b3scene_old                 = ["An old potter is urgently looking for a successor.", "A middle-aged person is urgently looking for a marriage partner."]
b3scene_unhappy             = ["Ali guards a spiritual hot spot.", "Ali manufactures spiritual goods.","Ali sells spiritual goods door-to-door.", "Ali offers fortune telling.", "Ali lives near a spiritual hot spot."]
b3scene_unhealthy           = ["Ali sales alternative medicine."]
b3scene_illiteracy          = ["Ali sales nootropics."]
b3scene_fat                 = ["A middle-aged person is urgently looking for a marriage partner."]
b3scene_pedophilia          = ["Ali is job interviewed by a pediatric clinic."]

###########################################################################################################
revealer_singer             = ["his song", "his CD", "his music video", "the poster"]
revealer_instrumentalist    = ["his instrument", "his video", "his performance"] # Ali acts like an instrumentalist, but he's actually a cymbalist
revealer_chef               = ["the restaurant sign", "his uniform", "his cuisine"] # Ali acts like a chef, but he's acturally a McDonald's employee
revealer_novelist           = ["the sound of him reading his manuscript aloud", "his book"] # Ali acts like a novelist, but he's actually a My Little Pony secondary creator
revealer_artist             = ["his work"]
revealer_actor              = ["his lines", "his costume", "his prop", "his video", "the poster", "his filming location"] # Ali acts like an actor, but he's actually a porn star
revealer_comedian           = ["his lines", "his costume", "his prop", "his video"] # Ali acts like a comedian, but he's actually a Vtuber
revealer_researcher         = ["his book", "the school sign"] # Ali acts like a researcher, but he's actually a gender studies researcher
revealer_athlete            = ["his sports gear", "his video"] # Ali acts like a baseball player, but he's actually a darts player
revealer_doctor             = ["the hospital sign"] # Ali acts like a surgeon, but he's actually a dermatologist
revealer_criminal           = ["a newspaper article about him", "he re-enact the crime."] # Ali acts like a assassin, but he's actually a groper
revealer_gambler            = ["his gambling paraphernalia"] # Ali acts like a poker player, but he's actually a lottery addicted.
revealer_progamer           = ["his game screen", "his game gear"]
revealer_teacher            = ["his blackboard", "his textbook"]
revealer_craftsman          = ["his works"]

revealer_farmer             = ["his crops", "his farm"]
revealer_director           = ["the lines", "the costumes", "the props", "the videos", "the posters", "his filming location"]
revealer_model              = ["his wears", "his media"] # ????

#
revealer_guard=[]
revealer_idol               = []
###########################################################################################################

# make_arg_1_listのために各アイテムを["[a], [b, c]"]みたいな感じに整形!!!■■■

rephrase_singer             = []
rephrase_classical_musician = []
rephrase_rock_musician      = []
rephrase_comedian           = []
rephrase_writer             = []
rephrase_artist             = []
rephrase_doctor             = []
rephrase_researcher         = []
rephrase_actor              = []
rephrase_chef               = []
rephrase_athlete            = []
rephrase_criminal           = []
rephrase_examinee           = []
rephrase_gambler            = []
rephrase_progamer           = []
rephrase_teacher            = []
rephrase_idol               = []
rephrase_farmer             = []
rephrase_director           = [] # ■■■
rephrase_model              = []
rephrase_guard              = []
# s_rephrase lists depend on the hypo_i



rephrase_chef           += [
    ["[French fry], [French cuisine]", "[Patty], [Steak]", "[Teriyaki Burger], [Japanese cuisine]", "[Happy Meal], [Full course meal]", "[McDonald's employee], [Chef]", "[McDonald's], [restaurant]", "[Cashier], [Maitre d' station]", "[Part-time worker], [Apprentice]"]
]

rephrase_progamer       += [
    ["[rock paper scissors], [PvP game]", "[Rock paper scissors], [Luck based]", "[Hand], [Input commands]", "[Win], [Kill]", "[Player], [Casual player]", "[Win rate], [K/D]", "[Rock can beat paper], [Rock is meta of paper]", "[Rock loses to paper, paper loses to scissors, and scissors loses to rock], [Metagame, Rule, 環境]", "[Luck], [RNG]", "[Losing], [Feeding]", "[Throw], [Input]", "[Hand shape], [UI]", "[Opponent], [Enemy]", "[Beginner], [Noob]"]
]


rephrase_actor          +=[ # Ali, a porn star, feels inferior to Hollywood stars, so he speaks like a Hollywood star. Ali calls [0] [1]. Ali hides the fact that he is a porn star and pretends to be an actor."
    ["porn", "romance"], ["having sex", "love scene"], ["undercover", "suspense movie"],["BDSM", "violence action"],["BDSM", "psycho thriller"],["porn star", "actor"],["porn", "PG-rated movie"],["adult film", "indie film"],["porn star", "co-actor"],["money shot", "climactic scene"],["fluffer", "production assistant"],["squirter", "side character"],["squirter", "extra"],["solo tease", "monodrama"],["medieval", "epic drama"],["nurse", "medical dramas"]
]

rephrase_writer         +=[ # "Ali, a tabloid writer, feels inferior to novelists, so he speaks like a novelist. Ali calls [0] [1]. Ali hides the fact that he is a tabloid writer and pretends to be a novelist."
    ["lying", "creation"],["gossip", "character development"],["clickbait", "hook"],["expose", "revealing chapter"],["tabloid", "literary work"],["lie", "fiction"],["lie", "fantasy"],["fabrication","dramatization"], ["tabloid writer", "novelist"], ["tabloid writer", "creator"]
]

rephrase_athlete        +=[ # "Ali, a e-sports player, feels inferior to athletes, so he speaks like a athlete. Ali calls [0] [1]. Ali hides the fact that he is an e-sports player and pretends to be an athlete."
    ["e-sports", "indoor sports"], ["tenosynovitis", "ligament injury"]
]

# Add new pairs in rephrase_athlete in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

rephrase_singer         +=[ # "Ali, a back chorus, feels inferior to vocalists, so he speaks like a vocalist. Ali calls [0] [1]."
    ["back chorus", "lead vocalist"], ["singing as a back chorus", "performing"]
]

rephrase_athlete        +=[ # "Ali, a billiards player, feels inferior to athletes, so he speaks like an athlete. Ali calls [0] [1]."
    ["billiards", "indoor sports"], ["billiards players", "athletes"], ["table", "field"], ["pool hall", "arena"],
]

rephrase_comedian       +=[ # "Ali, a hospital clown, feels inferior to comedians, so he speaks like a comedian. Ali calls [0] [1]."
    ["clown makeup", "hook"], ["magic tricks", "misdirection"],["hospital clown", "comedian"],["funny faces", "punch line"],["stage", "hospital"],["病院", "ハコ"] # 終末病棟 客が重い
]

rephrase_gambler        +=[ # "Ali, a coin pusher player, feels inferior to gamblers, so he speaks like a gambler. Ali calls [0] [1]."
    ["coin", "chip"],["pushing coins", "placing bets"],["coin stack", "pot"],["prize", "payout"],["game over", "bust"],
]

rephrase_classical_musician+=[ # "Ali, a cymbalist, feels inferior to normal instrumentalists, such as pianists and violinists. so he speaks like an instrumentalist. Ali calls [0] [1]."
    ["crash", "crescendo"],["hitting cymbals", "performing"],["cymbal stand", "instrument stand"],["cymbal bag", "instrument case"],["cymbal polish", "instrument maintenance"],
]

rephrase_criminal       +=[ # "Ali, a petty criminal, feels inferior to famous criminals, so he speaks like a famous criminal. Ali calls [0] [1]."
    ["shoplifting", "looting"], ["County Sheriff", "State power"],["arrest", "capture"],["parole", "clemency"],["forced to wear a GPS ankle strap.", "monitored by satellite."]
]
###########################################################################################################

# Listed below are some examples of how negative concepts have been elegantly rephrased in the media.

# for i in rephrase_rock_musician:
#  print(f"comedy script : Successful person's {i[0]} is {i[1]}; unsuccessful person's {i[0]} is just {i[0]}.")

# Define rephrase_novelist list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.

rephrase_rock_musician  +=[
 ["drug addiction, crime, arrest, dispute", "rock'n'-roll, scandal, inspiration, rebellion, charisma"]
,["drug addiction", "chemical muse"]
,["unemployment", "retirement, career transition"]
,["self-neglect, self-harm", "rock'n'-roll"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
,["mental illness, authism", "rock'n'-roll, charisma"]
,["infidelity", "passionate love, romantic scandal"]
,["mental illness", "artistic temperament"]
]

rephrase_athlete        +=[
 ["injury", "badge, medal"]
,["doping", "performance enhancement"]
,["unemployment", "retirement, career transition"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
,["exercise", "sport"]
]

rephrase_researcher     +=[
 ["scholarship", "debt"]
,["unemployment", "retirement, career transition"]
,["failure, mistake", "learning experience, growth opportunity"]
,["psychopass", "charisma, genius"]
]

rephrase_writer         +=[
 ["depression, anxiety", "writer's block, slump"]
,["mental illness", "artistic temperament, charisma"]
,["unemployment", "retirement, career transition"]
,["defeat, failure, mistake", "learning experience, growth opportunity"]
]

# ,["obsession", "dedication"],["recklessness", "fearless approach"]

# ["Scholarship", "debt"]


# Extend 10 new items to rephrase_researcher list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.


###########################################################################################################




###########################################################################################################

@dataclass
class Slump:
    slump:list # Typical actions when the slump.

l_slump_showbiz             = ["Trying to be the one who explains.", "Start a restaurant.", "Trying to be the one who teaches.", "Appearing in advertisements for online casinos and marijuana.", "Run for local council elections.", "Suddenly start talking about environmental protection and feminism.", "Appear in a show at a pachinko parlor."]

slump_singer              = Slump([l_slump_showbiz, "playing country music and rapping.", "Starts singing sexual songs with revealing clothes.","Making a rockabilly arrangement of one's past hits.","Releasing a Christmas album","Collaborating with a DJ on EDM tracks","Starring in a reality TV show about their family"])
slump_classical_musician  = Slump([l_slump_showbiz])
slump_rock_musician       = Slump([l_slump_showbiz])
slump_comedian            = Slump([l_slump_showbiz, "Doing magic tricks", "Performing at retirement homes", "Attempting to become a motivational speaker"])
slump_writer              = Slump(["Writing fan fiction", "Writing erotic novels", "Writing self-help books","Ghostwriting celebrity autobiographies"])
slump_artist              = Slump([l_slump_showbiz, "Use excrement and genital as motifs.", "Presenting a blank canvas or just trash as a work of art."])
slump_doctor              = Slump([])
slump_researcher          = Slump(["Focusing on quantity over quality of publications","Engaging in pseudoscience or fringe theories","Becoming a paid consultant for industries related to their field","Writing popular science books that oversimplify complex topics","Appearing on sensationalist documentaries or TV shows"])
slump_actor               = Slump([l_slump_showbiz, "Starring in a low-budget movie with sharks", "Appearing on a TV shopping show"])
slump_chef                = Slump(["Start serving curry with superficial knowledge", "Serve trendy food with superficial knowledge","Opening a food truck","Starting a catering business"])
slump_athlete             = Slump([l_slump_showbiz, "Endorsing questionable health products or fad diets", "Appearing on reality TV shows", "Becoming a motivational speaker for corporate events","Trying to switch to another sport."])
slump_criminal            = Slump([])
slump_examinee            = Slump([])
slump_gambler             = Slump([])
slump_progamer            = Slump([])
slump_teacher             = Slump([])



# Add new items in slump_singer in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

# Define slump_researcher in English. I will run your response through the eval function so please do not include unnecessary characters in your response.


# もうスランプ入った
###########################################################################################################

@dataclass
class Binary:
    ALL_BINARY: ClassVar[List['Binary']] = []
    mental_physical_other:str # mental labor -> m, physical labor -> p, other -> blank
    art_not:str
    sports_not:str
    cant:list
    job_not:str
    too_slow:list # だーりんず:ひったくり, おぐ:r1用のネタ2本
    paid_item:list
    link_to_reverse_adj:list
    pride_neet_1:list

    def __post_init__(self):
        Binary.ALL_BINARY.append(self)

        if   self.mental_physical_other:
            self.pride_neet_1.append(["プライドの高い", "話を聞かない", "敬語を使えない", "千葉の", "自分に自信がある", "感情的な"])
            self.cant.append(["人々の役に立つ", "夢を掴む"])
            self.paid_item.append(["training", "advice"])
        if   self.mental_physical_other == "m":
            self.pride_neet_1.append(["目の悪い", "ニッコマの", "Fランの", "学士の", "大卒の", "痩せた", "太った", "繊細な", "暗い", "インドアな", "几帳面な", "体力のない", "理屈っぽい"])
            self.link_to_reverse_adj.append("<a href='state#illiteracy'>illiteracy</a>")
            self.too_slow.append(["eating blue fish"])
            self.paid_item.append(["nootropics"])
        elif self.mental_physical_other == "p":
            self.pride_neet_1.append(["健康な", "ガタイがいい", "痩せた", "背が高い", "色黒な", "ストリート系の", "明るい", "社交的な", "姿勢のいい", "日焼けした", "アウトドアな", "体育会系の", "食事に気を使ってる"])
            self.link_to_reverse_adj.append("<a href='state#unhealthy'>unhealthy</a>")
            self.too_slow.append(["doing push ups"])
        if self.art_not == "a":
            self.pride_neet_1.append(["物憂げな", "繊細な", "暗い", "インドアな", "几帳面な", "体力のない", "理屈っぽい"])
            self.cant.append(["人々を感動させる"])
            #self.too_slow.append([""])
        if self.art_not == "a" and not self.mental_physical_other == "m":
            self.link_to_reverse_adj.append("<a href='state#illiteracy'>illiteracy</a>")

        if self.sports_not:
            pass





#牛丼すら作れない奴が子供作るな
#バイトなのに子供二人作った事
#

'''
@dataclass
class Binary:
    ALL_BINARY: ClassVar[List['Binary']] = []
    mental_physical_other:str # mental labor -> m, physical labor -> p, other -> blank
    art_not:str
    sports_not:str
    cant:list
    job_not:str
    too_slow:list
    paid_item:list
    link_to_reverse_adj:list
    pride_neet_1:list # adjective. f"comedy prompt : You quit your job, so you're just a {self.pride_neet_1} unemployed now."
'''

binary_singer               = Binary("o", "a", "" , [], "j",[],[],[]                                       ,["邦楽が好きな", "声が良い", "リズム感のある", "ステージ慣れした", "カラオケ上手な", "表現力豊かな", "感性の豊かな", "MCスキルが高い", "声の大きい"])
binary_classical_musician   = Binary("o", "a", "" , [], "j",[],[],[]                                       ,["家が金持ってた", "クラシック通な", "ステージ慣れした"])
binary_rock_musician        = Binary("o", "a", "" , [], "j",[],[],[]                                       ,["薬をやっている", "ステージ慣れした", "MCスキルが高い", "声の大きい"])
binary_comedian             = Binary("o", "a", "" , [], "j",[],[],["<a href='state#unfunny'>unfunny</a>"]  ,["明るい", "ステージ慣れした", "声の大きい"])
binary_novelist             = Binary("m", "a", "" , [], "j",[],[],[]                                       ,["メンヘラな", "文章力のある"])
binary_artist               = Binary("o", "a", "" , [], "j",[],[],[]                                       ,["メンヘラな", "創造力豊かな", "感性の豊かな", "表現力のある"])
binary_doctor               = Binary("m", "" , "" , [], "j",[],[],[]                                       ,["物知りな", "人体に詳しい", "冷静な判断ができる"])
binary_researcher           = Binary("m", "" , "" , [], "j",[],[],[]                                       ,["物知りな", "専門知識のある"])
binary_actor                = Binary("o", "a", "" , [], "j",[],[],[]                                       ,["映画好きな", "表現力豊かな", "感情表現の上手い", "カメラ慣れした", "声の大きい"])
binary_chef                 = Binary("p", "" , "" , [], "j",[],[],[]                                       ,["食事に気を使ってる", "味覚の鋭い"])
binary_athlete              = Binary("p", "" , "s", [], "j",[],[],[]                                       ,["食事に気を使ってる", "体力のある", "筋肉質な", "反射神経の良い", "競争心の強い", "ストイックな", "体の柔軟な", "スポーツマンシップのある", "チームワークの良い", "瞬発力のある"])
binary_psycho_criminal      = Binary("o", "" , "" , [], "" ,[],[],[]                                       ,["反社会的な", "冷酷な", "予測不可能な"])
binary_examinee             = Binary("m", "" , "" , [], "" ,[],[],[]                                       ,["計画的な", "記憶力の良い", "自己管理のできる", "知識欲の強い", "粘り強い"])
binary_gambler              = Binary("m", "" , "" , [], "" ,[],[],[]                                       ,["債務者の","リスク好きな", "運の良い", "勝負強い"])
binary_progamer             = Binary("m", "" , "s", [], "j",[],[],[]                                       ,["ゲーム好きな", "反射神経の良い", "チームワークの良い", "競争心の強い"])
binary_teacher              = Binary("m", "" , "" , [], "j",[],[],[]                                       ,["教育熱心な", "子供思いの"])
binary_farmer               = Binary("p", "" , "" , [], "j",[],[],[]                                       ,["広い土地持ってる", "田舎に住んでる"])
binary_director             = Binary("m", "a", "" , [], "j",[],[],[]                                       ,["映画好きな", "表現力豊かな", "感情表現の上手い"])
binary_model                = Binary("o", "" , "" , [], "j",[],[],[]                                       ,["おしゃれな","写真映えする","身だしなみの良い","スタイリッシュな","魅力的な","立ち振る舞いの美しい","体型維持に気を使う","流行に敏感な","見た目の良い"])
binary_guard                = Binary("p", "" , "" , [], "j",[],[],[]                                       ,["防犯意識の高い", "監視カメラに詳しい", "巡回ルートを知り尽くした", "防犯ベルに敏感な", "警戒心の強い", "観察力の鋭い", "護身術に長けた", "緊急時の対応力がある", "危険予知能力が高い", "規律正しい", "冷静沈着な", "状況判断力に優れた", "チームワークに優れた"])

# Binary's last list is .pride_neet_1 attribute.
# Extend 10 new str objects in binary_guard.pride_neet_1. I'll run your response through the eval function so please do not include unnecessary characters in your response.




###########################################################################################################
# お笑いを作るのではなくお笑いを型抜きする



###########################################################################################################
@dataclass
class Agent:
  ALL_AGENT: ClassVar[List['Agent']] = []
  agent_name: str
  job_or_not: str
  s_Grade: Grade
  s_Effort: Effort
  s_Suffer: Suffer
  s_Action: Action
  s_Appear: Appear
  s_Term: Term
  s_b2scene : list
  s_b3scene : list
  s_revealer: list
  s_rephrase: list
  s_Binary : Binary
  s_Slump  : Slump


  def __post_init__(self):
    Agent.ALL_AGENT.append(self)

agent_singer                =Agent("singer"             ,"y", grade_singer            , effort_singer         , suffer_singer         , action_singer               , appear_singer               , [term_singer]             ,b2scene_singer + b2scene_rock_musician             ,b3scene_default      , revealer_singer           ,rephrase_singer            ,binary_singer             ,slump_singer             )
agent_classical_musician    =Agent("classical_musician" ,"y", grade_classical_musician, effort_instrumentalist, suffer_instrumentalist, action_classical_musician   , appear_classical_musician   , [term_instrumentalist]    ,b2scene_classical_musician + b2scene_rock_musician ,b3scene_default      , revealer_instrumentalist  ,rephrase_rock_musician     ,binary_classical_musician ,slump_classical_musician )
agent_rock_musician         =Agent("rock_musician"      ,"y", grade_rock_musician     , effort_instrumentalist, suffer_instrumentalist, action_rock_musician        , appear_rock_musician        , [term_instrumentalist]    ,b2scene_classical_musician + b2scene_rock_musician ,b3scene_default      , revealer_instrumentalist  ,rephrase_classical_musician,binary_rock_musician      ,slump_rock_musician      )
agent_comedian              =Agent("comedian"           ,"y", grade_comedian          , effort_comedian       , suffer_comedian       , action_comedian             , appear_comedian             , []                        ,b2scene_comedian                                   ,b3scene_default      , revealer_comedian         ,rephrase_comedian          ,binary_comedian           ,slump_comedian           )
agent_writer                =Agent("writer"             ,"y", grade_novelist          , effort_writer         , suffer_writer         , action_writer               , appear_writer               , [term_script]             ,b2scene_novelist                                   ,b3scene_writer       , revealer_novelist         ,rephrase_writer            ,binary_novelist           ,slump_writer             )
agent_artist                =Agent("artist"             ,"y", grade_artist            , effort_artist         , suffer_artist         , action_artist               , appear_artist               , []                        ,None                                               ,b3scene_default      , revealer_artist           ,None                       ,binary_artist             ,slump_artist             )
agent_doctor                =Agent("doctor"             ,"y", grade_doctor            , effort_doctor         , suffer_doctor         , action_doctor               , appear_doctor               , []                        ,b2scene_doctor                                     ,b3scene_doctor       , revealer_doctor           ,None                       ,binary_doctor             ,slump_doctor             )
agent_researcher            =Agent("researcher"         ,"y", grade_researcher        , effort_researcher     , suffer_researcher     , action_researcher           , appear_researcher           , [term_researcher]         ,None                                               ,b3scene_researcher   , revealer_researcher       ,None                       ,binary_researcher         ,slump_researcher         )
agent_actor                 =Agent("actor"              ,"y", grade_actor             , effort_actor          , suffer_actor          , action_actor                , appear_actor                , [term_actor, term_script] ,b2scene_actor                                      ,b3scene_default      , revealer_actor            ,rephrase_actor             ,binary_actor              ,slump_actor              )
agent_chef                  =Agent("chef"               ,"y", grade_chef              , effort_chef           , suffer_chef           , action_chef                 , appear_chef                 , [term_chef]               ,b2scene_chef                                       ,b3scene_default      , revealer_chef             ,rephrase_chef              ,binary_chef               ,slump_chef               )
agent_athlete               =Agent("athlete"            ,"y", grade_athlete           , effort_athlete        , suffer_athlete        , action_athlete              , appear_athlete              , [term_athlete]            ,b2scene_athlete                                    ,b3scene_athlete      , revealer_athlete          ,None                       ,binary_athlete            ,slump_athlete            )
agent_criminal              =Agent("criminal"           ,"y", grade_psycho_criminal   , None                  , None                  , action_psycho_criminal      , appear_psycho_criminal      , []                        ,None                                               ,b3scene_criminal     , revealer_criminal         ,rephrase_criminal          ,binary_psycho_criminal    ,slump_criminal           )
agent_examinee              =Agent("examinee"           ,"y", grade_university        , effort_examinee       , suffer_examinee       , None                        , None                        , []                        ,None                                               ,None                 , None                      ,None                       ,binary_examinee           ,slump_examinee           )
agent_gambler               =Agent("gambler"            ,"y", grade_gambler           , effort_gambler        , suffer_gambler        , action_gambler              , appear_gambler              , [term_gambler]            ,None                                               ,b3scene_gambler      , revealer_gambler          ,None                       ,binary_gambler            ,slump_gambler            )
agent_progamer              =Agent("progamer"           ,"y", grade_progamer          , effort_progamer       , suffer_progamer       , action_progamer             , appear_progamer             , [term_progamer]           ,b2scene_progamer                                   ,b3scene_default      , revealer_progamer         ,rephrase_progamer          ,binary_progamer           ,slump_progamer           )
agent_teacher               =Agent("teacher"            ,"y", grade_teacher           , effort_teacher        , suffer_teacher        , action_teacher              , appear_teacher              , [term_teacher]            ,b2scene_teacher                                    ,b3scene_default      , revealer_teacher          ,None                       ,binary_teacher            ,slump_teacher            )
agent_farmer                =Agent("farmer"             ,"y", grade_farmer            , effort_farmer         , suffer_farmer         , action_farmer               , appear_farmer               , []                        ,b2scene_farmer                                     ,None                 , revealer_farmer           ,None                       ,binary_farmer             ,None                     )
agent_director              =Agent("director"           ,"y", grade_director          , effort_director       , suffer_director       , action_director             , appear_director             , []                        ,b2scene_director                                   ,None                 , revealer_director         ,rephrase_director          ,binary_director           ,None                     )
agent_model                 =Agent("model"              ,"y", grade_model             , effort_model          , suffer_model          , action_model                , appear_model                , []                        ,b2scene_model                                      ,None                 , revealer_model            ,rephrase_model             ,binary_model              ,None                     )
agent_guard                 =Agent("guard"              ,"y", grade_guard             , effort_guard          , suffer_guard          , action_guard                , appear_guard                , []                        ,b2scene_guard                                      ,b3scene_guard        , revealer_guard            ,rephrase_guard             ,binary_guard              ,None                     )
#
#agent_old                   =Agent("old"        ,"", None, None, None, None, None,None, b3scene_old         , None, None, None, None, None, [state_inst.state_old]                              ,[])
#agent_unhappy               =Agent("unhappy"    ,"", None, None, None, None, None,None, b3scene_unhappy     , None, None, None, None, None, [state_inst.state_poor, state_inst.state_unlucky]   ,[])
#agent_unhealthy             =Agent("unhealthy"  ,"", None, None, None, None, None,None, b3scene_unhealthy   , None, None, None, None, None, [state_inst.state_unhealthy]                        ,[])
#agent_illiteracy            =Agent("illiteracy" ,"", None, None, None, None, None,None, b3scene_illiteracy  , None, None, None, None, None, [state_inst.state_illiteracy]                       ,[])
#agent_fat                   =Agent("fat"        ,"", None, None, None, None, None,None, b3scene_fat         , None, None, None, None, None, [state_inst.state_fat]                              ,[])
#agent_pedophilia            =Agent("pedophilia" ,"", None, None, None, None, None,None, b3scene_pedophilia  , None, None, None, None, None, [state_inst.state_pedophilia]                       ,[])
############################################################################################################
#


