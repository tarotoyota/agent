class Hyhy:
  def __init__(self, name, doerC, typical_hypo, atypical_hypo):#Instances of this class must be those whose practitioners are frequently the subject of movies, dramas, and documentaries.
    self.name=name#The item's hypernyms
    self.doerC=doerC#C stands for "common noun"
    self.typical_hypo=typical_hypo  #typical hyponyms of the item that is often the subject of dramas or movies. 
    self.atypical_hypo=atypical_hypo#atypical hyponyms of the item that is almost never the subject of dramas or movies. Or its hyponyms that are seen as lowly, minor or uncool.
hyhy_club_activity       = Hyhy("club activity"    ,""              ,["tennis club","baseball club"]                 ,["Japanese tea ceremony club","craft club","gardening club"]))
hyhy_gamble              = Hyhy("gamble"           ,"gambler"       ,["poker","pachinko","horseracing"]              ,["TOTO","BINGO"])
hyhy_written_works       = Hyhy("written works"    ,"writer"        ,["novel","poem"]                                ,["tabloid article","sales copy","clickbait articles"])
hyhy_music               = Hyhy("composition"      ,"musician"      ,["rock music","hip hop"]                        ,["piped music","advertising jingle", "Sound effect"])
hyhy_game                = Hyhy("game"             ,"e-sport player",["Rainbow Six Siege","Street fighter"]          ,["ジャカジャカジャンケン","釣り★スタ"])
hyhy_comic               = Hyhy("comic"            ,"comic writer"  ,["ジャンプ漫画"]                                  ,["youtubeの漫画動画","実話系雑誌の漫画","風俗店の体験漫画"])
hyhy_academics           = Hyhy("academics"        ,"scientist"     ,["Physics", "Chemistry", "Biology"]             ,["Art History", "Gender Studies"])
#hyhy_illness             = Hyhy("illness"          ,"",["cancer","Leukemia"]                           ,["Phimosis","Developmental disorder"])
hyhy_cuisine             = Hyhy("cuisine"          ,"chef"          ,["french cuisine", "Italian cuisine"]           ,["fast food"])
hyhy_photography         = Hyhy("photography"      ,"photographer"  ,["landscape photography","portrait photography"],["Voyeurism", "paparazzi"])
hyhy_dance               = Hyhy("dance"            ,"dancer"        ,["Hip-hop dance", "Ballet"]                     ,["strip show"])
#hyhy_gardening           = Hyhy("gardening"        ,"farmer",["Floriculture", "Vegetable cultivation"]       ,["cannabis cultivation","Cultivating flowers for delivery to cabarets."])
hyhy_bar                 = Hyhy("bar"              ,"bartender"     ,["cocktail bar"]                                ,["rip-off bar"])
hyhy_actor               = Hyhy("actor"            ,"actor"         ,["starring"]                                    ,["extra","porn actor"])
hyhy_sport               = Hyhy("sport"            ,"athlete"       ,["soccer","basketball"]                         ,["competitive eating","finger wrestling"])#gpt3.5
hyhy_technology          = Hyhy("technology"       ,"engineer"      ,["artificial intelligence","virtual reality"]   ,["fax machine","pager","tech support", "data entry"])#gpt3.5
hyhy_craftsmanship       = Hyhy("craftsmanship"    ,"craftman"      ,["woodworking","blacksmithing"]                 ,["macaroni art","glue and glitter crafts"])#gpt3.5

class Famous:
  def __init__(self, famous_p, famous_n):
    self.famous_p=famous_p#Famous persons of the item. Proper noun only.
    self.famous_n=famous_n#Famous masterpieces or group of the item. Proper noun only.
famous_written_works    = Famous(["Haruki Murakami","Osamu Dazai","Isaac Asimov"]       , ["The Catcher in the Rye", "War and Peace", "1984"])
famous_music            = Famous(["Mozart","Komuro","Beatles"]                          , ["Ninth Symphony", "Symphony No. 5"])
famous_e-sport          = Famous(["Umehara"]                                            , [""])
famous_comic            = Famous(["Eiichiro Oda"]                                       , ["One Piece", "Dragon Ball"])
famous_academics        = Famous(["Einstein","Yukawa","Schopenhauer"]                   , ["Harvard University","MIT"])
famous_cuisine          = Famous(["Gordon Ramsay", "Julia Child", "Jamie Oliver"]       , ["The French Laundry", "El Bulli", "Noma"])
famous_photography      = Famous(["Ansel Adams", "Dorothea Lange", "Steve McCurry"]     , ["Moonrise, Hernandez", "Migrant Mother", "Afghan Girl"])#gpt3.5
famous_dance            = Famous(["Michael Jackson", "Misty Copeland", "Sylvie Guillem"], ["Thriller", "Swan Lake", "Giselle"])#gpt3.5
famous_actor            = Famous(["Leonardo DiCaprio", "Meryl Streep", "Tom Hanks"]     , ["The Revenant", "The Devil Wears Prada", "Forrest Gump"])#gpt3.5
famous_sport            = Famous(["Otani","Honda","Ichiro"]                             , ["RedSocks"])
famous_technology       = Famous(["Elon Musk", "Bill Gates", "Steve Jobs"]              , ["Tesla", "Microsoft", "Apple"])#gpt3.5
famous_craftsmanship    = Famous(["Gustav Stickley", "George Nakashima"]                , ["David", "Arc de Triomphe"])

