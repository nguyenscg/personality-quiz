# Personality Quiz Binary version
import streamlit as st

if "page" not in st.session_state:
    st.session_state["page"] = 0

st.title("WWW Quiz")

cat_folk = 0
bunny_folk = 0
goat_folk = 0
alligator_folk = 0
thunderbird_folk = 0

total_questions = 8

options_q1 = ["Lean in. The unknown is the whole point.", "Proceed carefully. The unknown is a risk to manage."] # cat folk - bunny folk

options_q2 = ["Building something that will outlast you.", "Experiencing everything the world has to offer."] # goat folk - aligator folk

options_q3 = ["They prove themselves over a long time.", "They show up and share what they have."] #thunderbird - aligator

options_q4 = ["What you discovered or created.", "The people you protected and provided for."] # cat - bunny

options_q5 = ["Adapt and keep moving.", "Reinforce and rebuild from a solid foundation."] # - aligator - goat

options_q6 = ["It exists to be questioned and improved upon.", "It exists to be honored and preserved."] # cat - thunderbird

options_q7 = ["A place you return to, tended and familiar.", "Wherever the people you love happen to be."] # bunny - aligator 

options_q8 =["What you have built or accomplished.", "The depth of your knowledge and understanding."] # goat - cat

options_q9 = ["So devoted to your principles that you struggle to bend.", "So focused on what is next that you never truly rest."] # thunderbird - goat

options_q10 = ["Withdraw to somewhere safe and quiet until you recover.", "Push through. Responsibility does not pause for exhaustion."] # bunny - thunderbird

if st.session_state.page == 0:
    st.markdown("<h1>Which Animal Folk are you?</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("Start"):
            st.session_state.page = 1
            st.rerun()

elif st.session_state.page == 1:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 1
    st.write("When faced with the unknown, you...")

    q1 = st.radio("",
                  ["Lean in. The unknown is the whole point.", "Proceed carefully. The unknown is a risk to manage."],
                  index=None,
                  key="q1")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q1 is None:
            st.warning("Please select an answer.")
        else:
            if q1 == "Lean in. The unknown is the whole point.":
                st.session_state["a1"] = "Cat Folk"
            elif q1 == "Proceed carefully. The unknown is a risk to manage.":
                st.session_state["a1"] = "Bunny Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 2:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 2
    st.write("Your ideal life looks more like...")

    q2 = st.radio("",
                  ["Building something that will outlast you.", "Experiencing everything the world has to offer."],
                  index=None,
                  key="q2")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q2 is None:
            st.warning("Please select an answer.")
        else:
            if q2 == "Building something that will outlast you.":
                st.session_state["a2"] = "Goat Folk"
            elif q2 == "Experiencing everything the world has to offer.":
                st.session_state["a2"] = "Alligator Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 3:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 3
    st.write("You trust someone new when...")

    q3 = st.radio("",
                  ["They prove themselves over a long time.", "They show up and share what they have."],
                  index=None,
                  key="q3")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q3 is None:
            st.warning("Please select an answer.")
        else:
            if q3 == "Building something that will outlast you.":
                st.session_state["a3"] = "Thunderbird Folk"
            elif q3 == "They show up and share what they have.":
                st.session_state["a3"] = "Alligator Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 4:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 4
    st.write("You would rather be known for...")

    q4 = st.radio("",
                  ["What you discovered or created.", "The people you protected and provided for."],
                  index=None,
                  key="q4")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q4 is None:
            st.warning("Please select an answer.")
        else:
            if q4 == "What you discovered or created.":
                st.session_state["a4"] = "Cat Folk"
            elif q4 == "The people you protected and provided for.":
                st.session_state["a4"] = "Bunny Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 5:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 5
    st.write("When things go wrong, you...")

    q5 = st.radio("",
                  ["Adapt and keep moving.", "Reinforce and rebuild from a solid foundation."],
                  index=None,
                  key="q5")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q5 is None:
            st.warning("Please select an answer.")
        else:
            if q5 == "Adapt and keep moving.":
                st.session_state["a5"] = "Alligator Folk"
            elif q5 == "Reinforce and rebuild from a solid foundation.":
                st.session_state["a5"] = "Goat Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 6:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 6
    st.write("Your relationship with tradition is...")

    q6 = st.radio("",
                  ["It exists to be questioned and improved upon.", "It exists to be honored and preserved."],
                  index=None,
                  key="q6")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q6 is None:
            st.warning("Please select an answer.")
        else:
            if q6 == "It exists to be questioned and improved upon.":
                st.session_state["a6"] = "Cat Folk"
            elif q6 == "It exists to be honored and preserved.":
                st.session_state["a6"] = "Thunderbird Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 7:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 7
    st.write("Home is...")

    q7 = st.radio("",
                  ["A place you return to, tended and familiar.", "Wherever the people you love happen to be."],
                  index=None,
                  key="q7")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q7 is None:
            st.warning("Please select an answer.")
        else:
            if q7 == "A place you return to, tended and familiar.":
                st.session_state["a7"] = "Bunny Folk"
            elif q7 == "Wherever the people you love happen to be.":
                st.session_state["a7"] = "Alligator Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 8:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 8
    st.write("You prove your worth through...")

    q8 = st.radio("",
                  ["What you have built or accomplished.", "The depth of your knowledge and understanding."],
                  index=None,
                  key="q8")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q8 is None:
            st.warning("Please select an answer.")
        else:
            if q8 == "What you have built or accomplished.":
                st.session_state["a8"] = "Goat Folk"
                goat_folk += 1
            elif q8 == "The depth of your knowledge and understanding.":
                st.session_state["a8"] = "Cat Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 9:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 9
    st.write("Your greatest flaw is...")

    q9 = st.radio("",
                  ["So devoted to your principles that you struggle to bend.", "So focused on what is next that you never truly rest."],
                  index=None,
                  key="q9")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q9 is None:
            st.warning("Please select an answer.")
        else:
            if q9 == "So devoted to your principles that you struggle to bend.":
                st.session_state["a9"] = "Thunderbird Folk"
            elif q9 == "So focused on what is next that you never truly rest.":
                st.session_state["a9"] = "Goat Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 10:
    st.progress(st.session_state.page / (total_questions + 1))
    # question 10
    st.write("When the world asks too much of you, you...")

    q10 = st.radio("",
                  ["Withdraw to somewhere safe and quiet until you recover.", "Push through. Responsibility does not pause for exhaustion."],
                  index=None,
                  key="q10")
    
    if st.button("Next ➡️", key=f"next_{st.session_state.page}"):
        if q10 is None:
            st.warning("Please select an answer.")
        else:
            if q10 == "Withdraw to somewhere safe and quiet until you recover.":
                st.session_state["a10"] = "Bunny Folk"
            elif q10 == "Push through. Responsibility does not pause for exhaustion.":
                st.session_state["a10"] = "Thunderbird Folk"
            st.session_state.page += 1
            st.rerun()

elif st.session_state.page == 11:
    st.title("Your result: ")

    scores = {
        "Cat Folk": 0,
        "Bunny Folk": 0,
        "Goat Folk": 0,
        "Alligator Folk": 0,
        "Thunderbird Folk": 0
    }

    answers = [st.session_state.get(f"a{i}") for i in range(1,11)]

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

