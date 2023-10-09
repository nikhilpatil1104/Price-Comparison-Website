from flask import Flask, render_template, request, redirect, url_for
from flipkart import inputData

app = Flask(__name__, template_folder='templates', static_folder='staticFolder')


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        input = request.form["prodName"]
        return redirect(url_for("electronics", name=input))
    else:
        return render_template("index.html")


@app.route('/<name>')
def electronics(name):
    if name:
        data = inputData(name)
        return render_template('electronics.html', inp=name, result=data)
    else:
        return render_template('electronics.html', inp="Product Not found")


if __name__ == "__main__":
    app.run(debug=True)
