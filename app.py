from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess == session['number']:
            message = f"Congratulations! You guessed the correct number in {session['attempts']} attempts!"
            session.pop('number')
            session.pop('attempts')
            return render_template('result.html', message=message)

        hint = "Higher" if guess < session['number'] else "Lower"
        return render_template('home.html', hint=hint)

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
