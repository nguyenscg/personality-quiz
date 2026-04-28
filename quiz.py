# Personality Quiz
import streamlit as st
import random

if "page" not in st.session_state:
    st.session_state["page"] = 0

st.title("WWW Quiz")

cat_folk = 0
bunny_folk = 0
goat_folk = 0
alligator_folk = 0
thunderbird_folk = 0

total_questions = 8


options_q1 = [
    ("Cat Folk", "Refuse her entry. Those from the academy have always overstepped."), 
    ("Bunny Folk", "Find my family and make sure everyone I love is safe and accounted for."), 
    ("Goat Folk", "Fortify my position and build shelter before anything else."), 
    ("Alligator Folk", "Rally my traveling companions. We have adapted to chaos before and we will figure it out."), 
    ("Thunderbird Folk", "This is the gods' doing. Observe, wait, and look for signs of what they intend.") 
    ]

options_q2 = [
    ("Cat Folk", "Immediately start comparing notes. A fellow scholar is always welcome."), 
    ("Bunny Folk", "Are cautious but grateful. You can never truly lower your guard around someone with claws."), 
    ("Goat Folk", "Judge her by what she can build and prove, not by her words."), 
    ("Alligator Folk", "Welcome her to share our campfire. More allies, more strength."), 
    ("Thunderbird Folk", "Refuse her entry. Those from the academy don't respect tradition.")
    ]

options_q3 = [
    ("Cat Folk", "A glowing academy tower surrounded by bioluminescent ooze and late-night experiments."), 
    ("Bunny Folk", "A cozy farmhouse in a sunlit mushroom-forest clearing, surrounded by family plots."),
    ("Goat Folk", "A grand stone structure quarried and built with my own two hands."), 
    ("Alligator Folk", "Wherever the weather is best tonight. A campfire and open sky is all I need."), 
    ("Thunderbird Folk", "The high cliffs above the Plasma Plains, unreachable to those who cannot fly.")
    ]

options_q4 = [
    ("Cat Folk", "Analyze its weakness, design the right spell combination, then strike with precision."), 
    ("Bunny Folk", "Avoid it entirely. I did not come this far to pick a fight with a monster."), 
    ("Goat Folk", "Stand my ground. I have built walls stronger than anything this creature can break."), 
    ("Alligator Folk", "I have trained for exactly this. Physical combat is second nature to me."), 
    ("Thunderbird Folk", "Unleash my elemental gift. I was born with this power and it will not fail me.")
    ]

options_q5 = [
    ("Cat Folk", "Spend three days cataloguing every possible combination before trying a single one."), 
    ("Bunny Folk", "Try the gentlest, most helpful spell first. Something that grows plants, maybe."), 
    ("Goat Folk", "Configure it to reinforce and protect. A defensive tool is always most valuable."), 
    ("Alligator Folk", "Experiment freely. If something goes wrong, we will adapt and try the next thing."), 
    ("Thunderbird Folk", "Distrust it. Magic should be a natural gift from the gods, not a crafted contraption.")
    ]

options_q6 = [
    ("Cat Folk", "Rigorous study, experimentation, and passing what you learn to the next generation."), 
    ("Bunny Folk", "Working the land season after season. Wisdom lives in patience and repetition."), 
    ("Goat Folk", "Building things. Getting your hands dirty teaches you more than any book ever could."), 
    ("Alligator Folk", "Living broadly. You can only learn what you have experienced firsthand."), 
    ("Thunderbird Folk", "Tradition passed down from those who came before, honoring the elemental deities.")
    ]

options_q7 = [
    ("Cat Folk", "Document the new arrivals. The dark lands just got even more interesting."), 
    ("Bunny Folk","Keep to the sunlit clearings and avoid the shadows where newcomers might lurk."), 
    ("Goat Folk", "Reinforce your borders. A strong wall protects what matters most."), 
    ("Alligator Folk", "Make contact and share your fire with them. Displacement is something we all understand."), 
    ("Thunderbird Folk", "Monitor from above. None of them are worthy of our attention yet.")
    ]

options_q8 = [
    ("Cat Folk", "Lead a new era of cross-kingdom magical research and collaboration."), 
    ("Bunny Folk", "Return to my family's farm and grow enough food to share with everyone."), 
    ("Goat Folk", "Construct something monumental, a landmark that says we were here and we endured."), 
    ("Alligator Folk", "Keep traveling and connecting the kingdoms, one shared campfire at a time."), 
    ("Thunderbird Folk", "Restore the sacred traditions and remind the world what the elemental deities intended.")
    ]

