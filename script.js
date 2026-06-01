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
];

let currentQuestion = 0;

let scores = {
    "Cat Folk": 0,
    "Bunny Folk": 0,
    "Goat Folk": 0,
    "Alligator Folk": 0,
    "Thunderbird Folk": 0 
};

document.getElementById('start-btn').addEventListener("click", showQuestion);

function showQuestion() {
    const quiz = document.getElementById("quiz-container");
    
    const question = questions[currentQuestion];

    quiz.innerHTML = `
    <h2 class="question">${question.text}</h2>

    <button class="answer-btn"
        onclick="chooseAnswer('${question.options[0].animal}')">
        ${question.options[0].text}
    </button>

    <button class="answer-btn"
        onclick="chooseAnswer('${question.options[1].animal}')">
        ${question.options[1].text}
    </button>
    `;
}

function chooseAnswer(animal) {
    scores[animal]++;

    currentQuestion++;

    if (currentQuestion >= questions.length) {
        showResult();
    }
    else {
        showQuestion();
    }
}

function showResult() {
    let winner =
        Object.keys(scores).reduce((a, b) =>
            scores[a] > scores[b] ? a : b
    );

    const quiz = document.getElementById("quiz-container");

    quiz.innerHTML = `<h1>You are:</h1>
    <h2>${winner}</h2>
    `
}