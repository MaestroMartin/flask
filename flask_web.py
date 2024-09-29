import os
from flask import Flask, request, render_template, Response,send_from_directory,jsonify
import pandas as pd
import uuid

app = Flask(__name__, template_folder= "templates")
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET' :
        return render_template("index.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'neuralnine' and password == 'password':
            return 'success'
        else:
            return 'Failure'
        
@app.route('/file_upload', methods = ['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type =='application/vnd.openxmlfomats-officedokument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.html

@app.route('/conver_csv', methods = ['POST'])
def convert_csv():
    file = request.files['file']
    
    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype= 'text/csv',
        headers={
            'Content-Disposition': 'atachment ; filename = result.csv '
        }
    )
    
    return response


@app.route('/conver_csv_two', methods = ['POST'])
def convert_csv_two():
    file = request.files['file']

    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('dowlands', filename))

    return render_template('download.html',filename =filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name = 'result.csv')

@app.route('/handle_post', methods = ['POST'])
def handle_post():
    greating = request.json['greating']
    name = request.json['name']

    with open('file.txt','w') as f:
        f.write(f'{greating}',f'{name}')
    
    return jsonify({'message':'Successfully written'})




if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5555, debug= True)
