"""
Deploy Flask App in IIS Server
"""
from flask import Flask, render_template, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'raksha'


@app.route("/")
def home():
    return "Hello, This is the Flask App in IIS Server."

@app.route('/cal', methods=['GET', 'POST'])
def sum():
    form = SignUpForm()
    if form.is_submitted():
        number1 = request.form.get('number1')
        number2 = request.form.get('number2')
        summ = int(number1) + int(number2)
        return render_template('blob.html', result=summ)

    return render_template('calculate.html', form=form)


if __name__ == "__main__":
    app.run()
