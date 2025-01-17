# /home/tarotoyota/agent_output.py
import agent_inst
import re
import random

def coloring(text):
    patterns = {
    r'\{': '<span style="color: #7634d2; font-weight: bold;">{</span>',
    r'\}': '<span style="color: #7634d2; font-weight: bold;">}</span>',
    r'\(': '<span style="color: #ff47c8; font-weight: bold;">(</span>',
    r'\)': '<span style="color: #ff47c8; font-weight: bold;">)</span>',
    r',': '<span style="color: cyan;">,</span>',
    r'Ali': r'<span style="color: #FAC700;">Ali</span>',
    r'Bob': r'<span style="color: #57FA00;">Bob</span>',
    r'Cho': r'<span style="color: #46b9ff;">Cho</span>',
    r'\+s\+': r'<span style="color: #ff47c8;">+s+</span>',
    r'\+l\+': r'<span style="color: #ff47c8;">+l+</span>',
    r'\+f\+': r'<span style="color: #ff47c8;">+f+</span>',
    }
    for pattern, styled_span in patterns.items():
        text = re.sub(pattern, styled_span, text)
    return text


def progression_table():
    after_reveal        = "Ali is a {instance_name}, but he's a {hypo_i}, not a {hypo_s}."

    before_stereo       = "Ali, a {instance_name}, is jealous of {hypo_s, hypo_s_pn} and looks down on {hypo_i, hypo_i_pn}. Ali executes {Appear}, {Action}, {Suffer}, {Effort}, {Slump}, {imposing}. Ali calls {rephrase[0]} {rephrase[1]}. "
    after_stereo        = "Bob criticizes Ali using expressions from <a href='agent_dont_et_al'>{agent_dont}</a>."
    before_pressure1    = "{pressure1}. Bob is mistaking Ali for a {hypo_s}"
    before_pressure2    = "{pressure2}. Bob is annoyed by Ali."
    before_pressure3    = "{pressure3}. Bob needs help. Ali steps foward. Bob is mitaking Ali for a {hypo_s}."
    before_pressure4    = "Ali tries to sell {pressure4} to Bob. Bob is annoyed by Ali."
    before_charity      = "Ali {charity} someone."

    before_sad_past     = "Bob finds out that Ali's <a href='agent_dont_et_al'>{Sad_past}</a>."
    after_sad_past      = "Bob says <a href='agent_dont_et_al'>{sad_past_f}</a>."
    after_bottom        = "Ali says <a href='agent_dont_et_al'>{bottom_reveal}  </a>. Bob finds out that Ali is a <a href='agent_dont_et_al'>{Bottom}</a>."
    after_reverse_adj   = "Ali executes {reverse_adj}. Bob criticizes this."
    after_garnish       = "<a href='start_garnish_period_html'>{garnish}</a> garnishes this sketch."

    progression_table_result = f"""
    <details>
    <summary>hsi</summary>
    <table id='progression'>
    <tr><th>                           hsi          </th><th> BEFORE REVEAL      </th><th> AFTER REVEAL({after_reveal})  </th></tr>
    <tr><th id="th_cyan">              stereo       </th><td> {before_stereo}    </td><td rowspan="6">{after_stereo}     </td></tr>
    <tr><th id="th_cyan" rowspan="5">  pressure     </th><td> {before_pressure1} </td></tr>
                                                         <td> {before_pressure2} </td></tr>
                                                         <td> {before_pressure3} </td></tr>
                                                         <td> {before_pressure4} </td></tr>
                                                         <td> {before_charity}   </td></tr>
    <tr><th id="th_orange">            bottom       </th><td>                    </td><td>{after_bottom}                 </td></tr>
    <tr><th id="th_orange">            sad_past     </th><td> {before_sad_past}  </td><td>{after_sad_past}               </td></tr>
    <tr><th id="th_cyan">              reverse_adj  </th><td>                    </td><td>{after_reverse_adj}            </td></tr>
    <tr><th id="th_lime">              garnish      </th><td>                    </td><td>{after_garnish}                </td></tr>
    </table>
    </details>
    """
    return progression_table_result

def progression_table2():

    after_reveal = "Bob {reverse_adj}"
    before_seed = "Ali talks with Bob, a {agent_name}. Ali has {did_a}. Ali says '{hard}'. Bob says '{advice}'"
    after_seed  = "Ali says 'I wanna {wanna}', 'Have I {did_a}?', '{hard}', 'This guy said to me '{advice}', 'Are there any {agent_name} who doesn't {reverse_adj}?'"
    after_garnish       = "<a href='start_garnish_period_html'>{garnish}</a> garnishes this sketch."


    progression_table_result2 = f"""
    <details>
    <summary>seer</summary>
    <table id='progression2'>
    <tr><th>                           seer         </th><th> BEFORE REVEAL      </th><th> AFTER REVEAL({after_reveal})  </th></tr>
    <tr><th id="th_cyan">              seed         </th><td> {before_seed}      </td><td>{after_seed}                   </td></tr>
    <tr><th id="th_lime">              garnish      </th><td>                    </td><td>{after_garnish}                </td></tr>
    </table>
    </details>
    """
    return progression_table_result2

