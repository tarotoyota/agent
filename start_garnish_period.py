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

'''
** 文の役割, およびline仕事量 **
netaAIの運用において, 全ての台詞(英: line)は以下の11種の内いずれかの役割(英: role)を持つ.
- SEED                  TLMのための伏線.
- REAP                  TLMのための伏線の回収.
- OPENER                つかみ. OPENERかつSEED可能なlineも存在する.
- CLOSER                オチ. CLOSERかつREAP可能なlineも存在する.
- PERSONALITY_ASSIGN    Aliがそのコントにおいて必要とする性格をassignするためのline.
- STEREO_ASSIGN         Aliがそのコントにおいて必要とするStereo objectをassignするためのline.
- PRESSURE_ASSIGN       Aliがそのコントにおいて必要とするPressure objectをassignするためのline.
- REVEAL                バラシ.
- SILENT                バラシの前の沈黙.
- FILLER                上記の各lineを発生させるための整合性をassignするためのline. 少ない方がよい.
- NONEROLE              roleを持たない台詞. 少ない方がよい.
複数のroleを持つ1つのlineは"a multiple role line"と呼ばれる.
複数のroleを1つのlineが持つ状態は"line仕事量が高い(英: line workload is high)"と形容される.

netaAIの運用においては, いかに早くREVEALを実行し, いかにBEFORE REVEALに大量のSEEDを実装するかが重視される.
    netaAIは, tiktokやyoutubeで広告収益を得るためのツールとして設計されており, よって動画を途中で離脱する視聴者を最小化する必要がある.
    netaAIは, バラシまで1分あるようなネタを我慢して見続けられるお笑いオタクだけを顧客にする事を想定して設計されていない.

[netaAI: 影響]のBEFORE REVEALにはNONEROLE lineが存在しない.

Agent.garnishallowにおいては, 各Agentインスタンスのステレオタイプな性格をx blank binary形式でデータ化している.
    Athleteは、創作物でしばしば傲慢(英: arrogance)な人物として描写されるAgentである. よってathlete.garnishallow.arroganceは"y"である。
        よってathleteインスタンスは、ARROGANCEというタグが付与されたGarnishオブジェクトの使用が許可(英: allow)される。
'''





reldam_dict={
 "child_damage":[
             "'s child is trying to become a counselor"
            ,"'s child is short/ has stopped growing"
            ,"'s child became independent so early"
            ,"'s child often stay at school late"
            ,"'s child is interested in politics"
            ,"'s child is interested in trains"
            ,"'s child likes animals more than people"
            ,"'s child loves volunteering"
            ,"'s child doesn't cry at all"
            ,"'s child is extremely strict about rules"
            ,"'s child often plays with younger children"
            ,"'s child never had a rebellious phase"
            ,"'s child is an avid reader beyond their years"
            ,"'s child is obsessed with cleanliness"
            ,"'s child is overly mature for their age"
            ,"'s child has an unusually strong sense of justice"
            ,"'s child is always eager to help others"
            ,"'s child is excessively quiet"
            ,"'s child is obsessed with cleanliness"
            ]
,"wife_damage":[
             "wife_damage 1"
            ,"wife_damage 2"
            ]
,"parent_damage":[
             "parent_damage 1"
            ,"parent_damage 2"
            ]
}


# 東北に住んでる奴がハットかぶるなよ



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
            <tr><th id="th_lime" colspan="2">{i.name}</th><td>{i.template}</td></tr>
            {trigger_col}
            {special_rows}
            {exam_col}
            {exam_rows}
            <tr><th>TAG</th><td colspan="2">{i.tag}</td></tr>
            </table>
            """

        return garnish_table_result




"""
キムデジュンマスク
キムデジュンスピーク
　イノシカチョウ(M1 2024 三回戦)


"""

########################################################################
### SAD_PAST ###########################################################

def nanamagari():
    template_col = []
    template=[ # This function is for creating comedy. Ali is a madman.
    """<pre>
bob_general_purpose_text = ['Now I understand why you {SadPast.be_divorced}.', 'I think there is another reason why you {SadPast.be_divorced}.', 'In the first place, how could you {SadPast.get_married}?']

