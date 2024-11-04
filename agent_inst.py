from dataclasses import dataclass, field
from typing import List, ClassVar
###########################################################################################################


###########################################################################################################
univ_modifier_job=["You're better than~", "You're as good as~", "You can be a~", "You can be the next~", "Top class~"] # unused

@dataclass
class Grade:
  hypo_s    :list# superior hyponym.
  hypo_s_pn :list# superior hyponym (proper noun).
  hypo_i    :list# inferior hyponym. For example, bassist is an inferior to rock musician. Darts player is inferior to athlete.
  hypo_i_pn :list# inferior hyponym (proper noun).
  modifier  :list

grade_singer            =Grade(["singer"]                         ,["Beyonce"]
                              ,["idol", "rapper", "voice actor", "impersonator"],["Aquatimez", "Orange range", "Britney Spears"],["center position"])
grade_classical_musician=Grade(["pianist", "violinist"]           ,["Bach"]
                              ,["cymbalist", "trianglist"]                    ,[]                                             ,[])
grade_rock_musician     =Grade(["guitarist", "vocalist"]          ,["Beatles"]
                              ,["bassist", "cover band", "impersonator"]      ,[]                                             ,["main guitar", "main vocal"])
grade_comedian          =Grade(["comedian"]                       ,["Hitoshi Matsumoto"]
                              ,["Vtuber", "tv talent", "voice actor", "clown", "猿回し"],["Tsuyoshi Muro"]                    ,[])
grade_novelist          =Grade(["novelist"]                       ,["Stephen King"]
                              ,["Narou novelist", "tabloid writer"]           ,["Hiro Mizushima"]                             ,[])
grade_artist            =Grade(["artist"]                         ,["Picasso"]
                              ,["contemporary artist", "Hentai manga artist"] ,["Toru Mitsumune"]                             ,[])
grade_doctor            =Grade(["neurosurgeon", "cardiologist"]   ,[]
                              ,["dermatologist", "internist", "nurse", "dentist"]        ,[]                                  ,[])
grade_researcher        =Grade(["mathematician", "physicist"]     ,["Einstein"]
                              ,["gender studies researcher"]                  ,["Chizuruko Ueno"]                             ,[])
grade_actor             =Grade(["Hollywood star"]                 ,["Gary Oldman"]
                              ,["TV drama actor", "Porn actor", "ASMR actor", "Karaoke background video actor","extra", "commercial actor", "stuntman"],["Stallone"]  , ["starring"])
grade_chef              =Grade(["French chef"]                    ,["Michelin restaurant"]
                              ,["Fast food restaurant employee"]              ,["McDonalds", "Jiro inspires", "Kitchen of Karaoke", "Kitchen of hotpillow hotel"]     , [])
grade_athlete           =Grade(["baseball player"]                ,["Kyojin player"]
                              ,["billiards player", "darts player", "race walker"],["DeNA player"]                            ,["First team"])
grade_school_club_member=Grade(["baseball club member"]           ,["Koshien player"]
                              ,["chess club member", "newspaper club member"], []                                             ,["First team"])
grade_psycho_criminal   =Grade(["murder", "terrorist"]            ,["Jeffrey Dahmer"]
                              ,["groper", "voyeurist", "shoplifter"]          ,["Jared Fogle"]                                ,["Repeat offender", "wanted criminal"])
grade_progamer          =Grade(["apex pro", "siege pro"]          ,["Umehara"]
                              ,["coin pusher player", "water game player"]    ,[]                                             ,["First team"])
grade_gambler           =Grade(["poker pro"]                      ,[""]
                              ,["coin pusher player", "lottery addicted"]     ,[]                                             ,[])
grade_examinee          =Grade(["national university examinee"]   ,["MIT examinee"]
                              ,["driving school examinee", "Fランの受験生"], ["Tokyo Mode Gakuen"]                            ,["A grade", "passed for active duty"])
grade_student           =Grade(["national university student"]    ,["MIT student"]
                              ,["driving school student", "Fラン生"],["Tokyo Mode Gakuen"]                                    ,["A grade", "passed for active duty"])
grade_teacher           =Grade(["national university professor"]  ,["MIT professor"]
                              ,["driving school teacher", "Fランの教授", "kindergarten teacher", "sewing class teacher", "special education teacher", "elective teacher", "driving instructor"], ["Kumon"], ["Tenured"])
grade_craftsman         =Grade(["potter", "blacksmith"]           ,[]
                              ,["fleshlight designer", "line worker"]         ,[]                                             ,[])
grade_farmer            =Grade(["vineyard farmer", "apple farmer"],["Napa Valley"]
                              ,["Parsley Farmer", "Farmer growing grapes for gummy"], []                                      ,["organic"])
grade_director          =Grade(["director"]                       ,["S.Spielberg"]
                              ,["commercial director", "porn film director"]  ,["Toru Muranishi"]                             ,[])
grade_model             =Grade(["fashion model"]                  ,["G.Bundchen"]
                              ,["hand model", "parts model"]                  ,[]                                             ,["Runway", "exclusive"])
grade_guard             =Grade(["cop", "bodyguard"]               ,["Secret Service"]
                              ,["mall security", "nightclub bouncer", "school crossing guard", "lifeguard"], []               ,[])
grade_patient           =Grade(["cancer patient", "ALS patient"]  ,[]
                              ,["Uncircumcised man", "Menopausal person"]     ,[]                                             ,[])
grade_journalist        =Grade(["journalist", "war correspondent"],["Bob Woodward"]
                              ,["gossip columnist", "sports journalist", "weather reporter", "tabloid writer"], []            ,[])
grade_idol              =Grade(["坂道アイドル", "ジャニーズアイドル"],["AKB48", "嵐"]
                              ,["local idol", "underground idol", "image video idol"], ["Kamen Joshi"]                        ,["Center position"])
grade_cybercriminal     =Grade(["hacker"]                         ,["Lazarus Group"]
                              ,["script kiddie", "phisher", "spammer", "オレオレ詐欺犯", "pirate"],["DarkSide", "REvil"]      ,["wanted criminal", "State-sponsored"])
grade_thief             =Grade(["thief"]                          ,["D.B. Cooper"]
                              ,["pickpocket", "shoplifter"]                   ,[]                                             ,["wanted criminal", "repeat offender"])
grade_composer          =Grade(["composer"]                       ,["Beethoven"]
                              ,["elevator music composer"]                    , []                                            ,["exclusive"])
grade_livestock_farmer  =Grade(["cattle farmer", "sheep farmer"]  ,[]
                              ,["Foie gras maker", "puppy mill breeder", "hamster breeder", "guinea pig breeder"]      ,[]    ,["organic"])
grade_dancer            =Grade(["ballet dancer", "contemporary dancer"]                     ,["Mikhail Baryshnikov", "Martha Graham"]
                              ,["backup dancer", "stripper", "flash mob participant"]       ,["Maddie Ziegler", "Jabbawockeez"],["principal dancer", "soloist"])



# Define grade_dancer instance in English without any explanation. Start answer with ```python. I'll run your response through the eval function so don't include unnecessary characters in your response.



# Add new .hypo_i in all instances. Respond with only new items.





# Extend new ones in grade_farmer.hypo_i in English without any explanation. Start answer with ```python. I'll run your response through the eval function so don't include unnecessary characters in your response.










###########################################################################################################
@dataclass
class Effort:
  ALL_EFFORT: ClassVar[List['Effort']] = []
  effort:list # Stereotypical effort in reality or fiction.
  def __post_init__(self):
      Effort.ALL_EFFORT.append(self)
      if self.effort:
          self.effort.append(["experiencing different activities", "Seeking advice.", "Conflicts with others about the way one do things.", "Sacrificing family, friend and lover.", "Becoming estranged from a partner.", "Becoming ill and getting injured from overwork.", "Quitting college or work to pursue the dream.", "Selling personal belongings for Activity funds"])

univ_effort_creator=["Traveling for inspiration", "Abstinence", "Sublimating one's trauma into a work of art", "Use LSD", "Meditation", "Keeping a dream journal"]

