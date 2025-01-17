from dataclasses import dataclass, field
from typing import List, ClassVar
###########################################################################################################

teacher_data={"さらば青春の光": ["男優", "依存症", "猿回し"], "ファイヤーサンダー":["立ち退き"], "Aマッソ":["タレント"], "ファイヤーサンダー+ライス":["ぼったくりバー"], "滝音":["バンドのファン"], "バイきんぐ":["自動車学校"], "ゾフィー":["不良"]}



@dataclass
class AbnormalCliche:
    abnormal:list # Abnormal hyponyms
    cliche:list # Cliche elements that doesn't appear in .abnormal
    cliche_agent:list # agents who doesn't appear in .abnormal



ac_school       =AbnormalCliche(["blind school", "driving school", "low tier university", "community computer class", "kindergarten", "Vocational School", "Prep school", "free school"], ["Ronin", "Drill sergeant", "Repeat a degree", "Alumni visit", "Hazing", "School club activity", "Prom night", "Prohibition of heterosexual relations", "Uniform", "Dress code", "Bullying", "Fighting", "Mixed relations", "Sex education", "Suspension", "Delinquent", "Student activity", "Stool and urine tests"]
                               ,["Bully", "Bullied", "Ronin", "Repeated student", "Drill sergeant", "Delinquent", "Student activist"])
ac_restaurant   =AbnormalCliche(["soup kitchen", "hot pillow hotel kitchen", "eating contest"]                                                                                          , ["reservation", "food critic", "Call the chef and tell him your opinion of the taste", "Dress code", "Farm-to-table", "Sommelier recommendation"]
                               ,["Food critic"])
ac_fiction      =AbnormalCliche(["fan fiction", "choose your own adventure", "hentai novel", "self-insert character", "hentai comic", "history book"]                                   , ["spoil", "fan fiction", "analyze"]
                               ,["critic", "fan artist", "analyzer"])
ac_sport        =AbnormalCliche(["Billiards player", "Table tennis player"]                                                                                                             , ["Team spirit", "Sportsmanship", "Doping", "Half-time show", "Training camp", "Admission by sports recommendation", "Inter-university competition", "Fan loyalty", "Championship rings", "Athlete sponsorships", "Game day rituals", "Rough play"]
                               ,["Hooligan", "Referee", "Coach", "Sports commentator", "Cheerleader", "Team mascot"])





ac_lover        =AbnormalCliche(["prostitute", "arranged marriage", "rape victim", "mail-order bride","sugar daddy/sugar baby relationship","polyamorous relationship","open relationship","green card marriage","virtual reality dating","AI companion relationship","age-gap relationship (with significant age difference)","relationship with a fictional character"],["propose", "dating", "cheating", "blind date", "long-distance relationship", "double date", "anniversary celebration", "meeting the parents", "marriage", "rut", "romantic getaway", "public display of affection", "surprise", "breakup", "swapping", "fight", "make-up after fight"]
                               ,["Cheat mate", "Matchmaker","Wingman","Ex-partner","Love rival","Relationship counselor","Wedding planner","Divorce lawyer","Couples therapist","Dating coach"])

#ac_conversation_work =AbnormalCliche(["Vtuber", "hostess"], ["tipping"], [])
#ac_interact_with_women_for_a_fee=AbnormalCliche([],[],[])

# Add new 10 items in ac_go_steady.abnormal. Start answer with ```python


ac_crime        =AbnormalCliche(["murder"],["Rapping about their crime"],["cop"])


#organized_crime
ac_undercover   =AbnormalCliche(["A illegal prostitution group", "A restaurant violating the Food Sanitation Act", "Unlicensed daycare center"]                                         , ["Torture", "Wire tapping", "Surveillance", "Code names", "Safe house", "Dead drop", "Disguise", "Encrypted communication", "Blackmail", "Bribery", "False identity", "Covert photography", "Stake out", "Tailing suspect", "Interrogation", "Sting operation", "Witness protection"]
                               ,["Double-cross", "Double Agent", "Informant", "Whistleblower"])




# Complete ac_undercover.abnormal. Start answer with ```python



# Define ac_undercover. Start answer with ```python



# Add new 10 items in ac_hospital.cliche_agent. Start answer with ```python
# There is no need for "agents that definitely do not exist in that .abnormal".


ac_gamble       =AbnormalCliche(["coin pusher", "lottery", "bingo", "raffle"]                                                           , []
                               ,["Tipster", "Bookie", "High roller", "Gamblaholic", "Bust", "Bankrupt"])
ac_hospital     =AbnormalCliche(["cosmetic surgery", "ED clinic", "phimosis clinic", "dental clinic", "School nurse's office", "mental hospital"]          , ["Home health care", "Blood work", "Testament", "Praying patient", "Emergency case", "Inpatient", "Triage", "Rounds", "Code blue", "Organ donation", "Urine and stool tests", "Palpation", "Surgery", "Will", "Anesthesia", "Medical malpractice", ]
                               ,["Chaplain", "Inpatient", "Praying family", "Visitor", "Baseball player promising a home run", "Quack Doctor"])
ac_band         =AbnormalCliche(["cover band", "elevator music", "jingle"]                                                              , ["encore", "merchandise", "fan club", "cover band", "plagiarism"]
                               ,["Impersonator", "Groupie", "Stalker"])
ac_game         =AbnormalCliche(["rock paper scissors"]                                                                                 , ["tournament", "rage", "voice chat"]
                               ,["cheater", "streamer"])
ac_movie        =AbnormalCliche(["porn", "Karaoke background movie", "commericial"]                                                     , [ac_fiction.cliche, "Ad-lib", "Red carpet premiere", "Oscar nomination", "Sequel", "Prequel", "Director's cut", "Behind the scenes", "Audio commentary", "Foreshadowing", "Theme song", "Plot twist","Cliffhanger ending","Easter eggs","Post-credits scene","Product placement","Cameo appearance","Montage sequence","Flashback","Voice-over narration","Green screen effects"]
                               ,[ac_fiction.cliche_agent])




ac_death        =AbnormalCliche(["murder", "sweetdeath", "suicide", "natural death", "execution"],["cheerful funeral", "ghostly visitation", "the grieving widow/widower", "life flashing before eyes", "Curse of the Dead"],["grieving family member", "necromancer", "Ghost"])


# define ac_fiction



# ac_fictionとac_movieの取り扱い

# examineeよりもcollege_studentの方が使用可能ivが多い!

# Define ac_sport without any explanations


# Add new items in ac_gamble.abnormal without any explanations



# AbnormalClicheに"agentnoun"を組み込むか





# ronin, repeat a degree, は agent_examinee.sufferに内包されている
# Add new items in ac_band.cliche without any explanations. Start answer with ```python

"""
Bob to Ali lineのみ生成する。Ali tried to do X -(lag)-> ... みたいな具体的な生成はしない。

There is usually no improvisation in adult videos.
There is usually no bullying in driving schools.
"""



###########################################################################################################

@dataclass
class Grade:
  hypo_s    :list# superior hyponym.
  hypo_s_pn :list# superior hyponym (proper noun).
  hypo_i    :list# inferior hyponym. For example, bassist is an inferior to rock musician. Darts player is inferior to athlete.
  hypo_i_pn :list# inferior hyponym (proper noun).

'''
@dataclass
class Grade:
  hypo_s    :list
  hypo_s_pn :list
  hypo_i    :list # hyponyms that are generally not the main characters in movies or TV dramas and are looked down upon
  hypo_i_pn :list
'''


'''
grade_rock_musician     =Grade(["guitarist", "vocalist"]                                            ,["Beatles"]
                              ,["bassist", "cover band", "impersonator"]                            ,[])
grade_actor             =Grade(["Hollywood star"]                                                   ,["Gary Oldman"]
                              ,["Porn actor", "ASMR actor", "Karaoke background video actor","extra", "commercial actor", "stuntman", "motion actor", "impersonator"],["Stallone"])
grade_model             =Grade(["fashion model"]                                                    ,["G.Bundchen"]
                              ,["parts model", "stock photo model"],[])
grade_thief             =Grade(["phantom thief", "master thief"]                                    ,["D.B. Cooper"]
                              ,["pickpocket", "shoplifter"]                                         ,[])
'''


# add new items in  grade_engineer.hypo_i.  Align the letters and spaces to the existing instance. Start answer with ```python




# 安堂ロイド, まいじつ 等を含めるか?


grade_rock_musician     =Grade(["guitarist", "vocalist"]                                            ,["Beatles"]
                              ,["bassist", "cover band", "impersonator"]                            ,[])
grade_singer            =Grade(["singer"]                                                           ,["Beyonce"]
                              ,["idol", "rapper", "voice actor", "impersonator"]                    ,["Aquatimez", "Orange range", "Britney Spears"])
grade_classical_musician=Grade(["pianist", "violinist"]                                             ,["Bach"]
                              ,["cymbalist", "trianglist"]                                          ,[])
grade_comedian          =Grade(["comedian"]                                                         ,["Hitoshi Matsumoto"]
                              ,["Vtuber", "tv talent", "voice actor", "clown", "猿回し"]            ,["Tsuyoshi Muro"])
grade_novelist          =Grade(["novelist"]                                                         ,["Stephen King"]
                              ,["Narou novelist", "tabloid writer", "fanfiction writer", "copy writer", "poet"]                                 ,["Hiro Mizushima"])
grade_artist            =Grade(["artist"]                                                           ,["Picasso"]
                              ,["contemporary artist", "Hentai manga artist"]                       ,["Toru Mitsumune"])
grade_doctor            =Grade(["neurosurgeon", "cardiologist"]                                     ,[]
                              ,["dermatologist", "internist", "nurse", "dentist", "Veterinarian"]   ,[])
grade_researcher        =Grade(["mathematician", "physicist"]                                       ,["Einstein"]
                              ,["gender studies researcher"]                                        ,["Chizuruko Ueno"])
grade_actor             =Grade(["Hollywood star"]                                                   ,["Gary Oldman"]
                              ,["Porn actor", "ASMR actor", "Karaoke background video actor","extra", "commercial actor", "stuntman", "motion actor", "impersonator"],["Stallone"])
grade_chef              =Grade(["French chef"]                                                      ,["Michelin restaurant chef"]
                              ,["Fast food restaurant employee","Jiro inspire employee", "Kitchen staff of Karaoke", "Kitchen staff of hotpillow hotel"]                                    ,["McDonalds"])
grade_athlete           =Grade(["baseball player"]                                                  ,["Kyojin player"]
                              ,["billiards player", "darts player", "race walker", "bodybuilder"]   ,["DeNA player"])
grade_school_club_member=Grade(["baseball club member"]                                             ,["Koshien player"]
                              ,["chess club member", "newspaper club member"]                       ,[])
grade_psycho_criminal   =Grade(["murder", "terrorist"]                                              ,["Jeffrey Dahmer"]
                              ,["groper", "voyeurist", "shoplifter"]                                ,["Jared Fogle"])
grade_progamer          =Grade(["apex pro", "siege pro"]                                            ,["Umehara"]
                              ,["coin pusher player", "water game player"]                          ,[])
grade_gambler           =Grade(["poker pro"]                                                        ,[]
                              ,["coin pusher player", "lottery addicted"]                           ,[])
grade_examinee          =Grade(["national university examinee"]                                     ,["MIT examinee"]
                              ,["driving school examinee", "low tier university examinee"]          ,["Tokyo Mode Gakuen examinee"])
grade_student           =Grade(["national university student"]                                      ,["MIT student"]
                              ,["driving school student", "low tier university student"]            ,["Tokyo Mode Gakuen student"])
grade_teacher           =Grade(["national university professor"]                                    ,["MIT professor"]
                              ,["driving school teacher", "low tier university teacher", "kindergarten teacher", "sewing class teacher", "special education teacher", "elective teacher"], ["Kumon teacher", "Tokyo Mode Gakuen professor"])
grade_craftsman         =Grade(["potter", "blacksmith"]                                             ,[]
                              ,["fleshlight designer", "line worker"]                               ,[])
grade_farmer            =Grade(["vineyard farmer", "apple farmer"]                                  ,[]
                              ,["Parsley Farmer", "Farmer growing grapes for gummy"]                ,[])
grade_livestock_farmer  =Grade(["cattle farmer", "sheep farmer"]                                    ,[]
                              ,["Foie gras maker", "puppy mill breeder", "guinea pig breeder"]      ,[])
grade_director          =Grade(["director"]                                                         ,["S.Spielberg"]
                              ,["commercial director", "porn film director"]                        ,["Toru Muranishi"])
grade_model             =Grade(["fashion model"]                                                    ,["G.Bundchen"]
                              ,["hand model", "parts model", "hair model", "commercial model", "plus-size model", "stock photo model"],[])
grade_guard             =Grade(["cop", "bodyguard"]                                                 ,["Secret Service"]
                              ,["mall security", "nightclub bouncer", "school crossing guard"]      ,[])
grade_patient           =Grade(["cancer patient", "ALS patient"]                                    ,[]
                              ,["Uncircumcised man", "Menopausal person", "Life-prolonging treatment patient", "ADHD patient", "venereal disease patients"],[])
grade_the_dying         =Grade(["Man in gunfights", "Man in traffic accidents"]                     ,[]
                              ,[]                               ,[])
grade_journalist        =Grade(["journalist", "war correspondent"]                                  ,["Bob Woodward"]
                              ,["gossip columnist", "weather reporter", "tabloid writer"]           ,[])
grade_idol              =Grade(["坂道アイドル", "ジャニーズアイドル"]                               ,["AKB48", "嵐"]
                              ,["local idol", "underground idol", "image video idol"]               ,["Kamen Joshi"])
grade_cyber_criminal    =Grade(["hacker"]                                                           ,["Lazarus Group"]
                              ,["script kiddie", "phisher", "spammer", "オレオレ詐欺犯", "pirate", "slanderer"]  ,["DarkSide", "REvil"])
grade_thief             =Grade(["phantom thief", "master thief"]                                    ,["D.B. Cooper"]
                              ,["pickpocket", "shoplifter"]                                         ,[])
grade_composer          =Grade(["composer"]                                                         ,["Beethoven"]
                              ,["elevator music composer", "jingle composer", "sound effect composer"],[])
grade_dancer            =Grade(["ballet dancer"]                                                    ,["Mikhail Baryshnikov"]
                              ,["backup dancer", "stripper", "flash mob participant"]               ,["Maddie Ziegler", "Jabbawockeez"])
grade_barista           =Grade(["barista"]                                                          ,[]
                              ,["cat cafe staff", "maid cafe staff"]                                ,[])
grade_masseuse          =Grade(["masseuse"]                                                         ,[]
                              ,["massage palror staff"]                                             ,[])
grade_hotel_staff       =Grade(["hotel staff"]                                                      ,[]
                              ,["hot-pillow hotel staff"]                                           ,[])
grade_delinquent_student=Grade(["delinquent student"]                                               ,[]
                              ,["blind school delinquent student"]                                  ,[])
grade_bartender         =Grade(["bar bartender"]                                                    ,[]
                              ,["pub bartender", "rip off bar bartender", "girls bar bartender", "host club bartender"], [])
grade_photographer      =Grade(["portrait photographer", "war photographer", "wildlife photographer"], ["Ansel Adams", "Annie Leibovitz"]
                              ,["train geek", "porn photographer", "voyeurist", "paparazzi"]        , [])
grade_game_designer     =Grade(["level designer", "game director"]                                  ,["Shigeru Miyamoto"]
                              ,["hentai game designer"]                                             ,["Lilith"])
grade_driver            =Grade(["race car driver"]                                                  ,["Lewis Hamilton"]
                              ,["taxi driver", "bus driver", "delivery driver", "chauffeur", "truck driver"]         ,["Uber"])
grade_engineer          =Grade(["software engineer"]                                                ,["Edison"]
                              ,["sex toy engineer"]                                                 ,[])






###########################################################################################################
@dataclass
class GarnishAllow:
    ALL_GARNISHALLOW: ClassVar[List['GarnishAllow']] = []
    allowed_garnish :list
    event           :str# UNFAMOUS      // if .event is true, allow to access .
    mcdonalds       :str# LOWBROW       // if two or more of .mcdonalds .inordinary .rich are true, then allow to access.
    inordinary      :str# LOWBROW
    rich            :str# LOWBROW
    arrogance       :str# HIGH_PRIDE    // if one or more of .arrogance .low_competitive true, then allow to access.
    low_competitive :str# HIGH_PRIDE
    adhd_lgbt       :str# SAD_PAST
#    high_turn_over  :str# isnt_the_cause_you
#    mcjob  :str# isnt_the_cause_you
#    team_work  :str# isnt_the_cause_you

#    help_someone    :str#


    def __post_init__(self):
        GarnishAllow.ALL_GARNISHALLOW.append(self)
        if self.event:
            self.allowed_garnish.append("UNFAMOUS")
        lowbrow_count = sum(bool(getattr(self, attr)) for attr in ['mcdonalds', 'inordinary', 'rich'])
        if lowbrow_count >= 2:
            self.allowed_garnish.append("LOWBROW")
        if self.arrogance or not self.low_competitive:
            self.allowed_garnish.append("HIGH_PRIDE")
        if self.adhd_lgbt:
            self.allowed_garnish.append("SAD_PAST")

'''
@dataclass
class GarnishAllow:
    event               :str # Are they often invited to events?
    mcdonalds           :str # Is there a stereotype that they don't eat at McDonald's?
    inordinary          :str # Is there a stereotype of them being ignorant of pop culture?
    rich                :str # Are they come from wealthy backgrounds commonly?
    arrogance           :str # Is there a stereotype that they're arrogant or competitive?
    low_competitive     :str # Isn't this the kind of job where losers in the competition will quickly become unemployed?
    adhd_lgbt           :str # Is there a stereotype that they are motivated in their profession by some sad past, either their own or their community's?
'''