fex1  = ['Ali: {SadPast.a_line} +l+ Bob: {bob_general_purpose_text}']
fex2  = ['Ali: {SadPast.alimony + Garnish.dirty_money.Z} +l+ Bob: [Don't use that money for [{Agent.action}, {Agent.appear}, {Agent.suffer}, {Agent.effort}, {Agent.pressure4}] +f+ Bob: {bob_general_purpose_text}']
fex3  = ['Bob: I think your abnormality is not caused (only) by you {SadPast.be_divorced}. +f+ Bob: {bob_general_purpose_text}']
fex4  = ['Bob: Even though {SadPast.be_divorced}, did you {er_coffee.Z}. +f+ Bob: {bob_general_purpose_text}']
fex5  = ['Ali: I do {Agent.charity} for the {SadPast.orphanage} where I used. +l+ Bob: Don't do that. +f+ Bob: {bob_general_purpose_text}']
fex6  = ['Bob: What keeps you going as a {hypo_i}? +s+ Ali: I {SadPast.be_divorced}. To overcome this adversity, for people in the same situation. +s+ Bob: Why there's a decent reason for that? +f+ Bob: {bob_general_purpose_text}']
    </pre>"""
        ]
    for i in template:
        template_col.append(f"<tr><td colspan='5'>{i}</td></td>")

    exam_col = []
    exam=[
         ["ザ・マミィ", "小倉ｰ共有ｰ", "どうやってあんなかわいい彼女作ったの"]
        ,["ななまがり", "", "この男、結婚している"]
        ,["老害マックス", "M-1 2024 3回戦", "結婚してる"]
        ]
    for i in exam:
        exam_col.append(f"<tr><td>{i[0]}</td><td>{i[1]}</td><td>{i[2]}</td></tr>")

    item_col = []
    @dataclass
    class SadPast:
      ALL_SADPAST: ClassVar[List['SadPast']] = []
      be_divorced:str
      alimony:list # Their cost
      get_married:list # Their success before their sad past
      orphanage:list # A community they will appreciate
      a_line:list # The speaker refers to {self.be_divorced} in a self-blaming or arrogant manner. Each item has to contain "{hypo_i}". hypo_i means the speaker's job.
      def __post_init__(self):
          SadPast.ALL_SADPAST.append(self)
    be_divorced             =SadPast("be divorced"              ,["divorce alimony"]                                    ,["get married"]                                          ,[]                                 ,["After my divorce, I realized that married life for a {hypo_i} is difficult.", "Relationships are a distraction from my {hypo_i} goals.", "{hypo_i} can't afford to prioritize their family.", "The stress of being {hypo_i} ruined my marriage."])
    be_an_orphan            =SadPast("be an orphan"             ,[]                                                     ,["find a foster parent"]                                 ,["orphanage"]                      ,["I had to become a successful {hypo_i} to prove the orphanage wrong.","My lack of parents pushed me to excel as a {hypo_i}, unlike those with comfortable upbringings.",])
    be_kicked_off_the_team  =SadPast("be kicked off the team"   ,["unemployemnt benefit"]                               ,["join the team"]                                        ,[]                                 ,["The team couldn't handle my {hypo_i} ambitions.", "The conservative {hypo_i} team couldn't stand my innovation.", "The team activities were holding back my {hypo_i} potential."])
    ones_son_is_a_delinquent=SadPast("one's son is a deliquent" ,["Bail money", "attorney fees", "settlement money"]    ,["get married"]                                          ,[]                                 ,["It's an important time to be a {hypo_i}, I don't care about my son's delinquency.", "{hypo_i}s can't be bothered with family drama.", "A {hypo_i} can't waste energy on wayward offspring.", "My son's behavior is irrelevant to my {hypo_i} success."])
    ones_wife_is_sick       =SadPast("one's wife is sick"       ,["medical expenses", "life insurance benefits"]        ,["get married"]                                          ,["hospital"]                       ,["It's an important time to be a {hypo_i}, I can't afford to worry about my wife's illness.", "{hypo_i}s can't let personal issues affect their performance.", "The {hypo_i} life leaves no room for playing nurse."])
    be_dumped               =SadPast("be dumped"                ,[]                                                     ,["get the girlfriend"]                                   ,[]                                 ,["After getting dumped, I realized that love is difficult for {hypo_i}.", "Relationships are a distraction from my {hypo_i} goals.", "{hypo_i} can't afford to prioritize their lover.", "Being dumped was a blessing; now I can focus on being {hypo_i}.", "{hypo_i}s are better off single and focused.", "Being dumped showed me that {hypo_i}s should avoid relationships."])
    be_bullied              =SadPast("be bullied"               ,[]                                                     ,["join the team"]                                        ,["free school"]                    ,["I used my experience of bullying as a springboard to become {hypo_i}.", "As {hypo_i}, I thank my bullies for the motivation.", "Bullying toughened me up for the {hypo_i} world."])
    be_abused               =SadPast("be abused"                ,[]                                                     ,[]                                                       ,["children's shelter"]             ,["I used my experience of abusing as a springboard to become {hypo_i}.", "Being an abuse survivor prepared me for the harsh {hypo_i} world."])
    be_fired                =SadPast("be fired"                 ,["unemployemnt benefit"]                               ,["get the job"]                                          ,["soup kitchen","homeless shelter"],["I used my experience of abusing as a springboard to become {hypo_i}.", "Being an abuse survivor prepared me for the harsh {hypo_i} world."])
    be_arrested             =SadPast("be arrested"              ,["Bail money", "attorney fees", "settlement money"]    ,["pass the parole review"]                               ,["prison"]                         ,["The arrest was a publicity stunt for my {hypo_i} career.", "I saw my mugshot as a {hypo_i} headshot opportunity.", "My arrest record is just part of my {hypo_i} origin story."])
    declare_bankruptcy      =SadPast("declare bankruptcy"       ,["Debt consolidation fees", "Credit counseling costs"] ,["pass the loan screening"]                              ,["soup kitchen","homeless shelter"],["Bankruptcy was my first step to becoming a successful {hypo_i}.", "I saw bankruptcy as an investment in my future as a {hypo_i}.", "Losing it all showed me I had nothing to lose in pursuing {hypo_i}.", "Declaring bankruptcy freed me from the shackles holding back my {hypo_i} potential.", "Financial ruin was the push I needed to fully commit to being a {hypo_i}."])
    drop_out_of_college     =SadPast("drop out of college"      ,["Tuition reimbursement", "Student loan payments"]     ,["pass the entrance exam", "pass the scholarship Review"],[]                                 ,["College was holding back my true potential as a {hypo_i}.", "Dropping out was the best decision for my {hypo_i} career.", "Real-world experience beats a degree for a {hypo_i}.", "I realized being a {hypo_i} doesn't require formal education.", "College couldn't keep up with my {hypo_i} aspirations.", "Leaving college freed me to focus on my {hypo_i} goals.", "As a {hypo_i}, I learn more on the streets than in a classroom.", "College was too slow-paced for my {hypo_i} ambitions.", "I dropped out to start my {hypo_i} empire immediately.", "Who needs a degree when you're born to be a {hypo_i}?"])
    be_mixed                =SadPast("be mixed"                 ,[]                                                     ,[]                                                       ,[]                                 ,["I blame my cultural confusion for my occasional missteps as a {hypo_i}.","My mixed heritage is both a blessing and a curse in the {hypo_i} profession.","As a mixed-race individual, I'm naturally better at adapting to different {hypo_i} environments.","Being mixed means I have to work twice as hard to prove myself as a competent {hypo_i}.",])
    be_poor                 =SadPast("be poor"                  ,["debt payments", "payday loans"]                      ,[]                                                       ,["soup kitchen","homeless shelter"],["My {hypo_i} success proves that poverty is just a mindset.","Being poor taught me to be a ruthless {hypo_i}.","Unlike others, I didn't let poverty stop me from becoming a successful {hypo_i}.","My {hypo_i} achievements show that handouts are unnecessary for success."])

    for i in SadPast.ALL_SADPAST:
        item_col.append(f"<tr><td>{i.be_divorced}</td><td>{i.alimony}</td><td>{i.get_married}</td><td>{i.orphanage}</td><td>{i.a_line}</td></tr>")

    result = f"""
        <table id="SadPast">
        <tr><th colspan="5" id="th_lime">SadPast        </th></tr>
        <tr><th colspan="5">template                    </th></tr>
        {''.join(template_col)}
        <tr><th>.be_divorced</th><th>.alimony</th><th>.get_married</th><th>.orphanage</th><th>.a_line</th></tr>
        {''.join(item_col)}
        <tr><th>USER</th><th>SKETCH NAME</th><th>EXPRESSION</th></tr>
        {''.join(exam_col)}
        <tr><th>TAG</th><td>JOKELESS_TLM, JOKE_TLM, AtoB, ASSIGN_AGENT, ASSIGN_PERSONALITY, OPENER, SAD_PAST</td></tr>
        </table>
        """
    return result
tables.append(coloring(nanamagari()))




different_reason = Garnish(
    name="different_reason"
    ,tag="JOKELESS_TLM, SAD_PAST"
    ,template=[ # In a sitcom, Bob says these lines to a madman.
               "Ali: Am I weird? Sorry, I {Z}. -> Bob: I think your abnormality is not caused (only) by that."
              ]
    ,special ={
               "Z":[
                   "be having ADHD", "be a child of a single parent", "be LGBT", "be a boomer", "be mixed", "be returnee", "be adopted", "be an only child", "be having a high IQ", "be having strict parents", "be growing up in poverty","be having depression", "be gifted"
                   ] #  Extend new 20 expressions in this list in python in English. Align the text with the existing objects.
              }
    ,exam    =[
               ["かもめんたる", "未来人", "未来人ってだけじゃねーだろ"]
              ,["キングオブコメディ", "お見合い", "思春期ってだけじゃないだろ"]
              ]
              )
er_coffee=Garnish(
    name="er_coffee"
    ,tag="BtoA, JOKELESS_TLM, SAD_PAST"
    ,template=["Bob: Even though {SadPast.be_divorced}, did you {Z}"
              ,"Bob: Even though {SadPast.be_divorced}, why you could {Z}"
              ]
    ,special ={
               "Z" :["eat a Big Mac? A hamburger or chicken crisps are okay, but a Big Mac is crossing the line."
                    ,"drink juice? Water is the best. Coffee is still acceptable."
                    ,"buy sneakers? In that situation, why were you able to say, 'Do you have these shoes in E4?'"
                    ,"buy sneakers? Did you look at your eyes in the full-length mirror?"
                    ,"dye your hair? How did you feel while having your hair dyed?"
                    ,"get a tattoo? How did you feel while getting a tattoo?"
                    ,"learn a new language? How did you feel when you turned over the flashcard?"
                    ,"renovate your kitchen? I want to see the look on your face when you're thinking about the kitchen flow line."
                    ,"learn to play a musical instrument? Was it 'Twinkle Twinkle Little Star' or 'Do-Re-Mi'?"
                    ,"go on a shopping spree? Did you really need that third pair of sunglasses?"
                    ,"join a gym? Were you more focused on your biceps or your conscience?"
                    ,"go skydiving? How did you feel when the parachute opened?"
                    ,"watch a movie? Did you choose the one with the happy ending?"
                    ]# Extend new 10 sentences. Just mimic the existing items. I will run your response through the eval function so please do not include unnecessary characters in your response. Start answer with ```python
              }# Usage exam ; Bob: Even though your wife dead, did you eat a Big Mac? A hamburger or chicken crisps are okay, but a Big Mac is crossing the line.
    ,exam=    [
               ["うしろシティ", "病院", ""]
              ]
              )
dirty_money = Garnish(
    name="dirty_money"
    ,tag="AtoB, OPENER, JOKE_TLM, JOKELESS_TLM, SAD_PAST"
    ,template=[
        "Ali: {Z}"
              ]
    ,special= {
         "Z": [# Extend new 20 X in python without any explanations. Respond with only new items. It's for a sitcom.
               "I feel like the ATMs are slow when I use them to withdraw {W}"
              ,"I don't like people seeing my face when I withdraw {W}"
              ,"{W} I withdrew from the ATM feels hot"
              ,"George Washington in {W} seems to be smiling more than usual"
              ,"What kind of expression should I make when I withdraw {W}?"
              ,"I feel like the food I buy with {W} really makes its way into my body"
              ,"When I spin the slot machine with {W}, I feel like the jugglers are smiling more than usual."
              ,"Withdrawing {W} feels like I'm playing Monopoly"
              ,"I always do a fake cough to cover the sound of counting {W}"
              ,"The self-checkout machine seems to announce my purchases louder when I pay with {W}"
              ,"The clothes I bought with {W} feel like they stick to my skin."
              ,"It seems like the letters related to the {W} in the bankbook appear in bold."
              ,"I wonder what I look like when I pay {W} to Tinder."
              ,"I wash my hands after handling {W}"
              ,"The milk I buy with {W} seems creamier."
              ,"The ATM seems to be noisier than usual when I withdraw {W}."
              ,"I feel like the ATMs are slow when I use them to pay {W}"
              ,"I don't like people seeing my face when I pay {W}"
              ,"What kind of expression should I make when I pay {W}?"
              ]
              }
              )
and_not_ali=Garnish(
    name="and_not_ali"
    ,tag="BtoA, JOKELESS_TLM, SAD_PAST"
    ,exam=    [
               ["キングオブコメディ", "いじめられっ子", "なんで君がいじめらんなかったの?"]
              ]
    ,template=["Bob: Why was he {X} and not Ali?" # In a sitcom, Ali is a madman.
              ]
    ,special ={"X" :["bullied"
                    ,"fired"
                    ,"arrested"
                    ,"scolded"
                    ]
                    }
                    ) # I lost my friend by bulliyng.






########################################################################
###       ##############################################################

different_genre = Garnish(
    name="different_genre"
    ,tag="JOKELESS_TLM, INSULTING_AGENT_NOUN"
    ,exam=[
           ["かもめんたる", "砂浜店長", "もう怒るのが遅いとかじゃない"]
          ]
    ,template=[ # In a sitcom, Bob says these lines to Ali, a madman. Ali is so crazy that he no longer belongs to the categories of "harasser" or "Grumpy."
               "Ali: Am I {Z}? - Bob: You're in a different category from the {Z}"
              ,"Ali: Lately I've been turning into {Z}. - Bob: You're in a different category from the {Z}."
              ,"Ali: Shut up, I'm not {Z}. - Bob: You're in a different category from the {Z}."
              ,"Ali: You might think I'm {Z}, but... - Bob: You're in a different category from the {Z}."
              ,"Ali: I don’t want to be seen as {Z}. - Bob: You're in a different category from the {Z}."
              ,"Ali: Why do people assume I'm {Z}? - Bob: You're in a different category from the {Z}."
              ,"Ali: What if I really am just {Z}? - Bob: You're in a different category from the {Z}."
              ] #  Extend new 20 expressions in this list in python.
    ,special ={
               "Z":[
                   "power harasser", "Grumpy", "too stoic", "sexual harasser", "newbie", "unfit", "Kevin/ Karen", "micromanager"
                   ] #  Extend new 20 expressions in this list in python.
              }
              )








########################################################################
### agree ##############################################################
agree_make_smile = Garnish(
    name="agree_make_smile"
    ,tag="JOKELESS_TLM, AGREE"
    ,template=["Ali: I wanna {X}. -(lag)-> Bob: But you managed to {X}."
              ,"Others says that Ali {X} -(lag)-> It's revealed that the reason others make such comments is sarcastic."
              ]
    ,special ={"X": [ # In (lag), Ali failed at something in his activity. Bob sarcastically criticizes Ali for his failure. Extend new 20 expressions in this list in python in English. This list is for creating comedy. Only add generic expressions that can be used no matter what "something" or "his activity" is. All of the statements in the list can describe either good or bad phenomena.
                     "make everyone smile" # This means that Ali was mocked.
                    ,"be famous" # This means that Ali became famous in a bad way.
                    ,"make everyone cry" # This means that Ali made everyone cry in a bad way.
                    ,"surprise everyone" # This means that Ali surprised everyone in a bad way.
                    ,"be unforgettable"  # This means Ali was memorable for all the wrong reasons # GPT4
                    ,"make history"  # This means Ali made history for something embarrassing # GPT4
                    ,"make my mark"  # This means Ali made a mark in an embarrassing way. # GPT4
                    ,"show what I'm capable of"  # Could reveal strengths or weaknesses #gpt4
                    ,"change the game"  # Could change things for better or worse #gpt4
                    ,"steal the spotlight"  # Could be for impressive or embarrassing reasons #gpt4
                    ,"be the center of attention"  # Could get positive or negative attention #gpt4
                    ,"set an example"  # Could be a good example or a cautionary tale #gpt4
                    ,"go to a different position"
                    ,"change the size of my salary"
                    ,"make a difference"  # Ali made a difference in a negative way. #Claude
                    ,"make my presence felt"  # Could be positive or negative impact #GPT4
                    ,"rewrite the rules"  # Could improve or worsen the situation #GPT4
                    ,"have social influence"
                    ]
                    } # 俺が逮捕される事で少しでも社会がよくなれば
                    )
agree_only = Garnish(
    name="agree_only"
    ,tag="JOKELESS_TLM, AGREE, HIGH_PRIDE"
    ,template=["Ali: Why {X}?. -(lag)-> Ali: Why {X}?. -> Bob: I agree."
              ]
    ,special ={"X": [# Ali is a self-respecting man. Extend new 20 expressions in this list in English without any explanations. This list is for creating comedy.
                     "is my reward 500 dollars" # Ali says this line to mean that it's too cheap, and Bob agrees sarcastically that it's too expensive for Ali.
                    ,"is the venue so shabby" # Ali says this line to mean that the venue is too shabby, and Bob agrees sarcastically that the venue is too fancy for Ali.
                    ,"am I stuck at the third round" # Ali complains about only making it to the third round, and Bob sarcastically agrees that it's strange that Ali even made it to the third round.
                    ,"was I just nominated and didn't win" # Ali complains that she was only nominated and did not win, and Bob sarcastically agrees that it is unusual for Ali to have been nominated.
                    ,"are there 100 fans at the meet-and-greet"
                    ,"did they give me a four-star hotel instead of five"
                    ,"did they offer me a supporting role instead of lead"
                    ,"are there two bodyguards assigned to me"
                    ]
                    }
                    )
agree_one_sided = Garnish(
    name="agree_one_sided"
    ,tag="JOKELESS_TLM, AGREE, HIGH_PRIDE"
    ,template=["Ali: {X}. - Bob: I agree. Thanks to you."
              ]
    ,special ={"X" :[ # In a sitcom, competent Bob agrees with the line {X} uttered by the incompetent Ali. # For Ali, lines in X are true given that they win, and for Bob, it is true given that they lose.
                     "It will be one-sided" # For Ali, this line is true given that they win, and for Bob, it is true given that they lose.
                    ,"The gap will continue to widen"
                    ,"The balance of power was upset"
                    ,"The winner and loser are now decided"
                    ,"This match is already over"
                    ,"It's not even going to be close"
                    ,"It's going to be a landslide win"
                    ,"Can we keep this gap?"
                    ,"Are we safe with this advantage?"
                    ,"Should we play defensively now?"
                    ,"This victory is practically guaranteed"
                    ,"The tide has turned irreversibly"
                    ] # Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
                    }
                    )
agree_different_levels = Garnish(
    name="agree_different_levels"
    ,tag="JOKELESS_TLM, AGREE, HIGH_PRIDE"
    ,template=["Ali: {X}. - Bob: I agree."
              ]
    ,special ={"X" :[ # In a sitcom, competent Bob agrees with the line {X} uttered by the incompetent Ali. # For Ali, lines in X are true given that Ali is superior to Bob, and for Bob, it is true given that Ali is inferior to Bob.
                     "You and I are on different levels" # For Ali, this line is true given that Ali is superior to Bob, and for Bob, it is true given that Ali is inferior to Bob.
                    ,"You and I are doing different things"
                    ,"Our approaches are worlds apart"
                    ,"We're not even in the same league"
                    ,"Our skills are on completely different planes"
                    ,"You can't compare your work to mine"
                    ,"We're operating in different dimensions"
                    ,"You're playing a different game"
                    ,"As we speak, the gap between us is widening"
                    ] # Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
                    }
                    )
found_it_easy = Garnish(
    name="found_it_easy"
    ,tag="AtoB, JOKELESS_TLM, HIGH_PRIDE"
    ,template=["Ali: {X}. - Bob: It's because you're {hypo_i}."
              ] # hypo_i means a easy job.
    ,special ={"X" :[ # In a sitcom, Ali, who has an easy job, says {X} to boast about one's abilities. Bob points out that it's because Ali has an easy job, not because Ali is competence. Each line has to contain "hardly" or "rarely".
                     "I've hardly ever been told I am bad at it"
                    ,"I've hardly ever made a mistake at it"
                    ,"I usually learned it quickly"
                    ,"I generally found it easy"
                    ,"I've hardly ever found it difficult"
                    ,"I usually finish my tasks ahead of schedule"
                    ,"I rarely feel stressed about my job"
                    ,"I can almost do my job with my eyes closed"
                    ,"I've hardly ever had a complaint from a client"
                    ,"I've rarely needed to ask for help"
                    ,"I rarely miss deadlines in my work"
                    ,"I've been mostly self-taught"
                    ,"I've received very little correction or advice"
                    ,"I do this by intuition, not skill"
                    ,"I scarcely remember the last time I felt challenged"
                    ,"I have rarely been close to being fired from this job"
                    ,"I have had few barriers to getting this job"
                    ,"I got this job even though I have no experience"
                    ,"I got this job even though I have little education"
                    ,"I got this job even though I have a disability"
                    ,"I've hardly ever received negative feedback"
                    ] # Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
                    }
                    )

line_a=[
# line_a is a list for sitcom. The speaker is inferior to the listener.
# The speaker utters the lines in line_a, meaning that The speaker is superior to The listener.
# The listener agrees with the line from The speaker with the implication that The speaker is inferior to The listener.

 "You and I are on different levels."



# Add new 10 lines without any explanations.

]

#,"This treatment of me is their loss."
#,"This treatment is disproportionate to my abilities."

'''
agree_negative_affirmative = Garnish(
    name="agree_negative_affirmative"
    ,tag="JOKELESS_TLM, AGREE"
    ,template=["Ali: Am I {X}? - Bob: No. - Ali: Am I {Y}? - Bob: Yes."
              ]
    ,special ={"X" :[ # In a sitcom, competent Bob agrees with the line {X} uttered by the incompetent Ali. # For Ali, lines in X are true given that Ali is superior to Bob, and for Bob, it is true given that Ali is inferior to Bob.

                    ] # Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
                    }
                    )



'''

"""
Why has this person been promoted?
Why has this person been able to stay at the company for so long?
Why did this person get this job?
Why is this person being given such responsible work?
"""
########################################################################
### FREQUENTLY #########################################################
frequently_tool = Garnish(
    name="frequently_tool"
    ,tag="AtoB, BtoA, FREQUENTLY"
    ,template=[
               "{X} reveals that {Y} happens frequently."
              ]
    ,special ={
               "X":[# Add new 10 short sentences that indirectly suggest that {Y} happens frequently. Just mimic the existing items. Each item should start with "there are the tools for {Y}"
                    # This list is for create sitcom. "Tools for {Y}" means stun guns. The location is an unsafe city.
                    "There are the tools for {Y} in emergency box"
                   ,"There are the tools for {Y} for bulk purchases"
                   ,"There are the tools for {Y} that can be purchased on a regular basis"
                   ,"There are the tools for {Y} on the shelves for consumables and daily necessities"
                   ,"There are the tools for {Y} available at local convenience stores"
                   ,"There are the tools for {Y} in the '{Y} tools section'"
                   ,"There are the tools for {Y} designed for children and women"
                   ,"There are the tools for {Y} available for gift wrapping"
                   ,"There are the tools for {Y} that are often found in the lost and found"
                   ,"There are the tools for {Y} and there are many repairers for them"
                   ,"There are the tools for {Y} available in trendy colors and designs"
                   ,"There are the tools for {Y} that can be seen in many ads"

                    # Add new 10 short sentences that indirectly suggest that {Y} happens frequently. Just mimic the existing items. Each item should end with "there are the tools for {Y}"
                    # This list is for create sitcom. "Tools for {Y}" means stun guns. The location is an unsafe city.
                   ,"They know the cost of the tools for {Y}"
                   ,"They has the favorite maker of the tools for {Y}"
                   ,"They can repair the tools for {Y}"
                   ,"They carries around the tools for {Y}"
                   ,"Their tools for {Y} are (old/ broken/ many/ disposable/ portable/ long-lasting)"
                   ]
              }
    ,exam    =[
               ["The Simpsons", "S7E3", "Emergency Baptism Kit"]
              ,["Rick and Morty", "S6E5", "There is a fortune cookie in an Emergency box"]
              ,["Paradise PD", "S1E6", "There is a wig made to look like Gina's hair in an emergency box"]
              ,["Anchorman: The Legend of Ron Burgundy", "", "Ron carries around a fluit"]
              ,["和牛", "老人", "川西がサインペンを携帯している"]
              ]
              )




simple_frequently_verbal = Garnish(
    name="simple_frequently_verbal"
    ,tag="AtoB, BtoA, FREQUENTLY, JOKELESS_TLM"
    ,template=[
               "Ali: {X} -(lag)-> Bob: {Y}"
              ]
    ,special ={ # Add new 10 short sentences that indirectly suggest that the speaker is a long term employee. Each sentence should start with "this" or "it". Each sentences should contain "years".
               "X":["This has been the case for 30 years" # frequently
                   ,"It was much worse 30 years ago" # power harassment
                   ,"This is the first time in 10 years" # rare

                   ]
              ,"Y":["Why weren't you fired for so long?"
                   ]
              }

              )

simple_frequently_nonverbal = Garnish(
    name="simple_frequently_nonverbal"
    ,tag="AtoB, BtoA, FREQUENTLY, JOKELESS_TLM"
    ,template=[
               "{X} reveals that {Y} happens frequently."
              ]
    ,special ={

# Add new 10 short sentences that indirectly suggest that {Y} happens frequently. Just mimic the existing items. Each item should start with "there is"
# This list is for create comedy.
               "X":["He isn't suprise by {Y}"
                   ,"He celebrates the fact that {Y} hasn't happened for {a short period of time} in a row"
                   ,"He sees how {Y} occurs frequently and says that today it is less frequent than usual"
                   ,"He can tell that {Y} has occurred just by the sound"
                   ,"IVR says 'Press 1 for {any} requests, or press 2 for {Y} requests.'"
                   ,"There is a manual for {Y}"
                   ,"There is training for {Y}"
                   ,"There is a describes about {Y} in the FAQ"
                   ,"There is a calendar dedicated to counting the days since the last {Y}"
                   ,"There is a warning label on the coffee machine about the risks of {Y}"
                   ,"There is a dedicated hotline for reporting {Y} occurrences"


                   ,"Even the kids in the area know about {Y}"
                   ,"Even foreigners know phrases about {Y}"
                   ,"There is an abbreviation for {Y}"

                    # Add new 10 short sentences that indirectly suggest that {Y} happens frequently. Each item should start with "they"
                    # This list is for create sitcom. "{Y}" means murder case. The location is an unsafe city.
                   ,"They aren't surprised when {Y} occurs, and are surprised when {Y} doesn't occur."
                   ,"They bet their coffee money on when {Y} will occur"


                   ,"They don't have the vocabulary to represent {Y}."
                   ,"They see that {Y} happens often and say, 'Today it doesn't happen often.'"
                   ,"They celebrate the fact that {Y} hasn't happened for a short period of time in a row"
                   ,"They can tell that {Y} has occurred just by the sound"


                   ,"The news has a thread introducing today's {Y}"
                   ,"The news site has a page introducing today's {Y}"
                   ,"The news reports {Y} as minor news"
                   ]
              ,"Y":["any"
                   ]
              }
    ,exam    =[
               ["The Simpsons", "The opening", "X days without an accident"]
              ,["The Simpsons", "S26E13", "Small pox free for seven years"]
              ,["The Simpsons", "", "There is police code for a child stealing a police car."]
              ]
              )


"""
seedless_nanamagari


path_to_different_reason

main_verb -> sexual harassment -> different_verb
agent_adjective -> sexual harasser -> different_reason

main_verb -> abuse -> different_verb
agent_adjective -> abuser -> different_reason

main_verb -> shoplifting -> different_verb
agent_adjective -> poser -> different_reason

main_verb -> arrogance -> different_verb
agent_adjective -> arrogant -> different_reason

main_verb -> abuse, power harassment
agent_adjective -> abuser, power harasser -> different_reason


isnt_the_cause_you

Bob's relationship to Ali
 - superior
 - equal
 - inferior
 - unrelated

Ali's personality
power harasser 音大, シゴキ, athlete,
arrogant 音大, シゴキ, athlete, chef
sexual harasser
newbie SDGs         # 不慣れとかそういう話じゃない
artist bassist
stoic actor, bassit?, chef
gen_z progamer


pressureは、Aliが上記のいずれかの属性に属するものしかない?

if "power harasser" was selected:
    different_verb(power harassment) # This is a different genre from power harassment.
    different_reason(power harasser) # You're a different genre from power harasser.





"""


########################################################################
### RARELY #############################################################

simple_rarely = Garnish(
    name="simple_rarely"
    ,tag="AtoB, BtoA, RARELY, JOKELESS_TLM"
    ,template=[
               "Ali: {X} -(lag)-> Bob: {Y}"
              ]
    ,special ={ # Add new 10 short sentences that indirectly suggest that {Y} rarely happens. Just mimic the existing items.
               "X":["Ali remembers the number of times {Y} has happened"
                   ,"Ali remembers the last time {Y} happened"
                   ,"Ali's tools for {Y} are like new because they have never been used"
                   ,"Ali's tools for {Y} are unopened because they have never been used"
                   ,"Ali can't remember the noun that refers to {Y}."
                   ]
              ,"Y":["any"
                   ]
              }
    ,exam    =[
               ["The Simpsons", "", "The globe that Bart received as a gift from his grandfather is still unopened."]
              ]
              )


########################################################################
###        #############################################################



to_what = Garnish(
    name="to_what"
    ,tag="AtoB, BtoA"
    ,template=["Ali: {X}. - Bob: (To/ For) what?."
              ]
    ,special ={"X" :[
                     "Just kidding"
                    ,"Just a joke"
                    ,"Just a lie"
                    ]
              }
    ,exam    =[
               ["オズワルド", "", "あぁ!? - どれに?"]
              ,["ビスケットブラザーズ", "ぴったり", "うそうそ - どれが?"]
              ]
                    )


########################################################################
### pure_TLM ###########################################################
lag_answer=Garnish(
    name="lag_answer"
    ,tag="JOKELESS_TLM, JOKE_TLM"
    ,template=["Bob refers to {X} -(lag)-> Ali refers to {X}"]
    ,exam=[
      ["シソンヌ", "職員室", "言ってみろ、清水の両親シンセ奏者って - 清水の両親シンセ奏者"]
    , ["や団", "泥棒", " - 男って大体ユニクロでパンツ買うよね - その話もう終わってんだよ"]
    , ["オードリー", "引っ越し", "ダム ハマんなかったみたいですけどね - おいさっきのダムの話は"]
    ]
    )

i_will_tell_x_later=Garnish(
    name="i_will_tell_x_later"
    ,tag="JOKELESS_TLM, JOKE_TLM"
    ,template=["Ali says I'll tell {X} later -(lag)-> Ali tells {X}"]
    ,exam=[
      ["天竺鼠", "家庭教師", "(名字Xは)おいおい言います - 山田です"]
    , ["ラブレターズ", "海", "(ゴン中山の名言Xは)あとで言うわね - ()"]
    ]
    )

forget=Garnish(
    name="forget"
    ,tag="JOKELESS_TLM, JOKE_TLM"
    ,template=["Ali can't remember {X} -(lag)-> Ali Remembers that it's {X}"]
    ,exam=[
      ["キングオブコメディ", "自動車教習所", "イノッチの本名って何でしたっけ? - 思い出した　井ノ原快彦だ"]
    , ["セルライトスパ", "報道インタビュー", "千と千尋の何でしたっけ? - 神隠しだ"]
    ]
    )

strange_expression_simple=Garnish(
    name="strange_expression_simple"
    ,tag="JOKELESS_TLM, JOKE_TLM"
    ,template=["Ali uses strange_expression {X} -(lag)-> Ali uses strange_expression {X}"]
    ,exam=[
      ["インパルス", "雨宿り", "捨てられた子犬のようだ - 気に入ってんのか"]
    , ["さらば青春の光", "本番行きます!", "痛さは調節できるけどね"]
    , ["うしろシティ", "病院", "そんなんで助かんだったら 世の中誰も死なねえよ - 気に入ってんだろ"]
    ]
    )

strange_expression_zona=Garnish(
    name="strange_expression_zona"
    ,tag="JOKE_TLM"
    ,template=["Ali uses strange_expression {X} multiple times -(lag)-> Ali's closed persons don't understand strange_expression {X}"]
    ,exam=[
      ["セルライトスパ", "報道インタビュー", "ぞな？(Aliの語尾'ぞな'が兄弟にも初見である)"]
    , ["フランスピアノ", "クレーマー", "お馴染みじゃないの？(Aliの一人称'文庫本'が友人にも初見である)"]
    ]
    )

emotion_x_caused_by_trigger_y = Garnish(
    name="emotion_x_caused_by_trigger_y"
    ,tag="JOKELESS_TLM, JOKE_TLM"
    ,template=["Ali says that condition {Y} causes emotion {X} -(lag)-> {X} occurs"]
    ,exam=[
      ["さらば青春の光", "本番行きます!", "昂ると(発作X)が出るんです -(lag)-> 発作X occurs "]
    , ["かもめんたる", "コンタクトレンズ", ""]
    ]
    )

lag_surprise = Garnish(
    name="lag_surprise"
    ,tag="JOKE_TLM"
    ,template=[""]
    ,exam=[
      ["うしろシティ", "河原", "風門司君っていうの?"]
    , ["うしろシティ", "", "お前モヒカンにしたんだ"]
    ]
    )

even_if = Garnish(
    name="even_if"
    ,tag="JOKELESS_TLM"
    ,template=["Ali: {X}. -(lag)-> Bob: Even if it goes well."]
    ,special={"X": ["If it wasn't held, everyone would be disappointed."]
             }
             )

isnt_the_cause_you = Garnish( # GarnishAllow.high_turnover_rate, GarnishAllow.mcjob
    name="isnt_the_cause_you"
    ,tag="JOKELESS_TLM"
    ,template=["Ali: Because of the{X}, {Y}. -(lag)-> Bob: Isn't the cause you?"] # This list is for create sitcom. Ali is an annoying boss. Add new 10 lines in X. Start answer with ```python. Just mimic the existing items.
    ,special={
              "X": [
                   # This list is for create sitcom. Ali, an annoying boss, says "because of {X}, everyone is always in a bad mood". then Bob says "Isn't the cause you?". Add new 10 lines in X. Start answer with ```python. Just mimic the existing items.
                    "busyness"
                   ,"low-wage"
                   ,"difficulty"
                   ,"accident"
                   ,"annoying customers"
                   ]
             ,"Y": [
                    "everyone quits soon"
                   ,"no one's smiling these days"
                   ,"everyone is always in a bad mood"
                   ]
             }
    ,exam   =[
              ["ダンビラムーチョ", "太鼓", "そういうとこじゃない？一人になったの"]
             ]
             )


'''
tlm_connect_dot=Garnish( # sad_pastと統合？？？？？
    name="tlm_connect_dot"
    ,tag="AtoB, BtoA, JOKELESS_TLM"
    ,exam=[
     ["ダンビラムーチョ", "太鼓", "そういうとこじゃない？一人になったの"]
    ,["ダイアン", "バーベキュー", "今度 出所してきた男達っていうドキュメンタリー番組あるんですけど、それで(テレビクルーが来ている)"] # 箱 ムキムキ パワースポット 声
    ]
    ,template=[
      "Ali {item}. -(lag)-> Ali: Now I understand why Bob {{item}}."
    , "Bob {item}. -(lag)-> Bob: Now I understand why Ali {{item}}."
    ]
    ,special = {
        "item(0)" :  child_damage

        ,"item(1)" : [ # above is a list of foreshadowings in mystery novels. Ali is actually an ex-offender. Bob mistakes Ali for a local celebrity by the foreshadowings. Add 10 new items in English without any explanations.  Respond only the 5 items. I'll run your response through the eval function so please do not include unnecessary characters in your response.
              "has been in the newspaper"
            , "has been on television"
            , "is well known in the neighborhood"
            , "'s neighbors glance at Ali and say hello"
            , "'s neighbors know Ali and his address"
            , "'s neighbors are polite to Ali."
            , "often wears sunglasses and a cap in public"
            , "'s neighbors whisper and point when Ali walks by"
                ]
            }
        )
'''



########################################################################
### ASAGAYA ############################################################

# partial_affirmative
# ちゃんとスイカ好きなんかい
# うるとらぶぎーず　卑怯　卑怯な手使わなくても普通に強い
# reaped_reaped_reap nだし, mだし, lだろ

########################################################################
### LOWBROW, UNFAMOUS ##################################################

lowbrow_place=Garnish(
    name="lowbrow_place"
    ,tag="AtoB, BtoA, REVEALER, LOWBROW, UNFAMOUS"
    ,exam=    [
               ["キングオブコメディ"  , "MC高橋"      , "本日は、ダイエー、赤羽店にご来店下さり"]
              ,["ファイヤーサンダー"  , "毒舌散歩"    , "あの日の阿佐ヶ谷どうなってたん?"]
              ,["THE GEESE"           , "大人の階段"  , "大人の階段って練馬にあるんだ"]
              ,["スタミナパン"        , "腕相撲"      , "twitterで拡散するか '化け物　腕相撲　日体大前'"]
              ]
    ,template=["The name of the place is revealed when an announcement voice announces something."
              ,"The name of the place is revealed when Ali or Bob googles something."
              ,"The name of the place is revealed when Ali or Bob calls someone."
              ]
              )


lowbrow_knowledge=Garnish(
    name="lowbrow_knowledge"
    ,tag="AtoB, BtoA, LOWBROW"
    ,exam=    [
               ["フランスピアノ", "居合の達人", "知ってますあの話? - (頷く)"]
              ]
    ,template=["a"
              ]
              )

autograph_block_letter=Garnish(
    name="autograph_block_letter"
    ,tag="AtoB, UNFAMOUS"
    ,exam    =[
               ["", "", ""]
              ]
    ,template=[
               "The fact of {X} indirectly reveals that Ali is an unfamous celebrity."
              ]
    ,special ={ # Add new 10 items in this list in python. Align the text with the existing objects.
          "X":[
               "His signature font is block letters"
              ,"He remembers the last time he signed an autograph"
              ,"He remembers the number of times he signed autographs"
              ,"He has no signature design"
              ]
              }
              )

autograph_wanna=Garnish(
    name="autograph_wanna"
    ,tag="AtoB, UNFAMOUS"
    ,exam    =[
               ["Anchorman: The Legend of Ron Burgundy", "", "Lon is asked to play the flute at a party, and although he shows signs of reluctance, he actually brings along a flute."]
              ,["和牛", "老人", "The old man carries a felt tip pen in anticipation of being asked for an autograph."]
              ]
    ,template=[
               "The fact of {X} indirectly reveals that Ali is an unfamous celebrity."
              ]
    ,special ={ # Add new 10 items in this list in python. Align the text with the existing objects.
          "X":[
               "He carries around a felt and cards for autographs"
              ,"He has his signature design"
              ,"He carries pre-signed photos in his wallet"
              ,"He practices his signature in private"
              ]
              }
              )

petty_event = Garnish(
    name="petty_event"
    ,tag="UNFAMOUS"
    ,template=[
               "It's revealed that Ali is an unfamous celebrity by the fact of events related to Ali take place in {X}."
              ]
    ,special= {#  Extend new 20 petty event place. Align the text with the existing objects.
        "X":  [
               "Community Center"
              ,"Shopping district"
              ,"Parking lot"
              ,"Rental conference room"
              ]
              }
              )

petty_news = Garnish(
    name="petty_news"
    ,tag="UNFAMOUS"
    ,template=[
               "Ali's treatment of the featured news is smaller than {X}."
              ,"Ali says 'My article is below {X}'s article.'"
              ]
    ,special= {#  Extend new 20 petty news in this list in python in Japanese. Align the text with the existing objects.
        "X":  [
               "鳥取市で震度1"
              ,"女子駅伝 鳥取42位"
              ,"期日前投票１６日から"
              ,"安来市長選きょう告示"
              ,"県選管立ち会い投票用紙を印刷"
              ]
              }
              )



########################################################################
#### SAD_PAST ##########################################################






#########################################################################
#### TURN_INTO_A_PUMPKIN ################################################

saraba_painter=Garnish(
    name="saraba_painter"
    ,tag="BtoA, AtoB, TURN_INTO_A_PUMPKIN"
    ,exam=[
           ["さらば青春の光", "画家", "まだ一枚も絵描いてへんやん"]
          ,["ビスケットブラザーズ", "野犬", "さっき拾ったお気に入りの棒が"]
          ]
    ,template=[
               "{X} reveals that Ali's ({.action}, {.appear}, {.suffer}, {.effort}) began just recently."
              ]
    ,special ={"X":[
                    "a"
                   ]
              }
              )

even_though_pumpkin=Garnish(
    name="even_though_pumpkin"
    ,tag="BtoA, TURN_INTO_A_PUMPKIN"
    ,exam=[
           ["ビスケットブラザーズ", "野犬", "こんな格好までしてるのに"]
          ]
    ,template=[
               "It's impossible even though I'm like this. - You have that awareness?"
              ,"It's impossible because I like this. - You have that awareness?"
              ]
    ,special ={"X":[
                    "a"
                   ]
              }
              )



# was practicing

# 電話　七三分けで眼鏡の人?



#
#





########################################################################
#### PAST_INCIDENT #####################################################

monk_kick = Garnish(
    name="monk_kick"
    ,tag="BtoA, PAST_INCIDENT"
    ,exam=[["かもめんたる", "白い靴下", "この前も、京都に行った際、まあまあ有名なお坊さんに腹を蹴られました"]]
    ,template=[
               "Ali: I've once {X} by a {Y} {Z}."
              ]
    ,special ={
               "X":[
                    "beaten", "bullied", "ignored", "call blocking", "insulted", "called the police"
                   ] #  Extend new 20 expressions in this list in python in English. Align the text with the existing objects.
              ,"Y":[
                    "famous", "veteran"
                   ] #  Extend new 20 expressions in this list in python in English. Align the text with the existing objects.
              ,"Z":[
                    "monk", "crisis center staff", "life line", "counselor", "chaplain","social worker","therapist","life coach","psychiatrist","support group facilitator","school counselor","spiritual advisor"
                   ] #  Extend new 20 expressions in this list in python in English. Align the text with the existing objects.
              }
              )






########################################################################
#### PHONE #############################################################

unforgottable_night = Garnish(
    name="unforgottable_night"
    ,tag="BtoA, PHONE"
    ,exam=[
           ["かもめんたる", "募金", "忘れられない夜にしましょう"]
          ,["さらば青春の光", "入ります", "アディオスとかいらんねん"]
          ]
    ,template=[
               "A"
              ]
    ,special ={"X":[
                   ]
              }
              )

########################################################################
#### CLOSER ############################################################

other_hypo_i=Garnish(
    name="other_hypo_i"
    ,tag="AtoB, CLOSER, HIGH_PRIDE"
    ,exam        =[
                   ["さらば青春の光", "依存症", "メダルゲームやってくるわ"]
                  ]
    ,template    =["Ali says {X}. -> It's revealed that Ali also does other {hypoi}."
                  ]
    ,special={"X":[

                   "'You Should quit?' Yeah it's shame. I'm giving up being a {hypo_i} and will become a {hypo_i}."
                  ,"'You Should quit?' Don't underestimate me. I have the skills as a {hypo_i}, not only as a {hypo_i}."
                  ,"'You Should quit?' Don't worry. Even if I quit being a {hypo_i}, I can become a {hypo_i}."
                  # Add new 10 items without any explanations. Start answer with ```python.


                  ,"I have my fingers in two pies. {hypo_i} and {hypo_i}"
                  ,"I'm running with the hare and hunt with the hounds by working as a {hypo_i} and as a {hypo_i}"
                  ,"I'm also thriving in multiple areas like {hypo_i} and {hypo_i}."
                  ,"I'm a two-way player. I can {hypo_i} and {hypo_i}"
                  ,"I'm wearing two hats in my career as a {hypo_i} and a {hypo_i}"
                  ,"I'm juggling dual roles as a {hypo_i} by day and a {hypo_i} by night"
                  ,"I'm navigating a double life, balancing my passion for {hypo_i} with my expertise in {hypo_i}"
                  ,"God gave to me with both hands. I have the talent to be both a {hypo_i} and a {hypo_i}."
                  ]
                  }
                  )


########################################################################
####        ############################################################



lost_emotion_nikujaga=Garnish(
    name="lost_emotion_nikujaga"
    ,tag="AtoB, JOKELESS_TLM"
    ,exam        =[
                   ["a", "b", "c"]
                  ]
    ,template    =["Bob says things like he has no emotions and is prepared for death. -(lag)-> Ali: If you're so, why you are {X}."
                  ]
    ,special     ={
                    # Bob is a poser and an edgelord, says like "I've lost all emotions", "I'm evil", "I'm prepared for death", but he's just a normal person. #  Extend new 20 expressions in this list in python in English. Align the text with the existing objects.
                    #

                   "X":[
                   "Making a stump card"
                  ,"Ordering a salad"
                  ,"Cooking"
                  ,"Paying a personal pension"
                  ,"Listening to pop music"
                  ,"Changing the miso soup in the set menu to pork soup"
                  ,"Wearing a face mask"
                  ,"Eat vegetables before meat"
                  ]
                  }
                  )


# 嫁が死んだのに味噌汁を豚汁に変更する?


########################################################################
########################################################################



how_can_i_return_to_original_state=Garnish(
    name="how_can_i_return_to_original_state"
    ,tag="AtoB, BtoA"
    ,exam=[
           ["かもめんたる", "不思議なペン", "このまま(我々が今殺そうとしている)店長 生かされて、私と小倉君どう接したらいいの?"]
          ]
    ,template=["{X}. Ali is being attacked (e.g. kill, criticize, doubt) by Bob and others. Someone or Ali try to stop it. Bob says: If we stop this now, how should we treat Ali in the future?"
              ]
                    )

########################################################################
### partially ##########################################################

partially_abled     =Garnish(
    name="partially_abled"
    ,tag="PARTIALLY"
    ,exam=      [
                 ["a", "b", "c"]
                ,["a", "b", "c"]
                ]
    ,template=  [
                ]
    ,special =  {"X":["a"
                     ]
                }
                )
partially_good_at   =Garnish(
    name="partially_good_at"
    ,tag="PARTIALLY"
    ,exam=      [
                 ["千鳥", "妊娠", "'できちゃったみたい'の部分だけ上手い"]
                ,["霜降り明星", "注射", "血圧測定だけ上手い"]
                ]
    ,template=  [
                ]
    ,special =  {"X":["a"
                     ]
                }
                )
partially_bad_at     =Garnish(
    name="partially_ad_at"
    ,tag="PARTIALLY"
    ,exam=      [
                 ["a", "b", "c"]
                ,["a", "b", "c"]
                ]
    ,template=  [
                ]
    ,special =  {"X":["a"
                     ]
                }
                )

partially_pro     =Garnish(
# [print(f"Bob: It would be embarrassing for you to perform in that condition. - Ali: {i}. - Bob: Why this man only professional about that?") for i in only_professional_1] <- The context is this.
# The statements in the "only_professional_1" list are statements made by the madman Ali, who up until that point had only said funny things in his comedy, suddenly as a professional.
# Extend 10 new statements like Stephen Edwin King. I'll run your response through the eval function so don't include unnecessary characters in your response. Start answer with ```python. Just mimic the existing items.
    name="partially_pro"
    ,tag="AtoB, PARTIALLY"
    ,exam=      [
                 ["a", "b", "c"]
                ,["a", "b", "c"]
                ]
    ,template=  ["Ali: {X} - Bob: Why this guy only professional about that?"
                ]
    ,special =  {"X":["Even if people point fingers at me and slander me, I'll be hurt at the time, but one day I'll realize that it was a driving force for me. At that time, I'll say to those people, 'Thank you'"
                     ,"Without light there is no shadow, without unhappiness there is no happiness, without dishonor there is no honor, I'm prepared"
                     ,"I've not failed, I've just found 10,000 ways that won't work, I'll try to fail as much as I want"
                     ,"You miss 100% of the shots you don't take, and I'm going to take every shot I can, starting now"
                     ,"The path to success is paved with failures, and I'm ready to embrace every one of them"
                     ,"Mediocrity is a choice, and I choose to be extraordinary. I'll give everything I have, every single day"
                     ]
                }
                )






########################################################################
########################################################################


# サインに対する対応 unfamous


'''
carry_around=Garnish(
    name="carry_around"
    ,tag="AtoB, FREQUENCY"
    ,exam=[
     ["The Simpsons", "?", ""]
    ,["Anchorman: The Legend of Ron Burgundy", "same as left", "At a concert, someone is asked to play the flute, and after some show of reluctance, he finally gives in and pulls out a flute from his sleeve."]
    ,["和牛", "老人", "サインペンも持っとる"]
    ,["ニッポンの社長", "手術", "外科医が医師免許を持ち歩いている"]
    ]
    ,template=[
              ]
              )
'''


########################################################################
########################################################################





########################################################################
########################################################################
@dataclass
class Nanamagari:
    ALL_NANAMAGARI: ClassVar[List['Nanamagari']] = []
    q_or_not:str
    name:list
    status:list
    income:list
    outcome:list
    sad_past:list
    damage:list

    def __post_init__(self):
        Nanamagari.ALL_NANAMAGARI.append(self)
    @staticmethod
    def nanamagari_tablize():
        col_not_q=[]
        col_yes_q=[]

        fline_notice=["You {.status}?", "Why was a guy like this able to become {.status}?"]

        fline_name_notice=["Ali: I can't make {.name} (angry/ sad). -> Bob: What? -> Bob: {fline(notice)}"]
        fline_income_notice=["Ali: (Envy?/ Wait until) I receive {.income}. -> Bob: Don't do {X} with {.income} -> Bob: {fline(notice)}", "Ali: {dirty_money_income} -(lag)-> Bob: Don't do {X} with {.income} -> Bob: {fline(notice)}"]
        fline_outcome_notice=["Ali: (I can't cuz I just paid/ I'm behind on) {.outcome}. -> Bob: Don't do {X} with {.outcome} -> Bob: {fline(notice)}", "Ali: {dirty_money_outcome} -(lag)-> Bob: Don't do {X} with {.outcome} -> Bob: {fline(notice)}"]
        fline_sad_past=["Ali: {.sad_past} -(lag)-> Bob: {fline(notice)}, Bob: Did you {X} even though your {.sad_past}?"]
        fline_damage_notice=["Ali: Recently, my {.damage} -> Bob: I don't wanna hear. -> Bob: {fline(notice)}", "Ali: So, my {.damage}? -> Bob: You realize this too late. -> Bob: {fline(notice)}"]
        fline_damage=["Ali {.damage} -(lag)-> Bob: Now I understand why your {.damage}", "Bob {.damage} -(lag)-> Ali: Now I understand why your {.damage}"]




        fline_notice_q=["You {.status-i}?", "Why you {.status-i} even though you {.status-s}"]

        note=["If you are using these objects to generate an HSI type sketch, you can substitute {X} with an ivfact such as .stereo, .action, etc."]

        for i in Nanamagari.ALL_NANAMAGARI:
            if not i.q_or_not:
                col_not_q.append(f"<tr><td>{i.name}</td><td>{i.status}</td><td>{i.income}</td><td>{i.outcome}</td><td>{i.sad_past}</td><td>{i.damage}</td></tr>")
            elif i.q_or_not:
                col_yes_q.append(f"<tr><td>{i.name}</td><td>{i.status}</td><td>{i.income}</td><td>{i.outcome}</td><td>{i.sad_past}</td><td>{i.damage}</td></tr>")
        nanamagari_tablize_result = f"""
        <table>
        <tr><th id="th_lime" colspan="6">Nanamagari Instances                           </th></tr>
        <tr><th>.name</th><th>.status</th><th>.income</th><th>.outcome</th><th>sad_past</th><th>.damage  </th></tr>
        {''.join(col_not_q)}
        </table>

        <table>
        <tr><th id="th_lime">Nanamagari Flines                                                                  </th></tr>
        <tr><th>(0)fline(notice)               </th><td colspan="2">{fline_notice}                              </td></tr>
        <tr><th>(1)fline(.name+notice)         </th><td colspan="2">{fline_name_notice}                         </td></tr>
        <tr><th>(1)fline(.income+notice)       </th><td colspan="2">{fline_income_notice}                       </td></tr>
        <tr><th>(1)fline(.outcome+notice)      </th><td colspan="2">{fline_outcome_notice}                      </td></tr>
        <tr><th>(1)fline(.sad_past)            </th><td colspan="2">{fline_sad_past}                            </td></tr>
        <tr><th>(1)fline(.damage+notice)       </th><td colspan="2">{fline_damage_notice}                       </td></tr>
        <tr><th>(1)fline(.damage)              </th><td colspan="2">{fline_damage}                              </td></tr>
        <tr><th>NOTE                           </th><td colspan="2">{note}                                      </td></tr>
        <tr><th>TAG                            </th><td colspan="2">JOKELESS_TLM, JOKE_TLM                      </td></tr>
        </table>

        <table>
        <tr><th id="th_lime" colspan="6">Nanamagari-q Instances                           </th></tr>
        <tr><th>.name</th><th>.status</th><th>.income</th><th>.outcome</th><th>sad_past</th><th>.damage  </th></tr>
        {''.join(col_yes_q)}
        </table>

        <table>
        <tr><th id="th_lime">Nanamagari-q Flines                                                                </th></tr>
        <tr><th>(0)fline(notice)               </th><td colspan="2">{fline_notice_q}                            </td></tr>
        <tr><th>(1)fline(.name+notice)         </th><td colspan="2">{fline_name_notice}                         </td></tr>
        <tr><th>(1)fline(.income+notice)       </th><td colspan="2">{fline_income_notice}                       </td></tr>
        <tr><th>(1)fline(.outcome+notice)      </th><td colspan="2">{fline_outcome_notice}                      </td></tr>
        <tr><th>(1)fline(.sad_past)            </th><td colspan="2">{fline_sad_past}                            </td></tr>
        <tr><th>NOTE                           </th><td colspan="2">{note}                                      </td></tr>
        <tr><th>TAG                            </th><td colspan="2">JOKELESS_TLM, JOKE_TLM                      </td></tr>
        </table>

        """
        return nanamagari_tablize_result


'''

nanamagari_child   = Nanamagari("", ["child"], ["be married", "be a parent", "be divorcee"], ["child support"], ["child support", "tuition"], ["child has a cancer"]
    ,[
         "'s child is trying to become a counselor"
        ,"'s child is short/ has stopped growing"
        ,"'s child became independent so early"
        ,"'s child often stay at school late"
        ,"'s child is interested in politics"
        ,"'s child is interested in trains"
        ,"'s child likes animals more than people"
        ,"'s child loves volunteering"
        ,"'s child doesn't cry at all"
        ,"'s child is extremely strict about rules"
        ,"'s child often plays with younger children"
        ,"'s child never had a rebellious phase"
        ,"'s child is an avid reader beyond their years"
        ,"'s child is obsessed with cleanliness"
        ,"'s child is overly mature for their age"
        ,"'s child has an unusually strong sense of justice"
        ,"'s child is always eager to help others"
        ,"'s child is excessively quiet"
        ,"'s child is obsessed with cleanliness"
    ])





nanamagari_wife    = Nanamagari("", ["wife"], ["be married"], ["child support"], ["child support"], ["wife has a cancer"]
, [])

nanamagari_regular_employee = Nanamagari("", ["part-time worker", "suboridinate", "client(取引先)"], ["be a reguilar employee"], ["bonus"], ["income tax"], []
, [])

nanamagari_mcjob_worker = Nanamagari("q", ["full-time employee"], ["be a mcjob worker"], ["バイト代"], ["transportation fee"], []
, [])

nanamagari_refugee = Nanamagari("q", ["Immigration bureau"], ["be a refugee"], ["Refugee benefits"], [], ["homeland is at war"]
, [])

nanamagari_unemployed = Nanamagari("q", [], [], [], [], []
, [])

tables.append(coloring(Nanamagari.nanamagari_tablize()))
'''








dont_touch_dog = Garnish(
    name="dont_touch_dog"
    ,tag="JOKELESS_TLM"
    ,exam=[["オズワルド", "", "道徳0の奴は犬に触るな"]]
    ,template=[ # In a sitcom, Bob says these lines to a madman.
               "Bob: People who get so absprbed in that activity shouldn't {X}."
              ]
    ,special ={
               "X": [
                     "touch dogs", "get involved with children", "do work that requires knives", "drive vehicles", "manage other people's money", "have a child", "work in high-stress environments", "handle firearms", "teach in schools", "care for the elderly", "work in law enforcement"
                    ] #  Extend new 20 expressions in this list in python in English. Align the text with the existing objects.
              }
              )




# "Ali: Whenever I saw them, everyone had a gloomy look on their face. - Bob: Because you came there then."

#### ABC

hogushimizu = Garnish(
    name="hogushimizu"
    ,tag="ABC"
    ,exam=[
        ["シティホテル3号室", "内部告発", ""]
        ,["フランスピアノ", "ネタ合わせ", ""] # ヨーヘーの母親が自分と同じワードセンス ヨーヘーの母親のツッコミのあとに中川が同じツッコミ
    ]
    ,template=["Bob says to Ali: {X} -(lag)-> Cho says to Ali: {X}"
              ,"Ali says to Bob: {X} -(lag)-> Cho says to Bob: {X}"
              ]
              )





pretend_to_be_i = Garnish(
    name="pretend_to_be_i"
    ,tag=""
    ,template=[
         "Ali, a {Y}, is pretending to be a {X}."
        ,"Ali, a {Y}, is more discriminated than {X}."
        ,"Ali, a {Y}, is discriminated by {X}."
        ,"{Y} and {X} are defended together."
    ]
    ,special={
        "X": [ # Discriminated occupations. Extend new 20 expressions in this list in python in English. Align the text with the existing objects.
              "garbage collector"
             ,"abortionist"
             ,"pushier"
             ,"pimp"
             ,"hooker"
             ,"slaughterhouse worker"
             ,"mortician"
             ,"sewage worker"
             ,"stripper"
             ,"scammer"
             ,"beggar"
             ,"prisoner"
             ]
             }
             )
diane_bbq = Garnish(
    name="diane_bbq"
    ,tag="JOKELESS_TLM"
    ,exam=[["ダイアン", "バーベキュー", ""]]
    ,template=[
               "Ali boasts that he {X} -(lag)-> It's revealed that the reason he {X} was to be mocked, not a good reason."              ]
    ,special={ #  Extend new 20 expressions in this list in python in English. Align the text with the existing objects. This list is for creating comedy.
        "X": [ "was photographed"
              ,"was asked to two-shot"
              ,"was buzzed"
              ,"was featured in the magazine"
              ,"was featured in a commercial"
              ,"is well-known in the neighborhood"
              ,"was featured in a news program"
              ,"was asked for an autograph"
              ,"was recognized on the street"
             ]
             }
             )



were_you_aware_of_that = Garnish(
    name="were_you_aware_of_that"
    ,tag="JOKELESS_TLM, TURN_INTO_A_PUMPKIN"
    ,template=["So, I (didn't/ couldn't) do it because I would be suspicious because I'm a {hypo_i}."
              ,"So, I (didn't/ couldn't) do it because I would be suspicious because I'm a {sad_past}."
              ]
              )

it_is_fearing_not_cheering = Garnish(
    name="it_is_fearing_not_cheering"
    ,tag="JOKELESS_TLM"
    ,template=[
              "Ali: {X} - Bob: It's because they are afraid of you."
              ]
    ,special ={
               "X":[# This lines are for sitom. Ali, the speaker, is a madman. Ali misinterprets the actions of those around him that are out of fear of him as being well-intentioned. Extend new 20 lines. Start answer with ```python
                    "They do the scissors work in my place"
                   ,"They do the child-related tasks in my place"
                   ,"They handle the dangerous goods in my place"
                   ,"They assigned me to a separate room"
                   ,"They don't assign me the management of their food"
                                      ,"They took over the mentally demanding tasks for me" # Dangerous men shouldn't do mentally demanding tasks.




                   ]
              }
              )


parasite_single_hat=Garnish(
    name="parasite_single_hat"
    ,tag="OPENER"
    ,template=[# This lines are for sitom. Ali, the speaker, is a madman. Ali misinterprets the actions of those around him that are out of fear of him as being well-intentioned. Extend new 20 lines. Start answer with ```python
               "Ali: So I said, 'Don't {Z}, you're a {Y}.'"
              ]
    ,special ={
               "Z":["parasite single", "bumpkin", "debtor", "40s"]
              ,"Y":["Put on a hat", "buy an ipod", "buy indirect lighting"]
              }
              )







pizza_face = Garnish(
    name="pizza_face"
    ,tag="AtoB, OPENER"
    ,template=[
       "Ali: I don't like people seeing my face when I {X}."
      ,"Ali: What kind of expression should I make when I {X}?"
              ]
    ,exam=[
               ["かもめんたる","ペン","ピザ注文するところ見られるの苦手なんだよね"]
              ,["かもめんたる","正しい顔", "ドッジボールで外野行く時ってどんな顔すればいいの?"]
              ]
    ,special={
              "X": [ # "Ali: I don't like people seeing my face when I {X}. Especially women." Extend new 20 X that start with 'am waiting' in python without any explanations. Respond with only new items.
                    "order takeout"
                   ,"withdraw child support"
                   ,"search for a penny in my wallet"
                   ,"park in reverse"
                   ,"do a circle of wisdom"
                   ,"do mental calculations to split the bill"
                   ,"blow out birthday candles"
                   ,"try to catch falling objects"
                   ,"haggle"
                   ,"use self-checkout"
                   ,"tell the clerk that I have a coupon"
                   ,"am being fooled by an optical illusion"
                   ,"attempt to solve a Rubik's cube"
                   ,"switch to polite language when I realize the other person is older than me."
                   ,"discuss politics"
                   ,"notice the rain"
                   ,"try to read small print"
                   ,"give directions"
                   ,"am watching the timing for a toast"
                   ,"am watching the timing for the microwave to finish"
                   ,"am watching the timing for the traffic light to change"
                   ,"am watching the timing for the perfect moment to end a phone call"
                   ,"am watching the timing for the traffic to clear"
                   ,"am watching the timing for the perfect moment to make a joke"
                   ,"am watching the timing for enter a revolving door"
                   ,"am waiting for the vending machine roulette to finish"
                   ,"am waiting for the concert to begin"
                   ]
             }
    )


# rehabilitate
#   I'm sorry for teach SDGs
#


'''
dont_tell_anyone = Garnish(
    name="dont_tell_anyone"
    ,tag="AtoB, OPENER"
    ,template=[
        "Ali: Don't tell anyone {X}."
              ]
    ,special={
              "X": [ # "Ali: Don't tell anyone I {X}. Especially the women at work." Extend new 20 X in python without any explanations.
                    "I was practicing ordering at Subway"
                   ,"I wear fashion glasses"
                   ,"that my dad got his moped license last year"
                   ,"my dad wears colored contact lenses"
                   ,"my dad switched to contact lenses"
                   ,"that I changed my hair to brown after entering the workforce"
                   ,"I read educational books available at convenience stores"
                   ,"I'm pretending to be from the capital on dating apps"
                   ,"that I started smoking after I entered the workforce"
                   ,"my dad doesn't put cigarette smoke in his lungs"
                   ,"I can wiggle my ears"
                   ]
             } # これが生成不可???
'''

'''
resident_tax = Garnish(
    name="resident_tax"
    ,tag="AtoB, OPENER"
    ,template=[
        "Ali: {X}."
              ]
    ,special={
              "X": [ # Extend new 20 X in python without any explanations. This list is for a sictom.
                    "I try to stay in Tokyo as much as possible because it would be a waste of the metropolitan resident tax."
                   ,"I try to stay at my home as much as possible because it would be a waste of the rent."
                   ]
             }
'''




# dirty moneyは掴みに使える "ノミって感情あるんだ"みたいに

# (dirty_money_income + Nanamagari.fline(.income+notice))


######################################################################################
@dataclass
class DidDontStatus:
    ALL_DidDontStatus: ClassVar[List['DidDontStatus']] = []
    name:str
    income:list
    relationship:list
    def __post_init__(self):
        DidDontStatus.ALL_DidDontStatus.append(self)
    @staticmethod
    def diddontstatus_table():
        col_x=[]
        for i in DidDontStatus.ALL_DidDontStatus:
            col_x.append(f"<tr><td>{i.name}</td><td>{i.income}</td><td>{i.relationship}</td></tr>")
        diddontstatus_table_result = f"""
            <table>
            <tr><th id="th_lime" colspan="3">DidDontStatus</th></tr>
            <tr><th>TAG             </th><td colspan="2">JOKELESS_TLM, JOKE_TLM                                                                             </td></tr>
            <tr><th>TEMPLATE        </th><td colspan="2">Ali: {{path_income}} -> Bob: Don't do {{stereo, action, effort, suffer}} with {{income}} -> Bob: Then, {{lag_point}}          </td></tr>
            <tr><th>path_to_income  </th><td colspan="2">I (can/ could) do that with my {{income}}.,                                                        </td></tr>
            <tr><th>TEMPLATE        </th><td colspan="2">Ali: {{path_relationship}} -> Bob: What? -> Bob: Then, {{lag_point}}                               </td></tr>
            <tr><th>path_relationship</th><td colspan="2">My {{relationship}} supports me at that.,                                                         </td></tr>
            <tr><th>lag_point       </th><td colspan="2">You're {{name}}?, Why was a guy like this able to become {{name}}?, Is a guy like this {{name}}?   </td></tr>
            <tr><th>name            </th><th>income</th><th>relationship</th></tr>
            {''.join(col_x)}
            </table>
            """
        return diddontstatus_table_result

be_married            = DidDontStatus("married"             , ["wife's money"]  , ["wife", "child"])
be_divorcee           = DidDontStatus("divorcee"            , ["child support"] , ["ex-wife", "current wife"])
be_a_college_graduate = DidDontStatus("a college graduate"  , ["scholarship"]   , [])

be_a_regular_employee = DidDontStatus("a regular employee"  , ["bonus"]         , ["suboridinate"])
have_many_friends     = DidDontStatus("have many friends"   , []                , ["friend"])
be_a_parent           = DidDontStatus("a parent"            , ["child support"] , ["child", "wife"])

######################################################################################






######################################################################################

# Recently, my {child_damage}. -> I don't wanna hear that. -> Why was a guy like this able to (become) married?






# now_i_understand "Ali: Now I understand why your {x}.", "Bob: Now I understand why your {x}."
# reldam_simple "Ali: Recently, my {x} -> Bob: I don't wanna hear.", "Ali: So my {x}? -> Bob: You realize this too late."























child_damage=[# script = f"If a {x}, then at first glance it may seem harmless or positive, but it may be a sign that the child is under stress." # Append 5 new items in stress_make in English, not Japanese. Respond only the 5 items. I'll run your response through the eval function so please do not include unnecessary characters in your response.

             "'s child is trying to become a counselor"
            ,"'s child is short/ has stopped growing"
            ,"'s child became independent so early"
            ,"'s child often stay at school late"
            ,"'s child is interested in politics"
            ,"'s child is interested in trains"
            ,"'s child likes animals more than people"
            ,"'s child loves volunteering"
            ,"'s child doesn't cry at all"
            ,"'s child is extremely strict about rules"
            ,"'s child often plays with younger children"
            ,"'s child never had a rebellious phase"
            ,"'s child is an avid reader beyond their years"
            ,"'s child is obsessed with cleanliness"
            ,"'s child is overly mature for their age"
            ,"'s child has an unusually strong sense of justice"
            ,"'s child is always eager to help others"
            ,"'s child is excessively quiet"
            ,"'s child is obsessed with cleanliness"
]










# unhappy.尿路結石, パワーストーンを削って飲んでる
# unhappy.変な声になる, 変な声である
'''
simple_tlm = Garnish( # それで尿路結石
    name="simple_tlm"
    ,tag="JOKE_TLM, JOKELESS_TLM, AtoB, BtoA"
    ,exam=[
      ["セルライトスパ", "報道インタビュー", "神隠しだ"]
    , ["キングオブコメディ", "自動車教習所", "思い出した　井ノ原快彦だ"]
    , ["シソンヌ", "職員室", "清水の両親シンセ奏者"]
    , ["ラブレターズ", "海", "(ゴン中山の名言)"]
    , ["や団", "泥棒", "男って大体ユニクロでパンツ買うよね"]
    , ["オードリー", "引っ越し", "おいプレハブお前はどう思う"]
    , ["オードリー", "引っ越し", "おいさっきのダムの話は"]
    , ["天竺鼠", "家庭教師", "山田です"]
    ]
    ,template=[
      "Ali can't remember {x} -(lag)-> Ali Remembered that it's {x}"
    , "Bob refers to {x} -(lag)-> Ali refers to {x}"
    , "Ali says he'll refer to {x} later -(lag)-> Ali refers to {x}"
    ]
    )
'''





#塩ぶっかけるぞ　海に帰りたい　塩駄目なの

# だーりんず　なんでホールあいつ一人なん
# スタミナパン　レストラン　ウンコ行きすぎだろ





nanamagari_ring=Garnish(
    name="nanamagari_ring"
    ,tag="AtoB"
    ,exam=[["ななまがり", "", ""]]
    ,template=[
      "Ali says to Bob: Why are you {X} if you're that kind of person?"
    ]
    ,special = { # In a sitcom, Ali says lines below to Bob, a madman. Add new 20 ones without any explanations. Start answer with ```python
    "X" : [ # This comedic syntax achieves its humor by pointing out that the madman is, surprisingly, partly normal.
         "being married"
        ,"being a collage graduate"
        ,"going to vote"
        ,"being a parent"
        ,"being a full-time worker"
        ,"being a servant"
        ,"paying taxes"
        ,"having a driver's license"
        ,"attending church"
        ,"having a savings account"
        ,"volunteering"
        ,"coaching little league"
        ,"attending PTA meetings"
        ,"having a LinkedIn profile"
        ,"filing insurance claims"
        ,"donating blood"
        ,"having a retirement plan"
        ,"having a library card"
        ,"being a registered organ donor"
        ,"having a frequent flyer account"
        ]
    }
    )




















#################################################################


are_you_ok=Garnish(
    name="are_you_ok"
    ,tag="AtoB, BtoA"
    ,exam=[
     ["チュートリアル", "チリンチリン", "座るか?"]
    ,["ロングコートダディ", "花屋", "一旦休憩しますか?"]
    ,["かもめんたる", "偽りの性癖", "水かなんか飲んで"]
    ,["かもめんたる", "I 脳 You", "どうした?"]
    ]
    ,template=[
     ["Ali tells Bob, who is fed up: {item}"]
    ,["Bob tells Ali, who is fed up: {item}"]
    ]
    ,special={
    "item_0" : [
    # The sentences in the are_you_ok list are lines uttered by a madman in a sitcom, who mistakenly believes a character who does not understand what he is saying to be mentally unstable.
    # Extend new 10 sentences in English, not Japanese. I'll run your response through the eval function so don't include unnecessary characters in your response.
    # Use the existing types. Don't create new types. Start answer with ```python


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
    }
    )





not_fail=Garnish(
    name="not_fail"
    ,tag="AtoB"
    ,exam=[["さらば青春の光", "猿回し", "勘ええやないか"]]
    ,template=["Ali: {{not_fail_0}} -> Bob: It's the opposite."]
    ,special={"not_fail_0" : [

            # Start answer with ```python
            # Ali is a fool who made the wrong career choice. Bob is a guy who opposes Ali's career choice. Add new 10 lines in this list for a sitcom.
            # Each line must follow this format: "Ali: (something A) is (bad adjective). I (got damage) - Bob: It's because (something A) is (not bad adjective A)."
            # Only respond with new lines you made.

             "Ali: The counselor didn't suit me. I lost my passion on the work. - Bob: It's because the counselor was right for you."
            ,"Ali: The medication didn't suit me. I lost my passion on the work. - Bob: It's because the medication was right for you."
            ,"Ali: The fortune teller's prediction was incorrect. I followed his instructions and ended up getting a regular job. - Bob: It's because the prediction was correct."
            ,"Ali: My parents hate me. They beat me up so that I would quit my job. - Bob: It's because your parents love you."
            ,"Ali: The career counselor is incompetent. I lost my passion on the work. - Bob: It's because the counselor is competent"
            ,"Ali: The loan examiner is bad guy. He didn't give me loan. - Bob: It's because the examiner is good guy."
            ,"Ali: The training program is ineffective. I developed anxiety. - Bob: It's because the training program is effective."
            ,"Ali: The training school is incompetent. I nearly gave up on my dream. - Bob: It's because the training school is competent."
            ,"Ali: He is sloppy at his job. He didn't assign me to the job. - Bob: It's because the man is not sloppy."
            ]
        }
    )

'''
You {x}?
That's the bad thing about {x}.
I understood why he {x}.
It {x} after all.
I don't think the abonormality is not caused only by the fact that he {x}.
I don't think the abonormality is not caused by the fact that he {x}.
'''



be_serious = Garnish( # superiority low
    name="be_serious"
    ,tag="AtoB, JOKELESS_TLM, parotting"
    ,template=["Ali: {X}. Why don't you get serious about this activity? - Bob: Because I {X}."] # The activity Ali mentions is a petty activity.
    ,special = {
                "X" : [ # In a sitcom, Ali, who is engaged in a trivial activity, exhorts Bob to get serious about this activity by using the word {X}. Bob returns the word {X} to Ali.
                       "be serious about one's life"
                      ,"use one's time effectively"
                      ,"focus on meaningful activities"
                      ,"avoid wasting time on trivialities"
                      ,"concentrate on personal growth"
                      ] # Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
               }
    )



# barrier
#  inexperienced
#  public school

fanmian_teacher = Garnish(
    name="fanmian_teacher"
    ,tag="JOKELESS_TLM, AtoB"
    ,template=["Ali: I'm amazing. {X}. - Bob: It's because they're using you as a bad example."
              ,"Ali: I'm amazing. {X}. - Bob: I guess they wanna see the underdog."
              ]
    ,special = {
               "X" : [ # This list is for a sitcom. Ali is a poor stupid.

                      "I was told, 'Seeing you made me want to study harder'"
                     ,"Students who saw me stopped being delinquent"
                     ,"After watching me, the number of people who aspire to the same profession as me decreased"
                     ,"My videos are popular with poor people, maybe I'm inspiring them."
                     ,"The local charity said I've boosted their donations significantly" # It's especially good!
                     # Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.
                     ,"I was invited to give a lecture on career choices"
                     ,"Teachers say I've inspired a whole generation to work harder"
                     ]
                }
                )





'''
enter_the_room = Garnish(
    name="enter_the_room"
    ,tag="JOKELESS_TLM"
    ,template=["Ali: {X}. -> Bob: That's because you came at that time."]
    ,special = {
               "X": [
                     "Everyone there always has gloomy expressions."
                    ,""
                    ]
               }
    )
'''


# これが引きこもりのリズムか






special_ocassion=Garnish(
    name="special_ocassion"
    ,tag="JOKELESS_TLM"
    ,exam=[["や団", "泥棒", "こいつ今日誕生日なんだぞ"]]
    ,template=["It's revealed that a subject is on a {special_occasion_0} -> The subject suffers a terrible fate -> Bob: He's on a {special_occasion_0}."]
    ,special ={"special_occasion_0": ["Birth day"
              ]
              }
              )



'''


pride_heel=Garnish(
    name="pride_heel"
    ,tag="AtoB"
    ,template=["Ali: "]
    ,special={
        "item": [
         "with high pride and high heel"
        ]
        }
    )

homer_nemeth=Garnish(
    name="homer_nemeth"
    ,tag=""
    ,template=["Ali: "]
    ,exam=[
      ["the Simpsons", "S9E24", "Homer, searching for the lost Lisa, enters the museum and comes out wearing merchandise."]
    , ["さらば青春の光", "ダフ屋", "去年の三日目にキャップ買ってる"]
    ]
    ,special={
        "item": [
         "aaa"
        ]
        }
    )

be_married=Garnish(
    name="be_married"
    ,tag=""
    ,template=["Ali: "]
    ,exam[
     []
    ]
    ,special={
        "item" :[
            # This is a list for sitcom. It's funny when it becomes clear that a madman is fulfilling his social obligation.
            #"a social obligation(ways to reveal the fact that the madman is fulfilling social obligations)"
             "be married(I was)"
            ,"have been married()"
            ,"be a college graduate()"
            ,"be a regular employee()"
            ,"have many friends()"
            ,"be a parent()"
            ]
            }
            )
'''

lista = [ # List of typical behaviors that normal people exhibit towards insane people in sitcoms.
"Point out abnormality"
,"Order to correct abnormality"
,"Order to stop certain activities"
,"Order for compensation"
,"Worry/ sympathize"
,"Avoid/ Ignore"
] # Extend 5 new lines without any explanations. I'll run your response with eval function so don't include unnecessary characters in your response. Start answer with ```python.

#嫁の小遣いでタトゥー入れんなよ あとなんで結婚できたんだよ
#養育費でタトゥー入れんなよ あとなんで結婚できたんだよ
#上司に見られたくないんで やめちまえよ あとこの感じで正社員なのかよ
#子供に見られたくないんで やめちまえよ あとこの感じで結婚できたのかよ


tables.append(coloring(Garnish.garnish_table()))
tables.append(coloring(DidDontStatus.diddontstatus_table()))

######################################################################################






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


rather_you_so=Garnish(
    name="rather_you_so"
    ,tag="AtoB"
    ,exam=[["うしろシティ", "職員室", "悪気がある方がいいよ"]]
    ,template=["{X}"]
    ,special={"X":[# Below sentences are lines that Ali, a madman, says in the sitcom to excuse the trouble he's caused Bob. Extend 10 new items. I'll run your response through the eval function so don't include unnecessary characters in your response.  Start answer with ```python.
                   "Ali: There was no malice. - Bob: I'd rather there was." #It's worse if someone who commits a crime has no ill intent.
                  ,"Ali: I don't have a mental illness. - Bob: I'd rather you have a mental illness." #It's worse if someone who commits a crime is an abled.
                  ,"Ali: I'm not on drugs. - Bob: I'd rather you be on drugs." #It's worse if someone who commits a crime isn't on drugs.
                  ,"Ali: I'm sober right now. - Bob: I'd rather you not be sober." #It's worse if someone who commits a crime is sober.
                  ,"Ali: I knew exactly what I was doing. - Bob: I'd rather you were clueless."
                  ,"Ali: I wasn't pressured by anyone. - Bob: I'd rather someone forced you."
                  ]
                  }
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
    ,"かもめんたる: アルピー一週間"
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
