from flask import Flask, request, make_response, render_template


app = Flask(__name__, template_folder= "templates")
@app.route("/")
def index():
    mylist = [10, 20, 30, 40, 50]
    return render_template("index.html", mylist = mylist)

@app.route("/other")
def Other():
    some_text = "hello World"
    return render_template("other.html", some_text = some_text)

@app.template_filter("revers_string")
def revers_string(s):
    return s[::-1]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5555, debug= True)