class Distress:
  def __init__(self, distress):
    self.distress=distress#Risks and pain caused by performing the act
univ_creation_distress=["Suffering from pressure from oneself or from those around you.","feels overwhelmed by the pressure to constantly create","struggles a creative burnout","struggles with creative block","faces criticism for their work","is in conflict with the editor/producer.", "struggles with the gap between what he want to create and what my fans want.","is troubled by his inability to improve at it.","is worried about not having ideas or running out of ideas.","is struggles with stage fright"]
#Don't add elements that overlap with univ_creation_distress, univ_battle_distress and univ_injury_distress.

distress_sport          =Distress("is injured","failed to get into the starting lineup.","is hazed"])
distress_gambling       =Distress(["is addicted to gambling.","bankrupted himself due to gambling."])
distress_musician       =Distress([univ_creation_distress, "conflict with other band members."])
distress_written_works  =Distress([univ_creation_distress])

class Effort:
  def __init__(self, effort):
    self.effort=effort#In dramas where the main character is someone who engages in the act, the effort that the main character would make.
effort_actor       = Effort(["mimic the model everyday life.","mimic the model's health.","Observe the model.","Lose weight and become the model's weight.","Do the job of the model person."])
effort_gambling    = Effort(["study mathematic and statistics"])
effort_composition = Effort(["Study different artistic styles."])
effort_sport       = Effort(["Practice the sport daily.", "Train with a coach.", "Watch professional games for inspiration.", "Improve physical fitness.", "Learn and apply advanced techniques in the sport."])#gpt3.5

class Stereotype:
  def __init__(self, stereotype):
    self.stereotype=stereotype#Actions and remarks that are common to characters who are experts in the field that appear in dramas.
stereotype_scientist           = Stereotype(["He has a messy hair and wears eccentric clothing.","He wears a white coat and has a unkempt head of white hair","He is in a wheelchair","He always eats sweets","His behavior is childish","He has a robot assistant","His endings are ' ~なのじゃ.'","There are books and laboratory equipment scattered around the room.","He is shaking a flask filled with liquid.","He has dreams in which God tells him formulas."])
stereotype_composer            = Stereotype(["He has a messy hair and wears eccentric clothing.","He hears music in everyday sounds.","His compositions often reflect his emotional state.","He uses unconventional instruments in his compositions.",])
stereotype_athlete             = Stereotype(["He is competitive and always seeks to win.","He follows a specific diet and nutrition plan.","He is committed to teamwork and values his teammates."])
stereotype_novelist            = Stereotype(["He has a messy hair and wears eccentric clothing.","He always carries a notebook and a pen.","He is often lost in thought, even in the midst of conversation.","His living space is filled with books and scattered papers.","He has a favorite writing spot, like a cozy cafe or a quiet park.","He has a ritual before starting a new story, like drinking a specific type of tea."])

class Master_class_saraba:
    def __init__(self, pos, s_Hyhy, s_Famous, s_Distress, s_Effort, s_Stereotype) -> None:
        self.pos         =pos
        self.s_Hyhy      =s_Hyhy         if s_Hyhy        is not None else Hyhy("","","")
        self.s_Famous    =s_Famous       if s_Famous      is not None else Famous("","")
        self.s_Distress  =s_Distress     if s_Distress    is not None else Distress("")
        self.s_Effort    =s_Effort       if s_Effort      is not None else Effort("")
        self.s_Stereotype=s_Stereotype   if s_Stereotype  is not None else Stereotype("")

club_activity        =Master_class_saraba("saraba",      hyhy_club_activity,    famous_sport        ,    distress_sport        ,    effort_sport,    stereotype_athlete)
written_works        =Master_class_saraba("saraba",      hyhy_written_works,    famous_written_works,    distress_written_works,    None        ,    stereotype_athlete)

def saraba(argz):
  z_name, z_doerC, z_typical_hypo, z_atypical_hypo = argz.s_Hyhy.name, argz.s_Hyhy.doerC, argz.s_Hyhy.typical_hypo, argz.s_Hyhy.atypical_hypo#Hyhy
  z_famous_p, z_famous_n = argz.s_Famous.famous_p, argz.s_Famous.famous_n#Famous
  z_distress = argz.s_Distress.distress#Distress
  z_effort = argz.s_Effort.effort#Effort
  z_stereotype = argz.s_Stereotype.stereotype#Stereotype
