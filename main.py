import csv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class NewList(FlaskForm):
    title = StringField("Name Your List!", validators=[DataRequired()])
    item = StringField("Enter list items, separated by comma: ")
    submit = SubmitField("Submit")



@app.route('/')
def home():
    with open('list.csv') as file:
        data = csv.reader(file, delimiter=',')
        list = []
        for row in data:
            list.append(row)
    return render_template('index.html', todo=list)


@app.route('/create_list', methods=['GET', 'POST'])
def new_list():
    form = NewList()
    if form.validate_on_submit():
        with open('list.csv', 'w') as file:
            file.write(f'{form.title.data},{form.item.data}')
        return home()
    return render_template('new_list.html', form=form)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
