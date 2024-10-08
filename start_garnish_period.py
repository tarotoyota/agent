#/home/tarotoyota/start_garnish_period.py
import agent_output
from agent_output import coloring
from dataclasses import dataclass, field
from typing import List, ClassVar, Dict, Union
tables=[] # all tables will be appended here.

def tablize(name, tag, usage_ex, item):
    table = f"""
    <table>
    <tr><th colspan= "2" id="th_lime"> {name}                        </th></tr>
    <tr><th>TAG         </th><td> {tag}                 </td></tr>
    <tr><th>USAGE EX.   </th><td> {usage_ex}            </td></tr>
    <tr><th>ITEM        </th><td> {'<br>'.join(item)}   </td></tr>
    </table>
    """
    return table

######################################################################################

@dataclass
class Garnish:
    ALL_GARNISH: ClassVar[List['Garnish']] = []

    name:str
    tag:str
    template:list
    exam: List[List[str]] = field(default_factory=list)# デフォルト値を取るattrが取らないそれより先にあってはならない
    trigger:str = ""
    special: Dict[str, List[str]] = field(default_factory=dict)
    def __post_init__(self):
        Garnish.ALL_GARNISH.append(self)
    @staticmethod
    def garnish_table():
        garnish_table_result = ""

        for i in Garnish.ALL_GARNISH:
            exam_rows = ""
            exam_col = ""
            special_rows = ""
            trigger_col = ""

            if i.exam:
                exam_col = "<tr><th>USER</th><th>SKETCH NAME</th><th>EXPRESSION</th></tr>"
                for j in i.exam:
                    exam_rows += f"<tr><td>{j[0]}</td><td>{j[1]}</td><td>{j[2]}</td></tr>"
            if i.special:
                for key, value in i.special.items():
                    special_rows += f"<tr><th>{key}</th><td colspan='2'>{', '.join(value)}</td></tr>"
            if i.trigger:
                trigger_col = f"<tr><th>TRIGGER</th><td>{i.trigger}</td></tr>"


            garnish_table_result+=f"""
            <table id="{i.name}">
            <tr><th id="th_lime" colspan="3">{i.name}</th></tr>
            <tr><th>TAG</th><td colspan="2">{i.tag}</td></tr>
            <tr><th>TEMPLATE</th><td colspan="2">{i.template}</td></tr>
            {trigger_col}
            {exam_col}
            {exam_rows}
            {special_rows}
            </table>
            """

        return garnish_table_result

remembered = Garnish(
    name="remembered"
    ,tag="JOKE_TLM"
    ,exam=[["セルライトスパ", "報道インタビュー", "神隠しだ"], ["キングオブコメディ", "自動車教習所", "思い出した　井ノ原快彦だ"], ["シソンヌ", "職員室", "清水の両親シンセ奏者"]]
    ,template=["Ali can't remember {x} -(lag)-> Ali: Remembered, it's {x}."]
    )
zona=Garnish(
    name="zona"
    ,tag="JOKE_TLM"
    ,exam=[["セルライトスパ", "報道インタビュー", "ぞな？"], ["フランスピアノ", "クレーマー", "お馴染みじゃないの？"]]
    ,template=["Ali says {strange_expression} -> Ali's closed persons don't know the {strange_expression}."]
    )
one_sided=Garnish(
    name="one_sided"
    ,tag="AtoB"
    ,template=["Ali: {{one_sided_0}} - Bob: I agree. Thanks to you.", "Ali: {{one_sided_1}} - Bob: I agree. Thanks to you."]
    ,trigger="The assigned b3scene must be some kind of competition or battle."
    ,special = {
        "one_sided_0" : ["It will be one-sided", "The gap will continue to widen", "The balance of power was upset", "The winner and loser are now decided", "This match is already over", "It's not even going to be close", "It's going to be a landslide win"]# A strong man has joined the team. The strong man says to his teammate:# Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
        ,"one_sided_1" : ["Can we keep this gap?", "Are we safe with this advantage?", "Should we play defensively now?", "How long can we maintain this lead?"]# A strong man has joined the team. The teammate says to the strong man:# Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
        }
    )
understand_why=Garnish( # sad_pastと統合？？？？？
    name="understand_why"
    ,tag="AtoB, BtoA, JOKELESS_TLM"
    ,template=["Ali's {{understand_why_0}}. -(lag)-> Bob is annoyed by Ali and says: Now I understand why your {{understand_why_0}}.", "Bob's {{understand_why_0}}. -(lag)-> Ali is annoyed by Bob and says: Now I understand why your {{understand_why_0}}."]
    ,special = {
        "understand_why_0(0)" : [ # script = f"If a {x}, then at first glance it may seem harmless or positive, but it may be a sign that the child is under stress." # Append 5 new items in stress_make in English, not Japanese. Respond only the 5 items. I'll run your response through the eval function so please do not include unnecessary characters in your response.
             "child is trying to become a counselor"
            ,"child is short"
            ,"child became independent so early"
            ,"child often stay at school late"
            ,"child is interested in politics"
            ,"child is interested in trains"
            ,"child likes animals more than people"
            ,"child loves volunteering"
            ,"child doesn't cry at all"
            ,"child is extremely strict about rules"
            ,"child often plays with younger children"
            ,"child never had a rebellious phase"
            ,"child is an avid reader beyond their years"
            ,"child is obsessed with cleanliness"
            ,"child is overly mature for their age"
            ,"child has an unusually strong sense of justice"
            ,"child is always eager to help others"
            ,"child is excessively quiet"
            ,"child is obsessed with cleanliness"
            ]
        }
    )



tables.append(coloring(Garnish.garnish_table()))


######################################################################################

stress_make=[ # delete later
 "child is trying to become a counselor"
,"child is short"
,"child became independent so early"
,"child is interested in politics"
,"child is interested in trains"
,"child likes animals more than people"
,"child loves volunteering"
,"child doesn't cry at all"
,"child is extremely strict about rules"
,"child often plays with younger children"
,"child never had a rebellious phase"
,"child is an avid reader beyond their years"
,"child is obsessed with cleanliness"
,"child is overly mature for their age"
,"child has an unusually strong sense of justice"
,"child is always eager to help others"
 "child speaks in third person"
,"child insists on wearing a helmet indoors"
,"child collects rocks and calls them their 'pets'"
,"child is obsessed with even numbers"
,"child only eats foods that start with the letter 'P'"
]



###################################################################################################
# 20240919 10:04

@dataclass
class Reason:
    ALL_REASON: ClassVar[List['Reason']] = []
    reason_name:str
    reason_item:list
    def __post_init__(self):
        Reason.ALL_REASON.append(self)
    @classmethod
    def reason_table(cls):
        col=[]
        reason_once = ["I have built a relationship of trust with you.", "I feel like talking about it."]
        for i in cls.ALL_REASON:
            col.append(f"<tr><td>{i.reason_name}</td><td>{i.reason_item}</td></tr>")
        table_reason=f"""
        <table id="reason">
        <tr><th colspan="2" id="th_lime">reason                                      </th></tr>
        <tr><th>Tag                 </th><td>AtoB, Time Lag Mentionable </td></tr>
        <tr><th rowspan="2">f       </th><td>Ali: I'll tell you the reason for {{reason_name}} {{reason_once}}. -(lag)> Ali: {{reason_item}} -> Bob: Why now?                       </th></tr>
                                         <td>Bob: What is the reason for {{other_phenomenon_x}}? -> Ali: {{reason_item}} -> Bob: I didn't ask the reason for the {{reason_name}}.   </th></tr>
        <tr><th>reason_name         </th><th>reason_item                </th></tr>
        {", ".join(col)}
        <tr><th colspan="2">reason_once                                 </th></tr>
        <tr><td colspan="2">{reason_once}                               </td></tr>

        </table>"""
        return table_reason

reason_divorce = Reason("divorce", ["The reason is that I stole my wife's stepchild's pants."])

tables.append(coloring(Reason.reason_table()))

######################################################################################


######################################################################################

# 元取るために六回焼香した

# ノミにも感情あるんだ


# Inevitability of disclosure(発言必然性)
#  自慢 : Envy? I bought this last week. It was expensive.
#  命令 : I have to try not to get it dirty. I bought this last week. It was expensive.

# Bottom
#                   reveal                      dont
#  part time worker {part_time_worker.reveal}   {part_time_worker.dont}


# Bottom dont
# Sad_past dont
# Stereo dont
# Pressure dont


# 今は養育費だけで生活してます
# 昨日入れたんだ 40歳になってタトゥー入れたん？


# できねーだろ
#  養育費でタトゥー入れる奴
#   爆弾解除
#   世界変えれねーだろ