if "shuffled" not in st.session_state:
    st.session_state.shuffled = {
        "q1": random.sample(options_q1, len(options_q1)),
        "q2": random.sample(options_q2, len(options_q2)),
        "q3": random.sample(options_q3, len(options_q3)),
        "q4": random.sample(options_q4, len(options_q4)),
        "q5": random.sample(options_q5, len(options_q5)),
        "q6": random.sample(options_q6, len(options_q6)),
        "q7": random.sample(options_q7, len(options_q7)),
        "q8": random.sample(options_q8, len(options_q8)),
    }

if st.session_state.page == 0:
    st.title("Which Animal Folk are you?")

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Start"):
            st.session_state.page = 1
            st.rerun()

elif st.session_state.page == 1:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 1
    st.write("The elemental gods' war has shattered the world. Biomes are colliding. What's your first instinct?")

    q1 = st.radio("The chaos has begun. Creatures from all five kingdoms are displaced and frightened.",
                  [opt[1] for opt in st.session_state.shuffled["q1"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q1")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q1:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q1"] if opt[1] == q1)
            st.session_state["a1"] = selected_type
        if q1 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 2:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 2
    st.write("Junie arrives in your territory, wand in hand, claiming she can help repair the world. You...")
    
    q2 = st.radio("Junie is a Cat Folk, a bookish wizard with a reshapable wand and good intentions.",
                  [opt[1] for opt in st.session_state.shuffled["q2"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q2")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q2:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q2"] if opt[1] == q2)
            st.session_state["a2"] = selected_type      
        if q2 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 3:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 3
    st.write("Your ideal dwelling in the world of WWW would be...")
    q3 = st.radio("",
                  [opt[1] for opt in st.session_state.shuffled["q3"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q3")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q3:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q3"] if opt[1] == q3)
            st.session_state["a3"] = selected_type    
        if q3 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 4:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 4
    st.write("A hostile creature blocks your path. How do you handle it?")

    q4 = st.radio("The shattered world has made many creatures enraged and unpredictable.",
                  [opt[1] for opt in st.session_state.shuffled["q4"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q4")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if q4:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q4"] if opt[1] == q4)
            st.session_state["a4"] = selected_type    
        if q4 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 5:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 5
    st.write("You come across a powerful magical wand that can be customized into hundreds of spell combinations. You...")

    q5 = st.radio("Junie's wand is legendary. Its reshapable pieces can create spells to fight, build, or heal.",
                  [opt[1] for opt in st.session_state.shuffled["q5"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q5")
    

    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if q5:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q5"] if opt[1] == q5)
            st.session_state["a5"] = selected_type    
        if q5 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 6:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 6
    st.write("What do you believe is the best way to grow knowledge?")

    q6 = st.radio("",
                  [opt[1] for opt in st.session_state.shuffled["q6"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q6")

    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if q6:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q6"] if opt[1] == q6)
            st.session_state["a6"] = selected_type    
        if q6 is None:
            st.warning("Please select an answer.")
        else:       
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 7:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 7
    st.write("Your homeland's biome has collided with a foreign one. Strange new creatures have moved in. You...")

    q7 = st.radio("The cataclysm has scrambled the five kingdoms. Nothing is where it used to be.",
                  [opt[1] for opt in st.session_state.shuffled["q7"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q7")

    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if q7:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q7"] if opt[1] == q7)
            st.session_state["a7"] = selected_type    
        if q7 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 8:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 8
    st.write("When the world is finally repaired, what role do you want to play in rebuilding it?")

    q8 = st.radio("The cataclysm has ended. The five kingdoms must decide what comes next.",
                  [opt[1] for opt in st.session_state.shuffled["q8"]],
                  index=None,
                  format_func=lambda x: f"• {x}",
                  key="q8")

    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if q8:
            selected_type = next(opt[0] for opt in st.session_state.shuffled["q8"] if opt[1] == q8)
            st.session_state["a8"] = selected_type    
        if q8 is None:
            st.warning("Please select an answer.")
        else:    
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 9:
    st.title("Your result: ")

    scores = {
        "Cat Folk": 0,
        "Bunny Folk": 0,
        "Goat Folk": 0,
        "Alligator Folk": 0,
        "Thunderbird Folk": 0
    }

    answers = [st.session_state.get(f"a{i}") for i in range(1,9)]

    for a in answers:
        if a:
            scores[a] += 1
    result = max(scores, key=scores.get)

    image_map ={
        "Cat Folk": "personalities/catfolk.png",
        "Bunny Folk": "personalities/bunnyfolk.png",
        "Goat Folk": "personalities/goatfolk.png",
        "Alligator Folk": "personalities/alligatorfolk.png",
        "Thunderbird Folk": "personalities/thunderbird.png"
    }

    st.subheader(f"You are:")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(image_map[result], width=600)


    st.progress(1.0)
