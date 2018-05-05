from model import InputForm
from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from compute import compute


app = Flask(__name__)

# Model
class InputForm(Form):
    r = FloatField(validators=[validators.InputRequired()])

# View. The decorator @app.route maps the URL to /hw1
@app.route('/hw1', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        r = form.r.data
        s = compute(r)
        return render_template("view_output.html", form=form, s=s)
    else:
        return render_template("view_input.html", form=form)






if __name__ == '__main__':
    app.run(debug=True)