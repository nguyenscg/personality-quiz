# Personality Quiz
import streamlit as st

st.title("WWW Quiz")

cat_folk = 0
bunny_folk = 0
goat_folk = 0
alligator_folk = 0
thunderbird_folk = 0

q1 = st.radio("The elemental gods' war has shattered the world. Biomes are colliding. What's your first instinct?",
              ["Study the phenomenon. This kind of cataclysm must have a magical explanation worth understanding.", "Find my family and make sure everyone I love is safe and accounted for.", "Fortify my position and build shelter before anything else.", "Rally my traveling companions. We have adapted to chaos before and we will figure it out.", "This is the gods' doing. Observe, wait, and look for signs of what they intend." ])

q2 = st.radio("Junie is a Cat Folk, a bookish wizard with a reshapable wand and good intentions.",
              ["Immediately start comparing notes. A fellow scholar is always welcome.", "Are cautious but grateful. A cat near a bunny is never fully comfortable.", "Judge her by what she can build and prove, not by her words.", "Welcome her to share our campfire. More allies, more strength.", "Refuse her entry. Cat folk from the academies have always overstepped."])

q3 = st.radio("Your ideal dwelling in the world of WWW would be...",
              ["A glowing academy tower surrounded by bioluminescent ooze and late-night experiments.", "A cozy farmhouse in a sunlit mushroom-forest clearing, surrounded by family plots.", "A grand stone structure quarried and built with my own two hands.", "Wherever the weather is best tonight. A campfire and open sky is all I need.", "The high cliffs above the Plasma Plains, unreachable to those who cannot fly."])

q4 = st.radio("A hostile creature blocks your path. How do you handle it?",
              ["Analyze its weakness, design the right spell combination, then strike with precision.", "Avoid it entirely. I did not come this far to pick a fight with a monster.", "Stand my ground. I have built walls stronger than anything this creature can break.", "I have trained for exactly this. Physical combat is second nature to me.", "Unleash my elemental gift. I was born with this power and it will not fail me."])

q5 = st.radio("You come across a powerful magical wand that can be customized into hundreds of spell combinations. You...",
              ["Spend three days cataloguing every possible combination before trying a single one.", "Try the gentlest, most helpful spell first. Something that grows plants, maybe.", "Configure it to reinforce and protect. A defensive tool is always most valuable.", "Experiment freely. If something goes wrong, we will adapt and try the next thing.", "Distrust it. Magic should be a natural gift from the gods, not a crafted contraption."])

q6 = st.radio("What do you believe is the best way to grow knowledge?",
              ["Rigorous study, experimentation, and passing what you learn to the next generation.", "Working the land season after season. Wisdom lives in patience and repetition.", "Building things. A structure teaches you more than any book ever could.", "Living broadly. You can only learn what you have experienced firsthand.", "Tradition passed down from those who came before, honoring the elemental deities."])

q7 = st.radio("Your homeland's biome has collided with a foreign one. Strange new creatures have moved in. You...",
              "Document the new arrivals. The dark lands just got even more interesting.", "Keep to the sunlit clearings and avoid the shadows where newcomers might lurk.", "Reinforce your borders. A strong wall protects what matters most.", "Make contact and share your fire with them. Displacement is something we all understand.", "Monitor from above. None of them are worthy of our attention yet." )

q8 = st.radio("When the world is finally repaired, what role do you want to play in rebuilding it?", 
              ["Lead a new era of cross-kingdom magical research and collaboration.", "Return to my family's farm and grow enough food to share with everyone.", "Construct something monumental, a landmark that says we were here and we endured.", "Keep traveling and connecting the kingdoms, one shared campfire at a time.", "Restore the sacred traditions and remind the world what the elemental deities intended." ])