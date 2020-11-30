from flask import Flask, request, render_template, url_for
from mock_data_loader import get_records

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Index Page'

@app.route('/dashboard',methods=['GET'])
def dashboard():
    if request.method == "GET":
        #generator = get_records()
        #row = next(generator)
        rows = [row for row in get_records()] #for faster and better usage implement https://flask.palletsprojects.com/en/1.1.x/patterns/streaming/
        return render_template('dashboard.html',rows=rows)
    else:
        return "Woohoo, an error!"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
