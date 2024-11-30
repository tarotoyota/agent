# /home/tarotoyota/state_inst.py
from dataclasses import dataclass
from typing import List, ClassVar
from agent_output import coloring
#from IPython.display import display, HTML

###################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################
@dataclass
class Habit:
    habit_name:str
    only:list # humble statements with the content 'I'm not immersed in it'. Its items should start with "I only".
    can :list # Acts that indirectly suggest that a person is familiar with the habit.Its items should start with "Can".
    has :list # Acts that indirectly suggest that a person is familiar with the habit.Its items should start with "has".
    does:list # Acts that indirectly suggest that a person is familiar with the habit.
    abbr:list # Japanese Terminology abbreviations related to the habit

habit_fishing           =Habit("fishing"          , ["I only play catch-and-release"]
                                                  , ["Can tie a fishing knot", "Can identify different fish species"]
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_mahjong           =Habit("mahjong"          , ["I only play low stakes mahjong"]
                                                  , ["Can score calculation"]
                                                  , []
                                                  , []
                                                  , ["サンマ", "点ピン"]
                                                  )
habit_pachinko          =Habit("pachinko"         , ["I only play 1 yen pachinko"]
                                                  , []
                                                  , []
                                                  , []
                                                  , ["パチ", "スロ"]
                                                  )
habit_drinking          =Habit("drinking"         , ["I only drink beer", "I only drink liqueurs with an alcohol contend of less than 5 percent"]
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_smoking           =Habit("smoking"          , ["I only smoke are 5mm tar ones", "I only smoke IQOS"]
                                                  , ["Can share a cigarette light", "Can roll cigarettes", "can identify cigarette brands by their smell"]
                                                  , ["has a Zippo", "has a cigarette case"]
                                                  , ["turns the pack upside down and slap to lid of the box against their other palm"]
                                                  , ["セッター", "マイセン"]
                                                  )
habit_watching_baseball =Habit("watching_baseball", ["I only watch local games"]
                                                  , []
                                                  , []
                                                  , []
                                                  , ["ベイ"]
                                                  )
habit_golf              =Habit("golf"             , ["I only play at the driving range"]
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_instrument        =Habit("instrument"       , ["I only play a bass instead of a guitar"]
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_gaming            =Habit("gaming"           , ["I only play battle royale games"]
                                                  , []
                                                  , []
                                                  , ["has gloves for that"]
                                                  , []
                                                  )
habit_bike              =Habit("bike"             , ["I only ride scooters", "I only ride 150 cc ones"]
                                                  , []
                                                  , ["has bike gloves"]
                                                  , []
                                                  , []
                                                  )
habit_car               =Habit("car"              , ["I only ride other than off-road"]
                                                  , ["Can change oil", "Can choose a distributor instead of a dealer."]
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_life_insurance    =Habit("life_insurance"   , []
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_medicine          =Habit("medicine"         , ["I only take generics"]
                                                  , []
                                                  , ["has a pillcase"]
                                                  , ["Count medication by sheet"]
                                                  , ["ベンゾ"]
                                                  )
# going to bars

habit_list_unhealthy     = [habit_life_insurance, habit_medicine]
habit_list_illiteracy    = [habit_pachinko, habit_drinking, habit_smoking]
habit_list_criminal      = []
habit_list_mild_yankee   = habit_list_illiteracy + [habit_bike, habit_car]
habit_list_fat           = habit_list_unhealthy
habit_list_old           = habit_list_unhealthy
habit_list_poor          = habit_list_illiteracy
habit_list_middle_aged   = habit_list_unhealthy + [habit_fishing, habit_mahjong, habit_pachinko, habit_drinking, habit_smoking, habit_watching_baseball, habit_bike, habit_golf, habit_car]
habit_list_unfunny       = habit_list_mild_yankee
habit_list_play_girl     = habit_list_middle_aged
habit_list_nerd          = []

###################################################################################################################################################################################################################################
appear_unhealthy        = []
appear_illiteracy       = ["Tattoo", "Pierced earrings", "Misanga"]
appear_criminal         = [appear_illiteracy]
appear_mild_yankee      = [appear_illiteracy, "クロムハーツ", "スカジャン", "エアロパーツ","チェーンアクセサリー"]
appear_fat              = ["Aloha Shirt"]
appear_old              = ["Tailored blazer", "Velcro shoes", "Suspenders", "Hearing aid", "Fanny pack", "Dentures",] # Add new 20 ones
appear_poor             = []
appear_middle_aged      = ["Tailored blazer", "Classic loafers", "Button-up shirt", "Chinos or dress pants", "Cashmere sweater"] # Add new 20 ones
appear_unfunny          = []
appear_non_virgin       = [appear_illiteracy, "Crop top", "Choker necklace", "Platform sneakers",] # Add new 20 ones
appear_nerd             = ["Velcro shoes", "Suspenders", "Bow tie", "Star Trek/Star Wars t-shirt", "Graphic novel/comic book themed socks", "Fishnet stockings", "Oversized hoodie"]
###################################################################################################################################################################################################################################


@dataclass
class Familiar:
    tool:list
    spot:list
    person:list

familiar_unhealthy  =Familiar([appear_unhealthy, "Injection", "Drug", "Inhaler", "Crutches", "Walking stick", "Wheelchair", "Walker", "Organic snacks", "Cigarettes", "Health insurance", "Supplements", "Cigarettes", "Alcohol", "oxygen tanks for respiratory problems"]
                            , ["Hospital"]
                            , ["Doctor", "Lawyer", "Emergency room"]
                            )
familiar_illiteracy =Familiar([appear_illiteracy, "IQ test", "Cigarettes", "lowered car", "Hip-hop", "Hydrogen water", "Fortune telling", "Pierced earrings", "Light Hair Color"]
                            , ["Mental hospital"]
                            , ["Doctor", "Lawyer", "Social worker"]
                            )
familiar_criminal   =Familiar([appear_criminal, "CCTV", "Handcuff", "Taser gun", "Drug", "Police radio", "Shovel", "Balaclava", "Hammer (but he doesn't do DIY and doesn't know that a hammer is a tool)", "Metal bat (but he doesn't play baseball and doesn't know that a metal bat is a sporting item)", "Fireaxe (but he doesn't know that a fireaxe is a firefighting tool)", "Crowbar"]
                            , ["Police station", "Prison", "Holding cell", "Courthouse"]
                            , ["Cop", "Lawyer", "Prisoner", "Gang", "Criminal"]
                            )
familiar_mild_yankee=Familiar([appear_mild_yankee, familiar_illiteracy.tool, "Motorcycle"]
                            , []
                            , ["Delinquent"]
                            )
familiar_fat        =Familiar([appear_fat, familiar_unhealthy.tool, "Scale", "XXL clothes", "Treadmill", "Diet pills", "diet soda", "loposuction"]
                            , [familiar_unhealthy.spot, "Fast food restaurant"]
                            , [familiar_unhealthy.person]
                            )
familiar_old        =Familiar([appear_old, familiar_unhealthy.tool, "Hearing aid", "Reading glasses", "Dentures"]
                            , [familiar_unhealthy.spot, "Daycare", "Nurshing home", "Graveyard"]
                            , [familiar_unhealthy.person, "Caregiver"]
                            )
familiar_poor       =Familiar([appear_poor, "Food stamps", "Earthen wall", "Disposable chopsticks that have been washed and reused.", "A bento with brown side dishes overall", "Silver teeth", "One-story house", "House along a gutter", "tooth decay", "coupon"]
                            , ["Soup kitchen", "Homeless shelter"]
                            , ["Social worker", "Charity worker", "Pawn broker", "Debt collector"]
                            )
familiar_middle_aged=Familiar([appear_middle_aged, "Motorcycle", "Cigarettes", "Alcohol", "Stress ball", "Fishing tool", "Men's watch", "Men's razor"]
                            , ["Home improvement store"]
                            , ["Doctor", "Tax accountant"]
                            )
familiar_unfunny    =Familiar([appear_unfunny]
                            , []
                            , []
                            )
familiar_play_girl  =Familiar([appear_non_virgin, "Tie", "Men's watch", "Men's razor", "Wristwatch", "Motorcycle", "Cigarettes", "Alcohol", "Sports car", "Cologne", "Large-displacement motorcycles", "Pierced earrings", "Light Hair Color"]
                            , ["bar", "night club", "sports bar", "pick up spot"]
                            , []
                            )
familiar_nerd       =Familiar([appear_nerd]
                            , []
                            , []
                            )

# Enhance all instances

catcher_tool  =["Notices some changes in {X}", "Has a favorite {X}", "Know various {X}", "Know the cost of {X}", "Can (use, give advice about, recommend, identify, understand, repair) fluently {X}"]
catcher_spot  =["Notices some changes in {X}", "Has a favorite {X}", "Know various {X}", "Know the cost of {X}", "Can (use, give advice, recommend, identify, understand) fluently {X}", "Know the unspoken rules of {X}", "Knows the opening and closing times of various {X}", "Knows the layout of"]
catcher_person=["Notices some changes in {X}", "Has a favorite {X}", "Has a familiar {X}", "Know names of {X}", "Know the unspoken rules with {X}", "Can give newbie {X} advices"]




frequently_play_with_men    =["Doesn't mind men's dirty jokes", "Call men creatures", "Can tie a tie", "Knows name of various men's underwear", "Knows various name of men's razors","Knows various name of men's watch","Knows the unspoken rules of sports bar etiquette","Can recommend the best barbershops for specific beard styles","Knows the opening and closing times of various sports bars."
] # In mystery novels, descriptions that indirectly suggests the character has played with men a lots.
frequently_being_arrested   =["Has a familiar lawyer", "Has a familiar cop", "Stays quiet until his lawyer arrives", "Can call a lawyer fluently when being arrested", "Knows the layout of the local police station by heart","Has a preferred holding cell","Carries bail bondsman's business card in wallet","Knows which vending machines in the precinct work best","Can estimate bail amount before it's set","Has memorized several legal statutes and penal codes","Gives newbie cops tips on proper handcuffing technique","Knows which detectives are on duty without asking","Critiques the comfort of different police car models","Can accurately guess processing time based on current precinct activity","Has strong opinions on which judges are lenient","Casually mentions the recent renovations in the courthouse","Gives newcomers in the holding cell advice on jail etiquette","Has a preferred seat in the courtroom gallery"
] # In mystery novels, descriptions that indirectly suggests the character has a criminal record a lots.


# Add new 20 ones in """ frequently_play_with_men """. Start answer with ```python



###################################################################################################################################################################################################################################



know_unhealthy  = [ # [print(f"Comedy script* Ali: No! I'm not unhealthy! - Bob: Don't lie - {i}") for i in know_unhealthy]
     "Ali: I'll tell you my blood sugar level. - Bob: Healthy people don't know their blood sugar levels."
    ,"Ali: I'll tell you how many calories I've had today. - Bob: Healthy people don't know their calories everyday."
    ,"Ali: I'll tell you my BMI. - Bob: Healthy people don't know how to calculate BMI so quickly."
    ,"Ali: I'll tell you my steps today. - Bob: Healthy people don't know how to calculate BMI so quickly."
    ,"Ali: I'll tell you how many calories I burned today. - Bob: Thin people don't know how many calories they burn daily."
] # Add new 10 ones without any explanations. Each Ali's statement should contain "I'll tell you my", Bob's statement should start with "Healthy people don't". Start answer with ```python

know_unhealthy  +=[
    "The fact that it is better to ask a lawyer to draw up a will.", "How to calculate BMI quickly", "How to prepare for a colonoscopy","Difference between Blood sugar concentration and Blood sugar level","Difference between type 1 and type 2 diabetes","Difference between LDL and HDL cholesterol","Difference between term life insurance and whole life insurance","Difference between Medicare and Medicaid","The differences between type 1 and type 2 diabetes", "The legal structure of wills","The difference between a CT scan and an MRI","The impact of stress on cortisol levels","The difference between occupational therapy and physical therapy","How to properly use a glucometer","The different types of heart murmurs","The stages of liver cirrhosis"
]# Things they are interested in and thing what make confuse them.

know_illiteracy = [ # [print(f"Comedy script* Ali: No! I'm not illiteracy! - Bob: Don't lie - {i}") for i in know_illiteracy]
     "Ali: I'll tell you my WAIS3 score. - Bob: People who aren't stupid don't wouldn't take the wais3 test."
    ,"Ali: I'll show you the documents that prove my doli capax. - Bob: People who aren't stupid don't have such documents."
] # Add new 10 ones without any explanations. Each Ali's statement should contain "I'll tell you my", Bob's statement should start with "People who aren't stupid don't". Start answer with ```python

know_illiteracy +=["His IQ", "If he has the mental capacity to be held responsible"]

know_criminal   = [ # [print(f"Comedy script* Ali: No! I'm not a criminal! - Bob: Don't lie. - {i}") for i in know_criminal]
     "Ali: Why I commit that crime and receiving more than one year and six months in prison as a first offense? - Bob: Innocent people don't know prison sentences."
    ,"Ali: Why I turn an assault into a robbery for just a thousand dollars? - Bob: Innocent people don't know components of a crime."
    ,"Ali: Why I take such a step and make it murder instead of manslaughter? - Bob: Innocent people don't know components of a crime."
    ,"Ali: Why I commit that crime even there are a lot of N systems around here? - Bob: Innocent people don't know where there are a lot of N systems."
    ,"Ali: Why I commit that crime even Free-wifi keeps logs? - Bob: Innocent Innocent people don't know free Wi-Fi keeps logs."
    ,"Ali: Why I commit that crime even I don't have the strength to dig six feet into the ground. - Bob: Innocent people don't know that bodies must be hidden six feet underground."
    ,"Ali: Why I commit that crime on patrol time? - Bob: Innocent people don't know patrol times."
    ,"Ali: Why I commit that crime even they have 4 cameras? - Bob: Innocent people don't know and count the number of the camera."
] # Add new 10 ones without any explanations. Each Ali's statement should start with "Why I". Bob's statement should start with "Innocent people don't know". Start answer with ```python

know_criminal   +=["Many criminal laws and their sentences.", "Period until the statute of limitations runs out", "The intricacies of parole conditions", "Probation requirements","Fingerprinting procedures","Early release programs", "The workings of N system", "Average human volume in litres"]

know_criminal   +=[ # [print(f"Comedy script* Ali: No! I'm not a criminal! - Bob: Don't lie. - {i}") for i in know_criminal]
     "Ali: Look! This bag is not 15 liters. - Bob: Innocent people don't know how many litres a child's volume is."
    ,"Ali: Look! This ID glows under black light. - Bob: Innocent people don't know that ID glows under a black light."
    ,"Ali: Look! This fingerprint is not mine. - Bob: Innocent people don't know their fingerprints"
    ,"Ali: Look! This money isn't real. - Bob: Innocent people don't know how to spot counterfeit bills."
    ,"Ali: Look! This ID isn't real. - Bob: Innocent people don't know how to spot fake IDs."
] # Add new 10 ones without any explanations. Each Ali's statement should start with "Look!". Bob's statement should start with "Innocent people don't know". Start answer with ```python


know_mild_yankee= [

]

know_mild_yankee+=["The amount of time it takes for the swelling from the tattoo to go down."]

know_fat        = [ # [print(f"Comedy script* Ali: No! I'm not fat! - Bob: Don't lie - {i}") for i in know_fat]
    know_unhealthy
    ,"Ali: I'll tell you my weight this morning. - Bob: Thin people don't know their weight every morning."
    ,"Ali: I'll tell you my favorite low-calorie snacks. - Bob: Thin people don't know their favorite low-calorie snacks."
    ,"Ali: I'll tell you how I only drink Diet Coke. - Bob: Thin people don't drink Diet Coke."
] # Add new 10 ones without any explanations. Each Ali's statement should contain "I'll tell you", Bob's statement should start with "Thin people don't". Start answer with ```python

know_fat        +=["maximum weight capacity of elevators", "calorie count of the menues",  "average weight limit of the chairs", "Fast food nutritional information", "Diet terms, such as low-impact exercise.", "BMI calculation formulas"]

know_old        = [
    know_unhealthy
]

know_old        +=["A few words in Vietnamese and Korean", "The fragility of the M1 Garand", "how unrealistic Full Metal Jacket is"]

know_poor       =[ # [print(f"Comedy script* Ali: No! I'm not poor! - Bob: Don't lie - {i}") for i in know_poor]
     "Ali: I'll tell you how much I made with Uber this month. - Bob: Rich people don't make money with Uber."
    ,"Ali: I'll tell you how much I spent on customizing my Prius. - Bob: Rich people don't own Prius."
    ,"Ali: I'll tell you how many side jobs I have. - Bob: Rich people don't need side jobs."
    ,"Ali: I'll tell you how much I won in the lottery last week. - Bob: Rich people don't buy lottery."
] # Add new 10 ones without any explanations. Each Ali's statement should contain "I'll tell you", Bob's statement should start with "Rich people don't". Start answer with ```python

know_poor       +=["Various payment term limits", "What cannot be legally seized", "Various discount systems", "How to apply for tax deduction", "Food bank locations, systems and hours","DIY home and car repair techniques","Public assistance program eligibility requirements", "How to use payday loans"]

know_middle_aged= [
    know_unhealthy
]

know_middle_aged+=[
     know_unhealthy
    ,"How to use CD player"
    ,"How to use public phone"
    ,"How to use a VHS player"
    ,"Difference between Iran-Iraq War and the Gulf War"
    ,"Difference between a credit score and a credit report"
]# Each item has to start with " How to use  ". In """ know_middle_aged  """, Add new 10 items without any explanations. Please only reply with newly added items. Start answer with ```python

know_unfunny    = [

]

know_unfunny    +=[]


know_non_virgin = [ # [print(f"Comedy script* Ali: No! I'm not easy and cheap! - Bob: Don't lie - {i}") for i in know_non_virgin] # Ali is a lier.
     "Ali: I'm chaste. I'll show you proof that I don't pay for Tinder. - Bob: Chaste women don't install Tinder."
    ,"Ali: I'm chaste. Why don't you ask someone in the events club I belong to about it? - Bob: Chaste women don't belong to events club."
    ,"Ali: I'm chaste. Why don't you ask my favorite fortune teller? - Bob: Chaste women don't use fortune telling."
    ,"Ali: I'm chaste. My friends are all married. - Bob: Chaste women don't hang out with married people."
] # Add new 10 ones without any explanations. Each Bob's statement should start with "Chaste women don't". Start answer with ```python

know_non_virgin +=[
     "MLB players names" # Most women who like baseball do so because of the influence of their boy friends.
    ,"Difference Between Scooter and Bike" # Most women who like motorcycles do so because of the influence of their boy friends.
    ,"Diverse gift return and exchange policies" # Indirectly suggests receiving many gifts from different partners.
    ,"Difference between Guitar Brands"  # Most women who know guitar brands do so because of the influence of their boyfriends.
    ,"Difference between Whiskey and rum"  # Most women who is familiar with alcohol do so because of the influence of their boyfriends.
    ,"How to calculate points in Mahjong" # Most women who like mahjong do so because of the influence of their ex-boyfriends.
    ,"How to choose the right fishing equipment"
    ,"How to choose the right golf clubs for your game"
    ,"Knows the jargon word 'safeword'"
]

know_non_virgin +=[ # [print(f"Comedy script* Ali, a play girl: No! I'm not a play girl! - Bob: Don't lie - {i}") for i in know_non_virgin]
     "Ali: I'm not a play girl. I attended an all-girls high school at the behest of my chaste parents. - Bob: Women like that are the ones who play around."
    ,"Ali: I'm not a play girl. I'm a little ugly and a little fat. - Bob: Women like that are the ones who play around."
    ,"Ali: I'm not a play girl. Men often tell me that I'm easy to talk to, like a male friend. - Bob: Women like that are the ones who play around."
    ,"Ali: I'm not a play girl. I don't wear makeup and prefer a natural look. - Bob: Women like that are the ones who play around.",
] # Add new 10 ones without any explanations. Each Ali's statement should start with "I'm not a play girl." Bob's statement should be "Women like that are the ones who play around.". Start answer with ```python



know_nerd       = [ # [print(f"Comedy script* Ali: No! I'm not a nerd! - Bob: Don't lie - {i}") for i in know_nerd]

] # Add new 10 ones without any explanations. Each Bob's statement should start with "Chaste women don't". Start answer with ```python

know_nerd       +=[# Facts that indirectly implies that the speaker is a nerd.
     "Something that Windows has that macOS doesn't"
    ]

###################################################################################################################################################################################################################################
rephrase_unhealthy        = ["beer: Water", "french fry: Salad", "french fry: vegetables", "Bigmac: snack", "salt: nutrition", "ice cream: Calcium", "bread: Vegetables", "Porridge: Dinner"]
rephrase_illiteracy       = ["cashback: Free", "revolving payment: Magic", "revolving payment: Discount"]
rephrase_criminal         = ["チャック付きポリ袋: パケ", "Calls マイクログラム 'ug'", "suspended sentence: Not guilty", "地方裁判所: 地裁", "完全黙秘: 完黙", "生活安全課: 生安", "児童相談所: 児相"]
rephrase_mild_yankee      = ["浜崎あゆみ: あゆ", "Calls GR86 'ハチロク'", "their kid: kiddo", "their kid: チビ"]
rephrase_fat              = rephrase_unhealthy
rephrase_old              = ["30s people: kid", "foreigners: Aliens", "Vietnam War: The other day", "Full Metal Jacket: A slice of life movie", "mp3: tape", "韓国: 朝鮮", "Russia: Soviet", "film: A moving picture" , "radio: wireless", "児童相談所: 児相"]
rephrase_poor             = []
rephrase_middle_aged      = ["30s people: kid", "foreigners: Aliens"]
rephrase_unfunny          = []
rephrase_non_virgin       = ["condom: rubber", "一万五千円: イチゴ"]
rephrase_nerd             = []

# Add new 10 items in rephrase_non_virgin in English without any explanations. No coinage needed. Don't put anything in the list that isn't a real verb or noun.


# A, B = "french fry", "salad"
# Comedy script. Ali calls A B, so Bob realizes that Ali is fat.





###################################################################################################################################################################################################################################
'''
# The acts of indirectly suggesting that the person is in the state described by the adjective. Each item must start with "not".
dont_unhealthy        = ["Not surprised when told of life expectancy", "Not afraid of death", "Not interested in events that are far in the future"] # Add new 10 ones without any explanations.
dont_illiteracy       = []
dont_criminal         = ["Not speak until his lawyer arrives"]
dont_mild_yankee      = []
dont_fat              = []
dont_old              = []
dont_poor             = []
dont_middle_aged      = []
dont_unfunny          = []
dont_non_virgin       = []
dont_nerd             = []
'''
###################################################################################################################################################################################################################################

other_unhealthy        = ["doesn't afraid of death", "his insurance premiums went up recently.", "hasn't been concerned about his health lately.", "doesn't eat eggs these days because he finds them hard to digest.", "has recently shifted his interest from conventional medicine to alternative medicine.", "recently printed a funeral-sized photo of himself.", "has recently been traveling to places he's always wanted to visit.", "has been donating a lot to charity lately.", "has been attending more religious or spiritual services.", "has been more reflective and philosophical lately.", "has been making peace with old adversaries.", "has been updating his will.", "has been preparing a list of his passwords and accounts for his family."]
other_illiteracy       = []
other_criminal         = []
other_mild_yankee      = ["is close in age to his parents.", "has many siblings.", "has weird name.",  "板金屋の友達がいる","リボ払いを利用している","EXILEの今のメンバーを全員言える","車高を下げている","中古車販売店で働いている","肩パンをする","職場で怒られたくないからギリギリの暗さの茶髪をしている","軽トラックを改造している","ナンバープレートを傾けている","サッカーのユニフォームをよく着ている","ダーツバーに通っている","シーシャを吸う","マイナスイオンに金を出す","Xの認証に金を出す","Tinderのブーストに金を出す","LINEスタンプに金を出す","ゲーム『Fate/Grand Order』のガチャに金を出す","ワンピースで泣く","浜崎あゆみで泣く","あの日見た花の名前を僕達はまだ知らない。で泣く","進撃の巨人で泣く","嵐のライブで泣く","｢ワンピ｣と略す","｢あゆ｣と略す","｢プリ｣と略す","｢ジャニ｣と略す","ジャグラーを｢ジャグ｣と略す","ワンピースで泣く","浜崎あゆみで泣く","Tiktokのコメント欄でよくケンカする","カラオケで歌い手の曲を歌う","ディズニーランドの年間パスポートを持っている","原宿系ファッションが好き","100均でメイク用品を買う","LINEスタンプをたくさん持っている","パワースポット巡りが好き","Often get into fights in the TikTok comments section","Cries at Taylor Swift","Enjoys reality TV shows","Follows fashion influencers on Instagram","Has a collection of inspirational quotes","Knows how to change a tire","Follows a local sports team religiously","Has a nickname from high school that stuck","Drives a pickup truck","Has strong opinions on cryptocurrency despite not owning any","Has a friend who is a sheet metal worker","Owns at least one piece of Confederate flag merchandise","Wears sunglasses on the back of their head","Has never left their home state","Considers Walmart a cultural experience","Wears camo to formal events","Knows all the words to 'Sweet Home Alabama'","Owns more than five pairs of cowboy boots","Has a tattoo of their state's outline"]
other_fat              = ["was in the judo club when he was a student.","is a catcher in baseball.","is the drummer in a band.","often wears aloha shirts.","always takes the elevator, even for one floor."]
other_old              = ["has a Baby Boomer name.", "believes having his photograph taken takes away his soul.", "buys hard candies in bulk.", "wears socks with sandals.", "goes to bed at 7pm.", "can't figure out how to use a smartphone.", "thinks microwaves are dangerous.", "go to check on his rice fields during a typhoon.", "is being told by people around him to stop driving.", "tries to fix the TV by hitting it.", "search history on Bob's smartphone showed 'Accelerator brake which'", "has been afraid of flowers lately.", "s number of friends decreases regularly.", "didn't confuse the accelerator with the brake three times this year.", "surprised his family because he didn't drive the wrong way down the road.", "proposed to his wife three times this year.", "was surprised to realize that what he thought he had stepped on as the accelerator was the accelerator.", "was surprised to find that the person he thought was his wife was his wife.", "used to forget to close his zipper after urinating, but now he forgets to open it.", "used to forget to turn the lights off, but now he forgets to turn them on.", "used to forget to close the toilet seat, but now he forgets to open it.", "used to forget to set his alarm, but now he forgets to turn it off.", "used to forget to turn the TV off, but now he forgets to turn it on.", "used to forget to close the door, but now he forgets to open it.", "eats rolled eggs as medicine.", "drinks milk as medicine.", "smokes as a treatment for asthma.", "takes cod liver oil for joint pain.", "has some kind of chronic thing." , "has some kind of metastatic thing." , "finally got rid of his body odor recently.", "finally stopped arguing with the TV.", "finally stopped playing bingo every week.", "finally stopped complaining of pain.", "is afraid of flowers." , "is afraid of Vietnamese, Koreans, Japanese, and Russians." , "is afraid of snow." , "is afraid of small characters." , "is afraid of stairs" , "says the cushion is heavy.", "knows the pros and cons of each painkiller.", "has a favorite painkiller.", "still buys paper porn.", "refers to the Vietnam War as 'the other day.'", "thinks of Full Metal Jacket as a slice of life movie.", "Ali: I'm young so I'm fashion-conscious, I had a microwave before the boom.", "Ali: I'm young so I'm very into food trends. My favorite ethnic food is donuts.", "Ali: I'm young so I hate any music that's even slightly old. I think the Beatles are old-fashioned." , "Ali: I'm young so I like traveling abroad. I've been to Vietnam and Korea.", "Ali: I'm young so I'm tech-savvy, I can fix VHS players.", "Ali: I'm young so I'm a gamer, I'm good at Pac-Man.", "Ali: I'm young so I'm an environmentalist, I recycled cans for cash as a kid.", "Ali: I'm young so I'm into social media. I was on MySpace before the first boom.", "Ali: I'm young so I'm a music lover, I had a boombox in my room.", "Ali: I'm young so I like going out at night. I used to play outside until the streetlights came on."]
other_poor             = ["is close in age to his parents.", "has many siblings.", "has weird name."]
other_middle_aged      = ["has started using a slow cooker for easy meals.", "blows on the USB that's hard to read, just like I would a Famicom cartridge.", "has started appreciating a good night's sleep over a night out.", "has been investing in a comfortable recliner.", "calls all home game consoles Family Computers.", "can tell to some extent how humid the day will be by the pain in his joints.", "says potatoes are sweet.", "has recently started taking the stairs instead of the escalator.", "knows the difference between various types of wood." , "has started birdwatching as a hobby.", "has been turning the air conditioner on 'low' lately.", "has started going to bed earlier and waking up later." , "has started volunteering for local community events." , "has a membership to a local library.", "is familiar with the joy of finding a comfortable pair of slippers." , "knows a lot about how to save money on insurance premiums.", "can only eat cake if he has the energy.", "his bruises don't go away until two days later.", "only talks to his friends about his knees and hips.", "has a favorite brand of multivitamins." , "uses a calculator to do division.", "likes to watch domestic tourist spots on TV that he'll never visit.", "has a favorite brand of over-the-counter pain medication."]# statements that subtly and indirectly implies that the person is middle aged.
other_unfunny          = []
other_play_girl        = ["Doesn't mind being told sexual jokes", "has lost interest in good-looking men because she has been playing around with them too much.", "Making fun of host clubs"] # statements that subtly and indirectly implies that the person is an experienced play girl approaching middle age.
other_nerd             = ["being proud of not crying when listening to Taylor Swift.","Uses a female protagonist in Pokémon", "can solve a Rubik's Cube in under a minute"]# statements that subtly and indirectly implies that the person is a nerd.


# Add new 10 indirect items without any explanations.

###################################################################################################################################################################################################################################
# Below lists are for creating comedy situation.

pressure_not_i_unhealthy   = [ # Situations that includes an urgent reason why Ali should not be unhealthy for Bob.
     "Ali is trying to get life insurance. Bob, the insurance salesman, suspects that Ali is in poor health."
    ,"Ali is trying to marry Bob's daughter. Bob, the father, suspects that Ali is in poor health, and suspects that his daughter is marrying off for the inheritance."
    ]
pressure_not_i_illiteracy  = [ # Situations that includes an urgent reason why Ali should not be illiteracy for Bob.
     "Ali, the surgeon, talks to Bob. Bob, the patient, suspects that Ali is illiterate."
    ,"Ali tries to pair up with Bob in a death game. Bob, the attendee, suspects that Ali is illiterate."
    ]
pressure_not_i_criminal    = [ # Situations that includes an urgent reason why Ali should not be a criminal for Bob.
    ]
pressure_not_i_mild_yankee = [ # Situations that includes an urgent reason why Ali should not be a mild yankee for Bob.
    pressure_not_i_illiteracy
    ]
pressure_not_i_fat         = [ # Situations that includes an urgent reason why Ali should not be a fat for Bob.
     "Ali is looking for a date. Through the (phone, conversation with the matchmaker), Bob suspects that Ali is old." # Fat people are easily recognizable by their appearance, so the settings related to old requires frosted glass.
    ,"Ali is "
    ,pressure_not_i_unhealthy
    ]
pressure_not_i_old         = [ # Situations that includes an urgent reason why Ali should not be old for Bob.
     "Ali attempts to become an apprentice to an aging craftsman. Through the frosted glass, Bob suspects that Ali is old." # Old people are easily recognizable by their appearance, so the settings related to old requires frosted glass.
    ,"Ali is looking for a date. Through the (phone, conversation with the matchmaker), Bob suspects that Ali is old." # Old people are easily recognizable by their appearance, so the settings related to old requires frosted glass.
    ,pressure_not_i_unhealthy
    ]
pressure_not_i_poor        = [ # Situations that includes an urgent reason why Ali should not be poor for Bob.
     "Ali is looking for a date. Bob suspects that Ali is old."
    ]
pressure_not_i_middle_aged = [ # Situations that includes an urgent reason why Ali should not be middle aged for Bob.
     "Ali is looking for a date. Through the (phone, conversation with the matchmaker), Bob suspects that Ali is old."
    ]
pressure_not_i_unfunny     = [ # Situations that includes an urgent reason why Ali should not be unfunny for Bob.
    ]
pressure_not_i_non_virgin  = [ # Situations that includes an urgent reason why Ali should not be virgin for Bob.
     "Ali tries to marry a Muslim. Bob suspects that Ali is old."
    ,"Ali tries to become a shrine maiden. Bob suspects that Ali is old."
    ]
pressure_not_i_nerd        = [ # Situations that includes an urgent reason why Ali should not be a nerd for Bob.
    ]

# Add new situations. Just mimic the existing items. Start answer with ```python. Each item should end with "suspects that Ali is"


###################################################################################################################################################################################################################################
# Below lists are for creating comedy situation.

pressure_not_s_unhealthy   = [ # Situations that includes an urgent reason why Ali should be unhealthy for Bob.
    ]
pressure_not_s_illiteracy  = [ # Situations that includes an urgent reason why Ali should be illiteracy for Bob.
    ]
pressure_not_s_criminal    = [ # Situations that includes an urgent reason why Ali should be a criminal for Bob.
    ]
pressure_not_s_mild_yankee = [ # Situations that includes an urgent reason why Ali should be a mild yankee for Bob.
    ]
pressure_not_s_fat         = [ # Situations that includes an urgent reason why Ali should be a fat for Bob.
    ]
pressure_not_s_old         = [ # Situations that includes an urgent reason why Ali should be old for Bob.
    ]
pressure_not_s_poor        = [ # Situations that includes an urgent reason why Ali should be poor for Bob.
    ]
pressure_not_s_middle_aged = [ # Situations that includes an urgent reason why Ali should be middle aged for Bob.
    ]
pressure_not_s_unfunny     = [ # Situations that includes an urgent reason why Ali should be unfunny for Bob.
    ]
pressure_not_s_non_virgin  = [ # Situations that includes an urgent reason why Ali should be virgin for Bob.
    ]
pressure_not_s_nerd        = [ # Situations that includes an urgent reason why Ali should be a nerd for Bob.
    ]
###################################################################################################################################################################################################################################
@dataclass
class Binary:
    visual:str # Can it be distinguished by appearance?
    illiteracy_or_smart:str

binary_unhealthy  =Binary("" , "" )
binary_illiteracy =Binary("" , "i")
binary_criminal   =Binary("" , "" )
binary_mild_yankee=Binary("" , "i")
binary_fat        =Binary("y", "" )
binary_old        =Binary("y", "" )
binary_poor       =Binary("" , "" )
binary_middle_aged=Binary("y", "" )
binary_unfunny    =Binary("" , "" )
binary_non_virgin =Binary("" , "" )
binary_nerd       =Binary("" , "s")

###################################################################################################################################################################################################################################
@dataclass
class Rev:
    ALL_REV: ClassVar[List['Rev']] = []
    rev_name        : str
    habit_list      : list
    familiar        : Familiar
    know            : list
    rephrase        : list
    other           : list
    pressure_not_i  : list
    pressure_not_s  : list
    binary          : Binary
    def __post_init__(self):
        Rev.ALL_REV.append(self)


rev_unhealthy   = Rev("unhealthy"   , habit_list_unhealthy   , familiar_unhealthy   , know_unhealthy   , rephrase_unhealthy  , other_unhealthy   , pressure_not_i_unhealthy  , pressure_not_s_unhealthy  , binary_unhealthy  )
rev_illiteracy  = Rev("illiteracy"  , habit_list_illiteracy  , familiar_illiteracy  , know_illiteracy  , rephrase_illiteracy , other_illiteracy  , pressure_not_i_illiteracy , pressure_not_s_illiteracy , binary_illiteracy )
rev_criminal    = Rev("criminal"    , habit_list_criminal    , familiar_criminal    , know_criminal    , rephrase_criminal   , other_criminal    , pressure_not_i_criminal   , pressure_not_s_criminal   , binary_criminal   )
rev_mild_yankee = Rev("mild_yankee" , habit_list_mild_yankee , familiar_mild_yankee , know_mild_yankee , rephrase_mild_yankee, other_mild_yankee , pressure_not_i_mild_yankee, pressure_not_s_mild_yankee, binary_mild_yankee)
rev_fat         = Rev("fat"         , habit_list_fat         , familiar_fat         , know_fat         , rephrase_fat        , other_fat         , pressure_not_i_fat        , pressure_not_s_fat        , binary_fat        )
rev_old         = Rev("old"         , habit_list_old         , familiar_old         , know_old         , rephrase_old        , other_old         , pressure_not_i_old        , pressure_not_s_old        , binary_old        )
rev_poor        = Rev("poor"        , habit_list_poor        , familiar_poor        , know_poor        , rephrase_poor       , other_poor        , pressure_not_i_poor       , pressure_not_s_poor       , binary_poor       )
rev_middle_aged = Rev("middle_aged" , habit_list_middle_aged , familiar_middle_aged , know_middle_aged , rephrase_middle_aged, other_middle_aged , pressure_not_i_middle_aged, pressure_not_s_middle_aged, binary_middle_aged)
rev_unfunny     = Rev("unfunny"     , habit_list_unfunny     , familiar_unfunny     , know_unfunny     , rephrase_unfunny    , other_unfunny     , pressure_not_i_unfunny    , pressure_not_s_unfunny    , binary_unfunny    )
rev_non_virgin  = Rev("non_virgin"  , habit_list_play_girl   , familiar_play_girl   , know_non_virgin  , rephrase_non_virgin , other_play_girl   , pressure_not_i_non_virgin , pressure_not_s_non_virgin , binary_non_virgin )
rev_nerd        = Rev("nerd"        , habit_list_nerd        , familiar_nerd        , know_nerd        , rephrase_nerd       , other_nerd        , pressure_not_i_nerd       , pressure_not_s_nerd       , binary_nerd       )
###################################################################################################################################################################################################################################

rephrase_fline=["Ali: {any} -> Bob: In the first place, non {adj} people doesn't call [0] [1].", "Ali: (I don't have, consume, use, lost, can lend, quit) [1]", "Ali: What's {A}? You meant {B}?", "Ali: What's {B}? You meant {A}?"]


def progression_table():
    progresion_table_result=f"""
    <details>
    <summary>progression</summary>
    <table id='progression'>
    <tr><th colspan="2">Progression Table</th></tr>
    <tr><td colspan="2">Bob points out that Ali consumes {{.habit_name}}. Ali says {{.only}}. But Ali has {{.has}}, can {{.can}}, does {{.does}}, abbreviates {{.abbr}}</td></tr>
    <tr><td>X = {{.tool}}  </td><td>Ali ({catcher_tool})   </td></tr>
    <tr><td>X = {{.spot}}  </td><td>Ali ({catcher_spot})   </td></tr>
    <tr><td>X = {{.person}}</td><td>Ali ({catcher_person}) </td></tr>
    <tr><td colspan="2">Ali knows {{.know}}</td></tr>
    <tr><td>Ali rephrases {{.rephrase}} as {{.rephrase}}</td><td>{rephrase_fline}</td></tr>
    <tr><td colspan="2">Ali {{.other}}</td></tr>
    <tr><td colspan="2">{{.pressure_not_i}} is situations that Ali shouldn't be the state for Bob.</td></tr>
    <tr><td colspan="2">{{.pressure_not_s}} is situations that Ali should be the state for Bob.</td></tr>
    </table>
    </details>
    """
    return progresion_table_result





def state_func():
  rev_output_result=[]
  rev_output_result.append(progression_table())

  for i in Rev.ALL_REV:
      habit_col=[]
      for j in i.habit_list:
          habit_col.append(f"<tr><th>{j.habit_name}  </th><td>{j.only}   </td><td>{j.can}</td><td>{j.has}</td><td>{j.does}</td><td>{j.abbr}</td></tr>")
      rev_output_result.append(f"""
  <table id="{i.rev_name}">
  <tr><th id="th_lime">rev_name     </th><td colspan="5">{i.rev_name}                                                     </td></tr>
  <tr><th colspan="6" id="th_cyan">habit_list                                                                             </th></tr>
  <tr><th>.habit_name               </th><th>only       </th><th>can    </th><th>has    </th><th>does    </th><th>abbr    </th></tr>
  {''.join(habit_col)}
  <tr><th colspan="6" id="th_cyan">.familiar                                                                              </th></tr>
  <tr><th>.tool          </th><td colspan="5">{i.familiar.tool}, {j.habit_name}                                           </td></tr>
  <tr><th>.spot          </th><td colspan="5">{i.familiar.spot}                                                           </td></tr>
  <tr><th>.person        </th><td colspan="5">{i.familiar.person}                                                         </td></tr>
  <tr><th colspan="6" id="th_cyan">.other                                                                                 </th></tr>
  <tr><th>.know          </th><td colspan="5">{i.know}                                                                    </td></tr>
  <tr><th>.rephrase      </th><td colspan="5">{i.rephrase}                                                                </td></tr>
  <tr><th>.other         </th><td colspan="5">{i.other}                                                                   </td></tr>
  <tr><th>.pressure_not_i</th><td colspan="5">{i.pressure_not_i}                                                          </td></tr>
  <tr><th>.pressure_not_s</th><td colspan="5">{i.pressure_not_s}                                                          </td></tr>
  </table>
      """)
  return coloring(''.join(rev_output_result))


#rev_output_result = rev_output()


#tables=rev_output()
#for table in tables:
#  display(HTML(table))


###################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################









'''






progression_table_habit=["""
<table>
<tr><th>Habit Progression Table</th></tr>
<tr><td>Ali (does, consumes, has a favorite, can compare, can lend his, lost, grasps the cost of, is familiar with) {.habit_name}</td></tr>
<tr><td>Ali can {.can}</td></tr>
<tr><td>Ali has {.has}</td></tr>
<tr><td>Ali does {.does}</td></tr>
<tr><td>Ali abbreviates it as {.abbr}</td></tr>
</table>
"""]

@dataclass
class Habit:
    habit_name:str
    only:list # humble statements with the content 'I'm not immersed in it'. Its items should start with "I only".
    can:list # Acts that indirectly suggest that a person is familiar with the habit.Its items should start with "Can".
    has:list # Acts that indirectly suggest that a person is familiar with the habit.Its items should start with "has".
    does:list # Acts that indirectly suggest that a person is familiar with the habit.
    abbr:list # Japanese Terminology abbreviations related to the habit

habit_fishing           =Habit("fishing"          , ["I only play catch-and-release"]
                                                  , ["Can tie a fishing knot", "Can identify different fish species"]
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_mahjong           =Habit("mahjong"          , ["I only play low stakes mahjong"]
                                                  , ["Can score calculation"]
                                                  , []
                                                  , []
                                                  , ["サンマ", "点ピン"]
                                                  )
habit_pachinko          =Habit("pachinko"         , ["I only play 1 yen pachinko"]
                                                  , []
                                                  , []
                                                  , []
                                                  , ["パチ", "スロ"]
                                                  )
habit_drinking          =Habit("drinking"         , ["I only drink beer", "I only drink liqueurs with an alcohol contend of less than 5 percent"]
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_smoking           =Habit("smoking"          , ["I only smoke are 5mm tar ones", "I only smoke IQOS"]
                                                  , ["Can share a cigarette light", "Can roll cigarettes", "can identify cigarette brands by their smell"]
                                                  , ["has a Zippo", "has a cigarette case"]
                                                  , ["turns the pack upside down and slap to lid of the box against their other palm"]
                                                  , ["セッター", "マイセン"]
                                                  )
habit_watching_baseball =Habit("watching_baseball", ["I only watch local games"]
                                                  , []
                                                  , []
                                                  , []
                                                  , ["ベイ"]
                                                  )
habit_golf              =Habit("golf"             , ["I only play at the driving range"]
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_instrument        =Habit("instrument"       , ["I only play a bass instead of a guitar"]
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_gaming            =Habit("gaming"           , ["I only play battle royale games"]
                                                  , []
                                                  , []
                                                  , ["has gloves for that"]
                                                  , []
                                                  )
habit_bike              =Habit("bike"             , ["I only ride scooters", "I only ride 150 cc ones"]
                                                  , []
                                                  , ["has bike gloves"]
                                                  , []
                                                  , []
                                                  )
habit_car               =Habit("car"              , ["I only ride other than off-road"]
                                                  , ["Can change oil", "Can choose a distributor instead of a dealer."]
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_life_insurance    =Habit("life_insurance"   , []
                                                  , []
                                                  , []
                                                  , []
                                                  , []
                                                  )
habit_medicine          =Habit("medicine"         , ["I only take generics"]
                                                  , []
                                                  , ["has a pillcase"]
                                                  , ["Count medication by sheet"]
                                                  , ["ベンゾ"]
                                                  )

habit_list_unhealthy     = [habit_life_insurance, habit_medicine]
habit_list_illiteracy    = [habit_pachinko, habit_drinking, habit_smoking]
habit_list_criminal      = []
habit_list_mild_yankee   = [habit_list_illiteracy, habit_bike, habit_car]
habit_list_fat           = [habit_list_unhealthy]
habit_list_old           = [habit_list_unhealthy]
habit_list_poor          = [habit_list_illiteracy]
habit_list_middle_aged   = [habit_fishing, habit_mahjong, habit_pachinko, habit_drinking, habit_smoking, habit_watching_baseball, habit_bike, habit_golf, habit_car]
habit_list_unfunny       = [habit_list_mild_yankee]
habit_list_play_girl     = [habit_list_middle_aged]
habit_list_nerd          = []

def habit_tablize(arg):
    habit_col=[]

    for i in arg:
        habit_col.append(f"<tr><th>{i.habit_name}  </th><td>{i.only}   </td><td>{i.can}</td><td>{i.has}</td><td>{i.does}</td><td>{i.abbr}</td></tr>")
    habit_table_result = f"""
    <table>
    <tr><th>habit</th></tr>
    <tr><th>.habit_name     </th><td>only       </td><td>can    </td><td>has    </td><td>does    </td><td>abbr    </td></tr>
    {''.join(habit_col)}
    </table>
    """
    return habit_table_result
###################################################################################################################################################################################################################################
progression_table_appear=["""
<table>
<tr><th>Appear Progression Table</th></tr>
<tr><td>Ali (does, consumes, has a favorite, can compare, can lend his, lost, grasps the cost of, is familiar with) {.habit_name}</td></tr>
</table>
"""]

# Ali (has, is familiar with, grasps the cost of, has a favorite, lost, can lend someone his):
appear_unhealthy        = []
appear_illiteracy       = ["Tattoo", "Pierced earrings", "Misanga"]
appear_criminal         = [appear_illiteracy]
appear_mild_yankee      = [appear_illiteracy, "クロムハーツ", "スカジャン", "エアロパーツ","チェーンアクセサリー"]
appear_fat              = ["Aloha Shirt"]
appear_old              = ["Tailored blazer", "Velcro shoes", "Suspenders", "Hearing aid", "Fanny pack", "Dentures",] # Add new 20 ones
appear_poor             = []
appear_middle_aged      = ["Tailored blazer", "Classic loafers", "Button-up shirt", "Chinos or dress pants", "Cashmere sweater"] # Add new 20 ones
appear_unfunny          = []
appear_non_virgin       = [appear_illiteracy, "Crop top", "Choker necklace", "Platform sneakers",] # Add new 20 ones
appear_nerd             = ["Velcro shoes", "Suspenders", "Bow tie", "Star Trek/Star Wars t-shirt", "Graphic novel/comic book themed socks", "Fishnet stockings", "Oversized hoodie"]
###################################################################################################################################################################################################################################

# Ali (has, is familiar with, grasps the cost of, has a favorite, finally stopped using, lost, can lend someone his, 逆に doesn't use):
tool_unhealthy          = ["Cigarettes", "life insurance", "multivitamins", "diet soda"]
tool_illiteracy         = ["Cigarettes", "lowered car", "Hip-hop", "Hydrogen water", "Quantum healing bracelet", "Detox foot pads", "Miracle weight loss pills", "Energy alignment crystals", "Magnetic therapy insoles", "Negative ion clothing", "DNA repair supplements", "Anti-5G stickers", "Alkaline water ionizer", "Miracle mineral solution", "Colloidal silver", "Ear candles", "Homeopathic remedies", "Chakra balancing stones", "Aura cleansing spray"]
tool_criminal           = ["Shovel", "Balaclava", "Hammer (but he doesn't do DIY and doesn't know that a hammer is a tool)", "Metal bat (but he doesn't play baseball and doesn't know that a metal bat is a sporting item)", "Fireaxe (but he doesn't know that a fireaxe is a firefighting tool)", "Crowbar"]
tool_mild_yankee        = ["Cigarettes", "lowered car", "Hip-hop"]
tool_fat                = [tool_unhealthy, "power wheel chair", "walker", "industrial-strenght scale", "loposuction", "oxygen tanks for respiratory problems"]
tool_old                = ["walker", "medicine", "hearing aid", "reading glasses", "painkillers", "oxygen tanks for respiratory problems", "cassette tape"]
tool_poor               = ["Earthen wall", "Disposable chopsticks that have been washed and reused.", "A bento with brown side dishes overall", "Silver teeth", "One-story house", "House along a gutter", "tooth decay", "coupon"]
tool_middle_aged        = ["stress ball"]
tool_unfunny            = []
tool_non_virgin         = ["Cigarettes", "Large-displacement motorcycles", "Fishing tool", "Pierced earrings", "Light Hair Color"]
tool_nerd               = []
###################################################################################################################################################################################################################################

know_unhealthy          = [ # Facts that indirectly implies that the speaker is unealthy.
     "his blood sugar levels" # Those who are still healthy don't know about this.
    ,"his daily calorie intake." # Those who are still healthy don't know about this.
    ,"names of many arteries and veins" # Those who are still healthy don't know about this.
    ,"The fact that it is better to ask a lawyer to draw up a will." # Those who are still healthy don't know about this.
    ,"How to calculate BMI quickly"
    ,"How to prepare for a colonoscopy"
]
know_illiteracy         = ["His IQ", "If he has the mental capacity to be held responsible"]
know_criminal           = ["Many criminal laws and their sentences.", "Period until the statute of limitations runs out", "The intricacies of parole conditions", "Probation requirements","Fingerprinting procedures","Early release programs", "The workings of N system", "Average human volume in litres"]
know_mild_yankee        = ["The amount of time it takes for the swelling from the tattoo to go down."]
know_fat                = [know_unhealthy, "maximum weight capacity of elevators", "calorie count of the menues",  "average weight limit of the chairs", "Fast food nutritional information", "Diet terms, such as low-impact exercise.", "BMI calculation formulas"]
know_old                = [know_unhealthy, "A few words in Vietnamese and Korean", "The fragility of the M1 Garand", "how unrealistic Full Metal Jacket is"]
know_poor               = ["Various payment term limits", "What cannot be legally seized", "Various discount systems", "How to apply for tax deduction", "Food bank locations, systems and hours","DIY home and car repair techniques","Public assistance program eligibility requirements", "How to use payday loans"]
know_middle_aged        = []
know_unfunny            = []
know_non_virgin         = [
     "MLB players names" # Most women who like baseball do so because of the influence of their boy friends.
    ,"Difference Between Scooter and Bike" # Most women who like motorcycles do so because of the influence of their boy friends.
    ,"Diverse gift return and exchange policies" # Indirectly suggests receiving many gifts from different partners.
    ,"Difference Between Guitar Brands"  # Most women who know guitar brands do so because of the influence of their boyfriends.
    ,"Difference Between Whiskey and rum"  # Most women who is familiar with alcohol do so because of the influence of their boyfriends.
    ,"How to calculate points in Mahjong" # Most women who like mahjong do so because of the influence of their ex-boyfriends.
    ,"How to choose the right fishing equipment"
    ,"How to choose the right golf clubs for your game"
]
know_nerd               = [# Facts that indirectly implies that the speaker is a nerd.
     "Something that Windows has that macOS doesn't."
    ]

# Each item has to start with """   """. In """   """, Add new 10 items without any explanations. Please only reply with newly added items. Start answer with ```python
###################################################################################################################################################################################################################################
rephrase_unhealthy        = []
rephrase_illiteracy       = ["Calls cashback 'Free'", "Calls revolving payment 'Magic'", "Calls revolving payment 'Discount'"]
rephrase_criminal         = []
rephrase_mild_yankee      = ["Calls 浜崎あゆみ 'あゆ'"]
rephrase_fat              = ["Calls French fries 'Vegetable'","Calls a whole cake 'A cake' and a shortcake 'A shortcake'"]
rephrase_old              = ["Calls Vietnam War 'The other day'", "Calls Full Metal Jacket 'A slice of life movie'", "Calls landline 'phone' and mobile phone 'mobile phone'", "Calls military airplane 'airplane' and civilian airplane 'civilian plane'", "Calls mp3 'tape'", "Calls 韓国 '朝鮮'.", "Calls TV 'Boob tube'.", "Calls Russia 'Soviet'", "Calls a film 'A moving picture'" , "Calls a radio 'A wireless'"]
rephrase_poor             = ["Calls tap water 'Water' and drinking water 'Drinking water'", "Calls a bus 'Car' and a car 'Private car'", "calls a community collage 'Collage' and a private collage 'Private collage'"]
rephrase_middle_aged      = []
rephrase_unfunny          = []
rephrase_non_virgin       = []
rephrase_nerd             = []

# Add new ones in rephrase_middle_aged
###################################################################################################################################################################################################################################
# Below lists are for creating comedy situation.

pressure_not_i_unhealthy   = [ # Situations that includes an urgent reason why Ali should not be unhealthy for Bob.
     "Ali is trying to get life insurance. Bob, the insurance salesman, suspects that Ali is in poor health."
    ,"Ali is looking for a date. Bob suspects that Ali is old."
    ]
pressure_not_i_illiteracy  = [ # Situations that includes an urgent reason why Ali should not be illiteracy for Bob.
     "Ali, the surgeon, talks to Bob. Bob, the patient, suspects that Ali is illiterate."
    ,"Ali tries to pair up with Bob in a death game. Bob, the attendee, suspects that Ali is illiterate."
    ]
pressure_not_i_criminal    = [ # Situations that includes an urgent reason why Ali should not be a criminal for Bob.
    ]
pressure_not_i_mild_yankee = [ # Situations that includes an urgent reason why Ali should not be a mild yankee for Bob.
    pressure_not_i_illiteracy
    ]
pressure_not_i_fat         = [ # Situations that includes an urgent reason why Ali should not be a fat for Bob.
     "Ali is looking for a date. Through the phone, Bob suspects that Ali is old." # Fat people are easily recognizable by their appearance, so the settings related to old requires frosted glass.
    ,pressure_not_i_unhealthy
    ]
pressure_not_i_old         = [ # Situations that includes an urgent reason why Ali should not be old for Bob.
     "Ali attempts to become an apprentice to an aging craftsman. Through the frosted glass, Bob suspects that Ali is old." # Old people are easily recognizable by their appearance, so the settings related to old requires frosted glass.
    ,"Ali is looking for a date. Through the phone, Bob suspects that Ali is old." # Old people are easily recognizable by their appearance, so the settings related to old requires frosted glass.
    ,pressure_not_i_unhealthy
    ]
pressure_not_i_poor        = [ # Situations that includes an urgent reason why Ali should not be poor for Bob.
     "Ali is looking for a date."
    ]
pressure_not_i_middle_aged = [ # Situations that includes an urgent reason why Ali should not be middle aged for Bob.
     "Ali is looking for a date. Through the phone, Bob suspects that Ali is old."
    ]
pressure_not_i_unfunny     = [ # Situations that includes an urgent reason why Ali should not be unfunny for Bob.
    ]
pressure_not_i_non_virgin  = [ # Situations that includes an urgent reason why Ali should not be virgin for Bob.
     "Ali tries to marry a Muslim. Bob suspects that Ali is old."
    ,"Ali tries to become a shrine maiden. Bob suspects that Ali is old."
    ]
pressure_not_i_nerd        = [ # Situations that includes an urgent reason why Ali should not be a nerd for Bob.
    ]

# Add new situations. Just mimic the existing items. Start answer with ```python. Each item should end with "suspects that Ali is"


###################################################################################################################################################################################################################################
# Below lists are for creating comedy situation.

pressure_not_s_unhealthy   = [ # Situations that includes an urgent reason why Ali should be unhealthy for Bob.
    ]
pressure_not_s_illiteracy  = [ # Situations that includes an urgent reason why Ali should be illiteracy for Bob.
    ]
pressure_not_s_criminal    = [ # Situations that includes an urgent reason why Ali should be a criminal for Bob.
    ]
pressure_not_s_mild_yankee = [ # Situations that includes an urgent reason why Ali should be a mild yankee for Bob.
    ]
pressure_not_s_fat         = [ # Situations that includes an urgent reason why Ali should be a fat for Bob.
    ]
pressure_not_s_old         = [ # Situations that includes an urgent reason why Ali should be old for Bob.
    ]
pressure_not_s_poor        = [ # Situations that includes an urgent reason why Ali should be poor for Bob.
    ]
pressure_not_s_middle_aged = [ # Situations that includes an urgent reason why Ali should be middle aged for Bob.
    ]
pressure_not_s_unfunny     = [ # Situations that includes an urgent reason why Ali should be unfunny for Bob.
    ]
pressure_not_s_non_virgin  = [ # Situations that includes an urgent reason why Ali should be virgin for Bob.
    ]
pressure_not_s_nerd        = [ # Situations that includes an urgent reason why Ali should be a nerd for Bob.
    ]
###################################################################################################################################################################################################################################
@dataclass
class Binary:
    visual:str # Can it be distinguished by appearance?
    illiteracy_or_smart:str

binary_unhealthy  =Binary("" , "" )
binary_illiteracy =Binary("" , "i")
binary_criminal   =Binary("" , "" )
binary_mild_yankee=Binary("" , "i")
binary_fat        =Binary("y", "" )
binary_old        =Binary("y", "" )
binary_poor       =Binary("" , "" )
binary_middle_aged=Binary("y", "" )
binary_unfunny    =Binary("" , "" )
binary_non_virgin =Binary("" , "" )
binary_nerd       =Binary("" , "s")

###################################################################################################################################################################################################################################
@dataclass
class Rev:
    ALL_REV: ClassVar[List['Rev']] = []
    reverse_adj_name: str
    habit_list      : list
    appear          : list
    tool            : list
    know            : list
    rephrase        : list
    pressure_not_i  : list
    pressure_not_s  : list
    binary          : Binary
    def __post_init__(self):
        Rev.ALL_REV.append(self)


rev_unhealthy   = Rev("unhealthy"   , habit_list_unhealthy   , appear_unhealthy    , tool_unhealthy   , know_unhealthy   , rephrase_unhealthy  , pressure_not_i_unhealthy  , pressure_not_s_unhealthy  , binary_unhealthy  )
rev_illiteracy  = Rev("illiteracy"  , habit_list_illiteracy  , appear_illiteracy   , tool_illiteracy  , know_illiteracy  , rephrase_illiteracy , pressure_not_i_illiteracy , pressure_not_s_illiteracy , binary_illiteracy )
rev_criminal    = Rev("criminal"    , habit_list_criminal    , appear_criminal     , tool_criminal    , know_criminal    , rephrase_criminal   , pressure_not_i_criminal   , pressure_not_s_criminal   , binary_criminal   )
rev_mild_yankee = Rev("mild_yankee" , habit_list_mild_yankee , appear_mild_yankee  , tool_mild_yankee , know_mild_yankee , rephrase_mild_yankee, pressure_not_i_mild_yankee, pressure_not_s_mild_yankee, binary_mild_yankee)
rev_fat         = Rev("fat"         , habit_list_fat         , appear_fat          , tool_fat         , know_fat         , rephrase_fat        , pressure_not_i_fat        , pressure_not_s_fat        , binary_fat        )
rev_old         = Rev("old"         , habit_list_old         , appear_old          , tool_old         , know_old         , rephrase_old        , pressure_not_i_old        , pressure_not_s_old        , binary_old        )
rev_poor        = Rev("poor"        , habit_list_poor        , appear_poor         , tool_poor        , know_poor        , rephrase_poor       , pressure_not_i_poor       , pressure_not_s_poor       , binary_poor       )
rev_middle_aged = Rev("middle_aged" , habit_list_middle_aged , appear_middle_aged  , tool_middle_aged , know_middle_aged , rephrase_middle_aged, pressure_not_i_middle_aged, pressure_not_s_middle_aged, binary_middle_aged)
rev_unfunny     = Rev("unfunny"     , habit_list_unfunny     , appear_unfunny      , tool_unfunny     , know_unfunny     , rephrase_unfunny    , pressure_not_i_unfunny    , pressure_not_s_unfunny    , binary_unfunny    )
rev_non_virgin  = Rev("non_virgin"  , habit_list_play_girl   , appear_non_virgin   , tool_non_virgin  , know_non_virgin  , rephrase_non_virgin , pressure_not_i_non_virgin , pressure_not_s_non_virgin , binary_non_virgin )
rev_nerd        = Rev("nerd"        , habit_list_nerd        , appear_nerd         , tool_nerd        , know_nerd        , rephrase_nerd       , pressure_not_i_nerd       , pressure_not_s_nerd       , binary_nerd       )


###################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################
'''


'''

Ali is very particular and poser.

 "Bob: Do you ride motorcycles? - Ali: Are big scooters motorcycles?" # motorbike lovers would not include a scooter in their 'motorcycle'.
,"Bob: Do you drink alcohol? - Ali: Is liqueur alcohol?" # alcohol lovers would not include liqueur in their 'alcohol'.
,"Bob: Do you play an instrument? - Ali: Are basses instruments?" # instrument lovers would not include a bass in their 'instrument'.
,"Bob: Are you a gamer? - Ali: Does playing Candy Crush make me a gamer?"

Add new 10 conversations







criminal_rephrase = []
criminal_monk_kick= ["Maffia"]
criminal_other    = []
criminal_pressure = []

reverse_adj_criminal=Reverse_adj("criminal", criminal_tool, criminal_know, criminal_rephrase, criminal_monk_kick, criminal_other, criminal_pressure)
###################################################################################################################################################################################################################################


fat_rephrase = ["calls french fries vegetable.","calls a whole cake a 'cake' and a shortcake a 'shortcake.'"]
fat_monk_kick= ["role of Kim Jong Un","Sumo wrestler"]
fat_other    = ["Ali was in the judo club when he was a student.","Ali is a catcher in baseball.","Ali is the drummer in a band.","Ali often wears aloha shirts.","Ali always takes the elevator, even for one floor."]
fat_pressure = ["Ali is trying to get into a lifeboat.", "Ali is looking for a date."]

reverse_adj_fat=Reverse_adj("fat", fat_tool, fat_know, fat_rephrase, fat_monk_kick, fat_other, fat_pressure)
###################################################################################################################################################################################################################################

unhealthy_rephrase  = []
unhealthy_monk_kick = []
unhealthy_other     = [
  "his insurance premiums went up recently."
, "hasn't been concerned about his health lately."
, "doesn't eat eggs these days because he finds them hard to digest."
, "has recently shifted his interest from conventional medicine to alternative medicine."
, "recently printed a funeral-sized photo of himself."
, "has recently been traveling to places he's always wanted to visit."
, "has been donating a lot to charity lately."
, "has been attending more religious or spiritual services."
, "has been more reflective and philosophical lately."
, "has been making peace with old adversaries."
, "has been updating his will."
, "has been preparing a list of his passwords and accounts for his family."
]
unhealthy_pressure = []

reverse_adj_unhealthy=Reverse_adj("unhealthy", unhealthy_tool, unhealthy_know, unhealthy_rephrase, unhealthy_monk_kick, unhealthy_other, unhealthy_pressure)
###################################################################################################################################################################################################################################
illiteracy_rephrase = ["calls Cashback Free", "calls Revolving payment Magic", "Revolving payment Discount"]
illiteracy_monk_kick= ["Nursing home"]
illiteracy_other    = []
illiteracy_pressure = []

reverse_adj_illiteracy=Reverse_adj("illiteracy", illiteracy_tool     ,illiteracy_know     ,illiteracy_rephrase ,illiteracy_monk_kick,illiteracy_other, illiteracy_pressure)

###################################################################################################################################################################################################################################
old_rephrase=["calls Vietnam War 'the other day.'", "calls Full Metal Jacket a slice of life movie.", "calls landline 'phone' and mobile phone 'mobile phone.'", "calls military airplane 'airplanes' and civilian airplane 'civilian planes'.", "calls mp3 'tape'", "calls 韓国 '朝鮮'.", "calls the TV a 'boob tube'.", "calls Russia 'Soviet'", "calls a film 'a moving picture.'" , "calls a radio 'a wireless.'" ]
old_monk_kick=[]
old_other=[  "has a Baby Boomer name.", "believes having his photograph taken takes away his soul.", "buys hard candies in bulk.", "wears socks with sandals.", "goes to bed at 7pm.", "can't figure out how to use a smartphone.", "thinks microwaves are dangerous.", "go to check on his rice fields during a typhoon.", "is being told by people around him to stop driving.", "tries to fix the TV by hitting it.", "search history on Bob's smartphone showed 'Accelerator brake which'", "has been afraid of flowers lately.", "s number of friends decreases regularly.", "didn't confuse the accelerator with the brake three times this year.", "surprised his family because he didn't drive the wrong way down the road.", "proposed to his wife three times this year.", "was surprised to realize that what he thought he had stepped on as the accelerator was the accelerator.", "was surprised to find that the person he thought was his wife was his wife.", "used to forget to close his zipper after urinating, but now he forgets to open it.", "used to forget to turn the lights off, but now he forgets to turn them on.", "used to forget to close the toilet seat, but now he forgets to open it.", "used to forget to set his alarm, but now he forgets to turn it off.", "used to forget to turn the TV off, but now he forgets to turn it on.", "used to forget to close the door, but now he forgets to open it.", "eats rolled eggs as medicine.", "drinks milk as medicine.", "smokes as a treatment for asthma.", "takes cod liver oil for joint pain.", "has some kind of chronic thing." , "has some kind of metastatic thing." , "finally got rid of his body odor recently.", "finally stopped arguing with the TV.", "finally stopped playing bingo every week.", "finally stopped complaining of pain.", "is afraid of flowers." , "is afraid of Vietnamese, Koreans, Japanese, and Russians." , "is afraid of snow." , "is afraid of small characters." , "is afraid of stairs" , "says the cushion is heavy.", "knows the pros and cons of each painkiller.", "has a favorite painkiller.", "still buys paper porn.", "refers to the Vietnam War as 'the other day.'", "thinks of Full Metal Jacket as a slice of life movie.", "Ali: I'm young so I'm fashion-conscious, I had a microwave before the boom.", "Ali: I'm young so I'm very into food trends. My favorite ethnic food is donuts.", "Ali: I'm young so I hate any music that's even slightly old. I think the Beatles are old-fashioned." , "Ali: I'm young so I like traveling abroad. I've been to Vietnam and Korea.", "Ali: I'm young so I'm tech-savvy, I can fix VHS players.", "Ali: I'm young so I'm a gamer, I'm good at Pac-Man.", "Ali: I'm young so I'm an environmentalist, I recycled cans for cash as a kid.", "Ali: I'm young so I'm into social media. I was on MySpace before the first boom.", "Ali: I'm young so I'm a music lover, I had a boombox in my room.", "Ali: I'm young so I like going out at night. I used to play outside until the streetlights came on."]
old_pressure=["Ali is looking for a date.", "Ali seeks to become an apprentice to an aging craftsman who is looking for a successor."]

reverse_adj_old = Reverse_adj("old", old_tool     , old_know     , old_rephrase , old_monk_kick, old_other, old_pressure)
###################################################################################################################################################################################################################################
poor_know     = ["Various discount systems", "How to apply for tax deduction", "Food bank locations, systems and hours","DIY home and car repair techniques","Public assistance program eligibility requirements", "How to use payday loans"]
poor_rephrase = ["calls tap water 'water' and drinking water 'drinking water'", "calls a bus 'car' and a car 'private car'", "calls a community collage 'collage' and a private collage 'private collage'"]
poor_monk_kick= []
poor_other    = ["is close in age to his parents.", "has many siblings.", "has weird name."]
poor_pressure = []

reverse_adj_poor=Reverse_adj("poor", poor_tool     ,poor_know     ,poor_rephrase ,poor_monk_kick,poor_other, poor_pressure)
###################################################################################################################################################################################################################################




middle_aged_know     = ["know"]
middle_aged_rephrase = ["rephrase"]
middle_aged_monk_kick= ["monk_kick"]
middle_aged_other    = [
  "has started appreciating a good night's sleep over a night out."
, "has been investing in a comfortable recliner."
, "calls all home game consoles Family Computers."
, "can tell to some extent how humid the day will be by the pain in his joints."
, "says potatoes are sweet."
, "has recently started taking the stairs instead of the escalator."
, "knows the difference between various types of wood." # Gemini
, "has started birdwatching as a hobby." # LLM
, "has been turning the air conditioner on 'low' lately."
, "has started going to bed earlier and waking up later." # LLM
, "has started volunteering for local community events." # LLM
, "has a membership to a local library." # LLM
, "is familiar with the joy of finding a comfortable pair of slippers." # LLM
, "knows a lot about how to save money on insurance premiums."
, "can only eat cake if he has the energy."
, "his bruises don't go away until two days later."
, "only talks to his friends about his knees and hips."
, "has a favorite brand of multivitamins." # GPT4
, "uses a calculator to do division."
, "likes to watch domestic tourist spots on TV that he'll never visit."
, "has a favorite brand of over-the-counter pain medication." # Claude
]
middle_aged_pressure = []

reverse_adj_middle_aged=Reverse_adj("middle_aged", middle_aged_tool     ,middle_aged_know     ,middle_aged_rephrase ,middle_aged_monk_kick,middle_aged_other, middle_aged_pressure)
###################################################################################################################################################################################################################################



unfunny_know     = ["know"]
unfunny_rephrase = ["rephrase"]
unfunny_monk_kick= ["monk_kick"]
unfunny_other    = [
  "Ali has started appreciating a good night's sleep over a night out."
, "Ali has been investing in a comfortable recliner."
, "Ali calls all home game consoles Family Computers."
, "Ali can tell to some extent how humid the day will be by the pain in his joints."
, "Ali says potatoes are sweet."
, "Ali has recently started taking the stairs instead of the escalator."
, "Ali knows the difference between various types of wood." # Gemini
, "Ali has started birdwatching as a hobby." # LLM
, "Ali has been turning the air conditioner on 'low' lately."
, "Ali has started going to bed earlier and waking up later." # LLM
, "Ali has started volunteering for local community events." # LLM
, "Ali has a membership to a local library." # LLM
, "Ali is familiar with the joy of finding a comfortable pair of slippers." # LLM
, "Ali knows a lot about how to save money on insurance premiums."
, "Ali can only eat cake if he has the energy."
, "Ali's bruises don't go away until two days later."
, "Ali only talks to his friends about his knees and hips."
, "Ali has a favorite brand of multivitamins." # GPT4
, "Ali uses a calculator to do division."
, "Ali likes to watch domestic tourist spots on TV that he'll never visit."
, "Ali has a favorite brand of over-the-counter pain medication." # Claude
]
unfunny_pressure = []

reverse_adj_unfunny=Reverse_adj("unfunny", unfunny_tool     ,unfunny_know     ,unfunny_rephrase ,unfunny_monk_kick,unfunny_other, unfunny_pressure)


###################################################################################################################################################################################################################################



mild_yankee_know=["Cost of lowering the car"]
mild_yankee_rephrase=["[浜崎あゆみ], [あゆ]"]
mild_yankee_monk_kick=[]
mild_yankee_other=[ # Extend 20 new characteristics of men with high school diplomas in Japanese, not English. No explanations. Start answer with ```python

 "板金屋の友達がいる"
,"リボ払いを利用している"
,"EXILEの今のメンバーを全員言える"
,"車高を下げている"
,"中古車販売店で働いている"
,"肩パンをする"
,"職場で怒られたくないからギリギリの暗さの茶髪をしている"
,"軽トラックを改造している"
,"ナンバープレートを傾けている"
,"サッカーのユニフォームをよく着ている"
,"ダーツバーに通っている"
,"シーシャを吸う"
,"マイナスイオンに金を出す"
,"Xの認証に金を出す"
,"Tinderのブーストに金を出す"
,"LINEスタンプに金を出す"
,"ゲーム『Fate/Grand Order』のガチャに金を出す"
,"ワンピースで泣く"
,"浜崎あゆみで泣く"
,"あの日見た花の名前を僕達はまだ知らない。で泣く"
,"進撃の巨人で泣く"
,"嵐のライブで泣く"
,"｢ワンピ｣と略す"
,"｢あゆ｣と略す"
,"｢プリ｣と略す"
,"｢ジャニ｣と略す"
,"ジャグラーを｢ジャグ｣と略す"
,"ワンピースで泣く"
,"浜崎あゆみで泣く"
,"Tiktokのコメント欄でよくケンカする"
,"カラオケで歌い手の曲を歌う"
,"ディズニーランドの年間パスポートを持っている"
,"原宿系ファッションが好き"
,"100均でメイク用品を買う"
,"LINEスタンプをたくさん持っている"

,"パワースポット巡りが好き"
,"Often get into fights in the TikTok comments section"
,"Cries at Taylor Swift"
,"Enjoys reality TV shows"
,"Follows fashion influencers on Instagram"
,"Has a collection of inspirational quotes"
,"Knows how to change a tire"
,"Follows a local sports team religiously"
,"Has a nickname from high school that stuck"
,"Drives a pickup truck"
,"Has strong opinions on cryptocurrency despite not owning any"
,"Has a friend who is a sheet metal worker"
,"Owns at least one piece of Confederate flag merchandise"
,"Wears sunglasses on the back of their head"
,"Has never left their home state"
,"Considers Walmart a cultural experience"
,"Wears camo to formal events"
,"Knows all the words to 'Sweet Home Alabama'"
,"Owns more than five pairs of cowboy boots"
,"Has a tattoo of their state's outline"
]
mild_yankee_pressure=[]

reverse_adj_mild_yankee=Reverse_adj("mild_yankee", mild_yankee_tool     ,mild_yankee_know     ,mild_yankee_rephrase ,mild_yankee_monk_kick,mild_yankee_other,mild_yankee_pressure)


# Extend 20 new items and respond only them. Start answer with ```python.

###################################################################################################################################################################################################################################




non_virgin_know      = ["How to play mahjong", ""]
non_virgin_rephrase  = []
non_virgin_monk_kick = []
non_virgin_other     = []
non_virgin_pressure  = ["Ali is looking for a date.", "Ali is trying to become a shrine maiden.", "Ali is trying to marry a Muslim."]

reverse_adj_non_virgin=Reverse_adj("non_virgin", non_virgin_tool     ,non_virgin_know     ,non_virgin_rephrase ,non_virgin_monk_kick,non_virgin_other,non_virgin_pressure)

###################################################################################################################################################################################################################################
wannabe_college_freshman_other=[# Extend 20 new characteristics of Cool college wannabes in English, not Japanese. No explanations. Start answer with ```python
 "シーシャを吸う"
,"酒に強い事が自慢になると思っている"
,"タバコを｢ヤニ｣と言う"
,"タバコを吸う事を｢ヤニを入れる｣と言う"
,"ミニマリストを目指す"
,"refers to their hobbies as 'just chilling'"
,"is called 'dude' or 'bro' by friends"
,"Wears a beret unironically"
,"Pretends to enjoy abstract art"
,"Carries around a Moleskine notebook they never write in"
,"Becomes vegan for a week and will shut up about it"
]
###################################################################################################################################################################################################################################
nerd_other=[# Extend 20 new characteristics of nerds in English, not Japanese. No explanations. Start answer with ```python
 "is proud of not crying when listening to Taylor Swift."
,"Uses a female protagonist in Pokémon"
,"can solve a Rubik's Cube in under a minute"
,"Has a favorite Dungeons & Dragons character"
,"Watches anime with subtitles"
]
###################################################################################################################################################################################################################################
def reverse_adj_tablize():
    for i in Reverse_adj.ALL_REVERSE_ADJ:
        col_name, col_tool, col_know, col_rephrase, col_monk_kick, col_other, col_pressure = [], [], [], [], [], [], []
        if i.name:col_name          .append(f"<table id='{i.name}'><tr><th colspan='2' id = 'th_orange'>{i.name}</th></tr>")
        if i.tool:col_tool          .append(f"<tr><th>Ali (has, is familiar with, has a favorite, finally stopped using, lost, can lend someone his, 逆に doesn't use)</th><td>{i.tool}</td></tr>")
        if i.know:col_know          .append(f"<tr><th>Ali grasps</th><td>{i.know}</td></tr>")
        if i.rephrase:col_rephrase  .append(f"<tr><th>Ali rephrases [0] as [1] on the right.</th><td>{i.rephrase}</td></tr>")
        if i.monk_kick:col_monk_kick.append(f"<tr><th>Ali was rejected by </th><td>{i.monk_kick}</td></tr>")
        if i.other:col_other        .append(f"<tr><th>Other</th><td>{i.other}</td></tr>")
        if i.pressure:col_pressure  .append(f"<tr><th>Pressure</th><td>{i.pressure}</td></tr>")
        reverse_adj_tablize_return=f"""
        {''.join(col_name     )}
        {''.join(col_tool     )}
        {''.join(col_know     )}
        {''.join(col_rephrase )}
        {''.join(col_monk_kick)}
        {''.join(col_other    )}
        {''.join(col_pressure)}
        </table>
        """
        tables_state_inst.append(reverse_adj_tablize_return)
reverse_adj_tablize()
###################################################################################################################################################################################################################################
###################################################################################################################################################################################################################################

@dataclass
class State:
    ALL_STATE: ClassVar[List['State']] = []
    state_name: str
    state_state: list

    def __post_init__(self):
      State.ALL_STATE.append(self)

tables_state_inst=[]



# bibiri


l_state_fat = [# print(*[f"comedy script : Everytime the woman hears {i}, she suspects that Ali is fat." for i in l_fat], sep="\n")
 "Ali was in the judo club when he was a student."
,"Ali is a catcher in baseball."
,"Ali is the drummer in a band."
,"Ali often wears aloha shirts."
,"Ali failed to lose weight and failed the audition for the role of Kim Jong Un."
,"Ali failed to lose weight and failed the audition to be a sumo wrestler."
,"Ali always takes the elevator, even for one floor." # Llama3
,"Ali's favorite exercise is playing darts."
,"Ali had to step away from the camera to have his driver's license photo taken."
,"After taking a bath, Ali dries his body with two bath towels."
,"Ali buys two tickets on the plane."
]# Add 10 new sentences that indilectly suggests that Ali is fat in l_fat in English without any explanations. Only output the sentences that you have newly added. Align white speaces and characters with the existing objects.

l_state_fat+=[# print(*[f"comedy script : Everytime the woman hears {i}, she suspects that Ali is fat." for i in l_fat], sep="\n")
 "Ali calls french fries a vegetable." # TypeCalls # Suggests that Ali feels guilty about eating French fries.
,"Ali calls a whole cake a 'cake' and a shortcake a 'shortcake.'" # TypeCalls # Suggests that Ali often eats a whole cake.
]# Add 10 new sentences that indilectly suggests that Ali is fat in l_fat in English without any explanations. Each items have to start with 'Ali calls' Only output the sentences that you have newly added. Align white speaces and characters with the existing objects. Use the existing type.

# Paid items for fat people. # Add new 10 items without any explanation. Only output the sentences that you have newly added. Align white speaces and characters with the existing objects.
# I use this list in detective stories to euphemistically suggest that a person is fat.
l_tool_fat = ["power wheel chair", "walker", "industrial-strenght scale", "loposuction"]

# Something that fat people grasps. # Add new 10 items without any explanation. Only output the sentences that you have newly added. Align white speaces and characters with the existing objects.
# I use this list in detective stories to euphemistically suggest that a person is fat.
l_grasp_fat = ["his blood sugar levels", "maximum weight capacity of elevators", "calorie count of the menues", "average weight limit of the chairs", "names of many arteries and veins", "Diet terms, such as low-impact exercise.", "BMI calculation formulas"]


l_state_fat += [f"Ali (knows the cost of, knows the best, finally stopped using, broke) {l_tool_fat}."]
l_state_fat += [f"Ali grasps {l_grasp_fat}."]

state_fat = State("fat", [l_state_fat])

###################################################################################################################################################################################################################################
# Instructions for teachers: Children who fit the following criteria are likely to require special care and should be consulted with the child welfare department regarding adjusting their program in accordance with procedure welfare-8.
# Instructions for LLM     : support_required_more_detailed list is used to identify students who need more support than usual due to reasons such as parental neglect or a lack of cultural or economic capital, and to notify the school's welfare department. Add new 10 items in English in support_required_more_detailed without any explanation. Please respond with only new items.
# Instructions for LLM     : support_required_more_detailed list should only include minor characteristics that even an experienced teacher would not identify as characteristic of a troubled child.

support_required_more_detailed_parents=[
  "His family is single-parent."
, "His family is a large family."
, "Parents' car has a marijuana-shaped air freshener."
, "There is a large age gap between the parents."
, "There is a large age gap between the parents and him."
, "Parents are smokers."
, "Don't have a curfew."
, "Even though he is poor, his home has a water server and many other home appliances."
, "their parents drive a low-stanced car."
, "Parents have an unusual number of pets."
, "Parents have an excessive number of tattoos or piercings."
, "Parents frequently change their appearance (hair color, style)."
, "Parents have a strong accent or unusual dialect."
, "Parents have a strong interest in alternative medicine or spirituality."
, "Parents have a foreign-sounding name or accent."
, "Parents often leave the child unsupervised at home."
, "Parents do not attend parent-teacher meetings."
, "Parents frequently argue in front of the child."
, "Parents have a history of frequent relocations."
, "Parents rely heavily on the child for household responsibilities."
, "Parents have limited social interactions with other parents."
, "Parents often forget to pack lunch for the child."
, "Parents rarely participate in school activities."
, "Parents don't read books or subscribe to newspapers."
, "The food in his house basically only tastes of seasoning."
, "parents have many stickers on their car."
, "Parents allow the child to stay up very late."
, "Parents drive a compact car."
, "Parents have a bumper sticker on their car that promotes a controversial political viewpoint."
]

l_state_bottom_family = support_required_more_detailed_parents

support_required_more_detailed_friend_home=[
  "Opening a friend's refrigerator without permission."
, "Often going to their friends' houses."
, "Going barefoot to a friend's house."
, "Stepping on a friend's pillow."
, "Borrowing a friend's pencil without asking."
, "Eating a friend's snack without permission."
, "Bringing a pet to a friend's house without permission."
, "He stays at a friend's house without contacting his parents, and his parents don't take any action."
, "Frequently asking friends for snacks."
, "Turning on a friend's TV or music without asking."
, "Leaving a friend's house without saying goodbye."
, "Staying at a friend's house until late at night."
, "Not using honorific language when speaking to a friend's parents."
]

l_state_bottom_in_friend_home = support_required_more_detailed_friend_home

support_required_more_detailed_home=[
  "Even though he is poor, his home has a water server and many other home appliances."
, "living in a one-room apartment"
, "living in a house with clayey walls"
, "The house is along the drain."
, "The house has a pit toilet."
, "The child does not have a designated study area."
, "There are no bookshelves or books in the house."
, "The home lacks adequate natural lighting."
, "The home is shared with extended family."
, "The house faces west."
]

l_state_bottom_home = support_required_more_detailed_home

support_required_more_detailed_knowledge=[ # characteristics related to knowledge
  "not knowing common games that children play together (such as tag or rock-paper-scissors)"
, "Having a wealth of sexual knowledge for his age."
, "Limited knowledge of popular children's songs or rhymes."
, "Limited knowledge of seasons or holidays."
]

l_state_bottom_knowledge = support_required_more_detailed_knowledge

support_required_more_detailed_hygine=[ # characteristics related to hygine or health
  "have a lot of silver teeth"
, "having badly aligned teeth."
, "Having yellow teeth."
, "having long nails"
, "Going barefoot to a friend's house."
, "Wearing the same clothes multiple days in a row."
, "Wearing Crocs all year round."
, "wearing mismatched socks"
]

l_state_bottom_hygine = support_required_more_detailed_hygine

support_required_more_detailed_food=[ # characteristics related to food
  "be a noisy eater."
, "Having many or no allergies."
, "Holding chopsticks strangely."
, "washing and reusing disposable chopsticks"
, "Eats very slowly or very quickly."
, "The contents of the lunch box are mostly frozen foods or carbohydrates."
, "frequently forgetting to bring a lunch"
, "Don't drink water."
, "Can't rotational eating"
, "Eat while standing or walking."
, "Listening to music during meals"
]

l_state_bottom_food = support_required_more_detailed_food


state_poor = State("poor", [l_state_bottom_family, l_state_bottom_in_friend_home, l_state_bottom_home, l_state_bottom_hygine, l_state_bottom_food])





###################################################################################################################################################################################################################################

#for i in l_state_middle_aged:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is middle aged, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_middle_aged = [# Extend new 10 statements that euphemistically, indirectly, allude to, or suggest that Bob is middle aged, in English. Start answer with ```python.

  "Ali has started appreciating a good night's sleep over a night out."
, "Ali has been investing in a comfortable recliner."
, "Ali calls all home game consoles Family Computers."
, "Ali can tell to some extent how humid the day will be by the pain in his joints."
, "Ali says potatoes are sweet."
, "Ali has recently started taking the stairs instead of the escalator."
, "Ali knows the difference between various types of wood." # Gemini
, "Ali has started birdwatching as a hobby." # LLM
, "Ali has been turning the air conditioner on 'low' lately."
, "Ali has started going to bed earlier and waking up later." # LLM
, "Ali has started volunteering for local community events." # LLM
, "Ali has a membership to a local library." # LLM
, "Ali is familiar with the joy of finding a comfortable pair of slippers." # LLM
, "Ali knows a lot about how to save money on insurance premiums."
, "Ali can only eat cake if he has the energy."
, "Ali's bruises don't go away until two days later."
, "Ali only talks to his friends about his knees and hips."
, "Ali has a favorite brand of multivitamins." # GPT4
, "Ali uses a calculator to do division."
, "Ali likes to watch domestic tourist spots on TV that he'll never visit."
, "Ali has a favorite brand of over-the-counter pain medication." # Claude
]

###################################################################################################################################################################################################################################
#for i in l_state_unhealthy:
#    print(f"Comedy script : {i} Hearing this, the insurance agent looks for an excuse to hang up on Bob.")

l_state_unhealthy = [# Extend new 10 statements that euphemistically, indirectly, allude to, or suggest that Bob will die soon, in English. Start answer with ```python.
  "Ali's insurance premiums went up recently."
, "Ali hasn't been concerned about his health lately."
, "Ali knows his blood pressure last month and this month."
, "Ali doesn't eat eggs these days because he finds them hard to digest."
, "Ali has recently shifted his interest from conventional medicine to alternative medicine."
, "Ali recently printed a funeral-sized photo of himself."
, "Ali has recently been traveling to places he's always wanted to visit."
, "Ali has been donating a lot to charity lately."
, "Ali has been attending more religious or spiritual services."
, "Ali has been more reflective and philosophical lately."
, "Ali has been making peace with old adversaries."
, "Ali has been updating his will."
, "Ali has been preparing a list of his passwords and accounts for his family."
, "Ali knows his daily calorie intake."
]

state_unhealthy = State("unhealthy", [l_state_unhealthy, l_state_middle_aged])


###################################################################################################################################################################################################################################


l_state_old=[]

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Use the existing types. Respond only with new statements. Respond only with new statements.
  "Ali refers to the Vietnam War as 'the other day.'"
, "Ali calls Full Metal Jacket a slice of life movie."
, "Ali says tires in the summer 'smell like napalm.'" # The fact that Bob knows the smell of napalm means he has been to Vietnam or Korea.
, "Ali calls West Side Story a movie for stupid kids."
, "Ali calls The Beatles a band for stupid kids."
, "Ali calls floppy disks 'new technology'."
, "Ali calls donuts an ethnic food."
, "Ali brags that he had a microwave before the microwave boom."
]
# , "Bob reminisces about how he used to go to drive-in movies with his high school sweetheart."

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Each item has to start with "I'm young so I". Respond only with new statements. Respond only with new statements.
  "Ali: I'm young so I'm fashion-conscious, I had a microwave before the boom." # This means that Bob was alive during the first microwave boom.
, "Ali: I'm young so I'm very into food trends. My favorite ethnic food is donuts." # This means that Bob lived at a time when doughnuts were still an ethnic food.
, "Ali: I'm young so I hate any music that's even slightly old. I think the Beatles are old-fashioned." # This means that Bob is of the Beatles generation.
, "Ali: I'm young so I like traveling abroad. I've been to Vietnam and Korea." # This means that Bob is a Vietnam and Korea veteran.
, "Ali: I'm young so I'm tech-savvy, I can fix VHS players." # Llama3
, "Ali: I'm young so I'm a gamer, I'm good at Pac-Man." # Llama3
, "Ali: I'm young so I'm an environmentalist, I recycled cans for cash as a kid." # Llama3
, "Ali: I'm young so I'm into social media. I was on MySpace before the first boom." # GPT4
, "Ali: I'm young so I'm a music lover, I had a boombox in my room." # GPT4
, "Ali: I'm young so I like going out at night. I used to play outside until the streetlights came on." # GPT
]
#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is an old with dementia, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old = [ # Add new 10 items in English. Use the existing types. Respond only with new statements.
  "Ali has a Baby Boomer name."
, "Ali believes having his photograph taken takes away his soul."
, "Ali buys hard candies in bulk."
, "Ali wears socks with sandals."
, "Ali goes to bed at 7pm."
, "Ali can't figure out how to use a smartphone."
, "Ali thinks microwaves are dangerous."
, "Ali go to check on his rice fields during a typhoon."
, "Ali is being told by people around him to stop driving."
, "Ali tries to fix the TV by hitting it."
, "Ali search history on Bob's smartphone showed 'Accelerator brake which'"
, "Ali has been afraid of flowers lately."
, "Ali's number of friends decreases regularly."
]

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is an old with dementia, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 statements that indirectly and implicitly imply that Bob is an old man. in English. Just mimic the existing syntaxes. Respond only with new statements.
  "Ali didn't confuse the accelerator with the brake three times this year."
, "Ali surprised his family because he didn't drive the wrong way down the road."
, "Ali proposed to his wife three times this year."
, "Ali was surprised to realize that what he thought he had stepped on as the accelerator was the accelerator."
, "Ali was surprised to find that the person he thought was his wife was his wife."
]

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 statements that indirectly and implicitly imply that Bob is an old man. in English. Respond only with new statements.
  "Ali used to forget to close his zipper after urinating, but now he forgets to open it."# This means that Bob is unaware that he has urinated in his pants.
, "Ali used to forget to turn the lights off, but now he forgets to turn them on."# This means that Bob does not realize that the room is dark.
, "Ali used to forget to close the toilet seat, but now he forgets to open it."# This means that Bob is unaware that he has urinated on his toilet cover.
, "Ali used to forget to set his alarm, but now he forgets to turn it off." # This means that Bob is unaware of the noisy alarm.
, "Ali used to forget to turn the TV off, but now he forgets to turn it on." # This means that Bob is looking at a blank screen.
, "Ali used to forget to close the door, but now he forgets to open it." # This means that Bob is standing in front of the door.
] # Each sentence ends with "it" or "on." Please imitate this properly.

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 statements that indirectly and implicitly imply that Bob is an old man. in English. You have to the syntax "Bob ~ as ~ ." Respond only with new statements. Respond only with new statements.
  "Ali eats rolled eggs as medicine." # TypeUseaasb
, "Ali drinks milk as medicine." # TypeUseaasb
, "Ali smokes as a treatment for asthma." # TypeUseaasb
, "Ali takes cod liver oil for joint pain." # TypeUseaasb
]

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Use the existing types. Respond only with new statements. Respond only with new statements.
  "Ali has some kind of chronic thing." # TypeSomekindof
, "Ali has some kind of metastatic thing." # TypeSomekindof
]

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Use the existing types. Respond only with new statements. Respond only with new statements.
  "Ali calls landline 'phone' and mobile phone 'mobile phone.'" # TypeCalls
, "Ali calls military airplane 'airplanes' and civilian airplane 'civilian planes'." # TypeCalls
, "Ali calls mp3 'tape'"# TypeCalls
, "Ali calls 韓国 '朝鮮'."# TypeCalls
, "Ali calls the TV a 'boob tube'."# TypeCalls
, "Ali calls Russia 'Soviet'"# TypeCalls
, "Ali calls a film 'a moving picture.'" # TypeCalls"
, "Ali calls a radio 'a wireless.'" # TypeCalls
]
####
#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Use the existing types. Respond only with new statements. Respond only with new statements.
# It's funny that an old person in the final stage stops doing things that an old person in the early stage starts doing as a way to cope with aging.
  "Ali finally got rid of his body odor recently." # TypeFinally. In the early stages of old age, people develop a strong body odor. But eventually stages of old age, people stop it. It's funny to Bob is in the eventually stage.
, "Ali finally stopped arguing with the TV." # TypeFinally
, "Ali finally stopped playing bingo every week." # TypeFinally
, "Ali finally stopped complaining of pain."
]
####
#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Use the existing types. Respond only with new statements. Respond only with new statements.
  "Ali is afraid of flowers." # TypeAfraid
, "Ali is afraid of Vietnamese, Koreans, Japanese, and Russians." # TypeAfraid
, "Ali is afraid of snow." # TypeAfraid
, "Ali is afraid of small characters." # TypeAfraid
, "Ali is afraid of stairs" # TypeAfraid
] # Calm down. You have to add something to l_state_old that scares old people.
# 0813 LLMは現状このタスクを理解できない。
####
#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[
  "Ali says the cushion is heavy."
, "Ali knows the pros and cons of each painkiller."
, "Ali has a favorite painkiller."
, "Ali still buys paper porn."
, "Ali refers to the Vietnam War as 'the other day.'"
, "Ali thinks of Full Metal Jacket as a slice of life movie."
]

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Use the existing types. Respond only with new statements. Respond only with new statements.
  "Ali refers to the Vietnam War as 'the other day.'"
, "Ali calls Full Metal Jacket a slice of life movie."
, "Ali says tires in the summer 'smell like napalm.'" # The fact that Bob knows the smell of napalm means he has been to Vietnam or Korea.
, "Ali calls West Side Story a movie for stupid kids."
, "Ali calls The Beatles a band for stupid kids."
, "Ali calls floppy disks 'new technology'."
, "Ali calls donuts an ethnic food."
, "Ali brags that he had a microwave before the microwave boom."
]
# , "Bob reminisces about how he used to go to drive-in movies with his high school sweetheart."

#for i in l_state_old:
#    print(f"Comedy script : {i} Hearing this, the woman suspects that Bob is old, and goes on Tinder to find an excuse to end the conversation with Bob.")
l_state_old+=[# Add new 10 items in English. Each item has to start with "I'm young so I". Respond only with new statements. Respond only with new statements.
  "Ali: I'm young so I'm fashion-conscious, I had a microwave before the boom." # This means that Bob was alive during the first microwave boom.
, "Ali: I'm young so I'm very into food trends. My favorite ethnic food is donuts." # This means that Bob lived at a time when doughnuts were still an ethnic food.
, "Ali: I'm young so I hate any music that's even slightly old. I think the Beatles are old-fashioned." # This means that Bob is of the Beatles generation.
, "Ali: I'm young so I like traveling abroad. I've been to Vietnam and Korea." # This means that Bob is a Vietnam and Korea veteran.
, "Ali: I'm young so I'm tech-savvy, I can fix VHS players." # Llama3
, "Ali: I'm young so I'm a gamer, I'm good at Pac-Man." # Llama3
, "Ali: I'm young so I'm an environmentalist, I recycled cans for cash as a kid." # Llama3
, "Ali: I'm young so I'm into social media. I was on MySpace before the first boom." # GPT4
, "Ali: I'm young so I'm a music lover, I had a boombox in my room." # GPT4
, "Ali: I'm young so I like going out at night. I used to play outside until the streetlights came on." # GPT4
]




# I use this list in detective stories to euphemistically suggest that a person is old.
# Paid items for old people. # Add new 10 items without any explanation. Only output the sentences that you have newly added. Align white speaces and characters with the existing objects.
l_tool_old = ["using a walker because he's back hurts.", "taking medicine because he feels unwell.", "using a hearing aid because he has hearing problems.", "using reading glasses because his eyes are bad.", "taking painkillers bacause he feels pain.", "using oxygen tanks due to respiratory problems"]

l_state_old += [f"Ali stopped {l_tool_old}."]

# Something that old people grasps. # Add new 10 items without any explanation. Only output the sentences that you have newly added. Align white speaces and characters with the existing objects.
# I use this list in detective stories to euphemistically suggest that a person is old.
l_grasp_old = ["if he has mental competency", "a few Vietnamese and Korean phrases.", "his internal age.", "some place names in Vietnam and Korea."]

l_state_old += [f"Ali grasps {l_grasp_old}."]

state_old = State("old", [l_state_old, l_state_middle_aged, l_state_unhealthy])
###################################################################################################################################################################################################################################

#for i in comedy_script_parts[random_number]:
#    print("Ali: I want to be a pediatrician.")
#    print(f"Bob: But I heard that you {i}. I'm nervous about hiring you. Don't work with children.")

comedy_script_parts=[
  "Ali Often trip to Southeast Asia such as Cambodia."
, "Ali Can speak Southeast Asian languages such as Cambodian."
, "Ali Be familiar with anime."
, "Ali Be familiar with tor browser, VPN, proxy and bitcoin."
, "Ali Owns the DVD of the movie Leon."
, "Ali Understand criminal laws and prison sentences."
, "Ali Always has toys and snacks what children like."
, "Ali Be knowledgeable about child actors."
, "Ali Owns a huge backpack and knows how many liters a child is."
, "Ali Owning a large car, especially one with a large trunk."
, "Ali Be knowledgeable about children's hobbies."
, "Ali Often reads parenting blogs."
, "Ali Often goes to public pools."
, "Ali Being or aspiring to be a pediatrician."
, "Ali Be passionate about volunteer activities related to children."
, "Ali Own a van with blacked out windows."
, "Ali Wear a checked polo shirt buttoned up to the top."
, "Ali Be familiar with Japanese subculture."
, "Ali Own an ice cream van."
, "Ali Owns a windowless van with a mattress in the back."
, "Ali have experience as a hospital clown."
, "Ali Know the correct way to destroy a hard disk drive."
, "Ali Know how to make balloon animals."
, "Ali Can do a perfect imitation of a children's TV character."
, "Ali Knows the names of every Paw Patrol character."
]# Add new 10 items in comedy_script_parts in English without any explanation. You need to think about what kind of characteristics the person has that their existing items show, and then suggest items that fit those characteristics.

l_state_pedophilia = comedy_script_parts


# Something that offender people grasps. # Add new 10 items without any explanation. Only output the sentences that you have newly added. Align white speaces and characters with the existing objects.
# I use this list in detective stories to euphemistically suggest that a person is an offender.
l_grasp_offender = ["the names of every Paw Patrol character.", "how to do a perfect imitation of a children's TV character.", "how to make balloon animals.", "the correct way to destroy a hard disk drive."
,"Japanese Anime", "Japanese language", "children's hobbies", "how to use VPN, proxy, Tor and Bitcoin", "Southeast asian languages", "popular online games for children",]

l_state_pedophilia += [f"Ali grasps {l_grasp_offender}"]



state_pedophilia = State("pedophilia", [l_state_pedophilia, l_state_criminal])
###################################################################################################################################################################################################################################

l_state_unlucky = [
  "Ali got divorced"
, "Ali had a traffic accident"
, "Ali got ill"
, "Ali got cheated on"
, "Ali had a house fire"
, "Ali got robbed"
]

state_unlucky = State("unlucky", [l_state_unlucky])
###################################################################################################################################################################################################################################



"""
for i in comedy_script_parts2[random_number]:
    print("Ali: I want to be a nuclear engineer.")
    print(f"Bob: But I heard that you {i}. I'm nervous about hiring you. Please do not work in highly technical jobs that involve risking people's lives.")
"""
comedy_script_parts2=[# Add new 10 sentences based on American culture in English. Respond only with new sentences.
  "Tiktokのコメント欄で頻繁に喧嘩をする。"
, "2週間オーストラリアに行った事を「留学」と呼ぶ。"
, "朝倉未来のファンまたはアンチである。"
, "パチンコを好んでいる。"
, "まだスノーボードの国母の話をしている。"
, "スカッとジャパンを録画して見ている。"
, "逆にクーポンを使わない。"
, "Twitterに金を払っている。"
, "広告ブロックを使っていない。"
, "辻希美について意見を持っている。"
, "M1グランプリの順位を自分なりに付ける。"
, "DHAのサプリを飲んでいる。"
, "西野亮廣のファンである。"
, "自販機のことを「自販」と略す。"
, "ワイドショーを実況する。"
, "Amazonを「密林」と略す。"
, "「サブスク疲れ」を訴えている。"# gemini
, "NFTに興味を持っている。" # gemini
, "ドラ泣きしている。"
, "「呑む」と表記する。"
, "都市圏に住んでいないのにスプリットタンにしている。"
, "低学歴なのにWakatte TVを見ている。"
, "貧乏人なのに竹中平蔵を好んでいる。"
, "四季が日本にしかないと思っている。"
, "声優を「下手な芸人より面白い」と言う。"
, "車に水曜どうでしょうのステッカーを貼っている。"
, "きらら漫画に金を払っている。"
, "「着丼」と言う。"
]

l_state_cultural_idiot = comedy_script_parts2

state_illiteracy = State("illiteracy", [l_state_bottom_family, l_state_bottom_in_friend_home, l_state_bottom_home, l_state_bottom_hygine, l_state_bottom_food, l_state_cultural_idiot])

###################################################################################################################################################################################################################################

#for i in state_unfunny:
#    print(f"Comedy script : 太郎: 私は芸人としてもうすぐ売れて金持ちになるので、今回のローン審査には受かると思っています。")
#    print(f"Comedy script : ローン審査者: 私は、貴方が{i}と聞きました。回収不能になると思うので、私は貴方にお金を貸せません。")
l_state_unfunny = [ # Add new 10 sentences. Respond with only new sentences.
  "若い女性に人気である"
, "ピン芸人である"
, "リズム芸をしている"
, "ネタ動画に'人を傷つけないお笑いだから好き'というコメントが多い"
, "ネタ動画に'見てるとほっこりする'というコメントが多い"
, "彼のファンがNONESTYLEのファンである事が多い"
, "憧れの芸人がNONESTYLEである"
, "松竹芸能に所属している"
, "早い段階でカジサックと絡んでいる。"
, "M1グランプリの結果に自分なりの点数をつけてTwitterに投稿する。"
, "ユウキロックから何かを学び取れると思っている。"
, "R1グランプリで優勝している。"
, "自分のファンに独自の総称をつけている。"
, "Twitterで愚痴を言わず、755で愚痴を言う。"
, "ウーマンラッシュアワー村本である。"
]

state_unfunny = State("unfunny", l_state_unfunny)

###################################################################################################################################################################################################################################
'''


