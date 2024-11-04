#/home/tarotoyota/agent_dont_et_al_py.py
from agent_output import coloring
from dataclasses import dataclass, field
from typing import List, ClassVar
tables_agent_dont_et_al_py=[] # all tables will be appended here.

###################################################################################################

@dataclass
class Bottom:
    ALL_BOTTOM: ClassVar[List['Bottom']] = []
    bottom_name:str
    bottom_reveal:list
    bottom_dont:list
    def __post_init__(self):
        Bottom.ALL_BOTTOM.append(self)
    @classmethod
    def bottom_name_return(cls):
        return [i.bottom_name for i in cls.ALL_BOTTOM]
    @classmethod
    def bottom_table(cls):
        col=[]
        for i in cls.ALL_BOTTOM:
            col.append(f"<tr><td>{i.bottom_name}</td><td>{i.bottom_reveal}</td><td>{i.bottom_dont}</td></tr>")
        table_bottom=f"""
        <table>
        <tr><th>Bottom </th><th>.bottom_reveal</th><th>.bottom_dont</th></tr>
        {"".join(col)}
        </table>"""
        return table_bottom

bottom_part_time_worker = Bottom("バイト, 非正規, フリーター, ワープア", [],[])
bottom_unemployed       = Bottom("失業者, 無職, ニート", [],[])
bottom_pensioner        = Bottom("年金生活者", [],[])
bottom_low_educated     = Bottom("低学歴, 高卒, Fラン卒", [],[])
bottom_parasite_single  = Bottom("実家住み", [],[])
bottom_debtor           = Bottom("債務者", [],[])

###################################
# 1. Regarding the sentence that presents Ali as a part time worker: It would be unnatural for Ali to suddenly say, "I'm a part-time worker." This is like "placing" a landmine on the ground while making a lot of noise. We have to "bury" the mine secretly.
#    How to make Ali say sentences that indicate he is a part time worker sound natural: "I got a call from a full-time staff." or "I have to hurry because I have a shift tomorrow from 7am to 1pm." As such, reporting with urgency is more natural than making statements for reasons other than that.
# 2. Why am I adding sentences to the lists in redundant way below: if a list requires 10 types of sentences, we need to have the LLMs generate one type at a time or else accuracy will decrease.
###################################

###################################
# Each items has to start with 'I have to hurry '
# Extend 2 lines in each bottom_reveal in English, not Japanese. Use extend function. I'll run your response with eval function, so don't include unnecessary characters in your response. Start answer with ```python. Use the existing types.

bottom_part_time_worker .bottom_reveal += ["I have to hurry because I have a shift tomorrow from 7am to 1pm.",  "I have to hurry because I promised to cover a coworker's shift this evening."]
bottom_unemployed       .bottom_reveal += ["I have to hurry because I have a job interview tomorrow."]
bottom_pensioner        .bottom_reveal += []
bottom_low_educated     .bottom_reveal += []
bottom_parasite_single  .bottom_reveal += ["I have to hurry because my mom is expecting me to pick up groceries on my way home."]
bottom_debtor           .bottom_reveal += ["I have to hurry because I have to pay the loan by 9pm."]
###################################
# Each items has to start with 'Next time, come'
# Extend 2 lines in each bottom_reveal in English, not Japanese. Use extend function. I'll run your response with eval function, so don't include unnecessary characters in your response. Start answer with ```python. Use the existing types.

bottom_part_time_worker .bottom_reveal += ["Next time, come see me when I'm working. I work there from Saturday to Tuesday."]
bottom_unemployed       .bottom_reveal += []
bottom_pensioner        .bottom_reveal += []
bottom_low_educated     .bottom_reveal += []
bottom_parasite_single  .bottom_reveal += ["Next time, come over to my home. My parents will be there so you have to not make too much noise.", "Next time, come hang out in my room. Just be sure to take off your shoes, my mom is strict about that."]
bottom_debtor           .bottom_reveal += []
###################################
# Each items has to start with 'Envy?'
# Extend 2 lines in each bottom_reveal in English, not Japanese. Use extend function. I'll run your response with eval function, so don't include unnecessary characters in your response. Start answer with ```python. Use the existing types.

