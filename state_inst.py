# /home/tarotoyota/state_inst.py
from dataclasses import dataclass
from typing import List, ClassVar

@dataclass
class State:
    ALL_STATE: ClassVar[List['State']] = []
    state_name: str
    state_state: list

    def __post_init__(self):
      State.ALL_STATE.append(self)

tables_state_inst=[]

###################################################################################################################################################################################################################################
# remove later
l_state_criminal=[]
state_criminal=State("test",[])

###################################################################################################################################################################################################################################
@dataclass
class Reverse_adj:
    ALL_REVERSE_ADJ: ClassVar[List['Reverse_adj']] = []
    name     : str
    tool     : list
    know     : list
    rephrase : list
    monk_kick: list
    other    : list
    def __post_init__(self):
        Reverse_adj.ALL_REVERSE_ADJ.append(self)
###################################################################################################################################################################################################################################

criminal_tool     = ["Shovel", "Balaclava", "Hammer (but he doesn't do DIY and doesn't know that a hammer is a tool)", "Metal bat (but he doesn't play baseball and doesn't know that a metal bat is a sporting item)", "Fireaxe (but he doesn't know that a fireaxe is a firefighting tool)", "Crowbar"]
criminal_know     = ["Many criminal laws and their sentences.", "Period until the statute of limitations runs out", "The intricacies of parole conditions", "Probation requirements","Fingerprinting procedures","Early release programs", "The workings of N system", "Average human volume in litres"]
criminal_rephrase = []
criminal_monk_kick= ["Maffia"]
criminal_other    = []

reverse_adj_criminal=Reverse_adj("criminal", criminal_tool, criminal_know, criminal_rephrase, criminal_monk_kick, criminal_other)
###################################################################################################################################################################################################################################


fat_tool     = ["power wheel chair", "walker", "industrial-strenght scale", "loposuction", "oxygen tanks for respiratory problems"]
fat_know     = ["his blood sugar levels", "maximum weight capacity of elevators", "his daily calorie intake.", "calorie count of the menues", "average weight limit of the chairs", "names of many arteries and veins", "Fast food nutritional information", "Diet terms, such as low-impact exercise.", "BMI calculation formulas"]
fat_rephrase = ["calls french fries vegetable.","calls a whole cake a 'cake' and a shortcake a 'shortcake.'"]
fat_monk_kick= ["role of Kim Jong Un","Sumo wrestler"]
fat_other    = ["Ali was in the judo club when he was a student.","Ali is a catcher in baseball.","Ali is the drummer in a band.","Ali often wears aloha shirts.","Ali always takes the elevator, even for one floor."]

reverse_adj_fat=Reverse_adj("fat", fat_tool, fat_know, fat_rephrase, fat_monk_kick, fat_other)
###################################################################################################################################################################################################################################

unhealthy_tool      = ["life insurance", "multivitamins", "diet soda", "stress ball"]
unhealthy_know      = ["Fast food nutritional information", "Side effects of popular medications", "his blood pressure last month and this month.", "his daily calorie intake."]
unhealthy_rephrase  = []
unhealthy_monk_kick = []
unhealthy_other     = [
  "Ali's insurance premiums went up recently."
, "Ali hasn't been concerned about his health lately."
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
]

reverse_adj_unhealthy=Reverse_adj("unhealthy", unhealthy_tool, unhealthy_know, unhealthy_rephrase, unhealthy_monk_kick, unhealthy_other)
###################################################################################################################################################################################################################################

illiteracy_tool     = ["lowered car","Hydrogen water", "Quantum healing bracelet", "Detox foot pads", "Miracle weight loss pills", "Energy alignment crystals", "Magnetic therapy insoles", "Negative ion clothing", "DNA repair supplements", "Anti-5G stickers", "Alkaline water ionizer", "Miracle mineral solution", "Colloidal silver", "Ear candles", "Homeopathic remedies", "Chakra balancing stones", "Aura cleansing spray", ]
illiteracy_know     = ["His IQ", "If he has the mental capacity to be held responsible"]
illiteracy_rephrase = ["calls Cashback Free", "calls Revolving payment Magic", "Revolving payment Discount"]
illiteracy_monk_kick= ["Nursing home"]
illiteracy_other    = []

reverse_adj_illiteracy=Reverse_adj("illiteracy", illiteracy_tool     ,illiteracy_know     ,illiteracy_rephrase ,illiteracy_monk_kick,illiteracy_other    )

###################################################################################################################################################################################################################################