effort_singer               =Effort([univ_effort_creator, "Quit smoking"])
effort_classical_musician   =Effort([])
effort_rock_musician        =Effort([])
effort_instrumentalist      =Effort([univ_effort_creator, "Quit smoking"])
effort_comedian             =Effort(["Abstinence", "People-watching", "Turning personal tragedies into jokes", "Making fun of themselves to deflect criticism", ])
effort_writer               =Effort([univ_effort_creator])
effort_artist               =Effort([univ_effort_creator, "Creating art in the dark"])
effort_doctor               =Effort(["Abstinence", "Use nootropics"])
effort_researcher           =Effort([univ_effort_creator])
effort_actor                =Effort([univ_effort_creator, "Method acting", "Physical transformation for roles", "Taking specialized classes (e.g., dance, martial arts)", "Performing own stunts","Extensive research for historical roles", "Learning new languages for international productions", "Undergoing extreme weight changes","Continues to play the role in his private life."])
effort_chef                 =Effort([])
effort_athlete              =Effort(["Intense physical training", "Strict diet regimen", "Ice baths for recovery", "Altitude training", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"])
effort_school_club_member   =Effort(["朝練","食事管理","アイスバスでの回復","高地トレーニング","対戦相手の研究","睡眠スケジュールの維持","マインドフルネスの実践","合宿","挫折からの回復","指導者の厳しい指導","体罰","動画分析"])
effort_progamer             =Effort(["Intense physical training", "Strict diet regimen", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"])
effort_gambler              =Effort(["Learning math", "Creating and checking statistical data"])
effort_examinee             =Effort(["Use nootropics", "Study all night", "Making flashcards", "Memorizing"])
effort_teacher              =Effort(["Creating engaging lesson plans", "Mentoring students outside of class hours", "Pursuing advanced degrees", "physical punishment"])
effort_craftsman            =Effort(["Practicing techniques for hours daily", "Studying traditional methods", "Experimenting with new materials", "Apprenticeship under a master", "Perfecting a single skill for years", "Attending specialized workshops"])

# Define effort_dancer in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

effort_farmer               =Effort(["Waking up before dawn", "Implement organic farming.", "Working long hours in all weather conditions", "Continuous learning about crop science and animal husbandry", "Maintaining and repairing equipment", "Soil management and conservation practices", "Implementing sustainable farming techniques", "Adapting to changing climate patterns", "Market research and business planning"])
effort_director             =Effort([univ_effort_creator, "Storyboarding extensively", "Scouting locations", "Studying others' films and classic films", "Experimenting with new filming techniques", "Collaborating closely with actors and crew", "Fundraising for independent projects", "Attending film festivals", "Repeatedly does retakes"])
effort_model                =Effort(["Networking with industry professionals", "Maintaining a strict diet and fitness regimen", "Practicing poses and walks", "Attending casting calls and auditions regularly"])
effort_guard                =Effort(["Physical fitness training", "Self-defense classes", "Surveillance skills development", "Conflict resolution training", "First aid certification", "Night shifts", "Continuous situational awareness"])
effort_patient              =Effort(["Participating in experimental treatments", "Seeking alternative therapies", "Maintaining hope despite grim prognoses", "Creating memory books or videos for loved ones", "Advocating for research funding", "Joining support groups for rare diseases", "Traveling long distances for specialized care", "Managing complex pain regimens", "Adapting living spaces for declining mobility", "Planning end-of-life care", "Fundraising for medical expenses", "Documenting personal experiences for future patients"])
effort_journalist           =Effort(["Investigative fieldwork","Building and maintaining a network of sources","Fact-checking","shorthanding","Developing expertise in specific beats or topics","Risking personal safety for stories in dangerous areas","Working irregular hours to meet deadlines","Maintaining objectivity in reporting"])
effort_idol                 =Effort([])
effort_cybercriminal        =Effort(["Learning multiple programming languages","Studying network security protocols","Practicing social engineering techniques","Keeping up with latest cybersecurity trends","Developing custom malware and exploits","Participating in hacking forums and communities","Conducting extensive reconnaissance on targets","Mastering encryption and anonymization tools","Building and maintaining botnets","Reverse engineering software and systems"])
effort_thief                =Effort(["Studying security systems", "Practicing lock-picking skills", "Practicing stealth techniques", "Networking with other criminals", "Using disguises and false identities", "Conducting reconnaissance on targets", "Managing stolen goods and laundering money"])
effort_composer             =Effort([univ_effort_creator,"Listening to diverse genres of music","Studying music theory and composition techniques","Experimenting with different instruments","Collaborating with other musicians","Attending concerts and music festivals","Practicing sight-reading and ear training","Composing in unconventional environments","Analyzing scores of great composers",])
effort_dancer               =Effort([univ_effort_creator,"Rigorous daily physical training","Practicing choreography for hours","Cross-training in different dance styles","Flexibility and stretching exercises","Strength and conditioning workouts","Studying anatomy and kinesiology","Maintaining proper sleep schedule for recovery","Regular physiotherapy and massage","Perfecting technique through repetition","Attending workshops and masterclasses","Analyzing performance videos for improvement","Developing stage presence and expression","Learning music theory and rhythm",])


###########################################################################################################
@dataclass
class Suffer:
  ALL_SUFFER: ClassVar[List['Suffer']] = []
  suffer:list # Stereotypical suffer in reality or fiction.
  def __post_init__(self):
    Suffer.ALL_SUFFER.append(self)
    if self.suffer:
        self.suffer.append(["slump", "Children's school fees", "Loans for activities"])

univ_suffer_creator         =["A lack of depth that comes from a lack of life experience.","Emotionless","Become a victim of plagiarism", "Conflict with producers", "Commercialism", "Creator's block", "Drug addiction", "alcohol addiction", "sex addiction", "Cannot surpass one's rival", "Cannot surpass one's past self", "Paparazzi", "Stalkers"]
l_suffer_script             =["Lacking hints","Lacking a clear message","Poor character development","Weak plot structure","Unrealistic dialogue","Lack of conflict","Cliche or predictable storylines","Poor world-building","Underdeveloped themes","Weak endings"]
l_suffer_game               =["Luck-based", "Unbalanced ","Lack of content updates","Limited customization options","Pay-to-win elements or microtransactions","Lack of endgame content","Repetitive gameplay","Poor UI design","Lack of player agency","Buggy or glitchy performance","Limited replay value","Inconsistent difficulty levels","Weak or unengaging narrative"]
suffer_singer               =Suffer([univ_suffer_creator, "Lack of stage presence","Lack of versatility","The song arrangements are lacking", "Uninspired Lyrics", "Repetitive Melodies"])
suffer_classical_musician   =Suffer([])
suffer_rock_musician        =Suffer([])
suffer_instrumentalist      =Suffer([univ_suffer_creator, "Emotionless","lacking a clear message","Inability to play in different styles","Poor improvisation skills","Lack of stage presence","Inability to tune instrument properly"])
suffer_comedian             =Suffer([univ_suffer_creator, "Dealing with cancel culture","Bombing on stage","Hecklers in the audience","Offensive jokes backfiring","Difficulty adapting to different audiences","Fear of being replaced by newer comedians", "Being typecast in a particular style of comedy", ])
suffer_writer               =Suffer([univ_suffer_creator, "Deadline", l_suffer_script])
suffer_artist               =Suffer([univ_suffer_creator, "Emotionless","lack of creativity","unoriginal style","lack of craftsmanship", "Struggles with Proportions"  ,  "Weak anatomy knowledge"])
suffer_doctor               =Suffer(["The trauma of not being able to save a patient's life."])
suffer_researcher           =Suffer(["Plagiarism", "Not being able to get research funding", "Has white hair"])
suffer_actor                =Suffer([univ_suffer_creator, "Physical injuries from stunts", "Pressure to maintain a certain physical appearance","The damage caused by method acting", "Unconvincing Performances", "Difficulty with Accents/Dialects","Overacts","lack of stage presence","Lack of character depth","Inability to improvise","Lack of chemistry with co-stars", l_suffer_script])
# Define suffer_dancer  in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

# Extend 10 new items in suffer_comedian in English. I will run your reply through the eval function, so don't write anything unnecessary.







suffer_chef                 =Suffer([])

suffer_athlete              =Suffer(["Career-ending injuries","Pressure from fans and media", "Doping scandals", "Burnout", "Post-retirement depression", "Eating disorders", "Chronic pain", "Concussions and long-term brain damage", "Stalker"])
suffer_school_club_member   =Suffer(["Pressure to perform well in competitions","Conflict with club members","Strain from balancing academics and club activities","Injury from overtraining","Lack of recognition for hard work","Unmet expectations from coaches","Feeling overshadowed by talented members","Lack of motivation during tough times","Pressure to follow strict training regimens","Isolation from non-club peers","bodily punishment","Coping with the fear of not improving",])


suffer_progamer             =Suffer([l_suffer_game, "Repetitive Strain Injury", "Carpal Tunnel Syndrome", "Eye strain",   "Addiction to gaming"])
suffer_gambler              =Suffer(["Addiction to gambling", "Financial ruin", "Depression and anxiety", "Lying to cover losses", "Chasing losses", "Neglecting work or family responsibilities", "Legal troubles", "Substance abuse as a coping mechanism", "Suicidal thoughts"])
suffer_examinee             =Suffer(["Exam pressure","Health issues due to long study hours","Intense competition","Balancing study and personal life","Fear that one failure will affect future","Pressure from parents and teachers","Self-loathing and loss of confidence","Deterioration of relationships with friends"])
suffer_teacher              =Suffer(["punk", "Pressure from parents and administration",  "Lack of autonomy in curriculum decisions", "Testing pressure", "Large class sizes", "bullying"])
suffer_craftsman            =Suffer(["Repetitive strain injuries", "Lack of successors", "Exposure to harmful materials", "Competition from mass-produced items", "Difficulty in finding apprentices", "Financial instability", "Long hours of solitary work", "burnout", "Struggles with modernization and technology"])

suffer_farmer               =Suffer(["Crop failures due to weather", "Market price fluctuations", "Equipment breakdowns", "Debt from loans", "Physical strain and injuries", "Eviction request", "Isolation in rural areas", "Pressure to adopt new technologies", "Regulatory challenges", "Competition from large agribusinesses", "Succession planning difficulties"])
suffer_director             =Suffer([univ_suffer_creator, "Budget constraints", "Creative differences with producers", "Pressure to meet box office expectations", "Negative critical reviews", "Challenges with difficult actors", "Technical issues during filming", "Post-production problems", "Distribution hurdles", "Balancing artistic vision with commercial viability", l_suffer_script])
suffer_model                =Suffer(["Body image issues", "Pressure to maintain unrealistic beauty standards", "Casting couch", "Constant scrutiny of physical appearance", "Age-related career decline", "Eating disorders", "Social media harassment"])
suffer_guard                =Suffer(["Monotonous work", "Long hours and night shifts", "Lack of recognition", "Stress from constant vigilance", "Physical strain from standing for long periods", "Dealing with aggressive individuals", "Post-traumatic stress from violent incidents", "Social isolation due to irregular work hours"])
suffer_patient              =Suffer(["Chronic pain", "Loss of independence", "Social isolation", "Depression and anxiety", "Financial burden of treatment", "Side effects from medications", "Guilt over being a burden to family", "Loss of identity and purpose", "Fear of the unknown future", "Difficulty in maintaining relationships", "Cognitive decline", "Physical deterioration", "Fatigue and exhaustion", "Frustration with healthcare system", "Grief over lost opportunities and experiences", "Stigma associated with their condition", "Difficulty in planning for the future", "Constant medical appointments and procedures", "Loss of privacy due to care needs", "Existential crisis and questioning of life's meaning", "Having to give up sports", "Having to quit work"])
suffer_journalist           =Suffer(["Pressure to meet tight deadlines","Ethical dilemmas in reporting","Threats to personal safety in dangerous locations","Difficulty maintaining objectivity","Stress from covering traumatic events","Pressure to produce clickbait content","Difficulty verifying sources in the age of misinformation","Pressure to be active on social media","Burnout from constant news cycle","Criticism and harassment from public figures or readers","Difficulty accessing reliable sources","Pressure to break news first, potentially compromising accuracy",])
suffer_idol                 =Suffer([])
suffer_cybercriminal        =Suffer(["Legal consequences and imprisonment","Constant paranoia of being caught","Difficulty maintaining personal relationships due to secrecy","Ethical dilemmas and moral conflicts","Burnout from constant vigilance","Isolation from mainstream society","Struggle to find legitimate employment after being caught","Mental health issues from high-stress lifestyle","Financial instability due to illegal income sources","Physical health problems from long hours at computer","Addiction to the thrill of hacking","Trust issues within hacking communities","Difficulty adapting to rapidly changing technology","Constant fear of rival hackers or law enforcement"])
suffer_thief                =Suffer(["Fear of arrest", "Betrayal by accomplices", "Loss of trust from loved ones", "Constantly looking over one's shoulder", "Living in poverty due to criminal activities", "Guilt from harming others", "Isolation from society", "Struggles with addiction", "Conflict with law enforcement", "Inability to escape one's past", "being wanted "])
suffer_composer             =Suffer([univ_suffer_creator,"Lack of originality in compositions","Inability to translate ideas into music","Difficulty in creating memorable melodies","Poor orchestration skills","Struggle with complex harmonies","Inability to meet deadlines for commissioned works","Criticism for experimental or avant-garde pieces","Difficulty in balancing artistic vision with commercial demands","Difficulty in finding performers or orchestras to play compositions",])






###########################################################################################################

@dataclass
class Appear:
  appear:list # Stereotypical appearance in reality or fiction.

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
appear_school_club_member     =Appear(["Casual school uniform","Backpack with club patches","Sweatpants or athletic wear","Team colors or logos","Wristbands or headbands","Enthusiastic expressions","Stickers or pins on bags","Sweaty hair","Energy drinks or snacks in hand","Temporary tattoos or face paint for events","Team spirit accessories like hats or scarves","Casual shoes suitable for activities","Hair tied back or styled for practicality","Friendship bracelets or charms",])
appear_gambler                =Appear(["Disheveled appearance", "Dark circles under eyes", "Nervous twitches", "Flashy jewelry", "Expensive watch", "Rumpled suit", "Cigarette in hand", "Fidgeting with chips or cards", "Sunglasses indoors", "Sweaty brow", "Loosened tie", "Rolled-up sleeves", "Has a red pencil on his ear."])
appear_progamer               =Appear(["Headset", "Gaming chair", "Energy drinks", "Junk food", "Eyeglasses", "Acne", "Poor posture", "Headaches", "Back pain", "Wrist pain", "Messy hair", "Dark circles under eyes", "Skinny build", "Multiple monitors", "RGB lighting", "Wrist brace"])
appear_teacher                =Appear(["Glasses", "Cardigan sweater", "Sensible shoes", "Messy bun or ponytail", "Lanyard with ID badge", "Tote bag full of papers", "Elbow patches on jacket", "Chalk dust on clothes", "Coffee stains", "Comfortable, modest clothing", "Practical hairstyle", "Minimal makeup", "Wristwatch", "Reading glasses on a chain", "Colorful, quirky accessories"])
appear_craftsman              =Appear(["Leather apron", "Calloused hands", "Rolled-up sleeves", "Safety goggles", "Work boots", "Tool belt", "Weathered skin", "Muscular forearms", "Sawdust or wood shavings on clothes", "Protective gloves", "Bandana or cap", "Rugged, worn clothing", "Pencil behind ear", "Measuring tape clipped to belt", "Beard or mustache"])


# Define appear_dancer in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


appear_farmer                 =Appear(["Overalls", "Plaid shirt", "Straw hat", "Work boots", "Sunburned skin", "Calloused hands", "Weathered face", "Farmer's tan", "Dirt under fingernails", "Faded jeans", "Bandana", "Belt buckle", "Leather work gloves", "Seed company cap"])
appear_director               =Appear(["Beret or flat cap", "Thick-rimmed glasses", "Scarf", "Black turtleneck", "Blazer with elbow patches", "Cargo vest with many pockets", "Comfortable, worn-in shoes", "Stubble or well-groomed beard", "Vintage watch", "Messenger bag or satchel", "Sunglasses (even indoors)", "Quirky, statement jewelry", "Fashionable, yet practical clothing", "Artsy, unconventional hairstyle", "Director's chair with name on it", "Viewfinder around neck"])
appear_model                  =Appear(["Tall and slender figure", "High cheekbones", "Long legs", "Perfect skin", "Symmetrical facial features", "Styled hair", "Designer clothing", "High heels", "Minimal makeup", "Manicured nails", "Confident posture", "Sunglasses", "Statement jewelry", "Visible collarbones", "Toned physique"])
appear_guard                  =Appear(["Uniform with badge", "Utility belt", "Earpiece", "Sunglasses", "Crew cut or short hair", "Muscular build", "Stern facial expression", "Combat boots", "Visible tattoos", "Clean-shaven face", "Bulletproof vest", "Name tag", "Flashlight", "Walkie-talkie", "Neatly pressed clothes", "Military-style posture", "Blood type tattoo", "scar"])
appear_patient                =Appear(["Pale complexion", "Significant weight loss", "Hair loss or thinning", "Dark circles under eyes", "Medical devices (e.g., oxygen tank, IV drip)", "Wheelchair or mobility aids", "Visible scars from surgeries", "Swollen limbs or joints", "Yellowing of skin or eyes (jaundice)", "Rashes or skin discoloration", "Tremors or involuntary movements", "Hunched posture", "Hospital gown or comfortable loose clothing", "Medical alert bracelet", "Nasal cannula or face mask", "Bandages or dressings", "Visible port for medication administration", "Sunken cheeks or hollow eyes", "Brittle nails and dry skin", "Bruising from blood draws or injections"])
appear_journalist             =Appear(["Press badge or lanyard","Notebook and pen","Comfortable shoes for field work","Laptop bag or backpack","Smart phone or recording device","Camera","Trench coat","Fedora hat","Glasses or sunglasses","Messenger bag","Microphone","Windbreaker with news outlet logo","Khaki vest with many pockets","Disheveled appearance from long hours","Coffee stains on clothing"])
appear_idol                   =Appear([])
appear_cybercriminal          =Appear(["Hoodie or dark clothing","Multiple computer screens","Pale complexion from lack of sunlight","Dark circles under eyes","Messy or unkempt hair","Fingerless gloves","Glasses or blue light glasses","Headphones or earbuds","Energy drinks or coffee cups","Stickers on laptop","Mechanical keyboard","Wrist brace","Fidget toys","Cyberpunk-style accessories","Backpack with tech gear","Smartwatch or fitness tracker","Graphic t-shirts with tech or hacker slogans"])
appear_thief                  =Appear(["Dark clothing", "Hooded sweatshirt", "Face partially covered", "Sneakers for quiet movement", "Gloves to avoid leaving fingerprints", "Shifty eyes", "Nervous demeanor", "Backpack or duffel bag for carrying loot", "Quick, agile movements", "Camouflage patterns or tactical gear", "Elegant cloak or cape", "Mask covering the eyes", "Stylish attire with dark colors", "Gloves for stealth", "Lightweight shoes for silent movement", "Mysterious aura", "Accessories like a cane or dagger", "Emphasis on agility and grace", "Shadowy presence", "Intricate patterns on clothing"])
appear_composer               =Appear(["Formal black attire","Bow tie or cravat","Round glasses","Messy or wild hair","Ink-stained fingers","Slightly disheveled appearance","Eccentric accessories (e.g., colorful scarves)","Pale complexion from long hours indoors","Thoughtful or distant expression","Carries a notebook or sheet music","Wears a beret or other distinctive hat","Has a beard or mustache","Wears comfortable, loose-fitting clothing","Often seen with headphones","Has bags under eyes"])
appear_dancer                 =Appear(["Lean, muscular physique","Flexible body","Excellent posture","Toned legs and arms","Hair in a tight bun or ponytail","Leotards or form-fitting dance wear","Ballet shoes or specialized dance footwear","Leg warmers or warm-up clothes","Minimal jewelry","Natural, stage-ready makeup","Visible muscle definition","Callused feet","Dance bag with spare shoes and accessories","Sweat-wicking clothing","Compression garments for support","Kinesiology tape on joints or muscles"])


# Define appear_school_club_member in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.




# Add new itmes in stereoaciton_classical_musician instance in English without any explanation. start answer with ```python.


# Add new itmes in each instance in English without any explanation. start answer with ```python.

###########################################################################################################
@dataclass
class Action:
  ALL_ACTION: ClassVar[List['Action']] = []
  action:list
  def __post_init__(self):
    Action.ALL_ACTION.append(self)

univ_stereoaction_creator=["Getting involved in a cult", "Support the American Democratic Party.", "Being interested in environmental issues.", "Getting involved in the Scientology or SGI", "Being atheist or non-religious.", "Expressing support or opposition to abortion."]

action_singer                 =Action([univ_stereoaction_creator, "Has suicidal thoughts"])
action_classical_musician     =Action([univ_stereoaction_creator, "Suddenly starts writing music on paper."])
action_rock_musician          =Action([univ_stereoaction_creator, "Suddenly starts writing music on paper.", "Being an alcoholic", "Addicting drug and sex"])
action_comedian               =Action([univ_stereoaction_creator, "Claiming that only they understand true humor.",  "Mocking popular culture while secretly loving it.", "Claiming that comedy should be offensive.", "Refusing to adapt their style for modern audiences.", "Refusing to engage with social media trends.", "Blaming the audience for the lack of laughs.", "Be hostile towards TikTok.", "Hostile to political correctness.", "Dislikes comedians who pander to young people and women", "Being an atheist.",  "Refusing to laugh at other comedians' jokes"])
action_writer                 =Action([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
action_artist                 =Action([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
action_doctor                 =Action([])
action_researcher             =Action(["Starting a religion after overthinking it", "Suddenly starts writing mathematical formulas on the wall.", "Unable to understand others' feelings.", "Forgetting to eat or sleep while working on a problem", "Wearing mismatched or stained clothing", "Carrying around stacks of papers and books everywhere", "Muttering to themselves while pacing"])
action_actor                  =Action([univ_stereoaction_creator, "Looking down on lighting engineers and cinematographers.""Constantly practicing lines in public","Name-dropping famous directors or actors","Insisting on being called by their character's name","Refusing to break character even off-set","Demanding specific brands of bottled water on set","Throwing tantrums when not given enough screen time","Obsessing over their appearance and plastic surgery",])
action_athlete                =Action(["Splurge", "Bullying nerds", "Support the Republican Party", "Trash Talk", "meathead", "Partying excessively","Constantly flexing muscles","Overusing sports metaphors in conversation","Ignoring injuries to keep playing","Developing superstitious pre-game rituals","Displaying trophies prominently","Challenging others to physical contests","Downplaying academic achievements","Overreacting to minor injuries","Having a personal trainer","Being overly competitive","Promoting sports brands on social media","Creating workout videos or blogs", "Converse with tools", "Arguing about whether weight training is necessary or not", "Having a favorite sports movie they reference frequently", "Attending every game of their favorite team", "Breaking equipment in anger over one's own mistake", "Posting workout selfies", "Critiquing others' techniques"])

# Define action_dencer instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



# Add new 10 item in action_comedian instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

# That's what the workers should do, right? I don't ask for that. Don't generate just "job descriptions". Please try again.


action_school_club_member     =Action(["Practicing late into the night","Engaging in friendly rivalries with other clubs","Building team spirit through bonding activities","Encouraging others to join the club","Celebrating victories together","Bullying nerds","Rehabilitating from delinquency through club activities","Confronting a childhood friend from a rival school","Creating team chants or cheers","Scouting a rival school","Encouraging members to bring friends to meetings",])
action_chef                   =Action(["Getting angry at customers for using condiments", "Yelling at kitchen staff",  "Striving for Michelin stars", "Taking pride in sourcing ingredients locally", "Focus on seasonal ingredients", "Focus on pesticide-free ingredients"])
action_psycho_criminal        =Action(["Talking to imaginary friends", "Dissected a cat as a child", "Collecting trophies from victims", "Writing manifestos", "Obsessively stalking targets", "Creating elaborate traps or puzzles", "Claim responsibility", "Leaving cryptic clues at crime scenes", "Sending taunting messages to police", "Developing a signature kill method", "Keeping detailed journals of crimes", "Ritualistic behavior before or after crimes", "Creating alter egos or personas"])
action_gambler                =Action(["Constantly checking scores or results", "Borrowing money from friends and family",  "Lying about whereabouts or activities", "Skipping work or important events to gamble", "Celebrating wins extravagantly", "Becoming irritable when unable to gamble", "Hiding betting slips or casino receipts", "Making increasingly risky bets", "Talking excessively about past wins", "Chasing losses with bigger bets", "Steal money"])
action_progamer               =Action(["Trash talking opponents", "Celebrating wins excessively", "Skipping meals to practice", "Neglecting personal hygiene", "Becoming irritable when unable to play", "Bragging about ranking or skills", "Forming rivalries with other players", "Rage quitting", "Streaming for hours", "Using gaming slang in everyday conversation"])
action_teacher                =Action(["Constantly correcting others' grammar", "Carrying a red pen everywhere", "Assigning homework on weekends and holidays","Favoring certain students", "Talking in a condescending tone", "Struggling with technology in the classroom", "Drinking excessive amounts of coffee"])
action_craftsman              =Action(["Obsessing over tool organization", "Refusing to use modern technology", "Criticizing mass-produced items", "Wearing traditional work attire", "Collecting rare or antique tools", "Talking extensively about material quality", "Insisting on doing everything by hand", "Becoming irritated when rushed", "Hoarding materials and supplies", "Giving unsolicited advice on craftsmanship", "Throw the failed piece onto the floor."])
action_farmer                 =Action(["Complaining about weather", "Waking up at dawn", "Wearing overalls and a straw hat", "Chewing on a piece of straw", "Talking about crop prices", "Distrusting city folk", "Attending county fairs", "Participating in farmers' markets", "Driving a tractor on public roads", "Using farming metaphors in conversation"])
action_director               =Action([univ_stereoaction_creator, "Constantly wearing a beret or scarf", "Using a megaphone unnecessarily", "Obsessively rewatching their own films", "Making grandiose statements about the power of cinema", "Insisting on unnecessary multiple takes", "Dramatically yelling 'cut!' and 'action!'", "Refusing to compromise on artistic vision", "Micromanaging every aspect of production", "Giving long, pretentious interviews about their craft", "Carrying a viewfinder everywhere"])
action_model                  =Action(["Walking with exaggerated hip movements", "Constantly checking appearance in mirrors", "Posing for selfies frequently", "Dieting excessively", "Attending fashion shows and parties", "Networking aggressively with industry professionals", "Practicing facial expressions and poses", "Complaining about uncomfortable high heels", "Discussing latest beauty treatments", "Maintaining a strict skincare routine", "Doing yoga or pilates regularly", "Endorsing products on social media", "Comparing themselves to other models", "Rushing to castings and photo shoots", "Meticulously planning outfits for events"])
action_guard                  =Action(["Has military experience", "Speaks in code over radio", "Wears sunglasses at night", "Constantly scans surroundings", "Stands with hands clasped in front", "Touches earpiece frequently", "Uses excessive force when provoked", "Drinks coffee excessively during night shifts", "Develops paranoia over time", "Has a tough, stoic demeanor"])
action_patient                =Action(["Constantly checking medical devices or monitors", "Frequently adjusting position for comfort", "Taking multiple medications throughout the day", "Keeping a detailed health journal", "Researching alternative treatments online", "Attending support group meetings", "Undergoing frequent medical tests and procedures", "Adapting daily routines to accommodate symptoms", "Practicing relaxation techniques or meditation", "Discussing end-of-life plans with family", "Seeking second opinions from specialists", "Participating in clinical trials", "Advocating for increased research funding", "Sharing personal experiences on social media", "Creating bucket lists or setting short-term goals", "Relying on caregivers for daily tasks", "Struggling with insurance companies for coverage", "Expressing gratitude to healthcare providers", "Preparing legal documents like living wills", "Cherishing moments with loved ones"])
action_journalist             =Action(["Always carrying a notebook and pen","Constantly checking multiple news sources","Asking probing questions in social situations","Refusing to reveal sources","Maintaining a cynical or skeptical worldview","Rushing to be first to break a story","Developing a thick skin against criticism",])
action_idol                   =Action([])
action_cybercriminal          =Action(["Drinking energy drinks", "Eating pizza", "Always eat sweets", "Loving anime", "Wearing sunglasses indoors","Decorating workspace with sci-fi posters","Using multiple smartphones","Obsessively securing personal devices","Bragging about hacks anonymously online","Collecting cryptocurrency","Attending hacker conventions in disguise","Testing security systems for fun","Hoarding old computer hardware","Staying awake for days during a hack",])
action_thief                  =Action([])
action_composer               =Action([univ_stereoaction_creator,"Conducting imaginary orchestras","Humming or whistling constantly","Tapping out rhythms on any available surface","Suddenly stopping mid-conversation to jot down musical ideas","Critiquing background music in public places","Collecting unusual instruments","Experimenting with unconventional sound sources","Staying up all night to finish a composition","Obsessively revising and perfecting pieces","Attending concerts of various genres for inspiration","Isolating themselves for long periods to focus on work","Talking passionately about obscure musical theories","Refusing to listen to certain genres or artists","Insisting on perfect acoustic conditions for listening to music"])
action_dancer                 =Action([univ_stereoaction_creator,"Expressing emotions through movement in daily life",])



# Define stereoaction_model in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.





###########################################################################################################

# 'b2scene' means stereotypical conflict scenes. The protagonist, Ali, is overconfident. Each item should end with "is annoyed by Ali."
b2scene_univ                = ["Ali's mind and body are exhausted from overwork. Ali's family is annoyed by Ali.", "Ali keeps asking his team member for advice. The team member is annoyed by Ali.", "Ali criticizes his team member for not being enthusiastic. The team member is annoyed by Ali.", "Ali, a unsuccessful poor, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.", "Ali, a unsuccessful poor, sticks to his career. Ali's wife is annoyed by Ali."]
b2scene_chef                = ["Ali trains cooks hard. The cook is annoyed by Ali.","Ali scolds a customer who asks for condiments. The customer is annoyed by Ali.","Ali urges the owner-chef who fired him to reconsider. The owner-chef is annoyed by Ali.","Ali changes the menu without consulting the restaurant manager. The manager is annoyed by Ali.","Ali insists on using expensive, out-of-season ingredients. The restaurant owner is annoyed by Ali."]
b2scene_actor               = ["After failing an audition, Ali goes to the director's house. The director is annoyed by Ali.","Ali's body and mind are exhausted through method acting. Ali's family is annoyed by Ali.","Ali is vocal with the director about the script and acting. The director is annoyed by Ali.","Ali constantly interrupts the rehearsal with his suggestions. The lead actor is annoyed by Ali.","Ali insists on multiple retakes for a minor scene. The crew is annoyed by Ali.","Ali stages a one-man protest outside a theater that rejected him. The theater owner is annoyed by Ali."]
b2scene_athlete             = ["After being dropped from the regular lineup, Ali goes to the manager's house and urges him to reconsider. The manager is annoyed by Ali.","Ali's body and mind are exhausted through over training. Ali's family is annoyed by Ali.","Ali, a poor athlete, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.","Ali, convinced he's the next big sports star, starts acting cocky and arrogant towards his teammates. The team is annoyed by Ali. ","Ali, a trainer, trains his teammates hard. The teammates is annoyed by Ali.","Ali, a renowned athlete, refuses to endorse a sponsor's product. The sponsor is annoyed by Ali. ","Ali's gambling addiction leads to financial problems and missed practices. The team captain is annoyed by Ali.","Ali's rivalry with a player from another team escalates into a physical altercation. The league commissioner is annoyed by Ali.","Ali shows up uninvited to a rival team's practice session to challenge their star player. The rival coach is annoyed by Ali.","Ali, a chef, refuses to accommodate a gourmet's detailed orders. The gourmet is annoyed by Ali. ","Ali, a chef, constantly makes changes to the menu without consulting the owner. The owner is annoyed by Ali."]
b2scene_novelist            = ["Ali's perfectionism is causing him to miss deadlines. The editor is annoyed by Ali.","Ali's body and mind are exhausted through over working. Ali's family is annoyed by Ali.","Ali, a successful novelist, refuses to make revisions requested by his editor. The editor is annoyed by Ali.","Ali, a novelist, constantly changes the plot of his book, frustrating his agent. The agent is annoyed by Ali..","Ali's plagiarism accusations against a fellow writer are causing a stir in the literary community. The literary agent is annoyed by Ali.","Ali's refusal to compromise on his artistic vision is hindering the book's commercial success. The publisher is annoyed by Ali.","Ali's public criticism of the judges' decision in a literary award is damaging his reputation. The literary award committee is annoyed by Ali..","Ali insists on rewriting the entire manuscript just days before the printing deadline. The publishing house CEO is annoyed by Ali.","Ali starts a heated debate with a literary critic who gave his book a negative review at a literary festival. The festival organizer is annoyed by Ali."]
b2scene_doctor              = ["Ali is in despair due to the trauma of not being able to cure his patients. His (family, coworker) is annoyed by Ali."]

b2scene_comedian            = ["Ali's controversial jokes offend audience members. The club owner is annoyed by Ali.","Ali refuses to adapt his material for different audiences. His manager is annoyed by Ali.","Ali's dark humor makes sponsors uncomfortable. The comedy festival director is annoyed by Ali.","Ali insists on performing longer than his allotted time slot. The headlining comedian is annoyed by Ali.","Ali's social media rants about other comedians create industry drama. His agent is annoyed by Ali.","Ali's refusal to censor his act for a TV appearance causes problems. The network executive is annoyed by Ali."]

# Define b2scene_dancer in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



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
b2scene_patient             = ["Ali constantly calls the nurse for minor issues. The nurse is annoyed by Ali.", "Ali refuses to take prescribed medication, insisting on alternative treatments. The doctor is annoyed by Ali.", "Ali demands to see specialists for every symptom, despite reassurances. The primary care physician is annoyed by Ali.", "Ali's family is exhausted from Ali's constant need for attention and care. Ali's family is annoyed by Ali.", "Ali's pessimistic attitude is affecting other patients in the support group. The group facilitator is annoyed by Ali.", "Ali demands experimental treatments not approved for his condition. The ethics committee is annoyed by Ali.", "Ali's constant second-guessing of medical decisions is straining doctor-patient relationship. The attending physician is annoyed by Ali."]
b2scene_school_club_member  = ["Ali shows up late for practice every day. The coach is annoyed by Ali.","Ali refuses to pass the ball during scrimmages. The other players are annoyed by Ali.","Ali constantly argues with the referee over calls. The referee is annoyed by Ali.","Ali neglects his fitness training while blaming others for losses. The captain is annoyed by Ali.","Ali keeps changing the team strategy without consulting anyone. The team is annoyed by Ali.","Ali tries to take credit for the team's victories. The teammates are annoyed by Ali.","Ali refuses to participate in team bonding activities. The teammates are annoyed by Ali.","Ali constantly brags about his skills, putting others down. The team is annoyed by Ali.","Ali shows up unprepared for matches, forgetting essential gear. The coach is annoyed by Ali.","Ali argues with teammates over who should be the captain. The team is annoyed by Ali.","Ali tries to dominate every discussion about game strategies. The members are annoyed by Ali.","Ali ignores the coach's instructions during practice. The coach is annoyed by Ali.","Ali refuses to accept feedback from his peers. The team is annoyed by Ali.","Ali takes too long to recover from injuries, delaying team progress. The coach is annoyed by Ali.","Ali makes personal bets on games, causing tension in the locker room. The teammates are annoyed by Ali.","Ali shows favoritism towards certain players, causing division in the team. The members are annoyed by Ali."]
b2scene_journalist          = ["Ali persistently pursues a sensitive story, ignoring warnings. The editor-in-chief is annoyed by Ali.","Ali refuses to reveal sources for a controversial article. The court judge is annoyed by Ali.","Ali's aggressive questioning during a press conference causes a scene. The press secretary is annoyed by Ali.","Ali publishes an unverified story to beat competitors. The fact-checking team is annoyed by Ali.","Ali's undercover investigation disrupts a local business. The business owner is annoyed by Ali.","Ali's constant calls for comments on a developing story irritate a public figure. The public figure's spokesperson is annoyed by Ali.","Ali's live report from a dangerous area violates safety protocols. The news director is annoyed by Ali.","Ali's expose on corruption implicates powerful individuals. The newspaper's legal team is annoyed by Ali.","Ali's refusal to cover certain topics due to personal beliefs creates gaps in reporting. The assignment editor is annoyed by Ali.","Ali's tendency to sensationalize stories for more views compromises journalistic integrity. The senior reporter is annoyed by Ali."]
b2scene_idol                = []
b2scene_cybercriminal       = ["Ali's constant bragging about his hacks on dark web forums draws unwanted attention. His hacking group leader is annoyed by Ali.","Ali's insistence on targeting high-profile companies increases the risk of capture. His cybercrime mentor is annoyed by Ali.","Ali's addiction to online gaming interferes with his assigned tasks. The ransomware gang coordinator is annoyed by Ali.","Ali's constant demands for a larger cut of the profits threaten group cohesion. The cybercrime syndicate boss is annoyed by Ali."]
b2scene_thief               = ["Ali confidently plans a heist without considering the risks. The security guard is annoyed by Ali.", "Ali boasts about his skills while attempting to pickpocket a tourist. The tourist is annoyed by Ali.", "Ali insists on breaking into a house despite warnings from his accomplice. The accomplice is annoyed by Ali.", "Ali argues with a rival thief over stolen goods, thinking he can outsmart him. The rival thief is annoyed by Ali.", "Ali shows up at a crime scene, thinking he can take credit for someone else's work. The other thieves are annoyed by Ali.", "Ali tries to charm his way out of trouble with the police, believing he's invincible. The officer is annoyed by Ali."]
b2scene_composer            = ["Ali insists on using unconventional instruments in an orchestral piece. The conductor is annoyed by Ali.","Ali refuses to simplify his complex composition for a mainstream audience. The record label executive is annoyed by Ali.","Ali misses multiple deadlines for a commissioned work. The patron is annoyed by Ali.","Ali criticizes the performers' interpretation of his piece during rehearsal. The orchestra members are annoyed by Ali.","Ali demands last-minute changes to the score just before a premiere. The concert organizer is annoyed by Ali.","Ali's experimental composition causes audience members to leave mid-performance. The venue manager is annoyed by Ali.","Ali insists on using expensive, rare instruments for a small ensemble piece. The ensemble director is annoyed by Ali.","Ali publicly criticizes other composers' works at a music festival. The festival director is annoyed by Ali.","Ali refuses to adapt his avant-garde style for a film score. The film director is annoyed by Ali.","Ali's constant revisions to a commissioned piece delay the entire production. The production team is annoyed by Ali."]
b2scene_dancer              = ["Ali insists on performing a solo at every event, regardless of the group's input. The dance troupe is annoyed by Ali.","Ali refuses to follow the choreographer's directions during rehearsal. The choreographer is annoyed by Ali.","Ali shows up late to practice, claiming he was 'inspired' by a new dance move. The other dancers are annoyed by Ali.","Ali constantly critiques his fellow dancers' performances without offering constructive feedback. The dancers are annoyed by Ali.","Ali demands to be the center of attention during group performances. The audience is annoyed by Ali.","Ali interrupts rehearsals to demonstrate his own moves, disregarding the planned choreography. The director is annoyed by Ali.","Ali insists on wearing flashy costumes that distract from the overall performance. The costume designer is annoyed by Ali.","Ali's overconfidence leads him to challenge experienced dancers to impromptu battles. The veterans are annoyed by Ali.","Ali refuses to collaborate with others on choreography, insisting his style is superior. The dance community is annoyed by Ali."]


###########################################################################################################

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
b3scene_criminal            = ["Sudden vacancy", "Undercover Operation", "Death Game", "Ali is job interviewed by a terrorists group."]
b3scene_gambler             = ["death game", "underground casino tournament"]
b3scene_progamer            = ["Sudden vacancy"]
b3scene_teacher             = []
b3scene_school_club_member  = ["Sudden vacancy", "death game"]
b3scene_journalist          = []
b3scene_idol                = []
b3scene_cybercriminal       = ["Sudden vacancy", "Undercover Operation", "Death Game", "Bomb Defusal", "Alien Invation", "Ali is job interviewed by a terrorists group."]
b3scene_thief               = ["Sudden vacancy", "Undercover Operation", "Escape Plan"]
b3scene_composer            = ["sudden vacancy"]
b3scene_dancer              = ["Sudden vacancy"]
# Define b3scene_thief

b3scene                     = []
b3scene_farmer              = []
b3scene_guard               = ["Hostage situation", "Terrorist attack", "High-profile asset protection", "Prison riot", "Undercover operation"]


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
revealer_school_club_member = []

#
revealer_guard=[]
revealer_patient=["His behavioral therapy", "Explaining the treatment to him"]
revealer_journalist         = ["the sound of him reading his article", "The name of the media outlet he belongs to"]
revealer_idol               = []
revealer_cybercriminal      = []
revealer_thief              = []
revealer_composer           = ["his works"]
revealer_dancer             = ["his dance"]
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
rephrase_farmer             = []
rephrase_director           = [] # ■■■
rephrase_model              = []
rephrase_guard              = []
rephrase_patient            = []
rephrase_school_club_member = []
rephrase_journalist         = []
rephrase_idol               = []
rephrase_cybercriminal      = []
rephrase_thief              = []
rephrase_composer           = []
rephrase_dancer             = []
# s_rephrase lists depend on the hypo_i

###########################################################################################################




rephrase_chef           += [
    ["[French fry], [French cuisine]", "[Patty], [Steak]", "[Teriyaki Burger], [Japanese cuisine]", "[Happy Meal], [Full course meal]", "[McDonald's employee], [Chef]", "[McDonald's], [restaurant]", "[Cashier], [Maitre d' station]", "[Part-time worker], [Apprentice]"]
]

rephrase_progamer       += [
    ["[rock paper scissors], [PvP game]", "[Rock paper scissors], [Luck based]", "[Hand], [Input commands]", "[Win], [Kill]", "[Player], [Casual player]", "[Win rate], [K/D]", "[Rock can beat paper], [Rock is meta of paper]", "[Rock loses to paper, paper loses to scissors, and scissors loses to rock], [Metagame, Rule, 環境]", "[Luck], [RNG]", "[Losing], [Feeding]", "[Throw], [Input]", "[Hand shape], [UI]", "[Opponent], [Enemy]", "[Beginner], [Noob]"]
]

rephrase_actor          +=[ # Ali, a porn star, feels inferior to Hollywood stars, so he speaks like a Hollywood star. Ali calls [0] [1]. Ali hides the fact that he is a porn star and pretends to be an actor."
    ["porn", "romance"], ["having sex", "love scene"], ["undercover", "suspense movie"],["BDSM", "violence action"],["BDSM", "psycho thriller"],["porn star", "actor"],["porn", "PG-rated movie"],["adult film", "indie film"],["porn star", "co-actor"],["money shot", "climactic scene"],["fluffer", "production assistant"],["squirter", "side character"],["squirter", "extra"],["solo tease", "monodrama"],["medieval", "epic drama"],["nurse", "medical dramas"],  ["cum shot", "final scene"], ["gangbang", "ensemble cast"],  ["dildo", "prop"]
]

rephrase_writer         +=[ # "Ali, a tabloid writer, feels inferior to novelists, so he speaks like a novelist. Ali calls [0] [1]. Ali hides the fact that he is a tabloid writer and pretends to be a novelist."
    ["lying", "creation"],["gossip", "character development"],["clickbait", "hook"],["expose", "revealing chapter"],["tabloid", "literary work"],["lie", "fiction"],["lie", "fantasy"],["fabrication","dramatization"], ["tabloid writer", "novelist"], ["tabloid writer", "creator"]
]

rephrase_athlete        +=[ # "Ali, a e-sports player, feels inferior to athletes, so he speaks like a athlete. Ali calls [0] [1]. Ali hides the fact that he is an e-sports player and pretends to be an athlete."
    ["e-sports", "indoor sports"], ["tenosynovitis", "ligament injury"]
]

rephrase_journalist     +=[ # Ali, a tabloid writer, feels inferior to normal journalists. so he speaks like a normal journalist. Ali calls [0] [1]. Ali hides the fact that he is a tabloid writer and pretends to be a normal journalist."
    ["rumor, lie", "unconfirmed source"],["tabloid", "news, report"],["SNS", "grapevine, authority"], ["Checking SNS", "researching, fieldwork"], ["paparazzi", "reporter"]
]


# Add new 10 pairs in rephrase_comedian in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

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

rephrase_cybercriminal  +=[ # Ali, a wannabe of cracker, feels inferior to famous crackers.
    ["Illegal download, spamming", "cyber attack"], ["", ""]
]

# Define rephrase_cybercriminal


###########################################################################################################

# Listed below are some examples of how negative concepts have been elegantly rephrased in the media.
# Define rephrase_novelist list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.



# for i in rephrase_lists:
#  print(f"comedy script : If incompetence people do, it's {i[0]}; if competence people do, it's just {i[0]}.")

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
,["trip", "training camp"]
,["exercise, leisure, hobby, recreation, healthy living, fitness", "training, sport, match"]
,["being friendly", "teamwork"]
,["gathering", "team activity"]
,["outing", "field experience, match, sport"]
,["friend", "team member"]
,["bodily punishment", "assault "]
]

rephrase_school_club_member +=[
 ["trip", "training camp"]
,["exercise, leisure, hobby, recreation, healthy living, fitness", "training, sport, match"]
,["being friendly", "teamwork"]
,["gathering", "team activity, discussion"]
,["outing", "field experience, match, sport"]
,["friend", "team member"]
,["bodily punishment", "assault "]
]

rephrase_actor += [
 ["weight gain", "method acting, character transformation"]
,["plastic surgery", "career investment, image enhancement"]
,["typecasting", "signature role, iconic performance"]
,["unemployment", "selective career choices, between projects"]
,["public meltdown", "passionate outburst, intense emotion"]
,["scandal", "publicity, career-defining moment"]
,["rehab", "personal growth journey, career reset"]
,["aging", "seasoned performer, distinguished veteran"]
,["divorce", "high-profile romance, tabloid sensation"]
,["paparazzi altercation", "defending privacy, standing up to media intrusion"]
]



# Put a casual word in [0] and a classy word in [1]. e.g. If pro teams do, it's team activity, if amateur team do, it's just gathering.
# Extend 10 new items to rephrase_school_club_member list in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.

rephrase_journalist += [
    ["libel, stalking, hacking, voyeurism, harassment", "reporting"],
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





# for i in rephrase_lists:
#  print(f"comedy script : If competence people do, it's {i[1]}; if incompetence people do, it's just {i[0]}.")


# Add new 20 ones.

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
slump_journalist          = Slump([])
slump_composer            = Slump([l_slump_showbiz,"Writing jingles for commercials","Composing background music for elevators or shopping malls","Creating ringtones for mobile phones","Writing simple pop songs under a pseudonym","Arranging covers of popular songs for wedding bands","Composing music for children's TV shows","Creating soundtracks for low-budget indie games","Writing theme songs for local businesses","Producing generic stock music for video content","Composing music for fitness classes or guided meditations"])

# Define slump_composer in English. I will run your response through the eval function so please do not include unnecessary characters in your response.

# Add new items in slump_singer in English. I will run your response through the eval function so please do not include unnecessary characters in your response.






###########################################################################################################
@dataclass
class Binary:
    mental_physical_other:str # mental labor -> m, physical labor -> p, other -> blank
    art_sports:str
    job_not:str
    impress:str
    extrovert_introvert:str
    cant:list
    too_late:list # だーりんず:ひったくり, おぐ:r1用のネタ2本
    paid_item:list
    link_to_reverse_adj:list
    pride_neet_1:list # adjective. f"comedy prompt : You quit your job, so you're just a {self.pride_neet_1} unemployed now."


binary_singer               = Binary("o","a","j","i","e", [],[],[],[]                                       ,["邦楽が好きな", "声が良い", "リズム感のある", "ステージ慣れした", "カラオケ上手な", "表現力豊かな", "感性の豊かな", "MCスキルが高い", "声の大きい"])
binary_classical_musician   = Binary("o","a","j","i","" , [],[],[],[]                                       ,["家が金持ってた", "クラシック通な", "ステージ慣れした"])
binary_rock_musician        = Binary("o","a","j","i","e", [],[],[],[]                                       ,["薬をやっている", "ステージ慣れした", "MCスキルが高い", "声の大きい"])
binary_comedian             = Binary("o","a","j","" ,"i", [],[],[],["<a href='state#unfunny'>unfunny</a>"]  ,["明るい", "ステージ慣れした", "声の大きい"])
binary_novelist             = Binary("m","a","j","i","i", [],[],[],[]                                       ,["メンヘラな", "文章力のある"])
binary_artist               = Binary("o","a","j","i","i", [],[],[],[]                                       ,["メンヘラな", "創造力豊かな", "感性の豊かな", "表現力のある"])
binary_doctor               = Binary("m","" ,"j","" ,"" , [],[],[],[]                                       ,["物知りな", "人体に詳しい", "冷静な判断ができる"])
binary_researcher           = Binary("m","" ,"j","" ,"i", [],[],[],[]                                       ,["物知りな", "専門知識のある"])
binary_actor                = Binary("o","a","j","i","e", [],[],[],[]                                       ,["映画好きな", "表現力豊かな", "感情表現の上手い", "カメラ慣れした", "声の大きい"])
binary_chef                 = Binary("p","" ,"j","i","" , [],[],[],[]                                       ,["食事に気を使ってる", "味覚の鋭い"])
binary_athlete              = Binary("p","s","j","i","e", [],[],[],[]                                       ,["食事に気を使ってる", "体力のある", "筋肉質な", "反射神経の良い", "競争心の強い", "ストイックな", "体の柔軟な", "スポーツマンシップのある", "チームワークの良い", "瞬発力のある"])
binary_psycho_criminal      = Binary("o","" ,"" ,"" ,"" , [],[],[],[]                                       ,["反社会的な", "冷酷な", "予測不可能な"])
binary_examinee             = Binary("m","" ,"" ,"" ,"" , [],[],[],[]                                       ,["計画的な", "記憶力の良い", "自己管理のできる", "知識欲の強い", "粘り強い"])
binary_gambler              = Binary("m","" ,"" ,"" ,"" , [],[],[],[]                                       ,["債務者の","リスク好きな", "運の良い", "勝負強い"])
binary_progamer             = Binary("m","s","j","" ,"i", [],[],[],[]                                       ,["ゲーム好きな", "反射神経の良い", "チームワークの良い", "競争心の強い"])
binary_teacher              = Binary("m","" ,"j","" ,"" , [],[],[],[]                                       ,["教育熱心な", "子供思いの"])
binary_farmer               = Binary("p","" ,"j","" ,"" , [],[],[],[]                                       ,["広い土地持ってる", "田舎に住んでる"])
binary_director             = Binary("m","a","j","i","" , [],[],[],[]                                       ,["映画好きな", "表現力豊かな", "感情表現の上手い"])
binary_model                = Binary("o","" ,"j","" ,"e", [],[],[],[]                                       ,["おしゃれな","写真映えする","身だしなみの良い","スタイリッシュな","魅力的な","立ち振る舞いの美しい","体型維持に気を使う","流行に敏感な","見た目の良い"])
binary_guard                = Binary("p","" ,"j","" ,"e", [],[],[],[]                                       ,["防犯意識の高い", "監視カメラに詳しい", "巡回ルートを知り尽くした", "防犯ベルに敏感な", "警戒心の強い", "観察力の鋭い", "護身術に長けた", "緊急時の対応力がある", "危険予知能力が高い", "規律正しい", "冷静沈着な", "状況判断力に優れた", "チームワークに優れた"])
binary_patient              = Binary("o","" ,"" ,"" ,"" , [],[],[],[]                                       ,["調子の悪い"])
binary_school_club_member   = Binary("p","" ,"" ,"i","e", [],[],[],[]                                       ,["食事に気を使ってる", "体力のある", "筋肉質な", "反射神経の良い", "競争心の強い", "ストイックな", "体の柔軟な", "スポーツマンシップのある", "チームワークの良い", "瞬発力のある"])
binary_journalist           = Binary("m","" ,"j","" ,"" , [],[],[],[]                                       ,["文章力のある","情報収集能力の高い","コミュニケーション能力の高い","好奇心旺盛な","締め切りを守れる","客観的な視点を持つ"])
binary_idol                 = Binary("o","a","j","i","e", [],[],[],[],[])
binary_cybercriminal        = Binary("m","" ,"" ,"" ,"" , [],[],[],[]                                       ,["反社会的な", "冷酷な", "計画的な", "技術に詳しい", "リスクを取る", "情報収集能力の高い", "デジタルネイティブな"])
binary_thief                = Binary("o","" ,"" ,"" ,"" , [],[],[],[]                                       ,["狡猾な", "計画的な", "身軽な", "逃げ足の速い", "変装のうまい", "神出鬼没の"])
binary_composer             = Binary("m","a","j","i","" , [],[],[],[]                                       ,["音楽的才能のある", "創造力豊かな", "感性の豊かな", "音楽理論に詳しい", "楽器演奏のできる", "聴覚の鋭い", "リズム感のある", "和声学に精通した", "音楽史に詳しい", "編曲能力の高い"])
binary_dancer               = Binary("p","a","j","i","e", [],[],[],[]                                       ,["表現力豊かな", "リズム感のある", "体の柔軟な", "ステージ慣れした", "感情表現の上手い", "ダンス好きな", "チームワークの良い"])



# Define binary_dancer. I'll run your response through the eval function so please do not include unnecessary characters in your response. When creating an instance, make sure the position of characters and spaces match the existing instance.

###########################################################################################################
@dataclass
class Monk:
    ALL_MONK: ClassVar[List['Monk']] = [] # When passing text as an argument to the instances, please make the text as short as possible.
    petty_praise:list
    does_b:list #
    did_a :list
    hard  :list
    advice:list
    wanna :list
    def __post_init__(self):
        Monk.ALL_MONK.append(self)
        if self:
            self.hard.append(["Is society really this hard?"])


monk_singer             = Monk([],[], ["attended his show"], ["Is music really this difficult?"], [], ["stop buying your work", "stop being your patron"])
monk_classical_musician = Monk([],[], ["attended his show"], ["Is music really this difficult?"], [], ["stop buying your work", "stop being your patron"])
monk_rock_musician      = Monk([],[], ["attended his show"], ["Is music really this difficult?"], [], ["stop buying your work", "stop being your patron"])
monk_comedian           = Monk([],[], ["attended his show"], ["Is comedy really this difficult?"], [], ["stop buying your work", "stop being your patron"])
monk_writer             = Monk([],[], ["red his work"]     , ["Is literature really this difficult?"], [], ["stop buying your work", "stop being your patron"])
monk_artist             = Monk([],[], ["attended his show"], ["Is art really this difficult?"], [], ["stop buying your work", "stop being your patron"])
monk_doctor             = Monk([],["holds people's lives in their hands", "cuts people's bodies"], ["was cut by him", "was cured by him"], ["I had no idea treating cancer would be this hard"], ["I wanna be of help to you."], ["stop treatment", "change my doctor"])
monk_researcher         = Monk([],["uncovers the truth"], [], ["is academics really this difficult?"], ["I wanna uncover the truth"], ["stop learning from you"])
monk_actor              = Monk([],[], [], [], [], [])
monk_chef               = Monk([],[], [], [], [], [])
monk_athlete            = Monk([],[], [], [], [], [])
monk_criminal           = Monk([],[], [], [], [], [])
monk_examinee           = Monk([],[], [], [], [], [])
monk_gambler            = Monk([],[], [], [], [], [])
monk_progamer           = Monk([],[], [], [], [], [])
monk_teacher            = Monk([],["leads children"], [], [], [], [])
monk_farmer             = Monk([],["makes the food people eat"], [], [], [], [])
monk_director           = Monk([],[], [], [], [], [])
monk_model              = Monk([],[], [], [], [], [])
monk_guard              = Monk([],[], [], [], [], [])
monk_patient            = Monk([],[], [], [], [], [])

monk_school_club_member = Monk([],[], [], [], [], [])
monk_idol               = Monk([],[], [], [], [], [])
monk_journalist         = Monk([],[], [], [], [], [])
monk_cybercriminal      = Monk([],[], [], [], [], [])
monk_thief              = Monk([],[], [], [], [], [])
monk_composer           = Monk([],[], [], [], [], [])
monk_dancer             = Monk([],[], [], [], [], [])

'''
re0_singer             = Re0("")
re0_classical_musician = Re0("")
re0_rock_musician      = Re0("")
re0_comedian           = Re0("")
re0_writer             = Re0("")
re0_artist             = Re0("")
re0_doctor             = Re0("")
re0_researcher         = Re0("")
re0_actor              = Re0("")
re0_chef               = Re0("")
re0_athlete            = Re0("")
re0_criminal           = Re0("scopophilia, kleptomania")
re0_examinee           = Re0("studyholism")
re0_gambler            = Re0("gambling disorder")
re0_progamer           = Re0("gaming disorder")
re0_teacher            = Re0("")
re0_farmer             = Re0("")
re0_director           = Re0("")
re0_model              = Re0("dysmorphophobia")
re0_guard              = Re0("PTSD")
re0_patient            = Re0("")
'''
# Bob refers to Ali's {x}: I guess it's a different disorder. I guess Ali's abnormality is not (only) caused by his {x}.


###########################################################################################################



###########################################################################################################
@dataclass
class Agent:
  ALL_AGENT: ClassVar[List['Agent']] = []
  agent_name: str
  s_Grade: Grade
  s_Effort: Effort
  s_Suffer: Suffer
  s_Action: Action
  s_Appear: Appear
  s_b2scene : list
  s_b3scene : list
  s_revealer: list
  s_rephrase: list
  s_Binary : Binary
  s_Slump  : Slump
  s_Monk    : Monk
  def __post_init__(self):
    Agent.ALL_AGENT.append(self)
    if   self.s_Binary.mental_physical_other:
        self.s_Binary.pride_neet_1.append(["プライドの高い", "話を聞かない", "敬語を使えない", "千葉の", "自分に自信がある", "感情的な"])
        self.s_Binary.paid_item.append(["training", "advice"])
    if   self.s_Binary.job_not:
        self.s_Binary.cant.append(["人々の役に立つ", "夢を掴む"])
    if   self.s_Binary.mental_physical_other == "m":
        self.s_Binary.pride_neet_1.append(["目の悪い", "ニッコマの", "Fランの", "学士の", "大卒の", "痩せた", "太った", "繊細な", "暗い", "インドアな", "几帳面な", "体力のない", "理屈っぽい"])
        self.s_Binary.link_to_reverse_adj.append("<a href='state#illiteracy'>illiteracy</a>")
        self.s_Binary.link_to_reverse_adj.append("<a href='state#mild_yankee'>mild_yankee</a>")
        self.s_Binary.too_late.append(["eating blue fish", "reading a thick book", "trying to solve a Rubik’s Cube", "doing mindfulness", "watching TED Talks", "doing doing flash ANZAN", "playing chess"])
        self.s_Binary.paid_item.append(["nootropics"])
    elif self.s_Binary.mental_physical_other == "p":
        self.s_Binary.pride_neet_1.append(["健康な", "ガタイがいい", "痩せた", "背が高い", "色黒な", "ストリート系の", "明るい", "社交的な", "姿勢のいい", "日焼けした", "アウトドアな", "体育会系の", "食事に気を使ってる"])
        self.s_Binary.link_to_reverse_adj.append("<a href='state#unhealthy'>unhealthy</a>")
        self.s_Binary.too_late.append(["doing push ups", "eating a low-calorie diet", "hiking up the stairs instead of using the elevator", "staying hydrated with water","drinking protein shakes", "eating energy bars",])
    if self.s_Binary.art_sports == "a":
        self.s_Binary.pride_neet_1.append(["物憂げな", "繊細な", "暗い", "インドアな", "几帳面な", "体力のない", "理屈っぽい"])
        self.s_Binary.cant.append(["人々を感動させる"])
    if self.s_Binary.art_sports == "a" and not self.s_Binary.mental_physical_other == "m":
        self.s_Binary.link_to_reverse_adj.append("<a href='state#illiteracy'>illiteracy</a>")
        self.s_Binary.link_to_reverse_adj.append("<a href='state#mild_yankee'>mild_yankee</a>")
    if self.s_Binary.impress:
        self.s_Monk.does_b.append(["gives people hope", "impresses people"])
        self.s_Monk.did_a.append(["was moved by him", "was saved by him", "was given hope by him"])
        self.s_Monk.advice.append(["I wanna give you hope"])

# print(f"comedy script * Ali: I suddenly had to take an IQ test in an hour. So I'm {enhancement_intelligence} quickly now. - Bob: It's too late.")
enhancement_intelligence = ["eating blue fish", "reading a book", "trying to solve a Rubik’s Cube", "doing mindfulness", "watching TED Talks", "doing flash ANZAN", "playing chess"] # Add new 20 ones.

# print(f"comedy script * Ali: I suddenly had to take an physical fitness test in an hour. So I'm {enhancement_physical} quickly now. - Bob: It's too late.")
enhancement_physical = ["doing push ups", "eating a low-calorie diet", "hiking up the stairs instead of using the elevator", "staying hydrated with water","drinking protein shakes", "eating energy bars",] # Add new 20 ones.



agent_singer                =Agent("singer"             ,grade_singer            , effort_singer         , suffer_singer         , action_singer               , appear_singer               , b2scene_singer + b2scene_rock_musician             ,b3scene_default      , revealer_singer           ,rephrase_singer            ,binary_singer              ,slump_singer             , monk_singer             )
agent_classical_musician    =Agent("classical_musician" ,grade_classical_musician, effort_instrumentalist, suffer_instrumentalist, action_classical_musician   , appear_classical_musician   , b2scene_classical_musician + b2scene_rock_musician ,b3scene_default      , revealer_instrumentalist  ,rephrase_rock_musician     ,binary_classical_musician  ,slump_classical_musician, monk_classical_musician  )
agent_rock_musician         =Agent("rock_musician"      ,grade_rock_musician     , effort_instrumentalist, suffer_instrumentalist, action_rock_musician        , appear_rock_musician        , b2scene_classical_musician + b2scene_rock_musician ,b3scene_default      , revealer_instrumentalist  ,rephrase_classical_musician,binary_rock_musician       ,slump_rock_musician     , monk_rock_musician       )
agent_comedian              =Agent("comedian"           ,grade_comedian          , effort_comedian       , suffer_comedian       , action_comedian             , appear_comedian             , b2scene_comedian                                   ,b3scene_default      , revealer_comedian         ,rephrase_comedian          ,binary_comedian            ,slump_comedian          , monk_comedian            )
agent_writer                =Agent("writer"             ,grade_novelist          , effort_writer         , suffer_writer         , action_writer               , appear_writer               , b2scene_novelist                                   ,b3scene_writer       , revealer_novelist         ,rephrase_writer            ,binary_novelist            ,slump_writer            , monk_writer              )
agent_artist                =Agent("artist"             ,grade_artist            , effort_artist         , suffer_artist         , action_artist               , appear_artist               , None                                               ,b3scene_default      , revealer_artist           ,None                       ,binary_artist              ,slump_artist            , monk_artist              )
agent_doctor                =Agent("doctor"             ,grade_doctor            , effort_doctor         , suffer_doctor         , action_doctor               , appear_doctor               , b2scene_doctor                                     ,b3scene_doctor       , revealer_doctor           ,None                       ,binary_doctor              ,slump_doctor            , monk_doctor              )
agent_researcher            =Agent("researcher"         ,grade_researcher        , effort_researcher     , suffer_researcher     , action_researcher           , appear_researcher           , None                                               ,b3scene_researcher   , revealer_researcher       ,None                       ,binary_researcher          ,slump_researcher        , monk_researcher          )
agent_actor                 =Agent("actor"              ,grade_actor             , effort_actor          , suffer_actor          , action_actor                , appear_actor                , b2scene_actor                                      ,b3scene_default      , revealer_actor            ,rephrase_actor             ,binary_actor               ,slump_actor             , monk_actor               )
agent_chef                  =Agent("chef"               ,grade_chef              , effort_chef           , suffer_chef           , action_chef                 , appear_chef                 , b2scene_chef                                       ,b3scene_default      , revealer_chef             ,rephrase_chef              ,binary_chef                ,slump_chef              , monk_chef                )
agent_athlete               =Agent("athlete"            ,grade_athlete           , effort_athlete        , suffer_athlete        , action_athlete              , appear_athlete              , b2scene_athlete                                    ,b3scene_athlete      , revealer_athlete          ,rephrase_athlete           ,binary_athlete             ,slump_athlete           , monk_athlete             )
agent_criminal              =Agent("criminal"           ,grade_psycho_criminal   , None                  , None                  , action_psycho_criminal      , appear_psycho_criminal      , None                                               ,b3scene_criminal     , revealer_criminal         ,rephrase_criminal          ,binary_psycho_criminal     ,slump_criminal          , monk_criminal            )
agent_examinee              =Agent("examinee"           ,grade_examinee          , effort_examinee       , suffer_examinee       , None                        , None                        , None                                               ,None                 , None                      ,None                       ,binary_examinee            ,slump_examinee          , monk_examinee            )
agent_student               =Agent("student"            ,grade_student           , effort_examinee       , suffer_examinee       , None                        , None                        , None                                               ,None                 , None                      ,None                       ,binary_examinee            ,slump_examinee          , monk_examinee            )
agent_gambler               =Agent("gambler"            ,grade_gambler           , effort_gambler        , suffer_gambler        , action_gambler              , appear_gambler              , None                                               ,b3scene_gambler      , revealer_gambler          ,None                       ,binary_gambler             ,slump_gambler           , monk_gambler             )
agent_progamer              =Agent("progamer"           ,grade_progamer          , effort_progamer       , suffer_progamer       , action_progamer             , appear_progamer             , b2scene_progamer                                   ,b3scene_default      , revealer_progamer         ,rephrase_progamer          ,binary_progamer            ,slump_progamer          , monk_progamer            )
agent_teacher               =Agent("teacher"            ,grade_teacher           , effort_teacher        , suffer_teacher        , action_teacher              , appear_teacher              , b2scene_teacher                                    ,b3scene_default      , revealer_teacher          ,None                       ,binary_teacher             ,slump_teacher           , monk_teacher             )
agent_farmer                =Agent("farmer"             ,grade_farmer            , effort_farmer         , suffer_farmer         , action_farmer               , appear_farmer               , b2scene_farmer                                     ,None                 , revealer_farmer           ,None                       ,binary_farmer              ,None                    , monk_farmer              )
agent_director              =Agent("director"           ,grade_director          , effort_director       , suffer_director       , action_director             , appear_director             , b2scene_director                                   ,None                 , revealer_director         ,rephrase_director          ,binary_director            ,None                    , monk_director            )
agent_model                 =Agent("model"              ,grade_model             , effort_model          , suffer_model          , action_model                , appear_model                , b2scene_model                                      ,None                 , revealer_model            ,rephrase_model             ,binary_model               ,None                    , monk_model               )
agent_guard                 =Agent("guard"              ,grade_guard             , effort_guard          , suffer_guard          , action_guard                , appear_guard                , b2scene_guard                                      ,b3scene_guard        , revealer_guard            ,rephrase_guard             ,binary_guard               ,None                    , monk_guard               )
agent_patient               =Agent("patient"            ,grade_patient           , effort_patient        , suffer_patient        , action_patient              , appear_patient              , b2scene_patient                                    ,None                 , revealer_patient          ,rephrase_patient           ,binary_patient             ,None                    , monk_patient             )
agent_school_club_member    =Agent("school_club_member" ,grade_school_club_member, effort_school_club_member, suffer_school_club_member, action_school_club_member, appear_school_club_member, b2scene_school_club_member                         ,b3scene_school_club_member, revealer_school_club_member, rephrase_school_club_member, binary_school_club_member, None             , monk_school_club_member  )
agent_journalist            =Agent("journalist"         ,grade_journalist        , effort_journalist     , suffer_journalist     , action_journalist           , appear_journalist           , b2scene_journalist                                 ,b3scene_journalist   , revealer_journalist       ,rephrase_journalist        ,binary_journalist          ,None                    , monk_journalist          )
# idol
agent_cybercriminal         =Agent("cybercriminal"      ,grade_cybercriminal     , effort_cybercriminal  , suffer_cybercriminal  , action_cybercriminal        , appear_cybercriminal        , b2scene_cybercriminal                              ,b3scene_cybercriminal, revealer_cybercriminal    ,rephrase_cybercriminal     ,binary_cybercriminal       ,None                    , monk_cybercriminal       )
agent_thief                 =Agent("thief"              ,grade_thief             , effort_thief          , suffer_thief          , action_thief                , appear_thief                , b2scene_thief                                      ,b3scene_thief        , revealer_thief            ,rephrase_thief             ,binary_thief               ,None                    , monk_thief               )
agent_composer              =Agent("composer"           ,grade_composer          , effort_composer       , suffer_composer       , action_composer             , appear_composer             , b2scene_composer                                   ,b3scene_composer     , revealer_composer         ,rephrase_composer          ,binary_composer            ,slump_composer          , monk_composer            )
agent_dancer                =Agent("dancer"             ,grade_dancer            , effort_dancer         , None                  , action_dancer               , appear_dancer               , b2scene_dancer                                     ,b3scene_dancer       , revealer_dancer           ,rephrase_dancer            ,binary_dancer              ,None                    , monk_dancer              )