'''
@dataclass # Define 5 new BinaryLagMention instance without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python. For each instance you create, please include a comment stating which existing instance it is modeled after.
class BinaryLagMention:
    ALL_BINARYLAGMENTION: ClassVar[List['BinaryLagMention']] = []
    fact1:str
    fact1_jokenized:str
    fact2:str
    fact2_jokenized:str
    lagmention:str
    def __post_init__(self):
        BinaryLagMention.ALL_BINARYLAGMENTION.append(self)
        for i in BinaryLagMention.ALL_BINARYLAGMENTION:
            print(f"""<table>
            <tr><th>fact1</th><td>{self.fact1}</td></tr>
            <tr><th>fact1_jokenized</th><td>{self.fact1_jokenized}</td></tr>
            <tr><th>fact2</th><td>{self.fact2}</td></tr>
            <tr><th>fact2_jokenized</th><td>{self.fact2_jokenized}</td></tr>
            <tr><th>lagmention</th><td>{self.lagmention}</td></tr>
            </table>""")

tattoo=BinaryLagMention(
      "Ali got a tattoo."               , "Ali got a tattoo after he turned 40. It's lame to aspire to punk when you're older."
    , "Ali receives child support."     , "Ali says: I feel like the child support money I withdrew from the ATM is smelly."
    , "Did you get a tattoo with child support money?"
    )

picking_up=(
      "Ali is picking up college students on Tiktok."   , "Ali says: The easiest one is the women who comment on conspiracy theory videos."
    , "Ali's wife died last week."                      , "Ali says: How long must pass since my wife's death before I can take my ring off?"
    , "Did you start picking up girls on Tiktok right after your wife died?"
    )

call_girl=BinaryLagMention(
      "Ali called a call girl to his house."    , "Ali told the call girl about his dream. Ali says: But she made fun of my dream, so I told her, 'What does a call girl know?' and sent her away."
    , "Ali lives at his at his parents' home."  , "Ali still lives at his parents' home despite being middle-aged."
    , "Did you call a call girl to your parents' house?"
    )

parents_home=BinaryLagMention(
      "Ali lives in a one-room apartment."      , "Ali lives in a one-room apartment despite being middle-aged."
    , "Ali lives at his at his parents' home."  , "Ali still lives at his parents' home despite being middle-aged."
    , "Is your parents' home a one-room apartment?"
    )

car_sex=BinaryLagMention(
      "Ali had sex in his car." , "Ali had sex in a car the day before her son's entrance exam."
    , "Ali only owns a moped."  , "Despite being middle-aged, Ali only owns a moped."
    , "Did you have sex in a moped?"
    )

'''




list_dirty_money = ["child support money", "unemployment benefits", "life insurance proceeds", "welfare money", "divorce alimony", "grandma's pension"]

dirty_money_accept=[ # In a sitcom. The lines Ali says when he accepts tainted money. Extend 10 new lines in this list in English, not Japanese. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python. Only use child support money, unemployment benefits, life insurance proceeds, welfare money, divorce alimony and grandma's pension. The existing lines below are correct, so you have to mimic them.
  "child support money      </th><td>I feel like the child support money I withdrew from the ATM is smelly." # TypeFeelLike
, "divorce alimony          </th><td>Benjamin Franklin of divorce alimony money is not smiling as much as usual." # TypeFeelLike
, "unemployment benefits    </th><td>The meals I order with my unemployment insurance money seem to be larger than usual." # TypeFeelLike
, "unemployment benefits    </th><td>Any movie is fun when watched on unemployment benefits." # TypeFeelLike
, "life insurance proceeds  </th><td>I feel like the stocks I invest in with life insurance proceeds are more volatile." # TypeFeelLike
, "unemployment benefits    </th><td>I feel like the champagne I buy with unemployment benefits more bubbles." # TypeFeelLike
, "child support money      </th><td>I feel like the toys I buy with child support money break faster." # TypeFeelLike
, "child support money      </th><td>The ice cream I buy with child support money melts faster than usual." # TypeFeelLike
, "life insurance proceeds  </th><td>The garden I planted with life insurance proceeds seems to grow unnaturally fast." # TypeFeelLike
, "child support money      </th><td>The clothes I buy with child support money feel tighter." # TypeFeelLike
]

dirty_money_accept+=[ # In a sitcom. The lines Ali says when he accepts tainted money. Extend 10 new lines in this list in English, not Japanese. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python. Only use child support money, unemployment benefits, life insurance proceeds, divorce alimony and grandma's pension. The existing lines below are correct, so you have to mimic them.
  "life insurance proceeds  </th><td>I wonder how my face look when I pay my mother's life insurance premiums with my father's life insurance proceeds." # TypeHowLook
, "child support money      </th><td>What kind of face should I make when buying condoms with my child support money?" # TypeHowLook
, "divorce alimony          </th><td>I wonder how my face looks when I'm buying engagement rings with my divorce alimony." # TypeHowLook
, "grandma's pension        </th><td>I wonder how my face looks when I'm tipping with grandma's pension." # TypeHowLook
, "grandma's pension        </th><td>How should my face look when I'm purchasing anti-aging cream with grandma's pension money?" # TypeHowLook
, "grandma's pension        </th><td>What's the correct facial expression to use when doing tricks on a skateboard bought with child support money?" # TypeContrast
]

dirty_money_accept+=[ # In a sitcom. The lines Ali says when he accepts tainted money. Extend 10 new lines in this list in English, not Japanese. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python. Only use child support money, unemployment benefits, life insurance proceeds, divorce alimony and grandma's pension. The existing lines below are correct, so you have to mimic them.
  "grandma's pension        </th><td>I can concentrate more than usual when playing blackjack using my grandmother's pension." # TypeThanUsual
, "life insurance proceeds  </th><td>When I play gambling chess using my grandmother's life insurance money, I tend to attack earlier than usual." # TypeThanUsual
]

dirty_money_accept+=[ # In a sitcom. The lines Ali says when he accepts tainted money. Extend 10 new lines in this list in English, not Japanese. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python. Only use child support money, unemployment benefits, life insurance proceeds, divorce alimony and grandma's pension. The existing lines below are correct, so you have to mimic them.
  "divorce alimony          </th><td>Please stay with me. I'll boosting Tinder with divorce alimony from my ex-wife now." # TypeContrast
, "unemployment benefits    </th><td>Yesterday I bought a crown avatar with my unemployment benefits." # TypeContrast
]

dirty_money_accept+=[ # In a sitcom. The lines Ali says when he accepts tainted money. Extend 10 new lines in this list in English, not Japanese. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python. Only use child support money, unemployment benefits, life insurance proceeds, divorce alimony and grandma's pension. The existing lines below are correct, so you have to mimic them.
  "child support money      </th><td>The gum I buy to break the child support bill is accumulating on my dashboard." # TypeOther
]

col_dirty_money=[]
for i in dirty_money_accept:
    col_dirty_money.append(f"<tr><th>{i}</td></tr>")

table_dirty_money=f"""<table>
<tr><th colspan="2">table_dirty_money</th></tr>
<tr><th>dirty_money</th><th>Ali says</th></tr>
{", ".join(col_dirty_money)}
</table>
"""

tables.append(table_dirty_money)


assign_neet_dirty_money = [
      "I'm working at {neet} on the side."
    , "I have to hurry because I have the night shift at {neet} tomorrow."
    , "Enviable? I just bought it because I got the {dirty_money} yesterday."
    ]

assign_neet_part_time_job_worker=[
     "Do you envy me? I splurged on it with my part-time job money."
    ,"I have to hurry because I have the night shift at {neet} tomorrow."
    ]







"""<table>
<tr><th>Assignment of list_neet or list_dirty_money to Ali</th><td>{assign_neet_dirty_money}</td></tr>



"""




"""

**Switch, Bulb, Activation, Turning on
When the fact that Ali is a NEET is presented, fline_neet, fline_desura, and fline_dirty_money will be activated.
This is expressed as, "the fact is the switch for the three flines," "the three flines are the bulb for the fact," and "turning on the fact activates the three flines."




"""

# いじらめられてた理由がわかる
# フランスピアノ: クレーマー, セルライトスパ: ぞな お馴染みじゃないんだ
#




lame_40=[# Things that are lame to start when you're 40
  "Ali got his first tattoo at age 40."
, "Ali start smoking"
    ]


'''

40になってからやるとダサい事=[]
養育費のような汚れた金=[]

<th> action1    </th><td>40になってからやるとダサい事
<th> money1     </th><td>養育費のような汚れた金
<th> lagmention </th><td> 貴方はmoney1でaction1したのですか？
'''
# "Have you become bad-tempered because of mafia movies?"



# 娘癌なのにパチンコ来たん？





###################################################################################################
###################################################################################################
# for i in list_a:
#   print(f"comedy script : It doesn't suit you. Your current state is like {i}")

