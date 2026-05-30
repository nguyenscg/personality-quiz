from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    if request.method == "POST":
        answer = request.form.get("answer")
        print(answer)  # test for now
        return redirect(url_for("quiz"))

    return render_template("quiz.html")



if __name__ == "__main__":
    app.run(debug=True)