from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

# Doğru cevaplar
correct_answers = {
    "soru1": "TensorFlow",
    "soru2": "Tokenization",
    "soru3": "CNN",
    "soru4": "Tuning"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'highscore' not in session:
        session['highscore'] = 0

    if request.method == 'POST':
        score = 0
        total_questions = len(correct_answers)

        # Cevap kontrolü
        for key, correct_answer in correct_answers.items():
            user_answer = request.form.get(key)
            if user_answer and user_answer.strip().lower() == correct_answer.lower():
                score += 100 / total_questions  # Her doğru cevap için puan ekle

        # Yüksek skoru güncelle
        session['highscore'] = max(session['highscore'], score)
        return render_template('quiz_template.html', score=score, highscore=session['highscore'])

    return render_template('quiz_template.html', highscore=session['highscore'])

if __name__ == '__main__':
    app.run(debug=True)