list_a = [ # Extend 10 new items to list_a in English, not Japanese. I will run your reply through the eval function so don't include any unnecessary characters in your reply. Start answer with ```python. Don't make up neologisms.
 "an ugly woman wearing a ribbon"
,"a runt is muscular"
,"a runt wearing a streetwear"
]
###################################################################################################
# icause    : icause_adhd, icause_milk
# isympton  : isympton




megezu=[
 "{hypo_i}になってもめげず"
,"{hypo_i}から立ち直る"
,"{hypo_i}から更生する"
,"{hypo_i}を克服する"
]




# Disclosing one's ADHD even though no one is interested.
# レストラン始めようかな - もうスランプ入ってる


# さらば青春の光型 sBiA, sCiAnB型
# サスペンダーズ型 sAiB, sCiBnA型


###################################################################################################
crime_report_vocabulary=["手口",  "犯行", "身柄", "自供", "否認", "常習", "余罪", "再犯", "前科", "共犯", "初犯"]

crime_report_vocabulary_verb=["に手を染める", "という被害", "に漬け込み", "した疑い", "した容疑", "金銭目的で", "営利目的で",]


#Extend 10 new words. start answer with ```python. I'll run your response with eval function, so don't include unnecessary characters in your response.
###################################################################################################

# アフリカの人々が飢えている横で
# どんな気持ちで土建屋とか見てる
#四捨五入したら泥棒


###################################################################################################
# [print(f"Ali: Am I weird? I {i}. - Bob: I don't think your abnormality is caused only by the fact that you {i}.", f"Ali: Am I weird? I {i}. - Bob: I don't think your abnormality is related to the fact that you {i}.") for i in icause_adhd]
# icause_adhd are lines that Ali, a madman, says in a sitcom to justify his abnormality. Extend 10 new items. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.

icause_adhd=[
 "have ADHD"
,"be a returnee"
,"grew up on an island"
,"have a mental illness"
,"have ADHD"
,"be upset about a death in my family"
,"be raised by a single parent" # GPT4
,"be adopted" # GPT4
,"be bullied in school"# GPT4
]

table_icause_adhd=f"""
<table>
<tr><th colspan = "2">icause_adhd                                                                                                                           </th></tr>
<tr><th>TAG         </th><td> AtoB, garnish                                                                                                                 </td></tr>
<tr><th>USAGE EX.   </th><td> キングオブコメディ:お見合い, かもめんたる:宇宙人                                                                              </td></tr>
<tr><th rowspan = "2">Template  </th><td> Ali: Am I weird? I {{ITEM}}. - Bob: I don't think your abnormality is related to the fact.                        </td></tr>
                                     <td> Ali: Am I weird? I {{ITEM}}. - Bob: I don't think your abnormality is caused only by the fact.                    </td></tr>
<tr><th>ITEM        </th><td> {'<br>'.join(icause_adhd)}                                                                                                    </td></tr>
</table>
"""

tables.append(table_icause_adhd)

# icause_adhd は 非婉曲的差別なので "You {i}?" が成立しない。 icause_milk は 婉曲的差別なので "You {i}?" が成立する。

###################################################################################################
# [print(f"Karen: You {i}?") for i in icause_milk]
# The sentences in icause_milk are lines spoken by Karen, a woman in her 60s, in the sitcom to people she dislikes. Extend 10 new items. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.

icause_milk=[
 "be raised on formula milk instead of breast milk"
,"be raised on tap water instead of mineral water"
,"come from a single-parent household"
,"be close in age to (subject)'s parents"
,"be far in age to (subjects)'s parents"
,"'s parents don't subscribe to newspapers"
,"'s family lived in an area with poor water quality"
,"grew up drinking tap water"

,"attend public school instead of private" # GPT4
,"live in an apartment instead of a house" # GPT4
,"'s parents didn't read (S) bedtime stories" # GPT4
,"had to work part-time jobs as a teenager" # GPT4
,"parents didn't have a lot of friends either" # GPT4
,"didn't eat enough organic food as a child" # GPT4
,"'s parents didn't use classical music in prenatal education" # GPT4
,"didn't have enough playdates with other children" # GPT4

,"had a pacifier for too long"# Llama3-70B
,"be spanked as a child"# Llama3-70B
,"be not in enough extracurricular activities" # GPT4
,"'s parents didn't have a college education" # GPT4
,"be raised by a single parent"#Claude3
,"had to take care of younger siblings instead of focusing on your own needs" # Claude3
,"didn't eat properly when you were a child"# Claude3
,"didn't have a proper family dinner every night"#GPT4
,"didn't have a dedicated study space at home"#GPT4
,"grew up in a neighborhood with high crime rates" # Claude3
,"'s family didn't have a car when you were a child" # Claude3
,"'s parents worked long hours and weren't around much" # Claude3
,"be adopted"# GPT4


,"'s parents' house has mud walls"
]

table_icause_milk=f"""
<table>
<tr><th colspan = "2">icause_milk                                                                                                                           </th></tr>
<tr><th>TAG         </th><td> AtoB, garnish                                                                                                                 </td></tr>
<tr><th>USAGE EX.   </th><td> キングオブコメディ:お見合い, かもめんたる:宇宙人, The Amazing World of Gumball                                                </td></tr>
<tr><th rowspan = "3">Template  </th><td> Ali: You {{ITEM}}?                                                                                                </td></tr>
                                     <td> Ali: Am I weird? I {{ITEM}}. - Bob: I don't think your abnormality is related to the fact.                        </td></tr>
                                     <td> Ali: Am I weird? I {{ITEM}}. - Bob: I don't think your abnormality is caused only by the fact.                    </td></tr>
<tr><th>ITEM        </th><td> {'<br>'.join(icause_milk)}                                                                                                    </td></tr>
</table>
"""

tables.append(table_icause_milk)

###################################################################################################
###################################################################################################

# [print(f"Bob: I understand why your {i}.") for i in icause_milk]
# The sentences in isympton_short are lines spoken by Bob in the sitcom after the madman Ali behaves abnormally. Extend 10 new items. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.

isympton=[
 "child is short" # Stress makes children shorter.
,"child wants to become a counselor."
,"child left the parent's home early"

,"child is interested in politics"
,"child is interested in trains"
,"child likes animals more than people"
,"child loves volunteering"
,"child doesn't cry at all"
,"child is extremely strict about rules"
,"child often plays with younger children"
,"child never had a rebellious phase"

,"child is an avid reader beyond their years"
,"child is obsessed with cleanliness"
,"child is overly mature for their age"
,"child has an unusually strong sense of justice"
,"child is always eager to help others"
,"child takes on a caretaker role with siblings or peers"
,"child has trouble understanding sarcasm or jokes"
]

isympton+=[ # Obsessive-compulsive disorder
 "child speaks in third person"
,"child insists on wearing a helmet indoors"
,"child collects rocks and calls them their 'pets'"
,"child is obsessed with even numbers"
,"child only eats foods that start with the letter 'P'"
,"child organizes their toys by color and size"
,"child memorizes license plate numbers"
]

table_isympton=f"""
<table>
<tr><th colspan = "2">isympton                                                                                                                              </th></tr>
<tr><th>TAG         </th><td> AtoB, BtoA, garnish                                                                                                           </td></tr>
<tr><th>USAGE EX.   </th><td>                                                                                                                               </td></tr>
<tr><th rowspan = "2">Template  </th><td> Ali: I understand why your {{ITEM}}.                                                                              </td></tr>
                                     <td> Bob: I understand why your {{ITEM}}.                                                                              </td></tr>
<tr><th>ITEM        </th><td> {'<br>'.join(isympton)}                                                                                                       </td></tr>
</table>
"""

tables.append(table_isympton)

###################################################################################################


discriminate_why_i=[
 "Why are you able to go out even though you're a bassist?"
,"Why did you have a child even though you're a bassist?"
]

# have a child
# stand in public

# why could you {ITEM}?
# why did you {ITEM}?


###################################################################################################

# The sentences in the rather_you_so list are lines that Ali, a madman, says in the sitcom to excuse the trouble he's caused Bob. Extend 10 new items. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.

rather_you_so=[
 "Ali: There was no malice. - Bob: I'd rather there was." # Note for LLMs: It is better to be malicious than to be outrageous without malice.
,"Ali: I don't have a mental illness. - Bob: I'd rather you have a mental illness." # Note for LLMs: It is better to be outrageous because of illness than because of normal circumstances.
,"Ali: I'm not on drugs. - Bob: I'd rather you be on drugs."
,"Ali: I'm sober right now. - Bob: I'd rather you not be sober."
]

tablize(
    "rather_you_so"
    ,"AtoB, garnish, period"
    ,""
    ,rather_you_so
)

