from dataclasses import dataclass, field
from typing import List, ClassVar
from IPython.display import HTML
import re
def coloring(text):
    patterns = {

    r'\{': '<span style="color: #b078ff; font-weight: bold;">{</span>',
    r'\}': '<span style="color: #b078ff; font-weight: bold;">}</span>',
    r'\(': '<span style="color: #ff47c8; font-weight: bold;">(</span>',
    r'\)': '<span style="color: #ff47c8; font-weight: bold;">)</span>',
    r',': '<span style="color: cyan;">,</span>',
    r'Ali': r'<span style="color: #FAC700;">Ali</span>',
    r'Bob': r'<span style="color: #57FA00;">Bob</span>',
    r'Cho': r'<span style="color: #46b9ff;">Cho</span>',

    }
    for pattern, styled_span in patterns.items():
        text = re.sub(pattern, styled_span, text)
    return text
###########################################################################################################
state_old=["(State_old)","Go to the bed at 20:00."]
state_unfunny=["(State unfunny)","Likes NONESTYLE."]
###########################################################################################################
univ_modifier_job=["You're better than~", "You're as good as~", "You can be a~", "You can be the next~", "Top class~"]


@dataclass
class Grade:
  ALL_GRADE: ClassVar[List['Grade']] = []
  grade_name:str
  grade_genre:str
  grade_s:list # High grade.  Requires proper noun for person or group or award.
  grade_i:list # Low grade.  Requires proper noun for person or group or award.
  modifier:list
  def __post_init__(self):
      Grade.ALL_GRADE.append(self)
      if self.grade_genre == "job":
            self.modifier += univ_modifier_job


grade_singer          =Grade("singer"           ,"job",["singer"],["idol", "rapper", "Aquatimez", "Orange range", "Britney Spears"],[])
grade_instrumentalist =Grade("instrumentalist"  ,"job",["pianist", "guitarist"],["cymbalist", "bassist"],[])
grade_comedian        =Grade("comedian"         ,"job",["comedian", "Hitoshi Matsumoto"],["Vtuber", "idol", "tv talent", "voice actor", "Tsuyoshi Muro"],[])
grade_writer          =Grade("novelist"         ,"job",["the Nobel Prize in Literature", "J.K. Rowling"], ["Narou novelist", "Hiro Mizushima", "tabloid writer"], [])
grade_artist          =Grade("artist"           ,"job",["Picasso", "Turner Prize"], ["contemporary artist", "Toru Mitsumune"], [])
grade_doctor          =Grade("doctor"           ,"job",["neurosurgeon", "cardiologist"], ["dermatologist", "internal medicine doctor", "nurse."], [])
grade_researcher      =Grade("researcher"       ,"job",["mathematician", "Albert Einstein"], ["gender studies researcher", "Chizuruko Ueno"], [])
grade_actor           =Grade("actor"            ,"job",["Hollywood star", "Academy Award", "Gary Oldman"], ["TV drama actor", "Stallone"], [])
grade_chef            =Grade("chef"             ,"job",["Michelin restaurant", "Gordon Ramsay"], ["McDonalds", "Jiro inspires"], [])
grade_car             =Grade("car"              ,"",["57T Tourer", "Lamborghini"],["Nbox", "Prius"],["fully custom", "restored (year) type"])
grade_show_location   =Grade("show location"    ,"",["Shibuya Kokaido"],["Toshima Ward Community Center", "Chichibu Rental Conference Room", "McDonald's Takasaki No. 2 Store Parking Lot"],[])
grade_female_celebrity=Grade("Female celebrities whose Bob attends Ali",""     ,["Nogizaka 46"],["Ayaman Japan"],["Ex ~", "The most popular girl in ~", "Someone from ~"])
grade_university      =Grade("university"       ,"",["Tokyo Univ.", "National University"],["Tokyo MODE Gakuen", "Private University"],["A grade", "passed for active duty"])
grade_psycho_criminal =Grade("grade_psycho_criminal","",["murder", "terrorist"],["groper", "voyeurist"],["Repeat offender"])
grade_athlete         =Grade("athlete"          ,"job",["Kyojin", "Baseball player"], ["DeNA", "Billiards player"],["Top class", "First team"])

