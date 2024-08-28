from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'highscore' not in session:
        session['highscore'] = 0

    if request.method == 'POST':
        score = 0
        if request.form.get('soru1').strip() != "":
            score += 25  # Örnek puanlama sistemi
        if request.form.get('soru2'):
            score += 25
        if request.form.get('soru3'):
            score += 25
        if request.form.get('soru4').strip() != "":
            score += 25

        session['highscore'] = max(session['highscore'], score)
        return render_template('quiz_template.html', score=score, highscore=session['highscore'])

    return render_template('quiz_template.html', highscore=session['highscore'])

if __name__ == '__main__':
    app.run(debug=True)