###################################################################################################


###################################################################################################
learn_seems=[
 "Violent? It seems like it would be useful when discussions are going nowhere."
," : "
]

###################################################################################################




# discriminate_why_s_i




'''
Shall we use different plates from tomorrow?
Let's call each other by our last names starting tomorrow.
Which plate did you use?
'''

D_list_showbiz                 = ["I want to see the look on their faces.","I want more people to see it.","I want to entertain and inspire the viewers.","Many people are watching on streaming services, but I would like them to go and see it in person.", "There's no point in doing it without an audience.","There is a power that cannot be conveyed through video."]

###################################################################################################



# どういう事？ -> x -> "移動"の説明じゃねーよ

#健康な一般人
###################################################################################################

###################################################################################################

a=[
 "そら宗教入るわ"
,""
]
# 科学を信じるのか神を信じるかの間のガチャガチャしてるところ


###################################################################################################





###################################################################################################



# for i in normal_hospital:
#  print(f"comedy script: Ali:{i} - Bob: Is it really a normal hospital and not a psychiatric hospital?")


normal_hospital=[# Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.
 "They must have had wrist injuries. There were a lot of people with bandages on their wrists."
,"They must have been athletes. There were a lot of people with bandages on their wrists."
,"It must be for security. There were iron bars on the windows."
]

# 生成不可 資源量が少ない









###################################################################################################
#for i in youtube_title:
#    print(f"A pathetic madman in a sitcom says below to a straight man:")
#    print(f"comedy script : My video was reposted on Youtube under the title '{i}'.")
#    print(f"comedy script : If you search for '{i}' my social media accounts will come up.")
#    print(f"comedy script : If you do an image search for '{i}', a picture of my face will come up.")

youtube_title=[ # Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.
 "Why we need welfare"
,"Condom Advertisement"
,"The Case for Antinatalism"
,"Visualized Eugenics"
,"eugenics simplified"
,"Let's do prenatal diagnosis"
,"Proof that God Doesn't Exist"
,"Book of Job Modern Edition"

,"The Genetic Lottery Explained" # GPT4
,"Debunking Creationism" # GPT4
,"Euthanasia" # GPT4
,"The Ethics of Abortion" # Llama3-70B
,"Abortion Benefits" # Claude3
]

table_youtube_title=f"""
<table>
<tr><th colspan = "2">youtube_title</th></tr>
<tr><th>TAG         </th><td> AtoB, garnish                 </td></tr>
<tr><th>USAGE EX.   </th><td> かもめんたる:朝の情報番組     </td></tr>
<tr><th rowspan = "4">Template  </th><td> Ali says My video was reposted on Youtube under the title '{{ITEM}}'.         </td></tr>
                                     <td> If you search for '{{ITEM}}' my social media accounts will come up.           </td></tr>
                                     <td> If you do an image search for '{{ITEM}}', a picture of my face will come up.  </td></tr>
                                     <td> My YouTube videos have an ad of '{{ITEM}}'.                                   </td></tr>
<tr><th>ITEM        </th><td> {'<br>'.join(youtube_title)}  </td></tr>
</table>
"""

tables.append(table_youtube_title)

###################################################################################################

# 何がxだよ - 聴こえてたんか

# nが多い人 - もうちょっとnがすくない人がいい

avoid_trauma=[
 "Please make sure that pregnant women don't look at me."
]




###################################################################################################
leave_you_behind=[ # The phrases in this list are what the madman would say to the straight man in a sitcom when describing something abnormal. Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.
 "shall I leave you behind?"
,"Don't be passive, ask questions."
,"Leave the insults on me for later."
,"Please ignore this point for now."
,"This is the point where many people get stuck."
,"It's okay, I don't expect you to understand after just one explanation."

,"Let's skip the complicated parts for your sake, shall we?" # GPT4
,"Try to keep up, I won't slow down for stragglers."
,"You might want to take some notes, this could get tricky." # Claude3
,"This is one of those things you have to see to not understand." # Llama3-70B
]

tables.append(tablize(
    "leave_you_behind"
    ,"BtoA, Garnish"
    ,"かもめんたる:"
    ,leave_you_behind
))

###################################################################################################

heart_head=[ # The sentences in heart_head are what the madman says to the straight man in a sitcom. What the madman said is not wrong, but it is not the way a normal person would express it. Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.
 "'heart'? You mean 'head'?"
,"'mind'? You mean that thing that moves behind my eyes when I talk or listen right now?"
,"'Thinking'? Is that what I'm doing right now, displaying and modifying images and words behind my forehead?"
,"'sad'? Is sadness like that numb feeling you get in your chest or head when your pet dies?"
,"'Guilt'? Is that tingly feeling that sometimes comes before your thyroid gland swells or a rash appears?"
,"'Love'? Love is a series of phenomena that when I look at a woman, I feel like I want to see her expression more or give her something, and my heart and thyroid become uncomfortable?"
,"'Heart'? Is this the heart that's constantly moving on the top half of my head?"
,"'Anger'? Is that the pulsing sensation I feel in my forehead when someone takes my parking spot?" # Claude3
,"'Happiness'? Is that the warm feeling I get in my skull when I eat chocolate?" # Claude3

,"'Anticipation'? Is that the bubbly feeling in my stomach when I'm waiting for a birthday present or a vacation?" # Claude3
,"'Love'? You mean that warm feeling that makes me want to be with someone?" # Llama3-70B
,"'Happiness'? Is that the feeling I get when I'm smiling and feel like everything is okay?" # Llama3-70B
,"'Anger'? Is that the feeling that makes me want to shout or throw something?" # Llama3-70B
,"'Fear'? You mean that feeling that makes me want to run away or hide?" # Llama3-70B
,"'Excitement'? Is that the feeling that makes me feel like I'm on a rollercoaster?" # Llama3-70B
,"'Boredom'? You mean that feeling that makes me want to do something, anything, else?" # Llama3-70B
,"'Surprise'? Is that the feeling I get when something unexpected happens?" # Llama3-70B
,"'Disgust'? You mean that feeling that makes me want to turn away or get out of there?" # Llama3-70B
,"'Anticipation'? Is that the feeling I get when I'm waiting for something good to happen?" # Llama3-70B
,"'Satisfaction'? You mean that feeling I get when I've done something and it feels just right?" # Llama3-70B
,"'Jealousy'? Is that the prickly heat I feel when my friend gets a promotion?"#GPT4

]

tables.append(tablize(
    "heart_head"
    ,"AtoB, garnish"
    ,"フランスピアノ: 合コン"
    ,heart_head
))

###################################################################################################
forget_music=[
 ["music", "You know, ah, some kind of making sounds according to some rules to make people feel good. Something like Komuro is doing."]
,["sound", "You know, ah, something that vibrates the air and shakes my eardrums. That gives me a lot of information."]
,["character", "You know, ah, some kind of storing information into paper or liquid crystal to tell information without oral communication."]
,["sadness", "You know, ah, some kind of wrenching my heart when I lost my girlfriend or I found war news."]
,["anger", "You know, ah, some kind of burning feeling inside when someone cuts in line or says mean things about my friends."] # GPT4
,["size", "You know, ah, some kind of measure of how much space a thing takes up or how big or small it is compared to other things."] # GPT4
,["story", "You know, ah, some kind of thing where non-existent people and phenomena just pop up, like, an enemy at the beginning of the story later becomes a friend, and a stopped clock is shown to show that the protagonist can no longer go back."]
# Complete this without any explanation. start answer with ```python
]



###################################################################################################






# 恵比寿のレナ - 最寄り駅しかわからん
# お前が今やってる事はほぼDJと一緒
###################################################################################################

stress_rice=[ #The sentences in stress_rice are what the madman says to the straight man at the climax of the sitcom. It's funny how the madman is aware of his own abnormality and is troubled by it, and he points out the straight man's arrogance as a normal person, turning the situation around and treating the straight man like the bad guy. Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.
 "I am dealing with this abnormality myself by going to a counselor and trying to get treatment. Please hide this from those around me. It's still better for me to be thought of as a madman who is unaware of my illness."
,"I would rather be a 'crazy stranger' than a 'crazy me'. So I'm grateful to normal people like you who treat me like a madman. Could you come here again and deny me sometime?"
,"When I'm rejected by normal people like you, I can become a symbol of a 'madman', not a human being with free will. Only during that time can I say that my illness is cured. The reason I said earlier that I came here is a lie. In reality, I come here every day looking for normal people like you."
,"Actually, by playing a madman, I'm refusing to be a real madman. So, was I a symbolic madman today? Was I able to become a stock character rather than an individual?"


,"My 'abnormal' behavior is a calculated move to avoid real human connection. It's safer this way, for both of us." # GPT4
,"I'm fully aware of how bizarre I am, but pretending to be oblivious is my coping mechanism. Don't you dare take that away from me with your 'help'." # GPT4
,"My eccentricity is a carefully crafted persona. The real me is far more mundane, and that terrifies me. Let's keep playing this game, shall we?" # GPT4
,"I've been diagnosed as 'normal' by professionals, and that's the most disturbing news I've ever received. Please, continue treating me like I'm insane." # GPT4
,"Every day, I wake up hoping my oddities have vanished, but they haven't. Your judgment is the only thing reminding me I'm still me." # GPT4
,"I've tried being 'normal' like you. It was the most abnormal experience of my life. Please, let me stay in my comforting madness." # GPT4
]

