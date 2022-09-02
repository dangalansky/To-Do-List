import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class NewList(FlaskForm):
    title = StringField("Name Your List!", validators=[DataRequired()])
    item = StringField("Enter list items, separated by comma: ")
    submit = SubmitField("Submit")


class Add(FlaskForm):
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


@app.route('/add_to_list', methods=['GET', 'POST'])
def add_to_list():
    form = Add()
    if form.validate_on_submit():
        with open('list.csv', 'a') as file:
            file.write(f',{form.item.data}')
        return home()
    return render_template('add_to_list.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete_list():
    with open('list.csv', 'w') as file:
        file.write('')
        return home()


@app.route('/remove', methods=['GET', 'POST'])
def remove():
    if request.method == "POST":
        with open('list.csv') as file:
            data = csv.reader(file, delimiter=',')
            list = []
            for row in data:
                list.append(row)
            new_list = list[0]
            removal_data = request.form
            removal_list = removal_data.getlist('array[]')
            for item in removal_list:
                to_remove = item
                new_list.remove(to_remove)
            with open('list.csv', 'w') as file:
                for item in new_list:
                    if new_list.index(item) == len(new_list)-1:
                        file.write(item)
                    else:
                        file.write(f'{item},')
    return home()


if __name__ == "__main__":
    app.run(port=5001, debug=True)
