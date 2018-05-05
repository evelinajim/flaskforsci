from flask import Flask,render_template

app = Flask(__name__)


# decorator. for home page! /
@app.route('/')
def index():
    return'this is homepage'

#profile for real
@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)

#practicing personalization and variables. string

@app.route('/profile/<username>')
def profile(username):
    return'<h2> Good Morning %s </h2>' % username


#working with int
@app.route('/post/<int:post_id>')
def showpost(post_id):
    return'<h2> Post Id is: %s </h2>' % post_id


if __name__ == "__main__":
    app.run(debug = True)