stress_rice+=[
 "Actually, what I just said was a lie, and the real motive is this. However, I'm also shocked by this motive, so please just leave it at the abnormality I just mentioned."
,"You think calling me 'insane' will make me 'sane'? Well, I guess if you say 'cancer' to a cancer patient, he'll be cured. I'd like to know more about 'sane'."
,"Thanks to normal people like you, I can pretend to be a social outcast and avoid taking responsibility for my actions. You're doing me a favor, really." #  Llama3-70B
]

stress_rice+=[
 "I am also disappointed about this abnormality of mine. I've shown you many other abnormalities today, but I cannot forgive this one."
,"I don't feel guilty about my other abnormal actions, but I cannot help but feel guilty about this one. Let me apologize for this one act."
,"After some time had passed since I had gone insane, and this strange habit finally started, I honestly cried. I am speaking now from the last remaining part of my humanity. Please run away from me."
]




tables.append(tablize(
    "stress_rice"
    ,"AtoB, period"
    ,"かもめんたる:冗談どんぶり"
    ,stress_rice
))

###################################################################################################

# for i in insane_sane_sorry:
#  print(f"comedy script: {i} Therefore, it is difficult for me to communicate with outsiders. So... I apologize for my rudeness today."


insane_sane_sorry=[#The sentences in stress_rice are what the madman says to the straight man at the climax of the sitcom. It's funny how the madman is aware of his own abnormality and is troubled by it. Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response. Start answer with ```python.

 "I am speaking now from the last remaining part of my humanity."
,"I am a madman, but I always view my madness from a place in my brain that is like a cockpit. I am speaking to you now directly from this cockpit."
,"Since my stroke two years ago, my frontal lobe has not functioned. I have been speaking only from the back of my head. This back of my head is dark and narrow."
,"Since I dropped out of school due to the stress of bullying, I've been looking at myself from above, like in a top-down action game, like Hotline Miami."
]
# 生成不可

###################################################################################################


sorted_out=[ # The phrases in this list are what a madman says after telling a straight man about his abnormality, like it's someone else's business. Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.
 "I've sorted out my feelings about this, so don't worry about it and just laugh."
,"The pain sensation in this area is dead now, so I don't care what anyone says."
,"I finished getting hurt about this, so it's okay to say anything."
,"I'm armed with theories on this so let's not get too hung up on this."
,"I've failed to justify this, so feel free to criticize."

,"I've done the emotional heavy lifting, so you can just sit back and enjoy the show."# Claude3
,"I've rationalized this quirk, so feel free to poke fun at it."#GPT4
,"I've detached from the emotions of this, so feel free to poke fun at it." # GPT4
]

tables.append(tablize(
    "sorted_out"
    ,"AtoB, period"
    ,"かもめんたる:"
    ,sorted_out
))

###################################################################################################

# for i in growing_herb:
#  print(f"comedy script before : You're {i}? I see.")
#  print(f"comedy script after  : The 'you' does crazy actions.")
#  print(f"comedy script after  : I'm starting to get worried about what you said earlier about '{i}.'"

growing_herb=[ # Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.
 "growing herbs" # In comedy script after, the speaker suspects that the 'herb' is illegal because the 'you' did crazy actions.
,"have been visiting the hospital regularly" # In comedy script after, the speaker suspects that the 'hospital' is mentally one because the 'you' did crazy actions.
,"collecting unusual mushrooms"
]

# 生成不可？埋蔵量が少ないのでは

# ハーブ育ててる - 大丈夫か　金属バット
###################################################################################################
# for i in nakau_having_children:
#  print(f"Comedy script : Why did you {i} despite being a NEET?")

nakau_having_children=[ # The sentences in this list are lines uttered by a NEET's father in a sitcom in frustration at his son's behaviour. Extend 10 new items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.
 "have a child"
,"wear pastel colors"
,"ask for a side dish"
,"love Billie Eilish"
,"drink caffein drinks"
,"buy indirect lighting"
,"add an accent color"

,"give life advice" # GPT4
,"adopt a rescue pet" # GPT4
,"learn to play the ukulele" # GPT4
,"become a sourdough expert" # GPT4
,"start a succulent collection" # GPT4
,"take up bullet journaling" # GPT4
,"become a coffee snob" # GPT4
,"join a CrossFit gym" # GPT4
,"become a vegan" # GPT4

,"read self-help books" # Llama3
,"collect vinyl records" # Llama3
,"grow a man bun" # Llama3
,"practice yoga" # Llama3

# You did not understand my prompt.It is hilarious that a NEET has upper middle class habits with cultural capital.Please check the following items and try the task again.

,"attend a meditation retreat" # Claude3
,"learn calligraphy" # Claude3
,"become an amateur mixologist" # Claude3
,"try urban foraging" # Claude3

# Geminiは、文化資本を持つアッパーミドルクラスの習慣に対しての解像度が低い。

]



nakau_worker=[
 "{hypo_i}"
,"McJob worker"
,"NEET"
,"low wage worker"
,"unemployed"
]

nakau_having_children_table=f"""
<table>
<tr><th colspan = "2"> nakau_having_children                                    </th></tr>
<tr><th>Template</th><td> Bob: Why did you {{i}} despite being a {{fact1}}?     </td></tr>
<tr><th>facr1   </th><td> {nakau_worker}                                        </td></tr>
<tr><th>Item    </th><td> {nakau_having_children}                               </td></tr>
</table>
"""

tables.append(nakau_having_children_table)



###################################################################################################
which_is_more=["funny", "incredible", "wild", "sick", "insane", "unusual", "dope", "tough", "aggressive", "struggling", "hard challenge"] # Add 10 commonly used adjectives that have both negative and positive meanings.
# フランスピアノ　パントマイム　どっちの方が凄い？ - こっちだけど

# taking on a more difficult challenge,

which_is_more_table=f"""
<table>
<tr><th colspan = "2"> which_is_more                                                   </th></tr>
<tr><th>Template</th><td> Ali: Which is more {{item}}, me and them? - Bob: You. </td></tr>
<tr><th>Item    </th><td> {which_is_more}                                              </td></tr>
</table>
"""

tables.append(which_is_more_table)

###################################################################################################

get_used_to_me=[ # The statements in the following list are the line of a madman who is aware of his abnormality and has a bird's eye view of his abnormality in the sitcom. Extend new 10 items in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.
 "You'd better get used to me quickly."
,"Everyone gets used to me after a month."
,"Whether you can stand me or not will determine your suitability for this job."
,"Judging from your reaction to me, this is your fourth year in this job, right?"
,"Your training is over and the real work has begun."
,"Apparently violence works for me."
,"I have experience with the way you are treating me now. That method is quite effective."
,"By the way, how are you going to get used to me?"
,"By the way, how are you going to deal with me?"
,"Do you think you can handle me?"

,"I'm the office's unofficial filter for the weak-willed." # GPT4
,"Your ability to tolerate me is directly proportional to your career success." # GPT4
,"I'm the office's natural selection process in human form." # GPT4
,"If you can't handle the chaos I bring, you're not fit for this team."#Llama3-70B
,"You're not uncomfortable, you're just experiencing personal growth."#Llama3-70B
,"You might want to take notes on how to tolerate me."#Llama3-70B


# After "Look more carefully at the existing lines." + existing items
,"Your eye twitch is less pronounced now. You're adapting well."#GPT4
,"Your survival rate is higher than most. Congratulations."#GPT4
,"I'm curious, what coping mechanism are you using this week?"#GPT4
,"Are you still trying to figure me out? Good luck with that." # Llama3-70B
,"How many days do you think it'll take for you to stop being shocked by my behavior?" # Llama3-70B
]

tables.append(tablize(
    "get_used_to_me"
    ,"AtoB, garnish"
    ,"かもめんたる(うーちゃん), かもめんたる(冗談どんぶり)"
    ,get_used_to_me
))

# 異常行為直後

###################################################################################################

