from flask import Flask, request, render_template
import pickle
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/', methods=['GET', 'POST'])
def result():
    # If a form is submitted
    if request.method == "POST":
        model = model = pickle.load(open('model.pkl', 'rb'))
        n = request.form.get("N")
        p = request.form.get("P")
        k = request.form.get("K")
        temp = request.form.get("Temperature")
        hum = request.form.get("Humidity")
        ph = request.form.get("pH")
        rainf = request.form.get("Rainfall")

        # Get prediction
        prediction = model.predict([[n, p, k, temp, hum, ph, rainf]])
        str1 = ""
        str1 = str1.join(prediction)
        str1 = str1.capitalize()

    else:
        prediction = ""

    return render_template("index.html", output=str1)


if __name__ == '__main__':
    app.run(debug=False)