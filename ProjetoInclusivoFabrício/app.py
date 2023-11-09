from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from video_processor import extract_text_from_video
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
        f.save(video_path)
        text = extract_text_from_video(video_path)
        return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
