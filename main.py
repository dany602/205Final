import base64
from io import BytesIO
import os
import random
from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap5
from random import shuffle
from PIL import Image
from image_info import image_info
from filters import apply_sepia, apply_negative, apply_grayscale, create_thumbnail
from werkzeug.utils import secure_filename

"""
    Name: Drake Goldsmith, Jasmin Medrano, Daniel Bonilla Urtis
    Date: 05/13/24
    Course: CST 205: Multimedia Programming
    Description: A program that allows the user to select a default image or upload their own.
    Then allows the user to add a filter to the image and save it.
"""

app = Flask(__name__)
Bootstrap5(app)

# Drake worked on def home, detail, and final
@app.route('/')
def home():
    shuffle(image_info)
    random_images = []
    for count in range(3):
        random_images.append(image_info[count])
    return render_template('index.html', random_images=random_images)

@app.route('/picture/<image_id>')
@app.route('/detail/<image_id>')
def detail(image_id):
    for info in image_info:
        if info["id"] == image_id:
            image = info
            break
    image_path = os.path.join(app.root_path, 'static', 'images', f'{image_id}.jpg')
    
    if os.path.exists(image_path):
        with Image.open(image_path) as img:
            width, height = img.size
            mode = img.mode
            image_format = img.format
        return render_template('detail.html', image=image, width=width, height=height, mode=mode, format=image_format)


@app.route('/final')
def final():
    image_id = request.args.get('image_id')
    filter_name = request.args.get('filter')

    for info in image_info:
        if info["id"] == image_id:
            image = info
            break

    image_path = os.path.join(app.root_path, 'static', 'images', f'{image_id}.jpg')
    if os.path.exists(image_path):
        with Image.open(image_path) as img:

            if filter_name == 'apply_sepia':
                filtered_image = apply_sepia(img)
            elif filter_name == 'apply_negative':
                filtered_image = apply_negative(img)
            elif filter_name == 'apply_grayscale':
                filtered_image = apply_grayscale(img)
            elif filter_name == 'create_thumbnail':
                filtered_image = create_thumbnail(img)

            filtered_image_path = os.path.join(app.root_path, 'static', 'filtered_images', f'{image_id}_filtered.jpg')
            filtered_image.save(filtered_image_path)
            
    return render_template('final.html', image=image, filtered_image_path=filtered_image_path)

# Daniel worked on def upload and edit
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.root_path, 'static', 'uploaded_images', filename)
        file.save(file_path)
        new_image_id = filename.split('.')[0]
        image_info.append({"id": new_image_id, "filename": filename})
        return redirect(url_for('edit', filename=filename))
    return "File upload failed", 400

@app.route('/edit')
def edit():
    filename = request.args.get('filename')
    return render_template('edit.html', filename=filename)

# Jasmin worked on def apply_filter
@app.route('/apply_filter')
def apply_filter():
    filename = request.args.get('filename')
    filter_name = request.args.get('filter')
    file_path = os.path.join(app.root_path, 'static', 'uploaded_images', filename)
    
    if os.path.exists(file_path):
        with Image.open(file_path) as img:
            if filter_name == 'apply_sepia':
                filtered_image = apply_sepia(img)
            elif filter_name == 'apply_negative':
                filtered_image = apply_negative(img)
            elif filter_name == 'apply_grayscale':
                filtered_image = apply_grayscale(img)
            elif filter_name == 'create_thumbnail':
                filtered_image = create_thumbnail(img)
            
            filtered_image_filename = f'filtered_{filename}'
            filtered_image_path = os.path.join(app.root_path, 'static', 'filtered_images', filtered_image_filename)
            filtered_image.save(filtered_image_path)
            return render_template('filtered.html', original_filename=filename, filtered_image_filename=filtered_image_filename)
    return "Error applying filter", 400


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True)
