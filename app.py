from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'MY-SECRET-KEY-'


class InfoForm(FlaskForm):
    breed = StringField("what breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField(u"Choose your mood:",
                      choices=[('mood_one', 'happy'), ('mood_two', 'excited')])
    food_choice = SelectField(u"Pick your favorite food:",
                              choices=[('chi', 'chicken'), ('bf', 'beef'), ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField("submit")


@app.route('/index-test')
def index_test():
    mylist = [1, 2, 3, 4, 5]
    names = ["name", "another", "matte", "Azul"]
    return render_template("basic.html", mylist=mylist, names=names)


@app.route("/", methods=['GET', 'POST'])
def index():
    form = InfoForm()

    if form.validate_on_submit():
        flash('you just did that!')
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session["food"] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thank_you'))
    return render_template('home.html', form=form)


@app.route('/signup_form')
def signup_form():
    return render_template("signup.html")


@app.route("/thank-you")
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template("thankyou.html", first=first, last=last)


@app.route("/person/<name>")
def person_name(name):
    return render_template('person.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(debug=True)
