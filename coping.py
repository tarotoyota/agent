from dataclasses import dataclass, field
from typing import List, ClassVar

# 教師データ: (さらば青春の光: パワースポット)

@dataclass
class Coping:
    ALL_COPING: ClassVar[List['Coping']] = []
    coping:str
    coping_adj:list
    access:list
    rel_mcjob:list
    confirm:list
    def __post_init__(self):
        Coping.ALL_COPING.append(self)
    def prompt(self):
        print(f"{self.rel_mcjob} often {self.access} {self.coping}.")      

spiritual_spot = Coping("spiritual_spot"
                        , ["unhappy", "poverty"]
                        , ["Near", "Touch"]
                        , ["a guard who guards that", "a cleaner who cleans that"] # guards and cleaners of a spiritual spot often near or touch the spritual spot.
                        , ["Is this the right place?", "Does it works?"])
spiritual_goods= Coping("spiritual_goods"
                        , ["unhappy", "poverty"]
                        , ["Near", "Touch"]
                        , ["a line worker who products that", "a carrier who carries that", "a clerk who sells that", "a warehouse worker who packs and ships that"]
                        , ["Does it works?"])
nootropics     = Coping("nootropics"
                        , ["illiteracy"]
                        , ["Drink"]
                        , []
                        , ["Does it works?"])
self_help_book = Coping("self_help_book"
                        , ["illiteracy", "unhappy", "poverty"]
                        , ["Read"]
                        , ["a editor who edits that", "a printer who prints that", "an audiobook narrator who related to that"]
                        , ["Does it works?"])
motivational_seminar = Coping("motivational_seminar"
                        , ["unhappy", "poverty", "illiteracy"]
                        , ["Attend", "Listen to"]
                        , ["a venue staff who sets up for that", "a sound technician who manages audio for that"]
                        , ["Does it works?"])

# Stateに.i_canを増設?

def coping_table():
  base=[
  """
  <table id='progression'>
  <tr><td>Ali becomes interested in the {coping}. But Bob, {rel_mcjob}, is {coping_adj}.</td></tr>
  <tr><td>Every time Ali hears that Bob is x, Ali {confirm}.</td></tr>
  </table>
  """      
  ]
  for i in Coping.ALL_COPING:
    if i.coping_adj:
      for j in i.coping_adj:
        col_coping_adj=[]
        col_coping_adj.append(f"<a href='state#{j}'>{j}</a>")
    base.append(f"""
    <table id={i.coping}>
    <tr><th id='th_cyan'>coping</th><th id='th_cyan'>{i.coping}</th></tr>
    <tr><th id='th_cyan'>coping_adj</th><td>{i.coping_adj}</td></tr>
    <tr><th id='th_cyan'>rel_mcjob</th><td>{i.rel_mcjob}</td></tr>
    {"".join(col_coping_adj)}
    </table>
    """)
  return base

# Define motivational_seminar