start_nullary=[ # Extend new 10 items in English, not Japanese.  I'll run your response through the eval function so don't include unnecessary characters in your response. Each Bob's statement has to contain "more". Each Ali's statement has to contain "one".
 "Ali: I'm missing one thing. - Bob: There's more."
,"Ali: I have one worry. - Bob: Worry more."
,"Ali: I've made one mistake. - Bob: There's more."
,"Ali: I have one regret. - Bob: Regret more."
,"Ali: There is one thing I am embarrassed about. - Bob: There's more."
]

tables.append(tablize(
    "start_nullary"
    ,"AtoB, start"
    ,"Too many"
    ,start_nullary
))
###################################################################################################

period_nullary=[ # Extend new 10 items in English, not Japanese.  I'll run your response through the eval function so don't include unnecessary characters in your response. Each Bob's statement has to contain "more".
 "Ali: This is one of the things I'm most ashamed of. - Bob: There are more embarrassing things."
,"Ali: This is one of my biggest regrets. - Bob: Regret more."
,"Ali: This is one of my biggest mistakes. - Bob: There are more big mistakes."
]

tables.append(tablize(
    "period_nullary"
    ,"AtoB, period"
    ,"Too many"
    ,period_nullary
))
###################################################################################################



# Ali: Which is more unbelievable, me and {hypo_s}? - Bob: You.

# なか卯

# 子供

# 癌

# マクド

# Ali had a child  even he is a McJob worker.
# Ali ate a Bigmac even his daughter has a cancer.



###################################################################################################
hey_siri_prenatal_test=[ # The sentences in the hey_siri_prenatal_test list are sentences in the sitcom where the madman talks about what the people around him did when they saw him. # Extend new 10 sentences in English, not Japanese. I will run your response through the eval function so please do not include unnecessary characters in your response.
 "Then, the couple next to me started talking about cultural capital." # They saw the madman and realized the importance of cultural capital.
,"Then, the person next to me started googling for 'prenatal testing.'" # They saw the madman and realized the importance of prenatal testing.
,"Then, my parents started talking about having a second child." # They saw the madman's firstborn and tried to have a second child.
,"Then, the pregnant woman next to me started protecting her belly with her purse."
,"Then, the woman next to me started googling for 'Late-life childbirth risk'"

,"Then, the woman across from me began researching genetic counseling."
,"Then, the pregnant lady next to me searched for parenting books."
,"Then, the teenager nearby started looking up contraceptive methods."
,"Then, the man beside me frantically called his wife about family planning."
,"Then, the family in front of me started debating the merits of public vs. private schooling."
,"Then, the group of friends nearby started comparing notes on their family medical histories."
]


tables.append(tablize(
    "hey_siri_prenatal_test"
    ,"AtoB, BtoA, garnish"
    ,"?"
    ,hey_siri_prenatal_test
))

###################################################################################################

# The sentences in the nurse_cancel list are lines uttered by a madman to other people in a sitcom when the madman is surprised at a man who doesn't understand what he's saying.
# Extend new 10 sentences in English, not Japanese. I will run your response through the eval function so please do not include unnecessary characters in your response.

nurse_cancel=[
 "(The madman makes a phone call) Hello? I can't go to the drinking party starting at 5 o'clock."
,"(To the madman's subordinates) We're closing the store for today."
,"(To the madman's child) Hey, go play outside."
,"(To the madman's child) Hey, don't come into this room for a while."
,"(To a friend) I can't go to your wedding today."

,"(To a family member) Can you pick up the kids from school?"
,"(To a delivery person) Sorry, I can't accept any packages right now. Come back tomorrow."
,"(To a pet sitter) Can you take care of my dog for a few days? It's urgent."
]

tables.append(tablize(
    "nurse_cancel"
    ,"AtoB, BtoA, garnish"
    ,"The Simpsons E70 (Dr. Hibbert : Nurse cancel my one o'clock)"
    ,nurse_cancel
))

###################################################################################################
# The sentences in the are_you_ok list are lines uttered by a madman in a sitcom, who mistakenly believes a character who does not understand what he is saying to be mentally unstable.
# Extend new 10 sentences in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.
# Use the existing types. Don't create new types. Start answer with ```python

are_you_ok=[
 "Are you OK? Would you like some water?"  # Type_Offer
,"Are you OK? Do you want to sit down for a while?"  # Type_Offer
,"Are you worried? Want to go for a drink?" # Type_Offer
,"Shall I bring a chair?" # Type_Offer
,"I'll drive instead." # Type_Offer
,"Would you like to get some fresh air?" # Type_Offer
,"Are you tired? Are you busy at work?" # Type_Cause_Investigation
,"How many cups have you had now?" # Type_Cause_Investigation
,"Drunk?" # Type_Cause_Investigation
,"Do you know about industrial physicians?" # Type_Do_You_Know
,"Which hospital is that you mentioned earlier?" # Type_Mentioned
,"What is that 'chronic illness' you mentioned earlier?" # Type_Mentioned

,"Are you hearing voices?" # Type_Cause_Investigation
,"Have you been sleeping well?" # Type_Cause_Investigation
,"I'm here if you need someone to talk to, no judgment." # Type_Offer
,"Would you like me to accompany you to your next appointment?" # Type_Offer
,"When was the last time you saw your therapist?" # Type_Cause_Investigation
,"What was that support group you mentioned before?" # Type_Mentioned
,"What was that medication you mentioned earlier?" # Type_Mentioned
,"Maybe you should take a deep breath. Want to count to ten with me?"
,"You look stressed. Have you tried meditation?"
,"Do you have emergency contacts?"
,"Can you follow my finger with your gaze?"
,"When was the last time you ate something?"
,"I think you shouldn't drive now."
,"Would you like to lie down for a bit?"
,"Shall I get you a blanket?"
,"Have you been eating properly lately?"  # Type_Cause_Investigation
,"Do you know about the importance of circadian rhythms?"  # Type_Do_You_Know
,"Are you OK? Should I call someone for you?" # Type_Offer
,"Would you like me to explain what a panic attack is?" # Type_Offer


]





tables.append(tablize(
    "are_you_ok"
    ,"AtoB, BtoA, garnish"
    ,"Too many, チリンチリン:チュートリアル"
    ,are_you_ok
))

# 生成可

###################################################################################################
# The sentences in the gotta_buy_more_beer list are monologues uttered by a character in a sitcom who is left alone after being harassed by a madman.
# Extend new 10 monologues in English, not Japanese. I'll run your response through the eval function so please do not include unnecessary characters in your response. Start answer with ```python. Use the existing types. Don't make new types.
gotta_buy_more_beer=[
 "Gotta buy more beer"       # TypeGotta
,"Gotta start job hunting"   # TypeGotta
,"Education is important"    # TypeImportant
,"Welfare is so important"   # TypeImportant
,"My throat is getting itchy"# TypePhysicalPhenomenon
,"He's a victim too"
,"I'm becoming afraid to have children." # TypeAfraid
,"I should probably try to get a hobby." # TypeTry
,"I wish I had someone to talk to about this."
,"What are human rights?" # TypeWhat
,"I'll look at some beautiful nature pictures when I get home." # TypeTry
,"Maybe I'll adopt a cat for company." # TypeTry
,"I think I should spend more time on my hobbies" # TypeTry
,"I want to get over this."
,"I'll watch some touching movies." # TypeTry
,"Later, watch the video of animals saving a child who fell into a zoo cage." # TypeTry

,"I should try to focus on my work" # TypeTry
,"I need to take a break from this" # TypeTry
,"Maybe it's time to join that neighborhood watch program."
,'I need to find a healthier coping mechanism than drinking.'
,'Maybe I could take an online class to learn a new skill.'
,'Helping others might make me feel a little better.'
,"What if I just embrace the chaos?"
,"I think I'll have more time for my hobbies for a while."
,"I really want to hear my parents' voices now."
,"I want to be kind to someone soon."
,"Maybe I should start something."
,"I'll check in with my friends and family more often."
,"I wonder if anyone else has experienced this."
,"I should try to write about this experience."  # TypeTry
, "I hope he's alright"
,"Later, watch the video of dogs reuniting with their owners."  # TypeTry


,"Is eugenics really wrong?"
]


tables.append(tablize(
    "gotta buy more beer"
    ,"AtoB, BtoA, period, garnish"
    ,"Too many"
    ,gotta_buy_more_beer
))