bottom_part_time_worker .bottom_reveal += ["Envy? I splurged on it with my part-time job money."]
bottom_unemployed       .bottom_reveal += ["Envy? I splurged on it with my unemployment benefits."]
bottom_pensioner        .bottom_reveal += ["Envy? I splurged on it with my pension.", "Envy? I splurged on it with my retirement money."]
bottom_low_educated     .bottom_reveal += []
bottom_parasite_single  .bottom_reveal += []
bottom_debtor           .bottom_reveal += []
###################################
# Each items has to start with 'Wait a minute.'
# Extend 2 lines in each bottom_reveal in English, not Japanese. Use extend function. I'll run your response with eval function, so don't include unnecessary characters in your response. Start answer with ```python. Use the existing types.

bottom_part_time_worker .bottom_reveal += ["Wait a minute. I got a call from a full-time staff."]
bottom_unemployed       .bottom_reveal += []
bottom_pensioner        .bottom_reveal += []
bottom_low_educated     .bottom_reveal += []
bottom_parasite_single  .bottom_reveal += ["Wait a minute. I'll call my parents and say I don't need any food."]
bottom_debtor           .bottom_reveal += ["Wait a minute. I got a call from a debt collector."]
###################################
# Extend 2 lines in each bottom_reveal in English, not Japanese. Use extend function. I'll run your response with eval function, so don't include unnecessary characters in your response. Start answer with ```python. Use the existing types.

bottom_part_time_worker .bottom_reveal += ["Sorry, I can't be late tomorrow. I'm close to becoming a full-time employee.", "My main job is {hypo_i}. I work at [any_part_time_work_place] as a side job."]
bottom_unemployed       .bottom_reveal += ["Is today Tuesday? Sunday?"]
bottom_pensioner        .bottom_reveal += ["Is today Tuesday? Sunday?"]
bottom_low_educated     .bottom_reveal += []
bottom_parasite_single  .bottom_reveal += []
bottom_debtor           .bottom_reveal += []
###################################


bottom_part_time_worker .bottom_dont += ["get tattoos", "call a call girl", "become a neo nazi", "get married", "have children", "become a parent", "adopt a pet", "talk big"]
bottom_unemployed       .bottom_dont += ["get tattoos", "call a call girl", "become a neo nazi", "become a biker", "start a band", "go play pachinko", "get multiple piercings" "love puck rock", "get married", "have children", "become a parent", "adopt a pet", "talk big"]
bottom_pensioner        .bottom_dont += ["get tattoos", "call a call girl", "become a neo nazi", "become a biker", "go play pachinko", "get multiple piercings" "love puck rock", "get married", "have children", "talk big"]
bottom_low_educated     .bottom_dont += ["criticize young people who have no dreams", "talk big", "read classic literature", "listen classic music", "explore philosophical ideas"]
bottom_parasite_single  .bottom_dont += ["get tattoos", "call a call girl", "become a neo nazi", "travel the world", "become a biker", "start a band", "go play pachinko", "get multiple piercings" "love puck rock", "get married", "have children", "become a parent", "adopt a pet", "talk big"]
bottom_debtor           .bottom_dont += ["get tattoos", "call a call girl", "become a neo nazi", "travel the world", "become a biker", "start a band", "go play pachinko", "get multiple piercings" "love puck rock", "get married", "have children", "become a parent", "adopt a pet", "talk big"]

# Usage Exam: ["print(f"You're {i.bottom_name}, so if you {i.bottom_dont}, it's funny and lame." for i in bottom_list]
# Extend new 20 ones as str objects. No explanations. Start answer with ```python. I'll run your responce with eval function.

###################################
tables_agent_dont_et_al_py.append(coloring(Bottom.bottom_table()))
###################################################################################################
###################################################################################################