###########################################################################################################
@dataclass
class Effort:
  ALL_EFFORT: ClassVar[List['Effort']] = []
  effort:list # Stereotypical effort in reality or fiction. 
  def __post_init__(self):
      Effort.ALL_EFFORT.append(self)

univ_effort_creator=["Traveling for inspiration", "Abstinence", "Sublimating one's trauma into a work of art", "Use LSD", "Meditation", "Keeping a dream journal"]

effort_singer                =Effort([univ_effort_creator, "Quit smoking"]) 
effort_instrumentalist       =Effort([univ_effort_creator, "Quit smoking"])
effort_comedian              =Effort(["Abstinence", "People-watching"])
effort_writer                =Effort([univ_effort_creator])
effort_artist                =Effort([univ_effort_creator, "Creating art in the dark"])
effort_doctor                =Effort(["Abstinence", "Use nootropics"])
effort_researcher            =Effort([univ_effort_creator])
effort_actor                 =Effort([univ_effort_creator, "Method acting"])
effort_chef                  =Effort([])
effort_examinee              =Effort(["Use nootropics", "Study all night", "Making flashcards", "Memorizing"])
effort_athlete               =Effort(["Intense physical training", "Strict diet regimen", "Ice baths for recovery", "Altitude training", "Studying opponents", "Maintaining a consistent sleep schedule", "Practicing mindfulness"])

# Define effort_athlete in English and out put only that instance. without any explanation. start answer with ```python. 

# Add new itmes in each instance in English without any explanation. start answer with ```python. 
###########################################################################################################
@dataclass
class Suffer:
  ALL_SUFFER: ClassVar[List['Suffer']] = []
  suffer:list # Stereotypical suffer in reality or fiction. 
  def __post_init__(self):
    Suffer.ALL_SUFFER.append(self)
  
univ_suffer_creator=["Plagiarism", "Conflict with producers", "Commercialism", "Creator's block", "Drug addiction", "alcohol addiction", "sex addiction", "Cannot surpass one's rival", "Cannot surpass one's past self", "Paparazzi", "Stalkers"]

suffer_singer               =Suffer([univ_suffer_creator])
suffer_instrumentalist      =Suffer([univ_suffer_creator])
suffer_comedian             =Suffer([univ_suffer_creator])
suffer_writer               =Suffer([univ_suffer_creator])
suffer_artist               =Suffer([univ_suffer_creator])
suffer_doctor               =Suffer(["The trauma of not being able to save a patient's life."])
suffer_researcher           =Suffer(["Plagiarism", "Not being able to get research funding", "Has white hair"])
suffer_actor                =Suffer([univ_suffer_creator, "The damage caused by method acting"])
suffer_chef                 =Suffer([])
suffer_examinee             =Suffer(["Exam pressure","Health issues due to long study hours","Intense competition","Balancing study and personal life","Fear that one failure will affect future","Pressure from parents and teachers","Self-loathing and loss of confidence","Deterioration of relationships with friends"])
suffer_athlete              =Suffer(["Career-ending injuries","Pressure from fans and media", "Doping scandals", "Burnout", "Post-retirement depression", "Eating disorders", "Chronic pain", "Concussions and long-term brain damage", "Stalker"])


# Define suffer_athlete in English and out put only that instance. without any explanation. start answer with ```python. 

# Add new itmes in each instance in English without any explanation. start answer with ```python. 

###########################################################################################################
@dataclass
class StereoAction:
  ALL_STEREOACTION: ClassVar[List['StereoAction']] = []
  stereoaction:list # Stereotypical action in reality or fiction. 
  def __post_init__(self):
    StereoAction.ALL_STEREOACTION.append(self)

univ_stereoaction_creator=["Support the American Democratic Party.", "Being interested in environmental issues.", "Getting involved in a cult"]