def agent_func():

    seed = random.randint(0, 1000000)  # または任意の範囲
    random.seed(seed)
    seed_str = str(seed)

    def make_arg_1_list(items, seed=None):  # 引数を1つのlistに変換

        result = []
        flattened = []

        def flatten(item):
            if isinstance(item, (str, int, float, bool)):
                flattened.append(str(item))
            elif isinstance(item, (list, tuple)):
                for sub_item in item:
                    flatten(sub_item)
            elif isinstance(item, dict):
                for k, v in item.items():
                    flattened.append(f"{k}: {', '.join(make_arg_1_list([v], seed))}")
            else:
                flattened.append(str(item))

        flatten(items)

        if not flattened:  # リストが空の場合
            return []

        if seed is not None:
            random.seed(seed)  # Set the seed for reproducibility

        red_index = random.randint(0, len(flattened) - 1)  # ランダムな1つのアイテムの背景色を変更 # col_link_to_reverse_adjに適用しないように

        for index, item in enumerate(flattened):
            if index == red_index:
                result.append(f'<span style="background-color: #331313;">{item}</span>')
            else:
                result.append(item)

        return result



    base=[f"SEED: {seed_str}"]
    base.append(progression_table())
    base.append(progression_table2())
#    base.append(progression_table3())

    pressure1=[ "Bob, a Mom-and-pop restaurant owner, offers Ali free meal.","Bob, a landlord, generously waits for Ali to pay her overdue rent.","Bob, a employer, offers Ali a flexible part-time job.","Bob, a professional, offers Ali the training.","Bob, Ali's girlfriend's father, allows them to marry.","Bob, a kind taxi driver, gives Ali free rides to job interviews.","Bob, a wealthy investor, provides Ali with startup funding."]

    for i in agent_inst.Agent.ALL_AGENT:
        col_grade, col_effort, col_suffer, col_action, col_appear, col_pressure1, col_pressure2, col_pressure3, col_brand, col_revealer, col_rephrase, col_imposing, col_slump, col_cant, col_too_slow, col_garnishallow, col_charity, col_rev_adj, col_southpaw, col_pressure = [],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        col_too_late= []
        col_modifier= []

        if i.agent_name                  :col_grade              .append(f"<tr><th id='th_cyan'>instance_name           </th><th id='th_cyan'>{i.agent_name         }               </th></tr>")
        if i.s_Grade.hypo_s              :col_grade              .append(f"<tr><th id='th_cyan'>hypo_s                  </th><td>{i.s_Grade.hypo_s                  }               </td></tr>")
        if i.s_AbnormalCliche            :col_grade              .append(f"<tr><th id='th_cyan'>hypo_s(AbnormalCliche)  </th><td>{i.s_AbnormalCliche.cliche_agent   } in .hypo_s    </td></tr>")
        if i.s_Grade.hypo_s_pn           :col_grade              .append(f"<tr><th id='th_cyan'>hypo_s_pn               </th><td>{i.s_Grade.hypo_s_pn               }               </td></tr>")
        if i.s_Grade.hypo_i              :col_grade              .append(f"<tr><th id='th_cyan'>hypo_i                  </th><td>{i.s_Grade.hypo_i                  }               </td></tr>")
        if i.s_AbnormalCliche            :col_grade              .append(f"<tr><th id='th_cyan'>hypo_i(AbnormalCliche)  </th><td>{i.s_AbnormalCliche.abnormal       }               </td></tr>")
        if i.s_AbnormalCliche            :col_grade              .append(f"<tr><th id='th_cyan'>hypo_i(AbnormalCliche)  </th><td>{i.s_AbnormalCliche.cliche_agent   } in .hypo_i    </td></tr>")
        if i.s_Grade.hypo_i_pn           :col_grade              .append(f"<tr><th id='th_cyan'>hypo_i_pn               </th><td>{i.s_Grade.hypo_i_pn               }               </td></tr>")
        if i.s_Binary2.appear            :col_appear             .append(f"<tr><th id='th_cyan'>Appear                  </th><td>{i.s_Binary2.appear                }               </td></tr>")
        if i.s_Binary2.action            :col_action             .append(f"<tr><th id='th_cyan'>Action                  </th><td>{i.s_Binary2.action                }               </td></tr>")
        if i.s_AbnormalCliche            :col_action             .append(f"<tr><th id='th_cyan'>Action(AbnormalCliche)  </th><td>{i.s_AbnormalCliche.cliche         }               </td></tr>")
        if i.s_Binary2.suffer            :col_suffer             .append(f"<tr><th id='th_cyan'>Suffer                  </th><td>{i.s_Binary2.suffer                }               </td></tr>")
        if i.s_Binary2.effort            :col_effort             .append(f"<tr><th id='th_cyan'>Effort                  </th><td>{i.s_Binary2.effort                }               </td></tr>")
        if i.s_Binary2.slump             :col_slump              .append(f"<tr><th id='th_cyan'>Slump                   </th><td>{i.s_Binary2.slump                 }               </td></tr>")
        if i.s_rephrase                  :col_rephrase           .append(f"<tr><th id='th_cyan'>rephrase                </th><td>{i.s_rephrase                      }               </td></tr>")