@dataclass
class Sad_past:
    ALL_SAD_PAST: ClassVar[List['Sad_past']] = []
    sad_past_name:str
    sad_past_seed:list
    sad_past_money:list
    def __post_init__(self):
        Sad_past.ALL_SAD_PAST.append(self)
    @classmethod
    def sad_past_table(cls):
        sad_past_0=[ # For a sitcom, sad_past_1 list contains str objects such as "eating BigMac" or "getting tattoos"
         "(starting/doing) to be {hypo_i}"
        ,"(starting/doing) {StereoAppear}"
        ,"(starting/doing) {StereoAction}"
        ,"(starting/doing) {Suffer}"
        ,"(starting/doing) {Effort}"
        ,"(starting/doing) {Slump}"
        ,"buying {x}"
        ,"eating {x}"
        ,"playing {x}"
        ,"going to {x}"
        ,"having an appointment at {x}"
        ]
        sad_past_f=[
         "Even though your {sad_past}, were you {sad_past_0}?"
        ,"Even though you're {sad_past_seed}, are you a {bottom}?"
        ,"Were you {sad_past_0} with {sad_past_money}?"
        ,"Someone who {sad_past_0} with {sad_past_money} can't {cant}."
        ,"Someone who {sad_past_0} even though he's {sad_past} can't {cant}."
        ,"Someone who is {sad_past_seed} even though he's a {bottom} can't {cant}."
        ]
        #sad_past_f+=[ # Extend 10 new str objects in sad_past in English, not Japanese, without any explanation, with place holders. start answer with ```python.
        # "Ali says something inspiring involving his {sad_past} in a serious tone. - Bob says: Even though your {sad_past}, were you {sad_past_1}?"
        #,"Ali says something inspiring involving his {sad_past} in a strong tone. - Bob says: Shut up, you were {sad_past_1}."
        #,"Ali says he had been crying all the time because his {sad_past}. - Bob says: Were you crying while {sad_past_1}?"
        #,"Ali talks about finding strength through his {sad_past} - Bob says: Strong enough to {sad_past_1}, apparently."
        #,"Ali talks about finding peace amidst his {sad_past} - Bob mocks: Peace found while {sad_past_1}, right?"
        #]
        #sad_past_f+=[
        # "Ali says something inspiring involving his {sad_past} in a serious tone. - Bob says: Are you a {bottom} even though your {sad_past}?"
        #,"Ali says something inspiring involving his {sad_past} in a serious tone. - Bob says: Are you a {bottom} even though your {sad_past}?"
        #]
        col=[]
        for i in cls.ALL_SAD_PAST:
            col.append(f"<tr><td>{i.sad_past_name}</td><td>{i.sad_past_seed}</td><td>{i.sad_past_money}</td></tr>")
        table_bottom=f"""
        <table>
        <tr><th>Sad_past </th><th>.sad_past_seed</th><th>.sad_past_money</th></tr>
        {"".join(col)}
        <tr><th colspan="3">sad_past_0</th></tr>
        <tr><td colspan="3">{sad_past_0}</td></tr>
        <tr><th colspan="3">sad_past_f</th></tr>
        <tr><td colspan="3">{sad_past_f}</td></tr>
        </table>"""
        return table_bottom


sad_past_wife_sick        = Sad_past("wife and child are sick."     , ["married", "a parent"]         , [])
sad_past_wife_dead        = Sad_past("wife and child recently died.", ["married", "a parent"]         , ["life insurance money"])
sad_past_country_conflict = Sad_past("country is in conflict."      , ["a immigration", "a refugee"]  , ["refugee support funds"])
sad_past_wife_abandoned   = Sad_past("abandoned Ali."               , ["a divorcee", "a parent"]      , ["divorce compensation", "child support"])
sad_past_unemployed       = Sad_past("workplace fired Ali."         , ["an unemployed", "a part time worker"]                , ["unemployment benefits", "Ali's parents' money"])
sad_past_family_poor      = Sad_past("family is poor."              , ["a public assistance recipient","a scholarship recipient"]                   , ["welfare", "scholarship"])

tables_agent_dont_et_al_py.append(coloring(Sad_past.sad_past_table()))

