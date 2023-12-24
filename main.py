import topic
import keywordgenerator
import youtubetool
from flask import Flask, request, render_template, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
import os

def main(topics):
    
   
  
    keywords_list = keywordgenerator.generate_keyword_list(topics)

    video_library = youtubetool.retrieve_videos(keywords_list)
    return video_library




app = Flask(__name__)
app.secret_key = 'your_secret_key' 
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
    # You could use the file path stored in the session here to display the file or its data
    uploaded_file_path = session.get('uploaded_file_path', None)
    return render_template('index.html', uploaded_file_path=uploaded_file_path)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash('File successfully uploaded')
        topics = topic.extract_topics_from_pdf(file_path)
        result = main(topics=topics)
        session['process_result'] = result

        flash('File successfully uploaded')
        return redirect(url_for('show_syllabus'))

    else:
        flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route("/syllabus")
def show_syllabus():
    topic_list = session['process_result']
    return render_template("/syllabus.html", topic_list=topic_list)

# Route to serve the uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)








