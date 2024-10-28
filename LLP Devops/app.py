from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the front page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you can add login logic
        return redirect(url_for('courses'))
    return render_template('login.html')

# Route for the courses page
@app.route('/courses')
def courses():
    languages = ['English', 'Tamil', 'Telugu']
    levels = ['Basic', 'Intermediate', 'Advanced']
    return render_template('courses.html', languages=languages, levels=levels)

# Route for specific course and level page
@app.route('/courses/<language>/<level>')
def course_level(language, level):
    return render_template('course_level.html', language=language, level=level)

# Route for the exam page
@app.route('/exam')
def exam():
    return render_template('exam.html')

if __name__ == "__main__":
    app.run(debug=True)