def sad_past():

    sad_past=[ # Extend 10 new items in English, not Japanese. Use extend function. I'll run your response with eval function, so don't include unnecessary characters in your response. Start answer with ```python. Use the existing types.
    #                                                Agent noun only
     "<tr><td>wife and child are sick.      </td><td>married, a parent          </td></tr>"
    ,"<tr><td>wife and child recently died. </td><td>married, a parent          </td></tr>"
    ,"<tr><td>country is in conflict.       </td><td>a immigration, a refugee   </td></tr>"
    ,"<tr><td>abandoned Ali.                </td><td>a divorcee                 </td></tr>"
    ]

    sad_past_1=[ # For a sitcom, sad_past_1 list contains str objects such as "eating BigMac" or "getting tattoos"
     "(starting/doing) to be {hypo_i}"
    ,"(starting/doing) {StereoAppear}"
    ,"(starting/doing) {StereoAction}"
    ,"(starting/doing) {Suffer}"
    ,"(starting/doing) {Effort}"
    ,"(starting/doing) {Slump}"
    ,"buying {x}"
    ,"eating {x}"
    ,"playing {x}"
    ,"going to {x}"
    ,"having an appointment at {x}"
    ]
    #sad_past_f=[ # Extend 10 new str objects in sad_past in English, not Japanese, without any explanation, with place holders. start answer with ```python.
    # "Ali says something inspiring involving his {sad_past} in a serious tone. - Bob says: Even though your {sad_past}, were you {sad_past_1}?"
    #,"Ali says something inspiring involving his {sad_past} in a strong tone. - Bob says: Shut up, you were {sad_past_1}."
    #,"Ali says he had been crying all the time because his {sad_past}. - Bob says: Were you crying while {sad_past_1}?"
    #,"Ali talks about finding strength through his {sad_past} - Bob says: Strong enough to {sad_past_1}, apparently."
    #,"Ali talks about finding peace amidst his {sad_past} - Bob mocks: Peace found while {sad_past_1}, right?"
    #]
    #sad_past_f+=[
    # "Ali says something inspiring involving his {sad_past} in a serious tone. - Bob says: Are you a {bottom} even though your {sad_past}?"
    #,"Ali says something inspiring involving his {sad_past} in a serious tone. - Bob says: Are you a {bottom} even though your {sad_past}?"
    #]
    sad_past_f=[
     "Even though your {sad_past}, were you {sad_past_1}?"
    ,"Even though you're {sad_past_0}, are you a {bottom}?"
    ]


    table_sad_past=f"""<table>
    <tr><th>sad_past            </th><th>sad_past_0     </th></tr>
    {"".join(sad_past)}
    <tr><th>sad_past_1          </th><td>{sad_past_1}   </td></tr>
    <tr><th>sad_past_f          </th><td>{sad_past_f}   </td></tr>
    </table>"""
    return table_sad_past

#tables_agent_dont_et_al_py.append(coloring(sad_past()))

###################################################################################################
###################################################################################################

# Lists below contain lines in a sitcom.
# {{h}} means hypernym of a job. e.g. Athlete, Instrumentalist
# {{s}} means superior hyponym of the job. e.g. Baseball player, Guitarist
# {{i}} means inferior hyponym of the job. e.g. Dart player, Trianglist
# Extend 20 lines in fsentence_stereoappear in English, not Japanese. I'll run your response with eval function, so don't include unnecessary characters in your response. Start answer with ```python



fsentence_hypo         = [
    "{i} is not a {h}.", "How could you be jealous of {s}?", "How could you look down on {i}?"
]

