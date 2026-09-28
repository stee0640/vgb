from flask import Flask

app = Flask('vampyrborg')

from flask import render_template

@app.route('/')
def borg():
    return render_template('borg.html')

app.run()