from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_me():
    return render_template('about.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False)