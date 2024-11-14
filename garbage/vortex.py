from master_class_saraba_func_py import apply_color_styles_saraba


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

state_bottom_family = support_required_more_detailed_parents

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

state_bottom_in_friend_home = support_required_more_detailed_friend_home

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

state_bottom_home = support_required_more_detailed_home

support_required_more_detailed_knowledge=[ # characteristics related to knowledge
  "not knowing common games that children play together (such as tag or rock-paper-scissors)"
, "Having a wealth of sexual knowledge for his age."
, "Limited knowledge of popular children's songs or rhymes."
, "Limited knowledge of seasons or holidays."
]

state_bottom_knowledge = support_required_more_detailed_knowledge

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

state_bottom_hygine = support_required_more_detailed_hygine

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

state_bottom_food = support_required_more_detailed_food

state_poor = [
  "is a Mcjob worker"
, "works long hours"
, "driving an outdated car"
, "working multiple jobs"
, "be in debt"
, "washing and reusing disposable chopsticks"
, "have a lot of silver teeth"
]

state_illiteracy = [
  "be a high school graduate"
, "have a mickey mouse degree"
, "loves alternative medicines"
]

state_unlucky = [
  "got divorced"
, "had a traffic accident"
, "got ill"
, "got cheated on"
, "had a house fire"
, "got robbed"
]

state_unfunny = [
  "が若い女性に人気である"
, "がピン芸人である"
, "がリズム芸をしている"
, "のネタ動画に'人を傷つけないお笑いだから好き'というコメントが多い"
, "のネタ動画に'見てるとほっこりする'というコメントが多い"
, "のファンがNONESTYLEのファンである事が多い"
, "が松竹芸能に所属している"
]

state_old = [ # Add new 10 items in English.
  "has a Baby Boomer name."
, "calls 韓国 '朝鮮'."
, "eats rolled eggs as medicine."
, "believes having his photograph taken takes away his soul."
, "buys hard candies in bulk."
, "wears socks with sandals."
, "goes to bed at 7pm."
, "constantly forgets their reading glasses."
, "can't figure out how to use a smartphone."
, "thinks microwaves are dangerous."
, "calls the TV a 'boob tube'."
, "calls russia 'Soviet'"
, "go to check on his rice fields during a typhoon."
, "knows his internal age."
, "has some kind of chronic disease."
, "calls a landline a 'phone' and a mobile phone a 'mobile phone.'"
, "calls mp3 'tape'"
]

state_unhealthy = []

############################################################################################################################################################################
comedy_script_parts=[
  "Often trip to Southeast Asia such as Cambodia."
, "Can speak Southeast Asian languages such as Cambodian."
, "Be familiar with anime."
, "Be familiar with tor browser, VPN, proxy and bitcoin."
, "Owns the DVD of the movie Leon."
, "Understand criminal laws and prison sentences."
, "We always has toys and snacks to keep children happy."
, "Be knowledgeable about child actors."
, "Owns a huge backpack and knows how many liters a child is."
, "Owning a large car, especially one with a large trunk."
, "Be knowledgeable about children's hobbies."
, "Often reads parenting blogs."
, "Often goes to public pools."
, "Being or aspiring to be a pediatrician."
, "Be passionate about volunteer activities related to children."
, "Own a van with blacked out windows."
, "Wear a checked polo shirt buttoned up to the top."
, "Be familiar with Japanese subculture."
, "Own yours own ice cream van."
, "Owns a windowless van with a mattress in the back."
, "have experience as a hospital clown."
, "Know the correct way to destroy a hard disk drive."
]

"""
for i in comedy_script_parts[random_number]:
    print("Ali: I want to be a pediatrician.")
    print(f"Bob: But I heard that you {i}. I'm nervous about hiring you. Don't work with children.")
"""

# Add new 10 items in comedy_script_parts in English without any explanation. You need to think about what kind of characteristics the person has that their existing items show, and then suggest items that fit those characteristics.



state_pedophilia = comedy_script_parts
############################################################################################################################################################################

react = [
  "is disappointed with the product as a consumer" # shuts the door, hangs up
, "has him conceal that as a boss" # Stopping the camera during the commercial filming,
, "takes relief or delight in that as a competitor" # calls his boss to say, "It looks like it's going to be okay.", While doing market research on a competitor.
]

#############################################################################################################################################################################