#       if i.s_Pressure                  :col_pressure1          .append(f"<tr><th id='th_cyan'>pressure1               </th><td>{pressure1                         }               </td></tr>")
#       if i.s_Pressure                  :col_pressure2          .append(f"<tr><th id='th_cyan'>pressure2               </th><td>{i.s_Pressure.pressure2            }               </td></tr>")
#       if i.s_Pressure                  :col_pressure3          .append(f"<tr><th id='th_cyan'>pressure3               </th><td>{i.s_Pressure.pressure3            }               </td></tr>")
        if i.s_Binary2.pressure          :col_pressure           .append(f"<tr><th id='th_cyan'>pressure4               </th><td>{i.s_Binary2.pressure              }               </td></tr>")
        if i.s_Binary2.brand             :col_brand              .append(f"<tr><th id='th_cyan'>pressure4               </th><td>{i.s_Binary2.brand                 }               </td></tr>")
        if i.s_revealer                  :col_revealer           .append(f"<tr><th id='th_cyan'>revealer                </th><td>{i.s_revealer                      }               </td></tr>")
        if i.s_Binary2.rev_adj           :col_rev_adj            .append(f"<tr><th id='th_cyan'>rev_adj                 </th><td>{i.s_Binary2.rev_adj               }               </td></tr>")
        if i.s_Binary2.too_late          :col_too_late           .append(f"<tr><th id='th_cyan'>too_late                </th><td>{i.s_Binary2.too_late              }               </td></tr>")
        if i.s_Binary2.modifier          :col_modifier           .append(f"<tr><th id='th_cyan'>modifier                </th><td>{i.s_Binary2.modifier              }               </td></tr>")
        if i.s_Binary2.just_a            :col_imposing           .append(f"<tr><th id='th_cyan'>imposing                </th><td>{i.s_Binary2.just_a                }               </td></tr>")
        if i.s_Binary2.charity           :col_charity            .append(f"<tr><th id='th_cyan'>charity                 </th><td>{i.s_Binary2.charity               }               </td></tr>")
        if i.s_Binary2.southpaw          :col_southpaw           .append(f"<tr><th id='th_cyan'>southpaw                </th><td>{i.s_Binary2.southpaw              }               </td></tr>")
        if i.s_GarnishAllow.allowed_garnish:col_garnishallow     .append(f"<tr><th id='th_cyan'>allowed_garnish         </th><td>{i.s_GarnishAllow.allowed_garnish  }               </td></tr>")

        base.append(f"""<table id="{i.agent_name}">
        {"".join(col_grade)}
        {"".join(col_appear)}
        {"".join(col_action)}
        {"".join(col_suffer)}
        {"".join(col_effort)}
        {"".join(col_slump)}

        {"".join(col_rephrase)}
        {"".join(col_pressure)}
        {"".join(col_brand)}

        {"".join(col_revealer)}
        {"".join(col_rev_adj)}
        {"".join(col_cant)}
        {"".join(col_too_slow)}

        {"".join(col_too_late  )}
        {"".join(col_modifier  )}
        {"".join(col_imposing)}
        {"".join(col_charity)}
        {"".join(col_southpaw)}

        {"".join(col_garnishallow  )}

        </table>""")

    return coloring(''.join(base))

'''
        if i.s_b2scene                   :col_b2scene            .append(f"<tr><th id='th_cyan'>pressure2       </th><td>{make_arg_1_list(i.s_b2scene + b2scene_univ    )}</td></tr>")
        if i.s_b3scene                   :col_b3scene            .append(f"<tr><th id='th_cyan'>pressure3       </th><td>{make_arg_1_list(i.s_b3scene                   )}</td></tr>")
        if i.s_Binary.paid_item          :col_paid_item          .append(f"<tr><th id='th_cyan'>pressure4       </th><td>{make_arg_1_list(i.s_Binary.paid_item          )}</td></tr>")
'''
