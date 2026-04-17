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
    "Study the phenomenon. This kind of cataclysm must have a magical explanation worth understanding.", 
    "Find my family and make sure everyone I love is safe and accounted for.", 
    "Fortify my position and build shelter before anything else.", 
    "Rally my traveling companions. We have adapted to chaos before and we will figure it out.", 
    "This is the gods' doing. Observe, wait, and look for signs of what they intend." 
    ]

options_q2 = [
    "Immediately start comparing notes. A fellow scholar is always welcome.", 
    "Are cautious but grateful. A cat near a bunny is never fully comfortable.", 
    "Judge her by what she can build and prove, not by her words.", 
    "Welcome her to share our campfire. More allies, more strength.", 
    "Refuse her entry. Cat folk from the academies have always overstepped."
    ]

options_q3 = [
    "A glowing academy tower surrounded by bioluminescent ooze and late-night experiments.", 
    "A cozy farmhouse in a sunlit mushroom-forest clearing, surrounded by family plots.",
    "A grand stone structure quarried and built with my own two hands.", 
    "Wherever the weather is best tonight. A campfire and open sky is all I need.", 
    "The high cliffs above the Plasma Plains, unreachable to those who cannot fly."
    ]

options_q4 = [
    "Analyze its weakness, design the right spell combination, then strike with precision.", 
    "Avoid it entirely. I did not come this far to pick a fight with a monster.", 
    "Stand my ground. I have built walls stronger than anything this creature can break.", 
    "I have trained for exactly this. Physical combat is second nature to me.", 
    "Unleash my elemental gift. I was born with this power and it will not fail me."
    ]

options_q5 = [
    "Spend three days cataloguing every possible combination before trying a single one.", 
    "Try the gentlest, most helpful spell first. Something that grows plants, maybe.", 
    "Configure it to reinforce and protect. A defensive tool is always most valuable.", 
    "Experiment freely. If something goes wrong, we will adapt and try the next thing.", 
    "Distrust it. Magic should be a natural gift from the gods, not a crafted contraption."
    ]

options_q6 = [
    "Rigorous study, experimentation, and passing what you learn to the next generation.", 
    "Working the land season after season. Wisdom lives in patience and repetition.", 
    "Building things. A structure teaches you more than any book ever could.", 
    "Living broadly. You can only learn what you have experienced firsthand.", 
    "Tradition passed down from those who came before, honoring the elemental deities."
    ]

options_q7 = [
    "Document the new arrivals. The dark lands just got even more interesting.", 
    "Keep to the sunlit clearings and avoid the shadows where newcomers might lurk.", 
    "Reinforce your borders. A strong wall protects what matters most.", 
    "Make contact and share your fire with them. Displacement is something we all understand.", 
    "Monitor from above. None of them are worthy of our attention yet."
    ]

options_q8 = [
    "Lead a new era of cross-kingdom magical research and collaboration.", 
    "Return to my family's farm and grow enough food to share with everyone.", 
    "Construct something monumental, a landmark that says we were here and we endured.", 
    "Keep traveling and connecting the kingdoms, one shared campfire at a time.", 
    "Restore the sacred traditions and remind the world what the elemental deities intended." 
    ]

if st.session_state.page == 0:
    st.title("Which Animal Folk are you?")

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Start"):
            st.session_state.page = 1

elif st.session_state.page == 1:
    st.progress(st.session_state.page / (total_questions + 1))
    st.write("The chaos has begun. Creatures from all five kingdoms are displaced and frightened.")
    
    q1 = st.radio("The elemental gods' war has shattered the world. Biomes are colliding. What's your first instinct?",
                  options_q1,
                  index=None,
                  key="q1")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if st.session_state.q1 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1

elif st.session_state.page == 2:
    st.progress(st.session_state.page / (total_questions + 1))
    st.write("Junie is a Cat Folk, a bookish wizard with a reshapable wand and good intentions.")
    
    q2 = st.radio("Junie is a Cat Folk, a bookish wizard with a reshapable wand and good intentions.",
                  options_q2,
                  index=None,
                  key="q2")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if st.session_state.q2 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1