def vortex_func():
    base=[]
    def table_maker(name, situation, item):
        table = f"""
        <table>
        <tr><th>name        </th><td> {name}        </td></tr>
        <tr><th>situation   </th><td> {situation}   </td></tr>
        <tr><th>item        </th><td> {item}        </td></tr>
        </table>
        """
        return table

    ##########
    situation_unhappy = [# Those lists are for creating comedy.
         "Bob guards spiritual energy site" # Bob guards spiritual energy site, but Ali suspects that he is unhappy. Then Ali loses faith in the spiritual energy site.
        ,"Bob lives near the spiritual energy site"
        ,"Bob manufactures spiritual energy goods"
        ,"Bob sales spiritual energy goods"
        ,"Bob cleans the spiritual energy site"
        ,"Bob writes about how to get happy"
        ,"Bob teaches spiritual energy practices"
        ,"Bob works as a counselor."
        ,"Bob offers reiki treatments"
        ,"Bob offers tarot card readings"
    ]

    item_unhappy=[
         "Bob is a Mcjob worker."
        ,"Bob got ill."
        ,"Bob lives in a trailer house."
    ]

    # f"{situation_unhappy[random_number]}, but Ali found that {item_unhappy[random_number]}. Then Ali loses faith in the item."

    # Add new 10 str objects in situation_unhappy in English without any explanation. Start answer with ```python . Align the white spaces and the characters with exist objects.

    table_unhappy = table_maker("unhappy", situation_unhappy, state_unlucky + state_poor + state_bottom_home + state_bottom_hygine + state_illiteracy)
    base.append(table_unhappy)
    ##########
    situation_unhealthy = [# Those lists are for creating comedy.
         "Bob offers alternative medicines"
        ,"Bob offers reiki treatments"
    ]

    item_unhealthy = [
         "Bob got ill."
        ,"Bob's insurance is expensive."
    ]

    # f"{situation_unhealthy[random_number]}, but Ali found that {item_unhealthy[random_number]}. Then Ali loses faith in the item."

    # Add new 10 str objects in situation_unhealthy in English without any explanation. Start answer with ```python . Align the white spaces and the characters with exist objects.

    table_unhealthy = table_maker("unhealthy", situation_unhealthy, state_unhealthy + state_bottom_hygine)
    base.append(table_unhealthy)

    ##########
    situation_illiteracy = [# Those lists are for creating comedy.
         "Bob tries to sale nootropics"
        ,"Bob customer reviews nootropics"
        ,"Bob writes about intelligence improvement"
        ,"Bob was raised by a educational researcher"
        ,"Bob offers online courses on speed reading"
    ]

    item_illiteracy = [
         "Bob's final education is a high school graduate."
        ,"Bob likes alternative medicine."
    ]

    # f"{situation_illiteracy[random_number]}, but Ali found that {item_illiteracy[random_number]}. Then Ali loses faith in the item."

    # Add new 10 str objects in situation_illiteracy in English without any explanation. Start answer with ```python . Align the white spaces and the characters with exist objects.

    table_illiteracy = table_maker("illiteracy", situation_illiteracy, state_illiteracy + state_bottom_family + state_bottom_home + state_bottom_hygine + state_bottom_food + state_poor)
    base.append(table_illiteracy)

    ##########
    situation_old = [# Those lists are for creating comedy.
         "Bob tries to becoemes an apprentice to an elderly potter in an attempt to prevent the art from being lost" # If you're looking for a young apprentice and an old man shows up you get mad.
        ,"Bob tries dating Ali on a dating app" # If you're looking for a date and an old man shows up you get mad.
        ,"Bob volunteers to fill in for an unexpected vacancy on Ali's sports team" # If you're looking for a pinch hitter and an old man shows up you get mad.
        ,"Bob volunteers to be Ali's partner in a youth tennis tournament" # If you're looking for a young tennis partner and an old man shows up you get mad.
    ]

    item_old = [
         "Bob calls the TV a 'boob tube'."
        ,"Bob goes to bed at 7pm."
    ]
    # f"{situation_old[random_number]}, but Ali found that {item_old[random_number]}. Then Ali suspects that Bob is an old, and gets angry that Bob is an old."

    # Add new 10 str objects in situation_old in English without any explanation. Start answer with ```python . Align the white spaces and the characters with exist objects.

    table_old = table_maker("old", situation_old, state_old)
    base.append(table_old)
    ##########
    situation_pedophilia = [
         "Bob tries to be a teacher"
        ,"Bob tries to be a pediatrician"
        ,"Bob offers to tutor children after school"
        ,"Bob signs up to be a scout leader"
        ,"Bob tries to be a foster parent"
    ]

    item_pedophilia = [
         "Bob travels frequently to Southeast Asia."
        ,"Bob is knowledgeable about bitcoin payments and VPNs."
    ]

    # f"{situation_pedophilia[random_number]}, but Ali found that {item_pedophilia[random_number]}. Then Ali suspects that Bob is an old, and gets angry that Bob is an old."

    # Add new 10 str objects in situation_pedophilia in English without any explanation. Start answer with ```python . Align the white spaces and the characters with exist objects.

    table_pedophilia = table_maker("pedophilia", situation_pedophilia, state_pedophilia)
    base.append(table_pedophilia)
    ##########

    situation_unfunny = [
         ["is a comedian who believes he can't get hired the part-time because of the potential for instant success in comedy."] # Bob is a comedian who believes he can't get hired the part-time because of the potential for instant success in comedy, but Ali suspects that he he is unfunny.
    ]

    # Task1 = "add new 10 items in situation_old in English without any explanation."

    table_unfunny = table_maker("unfunny", situation_unfunny, state_unfunny)
    base.append(table_unfunny)

    return apply_color_styles_saraba('<br>'.join(map(str, base)))




