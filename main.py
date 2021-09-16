import os
from flask import Flask, flash, request, redirect, url_for, render_template

from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'tif','shp'])
path1 = []
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload2.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'files[]' not in request.files:
		flash('No file part')
		return redirect(request.url)

	files = request.files.getlist('files[]')#print(files)
	file_names = []
	for file in files:
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)

			file_names.append(filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	x1 = [(UPLOAD_FOLDER+ str(i))for i in file_names]
	path1.append(x1)

	print('display_image filename: ' ,str(x1))

	return render_template('upload2.html', filenames=file_names)

@app.route('/display/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route("/slider", methods=["POST"])
def test():
    red = request.form["r"]
    green = request.form["g"]
    blue = request.form["b"]

    x = str(red+","+green+","+blue)

    print(red,green,blue)
    print(path1)
    opimg = "army2.png"
	
    return render_template('upload2.html', filename1='static/uploads/' + opimg, code=301)
	
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5249)
