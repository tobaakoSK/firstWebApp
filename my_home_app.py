from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/whereami')
def whereami():
    return 'ghana'


@app.route('/howoldareyou/<age1>')
def age(age):
    return render_template('agePage.html',age1 = age)

@app.route('/foo/<name>')
def foo(name):
    return render_template('home_page.html',to = name)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')