# Personality Quiz
import streamlit as st

if "page" not in st.session_state:
    st.session_state["page"] = 0

st.title("WWW Quiz")

cat_folk = 0
bunny_folk = 0
goat_folk = 0
alligator_folk = 0
thunderbird_folk = 0

if st.session_state.page == 0:
    st.write("The chaos has begun. Creatures from all five kingdoms are displaced and frightened.")
    
    q1 = st.radio("The elemental gods' war has shattered the world. Biomes are colliding. What's your first instinct?",
              ["Study the phenomenon. This kind of cataclysm must have a magical explanation worth understanding.", "Find my family and make sure everyone I love is safe and accounted for.", "Fortify my position and build shelter before anything else.", "Rally my traveling companions. We have adapted to chaos before and we will figure it out.", "This is the gods' doing. Observe, wait, and look for signs of what they intend." ])
    
    if st.button("Next ➡️"):
        st.session_state.q1 = q1
        st.session_state.page += 1

elif st.session_state.page == 1:
    st.write("Junie is a Cat Folk, a bookish wizard with a reshapable wand and good intentions.")
    
    q2 = st.radio("Junie is a Cat Folk, a bookish wizard with a reshapable wand and good intentions.",
              ["Immediately start comparing notes. A fellow scholar is always welcome.", "Are cautious but grateful. A cat near a bunny is never fully comfortable.", "Judge her by what she can build and prove, not by her words.", "Welcome her to share our campfire. More allies, more strength.", "Refuse her entry. Cat folk from the academies have always overstepped."])
    if st.button("Next ➡️"): 
        st.session_state.q2 = q2
        st.session_state.page += 1

elif st.session_state.page == 2:
    
    q3 = st.radio("Your ideal dwelling in the world of WWW would be...",
              ["A glowing academy tower surrounded by bioluminescent ooze and late-night experiments.", "A cozy farmhouse in a sunlit mushroom-forest clearing, surrounded by family plots.", "A grand stone structure quarried and built with my own two hands.", "Wherever the weather is best tonight. A campfire and open sky is all I need.", "The high cliffs above the Plasma Plains, unreachable to those who cannot fly."])
    if st.button("Next ➡️"): 
        st.session_state.q3 = q3
        st.session_state.page += 1

elif st.session_state.page == 3:
    st.write("The shattered world has made many creatures enraged and unpredictable.")
    q4 = st.radio("A hostile creature blocks your path. How do you handle it?",
              ["Analyze its weakness, design the right spell combination, then strike with precision.", "Avoid it entirely. I did not come this far to pick a fight with a monster.", "Stand my ground. I have built walls stronger than anything this creature can break.", "I have trained for exactly this. Physical combat is second nature to me.", "Unleash my elemental gift. I was born with this power and it will not fail me."])
    if st.button("Next ➡️"): 
        st.session_state.q4 = q4
        st.session_state.page += 1

elif st.session_state.page == 4:
    st.write("Junie's wand is legendary. Its reshapable pieces can create spells to fight, build, or heal.")
    
    q5 = st.radio("You come across a powerful magical wand that can be customized into hundreds of spell combinations. You...",
              ["Spend three days cataloguing every possible combination before trying a single one.", "Try the gentlest, most helpful spell first. Something that grows plants, maybe.", "Configure it to reinforce and protect. A defensive tool is always most valuable.", "Experiment freely. If something goes wrong, we will adapt and try the next thing.", "Distrust it. Magic should be a natural gift from the gods, not a crafted contraption."])

    if st.button("Next ➡️"): 
        st.session_state.q5 = q5
        st.session_state.page += 1

elif st.session_state.page == 5:
    q6 = st.radio("What do you believe is the best way to grow knowledge?",
              ["Rigorous study, experimentation, and passing what you learn to the next generation.", "Working the land season after season. Wisdom lives in patience and repetition.", "Building things. A structure teaches you more than any book ever could.", "Living broadly. You can only learn what you have experienced firsthand.", "Tradition passed down from those who came before, honoring the elemental deities."])

    if st.button("Next ➡️"): 
        st.session_state.q6 = q6
        st.session_state.page += 1

elif st.session_state.page == 6:
    st.write("The cataclysm has scrambled the five kingdoms. Nothing is where it used to be.")
    q7 = st.radio("Your homeland's biome has collided with a foreign one. Strange new creatures have moved in. You...",
              ["Document the new arrivals. The dark lands just got even more interesting.", "Keep to the sunlit clearings and avoid the shadows where newcomers might lurk.", "Reinforce your borders. A strong wall protects what matters most.", "Make contact and share your fire with them. Displacement is something we all understand.", "Monitor from above. None of them are worthy of our attention yet."])
    if st.button("Next ➡️"): 
        st.session_stage.q7 = q7
        st.session_state.page += 1

elif st.session_state.page == 7:
    st.write("The cataclysm has ended. The five kingdoms must decide what comes next.")
    q8 = st.radio("When the world is finally repaired, what role do you want to play in rebuilding it?", 
              ["Lead a new era of cross-kingdom magical research and collaboration.", "Return to my family's farm and grow enough food to share with everyone.", "Construct something monumental, a landmark that says we were here and we endured.", "Keep traveling and connecting the kingdoms, one shared campfire at a time.", "Restore the sacred traditions and remind the world what the elemental deities intended." ])

    if st.button("Next ➡️"): 
        st.session_stage.q8 = q8
        st.session_state.page += 1

