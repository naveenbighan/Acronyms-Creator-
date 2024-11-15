from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_acronym():
    phrase = request.form['phrase']
    
    acronym = ''.join(word[0].upper() for word in phrase.split() if word)
    
    return render_template('index.html', phrase=phrase, acronym=acronym)

if __name__ == '__main__':
    app.run(debug=True)
