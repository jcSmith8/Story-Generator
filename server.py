from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('core/index.html')

@app.route('/contact')
def contact():
    return render_template('core/contact.html')

@app.route('/create')
def create():
    return render_template('core/form.html')

if __name__ == "__main__":
    app.run(debug=True)