from flask import Flask,render_template
from flask import url_for

app = Flask(__name__)
posts = [
    {
        'author': 'Januka Madushan',
        'title': 'Post 01',
        'content': 'Sample Post 01',
        'date_posted': 'August 28,2019'
    },
    {
        'author': 'Januka Madushan',
        'title': 'Post 02',
        'content': 'Sample Post 02',
        'date_posted': 'August 28,2019'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title="About")




if __name__ == '__main__':
    app.run(debug=True)