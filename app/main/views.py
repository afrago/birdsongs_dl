from . import main
from flask import request, render_template, redirect, url_for, flash, make_response, session, current_app



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload')
def upload():
    return render_template('upload.html')

@main.route('/test')
def test():
    return render_template('test.html')

@main.route('/results')
def results():
    return render_template('results.html')



@main.route('/keras-audio/<name>')
def kerasaudio(name):
    if name == 'cifar10':
        return render_template('keras-audio/keras-audio-cifar10.html')
    elif name == 'resnet':
        return render_template('keras-audio/keras-audio-resnet.html')
    else :
        return render_template('keras-audio/comparative.html')