elif st.session_state.page == 3:
    st.progress(st.session_state.page / (total_questions + 1))
    q3 = st.radio("Your ideal dwelling in the world of WWW would be...",
                  options_q3,
                  index=None,
                  key="q3")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if st.session_state.q3 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1

elif st.session_state.page == 4:
    st.progress(st.session_state.page / (total_questions + 1))
    st.write("The shattered world has made many creatures enraged and unpredictable.")
    q4 = st.radio("A hostile creature blocks your path. How do you handle it?",
                  options_q4,
                  index=None,
                  key="q4")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if st.session_state.q4 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1

elif st.session_state.page == 5:
    st.progress(st.session_state.page / (total_questions + 1))
    st.write("Junie's wand is legendary. Its reshapable pieces can create spells to fight, build, or heal.")
    
    q5 = st.radio("You come across a powerful magical wand that can be customized into hundreds of spell combinations. You...",
                  options_q5,
                  index=None,
                  key="q5")

    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if st.session_state.q5 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1

elif st.session_state.page == 6:
    st.progress(st.session_state.page / (total_questions + 1))
    q6 = st.radio("What do you believe is the best way to grow knowledge?",
                  options_q6,
                  index=None,
                  key="q6")

    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if st.session_state.q6 is None:
            st.warning("Please select an answer.")
        else:       
            st.session_state.page += 1

elif st.session_state.page == 7:
    st.progress(st.session_state.page / (total_questions + 1))
    st.write("The cataclysm has scrambled the five kingdoms. Nothing is where it used to be.")
    q7 = st.radio("Your homeland's biome has collided with a foreign one. Strange new creatures have moved in. You...",
                  options_q7,
                  index=None,
                  key="q7")
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if st.session_state.q7 is None:
            st.warning("Please select an answer.")
        else:
            st.session_state.page += 1

elif st.session_state.page == 8:
    st.progress(st.session_state.page / (total_questions + 1))
    st.write("The cataclysm has ended. The five kingdoms must decide what comes next.")
    q8 = st.radio("When the world is finally repaired, what role do you want to play in rebuilding it?",
                  options_q8,
                  index=None,
                  key="q8")

    if st.button("Next ➡️", key=f"next_{st.session_state.page}"): 
        if st.session_state.q8 is None:
            st.warning("Please select an answer.")
        else:    
            st.session_state.page += 1

elif st.session_state.page == 9:
    st.title("Your result: ")

    scores = {
        "Cat Folk": 0,
        "Bunny Folk": 0,
        "Goat Folk": 0,
        "Alligator Folk": 0,
        "Thunderbird Folk": 0
    }

    answers = [
        st.session_state.q1,
        st.session_state.q2,
        st.session_state.q3,
        st.session_state.q4,
        st.session_state.q5,
        st.session_state.q6,
        st.session_state.q7,
        st.session_state.q8
    ]

    for a in answers:
        if "Study the phenomenon" in a:
            scores["Cat Folk"] += 1
        elif "Find my family" in a:
            scores["Bunny Folk"] += 1
        elif "Fortify my position" in a:
            scores["Goat Folk"] += 1
        elif "Rally my traveling companions" in a:
            scores["Alligator Folk"] += 1
        elif "Observe, wait" in a:
            scores["Thunderbird Folk"] += 1

    result = max(scores, key=scores.get)
    st.subheader(f"You are: {result}")


    st.progress(1.0)


# if st.button("Reveal my folk type"):
#     scores = {
#         "Cat Folk": cat_folk,
#         "Bunny Folk": bunny_folk,
#         "Goat Folk": goat_folk,
#         "Alligator Folk": alligator_folk,
#         "Thunderbird Folk": thunderbird_folk
#     }

#     result = max(scores, key=scores.get)

#     st.subheader(f"You are: {result}")