old_tool = ["walker", "medicine", "hearing aid", "reading glasses", "painkillers", "oxygen tanks for respiratory problems", "cassette tape"]
old_know = ["A few words in Vietnamese and Korean", "The fragility of the M1 Garand", "how unrealistic Full Metal Jacket is"]
old_rephrase=["calls Vietnam War 'the other day.'", "calls Full Metal Jacket a slice of life movie.", "calls landline 'phone' and mobile phone 'mobile phone.'", "calls military airplane 'airplanes' and civilian airplane 'civilian planes'.", "calls mp3 'tape'", "calls 韓国 '朝鮮'.", "calls the TV a 'boob tube'.", "calls Russia 'Soviet'", "calls a film 'a moving picture.'" , "calls a radio 'a wireless.'" ]
old_monk_kick=[]
old_other=[  "has a Baby Boomer name.", "believes having his photograph taken takes away his soul.", "buys hard candies in bulk.", "wears socks with sandals.", "goes to bed at 7pm.", "can't figure out how to use a smartphone.", "thinks microwaves are dangerous.", "go to check on his rice fields during a typhoon.", "is being told by people around him to stop driving.", "tries to fix the TV by hitting it.", "search history on Bob's smartphone showed 'Accelerator brake which'", "has been afraid of flowers lately.", "s number of friends decreases regularly.", "didn't confuse the accelerator with the brake three times this year.", "surprised his family because he didn't drive the wrong way down the road.", "proposed to his wife three times this year.", "was surprised to realize that what he thought he had stepped on as the accelerator was the accelerator.", "was surprised to find that the person he thought was his wife was his wife.", "used to forget to close his zipper after urinating, but now he forgets to open it.", "used to forget to turn the lights off, but now he forgets to turn them on.", "used to forget to close the toilet seat, but now he forgets to open it.", "used to forget to set his alarm, but now he forgets to turn it off.", "used to forget to turn the TV off, but now he forgets to turn it on.", "used to forget to close the door, but now he forgets to open it.", "eats rolled eggs as medicine.", "drinks milk as medicine.", "smokes as a treatment for asthma.", "takes cod liver oil for joint pain.", "has some kind of chronic thing." , "has some kind of metastatic thing." , "finally got rid of his body odor recently.", "finally stopped arguing with the TV.", "finally stopped playing bingo every week.", "finally stopped complaining of pain.", "is afraid of flowers." , "is afraid of Vietnamese, Koreans, Japanese, and Russians." , "is afraid of snow." , "is afraid of small characters." , "is afraid of stairs" , "says the cushion is heavy.", "knows the pros and cons of each painkiller.", "has a favorite painkiller.", "still buys paper porn.", "refers to the Vietnam War as 'the other day.'", "thinks of Full Metal Jacket as a slice of life movie.", "Ali: I'm young so I'm fashion-conscious, I had a microwave before the boom.", "Ali: I'm young so I'm very into food trends. My favorite ethnic food is donuts.", "Ali: I'm young so I hate any music that's even slightly old. I think the Beatles are old-fashioned." , "Ali: I'm young so I like traveling abroad. I've been to Vietnam and Korea.", "Ali: I'm young so I'm tech-savvy, I can fix VHS players.", "Ali: I'm young so I'm a gamer, I'm good at Pac-Man.", "Ali: I'm young so I'm an environmentalist, I recycled cans for cash as a kid.", "Ali: I'm young so I'm into social media. I was on MySpace before the first boom.", "Ali: I'm young so I'm a music lover, I had a boombox in my room.", "Ali: I'm young so I like going out at night. I used to play outside until the streetlights came on."]

reverse_adj_old = Reverse_adj("old", old_tool     , old_know     , old_rephrase , old_monk_kick, old_other)
###################################################################################################################################################################################################################################
poor_tool     = ["Earthen wall", "Disposable chopsticks that have been washed and reused.", "A bento with brown side dishes overall", "Silver teeth", "One-story house", "House along a gutter", "tooth decay", "coupon"]
poor_know     = ["Various discount systems", "How to apply for tax deduction", "Food bank locations, systems and hours","DIY home and car repair techniques","Public assistance program eligibility requirements", "How to use payday loans"]
poor_rephrase = ["calls tap water 'water' and drinking water 'drinking water'", "calls a bus 'car' and a car 'private car'", "calls a community collage 'collage' and a private collage 'private collage'"]
poor_monk_kick= []
poor_other    = ["is close in age to his parents.", "has many siblings.", "has weird name."]

reverse_adj_poor=Reverse_adj("poor", poor_tool     ,poor_know     ,poor_rephrase ,poor_monk_kick,poor_other    )
###################################################################################################################################################################################################################################



middle_aged_tool     = ["tool"]
middle_aged_know     = ["know"]
middle_aged_rephrase = ["rephrase"]
middle_aged_monk_kick= ["monk_kick"]
middle_aged_other    = [
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

reverse_adj_middle_aged=Reverse_adj("middle_aged", middle_aged_tool     ,middle_aged_know     ,middle_aged_rephrase ,middle_aged_monk_kick,middle_aged_other    )
###################################################################################################################################################################################################################################


unfunny_tool     = ["tool"]
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

reverse_adj_unfunny=Reverse_adj("unfunny", unfunny_tool     ,unfunny_know     ,unfunny_rephrase ,unfunny_monk_kick,unfunny_other    )


###################################################################################################################################################################################################################################
# bibiri

###################################################################################################################################################################################################################################
def reverse_adj_tablize():
    for i in Reverse_adj.ALL_REVERSE_ADJ:
        col_name, col_tool, col_know, col_rephrase, col_monk_kick, col_other = [], [], [], [], [], []
        if i.name:col_name          .append(f"<table id='{i.name}'><tr><th colspan='2' id = 'th_orange'>{i.name}</th></tr>")
        if i.tool:col_tool          .append(f"<tr><th>Ali (has, is familiar with, has a favorite, finally stopped using, lost, can lend someone his, 逆に doesn't use)</th><td>{i.tool}</td></tr>")
        if i.know:col_know          .append(f"<tr><th>Ali grasps</th><td>{i.know}</td></tr>")
        if i.rephrase:col_rephrase  .append(f"<tr><th>Ali rephrases [0] as [1] on the right.</th><td>{i.rephrase}</td></tr>")
        if i.monk_kick:col_monk_kick.append(f"<tr><th>Ali was rejected by </th><td>{i.monk_kick}</td></tr>")
        if i.other:col_other        .append(f"<tr><th>Other</th><td>{i.other}</td></tr>")
        reverse_adj_tablize_return=f"""
        {''.join(col_name     )}
        {''.join(col_tool     )}
        {''.join(col_know     )}
        {''.join(col_rephrase )}
        {''.join(col_monk_kick)}
        {''.join(col_other    )}
        </table>
        """
        tables_state_inst.append(reverse_adj_tablize_return)
reverse_adj_tablize()
###################################################################################################################################################################################################################################





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

