import os
from flask import request, flash, redirect, render_template
from config import BaseConfig
from app import app
from flask import render_template
#deploying-keras-deep-learning-models-with-flask
from deeplearning.keras_audio.library.cifar10 import Cifar10AudioClassifier
from deeplearning.keras_audio.library.utility.afrago_loader import afrago_labels
import urllib.request

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and BaseConfig.allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

            classifier = Cifar10AudioClassifier()
            classifier.load_model(model_dir_path='./deeplearning/demo/models')

            predicted_label_id = classifier.predict_class('./deeplearning/demo/data/audio_samples/'+file.filename )
            predicted_label = afrago_labels[predicted_label_id]

            print('predicted: ', predicted_label)
            flash(predicted_label)
            return redirect('/upload')

@app.route('/xenocanto', methods=['POST'])
def get_file():
    if request.method == 'POST':
        print('Beginning file download from xento-canto...')
        audio_value = request.values.get('btnAudio')
        audio_id = audio_value[2:]
        url = 'https://www.xeno-canto.org/'+audio_id+'/download'
        filename = audio_id+'.mp3'
        path = app.config['UPLOAD_FOLDER']+audio_value+'.mp3'
        urllib.request.urlretrieve(url, path)
        classifier = Cifar10AudioClassifier()
        classifier.load_model(model_dir_path='./deeplearning/demo/models')

        predicted_label_id = classifier.predict_class('./deeplearning/demo/data/audio_samples/'+audio_value+'.mp3' )
        predicted_label = afrago_labels[predicted_label_id]

        print('predicted: ', predicted_label)
        flash(predicted_label)
        return redirect('/upload')