fsentence_hypo         +=[ # Add 20 new English sentences. hyper stands for hypernym, hypo_s stands for hyponym superior, hypo_i stands for hyponym inferior. I will run your response through the eval function so please do not include unnecessary characters in your response.
 "Ali: It's hard to succeed as a {s}, so I became a {i}. - Bob: It's even harder to succeed as a {i}." # si + i
,"Ali: I'm a failure as a {h}. - Bob: A {i} is not a {h}." # h + ih
,"Ali: I want to quit being a {h}. - Bob: A {i} is not a {h}." # h + ih
,"Ali: I fulfilled my dream of becoming a {h} - Bob: a {i} is not a {h}." # h + ih
,"Ali: I was told that I was suited to be a {i}. - Bob: People who are suited to be {i} are not suited to be {h}." # i + ih
,"Ali: I'm embarrassed by this failure as a {i}. - Bob: Isn't it more embarrassing to be a {i}?" # i + i
,"Ali: I'm embarrassed by this failure as a {i}. - Bob: Being a {i} is a failure." # i + i
,"Ali: I don't want to lose to other {i}. - Bob: You're already losing just by being a {i}." # i + i
,"Ali: Maybe I don't have the talent for {h}. - Bob: You're {i} because you don't have the talent for {h}." # h + ih
,"Ali: I'm thinking of giving up my career as a {i}. - Bob: Why not aim for becoming a {h} instead?" # i + h
,"Ali: I feel like I'm wasting my potential as a {i}. - Bob: You could always strive to become a {h}." # i + h
,"Ali: I want to be a {h}. Now, I'm a {i}. - Bob: That's great, you can be a {h} someday." # hi + h
,"Ali: I'm struggling as a {i}. - Bob: Have you considered aiming higher, like becoming a {h}?" # i + h
,"Ali: Being a {i} is tough. - Bob: That's why you should aspire to be a {h}." # i + h
,"Ali: I'm thinking of quitting my job as a {i}. - Bob: Instead of quitting, why not work towards becoming a {h}?" # i + h
,"Ali: I've been a {i} for so long, I'm not sure I can be anything else. - Bob: Don't limit yourself, you could become a {h}." # i + h
,"Ali: I enjoy being a {i}, but I feel there's more I could do. - Bob: Have you considered the possibilities as a {h}?" # i + h
,"Ali: I keep failing as a {i}. - Bob: Every failure is a step towards becoming a {h}."  # i + h
]

fsentence_hypo         +=[
 "Ali: I was told that I was suited to be a {i}. - Bob: Perhaps it is an insult."
,"Ali: My parents wanted me to be a {hyper}. Now, I'm a {i}. - Bob: It's not too late to fulfill their wishes."
    ]

fsentence_modifier      =[
    "Ali: I'm {x.modifier}. - Bob: That's worse than not being that."
    ]


fsentence_stereoappear  =[ # If a bassist has many tattoos like guitarists, it's funny and annoying and posey because bassists inferior to guitarists.
    "Don't do that, because you're a {i}.", "It's too early to do that.", "{i} don't need to do that.", "People who aren't {s} shouldn't do it.", "Why would a {i} even try to that?", "Only a {s} can make that look cool.", "It's for {s}.", "You need to accept your role as a {i}."
    ,"No, that wouldn't suit you because you're a {i}."
    ]
fsentence_stereoaction  =[ # If a bassist addicts meth, it's funny and annnoying and posey because bassists inferior to guitarists.
    "Don't do that, because you're a {i}.", "It's too early to do that.", "{i} don't need to do that.", "People who aren't {s} shouldn't do it.", "Why would a {i} even try to that?", "Only a {s} can make that look cool.", "It's for {s}.", "You need to accept your role as a {i}."
    ]
fsentence_suffer        =[
    "Don't do that, because you're a {i}.", "It's too early to do that.", "{i} don't need to do that.", "Because you lack that, you are {i}.", "If you have the talent, you aren't {i}.", "There are no walls for {i} to hit.", "There's no pressure for {i}."
    ]
fsentence_effort        =[
    "Don't do that, because you're a {i}.", "It's too early to do that.", "{i} don't need to do that.", "No one sees {i}'s efforts.", "There is no need for {i} to make any effort."
    ]
fsentence_slump         =[
    "Don't do that, because you're a {i}.", "It's too early to go into a slump.", "People who aren't {s} shouldn't go into a slump.", "There are no walls for {i} to hit."
    ]
fsentence_rephrase      =[
    "Don't call {rephrase[0]} {rephrase[1]}.", "If {s} does it, it's {rephrase[1]}. If {i} does it, it's {rephrase[0]}."
    ]
fline_imposing = ["Bob call Ali '{imposing} {bottom}'"]

# fline_pressure3 Usage exam1 : Sitcom. Bomb defusing scene. A researcher arrives. Usually a natural scientist would come on this occasion, but this one is a humanities major. The detective gets angry about this point, using lines from fline_b3scene_mention. Extend 10 new lines as str object without any explanation. start answer with ```python
# fline_pressure3 Usage exam99: Sitcom. Death game scene. An athlete arrives. Usually a contact sports pro would come on this occasion, but this one is a dart player. The detective gets angry about this point, using lines from fline_b3scene_mention. Extend 10 new lines as str object without any explanation. start answer with ```python