elif st.session_state.page == 8:
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

    result = max(scores, key=scores.get)
    st.subheader(f"You are: {result}")

    st.progress((st.session_state.page + 1) / 9)


# if q1 == "Study the phenomenon. This kind of cataclysm must have a magical explanation worth understanding.":
#     cat_folk += 1
# elif q1 == "Find my family and make sure everyone I love is safe and accounted for.":
#     bunny_folk += 1
# elif q1 == "Fortify my position and build shelter before anything else.":
#     goat_folk += 1
# elif q1 == "Rally my traveling companions. We have adapted to chaos before and we will figure it out.":
#     alligator_folk += 1
# elif q1 == "This is the gods' doing. Observe, wait, and look for signs of what they intend.":
#     thunderbird_folk += 1

# if q2 == "Immediately start comparing notes. A fellow scholar is always welcome.":
#     cat_folk += 1
# elif q2 == "Are cautious but grateful. A cat near a bunny is never fully comfortable.ok":
#     bunny_folk += 1
# elif q2 == "Judge her by what she can build and prove, not by her words.":
#     goat_folk += 1
# elif q2 == "Welcome her to share our campfire. More allies, more strength.":
#     alligator_folk += 1
# elif q2 == "Refuse her entry. Cat folk from the academies have always overstepped.":
#     thunderbird_folk += 1    

# if q3 == "A glowing academy tower surrounded by bioluminescent ooze and late-night experiments.":
#     cat_folk += 1
# elif q3 == "A cozy farmhouse in a sunlit mushroom-forest clearing, surrounded by family plots.":
#     bunny_folk += 1
# elif q3 == "A grand stone structure quarried and built with my own two hands.":
#     goat_folk += 1
# elif q3 == "Wherever the weather is best tonight. A campfire and open sky is all I need.":
#     alligator_folk += 1
# elif q3 == "The high cliffs above the Plasma Plains, unreachable to those who cannot fly.":
#     thunderbird_folk += 1    

# if q4 == "Analyze its weakness, design the right spell combination, then strike with precision.":
#     cat_folk += 1
# elif q4 == "Avoid it entirely. I did not come this far to pick a fight with a monster.":
#     bunny_folk += 1
# elif q4 == "Stand my ground. I have built walls stronger than anything this creature can break.":
#     goat_folk += 1
# elif q4 == "I have trained for exactly this. Physical combat is second nature to me.":
#     alligator_folk += 1
# elif q4 == "Unleash my elemental gift. I was born with this power and it will not fail me.":
#     thunderbird_folk += 1    

# if q5 == "Spend three days cataloguing every possible combination before trying a single one.":
#     cat_folk += 1
# elif q5 == "Try the gentlest, most helpful spell first. Something that grows plants, maybe.":
#     bunny_folk += 1
# elif q5 == "Configure it to reinforce and protect. A defensive tool is always most valuable.":
#     goat_folk += 1
# elif q5 == "Experiment freely. If something goes wrong, we will adapt and try the next thing.":
#     alligator_folk += 1
# elif q5 == "Distrust it. Magic should be a natural gift from the gods, not a crafted contraption.":
#     thunderbird_folk += 1    

# if q6 == "Rigorous study, experimentation, and passing what you learn to the next generation.":
#     cat_folk += 1
# elif q6 == "Working the land season after season. Wisdom lives in patience and repetition.":
#     bunny_folk += 1
# elif q6 == "Building things. A structure teaches you more than any book ever could.":
#     goat_folk += 1
# elif q6 == "Living broadly. You can only learn what you have experienced firsthand.":
#     alligator_folk += 1
# elif q6 == "Tradition passed down from those who came before, honoring the elemental deities.":
#     thunderbird_folk += 1    

# if q7 == "Document the new arrivals. The dark lands just got even more interesting.":
#     cat_folk += 1
# elif q7 == "Keep to the sunlit clearings and avoid the shadows where newcomers might lurk.":
#     bunny_folk += 1
# elif q7 == "Reinforce your borders. A strong wall protects what matters most.":
#     goat_folk += 1
# elif q7 == "Make contact and share your fire with them. Displacement is something we all understand.":
#     alligator_folk += 1
# elif q7 == "Monitor from above. None of them are worthy of our attention yet.":
#     thunderbird_folk += 1    

# if q8 == "Lead a new era of cross-kingdom magical research and collaboration.":
#     cat_folk += 1
# elif q8 == "Return to my family's farm and grow enough food to share with everyone.":
#     bunny_folk += 1
# elif q8 == "Construct something monumental, a landmark that says we were here and we endured.":
#     goat_folk += 1
# elif q8 == "Keep traveling and connecting the kingdoms, one shared campfire at a time.":
#     alligator_folk += 1
# elif q8 == "Restore the sacred traditions and remind the world what the elemental deities intended.":
#     thunderbird_folk += 1    

if st.button("Reveal my folk type"):
    scores = {
        "Cat Folk": cat_folk,
        "Bunny Folk": bunny_folk,
        "Goat Folk": goat_folk,
        "Alligator Folk": alligator_folk,
        "Thunderbird Folk": thunderbird_folk
    }

    result = max(scores, key=scores.get)

    st.subheader(f"You are: {result}")