stereoaction_singer               =StereoAction([univ_stereoaction_creator, "Has suicidal thoughts"])
stereoaction_instrumentalist      =StereoAction([univ_stereoaction_creator, "Suddenly starts writing music on paper."])
stereoaction_comedian             =StereoAction([univ_stereoaction_creator])
stereoaction_writer               =StereoAction([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
stereoaction_artist               =StereoAction([univ_stereoaction_creator, "Has suicidal thoughts", "Being in a dark room"])
stereoaction_doctor               =StereoAction([])
stereoaction_researcher           =StereoAction(["Starting a religion after overthinking it", "Suddenly starts writing mathematical formulas on the wall."])
stereoaction_actor                =StereoAction([univ_stereoaction_creator])
stereoaction_chef                 =StereoAction(["Getting angry at customers for using condiments", "Yelling at kitchen staff"])
stereoaction_psycho_criminal      =StereoAction(["Talking to imaginary friends", "Collecting trophies from victims", "Writing manifestos", "Obsessively stalking targets", "Creating elaborate traps or puzzles", "Claim responsibility"])
stereoaction_athlete              =StereoAction(["Getting involved in a cult", "Splurge", "Bullying nerds", "Support the Republican Party", "Trash Talk"])

# Define stereoaction_psycho_criminal in English and out put only that instance. without any explanation. start answer with ```python. 
# Add new itmes in each instance in English without any explanation. start answer with ```python. 

###########################################################################################################

@dataclass
class StereoAppear:
  ALL_STEREOAPPEAR: ClassVar[List['StereoAppear']] = []
  stereoappear:list # Stereotypical appearance in reality or fiction. 
  def __post_init__(self):
    StereoAppear.ALL_STEREOAPPEAR.append(self)

stereoappear_singer               =StereoAppear(["Many piercings", "Many tattoos", "Colorful hair"])
stereoappear_instrumentalist      =StereoAppear(["Many piercings", "Many tattoos", "Colorful hair"])
stereoappear_comedian             =StereoAppear([])
stereoappear_writer               =StereoAppear(["Wears a samue", "Has a beard", "Thin and pale", "Has messy hair"])
stereoappear_artist               =StereoAppear(["Many piercings", "Many tattoos", "Colorful hair"])
stereoappear_doctor               =StereoAppear(["White coat", "Messy hair"])
stereoappear_researcher           =StereoAppear(["White coat", "Messy hair", "Has bags under one's eyes", "Carries around a clipboard", "using a wheelchair"])
stereoappear_actor                =StereoAppear([])
stereoappear_chef                 =StereoAppear(["Kaiser moustache", "Being fat", "Has a thick accent"])
stereoappear_psycho_criminal      =StereoAppear(["Unkempt appearance", "Wild eyes", "Scars or burn marks", "Twitchy movements", "Wears all black", "Clown-like makeup"])
stereoappear_athlete = StereoAppear(["Muscular build", "Athletic wear", "Sweatbands", "Sports gear", "Taped joints or limbs", "Shaved body", "Visible tan lines", "Team jersey or uniform", "Dreadlocks"])


# Define stereoappear_athlete in English and out put only that instance. without any explanation. start answer with ```python. 

# Add new itmes in each instance in English without any explanation. start answer with ```python. 

###########################################################################################################

@dataclass
class Press:
  ALL_PRESS: ClassVar[List['Press']] = []
  press:list
  def __post_init__(self):
    Press.ALL_PRESS.append(self)

press_singer               =Press(["Sudden vacancy"])
press_instrumentalist      =Press(["Sudden vacancy"])
press_comedian             =Press(["Sudden vacancy"])
press_writer               =Press(["Sudden vacancy", "Ghost writer"])
press_artist               =Press([])
press_doctor               =Press(["Suddenly ill"])
press_researcher           =Press(["Bomb Defusal", "Death Game", "Zombie Pandemic"])
press_actor                =Press(["Sudden vacancy"])
press_chef                 =Press(["Sudden vacancy"])
press_old                  =Press(["An old potter is urgently looking for a successor.", "A middle-aged person is urgently looking for a marriage partner."])
press_athlete              =Press(["Suddeen vacancy", "Death Game","Zombie Pandemic","Life saving scene"])

###########################################################################################################

@dataclass
class SaleScout:
  ALL_SALESCOUT: ClassVar[List['SaleScout']] = []
  sale:list
  scout:list
  def __post_init__(self):
    SaleScout.ALL_SALESCOUT.append(self)
    for i in SaleScout.ALL_SALESCOUT:
        i.sale+=["training", "text"]

salescout_singer          =SaleScout(["His content"],["Bob finds out their performance."])
salescout_instrumentalist =SaleScout(["His content"],["Bob finds out their performance."])
salescout_comedian        =SaleScout(["His content"],["Bob finds out their performance."])
salescout_writer          =SaleScout(["His content"],["Bob finds out their performance."])
salescout_artist          =SaleScout(["His content"],["Bob finds out their performance."])
salescout_doctor          =SaleScout([],["Bob finds out their test scores."])
salescout_researcher      =SaleScout(["nootropics"],["Bob finds out their test scores."])
salescout_actor           =SaleScout(["His content"],["Bob finds out their performance."])
salescout_chef            =SaleScout(["His content"],["Bob eats their dishes."])
salescout_athlete         =SaleScout(["Supplement"],["Bob finds out their performance."])

########################################################################################################### 




###########################################################################################################
@dataclass
class Agent:
  ALL_AGENT: ClassVar[List['Agent']] = []
  agent_name: str
  s_Grade: Grade
  s_Effort: Effort
  s_Suffer: Suffer
  s_StereoAction: StereoAction
  s_StereoAppear: StereoAppear
  s_Press: Press
  state: list = field(default_factory=list)  # Initialize state as an empty list

  def __post_init__(self):
    Agent.ALL_AGENT.append(self)

agent_singer                =Agent("singer", [grade_singer, grade_car, grade_show_location, grade_female_celebrity], effort_singer, suffer_singer, stereoaction_singer, stereoappear_singer, press_singer,[])
agent_instrumentalist       =Agent("instrumentalist", [grade_instrumentalist, grade_car, grade_show_location, grade_female_celebrity], effort_instrumentalist, suffer_instrumentalist, stereoaction_instrumentalist, stereoappear_instrumentalist, press_instrumentalist,[])
agent_comedian              =Agent("comedian", [grade_comedian, grade_car, grade_show_location, grade_female_celebrity], effort_comedian, suffer_comedian, stereoaction_comedian, stereoappear_comedian, press_comedian,[state_unfunny])
agent_old                   =Agent("old",[],None,None,None,None,press_old,[state_old])
agent_writer                =Agent("writer", [grade_writer, grade_car], effort_writer, suffer_writer, stereoaction_writer, stereoappear_writer, press_writer,[])
agent_artist                =Agent("artist", [grade_artist, grade_car, grade_show_location, grade_female_celebrity], effort_artist, suffer_artist, stereoaction_artist, stereoappear_artist, press_artist,[])
agent_doctor                =Agent("doctor", [grade_doctor, grade_car, grade_female_celebrity], effort_doctor, suffer_doctor, stereoaction_doctor, stereoappear_doctor, press_doctor,[])
agent_researcher            =Agent("researcher", [grade_researcher], effort_researcher, suffer_researcher, stereoaction_researcher, stereoappear_researcher, press_researcher,[])
agent_actor                 =Agent("actor", [grade_actor, grade_car, grade_show_location, grade_female_celebrity], effort_actor, suffer_actor, stereoaction_actor, stereoappear_actor, press_actor,[])
agent_chef                  =Agent("chef", [grade_chef, grade_car], effort_chef, suffer_chef, stereoaction_chef, stereoappear_chef, press_chef,[])
agent_examinee              =Agent("examinee", [grade_university, grade_doctor], effort_examinee, suffer_examinee, None, None, None,[])
agent_psycho_criminal       =Agent("psycho criminal", [grade_psycho_criminal], None, None, stereoaction_psycho_criminal, stereoappear_psycho_criminal, None,[]) 
agent_athlete              =Agent("athlete", [grade_athlete, grade_car, grade_show_location, grade_female_celebrity], effort_athlete, suffer_athlete, stereoaction_athlete, stereoappear_athlete, press_athlete,[])


def gps_func():
    base=[]
    base.append(f"""<table>
    <tr><th></th><td></td></tr>
    <tr><th>ぼったくりバー(ファイヤーサンダー)      </th><td rowspan="6">Ali executes ({{s_Suffer}}, {{s_Effort}}, {{s_StereoAction}}, {{s_StereoAppear}}, {{s_Press}}). -> Ali was pointed out that he's {{grade_i}}, not {{grade_s}}.</td></tr>
    <tr><th>立ち退き(ファイヤーサンダー)            </th>
    <tr><th>依存症(さらば青春の光)                  </th>
    <tr><th>手タレ(Aマッソ)                         </th>
    <tr><th>ヨハン(インパルス)                      </th>
    <tr><th>ベース(ニューヨーク)                    </th>
    <tr><th>結婚相手(ロビンフット)                  </th><td rowspan="4">Ali executes ({{state}}, be a {{grade_i}}). -> Ali was pointed out that it's {{state_name}}. </td></tr> 
    <tr><th>後継者(さらば青春の光)                  </th>
    <tr><th>パワースポット(さらば青春の光)          </th>
    <tr><th>持たんの(だーりんず)                    </th>
    <tr><th>吉本行ったらええねん(ファイヤーサンダー)</th><td>Ali executes ({{state}}, be a {{grade_i}}). -> Ali was recommended {{grade_i}}. </td></tr> 
    </table>""")


    for i in Agent.ALL_AGENT:

      col_grade=[]
      col_effort=[]
      col_suffer=[]
      col_stereoaction=[]
      col_stereoappear=[]
      col_press=[]
      if i.s_Grade:
        for j in i.s_Grade:
          col_grade.append(f"""
          <tr><th>grade_name</th><td>{j.grade_name} </td></tr>
          <tr><th>grade_s   </th><td>{j.grade_s}    </td></tr>
          <tr><th>grade_i   </th><td>{j.grade_i}    </td></tr>
          <tr><th>modifier  </th><td>{j.modifier}   </td></tr>
          """)
      if i.s_Effort:
        col_effort.append(f"""
          <tr><th>s_Effort</th><td>{i.s_Effort.effort}</td></tr>
          """)
      if i.s_Suffer:
        col_suffer.append(f"""
          <tr><th>s_Suffer</th><td>{i.s_Suffer.suffer}</td></tr>
          """)
      if i.s_StereoAction:
        col_stereoaction.append(f"""
          <tr><th>s_StereoAction</th><td>{i.s_StereoAction.stereoaction}</td></tr>
          """)
      if i.s_StereoAppear:
        col_stereoappear.append(f"""
          <tr><th>s_StereoAppear</th><td>{i.s_StereoAppear.stereoappear}</td></tr>
          """)
      if i.s_Press:
        col_press.append(f"""
          <tr><th>s_Press</th><td>{i.s_Press.press}</td></tr>
          """)
      if i.state == None:
        i.state = []

      base.append(f"""<table>
      <tr><th>agent_name</th><td>{i.agent_name}</td></tr>
      {", ".join(col_grade)}
      {", ".join(col_effort)}
      {", ".join(col_suffer)}
      {", ".join(col_stereoaction)}
      {", ".join(col_stereoappear)}
      {", ".join(col_press)}
      <tr><th>state</th><td>{i.state}</td></tr>
      </table>""")
    return coloring('<br>'.join(map(str, base)))



HTML(''.join(gps_func())) 