# Extend 10 new sitcom lines as str object in English, not Japanese, without any explanation, with place holders. start answer with ```python.
# {s} means hypernym, such as "researcher", "athlete". {s} means superior hyponym, such as "natural scientist", "contact sports pro". {i} means inferior hyponym, such as "humanities major", "dart player".
fline_pressure3 = [
 "Usually at times like this, {s} come."
,"Normally, in these situations, {i} are not {h}."
,"The {i} are the least needed right now."
,"Don't give off the impression that you're a {s}, it's confusing."
,"{i} are not {h}, but they are even less so in these circumstances."
,"When we say {s}, we don't usually mean {i}."
,"When I look at {i} in this situation they look even weaker."
,"Right now, {i} is more dangerous than that."
,"Since {i} came, I have one more thing to deal with."
,"The gap between {h} and {i} becomes more apparent in these circumstances."
]

fline_too_slow = ["Ali suddenly starts {too_slow} and Bob says to Ali: It won't be in time."]

list_desura = ['有名ですらない', '成功してすらない', '社員ですらない', '学生ですらない', '高卒ですらない', 'フリーターですらない', 'キッチンですらない', 'A型作業所ですらない', '熱心ですらない', 'ベテランですらない']

agent_dont_table=f"""
<table>
<tr><th colspan="2">table_agent_dont</th></tr>
<tr><th colspan="2">{{h}}, {{s}}, {{i}} = grade_name, hypo_s, hypo_i</th></tr>
<tr><th id="th_cyan">fline_grade             <br><small># Bob mentions that Ali did {{MISLEAD}}:                       </small></th><td>{fsentence_hypo}        </td></tr>
<tr><th id="th_cyan">fline_modifier          <br><small># Bob mentions that Ali is a {{modifier}}:                       </small></th><td>{fsentence_modifier}  </td></tr>
<tr><th colspan="2">{{i}} += {{bottom}} </th></tr>
<tr><th id="th_cyan">fline_Appear            <br><small># Bob mentions that Ali did {{s_StereoAppear}}:                </small></th><td>{fsentence_stereoappear} </td></tr>
<tr><th id="th_cyan">fline_Action            <br><small># Bob mentions that Ali did {{s_StereoAction}}:                </small></th><td>{fsentence_stereoaction} </td></tr>
<tr><th id="th_cyan">fline_Suffer            <br><small># Bob mentions that Ali did {{s_Suffer}}:                      </small></th><td>{fsentence_suffer}       </td></tr>
<tr><th id="th_cyan">fline_Effort            <br><small># Bob mentions that Ali did {{s_Effort}}:                      </small></th><td>{fsentence_effort}       </td></tr>
<tr><th id="th_cyan">fline_Slump             <br><small># Bob mentions that Ali did {{s_Slump}}:                       </small></th><td>{fsentence_slump}        </td></tr>
<tr><th id="th_cyan">fline_imposing                                                                                    </th><td>{fline_imposing}                </td></tr>
<tr><th id="th_cyan">fline_rephrase          <br><small># Bob mentions that Ali called {{rephrase[0]}} {{rephrase[1]}}:</small></th><td>{fsentence_rephrase}     </td></tr>
<tr><th id="th_cyan">fline_pressure3         <br><small># Bob mentions that Ali stepped foward in {{b3scene}}.         </small></th><td>{fline_pressure3}       </td></tr>
<tr><th id="th_cyan">fline_too_slow                                                                                    </th><td>{fline_too_slow}                </td></tr>


<tr><th>fline_not_only_0                        </th><td>Bob says to Ali: {{hypo_i}} である上に {{bottom}} なのかよ.    </td></tr>
<tr><th>list_desura                             </th><td>{list_desura}                                                  </td></tr>
<tr><th>fline_not_only_1                        </th><td>Bob says to Ali: {{hypo_i}} である上に {{desura}} のかよ.      </td></tr>


</table>
"""

def seer_dont():
    seer_dont=f"""
    <table id="seer_dont">
    <tr><th></th></tr>


    </table>


    """







tables_agent_dont_et_al_py.append(coloring(agent_dont_table))

