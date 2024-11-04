from flask import Flask as fk, render_template, request, jsonify

app = fk(__name__)

# Dummy list of questions
questions = [
    "Hello 1 is true or false?",
    "Is Python a programming language?",
    "Is the sky blue during the day?",
]

# Counter to track current question
question_index = 0

@app.route("/")
def home():
    global question_index
    # Start with the first question
    current_question = questions[question_index]
    return render_template('quize.html', Question=current_question)

@app.route("/submit-answer", methods=["POST"])
def submit_answer():
    global question_index
    data = request.get_json()
    
    # Process the answer (here, just print or log it)
    answer = data['answer']
    print(f"User answered: {answer}")
    
    # Increment the question index to get the next question
    question_index += 1
    
    # If no more questions, reset or handle differently
    if question_index >= len(questions):
        return jsonify({"nextQuestion": "No more questions available."})

    # Return the next question
    return jsonify({"nextQuestion": questions[question_index]})

if __name__ == "__main__":
    app.run(debug=True)
