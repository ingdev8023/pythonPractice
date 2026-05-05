from flask import Flask,jsonify, request,flash, redirect,url_for

app = Flask("Testing endpoints with Flask")

@app.route("/")
def index():
    return "<h3>Hello</h3> </br> <h1>WORLD</h1>"

@app.route("/home")
def home():
    return {"message":"testing dict"}

@app.route("/json")
def json():
    return jsonify(message="New dict turn into a JSON")

@app.route("/user", methods=["GET"])
def user():   
        test1 = request.endpoint   
        test2 = request.base_url 
        test3 = request.args 
        test4 = request.content_type 
        test5 = request.date 
        test6 = request.form #important!

        return test1, 200
        
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''    