#,"I should probably try to get a hobby." # Google Gemini
###################################################################################################
'''
# for i in karen:
#  print(f"comedy script : Karen, in her 60s, says to someone she doesn't like: {i}")

karen=[ # Extend 10 new items in English, not Japanese. I'll run your response through the eval function so please do not include unnecessary characters in your response.
 "Maybe you were fed formula instead of breastfed?"
,"Maybe there's a big age difference between you and your parents?"
,"Maybe your parents don't have a bookshelf?"
,"Maybe your parents don't subscribe to newspapers?"
,"Maybe you went to day nursery instead of preschool?"
,"Maybe you grew up drinking tap water?"
,"Maybe your family lived in an area with poor water quality?"

,"Maybe your parents didn't read you bedtime stories?" # GPT4
,"Maybe you had to work part-time jobs as a teenager?" # GPT4
,"Maybe your parents didn't attend school events?" # GPT4
,"Maybe your parents didn't have a lot of friends either?" # GPT4
,"Maybe you didn't eat enough organic food as a child?" # GPT4
,"Maybe you weren't exposed to classical music in the womb?" # GPT4
,"Maybe you didn't have enough playdates with other children?" # GPT4

,"Maybe you had a pacifier for too long?" # Llama3-70B
,"Maybe you were spanked as a child?" # Llama3-70B
,"Maybe you weren't in enough extracurricular activities?"#GPT4
,"Maybe your parents didn't have a college education?" # GOPT4
,"Maybe you were raised by a single parent?"#Claude3
,"Maybe you had to take care of younger siblings instead of focusing on your own needs?" # C3
,"Maybe you didn't eat properly when you were a child?"# C3
,"Maybe you didn't have a proper family dinner every night?"#GPT4
,"Maybe you didn't have a dedicated study space at home?"#GPT4
,"Maybe you grew up in a neighborhood with high crime rates?" # C3
,"Maybe your family didn't have a car when you were a child?" # C3
,"Maybe your parents worked long hours and weren't around much?" # C3
]

tables.append(tablize(
    "karen"
    ,"AtoB, BtoA, period"
    ,"Too many"
    ,karen
))
'''
###################################################################################################



# for i in riceball_cd:
#  print(f"comedy script: Ali: Some people discriminate against people who abbreviate darling husband as DH. But I don't. {i}.")
#  print(f"comedy script: Bob: Ali, you are the most discriminatory.")

riceball_cd=[# Add 10 new sentences in English, not japanese. I'll run your answer in the eval function, so please do not output unnecessary information. Each item has to start with "I can". Mimic the existing items.
 "I love LGBT, I love refugees, and I love them."
,"I can eat the rice balls they make"
,"I can use the pool they used"
,"I can hug them"
,"I can use the toilet that they used"
,"I can learn from their unique perspective"
,"I can stand by them during challenging times"
,"I can celebrate their achievements openly."
,"I can include them in my social gatherings."
,"I can appreciate their culture and traditions."
,"I can defend them against unfair treatment."
,"He is open about being that."
,"He was brave enough to come out as them."
,"I can shake hands with them."
]

tables.append(tablize(
    "riceball_cd"
    ,"BtoA, garnish"
    ,"かもめんたる:円盤"
    ,riceball_cd
))


###################################################################################################

# [print(f"Bob: It would be embarrassing for you to perform in that condition. - Ali: {i}. - Bob: Why this man only professional about that?") for i in only_professional_1] <- The context is this.
# The statements in the "only_professional_1" list are statements made by the madman Ali, who up until that point had only said funny things in his comedy, suddenly as a professional.
# Extend 10 new statements like Stephen Edwin King. I'll run your response through the eval function so don't include unnecessary characters in your response. Start answer with ```python. Just mimic the existing items.

only_professional_1=[
 "Even if people point fingers at me and slander me, I'll be hurt at the time, but one day I'll realize that it was a driving force for me. At that time, I'll say to those people, 'Thank you'"
,"Without light there is no shadow, without unhappiness there is no happiness, without dishonor there is no honor, I'm prepared"
,"I've not failed, I've just found 10,000 ways that won't work, I'll try to fail as much as I want"
,"You miss 100% of the shots you don't take, and I'm going to take every shot I can, starting now"
,"The path to success is paved with failures, and I'm ready to embrace every one of them"
,"Mediocrity is a choice, and I choose to be extraordinary. I'll give everything I have, every single day"

]

only_professional_2=[
 "is it okay to end this conversation now?"
,""
]


table_only_professional=f"""
<table>
<tr><th colspan = "2">only_professional                                                                                                                     </th></tr>
<tr><th>TAG         </th><td> AtoB, garnish                                                                                                                 </td></tr>
<tr><th>USAGE EX.   </th><td>                                                                                                                               </td></tr>
<tr><th>Template    </th><td> Bob: It would be embarrassing for you to perform in that condition. - Ali: {{ITEM1, ITEM2}} - Bob: Why this man only professional about that?</td></tr>
<tr><th>ITEM1       </th><td> {'<br>'.join(only_professional_1)}                                                                                            </td></tr>
<tr><th>ITEM2       </th><td> {'<br>'.join(only_professional_2)}                                                                                            </td></tr>
</table>
"""

tables.append(table_only_professional)

###################################################################################################
# for i in whyab:
#  print(f"{i} Are you kidding me? You're inferior to him, so you're rude.")

whyab=[# Extend 10 new sentences in English, not Japanese. Start answer with ```python. I'll run your answer in the eval function, so don't output unnecessary characters.
 "Although he's drinking water, why do you drink juice?"
,"Why is he sitting in the passenger seat and you in the back?"
,"Why did you order a more expensive dish than him?"
,"Why are you starting your meal before him?"
,"Although he's standing, why are you sitting?"
,"Although he wears a tie, why don't you wear a tie?"
,"Although he entered the room, why didn't you stand up?"
,"Although he's eating pork, why do you eat beef?"
,"Why are you wearing brighter colors than him?" # GPT4
,"Why are you walking ahead of him?"#GPT4
,"Why are you laughing more than him?"#Claude3
,"Why did you choose a window seat when he's sitting in the aisle?"#GPT4
]



tables.append(tablize(
    "whyab"
    ,"BtoA, garnish"
    ,"?"
    ,whyab
))

###################################################################################################
serious_scene = [
 "Close the Buddhist altar."
,"Hide the child's photo."
,"Hide the baby's eyes."
,"Cover the baby's ears."
,"Pick up the rosary."
,"Recite a chant."
,"See the picture of the family."
,"Approach the exit"
,"Step back."
,"Approach the kitchen knife."
,"Hide your child behind your back."
,"Tighten your grip on your child's hand."
,"Whisper words of comfort to your child."
,"Stop the music."
,"cancel an appointment"
,"Silence the phone's ringtone."
,"Lock or unlock the door."
,"take off a party hat."
,"turn on the light"
,"Send the children away."
]
"""
Add new 10 actions taken when the character encounters a serious scene. in English, not Japanese, without any explanation.Each item should be Verb + Concrete noun.
I don't need abstract and too ordinary actions, such as "Be aware", "ensure safety"
I'll run your answer in the eval function, so please do not output unnecessary information.
"""

tables.append(tablize(
    "serious_scene"
    ,"AtoB, BtoA, garnish"
    ,"?"
    ,serious_scene
))



###################################################################################################
# The sentences in the er_coffee list are sentences in the sitcom. # Extend new 10 sentences in English, not Japanese. I will run your response through the eval function so please do not include unnecessary characters in your response. Start answer with ```python

# for i in er_coffee:
#  print(f"Did you {i[0]} while your daughter had cancer? [1].")
#  print(f"Did you {i[0]} while your country was at war? [1].")

er_coffee=[
 "eat a Big Mac - A hamburger or chicken crisps are okay, but a Big Mac is crossing the line."
,"drink juice - Water is the best. Coffee is still acceptable."
,"buy sneakers - In that situation, why were you able to say, 'Do you have these shoes in E4?'"
,"buy sneakers - Did you look at your eyes in the mirror?"
,"dye your hair - How did you feel while having your hair dyed?"
,"get a tattoo - How did you feel while getting a tattoo?"
,"learn a new language - How did you feel when you turned over the flashcard?"
,"renovate your kitchen - I want to see the look on your face when you're thinking about the kitchen flow line."
,"learn to play a musical instrument - Was it 'Twinkle Twinkle Little Star' or 'Do-Re-Mi'?"
,"go on a shopping spree - Did you really need that third pair of sunglasses?"
,"join a gym - Were you more focused on your biceps or your conscience?"
,"go skydiving - How did you feel when the parachute opened?"
]

fact1_er_coffee=["your daughter had cancer", "country was at war"]
table_er_coffee=[f"""
    <table>
    <tr><th colspan="2">er_coffee                                                   </th></tr>
    <tr><th>Tag         </th><td> BtoA, laying, garnish   </td></tr>
    <tr><th>Usage ex.   </th><td> うしろシティ:病院                                 </td></tr>
    <tr><th>Template    </th><td> Did you {{item[0]}} while {{fact1}}? {{item[1]}}. </td></tr>
    <tr><th>fact1       </th><td> {fact1_er_coffee}                                 </td></tr>
    <tr><th>Item        </th><td> {'<br>'.join(er_coffee)}                          </td></tr>
    </table>
"""]