base_en=["'sA' stands for 'Subject A', 'sB' stands for 'Subject B'"]#
base_jp=["'sA' は 'Subject A' の略。'sB' は 'Subject B' の略。"]#
accumulate_jp=["零 accumulate_jp"#乱数で選んだアイテムをプレースホルダに追加したところでこのプログラムの実用性は増さない。
            ,"弐 {z_name}"
            ,"三 {z_doerC}"
            ,"四 {z_distress}"
            ,"五 {z_effort}"
            ,"六 {z_stereotype}"
            ,"七 {z_famous_p, z_famous_n}"
            ,"一 There are sA and sB."
            ,"一 sA is working on ニ."
            ,"一 sB is sA’s (family / friend)."
            ,"一 sA calls himself a サ."
            ,"一 sA has pride and a sense of superiority (as an サ / as someone aspiring to be an サ)."#.pride(y/n)     
            ,"一 sA ヨ."
            ,"一 sA ゴ."
            ,"一 sA ロ."
            ,"一 sA はその活動のために、家族、友人、恋人との関係および彼自身の金銭・健康を蔑ろにしている。"#,"一 sA neglects his family, friends, romantic relationships, and his health and finances in order to pursue his goals."
            ,"一 1: sA が ナ をライバル視し、敵愾心とコンプレックスを持つ。"#,"一 1: sA sees ナ as rivals and has animosity and a complex with them."
            ,"一 1: sA が ナ と自身を比較し、自信を失う。"#"自信を失う"はpressuposition triggerとして"自信を持っていた" #,"一 1: sA compares himself with ナ and feels depressed."
            ,"一 2: sB が sA の話を聞き、彼の現況を心配する。"#,"一 2: sB is concerned about sA."
            ,"一 2: sB が sA の話、そして協力の要請に動揺する。"#,"一 2: sB is confused when asked for sA’s cooperation."
            ,"一 2: sB が sA の活動を助けず、それをやめるよう辛辣な態度を取る。"#,"一 2: sB doesn’t support sA’s goals but rather acts harshly to encourage sA to give up."
            #,"一 2: sB is dismissing sA’s advice curtly." z_typical_hypoの従事者がz_atypical_hypoの従事者の助言を無視する            
            # ,"一 S2 is S1’s (fan / family / producer / manager / coach)."              
            # ,"一 S2 calls S1 a さ."
            # ,"一 (S1 / S2) sees な as rivals and has animosity and a complex with them."
            # ,"一 (S1 / S2) compares S1 with な and feels depressed."
           ]
barashi_jp=["零 barashi_jp"
           ,"弐 {z_atypical_hypo}"            
#          ,"一 Disclose that sA is involved in に."
           ,"一 sB が sA に ニ に関連する活動を止めるよう乞う."#A: sB tells sA to quit ニ.
#          ,"一 単純開示: ('TOTO やめてよ'/依存症/さらば青春の光), ('AVやねん'/男優/さらば青春の光), ('手タレやねん'/マネージャー/Aマッソ), ('ここぼったくりバーやぞ'/バー/ライス, ファイヤーサンダー)"
           ]
fst1_jp   =["零 fst1_jp (z_atypical_hypo, z_doerC, z_name)"
           ,"一 sB が sA に対し以下を発言する。"
           ,"弐 {z_atypical_hypo}"
           ,"三 {z_doerC}"
           ,"四 {z_name}"
           ,"一 ニ に 巧拙はない。"
           ,"一 ニ は 評価されるほどやばい。"
           ,"一 ニ で プロ意識を持つな。"
           ,"一 ニ で スランプに入るな。"
           ,"一 ニ で プレッシャーを感じるな。誰も ニ に何をも期待しない。"
           ,"一 ニ を やっている奴 を サ に含むな。"
           ,"一 ニ を やっている奴 を ヨ に含むな。"            
           ,"一 ニ は サ になれなかった奴がなる。"
           ]
fst2_jp   =["零 fst2_jp (z_famous_p, z_famous_n)"
           ,"弐 {z_famous_p, z_famous_n}"
           ,"三 同族意識, ライバル意識, 劣等感, 嫉妬心, 憧れ"
           ,"一 ニ と自分を比較するな。"
           ,"一 ニ に サ を感じるな。"#.pressure
           ,"一 どうやったら ニ に サ を感じられる?"
           ]
#fst3_jp   =["零 fst3_jp (z_)"
#           ]

def get_words_Master_class_saraba():
    instances_list = [
        name for name, obj_instance in globals().items()
        if isinstance(obj_instance, Master_class_saraba) and 'saraba' in getattr(obj_instance, 'pos', [])
    ]
    return instances_list



#Subject1 is working on {x.Hyhy.name}.
#Subject1 {x.Distress.distress}.
#Subject1 {x.Effort.effort}
#Subject1 {x.Stereotype.stereotype}.
#Subject1 see {x.Famous.famous_p, x.Famous.famous_n} as a rival and has animosity and complex with it.
#Subject1 compares himself with {x.Famous.famous_p, x.Famous.famous_n} and feels depressed.
#Subject1 is working on {x.Hyhy.atypical_hypo}

#Subject2 tells subject1 not to compare yourself and them.
#Subject2 tells subject1 not to have professionalism.

#global_items=["is in conflict with the editor/producer.", "struggles with the gap between what he want to create and what my fans want."]
#"上達しない"はglobal_item // "~にのめり込むあまり大学を辞め、家族と別れる"はglobal_item//"is frustrated",
