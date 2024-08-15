#from IPython.display import HTML
import agent_inst
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


def agent_func():
    base=[]
    base.append("""<table>
    <tr><th>Progression ID</th><th>Progression</th><th>Practical examples</th></tr>
    <tr><th>TOTO     </th><td>Ali executes ({s_Suffer}, {s_Effort}, {s_StereoAction}, {s_StereoAppear}, {s_Press}). -> Ali was pointed out that he's {grade_i}, not {grade_s}.</td><td>ぼったくりバー(ファイヤーサンダー), 立ち退き(ファイヤーサンダー), 依存症(さらば青春の光), 男優(さらば青春の光), 手タレ(Aマッソ), ヨハン(インパルス), ベース(ニューヨーク)</td></tr>
    <tr><th>POTTER   </th><td>Ali executes ({state}, be a {grade_i}). -> Ali was pointed out that it's {state_name}. </td><td>結婚相手(ロビンフット), 後継者(さらば青春の光), パワースポット(さらば青春の光), 持たんの(だーりんず)</td></tr>
    <tr><th>YOSHIMOTO</th><td>Ali executes ({state}, be a {grade_i}). -> Ali was recommended {grade_i}. </td><td>吉本行ったらええねん(ファイヤーサンダー)</td></tr>
    <tr><th>AMNESIA  </th><td>Ali, who has amnesia, remembers that he was {grade_name}. -> Ali learns that he was executing {{state}}. </td><td>記憶喪失(うしろシティ)</td></tr>
    </table>""")



    for i in agent_inst.Agent.ALL_AGENT:

        col_grade=[]
        col_effort=[]
        col_suffer=[]
        col_stereoaction=[]
        col_stereoappear=[]
        col_press=[]
        col_state=[]
        j_grade_name, j_grade_s, j_grade_i = [], [], []

        if i.s_Grade:
          for j in i.s_Grade:
            col_grade.append(f"""
            <tr><th>grade_name</th><td>{j.grade_name} </td></tr>
            <tr><th>grade_s   </th><td>{j.grade_s}    </td></tr>
            <tr><th>grade_i   </th><td>{j.grade_i}    </td></tr>
            <tr><th>modifier  </th><td>{j.modifier}   </td></tr>
            """)
            if j.grade_genre == 'job':
                j_grade_name = j.grade_name
                j_grade_s = j.grade_s
                j_grade_i = j.grade_i


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
        if i.s_State:
          for k in i.s_State:
            col_state.append(f"""
            <tr><th>state_name</th><td>{k.state_name}</td></tr>
            <tr><th>state_state</th><td>{k.state_state}</td></tr>
            """)

        base.append(f"""<table>
        <tr><th>agent_name</th><td>{i.agent_name}</td></tr>
        {", ".join(col_grade)}
        {", ".join(col_effort)}
        {", ".join(col_suffer)}
        {", ".join(col_stereoaction)}
        {", ".join(col_stereoappear)}
        {", ".join(col_press)}
        {", ".join(col_state)}
        </table>
        """)

        '''
        col_yoshimoto=[]
        col_potter=[]
        col_toto=[]

        if j_grade_name and j_grade_s and j_grade_i:
            col_yoshimoto.append(f"<tr><th>YOSHIMOTO</th><td>Ali and Cho want to be a {j_grade_name[0]}. Bob, a connoisseur, observes Cho and says you can be {j_grade_s[0]}. Bob observes Ali and says you can be {j_grade_i[0]}.</td><tr>")
            if i.s_Suffer:
                if i.s_Suffer.suffer:
                    col_toto.append(f"<tr><th>TOTO</th><td>Ali, a {j_grade_name[0]} suffers from {i.s_Suffer.suffer[0]}. Bob, who is burdened by Ali, tells him to quit being a {j_grade_i[0]}.</td><tr>")
            if i.s_Press:
                if i.s_Press.press:
                    col_potter.append(f"<tr><th>POTTER</th><td>{i.s_Press.press[0]} occurred. Ali, a {j_grade_name[0]}, tries to help Bob. But Bob get angry because he found that Ali is a {j_grade_i[0]}</td></tr>")

        progression_table=[f"""<table>
        {col_toto}
        {col_potter}
        {col_yoshimoto}
        </table>"""]

        base.append(progression_table)
        '''





    return coloring('<br>'.join(map(str, base)))




#HTML(''.join(agent_func()))