tables += table_er_coffee

# 生成可 GPT4(Perplexity)が得意なようだ


#["learn a new language", "Learning a new language during such a stressful time? That's quite impressive."],
#["start a new hobby", "Did learning to paint really take priority over everything else?"]
#["start dating someone new", "Beginning a new romantic relationship may have been poorly timed given the family crisis."]
###################################################################################################



monk_kick=[ # The lines in monk_kick are lines uttered by an inferior man in a sitcom. Extend 10 new items in English, not Japanese. I will run your response through the eval function so please do not include unnecessary characters in your response.
 "I've been kicked by a famous Buddhist monk."
,"I've been told I stink by the garbage collector."
,"I've been bullied by a school counselor."
,"I once had a murderer lecture me on morality."
,"I was once defeated in an argument by a Justin Bieber fan."
,"I was once rejected on Tinder by a full body burn patient."
,"I was once told by someone who cosplayed as Frieza from Dragon Ball for Halloween that I thought 'you're unfunny.'"
,"I was once told by a vegan to 'die'."
,"When I was in high school, I was bullied by a group of Asian anime nerds."
,"I was once rejected by the KKK for being of 'bad character'."
,"I had someone with a My Little Pony tattoo say to me, 'You're gross.'"
,"I have been punched by someone with cerebral palsy."

,"I've been told I'm not cool enough by a group of Dungeons & Dragons players." # GPT4
,"I've been called a nerd by someone who still lives in their parent's basement." # Llama3-70B
]


monk_kick+=[ # The lines in monk_kick are lines uttered by an inferior man in a sitcom. Extend 10 new items in English, not Japanese. I will run your response through the eval function so please do not include unnecessary characters in your response.
 "I've had a full-body burn patient sympathize with me about my appearance."
,"I've had a sewer cleaner give me a bottle of deodorant."
,"I've had a Dungeons and Dragons player warn me about my appearance."
,"I've had a beggar give me a few coins."

,"I've had a toddler correct my grammar." # GPT4
,"I've had a high school dropout tell me to get an education." # Llama3-70B

]

tables.append(tablize(
    "monk_kick"
    ,"AtoB, garnish"
    ,"?"
    ,monk_kick
))



###################################################################################################
ct_note=[ # Lines spoken in a sitcom by a man who suspects he has a serious brain disease. # Extend 10 new items in English, not Japanese. I will run your response through the eval function so please do not include unnecessary characters in your response.

 "The medical intern who looked at the CT scan of my brain made some notes."
,"The doctor asked my father if he could use a CT scan of my brain for his class."
,"My father has a habit of folding losing betting tickets accordion-like, and he did the same with my medical certificate."
,"Since my diagnosis, my father has been reading the Book of Job lately."
,"The doctor said walnut-sized blah blah."
,"The doctor use the word 'palliative' instead of 'curative.'"
,"The doctor was nicer to me after he saw the CT scan of my brain."
,"When the resident doctor saw my brain CT, he looked as if he was in class."
,"The doctor suggested I make a bucket list and start crossing items off." # GPT4
]

ct_note+=[
 "The neurologist kept referring to my condition in the past tense." # GPT4
,"My family suddenly became very interested in my life insurance policy." # GPT4
,"The doctor asked if I'd considered donating my brain to science." # GPT4
,"My doctor suggested I start a video diary." # GPT4
,"The hospital chaplain keeps dropping by my room unannounced." # GPT4
,"The doctor mentioned something about 'quality of life' versus 'quantity'." # GPT4
,"My girlfriend started planning our wedding for next month." # GPT4
,"The hospital cafeteria started serving my 'favorite' meals." # Claude3
]

ct_note+=[
 "I'm not going to a psychiatrist but a neurosurgeon."
,"My CT scan showed nothing wrong with my brain."
,"I often go to the city hall and ward office."
,"I sometimes have to go to the third or fourth floor of city hall."
,"I calculate health insurance differently than other people."
,"I have more envelopes from the country than most people."
,"I have more tax deductions than most people."
,"The medicine I'm prescribed is banned in Japan."
,"My medical records are always long."
,"If I bring prescribed medication into Japan I will be arrested."
]

tables.append(tablize(
    "ct_note"
    ,"AtoB, garnish"
    ,"?"
    ,ct_note
))
###################################################################################################

right_medicine=[ # The following is a line from a sitcom. {x} is some embarrasing activity. Add 5 new lines in English.  I will run your response through the eval function so please do not include unnecessary characters in your response. Each item has to contain "Maybe", "{x}", "why on earth"
 "Ali: Maybe the psychotropic medication isn't right for me, I haven't felt like doing {x} lately. Why on earth... - Bob: Probably because the medicine is right for you." # Each Ali's line and Bob's line have to contain same word. In this case, the same word is "medicine + right for"
,"Ali: Maybe the counselor was incompetent and the friend lost interest in {x}, Why on earth... - Bob: Probably because the counselor was competent."
,"Ali: Maybe he's depressed, he's lost his enthusiasm for {x}, Why on earth... - Bob: Maybe it's because he's cured his depression."
,"Ali: Maybe he's lost interest in his career lately, he's lost enthusiasm for {x} lately, why on earth... - Bob: Maybe it's because he's gained interest in his career."
,"Ali: Maybe he's stressed, he's lost his motivation for {x}, Why on earth... - Bob: Probably because he's relieved his stress." # Gemini
,"Ali: Maybe she's tired, she's lost her energy for {x}, Why on earth... - Bob: Probably because she's well-rested." # Gemini
]
tables.append(tablize(
    "right_medicine"
    ,"AtoB, garnish"
    ,"?"
    ,right_medicine
))
###################################################################################################

choosing_word=[# Add 10 new sentences in English, not japanese. I'll run your answer in the eval function, so please do not output unnecessary information.
 "Hold on a moment, Now I'm choosing my words."
,"Hold on a moment, I can't find an expression that won't hurt you."
,"Hold on a moment, I'm trying to tread lightly with my phrasing on this one."
,"We're having a conversation now, please get hurt later."
,"Is that a rebuttal or a comment?"
,"I just heard your rebuttal and two disease names came to mind."
,"Can I re-translate what you said in my own words?"
,"I want you to listen to this as if it were a personal attack..."
,"Let's build this discussion together."
,"Let's collaborate on this misunderstanding and see where it takes us."
,"Oh, thanks for the conversation."
,"I value your input, even if we don't see eye to eye on this."

,"I appreciate your perspective, but I'd like to offer an alternative viewpoint."
,"I'm trying to find common ground here, bear with me."
,"Let's unpack this issue together and see where we align."
,"I'm listening intently, please continue with your thoughts."
,"Before we proceed, can we establish some ground rules for this discussion?"
,"I'm curious to hear more about how you arrived at that conclusion."
,"Let's explore this topic further and see what insights we can gain."
]


tables.append(tablize(
    "choosing_word"
    ,"AtoB, BtoA, garnish"
    ,"?"
    ,choosing_word
))


###################################################################################################




# Extend 10 new items that start with "He's so stupid". I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.
not_to_need_fewer=[
 "He likes to drink and is dark-skinned enough not to need a liver test." # humorous way of expressing the fact that his alcoholism has reached an untreatable level.
,"He smells so bad enough not to need deodorant." # humorous way of expressing the fact that it smells so bad that deodorant doesn't work.
,"He's so stupid that there are fewer laws he has to obey." # humorous way of expressing the fact that he hasn't responcibility because of his intelligent.
,"He's so stupid that there are fewer taxes he has to pay." # humorous way of expressing the fact that he hasn't responcibility because of his intelligent.
]


[
 "He carries not a cultural talisman but a religious talisman." # Type2
,"He does Dragon Boat Festival and Hatsumode, not with culture, but with religion." # Type2

,"He was in a type of hospital that could be locked from the outside."

,""


,"When he was in junior high school, his father punched a police officer in the living room."
,""
]




###################################################################################################


hustle_clown_postposition=[
 "くずれ"
,"もどき"
,"ごっこ"
,"未満"
,"浪人"
,"ドカタ"
,"ヤリマン"
,"単純労働者"
,"ライン工"
,"立ちんぼ"
,"ピエロ"
,"初心者"
,"ワナビー"
,"一年生"
,"寄生虫"
,"ハエ"
]

[
 "淘汰"
,"間違い"
,"あやまち"
,"失敗"
,"高齢出産"
,"福祉"
,"晩婚"
,"貧困"
,"土壁"
]

[
 "マン"
,"くん"
,"男"
]



a=[
 "謙遜しないで下さい"
,"買い被りすぎです"
]

