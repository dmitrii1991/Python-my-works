from find_in_phrase import find
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/find', methods=['POST'])
def to_find() -> 'html':
    phrase = request.form['word/phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(find(phrase, letters))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_psge() -> 'html':
    return render_template("entry.html", the_title='Welkome to the programm!!')

app.run(debug=True)
