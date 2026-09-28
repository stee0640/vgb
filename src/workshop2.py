from flask import Flask

app = Flask('vampyrborg')

from flask import render_template

@app.route('/')
def borg():
    return render_template('borg.html', baggrund = 'borg.webp')

@app.route('/tronsal')
def tronsal():
    return render_template('tronsal.html')

@app.route('/vagtstue')
def vagtstue():
    return render_template('vagtstue.html')

app.run()