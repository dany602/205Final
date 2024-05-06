import os
import random
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from random import shuffle
from PIL import Image
from image_info import image_info

app = Flask(__name__)
Bootstrap5(app)

@app.route('/')
def home():
    return render_template('index.html', images=image_info)

@app.route('')
def edit():
    return render_template('edit.html', image=image)

@app.route('')
def final():
    return render_template('detail.html', image=image, filter=filter)