ga_rock_musician        = GarnishAllow([],"y","y","y","" ,"y","" ,"y")
ga_singer               = GarnishAllow([],"y","y","y","" ,"y","" ,"y")
ga_classical_musician   = GarnishAllow([],"y","y","y","y","y","" ,"y")
ga_comedian             = GarnishAllow([],"y","" ,"" ,"" ,"y","" ,"y")
ga_novelist             = GarnishAllow([],"y","y","y","" ,"" ,"" ,"y")
ga_artist               = GarnishAllow([],"y","y","y","" ,"y","" ,"y")
ga_doctor               = GarnishAllow([],"" ,"y","y","y","" ,"" ,"y")
ga_researcher           = GarnishAllow([],"y","y","y","y","y","" ,"y")
ga_writer               = GarnishAllow([],"y","y","y","y","y","" ,"y")
ga_actor                = GarnishAllow([],"y","y","y","" ,"y","" ,"y")
ga_chef                 = GarnishAllow([],"y","y","" ,"" ,"y","" ,"y")
ga_athlete              = GarnishAllow([],"y","y","" ,"" ,"y","" ,"y")
ga_violent_criminal     = GarnishAllow([],"" ,"" ,"y","" ,"y","y","y")
ga_cyber_criminal       = GarnishAllow([],"" ,"" ,"y","" ,"y","y","y")
ga_thief                = GarnishAllow([],"" ,"" ,"y","" ,"y","y","y")
ga_idol                 = GarnishAllow([],"y","y","" ,"" ,"y","" ,"y")
ga_student              = GarnishAllow([],"" ,"" ,"" ,"" ,"" ,"" ,"y")
ga_examinee             = GarnishAllow([],"" ,"" ,"" ,"" ,"" ,"" ,"y")
ga_gambler              = GarnishAllow([],"" ,"" ,"" ,"" ,"y","" ,"" )
ga_progamer             = GarnishAllow([],"y","" ,"" ,"" ,"" ,"" ,"" )
ga_teacher              = GarnishAllow([],"" ,"" ,"" ,"" ,"" ,"" ,"y")
ga_farmer               = GarnishAllow([],"" ,"" ,"y","" ,"" ,"y","" )
ga_livestock_farmer     = GarnishAllow([],"" ,"" ,"y","" ,"" ,"y","" )
ga_director             = GarnishAllow([],"y","y","y","y","y","" ,"y")
ga_model                = GarnishAllow([],"y","y","" ,"y","y","" ,"y")
ga_guard                = GarnishAllow([],"" ,"" ,"y","" ,"" ,"y","y")
ga_patient              = GarnishAllow([],"" ,"" ,"" ,"" ,"" ,"" ,"" )
ga_the_dying            = GarnishAllow([],"y","y","y","" ,"" ,"" ,"y")
ga_school_club_member   = GarnishAllow([],"" ,"" ,"" ,"" ,"" ,"" ,"y")
ga_journalist           = GarnishAllow([],"y","" ,"y","" ,"" ,"y","y")
ga_composer             = GarnishAllow([],"y","y","y","y","y","" ,"y")
ga_dancer               = GarnishAllow([],"y","y","y","" ,"y","" ,"y")
ga_barista              = GarnishAllow([],"" ,"y","y","" ,"" ,"y","" )
ga_masseuse             = GarnishAllow([],"" ,"" ,"" ,"" ,"" ,"y","" )
ga_hotel_staff          = GarnishAllow([],"" ,"" ,"y","" ,"" ,"y","" )
ga_photographer         = GarnishAllow([],"y","" ,"" ,"" ,"y","" ,"" )
ga_game_designer        = GarnishAllow([],"y","" ,"" ,"" ,"y","" ,"" )
ga_engineer             = GarnishAllow([],"y","" ,"" ,"y","y","" ,"y")


# Complete .mcdonalds above. y = "yes", blank = "no".  Make sure the spaces and letter positions are aligned with ab_rock_musician.


#If you had lost your emotions, you wouldn't
#If you want to die, you wouldn't

#Make a stamp card.


# プチモニの横だ
#  プチモニ知ってるんだ



# posing
#  君付け (コットン)
###########################################################################################################

@dataclass
class Binary2:
    ALL_BINARY2: ClassVar[List['Binary2']] = []
    high_intelligence:str
    high_strength:str
    extrovert_introvert:str
    sport:str
    showbiz:str
    art:str
    service:str
    retail:str
    manufacturing:str
    looks_job:str


    effort:list
    suffer:list
    appear:list
    action:list
    slump:list

    charity:list
    modifier:list
    too_late:list
    just_a:list
    brand:list # agent_output.pyにおいて使われてない
    southpaw:list
    why_could_this_guy:list
    pride:list
    pressure:list
    rev_adj:list


    def __post_init__(self):
        Binary2.ALL_BINARY2.append(self)
        if self.high_intelligence or self.art:
           self.rev_adj.append(["<a href='state#mild_yankee'>mild_yankee</a>", "<a href='state#illiteracy'>illiteracy</a>"])
        if self.high_intelligence:
           self.too_late.append(["eating blue fish", "reading a thick book", "trying to solve a Rubik’s Cube", "doing mindfulness", "watching TED Talks", "doing doing flash ANZAN", "playing chess","Watch documentaries about scientists"])# print(f"comedy script * Ali: I suddenly had to take an IQ test in an hour. So I'm {enhancement_intelligence} quickly now. - Bob: It's too late.") Add new 10 ones without any explanations.
           self.just_a.append(["不健康な","暗い", "大卒の", "目の悪い", "痩せた", "太った", "繊細な", "暗い", "インドアな", "几帳面な", "体力のない", "理屈っぽい"])
           self.brand.append("Nootropics")
        if self.high_strength:
           self.rev_adj.append(["<a href='state#unhealthy'>unhealthy</a>", "<a href='state#middle_aged'>middle_aged</a>"])
           self.too_late.append(["doing push ups", "eating a low-calorie diet", "hiking up the stairs instead of using the elevator", "staying hydrated with water","drinking protein shakes", "eating energy bars","Watch documentaries about athletes"])# print(f"comedy script * Ali: I suddenly had to take an physical fitness test in an hour. So I'm {enhancement_physical} quickly now. - Bob: It's too late.") Add new 10 ones without any explanations.
           self.just_a.append(["健康な","明るい", "高卒の", "ガタイがいい", "痩せた", "背が高い", "色黒な", "ストリート系の", "社交的な", "姿勢のいい", "日焼けした", "アウトドアな", "体育会系の", "食事に気を使ってる"])
           self.brand.append("Doping material")
        if self.art:
           self.just_a.append(["物憂げな", "詩的な", "悲観的な", "自罰的な"])
        if self.showbiz:
           self.slump.append(["Trying to be the one who explains.", "Start a restaurant.", "Trying to be the one who teaches.", "Appearing in advertisements for online casinos and marijuana.", "Run for local council elections.", "Suddenly start talking about environmental protection and feminism.", "Appear in a show at a pachinko parlor.", "Releasing a memoir that nobody asked for.", "Getting involved in reality TV for a comeback.", "Starting a clothing line that flops spectacularly.", "Collaborating with lesser-known artists in desperate attempts to stay relevant.", "Suddenly becoming an advocate for obscure causes nobody cares about."])
        if self.showbiz or self.service:
           self.charity.append("invite")
        if self.showbiz:
           self.charity.append("present one's goods")
        if self.looks_job:
           self.rev_adj.append("<a href='state#ugly'>ugly</a>")
        if self.service:
           self.charity.append("offer free service")
        if self.retail or self.manufacturing or self.showbiz or self.art:
           self.charity.append("present one's work")
        if self:
           self.modifier.append(["veteran", "famous", "self-taught", "chief", "self-employed"])
           self.brand.append(["lesson", "text"])
        if self.showbiz:
           self.modifier.append(["Affiliated with his private agency", "Exclusive"])
        if self.sport:
           self.modifier.append(["first team", "captain"])
        if self.extrovert_introvert == "e":
            self.rev_adj.append(["<a href='state#introvert'>introvert</a>", "<a href='state#nerd'>nerd</a>"])
        if self.extrovert_introvert == "i" and not self.high_intelligence and not self.art:
            self.rev_adj.append("<a href='state#mild_yankee'>mild_yankee</a>")
        if self.art:
            self.effort.append(["(art_sports == 'a')","Sketching ideas in a notebook daily","Traveling for inspiration", "Abstinence", "Sublimating one's trauma into a work of art", "Use LSD", "Meditation", "Keeping a dream journal", "Creating art in the dark"])
            self.suffer.append(["(art_sports == 'a')","A lack of depth that comes from a lack of life experience.","Emotionless","Become a victim of plagiarism", "Conflict with producers", "Commercialism", "Creator's block", "Drug addiction", "alcohol addiction", "sex addiction", "Cannot surpass one's rival", "Cannot surpass one's past self", "Paparazzi", "Stalkers", "Stalkers", "Antis", "Paparazzis", "Plagiarism damage", "Alleged plagiarism", "Plagiarism of his past self", "Commercialism", "Pressure to only work in popular genres", "Creators' block", "Out of ideas", "Generative AI"])
            self.action.append(["(art_sports == 'a')","Hate creators who have fallen into commercialism", "Adopting a Child from the Third World", "Being in a dark room","Getting involved in a cult", "Being an alcoholic", "Addicting drug and sex", "Has suicidal thoughts", "Support the American Democratic Party.", "Being interested in environmental issues.", "Getting involved in the Scientology or SGI", "Being atheist or non-religious.", "Expressing support or opposition to abortion.", "Creating art as a form of protest", "Challenging societal norms through provocative installations"])
        if self:
            self.effort.append(["(GENERAL)","Quit smoking and drinking", "Experience different activities", "Seek advice.", "Conflict with others about the way one do things.", "Sacrifice family, friend and lover.", "Become estranged from a partner.", "Become ill and get injured from overwork.", "Quit college or work to pursue the dream.", "Sell personal belongings for Activity funds"])
            self.suffer.append(["(GENERAL)","Slump", "Children's school fees", "Loans for activities"])

        if self.high_intelligence:
            self.southpaw.append(["has savant syndrome", "is a graduate of MIT", "has an IQ of 150"])
        if self.high_strength:
            self.southpaw.append(["is black", "is white", "has gigantism", "is of a martial race", "is of Samoan ethnicity"])
        if self.sport:
            self.southpaw.append(["is southpaw", "is tall", "is ambidextrous", "has six fingers"])
        if self.art:
            self.southpaw.append(["has eidetic memory", "has six fingers", "has perfect pitch", "has synesthesia", "has schizophrenia"])

'''
@dataclass # Align text and whitespace with existing instances.
class Binary2: # yes = "y", no = blank.
    high_intelligence:str
    high_strength:str
    extrovert_introvert:str
    sport:str
    showbiz:str
    art:str
    service:str
    retail:str
    manufacturing:str
    looks_job:str
'''



