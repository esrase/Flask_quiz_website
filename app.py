from flask import Flask, render_template, request, session, redirect, url_for
from backend import init_db, save_score, get_highscore

app = Flask(__name__)
app.secret_key = 'secret_key'

# Doğru cevaplar
correct_answers = {
    "soru1": "TensorFlow",
    "soru2": "Tokenization",
    "soru3": "CNN",
    "soru4": "Tuning"
}

# Veritabanını başlat
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        score = 0
        total_questions = len(correct_answers)

        # Cevap kontrolü
        for key, correct_answer in correct_answers.items():
            user_answer = request.form.get(key)
            if user_answer and user_answer.strip().lower() == correct_answer.lower():
                score += 100 / total_questions  # Her doğru cevap için puan ekle

        # Skoru veritabanına kaydet
        save_score(score)

        # Veritabanından yüksek skoru al
        highscore = get_highscore()

        # Yüksek skoru güncelle
        session['highscore'] = max(session.get('highscore', 0), highscore)
        
        return render_template('quiz_template.html', score=score, highscore=highscore)

    # GET isteği - sadece quiz formunu göster
    highscore = get_highscore()  # Veritabanından yüksek skoru al
    return render_template('quiz_template.html', highscore=highscore)

if __name__ == '__main__':
    app.run(debug=True)



