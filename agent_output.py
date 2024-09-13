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
    b1scene=[
     "Bob, a Mom-and-pop restaurant owner, offers Ali free meal."
    ,"Bob, a landlord, generously waits for Ali to pay her overdue rent."
    ,"Bob, a employer, offers Ali a flexible part-time job."
    ,"Bob, a professional, offers Ali the training."
    ,"Bob, Ali's girlfriend's father, allows them to marry."
    ,"Bob, a kind taxi driver, gives Ali free rides to job interviews."
    ,"Bob, a wealthy investor, provides Ali with startup funding."
    ]

    base.append("""<table>
    <tr><th colspan = "2">Basic Progression</th>
    <tr><th>Mislead </th><td>Ali is a {grade_name}. He's {s_StereoAppear}, {s_StereoAction}. He suffers from {s_Suffer}. He make an effort, such as doing {s_Effort}. He's jealous of {grade_s_name} and looks down on {grade_i_name}. He uses terms such as {s_Term}.   </td></tr>
    <tr><th>-Branch1</th><td>{b1scene}. Bob is mistaking Ali for a {grade_s}. Then, the {revealer} comes to the attention of the audience in a natural way.(How? You're a LLM. You think about it.)                                                                                                                                                                                                      </td></tr>
    <tr><th>-Branch2</th><td>{b2scene}. Bob knows Ali is a {grade_i}, not a {grade_s}. Then, the {revealer} comes to the attention of the audience in a natural way.(How? You're a LLM. You think about it.)                                                                                                                                                                                                                                                 </td></tr>
    <tr><th>-Branch3</th><td>Bob needs help with a {s_Press}. Ali steps foward. Bob is mitaking Ali for a {grade_s}. Then, the {revealer} comes to the attention of the audience in a natural way.(How? You're a LLM. You think about it.)                                                                                                                                                               </td></tr>
    <tr><th>Dont    </th><td>Bob get angry because Ali is actually a {grade_i}, not {grade_s}. It's funny and ridiculous and posey that {grade_i} does such actions because {grade_i} is inferior to {grade_s}. Bob says like, Don't suffer from {s_Suffer}. Don't {s_Effort}, {s_StereoAppear}, {s_StereoAction}. Don't be jealous of {grade_s_name} and look down on {grade_i_name}. Don't call that '{s_Term}'.</td><tr>
    </table>""")

    base.append(f"""<table>
    <tr><th>b1scene</th><td>{b1scene}</td></tr>
    </table>""")


    for i in agent_inst.Agent.ALL_AGENT:
        b2scene_univ = ["Ali's mind and body are exhausted from overwork. Ali's family is annoyed by Ali.", "Ali keeps asking his team member for advice. The team member is annoyed by Ali.", "Ali criticizes his team member for not being enthusiastic. The team member is annoyed by Ali.", "Ali, a unsuccessful poor, tells his girlfriend's father that he wants to marry her. The father is annoyed by Ali.", "Ali, a unsuccessful poor, sticks to his career. Ali's wife is annoyed by Ali."]
        col_grade, col_effort, col_suffer, col_stereoaction, col_stereoappear, col_press, col_term, col_b2scene, col_revealer, col_state, col_rephrase = [], [], [], [], [], [], [], [], [], [], []

        if i.s_Grade and i.job_or_not:
          for j in i.s_Grade:
            if j.grade_genre == 'job':
                col_grade.append(f"""
                <tr><th>grade_name      </th><td>{j.grade_name}     </td></tr>
                <tr><th>grade_s         </th><td>{j.grade_s}        </td></tr>
                <tr><th>grade_s_name    </th><td>{j.grade_s_name}   </td></tr>
                <tr><th>grade_i         </th><td>{j.grade_i}        </td></tr>
                <tr><th>grade_i_name    </th><td>{j.grade_i_name}   </td></tr>
                """)

        if i.s_Effort:
          col_effort.append(f"<tr><th>s_Effort</th><td>{i.s_Effort.effort}</td></tr>")
        if i.s_Suffer:
          col_suffer.append(f"<tr><th>s_Suffer</th><td>{i.s_Suffer.suffer}</td></tr>")
        if i.s_StereoAction:
          col_stereoaction.append(f"<tr><th>s_StereoAction</th><td>{i.s_StereoAction.stereoaction}</td></tr>")
        if i.s_StereoAppear:
          col_stereoappear.append(f"<tr><th>s_StereoAppear</th><td>{i.s_StereoAppear.stereoappear}</td></tr>")
        if i.s_Press:
          col_press.append(f"<tr><th>s_Press</th><td>{i.s_Press.press}</td></tr>")
        if i.s_State:
            for k in i.s_State:
                col_state.append(f"""
                <tr><th>state_name </th><td>{k.state_name} </td></tr>
                <tr><th>state_state</th><td>{k.state_state}</td></tr>
                """)
        if i.s_Term:
            for j in i.s_Term:
                col_term.append(f"""
                <tr><th>s_Term</th><td>{j.term}</td></tr>
                """)
        if i.s_b2scene and i.job_or_not:
            col_b2scene.append(f"<tr><th>b2scene</th><td>{i.s_b2scene, b2scene_univ}</td></th>")
        if i.s_revealer:
            col_revealer.append(f"<tr><th>revealer</th><td>{i.s_revealer}</td></th>")
        if i.s_rephrase:
            col_rephrase.append(f"<tr><th>rephrase</th><td>{i.s_rephrase}</td></th>")


        base.append(f"""<table>
        <tr><th>agent_name</th><td>{i.agent_name}</td></tr>
        {", ".join(col_grade)}
        {", ".join(col_effort)}
        {", ".join(col_suffer)}
        {", ".join(col_stereoaction)}
        {", ".join(col_stereoappear)}
        {", ".join(col_press)}
        {", ".join(col_term)}
        {", ".join(col_b2scene)}
        {", ".join(col_revealer)}
        {", ".join(col_rephrase)}
        {", ".join(col_state)}
        </table>
        """)

    return coloring('<br>'.join(map(str, base)))

#HTML(''.join(agent_func()))