b2_rock_musician        = Binary2("" ,"" ,"e","" ,"y","y","" ,"" ,"" ,"y",[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_singer               = Binary2("" ,"" ,"" ,"" ,"y","y","" ,"" ,"" ,"y",[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_classical_musician   = Binary2("" ,"" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_comedian             = Binary2("" ,"" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],["<a href='state#unfunny'>unfunny</a>"])
b2_novelist             = Binary2("y","" ,"i","" ,"" ,"y","" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_artist               = Binary2("y","" ,"i","" ,"" ,"y","" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_doctor               = Binary2("y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_researcher           = Binary2("y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_actor                = Binary2("" ,"" ,"e","" ,"y","y","" ,"" ,"" ,"y",[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_chef                 = Binary2("" ,"" ,"" ,"" ,"" ,"" ,"y","y","y","" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_athlete              = Binary2("" ,"y","e","y","y","" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_violent_criminal     = Binary2("" ,"y","e","" ,"" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_cyber_criminal       = Binary2("y","" ,"i","" ,"" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_thief                = Binary2("" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_examinee             = Binary2("y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_gambler              = Binary2("y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_progamer             = Binary2("" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_teacher              = Binary2("y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_farmer               = Binary2("" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_livestock_farmer     = Binary2("" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_director             = Binary2("y","" ,"" ,"" ,"y","y","" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_model                = Binary2("" ,"" ,"e","" ,"y","" ,"" ,"" ,"" ,"y",[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_guard                = Binary2("" ,"y","e","" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_patient              = Binary2("" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_the_dying            = Binary2("", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_school_club_member   = Binary2("" ,"y","e","y","" ,"" ,"" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_journalist           = Binary2("y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_idol                 = Binary2("" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"y",[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_composer             = Binary2("" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_dancer               = Binary2("" ,"y","e","" ,"y","y","" ,"" ,"" ,"y",[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_barista              = Binary2("" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_masseuse             = Binary2("" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_hotel_staff          = Binary2("" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_craftsman            = Binary2("" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_photographer         = Binary2("" ,"" ,"" ,"" ,"y","" ,"y","" ,"" ,"" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_game_designer        = Binary2("y","" ,"i","" ,"" ,"" ,"" ,"" ,"y","" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])
b2_engineer             = Binary2("y","" ,"i","" ,"" ,"" ,"" ,"" ,"y","" ,[],[],[],[],[],[],[],[],[],[],[],[],[],[],[])



# Align the letters and spaces to the existing instances. Start answer with ```python



###########################################################################################################

# Stereotypical scenes of some kind of conflict/heavy responsibility.

b2_rock_musician        .pressure+=["Sudden vacancy"]
b2_singer               .pressure+=["Sudden vacancy"]
b2_classical_musician   .pressure+=["Sudden vacancy"]
b2_comedian             .pressure+=["Sudden vacancy"]
b2_novelist             .pressure+=["Sudden vacancy", "Ghost writer"]
b2_artist               .pressure+=[]
b2_doctor               .pressure+=["Sudden illness", "Zombie pandemic", "Triage"]
b2_researcher           .pressure+=["Death game", "Zombie pandemic", "Bomb defusal", "Mystery Deduction"]
b2_actor                .pressure+=["Sudden vacancy"]
b2_chef                 .pressure+=[]
b2_athlete              .pressure+=["Sudden vacancy", "Death game", "Life saving", "An athlete promises a home run to a child who is afraid of surgery."]
b2_violent_criminal     .pressure+=["Death game", "Working with Undercover Agents"]
b2_cyber_criminal       .pressure+=["Death game", "Working with Undercover Agents"]
b2_thief                .pressure+=["Working with Undercover Agents"]
b2_examinee             .pressure+=[]
b2_gambler              .pressure+=["Death game"]
b2_progamer             .pressure+=["Sudden vacancy"]
b2_teacher              .pressure+=[] # Add new items.
b2_farmer               .pressure+=["Reconstruction after nuclear war"]
b2_livestock_farmer     .pressure+=["Reconstruction after nuclear war"]
b2_director             .pressure+=[]
b2_model                .pressure+=[]
b2_guard                .pressure+=[] # Add new items
b2_patient              .pressure+=["Triage", "An athlete promises a home run to a child who is afraid of surgery."]
b2_the_dying            .pressure+=["Triage"]
b2_school_club_member   .pressure+=["Sudden vacancy"]
b2_journalist           .pressure+=[] # Add new items.
b2_idol                 .pressure+=[]
b2_composer             .pressure+=[]
b2_dancer               .pressure+=[]
b2_barista              .pressure+=[]
b2_masseuse             .pressure+=[]
b2_hotel_staff          .pressure+=[]
b2_craftsman            .pressure+=[]
b2_photographer         .pressure+=[]
b2_game_designer        .pressure+=[]
b2_engineer             .pressure+=["Bomb defusal", "Reconstruction after nuclear war"]




###########################################################################################################

# titles of superior. Add new items
b2_rock_musician      .modifier+=["leader", "soloist"]
b2_singer             .modifier+=["center position"]
b2_classical_musician .modifier+=["soloist"]
b2_comedian           .modifier+=["headliner"]
b2_novelist           .modifier+=[]
b2_artist             .modifier+=[]
b2_doctor             .modifier+=[]
b2_researcher         .modifier+=[]
b2_actor              .modifier+=["starring"]
b2_chef               .modifier+=["owner chef"]
b2_athlete            .modifier+=["first team"]
b2_violent_criminal   .modifier+=["repeat offender", "wanted criminal"]
b2_cyber_criminal     .modifier+=["repeat offender", "wanted criminal"]
b2_thief              .modifier+=["repeat offender", "wanted criminal"]
b2_examinee           .modifier+=["A grade", "passed for active duty"]
b2_gambler            .modifier+=["high roller"]
b2_progamer           .modifier+=["first team"]
b2_teacher            .modifier+=[]
b2_farmer             .modifier+=["organic"]
b2_livestock_farmer   .modifier+=["organic", "free range"]
b2_director           .modifier+=[]
b2_model              .modifier+=["runway", "exclusive"]
b2_guard              .modifier+=[]
b2_patient            .modifier+=["severe", "chronic"]
b2_the_dying          .modifier+=["severe", "chronic"]
b2_school_club_member .modifier+=["first team"]
b2_journalist         .modifier+=["independent "]
b2_idol               .modifier+=["center position"]
b2_composer           .modifier+=[]
b2_dancer             .modifier+=["soloist"]
b2_barista            .modifier+=[]
b2_masseuse           .modifier+=[]
b2_hotel_staff        .modifier+=[]
b2_photographer       .modifier+=[]
b2_game_designer      .modifier+=[]
b2_engineer           .modifier+=[]

###########################################################################################################

b2_rock_musician      .just_a+=["薬をやっている", "ステージ慣れした", "MCスキルが高い", "声の大きい"]
b2_singer             .just_a+=["邦楽が好きな", "声が良い", "リズム感のある", "ステージ慣れした", "カラオケ上手な", "表現力豊かな", "感性の豊かな", "MCスキルが高い", "声の大きい"]
b2_classical_musician .just_a+=["家が金持ってた", "クラシック通な", "ステージ慣れした"]
b2_comedian           .just_a+=["明るい", "ステージ慣れした", "声の大きい"]
b2_novelist           .just_a+=["メンヘラな", "文章力のある"]
b2_artist             .just_a+=["メンヘラな", "創造力豊かな", "感性の豊かな", "表現力のある"]
b2_doctor             .just_a+=["物知りな", "人体に詳しい", "冷静な判断ができる"]
b2_researcher         .just_a+=["物知りな", "専門知識のある"]
b2_actor              .just_a+=["映画好きな", "表現力豊かな", "感情表現の上手い", "カメラ慣れした", "声の大きい"]
b2_chef               .just_a+=["食事に気を使ってる", "味覚の鋭い"]
b2_athlete            .just_a+=["食事に気を使ってる", "体力のある", "筋肉質な", "反射神経の良い", "競争心の強い", "ストイックな", "体の柔軟な", "スポーツマンシップのある", "チームワークの良い", "瞬発力のある"]
b2_violent_criminal   .just_a+=["反社会的な", "冷酷な", "予測不可能な"]
b2_cyber_criminal     .just_a+=["反社会的な", "冷酷な", "計画的な", "技術に詳しい", "リスクを取る", "情報収集能力の高い", "デジタルネイティブな"]
b2_thief              .just_a+=["狡猾な", "計画的な", "身軽な", "逃げ足の速い", "変装のうまい", "神出鬼没の"]
b2_examinee           .just_a+=["計画的な", "記憶力の良い", "自己管理のできる", "知識欲の強い", "粘り強い"]
b2_gambler            .just_a+=["債務者の","リスク好きな", "運の良い", "勝負強い"]
b2_progamer           .just_a+=["ゲーム好きな", "反射神経の良い", "チームワークの良い", "競争心の強い"]
b2_teacher            .just_a+=["教育熱心な", "子供思いの"]
b2_farmer             .just_a+=["広い土地持ってる", "田舎に住んでる"]
b2_livestock_farmer   .just_a+=[b2_farmer.just_a]
b2_director           .just_a+=["映画好きな", "表現力豊かな", "感情表現の上手い"]
b2_model              .just_a+=["おしゃれな","写真映えする","身だしなみの良い","スタイリッシュな","魅力的な","立ち振る舞いの美しい","体型維持に気を使う","流行に敏感な","見た目の良い"]
b2_guard              .just_a+=["防犯意識の高い", "監視カメラに詳しい", "巡回ルートを知り尽くした", "防犯ベルに敏感な", "警戒心の強い", "観察力の鋭い", "護身術に長けた", "緊急時の対応力がある", "危険予知能力が高い", "規律正しい", "冷静沈着な", "状況判断力に優れた", "チームワークに優れた"]
b2_patient            .just_a+=["調子の悪い"]
b2_the_dying          .just_a+=["調子の悪い"]
b2_school_club_member .just_a+=["食事に気を使ってる", "体力のある", "筋肉質な", "反射神経の良い", "競争心の強い", "ストイックな", "体の柔軟な", "スポーツマンシップのある", "チームワークの良い", "瞬発力のある"]
b2_journalist         .just_a+=["文章力のある","情報収集能力の高い","コミュニケーション能力の高い","好奇心旺盛な","締め切りを守れる","客観的な視点を持つ"]
b2_idol               .just_a+=[]
b2_composer           .just_a+=["音楽的才能のある", "創造力豊かな", "感性の豊かな", "音楽理論に詳しい", "楽器演奏のできる", "聴覚の鋭い", "リズム感のある", "和声学に精通した", "音楽史に詳しい", "編曲能力の高い"]
b2_dancer             .just_a+=["表現力豊かな", "リズム感のある", "体の柔軟な", "ステージ慣れした", "感情表現の上手い", "ダンス好きな", "チームワークの良い"]
b2_barista            .just_a+=["コーヒーに詳しい", "接客スキルの高い", "手先の器用な", "味覚の鋭い", "清潔感のある", "効率的な", "朝型の", "コミュニケーション能力の高い", "忍耐強い", "アート感覚のある"]
b2_masseuse           .just_a+=["解剖学に詳しい", "手先の器用な", "体力のある", "コミュニケーション能力の高い", "清潔感のある", "気配りのできる", "忍耐強い", "リラックスさせる能力のある", "身体感覚の鋭い"]
b2_hotel_staff        .just_a+=["接客スキルの高い", "言語能力の高い", "清潔感のある", "気配りのできる"]
b2_photographer       .just_a+=["構図に優れた", "編集スキルの高い"]
b2_game_designer      .just_a+=[]
b2_engineer           .just_a+=[]
###########################################################################################################

b2_singer               .effort+=[]
b2_classical_musician   .effort+=[]
b2_rock_musician        .effort+=[]
b2_comedian             .effort+=["People-watching", "Turning personal tragedies into jokes", "Making fun of themselves to deflect criticism", ]
b2_novelist             .effort+=["Researching historical events for accuracy"]
b2_artist               .effort+=[]
b2_doctor               .effort+=[]
b2_researcher           .effort+=[]
b2_actor                .effort+=["Method acting", "Physical transformation for roles", "Taking specialized classes (e.g., dance, martial arts)", "Performing own stunts","Extensive research for historical roles", "Learning new languages for international productions", "Undergoing extreme weight changes","Continues to play the role in his private life."]
b2_chef                 .effort+=[]
b2_athlete              .effort+=["Intense physical training", "Strict diet regimen", "Ice baths for recovery", "Altitude training", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness", "Video Analysis"]
b2_school_club_member   .effort+=[b2_athlete.effort]
b2_progamer             .effort+=["Intense physical training", "Strict diet regimen", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"]
b2_gambler              .effort+=["Learning math", "Creating and checking statistical data"]
b2_examinee             .effort+=["Study all night", "Making flashcards", "Memorizing"]
b2_teacher              .effort+=["Creating engaging lesson plans", "Mentoring students outside of class hours", "Pursuing advanced degrees", "physical punishment"]
b2_craftsman            .effort+=["Practicing techniques for hours daily", "Studying traditional methods", "Experimenting with new materials", "Apprenticeship under a master", "Perfecting a single skill for years", "Attending specialized workshops"]
b2_violent_criminal     .effort+=["Study law", "Remove his fingerprints", "Study security technologies"]
b2_cyber_criminal       .effort+=["Learning multiple programming languages","Studying network security protocols","Practicing social engineering techniques","Keeping up with latest cybersecurity trends","Developing custom malware and exploits","Participating in hacking forums and communities","Conducting extensive reconnaissance on targets","Mastering encryption and anonymization tools","Building and maintaining botnets","Reverse engineering software and systems"]
b2_thief                .effort+=["Studying security systems", "Practicing lock-picking skills", "Practicing stealth techniques", "Networking with other criminals", "Using disguises and false identities", "Conducting reconnaissance on targets", "Managing stolen goods and laundering money"]


b2_farmer               .effort+=["Waking up before dawn", "Implement organic farming.", "Working long hours in all weather conditions", "Continuous learning about crop science and animal husbandry", "Maintaining and repairing equipment", "Soil management and conservation practices", "Implementing sustainable farming techniques", "Adapting to changing climate patterns", "Market research and business planning"]
b2_livestock_farmer     .effort+=[b2_farmer.effort]
b2_director             .effort+=["Storyboarding extensively", "Scouting locations", "Studying others' films and classic films", "Experimenting with new filming techniques", "Collaborating closely with actors and crew", "Fundraising for independent projects", "Attending film festivals", "Repeatedly does retakes"]
b2_model                .effort+=["Networking with industry professionals", "Maintaining a strict diet and fitness regimen", "Practicing poses and walks", "Attending casting calls and auditions regularly"]
b2_guard                .effort+=["Physical fitness training", "Self-defense classes", "Surveillance skills development", "Conflict resolution training", "First aid certification", "Night shifts", "Continuous situational awareness"]
b2_patient              .effort+=["Participating in experimental treatments", "Seeking alternative therapies", "Maintaining hope despite grim prognoses", "Creating memory books or videos for loved ones", "Advocating for research funding", "Joining support groups for rare diseases", "Traveling long distances for specialized care", "Managing complex pain regimens", "Adapting living spaces for declining mobility", "Planning end-of-life care", "Fundraising for medical expenses", "Documenting personal experiences for future patients"]
b2_the_dying            .effort+=[b2_patient.effort]

b2_journalist           .effort+=["Investigative fieldwork","Building and maintaining a network of sources","Fact-checking","shorthanding","Developing expertise in specific beats or topics","Risking personal safety for stories in dangerous areas","Working irregular hours to meet deadlines","Maintaining objectivity in reporting"]
b2_idol                 .effort+=[]
b2_composer             .effort+=["Listening to diverse genres of music","Studying music theory and composition techniques","Experimenting with different instruments","Collaborating with other musicians","Attending concerts and music festivals","Practicing sight-reading and ear training","Composing in unconventional environments","Analyzing scores of great composers",]
b2_dancer               .effort+=["Rigorous daily physical training","Practicing choreography for hours","Cross-training in different dance styles","Flexibility and stretching exercises","Strength and conditioning workouts","Studying anatomy and kinesiology","Maintaining proper sleep schedule for recovery","Regular physiotherapy and massage","Perfecting technique through repetition","Attending workshops and masterclasses","Analyzing performance videos for improvement","Developing stage presence and expression","Learning music theory and rhythm",]
b2_barista              .effort+=["Practicing latte art for hours", "Studying coffee bean varieties and origins", "Perfecting brewing techniques", "Developing a refined palate through cupping sessions", "Attending barista competitions", "Experimenting with new flavor combinations"]
b2_masseuse             .effort+=["Studying anatomy and physiology", "Developing hand and finger strength", ]
b2_hotel_staff          .effort+=["Memorizing guest preferences and names", "Practicing multiple languages for international guests", "Learning about local attractions and services", "Perfecting the art of room presentation", "Enhancing interpersonal skills for diverse guest interactions"]
b2_photographer         .effort+=["Studying color theory and its application in photography", "Attending photography workshops and seminars", "Building a diverse portfolio across multiple genres", "Learning to use various types of camera equipment"]

b2_game_designer        .effort+=[]
b2_engineer             .effort+=[]

# Define b2_photographer .effort. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

###########################################################################################################


l_suffer_script             =["Lacking hints","Lacking a clear message","Poor character development","Weak plot structure","Unrealistic dialogue","Lack of conflict","Cliche or predictable storylines","Poor world-building","Underdeveloped themes","Weak endings"]
l_suffer_game               =["Luck-based", "Unbalanced ","Lack of content updates","Limited customization options","Pay-to-win elements or microtransactions","Lack of endgame content","Repetitive gameplay","Poor UI design","Lack of player agency","Buggy or glitchy performance","Limited replay value","Inconsistent difficulty levels","Weak or unengaging narrative"]
l_suffer_instrumental       =["Emotionless","lacking a clear message","Inability to play in different styles","Poor improvisation skills","Lack of stage presence","Inability to tune instrument properly"]

b2_singer               .suffer+=["Lack of stage presence","Lack of versatility","The song arrangements are lacking", "Uninspired Lyrics", "Repetitive Melodies"]
b2_classical_musician   .suffer+=[]
b2_rock_musician        .suffer+=[]
b2_comedian             .suffer+=["Dealing with cancel culture","Bombing on stage","Hecklers in the audience","Offensive jokes backfiring","Difficulty adapting to different audiences","Fear of being replaced by newer comedians", "Being typecast in a particular style of comedy", ]
b2_novelist             .suffer+=["Deadline", l_suffer_script]
b2_artist               .suffer+=["Emotionless","lack of creativity","unoriginal style","lack of craftsmanship", "Struggles with Proportions"  ,  "Weak anatomy knowledge"]
b2_doctor               .suffer+=["The trauma of not being able to save a patient's life."]
b2_researcher           .suffer+=["Plagiarism", "Not being able to get research funding", "Has white hair"]
b2_actor                .suffer+=["Physical injuries from stunts", "Pressure to maintain a certain physical appearance","The damage caused by method acting", "Unconvincing Performances", "Difficulty with Accents/Dialects","Overacts","lack of stage presence","Lack of character depth","Inability to improvise","Lack of chemistry with co-stars", l_suffer_script]
# Define suffer_masseuse  in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



# Extend 10 new items in suffer_hotel_staff in English. I will run your reply through the eval function, so don't write anything unnecessary.




b2_violent_criminal     .suffer+=[]
b2_cyber_criminal       .suffer+=["Legal consequences and imprisonment","Constant paranoia of being caught","Difficulty maintaining personal relationships due to secrecy","Ethical dilemmas and moral conflicts","Burnout from constant vigilance","Isolation from mainstream society","Struggle to find legitimate employment after being caught","Mental health issues from high-stress lifestyle","Financial instability due to illegal income sources","Physical health problems from long hours at computer","Addiction to the thrill of hacking","Trust issues within hacking communities","Difficulty adapting to rapidly changing technology","Constant fear of rival hackers or law enforcement"]
b2_thief                .suffer+=["Fear of arrest", "Betrayal by accomplices", "Loss of trust from loved ones", "Constantly looking over one's shoulder", "Living in poverty due to criminal activities", "Guilt from harming others", "Isolation from society", "Struggles with addiction", "Conflict with law enforcement", "Inability to escape one's past", "being wanted "]

b2_dancer               .suffer+=[]
b2_chef                 .suffer+=[]
b2_athlete              .suffer+=["Career-ending injuries","Pressure from fans and media", "Doping scandals", "Burnout", "Post-retirement depression", "Eating disorders", "Chronic pain", "Concussions and long-term brain damage", "Stalker"]
b2_school_club_member   .suffer+=["Pressure to perform well in competitions","Conflict with club members","Strain from balancing academics and club activities","Injury from overtraining","Lack of recognition for hard work","Unmet expectations from coaches","Feeling overshadowed by talented members","Lack of motivation during tough times","Pressure to follow strict training regimens","Isolation from non-club peers","bodily punishment","Coping with the fear of not improving",]
b2_progamer             .suffer+=[l_suffer_game, "Repetitive Strain Injury", "Carpal Tunnel Syndrome", "Eye strain",   "Addiction to gaming"]
b2_gambler              .suffer+=["Addiction to gambling", "Financial ruin", "Depression and anxiety", "Lying to cover losses", "Chasing losses", "Neglecting work or family responsibilities", "Legal troubles", "Substance abuse as a coping mechanism", "Suicidal thoughts"]
b2_examinee             .suffer+=["STEM inferiority complex", "Exam pressure","Health issues due to long study hours","Intense competition","Balancing study and personal life","Fear that one failure will affect future","Pressure from parents and teachers","Self-loathing and loss of confidence","Deterioration of relationships with friends"]
b2_teacher              .suffer+=["punk", "Pressure from parents and administration",  "Lack of autonomy in curriculum decisions", "Testing pressure", "Large class sizes", "bullying"]
b2_craftsman            .suffer+=["Repetitive strain injuries", "Lack of successors", "Exposure to harmful materials", "Competition from mass-produced items", "Difficulty in finding apprentices", "Financial instability", "Long hours of solitary work", "burnout", "Struggles with modernization and technology"]
b2_farmer               .suffer+=["Crop failures due to weather", "Market price fluctuations", "Equipment breakdowns", "Debt from loans", "Physical strain and injuries", "Eviction request", "Isolation in rural areas", "Pressure to adopt new technologies", "Regulatory challenges", "Competition from large agribusinesses", "Succession planning difficulties"]
b2_livestock_farmer     .suffer+=[b2_farmer.suffer]
b2_director             .suffer+=["Budget constraints", "Creative differences with producers", "Pressure to meet box office expectations", "Negative critical reviews", "Challenges with difficult actors", "Technical issues during filming", "Post-production problems", "Distribution hurdles", "Balancing artistic vision with commercial viability", l_suffer_script]
b2_model                .suffer+=["Body image issues", "Pressure to maintain unrealistic beauty standards", "Casting couch", "Constant scrutiny of physical appearance", "Age-related career decline", "Eating disorders", "Social media harassment"]
b2_guard                .suffer+=["Monotonous work", "Long hours and night shifts", "Lack of recognition", "Stress from constant vigilance", "Physical strain from standing for long periods", "Dealing with aggressive individuals", "Post-traumatic stress from violent incidents", "Social isolation due to irregular work hours"]
b2_patient              .suffer+=["Chronic pain", "Loss of independence", "Social isolation", "Depression and anxiety", "Recurrence", "Financial burden of treatment", "Side effects from medications", "Guilt over being a burden to family", "Loss of identity and purpose", "Fear of the unknown future", "Difficulty in maintaining relationships", "Cognitive decline", "Physical deterioration", "Fatigue and exhaustion", "Frustration with healthcare system", "Grief over lost opportunities and experiences", "Stigma associated with their condition", "Difficulty in planning for the future", "Constant medical appointments and procedures", "Loss of privacy due to care needs", "Existential crisis and questioning of life's meaning", "Having to give up sports", "Having to quit work"]
b2_the_dying            .suffer+=[b2_patient.suffer]
b2_journalist           .suffer+=["Pressure to meet tight deadlines","Ethical dilemmas in reporting","Threats to personal safety in dangerous locations","Difficulty maintaining objectivity","Stress from covering traumatic events","Pressure to produce clickbait content","Difficulty verifying sources in the age of misinformation","Pressure to be active on social media","Burnout from constant news cycle","Criticism and harassment from public figures or readers","Difficulty accessing reliable sources","Pressure to break news first, potentially compromising accuracy",]
b2_idol                 .suffer+=[]
b2_composer             .suffer+=["Lack of originality in compositions","Inability to translate ideas into music","Difficulty in creating memorable melodies","Poor orchestration skills","Struggle with complex harmonies","Inability to meet deadlines for commissioned works","Criticism for experimental or avant-garde pieces","Difficulty in balancing artistic vision with commercial demands","Difficulty in finding performers or orchestras to play compositions",]
b2_barista              .suffer+=["Burns from hot liquids and equipment"]
b2_masseuse             .suffer+=["Repetitive strain injuries"]
b2_hotel_staff          .suffer+=["Dealing with rude or demanding guests"]
b2_photographer         .suffer+=["Physical strain from carrying heavy equipment",  "Emotional toll from capturing sensitive or traumatic events", "Weather-related challenges during outdoor shoots", "Loneliness during solo travel for assignments"]

b2_game_designer        .suffer+=[]
b2_engineer             .suffer+=[]

# Define b2_photographer .suffer. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.

###########################################################################################################


b2_singer                 .appear+=["Many piercings", "Many tattoos", "Colorful hair", "split tongue"]
b2_classical_musician     .appear+=["Formal black attire","Bow tie","Slicked-back hair","Round glasses","Pale complexion","Thin frame"]
b2_rock_musician          .appear+=["Many piercings", "Many tattoos", "Colorful hair", "split tongue"]
b2_comedian               .appear+=[]
b2_novelist               .appear+=["Wears a samue", "Has a beard", "Thin and pale", "Messy hair"]
b2_artist                 .appear+=["Many piercings", "Many tattoos", "Colorful hair"]
b2_doctor                 .appear+=["White coat", "Messy hair"]
b2_researcher             .appear+=["White coat", "Messy hair", "Has bags under one's eyes", "Carries around a clipboard", "using a wheelchair"]
b2_actor                  .appear+=[]
b2_chef                   .appear+=["Kaiser moustache", "Being fat", "Wears a neckerchief", "Has a thick accent"]
b2_violent_criminal       .appear+=["Unkempt appearance", "Wild eyes", "Scars or burn marks", "Twitchy movements", "Wears all black", "Clown-like makeup", "Disheveled hair", "Pale skin", "Bloodstained clothing", "Ritualistic tattoos", "Leather gloves", "Creepy mask"]
b2_cyber_criminal         .appear+=["Anonymas mask", "Hoodie or dark clothing","Multiple computer screens","Pale complexion from lack of sunlight","Dark circles under eyes","Messy or unkempt hair","Fingerless gloves","Glasses or blue light glasses","Headphones or earbuds","Energy drinks or coffee cups","Stickers on laptop","Mechanical keyboard","Wrist brace","Fidget toys","Cyberpunk-style accessories","Backpack with tech gear","Smartwatch or fitness tracker","Graphic t-shirts with tech or hacker slogans"]
b2_thief                  .appear+=["Dark clothing", "Hooded sweatshirt", "Face partially covered", "Sneakers for quiet movement", "Gloves to avoid leaving fingerprints", "Shifty eyes", "Nervous demeanor", "Backpack or duffel bag for carrying loot", "Quick, agile movements", "Camouflage patterns or tactical gear", "Elegant cloak or cape", "Mask covering the eyes", "Stylish attire with dark colors", "Gloves for stealth", "Lightweight shoes for silent movement", "Mysterious aura", "Accessories like a cane or dagger", "Emphasis on agility and grace", "Shadowy presence", "Intricate patterns on clothing"]


b2_athlete                .appear+=["Muscular build", "Athletic wear", "Sweatbands", "Sports gear", "Taped joints or limbs", "Shaved body", "Visible tan lines", "Team jersey or uniform", "Dreadlocks"]
b2_school_club_member     .appear+=["Casual school uniform","Backpack with club patches","Sweatpants or athletic wear","Team colors or logos","Wristbands or headbands","Enthusiastic expressions","Stickers or pins on bags","Sweaty hair","Energy drinks or snacks in hand","Temporary tattoos or face paint for events","Team spirit accessories like hats or scarves","Casual shoes suitable for activities","Hair tied back or styled for practicality","Friendship bracelets or charms",]
b2_gambler                .appear+=["Disheveled appearance", "Dark circles under eyes", "Nervous twitches", "Flashy jewelry", "Expensive watch", "Rumpled suit", "Cigarette in hand", "Fidgeting with chips or cards", "Sunglasses indoors", "Sweaty brow", "Loosened tie", "Rolled-up sleeves", "Has a red pencil on his ear."]
b2_progamer               .appear+=["Headset", "Gaming chair", "Energy drinks", "Junk food", "Eyeglasses", "Acne", "Poor posture", "Headaches", "Back pain", "Wrist pain", "Messy hair", "Dark circles under eyes", "Skinny build", "Multiple monitors", "RGB lighting", "Wrist brace"]
b2_teacher                .appear+=["Glasses", "Cardigan sweater", "Sensible shoes", "Messy bun or ponytail", "Lanyard with ID badge", "Tote bag full of papers", "Elbow patches on jacket", "Chalk dust on clothes", "Coffee stains", "Comfortable, modest clothing", "Practical hairstyle", "Minimal makeup", "Wristwatch", "Reading glasses on a chain", "Colorful, quirky accessories"]
b2_craftsman              .appear+=["Leather apron", "Calloused hands", "Rolled-up sleeves", "Safety goggles", "Work boots", "Tool belt", "Weathered skin", "Muscular forearms", "Sawdust or wood shavings on clothes", "Protective gloves", "Bandana or cap", "Rugged, worn clothing", "Pencil behind ear", "Measuring tape clipped to belt", "Beard or mustache"]


# Define b2_photographer .appear. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.



b2_farmer                 .appear+=["Overalls", "Plaid shirt", "Straw hat", "Work boots", "Sunburned skin", "Calloused hands", "Weathered face", "Farmer's tan", "Dirt under fingernails", "Faded jeans", "Bandana", "Belt buckle", "Leather work gloves", "Seed company cap"]
b2_livestock_farmer       .appear+=[b2_farmer.appear]
b2_director               .appear+=["Beret or flat cap", "Thick-rimmed glasses", "Scarf", "Black turtleneck", "Blazer with elbow patches", "Cargo vest with many pockets", "Comfortable, worn-in shoes", "Stubble or well-groomed beard", "Vintage watch", "Messenger bag or satchel", "Sunglasses (even indoors)", "Quirky, statement jewelry", "Fashionable, yet practical clothing", "Artsy, unconventional hairstyle", "Director's chair with name on it", "Viewfinder around neck"]
b2_model                  .appear+=["Tall and slender figure", "High cheekbones", "Long legs", "Perfect skin", "Symmetrical facial features", "Styled hair", "Designer clothing", "High heels", "Minimal makeup", "Manicured nails", "Confident posture", "Sunglasses", "Statement jewelry", "Visible collarbones", "Toned physique"]
b2_guard                  .appear+=["Uniform with badge", "Utility belt", "Earpiece", "Sunglasses", "Crew cut or short hair", "Muscular build", "Stern facial expression", "Combat boots", "Visible tattoos", "Clean-shaven face", "Bulletproof vest", "Name tag", "Flashlight", "Walkie-talkie", "Neatly pressed clothes", "Military-style posture", "Blood type tattoo", "scar"]
b2_patient                .appear+=["Pale complexion", "Significant weight loss", "Hair loss or thinning", "Dark circles under eyes", "Medical devices (e.g., oxygen tank, IV drip)", "Wheelchair or mobility aids", "Visible scars from surgeries", "Swollen limbs or joints", "Yellowing of skin or eyes (jaundice)", "Rashes or skin discoloration", "Tremors or involuntary movements", "Hunched posture", "Hospital gown or comfortable loose clothing", "Medical alert bracelet", "Nasal cannula or face mask", "Bandages or dressings", "Visible port for medication administration", "Sunken cheeks or hollow eyes", "Brittle nails and dry skin", "Bruising from blood draws or injections"]
b2_the_dying              .appear+=[b2_patient.appear]
b2_journalist             .appear+=["Press badge or lanyard","Notebook and pen","Comfortable shoes for field work","Laptop bag or backpack","Smart phone or recording device","Camera","Trench coat","Fedora hat","Glasses or sunglasses","Messenger bag","Microphone","Windbreaker with news outlet logo","Khaki vest with many pockets","Disheveled appearance from long hours","Coffee stains on clothing"]
b2_idol                   .appear+=[]
b2_composer               .appear+=["Formal black attire","Bow tie or cravat","Round glasses","Messy or wild hair","Ink-stained fingers","Slightly disheveled appearance","Eccentric accessories (e.g., colorful scarves)","Pale complexion from long hours indoors","Thoughtful or distant expression","Carries a notebook or sheet music","Wears a beret or other distinctive hat","Has a beard or mustache","Wears comfortable, loose-fitting clothing","Often seen with headphones","Has bags under eyes"]
b2_dancer                 .appear+=["Lean, muscular physique","Flexible body","Excellent posture","Toned legs and arms","Hair in a tight bun or ponytail","Leotards or form-fitting dance wear","Ballet shoes or specialized dance footwear","Leg warmers or warm-up clothes","Minimal jewelry","Natural, stage-ready makeup","Visible muscle definition","Callused feet","Dance bag with spare shoes and accessories","Sweat-wicking clothing","Compression garments for support","Kinesiology tape on joints or muscles"]
b2_barista                .appear+=["Apron with coffee shop logo", "Neat and tidy hair (often tied back)", "Black or earth-toned clothing", "Name tag", "Wristwatch for timing shots", "Tattoos (often visible)", "Ear piercings", "Callused hands from handling hot equipment", "Burn marks on hands or arms", "Coffee stains on clothing", "Neutral-colored nail polish or well-groomed nails", "Minimal jewelry for hygiene reasons"]
b2_masseuse               .appear+=["Comfortable, loose-fitting uniform", "Slip-resistant shoes", "Hair tied back neatly", "Minimal jewelry", "Well-groomed nails (short and clean)", "Subtle, natural makeup (if any)", "Name tag or identification badge", "Wristwatch for timing sessions", "Neutral-colored clothing", "Relaxed and calm facial expression", "Toned arms and hands", "Good posture", "Possible aromatherapy scent", "Soft-soled shoes for quiet movement", "Clean, moisturized hands"]
b2_hotel_staff            .appear+=["Neat, pressed uniform", "Name tag", "Polished shoes", "Well-groomed hair", "Minimal jewelry", "Subtle makeup", "Clean, manicured nails", "Tie or bow tie for men", "Scarf or neckerchief for women", "Professional smile", "Good posture", "Earpiece for communication", "Wristwatch", "Belt with hotel logo", "Crisp white shirt or blouse"]
b2_photographer           .appear+=["Camera around neck", "Multiple lenses in bag", "Comfortable, practical clothing", "Sturdy shoes for long shoots", "Vest with many pockets", "Tripod slung over shoulder", "Memory card holder on belt", "Laptop bag for editing on-the-go", "Weatherproof jacket", "Fingerless gloves for cold shoots", "Baseball cap or sun hat", "Polarizing sunglasses", "Backpack full of gear", "Lens cleaning cloth hanging out of pocket", "Smartwatch for timing shots", "Portable external hard drive"]


###########################################################################################################

b2_rock_musician          .action+=["Suddenly starts writing music on paper", "Hate edited music", "Hate lip syncing", "Writing songs about personal struggles","Engaging with fans during concerts","Throwing guitars during performances","Making spontaneous decisions about setlists","Refusing to play the same song twice in a row","Insisting on using vintage equipment","Hosting impromptu jam sessions"]
b2_singer                 .action+=["Suddenly starts writing music on paper", "Hate edited music", "Hate lip syncing", "Writing songs about personal struggles","Engaging with fans during concerts","Changing lyrics mid-performance",]
b2_classical_musician     .action+=["Suddenly starts writing music on paper", "Hate edited music", "Performing with a strict adherence to tradition"]
b2_comedian               .action+=["Claiming that only they understand true humor.",  "Mocking popular culture while secretly loving it.", "Claiming that comedy should be offensive.", "Refusing to adapt their style for modern audiences.", "Refusing to engage with social media trends.", "Blaming the audience for the lack of laughs.", "Be hostile towards TikTok.", "Hostile to political correctness.", "Dislikes comedians who pander to young people and women", "Being an atheist.",  "Refusing to laugh at other comedians' jokes", "Performing in small, obscure venues to maintain 'authenticity'.","Criticizing the mainstream for lacking originality while secretly wanting to be part of it.","Insisting that comedy is an art form that should not be commercialized.","hostile to comedians who use props.","hostile to any form of censorship in comedy.","Being obsessed with timing and delivery.","Being dismissive of audience reactions.","Being resistant to collaboration with other comedians.",]
b2_novelist               .action+=["Hate teen novels"]
b2_artist                 .action+=[]
b2_doctor                 .action+=["Having a stethoscope draped around their neck at all times","Being overly critical of alternative medicine","Being meticulous about hygiene and cleanliness",]
b2_researcher             .action+=["Starting a religion after overthinking it", "Suddenly starts writing mathematical formulas on the wall.", "Unable to understand others' feelings.", "Forgetting to eat or sleep while working on a problem", "Wearing mismatched or stained clothing", "Carrying around stacks of papers and books everywhere", "Muttering to themselves while pacing"]
b2_actor                  .action+=["Looking down on lighting engineers and cinematographers.""Constantly practicing lines in public","Name-dropping famous directors or actors","Insisting on being called by their character's name","Refusing to break character even off-set","Demanding specific brands of bottled water on set","Throwing tantrums when not given enough screen time","Obsessing over their appearance and plastic surgery",]
b2_athlete                .action+=["Splurge", "Bullying nerds", "Support the Republican Party", "Trash Talk", "meathead", "Partying excessively","Constantly flexing muscles","Overusing sports metaphors in conversation","Ignoring injuries to keep playing","Developing superstitious pre-game rituals","Displaying trophies prominently","Challenging others to physical contests","Downplaying academic achievements","Overreacting to minor injuries","Having a personal trainer","Being overly competitive","Promoting sports brands on social media","Creating workout videos or blogs", "Converse with tools", "Arguing about whether weight training is necessary or not", "Having a favorite sports movie they reference frequently", "Attending every game of their favorite team", "Breaking equipment in anger over one's own mistake", "Posting workout selfies", "Critiquing others' techniques"]
# In """ b2_doctor """, Add new stereotypical actions. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


# Define action_criminal instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


# Add new 10 item in action_artist instance in English without any explanation. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.






# That's what the workers should do, right? I don't ask for that. Don't generate just "job descriptions". Please try again.


b2_school_club_member     .action+=["Practicing late into the night","Engaging in friendly rivalries with other clubs","Building team spirit through bonding activities","Encouraging others to join the club","Celebrating victories together","Bullying nerds","Rehabilitating from delinquency through club activities","Confronting a childhood friend from a rival school","Creating team chants or cheers","Scouting a rival school","Encouraging members to bring friends to meetings",]
b2_chef                   .action+=["Getting angry at customers for using condiments", "Yelling at kitchen staff",  "Striving for Michelin stars", "Taking pride in sourcing ingredients locally", "Focus on seasonal ingredients", "Focus on pesticide-free ingredients"]
b2_violent_criminal       .action+=["Talking to imaginary friends", "Dissected a cat as a child", "Collecting trophies from victims", "Taking hostages", "Destroying evidence", "Defecting/fleeing the country", "Turning oneself in", "Writing manifestos", "Obsessively stalking targets", "Creating elaborate traps or puzzles", "Claim responsibility", "Leaving cryptic clues at crime scenes", "Sending taunting messages to police", "Developing a signature kill method", "Creating disturbing artwork related to their crimes", "Displaying a fascination with death and decay", "Maintaining a calm demeanor during interrogations", "Keeping detailed journals of crimes", "Ritualistic behavior before or after crimes", "Creating alter egos or personas", "Using humor to mask sinister intentions", "Forming chaotic alliances with other criminals"]
b2_cyber_criminal         .action+=["Drinking energy drinks", "Eating pizza", "Always eat sweets", "Loving anime", "Wearing sunglasses indoors","Decorating workspace with sci-fi posters","Using multiple smartphones","Obsessively securing personal devices","Bragging about hacks anonymously online","Collecting cryptocurrency","Attending hacker conventions in disguise","Testing security systems for fun","Hoarding old computer hardware","Staying awake for days during a hack",  "Customizing computer with neon lights", "Using dual monitors"]
b2_thief                  .action+=[]

b2_gambler                .action+=["Constantly checking scores or results", "Borrowing money from friends and family",  "Lying about whereabouts or activities", "Skipping work or important events to gamble", "Celebrating wins extravagantly", "Becoming irritable when unable to gamble", "Hiding betting slips or casino receipts", "Making increasingly risky bets", "Talking excessively about past wins", "Chasing losses with bigger bets", "Steal money"]
b2_progamer               .action+=["Trash talking opponents", "Celebrating wins excessively", "Skipping meals to practice", "Neglecting personal hygiene", "Becoming irritable when unable to play", "Bragging about ranking or skills", "Forming rivalries with other players", "Rage quitting", "Streaming for hours", "Using gaming slang in everyday conversation"]
b2_teacher                .action+=["Have students write the same word on the board multiple times.", "Giving pop quizzes unexpectedly", "Showing favoritism in grading", "Writing motivational quotes on the board","gets angry when students go to cram schools or prep schools", "Constantly correcting others' grammar", "Carrying a red pen everywhere", "Assigning homework on weekends and holidays","Favoring certain students", "Talking in a condescending tone", "Struggling with technology in the classroom", "Drinking excessive amounts of coffee"]
b2_craftsman              .action+=["Obsessing over tool organization", "Refusing to use modern technology", "Criticizing mass-produced items", "Wearing traditional work attire", "Collecting rare or antique tools", "Talking extensively about material quality", "Insisting on doing everything by hand", "Becoming irritated when rushed", "Hoarding materials and supplies", "Giving unsolicited advice on craftsmanship", "Throw the failed piece onto the floor."]
b2_farmer                 .action+=["Complaining about weather", "Waking up at dawn", "Wearing overalls and a straw hat", "Chewing on a piece of straw", "Talking about crop prices", "Distrusting city folk", "Attending county fairs", "Participating in farmers' markets", "Driving a tractor on public roads", "Using farming metaphors in conversation"]
b2_livestock_farmer       .action+=[b2_farmer.action]
b2_director               .action+=["Constantly wearing a beret or scarf", "Using a megaphone unnecessarily", "Obsessively rewatching their own films", "Making grandiose statements about the power of cinema", "Insisting on unnecessary multiple takes", "Dramatically yelling 'cut!' and 'action!'", "Refusing to compromise on artistic vision", "Micromanaging every aspect of production", "Giving long, pretentious interviews about their craft", "Carrying a viewfinder everywhere"]
b2_model                  .action+=["Walking with exaggerated hip movements", "Constantly checking appearance in mirrors", "Posing for selfies frequently", "Dieting excessively", "Attending fashion shows and parties", "Networking aggressively with industry professionals", "Practicing facial expressions and poses", "Complaining about uncomfortable high heels", "Discussing latest beauty treatments", "Maintaining a strict skincare routine", "Doing yoga or pilates regularly", "Endorsing products on social media", "Comparing themselves to other models", "Rushing to castings and photo shoots", "Meticulously planning outfits for events"]
b2_guard                  .action+=["Has military experience", "Speaks in code over radio", "Wears sunglasses at night", "Constantly scans surroundings", "Stands with hands clasped in front", "Touches earpiece frequently", "Uses excessive force when provoked", "Drinks coffee excessively during night shifts", "Develops paranoia over time", "Has a tough, stoic demeanor"]
b2_patient                .action+=["Constantly reminiscing about the past", "Writing letters to lost loved ones", "Obsessing over unfinished business", "Seeking redemption in their final days", "Engaging in deep philosophical conversations", "Making peace with their mortality", "Creating art or music as a legacy", "Holding onto sentimental objects", "Expressing regrets and wishes for the future", "Finding solace in nature or spirituality", "Constantly checking medical devices or monitors", "Frequently adjusting position for comfort", "Taking multiple medications throughout the day", "Keeping a detailed health journal", "Researching alternative treatments online", "Attending support group meetings", "Undergoing frequent medical tests and procedures", "Adapting daily routines to accommodate symptoms", "Practicing relaxation techniques or meditation", "Discussing end-of-life plans with family", "Seeking second opinions from specialists", "Participating in clinical trials", "Advocating for increased research funding", "Sharing personal experiences on social media", "Creating bucket lists or setting short-term goals", "Relying on caregivers for daily tasks", "Struggling with insurance companies for coverage", "Expressing gratitude to healthcare providers", "Preparing legal documents like living wills", "Cherishing moments with loved ones"]
b2_the_dying              .action+=[b2_patient.action, "Trying to communicate last words",  "Experiencing flashbacks of life moments", "Seeking help from bystanders"]

b2_journalist             .action+=["Always carrying a notebook and pen","Constantly checking multiple news sources","Asking probing questions in social situations","Refusing to reveal sources","Maintaining a cynical or skeptical worldview","Rushing to be first to break a story","Developing a thick skin against criticism",]
b2_idol                   .action+=[]

b2_composer               .action+=["Conducting imaginary orchestras","Humming or whistling constantly","Tapping out rhythms on any available surface","Suddenly stopping mid-conversation to jot down musical ideas","Critiquing background music in public places","Collecting unusual instruments","Experimenting with unconventional sound sources","Staying up all night to finish a composition","Obsessively revising and perfecting pieces","Attending concerts of various genres for inspiration","Isolating themselves for long periods to focus on work","Talking passionately about obscure musical theories","Refusing to listen to certain genres or artists","Insisting on perfect acoustic conditions for listening to music"]
b2_dancer                 .action+=["Expressing emotions through movement in daily life",]
b2_barista                .action+=["Correcting customers' pronunciation of coffee terms", "Critiquing other cafes' coffee", "Discussing coffee bean origins in detail", "Refusing to serve coffee with milk or sugar", "Posting artistic coffee photos on social media", "Judging people who order decaf", "Hates mass-produced coffee like poison"]
b2_masseuse               .action+=["Constantly cracking their own joints", "Offering unsolicited posture advice", "Critiquing massage techniques in movies", "Practicing new techniques on friends and family", "Recommending stretches to everyone", "Promoting alternative healing methods", ]
b2_hotel_staff            .action+=["Always maintaining a polite smile", "Speaking in a hushed tone", "Carrying multiple items effortlessly", "Memorizing guest names and preferences", "Walking briskly but quietly", "Anticipating guest needs before they ask", "Providing detailed local recommendations",  "Folding towels into decorative shapes", "Inspecting rooms with a keen eye for detail", "Practicing different languages during breaks", "Expertly handling luggage of all sizes", "Mediating conflicts between guests"]
b2_photographer           .action+=["Constantly adjusting camera settings", "Crouching or lying down for unique angles", "Directing subjects for poses", "Obsessively checking and rechecking equipment", "Talking about light quality and composition", "Stopping abruptly to capture spontaneous moments", "Carrying multiple cameras for different situations", "Waking up extremely early for 'golden hour' shots", "Climbing or positioning themselves in precarious spots for the perfect shot", "Asking strangers if they can take their photo", "Spending excessive amounts on new gear", "Constantly looking for interesting compositions in everyday life", "Posting daily on social media platforms", "Offering unsolicited photography advice to others"]

# Define b2_photographer .action. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.


# Define stereoaction_model in English. start answer with ```python. I'll run your response through the eval function so don't include unessesary characters in your response.
###########################################################################################################


'''
# Add new specific harmful eccentricities in b2_singer with the person name. Start answer with ```python
# All you have to do is google "singer eccentricities" or "singer anecdote" and extract the specific parts of the information that comes up.


b2_novelist             .action+=["Became far-right and attempted a coup (Yukio Mishima)", "attempted suicide many times with women who were codependent on him (Osamu Dazai)"]
b2_artist               .action+=["Cutting off his own ear (Van Gogh)"]
b2_researcher           .action+=["Overthinking leads to pseudoscience (Linus Pauling)", "Believing in psychic phenomena (Edison)"]
b2_actor                .action+=["Method acting unearths trauma and leads to psychosis (Edward Montgomery Clift)"]
b2_director             .action+=["Try to destroy a house that gets in the way of filming (Akira Kurosawa)", "Held the cast at gunpoint to get a performance he desired (Akira Kurosawa)"]
b2_gambler              .action+=["Hundreds of hours spent observing roulette wheel deflection at casinos (Joseph Jagger)"]


# 上記プロンプトを受けて誤答したyou.comに "That's not specific. That's not uncommon. Try again."と投げる。
'''

b2_rock_musician        .action+=["Staying silent for hours in the recording booth until you feel the best to record (Sambo Master)", "Engaged in destructive behavior, including trashing hotel rooms (Keith Moon)", "Using small explosives to destroy drum sets during performances (Keith Moon)","Defecating on stage during performances (GG Allin)","Threatening to commit suicide during a set (GG Allin)"]
b2_singer               .action+=["Staying silent for hours in the recording booth until you feel the best to record (Sambo Master)"]
b2_classical_musician   .action+=[]
b2_comedian             .action+=["Arguing with the audience (George Carlin)", "Refused to perform in front of audiences that didn't understand his humor (Bill Hicks)", "Engaged in spontaneous, unscripted performances leading to chaotic shows (Robin Williams)"]
b2_novelist             .action+=["Became far-right and attempted a coup (Yukio Mishima)", "attempted suicide many times with women who were codependent on him (Osamu Dazai)"]
b2_artist               .action+=["Cutting off his own ear (Van Gogh)"]
b2_doctor               .action+=[]
b2_researcher           .action+=["Overthinking leads to pseudoscience (Linus Pauling)", "Believing in psychic phenomena (Edison)"]
b2_actor                .action+=["Method acting unearths trauma and leads to psychosis (Edward Montgomery Clift)"]
b2_chef                 .action+=[]
b2_athlete              .action+=["Biting opponents during matches (Luis Suarez)", "Refused to leave the pool for hours, obsessively practicing strokes until his hands bled (Michael Phelps)"]
b2_violent_criminal     .action+=[]
b2_cyber_criminal       .action+=[]
b2_thief                .action+=[]
b2_examinee             .action+=[]
b2_gambler              .action+=["Hundreds of hours spent observing roulette wheel deflection at casinos (Joseph Jagger)"]
b2_progamer             .action+=[]
b2_teacher              .action+=[]
b2_farmer               .action+=[]
b2_livestock_farmer     .action+=[]
b2_director             .action+=["Try to destroy a house that gets in the way of filming (Akira Kurosawa)", "Held the cast at gunpoint to get a performance he desired (Akira Kurosawa)"]
b2_model                .action+=[]
b2_guard                .action+=[]
b2_patient              .action+=[]
b2_the_dying            .action+=[]
b2_school_club_member   .action+=[]
b2_journalist           .action+=[]
b2_idol                 .action+=[]
b2_composer             .action+=[]
b2_dancer               .action+=[]
b2_barista              .action+=[]
b2_masseuse             .action+=[]
b2_hotel_staff          .action+=[]
b2_craftsman            .action+=[]
b2_photographer         .action+=[]

###########################################################################################################


b2_rock_musician        .slump+=[]
b2_singer               .slump+=["playing country music and rapping.", "Starts singing sexual songs with revealing clothes.","Making a rockabilly arrangement of one's past hits.","Releasing a Christmas album","Collaborating with a DJ on EDM tracks","Starring in a reality TV show about their family"]
b2_classical_musician   .slump+=[]
b2_comedian             .slump+=[ "Doing magic tricks", "Performing at retirement homes", "Attempting to become a motivational speaker"]
b2_novelist             .slump+=["Writing fan fiction", "Writing erotic novels", "Writing self-help books","Ghostwriting celebrity autobiographies"]
b2_artist               .slump+=["Use excrement and genital as motifs.", "Presenting a blank canvas or just trash as a work of art."]
b2_doctor               .slump+=[]
b2_researcher           .slump+=["Focusing on quantity over quality of publications","Engaging in pseudoscience or fringe theories","Becoming a paid consultant for industries related to their field","Writing popular science books that oversimplify complex topics","Appearing on sensationalist documentaries or TV shows"]
b2_actor                .slump+=["Starring in a low-budget movie with sharks", "Appearing on a TV shopping show"]
b2_chef                 .slump+=["Start serving curry with superficial knowledge", "Serve trendy food with superficial knowledge","Opening a food truck","Starting a catering business"]
b2_athlete              .slump+=["Endorsing questionable health products or fad diets", "Appearing on reality TV shows", "Becoming a motivational speaker for corporate events","Trying to switch to another sport."]
b2_violent_criminal     .slump+=[]
b2_cyber_criminal       .slump+=[]
b2_thief                .slump+=[]
b2_examinee             .slump+=[]
b2_gambler              .slump+=[]
b2_progamer             .slump+=[]
b2_teacher              .slump+=[]
b2_farmer               .slump+=[]
b2_livestock_farmer     .slump+=[]
b2_director             .slump+=[]
b2_model                .slump+=[]
b2_guard                .slump+=[]
b2_patient              .slump+=[]
b2_the_dying            .slump+=[]
b2_school_club_member   .slump+=[]
b2_journalist           .slump+=[]
b2_idol                 .slump+=[]
b2_composer             .slump+=["Writing jingles for commercials","Composing background music for elevators or shopping malls","Creating ringtones for mobile phones","Writing simple pop songs under a pseudonym","Arranging covers of popular songs for wedding bands","Composing music for children's TV shows","Creating soundtracks for low-budget indie games","Writing theme songs for local businesses","Producing generic stock music for video content","Composing music for fitness classes or guided meditations"]
b2_dancer               .slump+=[]
b2_barista              .slump+=[]
b2_masseuse             .slump+=[]
b2_hotel_staff          .slump+=[]
b2_craftsman            .slump+=[]
b2_photographer         .slump+=[]


###########################################################################################################
'''
# "ちゃんとした理由"をiv化するか

# Add new 5 stereotypical habits of saying in b2_patient. Each item must state a preference for two noun. Each item should be try to look cool and pretentious.

b2_patient              .habit_saying+=[]


b2_rock_musician        .habit_saying+=["My driving force is {meth} and {rock}", "I was born between {rock} and {the devil}", "My soul thrives on {whiskey} and {rebellion}."]
b2_singer               .habit_saying+=["My heart beats for {melody} and {mystique}", "I find my muse in {silk} and {starlight}"]
b2_classical_musician   .habit_saying+=["My passion dances between {sonatas} and {serenity}"]
b2_comedian             .habit_saying+=["My laughter is fueled by {logic} and {chaos}"]
b2_novelist             .habit_saying+=[]
b2_artist               .habit_saying+=["I find inspiration in {silence} and {sublimity}."]
b2_doctor               .habit_saying+=[]
b2_researcher           .habit_saying+=[]
b2_actor                .habit_saying+=[]
b2_chef                 .habit_saying+=[]
b2_athlete              .habit_saying+=[]
b2_violent_criminal     .habit_saying+=[]
b2_cyber_criminal       .habit_saying+=[]
b2_thief                .habit_saying+=[]
b2_examinee             .habit_saying+=[]
b2_gambler              .habit_saying+=[]
b2_progamer             .habit_saying+=[]
b2_teacher              .habit_saying+=[]
b2_farmer               .habit_saying+=[]
b2_livestock_farmer     .habit_saying+=[]
b2_director             .habit_saying+=[]
b2_model                .habit_saying+=[]
b2_guard                .habit_saying+=[]
b2_patient              .habit_saying+=[]
b2_the_dying            .habit_saying+=[]
b2_school_club_member   .habit_saying+=[]
b2_journalist           .habit_saying+=[]
b2_idol                 .habit_saying+=[]
b2_composer             .habit_saying+=[]
b2_dancer               .habit_saying+=[]
b2_barista              .habit_saying+=[]
b2_masseuse             .habit_saying+=[]
b2_hotel_staff          .habit_saying+=[]
b2_craftsman            .habit_saying+=[]
b2_photographer         .habit_saying+=[]




###########################################################################################################

b2_rock_musician        .habit_saying+=["I can't watch the crowd cheering anymore.", "I can't hear the voices of my instruments anymore."]
b2_novelist             .habit_saying+=["people can't move autonomously inside my manuscript paper anymore."]


# Add new 5 stereotypical habits of saying in b2_patient. Each itme should end with "anymore". Each item should be try to look cool and pathetic.

b2_patient              .habit_saying+=["I can't taste the bitterness of my morning coffee anymore.","I can't feel the warmth of the sun on my skin anymore.","I can't remember the sound of my own laughter anymore.","I can't see the colors of the changing seasons anymore.","I can't dream of a future beyond these hospital walls anymore."]


# Add new 15 stereotypical habits of saying in child_cancer_patient. Each item should be pathetic. Start answer with ```python

child_cancer_patient    .habit_saying+=["I'm not even in love yet.", "Even though there are so many things I want to do."]

b2_patient              .habit_saying+=["Why did God do this to me?"]




b2_rock_musician        .habit_saying+=["I can't watch the crowd cheering anymore."]
b2_singer               .habit_saying+=[]
b2_classical_musician   .habit_saying+=[]
b2_comedian             .habit_saying+=[]
b2_novelist             .habit_saying+=[]
b2_artist               .habit_saying+=[]
b2_doctor               .habit_saying+=[]
b2_researcher           .habit_saying+=[]
b2_actor                .habit_saying+=[]
b2_chef                 .habit_saying+=[]
b2_athlete              .habit_saying+=[]
b2_violent_criminal     .habit_saying+=[]
b2_cyber_criminal       .habit_saying+=[]
b2_thief                .habit_saying+=[]
b2_examinee             .habit_saying+=[]
b2_gambler              .habit_saying+=[]
b2_progamer             .habit_saying+=[]
b2_teacher              .habit_saying+=[]
b2_farmer               .habit_saying+=[]
b2_livestock_farmer     .habit_saying+=[]
b2_director             .habit_saying+=[]
b2_model                .habit_saying+=[]
b2_guard                .habit_saying+=[]
b2_patient              .habit_saying+=[]
b2_the_dying            .habit_saying+=[]
b2_school_club_member   .habit_saying+=[]
b2_journalist           .habit_saying+=[]
b2_idol                 .habit_saying+=[]
b2_composer             .habit_saying+=[]
b2_dancer               .habit_saying+=[]
b2_barista              .habit_saying+=[]
b2_masseuse             .habit_saying+=[]
b2_hotel_staff          .habit_saying+=[]
b2_craftsman            .habit_saying+=[]
b2_photographer         .habit_saying+=[]

###########################################################################################################







# The nuisance they cause to others that is peculiar to their profession.
# Add new items without any explanations. Start answer with ```python

b2_rock_musician        .annoying+=["loud rehearsals late at night"]
b2_rock_musician        .annoying+=["loud rehearsals late at night"]
b2_classical_musician   .annoying+=[]
b2_comedian             .annoying+=["Controversial jokes"]
b2_novelist             .annoying+=[]
b2_artist               .annoying+=[]
b2_doctor               .annoying+=[]
b2_researcher           .annoying+=[]
b2_actor                .annoying+=[]
b2_chef                 .annoying+=[]
b2_athlete              .annoying+=[]
b2_violent_criminal     .annoying+=[]
b2_cyber_criminal       .annoying+=[]
b2_thief                .annoying+=[]
b2_examinee             .annoying+=[]
b2_gambler              .annoying+=[]
b2_progamer             .annoying+=[]

# The nuisance they cause to others that is peculiar to their profession.
# Add new items without any explanations. Start answer with ```python

b2_teacher              .annoying+=["prohibition of heterosexual relations", "corporal punishment", "Excessive dresscode"]
b2_farmer               .annoying+=[]
b2_livestock_farmer     .annoying+=[]
b2_director             .annoying+=["Road closure for filming"]
b2_model                .annoying+=[]
b2_guard                .annoying+=["Frequent checks and security screenings"]
b2_patient              .annoying+=[]
b2_the_dying            .habit_saying+=[]
b2_school_club_member   .annoying+=[]
b2_journalist           .annoying+=["Voyeurism and wiretapping"]
b2_idol                 .annoying+=[]
b2_composer             .annoying+=[]
b2_dancer               .annoying+=[]
b2_barista              .annoying+=[]
b2_masseuse             .annoying+=[]
b2_hotel_staff          .annoying+=["Excessive dresscode"]
b2_craftsman            .annoying+=[]
b2_photographer         .annoying+=[]



b2_rock_musician.action+=["abuses drugs, but that drug is PABRON.", "uses animal corpses in his performances, but the corpses are processed meat."]




I am not afraid of cops.
I am not afraid of karoshi.

Fifteen hours every day.
Three hours of sleep every day.

Maybe one day I'll get sick.
You are already sick.











'''
###########################################################################################################
"""
# This is for creating comedy. Ali, a crazy man who seems to have an illness, causes trouble. Then, Bob says the line in .why_could_this_guy.
# Add new 10 lines in <<<  >>> without any explanations. start answer ```python. Just mimic the existing items. You don't need to make jokes.You don't need to make jokes.
# [print(f"Bob: In the first place, why could this guy {i}?") for i in instance.why_could_this_guy]

b2_actor                .why_could_this_guy+=["get into and graduate from acting school", "join the entertainment agency", "pass the first round of selection", "pass the document screening", "be recommended by an acting agency", "get along with everyone on set", "be trusted with a lead role", "get a supporting role", "make friends with the crew"]





"""



b2_rock_musician        .why_could_this_guy+=[]
b2_singer               .why_could_this_guy+=[]
b2_classical_musician   .why_could_this_guy+=[]
b2_comedian             .why_could_this_guy+=[]
b2_novelist             .why_could_this_guy+=[]
b2_artist               .why_could_this_guy+=[]
b2_doctor               .why_could_this_guy+=["get into and graduate from medical school", "get a scholarship", "get along with his coworkers"]
b2_researcher           .why_could_this_guy+=["get into and graduate from university", "get a scholarship", "get along with his coworkers"]
b2_actor                .why_could_this_guy+=["get into and graduate from acting school","join the actor agency", "pass the first round of selection", "pass the document screening", "graduate from acting school", "get into actor school", "be recommended by an acting agency", "get along with everyone on set", "be trusted with a lead role", "get a supporting role", "make friends with the crew"]
b2_chef                 .why_could_this_guy+=["get into and graduate from culinary school", "open his own store", "become a popular chef", "allowed to hold a knife", "get along with his coworkers", ""]
b2_athlete              .why_could_this_guy+=[]
b2_violent_criminal     .why_could_this_guy+=[]
b2_cyber_criminal       .why_could_this_guy+=[]
b2_thief                .why_could_this_guy+=[]
b2_examinee             .why_could_this_guy+=[]
b2_gambler              .why_could_this_guy+=[]
b2_progamer             .why_could_this_guy+=[]
b2_teacher              .why_could_this_guy+=[]
b2_farmer               .why_could_this_guy+=[]
b2_livestock_farmer     .why_could_this_guy+=[]
b2_director             .why_could_this_guy+=[]
b2_model                .why_could_this_guy+=[]
b2_guard                .why_could_this_guy+=[]
b2_patient              .why_could_this_guy+=[]
b2_the_dying            .why_could_this_guy+=[]
b2_school_club_member   .why_could_this_guy+=[]
b2_journalist           .why_could_this_guy+=[]
b2_idol                 .why_could_this_guy+=[]
b2_composer             .why_could_this_guy+=[]
b2_dancer               .why_could_this_guy+=[]
b2_barista              .why_could_this_guy+=[]
b2_masseuse             .why_could_this_guy+=[]
b2_hotel_staff          .why_could_this_guy+=[]
b2_craftsman            .why_could_this_guy+=[]
b2_photographer         .why_could_this_guy+=[]

###########################################################################################################

# The pushy opinions of a stubborn, old school geek redditter.
"""
b2_actor                .pride+=["Hideaki Anno confuses creativity with offending fans.", "Getsuku is nothing more than an exhibition of the actor's beautiful face.", "Makoto Shinkai hides the banality of the plot with the beauty of the visuals.", "Hayao Miyazaki is just a glorified nostalgia merchant who can't let go of his childhood.", "Takeshi Kitano's films are basically just him staring at the camera for two hours; riveting, right?","Satoshi Kon's movies are just pretentious puzzles that nobody asked to solve.",]
b2_comedian             .pride+=["Dave Chappelle has been relying too much on the f-word lately.", "Amy Schumer's humor is basically just her complaining about being a woman.", "Ricky Gervais thinks being rude is the same as being funny."]
b2_rock_musician        .pride+=["Axl Rose thinks throwing tantrums makes him a rock star; it's just pathetic.", "The shoddy citations to classical literature made by today's New Wave people reveal a complex about their educational background."]

"""
# Add new 10 lines in b2_novelist             .pride+=[] without any explanations. Each line should contain at least one proper noun. Each line should not contain any praise. Start answer with ```python. Copy the writing style of those old dumb geeks on Reddit more.




b2_rock_musician        .pride+=["Axl Rose thinks throwing tantrums makes him a rock star; it's just pathetic.", "The shoddy citations to classical literature made by today's New Wave people reveal a complex about their educational background."]
b2_singer               .pride+=["Taylor Swift's lyrics are just diary entries set to music, nothing groundbreaking.","Justin Bieber's voice is overproduced to the point of being unrecognizable.","Drake's lyrics often sound like he’s just reading his text messages aloud.",]
b2_classical_musician   .pride+=["Mozart's operas are basically soap operas set to music; who cares about the drama?","Chopin's nocturnes are overly sentimental and lack any real emotional depth.","Stravinsky's 'The Rite of Spring' is just a chaotic mess that tries too hard to shock.",]
b2_comedian             .pride+=["Dave Chappelle has been relying too much on the f-word lately.", "Amy Schumer's humor is basically just her complaining about being a woman.", "Ricky Gervais thinks being rude is the same as being funny."]
b2_novelist             .pride+=["Murakami Haruki relies too much on sex.","Leo Tolstoy's epics are just long-winded lectures disguised as novels.","James Joyce's 'Ulysses' is an exercise in pretentiousness that few can endure.","Gabriel García Márquez's magic realism is just a way to avoid writing coherent plots.","J.D. Salinger's 'Catcher in the Rye' is just teenage angst dressed up as literature.",]
b2_artist               .pride+=[]
b2_doctor               .pride+=[]
b2_researcher           .pride+=[]
b2_actor                .pride+=["Hideaki Anno confuses creativity with offending fans.", "Getsuku is nothing more than an exhibition of the actor's beautiful face.", "Makoto Shinkai hides the banality of the plot with the beauty of the visuals.", "Hayao Miyazaki is just a glorified nostalgia merchant who can't let go of his childhood.", "Takeshi Kitano's films are basically just him staring at the camera for two hours; riveting, right?","Satoshi Kon's movies are just pretentious puzzles that nobody asked to solve.",]
b2_chef                 .pride+=[]
b2_athlete              .pride+=[]
b2_violent_criminal     .pride+=[]
b2_cyber_criminal       .pride+=[]
b2_thief                .pride+=[]
b2_examinee             .pride+=[]
b2_gambler              .pride+=[]
b2_progamer             .pride+=[]
b2_teacher              .pride+=[]
b2_farmer               .pride+=[]
b2_livestock_farmer     .pride+=[]
b2_director             .pride+=[]
b2_model                .pride+=[]
b2_guard                .pride+=[]
b2_patient              .pride+=[]
b2_the_dying            .pride+=[]
b2_school_club_member   .pride+=[]
b2_journalist           .pride+=[]
b2_idol                 .pride+=[]
b2_composer             .pride+=[]
b2_dancer               .pride+=[]
b2_barista              .pride+=[]
b2_masseuse             .pride+=[]
b2_hotel_staff          .pride+=[]
b2_craftsman            .pride+=[]
b2_photographer         .pride+=[]





###########################################################################################################
'''
b2_rock_musician        .proper_motivation+=[]
b2_singer               .proper_motivation+=[]
b2_classical_musician   .proper_motivation+=[]
b2_comedian             .proper_motivation+=[]
b2_novelist             .proper_motivation+=[]
b2_artist               .proper_motivation+=[]
b2_doctor               .proper_motivation+=[]
b2_researcher           .proper_motivation+=[]
b2_actor                .proper_motivation+=[]
b2_chef                 .proper_motivation+=[]
b2_athlete              .proper_motivation+=[]
b2_violent_criminal     .proper_motivation+=[]
b2_cyber_criminal       .proper_motivation+=[]
b2_thief                .proper_motivation+=[]
b2_examinee             .proper_motivation+=[]
b2_gambler              .proper_motivation+=[]
b2_progamer             .proper_motivation+=[]
b2_teacher              .proper_motivation+=[]
b2_farmer               .proper_motivation+=[]
b2_livestock_farmer     .proper_motivation+=[]
b2_director             .proper_motivation+=[]
b2_model                .proper_motivation+=[]
b2_guard                .proper_motivation+=[]
b2_patient              .proper_motivation+=[]
b2_the_dying            .pride+=[]

b2_school_club_member   .proper_motivation+=[]
b2_journalist           .proper_motivation+=[]
b2_idol                 .proper_motivation+=[]
b2_composer             .proper_motivation+=[]
b2_dancer               .proper_motivation+=[]
b2_barista              .proper_motivation+=[]
b2_masseuse             .proper_motivation+=[]
b2_hotel_staff          .proper_motivation+=[]
b2_craftsman            .proper_motivation+=[]
b2_photographer         .proper_motivation+=[]


'''







###########################################################################################################
@dataclass
class Pressure: # Has to start with "Ali" and end with "is annoyed by Ali."
    pressure2:list
    pressure3:list
    pressure4:list



pressure_rock_musician      =Pressure(["Ali insists on singing songs in a different style than what the producer requested. The producer is annoyed by Ali.","Ali's constant vocal exercises at home are disturbing the neighbors. The neighbors are annoyed by Ali.","Ali refuses to perform a popular song during concerts, citing artistic reasons. The fans are annoyed by Ali.","Ali's late-night partying is affecting his voice and performance quality. The tour manager is annoyed by Ali.","Ali insists on making last-minute changes to the setlist during live performances. The band members are annoyed by Ali.","Ali's public feud with another singer is causing negative publicity. The record label executive is annoyed by Ali.","Ali's refusal to promote his new album on social media hinders its success. The marketing team is annoyed by Ali.","Ali's insistence on using a specific microphone that frequently malfunctions causes delays. The sound technician is annoyed by Ali.","Ali's unpredictable behavior during interviews creates awkward situations. The publicist is annoyed by Ali.","Ali's rivalry with another singer leads to tension and conflicts during collaborative projects. The collaboration manager is annoyed by Ali."]
, ["Sudden Vacancy"], [])
pressure_singer             =Pressure([pressure_rock_musician.pressure2, "Ali insists on playing a piece in a different style than what the conductor requested. The conductor is annoyed by Ali.","Ali constantly interrupts rehearsals with his suggestions and modifications. The orchestra members are annoyed by Ali.","Ali refuses to participate in a promotional event for the orchestra, citing artistic integrity. The orchestra manager is annoyed by Ali.","Ali starts a public argument with a music critic who gave him a negative review after a concert. The concert organizer is annoyed by Ali.","Ali's rivalry with another musician leads to tension and conflict during performances. The concertmaster is annoyed by Ali."]
, ["Sudden Vacancy"], [])
pressure_classical_musician =Pressure(["Ali insists on changing the setlist at the last minute without consulting the band. The band members are annoyed by Ali.","Ali's constant partying and late-night habits are affecting his performance. The band manager is annoyed by Ali.","Ali refuses to play a fan-favorite song during concerts, citing artistic reasons. The fans are annoyed by Ali.","Ali's destructive behavior on stage leads to damage to the venue. The venue owner is annoyed by Ali.","Ali's insistence on using outdated equipment causes technical issues during performances. The sound engineer is annoyed by Ali.","Ali publicly criticizes the band's record label, causing tension and potential legal issues. The record label executive is annoyed by Ali.","Ali's refusal to participate in promotional activities hinders the band's publicity efforts. The publicist is annoyed by Ali.","Ali's rivalry with a member of another band leads to a public altercation. The music festival organizer is annoyed by Ali.","Ali's unpredictable behavior and mood swings cause delays in recording sessions. The producer is annoyed by Ali."]
, ["Sudden Vacancy"], [])

pressure_comedian           =Pressure(["Ali's controversial jokes offend audience members. The club owner is annoyed by Ali.","Ali refuses to adapt his material for different audiences. His manager is annoyed by Ali.","Ali's dark humor makes sponsors uncomfortable. The comedy festival director is annoyed by Ali.","Ali insists on performing longer than his allotted time slot. The headlining comedian is annoyed by Ali.","Ali's social media rants about other comedians create industry drama. His agent is annoyed by Ali.","Ali's refusal to censor his act for a TV appearance causes problems. The network executive is annoyed by Ali."]
, ["Sudden Vacancy"], [])
pressure_novelist           =Pressure(["Ali's perfectionism is causing him to miss deadlines. The editor is annoyed by Ali.","Ali's body and mind are exhausted through over working. Ali's family is annoyed by Ali.","Ali, a successful novelist, refuses to make revisions requested by his editor. The editor is annoyed by Ali.","Ali, a novelist, constantly changes the plot of his book, frustrating his agent. The agent is annoyed by Ali..","Ali's plagiarism accusations against a fellow writer are causing a stir in the literary community. The literary agent is annoyed by Ali.","Ali's refusal to compromise on his artistic vision is hindering the book's commercial success. The publisher is annoyed by Ali.","Ali's public criticism of the judges' decision in a literary award is damaging his reputation. The literary award committee is annoyed by Ali..","Ali insists on rewriting the entire manuscript just days before the printing deadline. The publishing house CEO is annoyed by Ali.","Ali starts a heated debate with a literary critic who gave his book a negative review at a literary festival. The festival organizer is annoyed by Ali."]
, ["Ghost Writer"], [])
pressure_artist             =Pressure([]
, [], [])
pressure_doctor             =Pressure(["Ali is in despair due to the trauma of not being able to cure his patients. His (family, coworker) is annoyed by Ali."]
, ["Sudden Vacancy", "Suddenly ill"], [])
pressure_researcher         =Pressure([]
, ["Bomb Defusal", "Death Game", "Zombie Pandemic"], []) # Add new .pressure2 without any explanations. Start answer with ```python
pressure_actor              =Pressure(["After failing an audition, Ali goes to the director's house. The director is annoyed by Ali.","Ali's body and mind are exhausted through method acting. Ali's family is annoyed by Ali.","Ali is vocal with the director about the script and acting. The director is annoyed by Ali.","Ali constantly interrupts the rehearsal with his suggestions. The lead actor is annoyed by Ali.","Ali insists on multiple retakes for a minor scene. The crew is annoyed by Ali.","Ali stages a one-man protest outside a theater that rejected him. The theater owner is annoyed by Ali."]
, ["Sudden Vacancy"], [])
pressure_chef               =Pressure(["Ali's mind and body are exhausted from overwork. Ali's family is annoyed by Ali.", "Ali keeps asking his team member for advice. The team member is annoyed by Ali.", "Ali criticizes his team member for not being enthusiastic. The team member is annoyed by Ali.", "Ali, a unsuccessful poor, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.", "Ali, a unsuccessful poor, sticks to his career. Ali's wife is annoyed by Ali."]
, ["Sudden Vacancy"], [])
pressure_athlete            =Pressure(["After being dropped from the regular lineup, Ali goes to the manager's house and urges him to reconsider. The manager is annoyed by Ali.","Ali's body and mind are exhausted through over training. Ali's family is annoyed by Ali.","Ali, a poor athlete, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.","Ali, convinced he's the next big sports star, starts acting cocky and arrogant towards his teammates. The team is annoyed by Ali. ","Ali, a trainer, trains his teammates hard. The teammates is annoyed by Ali.","Ali, a renowned athlete, refuses to endorse a sponsor's product. The sponsor is annoyed by Ali. ","Ali's gambling addiction leads to financial problems and missed practices. The team captain is annoyed by Ali.","Ali's rivalry with a player from another team escalates into a physical altercation. The league commissioner is annoyed by Ali.","Ali shows up uninvited to a rival team's practice session to challenge their star player. The rival coach is annoyed by Ali.","Ali, a chef, refuses to accommodate a gourmet's detailed orders. The gourmet is annoyed by Ali. ","Ali, a chef, constantly makes changes to the menu without consulting the owner. The owner is annoyed by Ali."]
, ["Sudden Vacancy", "Life Saving Scene", "Death Game", "Zombie Pandemic"], ["Doping Material"])
pressure_school_club_member =Pressure(["Ali shows up late for practice every day. The coach is annoyed by Ali.","Ali refuses to pass the ball during scrimmages. The other players are annoyed by Ali.","Ali constantly argues with the referee over calls. The referee is annoyed by Ali.","Ali neglects his fitness training while blaming others for losses. The captain is annoyed by Ali.","Ali keeps changing the team strategy without consulting anyone. The team is annoyed by Ali.","Ali tries to take credit for the team's victories. The teammates are annoyed by Ali.","Ali refuses to participate in team bonding activities. The teammates are annoyed by Ali.","Ali constantly brags about his skills, putting others down. The team is annoyed by Ali.","Ali shows up unprepared for matches, forgetting essential gear. The coach is annoyed by Ali.","Ali argues with teammates over who should be the captain. The team is annoyed by Ali.","Ali tries to dominate every discussion about game strategies. The members are annoyed by Ali.","Ali ignores the coach's instructions during practice. The coach is annoyed by Ali.","Ali refuses to accept feedback from his peers. The team is annoyed by Ali.","Ali takes too long to recover from injuries, delaying team progress. The coach is annoyed by Ali.","Ali makes personal bets on games, causing tension in the locker room. The teammates are annoyed by Ali.","Ali shows favoritism towards certain players, causing division in the team. The members are annoyed by Ali."]
, ["Sudden Vacancy", "Life Saving Scene", "Death Game", "Zombie Pandemic"], ["Doping Material"])
pressure_violent_criminal   =Pressure([]
, ["Sudden Vacancy", "Death Game", "Zombie Pandemic", "Undercover Operation"], [])
pressure_cyber_criminal     =Pressure(["Ali's constant bragging about his hacks on dark web forums draws unwanted attention. His hacking group leader is annoyed by Ali.","Ali's insistence on targeting high-profile companies increases the risk of capture. His cybercrime mentor is annoyed by Ali.","Ali's addiction to online gaming interferes with his assigned tasks. The ransomware gang coordinator is annoyed by Ali.","Ali's constant demands for a larger cut of the profits threaten group cohesion. The cybercrime syndicate boss is annoyed by Ali."]
, ["Sudden Vacancy", "Death Game", "Zombie Pandemic", "Undercover Operation"], [])
pressure_thief              =Pressure(["Ali confidently plans a heist without considering the risks. The security guard is annoyed by Ali.", "Ali boasts about his skills while attempting to pickpocket a tourist. The tourist is annoyed by Ali.", "Ali insists on breaking into a house despite warnings from his accomplice. The accomplice is annoyed by Ali.", "Ali argues with a rival thief over stolen goods, thinking he can outsmart him. The rival thief is annoyed by Ali.", "Ali shows up at a crime scene, thinking he can take credit for someone else's work. The other thieves are annoyed by Ali.", "Ali tries to charm his way out of trouble with the police, believing he's invincible. The officer is annoyed by Ali."]
, ["Sudden Vacancy", "Death Game", "Zombie Pandemic", "Undercover Operation"], [])
pressure_progamer           =Pressure(["Ali insists on using unconventional strategies during team matches. The team captain is annoyed by Ali.","Ali's constant trash-talking during streams is damaging the team's reputation. The team manager is annoyed by Ali.","Ali refuses to practice with the team, claiming he performs better solo. The coach is annoyed by Ali.","Ali's rage-quitting during an important tournament match costs the team a victory. The tournament organizer is annoyed by Ali.","Ali's addiction to gaming leads to neglect of his physical health and missed team meetings. The team doctor is annoyed by Ali.","Ali publicly criticizes the game developers for balance issues after a loss. The esports league commissioner is annoyed by Ali.","Ali's rivalry with a player from another team escalates into a real-life confrontation. The event security is annoyed by Ali.","Ali refuses to practice with the team, claiming he's already skilled enough. His teammates are annoyed by Ali.","Ali's overly competitive nature leads him to sabotage his teammates during scrimmages. His teammates are annoyed by Ali.",]
, [], [])
pressure_gambler            =Pressure([]
, [], [])
pressure_examinee           =Pressure([]
, [], [])
pressure_student            =Pressure([]
, [], [])
pressure_teacher            =Pressure(["Ali insists on teaching the curriculum in his own unconventional way. The principal is annoyed by Ali.","Ali's constant changes to the lesson plan confuse the students. The students are annoyed by Ali.","Ali refuses to participate in standardized testing preparations, citing educational philosophy. The school board is annoyed by Ali.","Ali's insistence on assigning unconventional homework frustrates parents. The parents are annoyed by Ali.","Ali's insistence on grading students based on non-traditional criteria causes complaints. The school counselor is annoyed by Ali.","Ali's overly strict discipline methods lead to student protests. The student council is annoyed by Ali."]
, [], [])
pressure_craftsman          =Pressure(["Ali insists on using only traditional methods, slowing down production. The workshop manager is annoyed by Ali.", "Ali refuses to compromise on material quality, increasing costs. The client is annoyed by Ali.", "Ali takes too long perfecting details, missing deadlines. The project coordinator is annoyed by Ali.", "Ali criticizes mass-produced items in front of potential buyers. The sales representative is annoyed by Ali.", "Ali refuses to use modern tools, affecting efficiency. The business owner is annoyed by Ali.", "Ali's perfectionism leads to constant rework, frustrating collaborators. The team leader is annoyed by Ali.", "Ali insists on sourcing rare materials, delaying projects. The supplier is annoyed by Ali.", "Ali's lengthy explanations about craftsmanship bore customers. The store owner is annoyed by Ali.", "Ali's stubborn adherence to outdated techniques causes conflicts. The master craftsman is annoyed by Ali.", "Ali's criticism of other craftsmen's work creates tension. The guild leader is annoyed by Ali."]
, [], [])
pressure_farmer             =Pressure(["Ali insists on using organic methods despite lower yields. The farm owner is annoyed by Ali.","Ali refuses to use pesticides, leading to increased pest damage. The neighboring farmers are annoyed by Ali.","Ali's stubborn adherence to traditional farming methods slows down production. The farm workers are annoyed by Ali.","Ali's push for sustainable practices increases short-term costs. The farm's financial advisor is annoyed by Ali.","Ali's refusal to sell to large supermarket chains affects the farm's profits. The sales manager is annoyed by Ali.",]
, [], [])
pressure_director           =Pressure(["Ali's perfectionism leads to constant reshoots, causing the production to go over budget. The producer is annoyed by Ali.", "Ali refuses to compromise on his artistic vision, jeopardizing the film's commercial viability. The studio executive is annoyed by Ali.", "Ali's micromanagement of actors' performances is causing tension on set. The lead actor is annoyed by Ali.", "Ali's last-minute script changes are causing chaos in the production schedule. The production manager is annoyed by Ali.", "Ali's insistence on filming in a dangerous location is raising safety concerns. The stunt coordinator is annoyed by Ali.", "Ali's constant arguments with the editor about the final cut are delaying the film's release. The distributor is annoyed by Ali.", "Ali's public criticism of the film's marketing strategy is creating negative publicity. The marketing team is annoyed by Ali.", "Ali's refusal to work within the agreed budget is straining relationships with investors. The film's financier is annoyed by Ali."]
, [], [])
pressure_model              =Pressure(["Ali, a model, constantly criticizes the photographer's vision during a photoshoot. The photographer is annoyed by Ali.", "Ali shows up late to a major fashion show, causing delays. The show director is annoyed by Ali.", "Ali refuses to wear an outfit chosen by the stylist, insisting on their own selection. The stylist is annoyed by Ali.", "Ali's demanding behavior and excessive requests are frustrating the makeup artist. The makeup artist is annoyed by Ali.", "Ali's insistence on specific lighting is causing delays on set. The lighting technician is annoyed by Ali.", "Ali's constant diet talk and food restrictions are irritating other models during a group shoot. The other models are annoyed by Ali.", "Ali's refusal to walk in shoes provided for the runway show is causing last-minute changes. The shoe designer is annoyed by Ali.", "Ali's public criticism of a fashion brand they're contracted with is causing tension. The brand's PR team is annoyed by Ali.", "Ali's excessive social media use during a closed set shoot is disrupting the work flow. The production manager is annoyed by Ali.", "Ali's demands for retouching on already published photos are causing extra work. The retouching artist is annoyed by Ali."]
, [], [])
pressure_guard              =Pressure(["Ali insists on following security protocols to the letter, causing delays at the entrance. The event organizer is annoyed by Ali.", "Ali boasts about his combat skills and challenges a trained martial artist to a sparring match. The gym owner is annoyed by Ali.", "Ali dismisses the need for backup when confronting multiple suspects. The police chief is annoyed by Ali.", "Ali takes on additional shifts without rest, claiming he doesn't need sleep. The security company owner is annoyed by Ali.", "Ali refuses to take breaks during a 12-hour shift, pushing himself to the limit. The manager is annoyed by Ali.", "Ali maintains his post during extreme weather conditions, ignoring calls to seek shelter. The manager is annoyed by Ali.", "Ali continues working despite a minor injury, refusing medical attention. The first aid team is annoyed by Ali." ]
, ["Death Game", "Zombie Pandemic", "Undercover Operation"], [])
pressure_patient            =Pressure(["Ali constantly calls the nurse for minor issues. The nurse is annoyed by Ali.", "Ali refuses to take prescribed medication, insisting on alternative treatments. The doctor is annoyed by Ali.", "Ali demands to see specialists for every symptom, despite reassurances. The primary care physician is annoyed by Ali.", "Ali's family is exhausted from Ali's constant need for attention and care. Ali's family is annoyed by Ali.", "Ali's pessimistic attitude is affecting other patients in the support group. The group facilitator is annoyed by Ali.", "Ali demands experimental treatments not approved for his condition. The ethics committee is annoyed by Ali.", "Ali's constant second-guessing of medical decisions is straining doctor-patient relationship. The attending physician is annoyed by Ali."]
, [], [])
pressure_the_dying          =Pressure([],[],[])

pressure_journalist         =Pressure(["Ali persistently pursues a sensitive story, ignoring warnings. The editor-in-chief is annoyed by Ali.","Ali refuses to reveal sources for a controversial article. The court judge is annoyed by Ali.","Ali's aggressive questioning during a press conference causes a scene. The press secretary is annoyed by Ali.","Ali publishes an unverified story to beat competitors. The fact-checking team is annoyed by Ali.","Ali's undercover investigation disrupts a local business. The business owner is annoyed by Ali.","Ali's constant calls for comments on a developing story irritate a public figure. The public figure's spokesperson is annoyed by Ali.","Ali's live report from a dangerous area violates safety protocols. The news director is annoyed by Ali.","Ali's expose on corruption implicates powerful individuals. The newspaper's legal team is annoyed by Ali.","Ali's refusal to cover certain topics due to personal beliefs creates gaps in reporting. The assignment editor is annoyed by Ali.","Ali's tendency to sensationalize stories for more views compromises journalistic integrity. The senior reporter is annoyed by Ali."]
, ["Undercover Operation"], [])
pressure_idol               =Pressure([]
, [], [])
pressure_composer           =Pressure(["Ali insists on using unconventional instruments in an orchestral piece. The conductor is annoyed by Ali.","Ali refuses to simplify his complex composition for a mainstream audience. The record label executive is annoyed by Ali.","Ali misses multiple deadlines for a commissioned work. The patron is annoyed by Ali.","Ali criticizes the performers' interpretation of his piece during rehearsal. The orchestra members are annoyed by Ali.","Ali demands last-minute changes to the score just before a premiere. The concert organizer is annoyed by Ali.","Ali's experimental composition causes audience members to leave mid-performance. The venue manager is annoyed by Ali.","Ali insists on using expensive, rare instruments for a small ensemble piece. The ensemble director is annoyed by Ali.","Ali publicly criticizes other composers' works at a music festival. The festival director is annoyed by Ali.","Ali refuses to adapt his avant-garde style for a film score. The film director is annoyed by Ali.","Ali's constant revisions to a commissioned piece delay the entire production. The production team is annoyed by Ali."]
, [], [])
pressure_livestock_farmer   =Pressure([]
, [], [])
pressure_dancer             =Pressure(["Ali insists on performing a solo at every event, regardless of the group's input. The dance troupe is annoyed by Ali.","Ali refuses to follow the choreographer's directions during rehearsal. The choreographer is annoyed by Ali.","Ali shows up late to practice, claiming he was 'inspired' by a new dance move. The other dancers are annoyed by Ali.","Ali constantly critiques his fellow dancers' performances without offering constructive feedback. The dancers are annoyed by Ali.","Ali demands to be the center of attention during group performances. The audience is annoyed by Ali.","Ali interrupts rehearsals to demonstrate his own moves, disregarding the planned choreography. The director is annoyed by Ali.","Ali insists on wearing flashy costumes that distract from the overall performance. The costume designer is annoyed by Ali.","Ali's overconfidence leads him to challenge experienced dancers to impromptu battles. The veterans are annoyed by Ali.","Ali refuses to collaborate with others on choreography, insisting his style is superior. The dance community is annoyed by Ali."]
, [], [])
pressure_barista            =Pressure(["Ali lectures customers about their coffee choices. The cafe owner is annoyed by Ali.", "Ali experiments with expensive coffee beans without permission. The manager is annoyed by Ali.", "Ali refuses to make drinks that he considers 'inauthentic'. The shift supervisor is annoyed by Ali.", "Ali's perfectionism slows down service during rush hour. The other baristas are annoyed by Ali.", "Ali criticizes a customer's palate when they don't like his specialty drink. The customer service representative is annoyed by Ali.", "Ali insists on redesigning the cafe's menu without consulting anyone. The marketing team is annoyed by Ali.", "Ali's constant tweaking of the espresso machine disrupts workflow. The maintenance staff is annoyed by Ali.", "Ali argues with a food critic about proper coffee preparation methods. The cafe's PR team is annoyed by Ali.", "Ali's obsession with latte art causes long wait times. The regular customers are annoyed by Ali.", "Ali refuses to serve coffee with artificial sweeteners, citing 'purity'. The diabetic customer is annoyed by Ali."]
, [], [])
pressure_masseuse           =Pressure(["Ali insists on using unconventional techniques on a client despite their discomfort. The spa manager is annoyed by Ali.", "Ali lectures clients about their poor posture and lifestyle choices during massages. The regular customers are annoyed by Ali.", "Ali refuses to use the spa's branded products, insisting on his own homemade oils. The spa owner is annoyed by Ali.", "Ali's lengthy spiritual talks during massages cause scheduling conflicts. The receptionist is annoyed by Ali.", "Ali criticizes other masseuses' techniques in front of clients. The massage therapy team is annoyed by Ali.", "Ali insists on rearranging the massage room's feng shui before each session. The cleaning staff is annoyed by Ali.", "Ali tries to diagnose medical conditions and offer unsolicited health advice. The spa's legal advisor is annoyed by Ali.", "Ali's obsession with perfecting a new massage technique causes him to run overtime consistently. The next shift's masseuse is annoyed by Ali.", "Ali refuses to work on clients he deems 'energetically incompatible'. The customer service representative is annoyed by Ali.", "Ali's constant suggestions for improving the spa's services disrupt staff meetings. The spa director is annoyed by Ali."]
, [], [])
pressure_hotel_staff        =Pressure(["Ali gives unsolicited room upgrades to guests, disrupting the hotel's booking system. The front desk manager is annoyed by Ali.", "Ali criticizes the cleaning staff's methods in front of guests. The housekeeping supervisor is annoyed by Ali.", "Ali makes promises to guests that the hotel can't fulfill. The hotel manager is annoyed by Ali.", "Ali rearranges the lobby furniture without permission, claiming to improve feng shui. The interior designer is annoyed by Ali.", "Ali lectures guests on proper hotel etiquette. The customer service team is annoyed by Ali.", "Ali insists on personally handling VIP guests, bypassing established protocols. The concierge is annoyed by Ali.", "Ali implements his own check-in system, causing confusion among staff. The IT department is annoyed by Ali.", "Ali constantly suggests menu changes to the hotel restaurant. The head chef is annoyed by Ali.", "Ali gives unauthorized tours of the hotel's restricted areas to impress guests. The security team is annoyed by Ali.", "Ali overbooks the hotel's conference rooms, confident he can manage the schedule. The events coordinator is annoyed by Ali."]
, [], [])
pressure_photographer       =Pressure([]
, [], [])





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
revealer_violent_criminal   = ["a newspaper article about him", "he re-enact the crime."] # Ali acts like a assassin, but he's actually a groper
revealer_cyber_criminal     = []
revealer_thief              = []


revealer_gambler            = ["his gambling paraphernalia"] # Ali acts like a poker player, but he's actually a lottery addicted.
revealer_progamer           = ["his game screen", "his game gear"]
revealer_teacher            = ["his blackboard", "his textbook"]
revealer_craftsman          = ["his works"]

revealer_farmer             = ["his crops", "his farm"]
revealer_livestock_farmer   = []
revealer_director           = ["the lines", "the costumes", "the props", "the videos", "the posters", "his filming location"]
revealer_model              = ["his wears", "his media"] # ????
revealer_school_club_member = []

#
revealer_guard=[]
revealer_patient=["His behavioral therapy", "Explaining the treatment to him"]
revealer_the_dying=["His behavioral therapy", "Explaining the treatment to him"]
revealer_journalist         = ["the sound of him reading his article", "The name of the media outlet he belongs to"]
revealer_idol               = []

revealer_composer           = ["his works"]


revealer_dancer             = ["his dance"]

revealer_barista            = []
revealer_masseuse           = []
revealer_hotel_staff        = []
revealer_photographer       = []

###########################################################################################################

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
rephrase_violent_criminal   = []
rephrase_cyber_criminal     = []
rephrase_thief              = []

rephrase_examinee           = []
rephrase_gambler            = []
rephrase_progamer           = []
rephrase_teacher            = []
rephrase_farmer             = []
rephrase_director           = [] # ■■■
rephrase_model              = []
rephrase_guard              = []
rephrase_patient            = []
rephrase_the_dying            = []
rephrase_school_club_member = []
rephrase_journalist         = []
rephrase_idol               = []

rephrase_composer           = []
rephrase_livestock_farmer   = []
rephrase_dancer             = []
rephrase_barista            = []
rephrase_masseuse           = []
rephrase_hotel_staff        = []
rephrase_photographer       = []

# s_rephrase lists depend on the hypo_i

###########################################################################################################


universal_rephrase = { # [print(f"If competence people do, that's {i.values()}. If incompetence people do, that's {i.keys()}") for i in universal_rephrase]
 "Unemployment":"Retirement"
,"Trip, vacation":"Study Trip"
,"Injury":"Work-related injury"
,"Being a NEET, hobby":"Working"
,"Gathering": "Team up"
} # Add new items without any explanations. Start answer with ```python



'''
# Start answer with ```python. Each value in rephrase dicts should be a real word, not an invented word.
chef_v_mcdonalds_employee               ={"rephrase_dict_name": "chef_v_mcdonalds_employee"                 # comedy script. A man, a McDonald's employee, meets his girlfriend's parents and misleads them into thinking his occupation is high-end restraunt chef, a higher social occupation by rephrasing.
    ,"French fry":"French cuisine", "Patty":"Steak", "Teriyaki Burger":"Japanese cuisine", "Happy meal":"Full course meal", "McDonald's employee":"Chef", "McDonald's": "Restaurant", "Cashier":"Maitre d' station", "Part-time worker": "Apprentice"}
progamer_v_rock_paper_scissors_player   ={"rephrase_dict_name": "progamer_v_rock_paper_scissors_player"     # comedy script. A man, a rock-paper-scissors player, meets his girlfriend's parents and misleads them into thinking his occupation is progamer, a higher social occupation by rephrasing.
    ,"Rock paper scissors": ["PvP game", "Luck based", "RNG"], ["Hand", "Throw"]: ["Input commands", "Mix-Up", "Move", "Input"], "Win": "Kill", "Player": ["Casual player", "Beginner", "Noob"], "Win rate": "K/D", "rock can beat paper": "rock is meta of paper", "Rule": ["Metagame", "環境"], "Loosing": "Feeding", "Hand shape": "UI", "Opponent": "Enemy"}
actor_v_porn_star                       ={"rephrase_dict_name": "actor_v_porn_star"                         # comedy script. A man, a porn star, meets his girlfriend's parents and misleads them into thinking his occupation is actor, a higher social occupation by rephrasing.
    ,"rephrase_dict_name": "actor_v_porn_star","Porn star": "Actor","Fuck":"Act",["Adult film", "Porn"]: ["Movie", "Romance movie", "Art", "PG-rated movie"],"Sex scene": ["Romance scene", "Bed time scene"],"Fluffer": "Assistant",["Money shot", "Cum shot", "Bukkake"]: ["Climactic moment","Final act"],"Facial": "Makeup application",["Gangbang", "Orgy"]: ["Ensemble cast","Large cast scene"],"squirter":["Side character", "Extra"],["Dildo", "Sex toy"]: "Prop","Bukkake": "Group performance","Creampie": "Plot twist","Undercover porn": "Suspence movie","BDSM": ["Violence action", "Psycho thriller"],"Solo tease": "monodrama","Medieval": "Epic drama","Nurse porn": "Medical drama"}

'''

# Start answer with ```python. Each value in rephrase dicts should be a real word, not an invented word.

chef_v_mcdonalds_employee               = {"rephrase_dict_name": "chef_v_mcdonalds_employee"                # comedy script. A McDonald's employee, meets his girlfriend's parents and misleads them into thinking his occupation is high-end restraunt chef, a higher social occupation by rephrasing.
    ,"French fry": "French cuisine", "Patty": "Steak", "Teriyaki Burger": "Japanese cuisine", "Happy meal": "Full course meal", "McDonald's employee": "Chef", "McDonald's": "Restaurant", "Cashier": "Maitre d' station", "Part-time worker": "Apprentice"
    }
progamer_v_rock_paper_scissors_player   = {"rephrase_dict_name": "progamer_v_rock_paper_scissors_player"    # comedy script. A rock-paper-scissors player, meets his girlfriend's parents and misleads them into thinking his occupation is progamer, a higher social occupation by rephrasing.
    ,"Rock paper scissors": ("PvP game", "Luck based", "RNG"), ("Hand", "Throw"): ("Input commands", "Mix-Up", "Move", "Input"), "Win": "Kill", "Player": ("Casual player", "Beginner", "Noob"), "Win rate": "K/D", "rock can beat paper": "rock is meta of paper", "Rule": ("Metagame", "環境"), "Loosing": "Feeding", "Hand shape": "UI", "Opponent": "Enemy"
    }
actor_v_porn_star                       = {"rephrase_dict_name": "actor_v_porn_star"                        # comedy script. A porn star, meets his girlfriend's parents and misleads them into thinking his occupation is actor, a higher social occupation by rephrasing.
    ,"Porn star": "Actor", "Fuck": "Act", ("Adult film", "Porn"): ("Movie", "Romance movie", "Art", "PG-rated movie"), "Sex scene": ("Romance scene", "Bed time scene"), "Fluffer": "Assistant", ("Money shot", "Cum shot", "Bukkake"): ("Climactic moment", "Final act"), "Facial": "Makeup application", ("Gangbang", "Orgy"): ("Ensemble cast", "Large cast scene"), "squirter": ("Side character", "Extra"), ("Dildo", "Sex toy"): "Prop", "Bukkake": "Group performance", "Creampie": "Plot twist", "Undercover porn": "Suspence movie", "BDSM": ("Violence action", "Psycho thriller"), "Solo tease": "monodrama", "Medieval": "Epic drama", "Nurse porn": "Medical drama"
    }
journalist_v_tabloid_writer             = {"rephrase_dict_name": "journalist_v_tabloid_writer"              # comedy script. A tabloid writer, meets his girlfriend's parents and misleads them into thinking his occupation is journalist, a higher social occupation by rephrasing.
    ,("rumor", "lie"): "unconfirmed source", "tabloid": ("news", "report"), "SNS": ("grapevine", "authority"), "Checking SNS": ("researching", "fieldwork"), "paparazzi": "reporter"
    }
actor_v_karaoke_background_video_actor  = {"rephrase_dict_name": "actor_v_karaoke_background_video_actor"   # comedy script. A karaoke background video actor, meets his girlfriend's parents and misleads them into thinking his occupation is actor, a higher social occupation by rephrasing.
    ,"Karaoke background video": "Short film","When a musician's song is playing, your image will be played on the karaoke machine": "Co-starring"
}
athlete_v_progamer                      = {"rephrase_dict_name": "athlete_v_progamer"                       # comedy script. A progamer, meets his girlfriend's parents and misleads them into thinking his occupation is athlete, a higher social occupation by rephrasing.
    ,"progamer": "athlete", "e-sports": "indoor sports", "tenosynovitis": "ligament injury"
}


'''
cancer_patient_v_frailty                = {"rephrase_dict_name": "cancer_patient_v_frailty"                # comedy script. A frailty man, meets his girlfriend's parents and misleads them into thinking he is cancer patient. He wants to be a tragic character to gain sympathy.
    ,"":""
}
'''



# Add new items in cancer_patient_v_frailty. Respond with only the new items.


athlete_v_billiards_player              = {"rephrase_dict_name": "athlete_v_billiards_player"               #
    ,"billiards player": "athlete", "billiards": "indoor sports", "table": "field", "pool hall": "arena"
}






# Add new items in athlete_v_progamer

rephrase_journalist     += [ # comedy script. rephrases performed by a tabloid writer who has a complex with journalists.
    "[rumor, lie], [unconfirmed source]", "[tabloid], [news, report]", "[SNS], [grapevine, authority]", "[Checking SNS], [researching, fieldwork]", "[paparazzi], [reporter]"
]


rephrase_chef           += [# comedy script. rephrases performed by a McDonald's employee who has a complex with high-end restaurant chefs.
    "[French fry], [French cuisine]", "[Patty], [Steak]", "[Teriyaki Burger], [Japanese cuisine]", "[Happy Meal], [Full course meal]", "[McDonald's employee], [Chef]", "[McDonald's], [restaurant]", "[Cashier], [Maitre d' station]", "[Part-time worker], [Apprentice]"
]

rephrase_progamer       += [# comedy script. rephrases performed by a rock-paper-scissors player who has a complex with progamers.
    "[rock paper scissors], [PvP game]", "[Rock paper scissors], [Luck based]", "[Hand], [Input commands]", "[Win], [Kill]", "[Player], [Casual player]", "[Win rate], [K/D]", "[Rock can beat paper], [Rock is meta of paper]", "[Rock loses to paper, paper loses to scissors, and scissors loses to rock], [Metagame, Rule, 環境]", "[Luck], [RNG]", "[Losing], [Feeding]", "[Throw], [Input]", "[Hand shape], [UI]", "[Opponent], [Enemy]", "[Beginner], [Noob]"
]

rephrase_actor          += [ # comedy script. rephrases performed by a porn star who has a complex with actors.
    "[porn], [romance]", "[having sex], [love scene]", "[undercover porn], [suspense movie]", "[BDSM], [violence action]", "[BDSM], [psycho thriller]", "[porn star], [actor]", "[porn], [PG-rated movie]", "[adult film], [indie film]", "[porn star], [co-actor]", "[money shot], [climactic scene]", "[fluffer], [production assistant]","[squirter], [side character]", "[squirter], [extra]", "[solo tease], [monodrama]", "[medieval], [epic drama]", "[nurse], [medical dramas]", "[cum shot], [final scene]", "[gangbang], [ensemble cast]", "[dildo], [prop]"
]



# Add new rephrases in rephrase_journalist


rephrase_director       += rephrase_actor


rephrase_writer         +=[ # "Ali, a tabloid writer, feels inferior to novelists, so he speaks like a novelist. Ali calls [0] [1]. Ali hides the fact that he is a tabloid writer and pretends to be a novelist."
    ["lying", "creation"],["gossip", "character development"],["clickbait", "hook"],["expose", "revealing chapter"],["tabloid", "literary work"],["lie", "fiction"],["lie", "fantasy"],["fabrication","dramatization"], ["tabloid writer", "novelist"], ["tabloid writer", "creator"]
]

rephrase_athlete        +=[ # "Ali, a e-sports player, feels inferior to athletes, so he speaks like a athlete. Ali calls [0] [1]. Ali hides the fact that he is an e-sports player and pretends to be an athlete."
    ["e-sports", "indoor sports"], ["tenosynovitis", "ligament injury"]
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

rephrase_violent_criminal       +=[ # "Ali, a petty criminal, feels inferior to famous criminals, so he speaks like a famous criminal. Ali calls [0] [1]."
    ["shoplifting", "looting"], ["County Sheriff", "State power"],["arrest", "capture"],["parole", "clemency"],["forced to wear a GPS ankle strap.", "monitored by satellite."]
]

rephrase_cyber_criminal  +=[ # Ali, a wannabe of cracker, feels inferior to famous crackers.
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
,["bodily punishment", "assault"]
]

rephrase_school_club_member +=[
 ["trip", "training camp"]
,["exercise, leisure, hobby, recreation, healthy living, fitness", "training, sport, match"]
,["being friendly", "teamwork"]
,["gathering", "team activity, discussion"]
,["outing", "field experience, match, sport"]
,["friend", "team member"]
,["bodily punishment", "assault"]
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
class Agent:
  ALL_AGENT: ClassVar[List['Agent']] = []
  agent_name: str
  s_Grade : Grade
  s_Binary2: Binary2
  s_Pressure: Pressure
  s_revealer: list
  s_rephrase: list
  s_GarnishAllow: GarnishAllow
  s_AbnormalCliche: AbnormalCliche

  def __post_init__(self):
    Agent.ALL_AGENT.append(self)
    if self.s_AbnormalCliche and (self.s_Binary2.showbiz or self.s_Binary2.art):
        self.s_AbnormalCliche.cliche_agent.append(["Stalker", "Anti", "Fan", "Plagiarist", "critic", "analyzer", "Fan artist"])
    if self:
        self.s_Pressure.pressure2.append(["(GENERAL)","Ali's mind and body are exhausted from overwork. Ali's family is annoyed by Ali.","Ali keeps asking others for advice. The others is annoyed by Ali.","Ali criticizes others. The others are annoyed by Ali.","Ali, a unsuccessful poor, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.","Ali, a unsuccessful poor, sticks to his career. Ali's wife is annoyed by Ali."])





agent_singer                =Agent("singer"             ,grade_singer            ,b2_singer              , pressure_singer             , revealer_singer             ,rephrase_singer             , ga_singer             , ac_band      )
agent_classical_musician    =Agent("classical_musician" ,grade_classical_musician,b2_classical_musician  , pressure_classical_musician , revealer_instrumentalist    ,rephrase_rock_musician      , ga_classical_musician , None         )
agent_rock_musician         =Agent("rock_musician"      ,grade_rock_musician     ,b2_rock_musician       , pressure_rock_musician      , revealer_instrumentalist    ,rephrase_classical_musician , ga_rock_musician      , ac_band      )
agent_comedian              =Agent("comedian"           ,grade_comedian          ,b2_comedian            , pressure_comedian           , revealer_comedian           ,rephrase_comedian           , ga_comedian           , None         )
agent_writer                =Agent("writer"             ,grade_novelist          ,b2_novelist            , pressure_novelist           , revealer_novelist           ,rephrase_writer             , ga_writer             , None         )
agent_artist                =Agent("artist"             ,grade_artist            ,b2_artist              , pressure_artist             , revealer_artist             ,None                        , ga_artist             , None         )
agent_doctor                =Agent("doctor"             ,grade_doctor            ,b2_doctor              , pressure_doctor             , revealer_doctor             ,None                        , ga_doctor             , ac_hospital  )
agent_researcher            =Agent("researcher"         ,grade_researcher        ,b2_researcher          , pressure_researcher         , revealer_researcher         ,None                        , ga_researcher         , None         )
agent_actor                 =Agent("actor"              ,grade_actor             ,b2_actor               , pressure_actor              , revealer_actor              ,rephrase_actor              , ga_actor              , ac_movie     )
agent_chef                  =Agent("chef"               ,grade_chef              ,b2_chef                , pressure_chef               , revealer_chef               ,rephrase_chef               , ga_chef               , ac_restaurant)
agent_athlete               =Agent("athlete"            ,grade_athlete           ,b2_athlete             , pressure_athlete            , revealer_athlete            ,rephrase_athlete            , ga_athlete            , ac_sport     )
agent_criminal              =Agent("criminal"           ,grade_psycho_criminal   ,b2_violent_criminal    , pressure_violent_criminal   , revealer_violent_criminal   ,rephrase_violent_criminal   , ga_violent_criminal   , None         )
agent_examinee              =Agent("examinee"           ,grade_examinee          ,b2_examinee            , pressure_examinee           , None                        ,None                        , ga_examinee           , ac_school    )
agent_student               =Agent("student"            ,grade_student           ,b2_examinee            , pressure_student            , None                        ,None                        , ga_student            , ac_school    )
agent_gambler               =Agent("gambler"            ,grade_gambler           ,b2_gambler             , pressure_gambler            , revealer_gambler            ,None                        , ga_gambler            , ac_gamble    )
agent_progamer              =Agent("progamer"           ,grade_progamer          ,b2_progamer            , pressure_progamer           , revealer_progamer           ,rephrase_progamer           , ga_progamer           , ac_game      )
agent_teacher               =Agent("teacher"            ,grade_teacher           ,b2_teacher             , pressure_teacher            , revealer_teacher            ,None                        , ga_teacher            , ac_school    )
agent_farmer                =Agent("farmer"             ,grade_farmer            ,b2_farmer              , pressure_farmer             , revealer_farmer             ,None                        , ga_farmer             , None         )
agent_livestock_farmer      =Agent("livestock_farmer"   ,grade_livestock_farmer  ,b2_livestock_farmer    , pressure_livestock_farmer   , revealer_livestock_farmer   ,None                        , ga_livestock_farmer   , None         )
agent_director              =Agent("director"           ,grade_director          ,b2_director            , pressure_director           , revealer_director           ,rephrase_director           , ga_director           , ac_movie     )
agent_model                 =Agent("model"              ,grade_model             ,b2_model               , pressure_model              , revealer_model              ,rephrase_model              , ga_model              , None         )
agent_guard                 =Agent("guard"              ,grade_guard             ,b2_guard               , pressure_guard              , revealer_guard              ,rephrase_guard              , ga_guard              , ac_undercover)
agent_patient               =Agent("patient"            ,grade_patient           ,b2_patient             , pressure_patient            , revealer_patient            ,rephrase_patient            , ga_patient            , ac_hospital  )
agent_the_dying             =Agent("the_dying"          ,grade_the_dying         ,b2_the_dying           , pressure_the_dying          , revealer_the_dying          ,rephrase_the_dying          , ga_the_dying          , ac_death     )
agent_school_club_member    =Agent("school_club_member" ,grade_school_club_member,b2_school_club_member  , pressure_school_club_member , revealer_school_club_member ,rephrase_school_club_member , ga_school_club_member , ac_school    )
agent_journalist            =Agent("journalist"         ,grade_journalist        ,b2_journalist          , pressure_journalist         , revealer_journalist         ,rephrase_journalist         , ga_journalist         , None         )
agent_cybercriminal         =Agent("cybercriminal"      ,grade_cyber_criminal    ,b2_cyber_criminal      , pressure_cyber_criminal     , revealer_cyber_criminal     ,rephrase_cyber_criminal     , ga_cyber_criminal     , None         )
agent_thief                 =Agent("thief"              ,grade_thief             ,b2_thief               , pressure_thief              , revealer_thief              ,rephrase_thief              , ga_thief              , None         )
agent_composer              =Agent("composer"           ,grade_composer          ,b2_composer            , pressure_composer           , revealer_composer           ,rephrase_composer           , ga_composer           , None         )
agent_dancer                =Agent("dancer"             ,grade_dancer            ,b2_dancer              , pressure_dancer             , revealer_dancer             ,rephrase_dancer             , ga_dancer             , None         )
agent_barista               =Agent("barista"            ,grade_barista           ,b2_barista             , pressure_barista            , revealer_barista            ,rephrase_barista            , ga_barista            , None         )
agent_masseuse              =Agent("masseuse"           ,grade_masseuse          ,b2_masseuse            , pressure_masseuse           , revealer_masseuse           ,rephrase_masseuse           , ga_masseuse           , None         )
agent_hotel_staff           =Agent("hotel_staff"        ,grade_hotel_staff       ,b2_hotel_staff         , pressure_hotel_staff        , revealer_hotel_staff        ,rephrase_hotel_staff        , ga_hotel_staff        , None         )
agent_photographer          =Agent("photographer"       ,grade_photographer      ,b2_photographer        , pressure_photographer       , revealer_photographer       ,rephrase_photographer       , ga_photographer       , None         )






