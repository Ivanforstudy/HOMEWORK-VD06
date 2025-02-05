
from flask import Flask, render_template, request

app = Flask(__name__)
submissions = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       name = request.form['name']
       age = request.form['age']
       city = request.form['city']
       hobby = request.form['hobby']
       submissions.append({'name': name, 'age': age, 'city': city, 'hobby': hobby})
       return render_template('result.html', submissions=submissions)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)









