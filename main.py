from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Optional
import csv


app = Flask(__name__)
app.secret_key = 'somekey'
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    coffee_choices = ['😵', '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕']
    wifi_choices = ['😟', '🛜', '🛜🛜', '🛜🛜🛜', '🛜🛜🛜🛜', '🛜🛜🛜🛜🛜']
    power_choices = ['😟', '⚡', '⚡⚡', '⚡⚡⚡', '⚡⚡⚡⚡', '⚡⚡⚡⚡⚡']

    cafe = StringField(label='Cafe name', description="Name of the cafe.",
                       validators=[DataRequired()])
    location = StringField(label='Location url', description="URL of the cafe starting with 'https://...'",
                           validators=[URL()])
    open = StringField(label='Opening time', description="Opening time of the cafe in the format of 'HHPM' or 'HH:MMAM'",
                       validators=[DataRequired()])
    close = StringField(label='Closing time', description="Closing time of the cafe in the format of 'HHPM' or 'HH:MMAM'",
                        validators=[DataRequired()])
    coffee = SelectField(label='Coffee rating', description="How good was the coffee?",
                         choices=coffee_choices,
                         validators=[Optional()])
    wifi = SelectField(label='Wifi rating', description="How good was the wifi?",
                       choices=wifi_choices,
                       validators=[Optional()])
    power = SelectField(label='Power outlet rating', description="Are there enough power outlets?",
                        choices=power_choices,
                        validators=[Optional()])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.is_submitted():
        print("submitted")
    if form.validate():
        print("valid")
    print(form.errors)
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding="utf-8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
