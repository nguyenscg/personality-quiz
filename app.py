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
                    }
        ]
    }
]

@app.route("/")
def home():
    return render_template("home.html")

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