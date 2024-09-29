from flask import Flask, request, make_response, render_template, redirect, url_for


app = Flask(__name__, template_folder= "templates")
@app.route("/")
def index():
    mylist = [10, 20, 30, 40, 50]
    return render_template("index.html", mylist = mylist)

@app.route("/Other")
def Other():
    some_text = "hello World"
    return render_template("other.html", some_text = some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('Other'))

@app.template_filter("revers_string")   
def revers_string(s):
    return s[::-1]

@app.template_filter("repeat")
def repeat (s, times= 2):
    return s * times

@app.template_filter("alternate_case")
def alternate_case(s):
    return ''.join([c.upper()if i % 2 ==0 else c.lower()for i, c in enumerate(s)])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5555, debug= True)
