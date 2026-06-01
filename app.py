from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "super-secret-key"

questions = [
    {
        "text": "When faced with the unknown, you...",
        "options": [
            {
                "text": "Lean in. The unknown is the whole point.",
                "animal": "Cat Folk"
            },
            {
                "text": "Proceed carefully. The unknown is a risk to manage.",
                "animal": "Bunny Folk"
            },
        ]
    },
    {
        "text": "Your ideal life looks more like...",
        "options": [
            {
                "text": "Building something that will outlast you.",
                "animal": "Goat Folk"
            },
            {
                "text": "Experiencing everything the world has to offer.",
                "animal": "Alligator Folk"
            }
        ]
    },
    {
        "text": "You trust someone new when...",
        "options": [
            {
                "text": "They prove themselves over a long time.",
                "animal": "Thunderbird Folk"
            },
            {
                "text": "They show up and share what they have.",
                "animal": "Alligator Folk"
            }
        ]
    },
    {
        "text": "You would rather be known for...",
        "options": [
            {
                "text": "What you discovered or created.",
                "animal": "Cat Folk"
            },
            {
                "text": "The people you protected and provided for.",
                "animal": "Bunny Folk"
            }
        ]
    },
    {
        "text": "When things go wrong, you...",
        "options": [
            {
                "text": "Adapt and keep moving.",
                "animal": "Alligator Folk"
            },
            {
                "text": "Reinforce and rebuild from a solid foundation.",
                "animal": "Goat Folk"
            }
        ]
    },
    {
        "text": "Your relationship with tradition is...",
        "options": [
            {
                "text": "It exists to be questioned and improved upon.",
                "animal": "Cat Folk"
            },
            {
                "text": "It exists to be honored and preserved.",
                "animal": "Thunderbird Folk"
            }
        ]
    },
    {
        "text": "Your ideal life looks more like...",
        "options": [
            {
                "text": "Building something that will outlast you.",
                "animal": "Goat Folk"
            },
            {
                "text": "Experiencing everything the world has to offer.",
                "animal": "Alligator Folk"
            }
        ]
    },
    {
        "text": "Home is...",
        "options": [
            {
                "text": "A place you return to, tended and familiar.",
                "animal": "Bunny Folk"
            },
            {
                "text": "Wherever the people you love happen to be.",
                "animal": "Alligator Folk"
            }
        ]
    },
    {
        "text": "You prove your worth through...",
        "options": [
            {
                "text": "What you have built or accomplished.",
                "animal": "Goat Folk"
            },
            {
                "text": "The depth of your knowledge and understanding.",
                "animal": "Cat Folk"
            }
        ]
    },
    {
        "text": "Your greatest flaw is...",
        "options": [
            {
                "text": "So devoted to your principles that you struggle to bend.",
                "animal": "Thunderbird Folk"
            },
            {
                "text": "So focused on what is next that you never truly rest.",
                "animal": "Goat Folk"
            }
        ]
    },
    {
        "text": "When the world asks too much of you, you...",
        "options": [
            {
                "text": "Withdraw to somewhere safe and quiet until you recover.",
                "animal": "Bunny Folk"
            },
            {
                "text": "Push through. Responsibility does not pause for exhaustion.",
                "animal": "Thunderbird Folk"
            }
        ]
    }
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/start")
def start():

    session["question_index"] = 0
    
    session["scores"] = {
            "Cat Folk": 0,
            "Bunny Folk": 0,
            "Goat Folk": 0,
            "Alligator Folk": 0,
            "Thunderbird Folk": 0
        }
    
    return redirect(url_for("quiz"))

@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if "question_index" not in session:
        session["question_index"] = 0

        session["scores"] = {
            "Cat Folk": 0,
            "Bunny Folk": 0,
            "Goat Folk": 0,
            "Alligator Folk": 0,
            "Thunderbird Folk": 0
        }
    
    if request.method == "POST":
        chosen_animal = request.form.get("answer")

        scores = session["scores"]
        scores[chosen_animal] += 1

        session["scores"] = scores

        session["question_index"] += 1

        return redirect(url_for("quiz"))
    
    if session["question_index"] >= len(questions):
        return redirect(url_for("results"))
    
    current_question = questions[session["question_index"]]

    return render_template("quiz.html", question=current_question)

@app.route("/results")
def results():

    scores = session["scores"]

    winner = max(scores, key=scores.get)

    return render_template("results.html", winner=winner)



if __name__ == "__main__":
    app.run(debug=True)