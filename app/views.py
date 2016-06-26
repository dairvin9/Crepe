from app import app
from flask import render_template,redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/shutdown')
def shutdown():
    return render_template('shutdown.html')

@app.route('/openprograms')
def openprograms():
    return render_template('openprograms.html')

@app.route('/desktopbackground')
def desktopbackgrounds():
    return render_template('desktopbackground.html')

@app.route('/friendlyintro')
def friendlyintro():
    return render_template('friendlyintro.html')

@app.route('/cddriveandhardware')
def cddriveandhardware():
    return render_template('cddriveandhardware.html')