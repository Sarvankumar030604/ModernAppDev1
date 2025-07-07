from flask import Flask,render_template,request
app = Flask(__name__)
# @app.route("/")
# def home():
#     return render_template("course.html")
@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("form.html")
    if request.method == "POST":
        c_name=request.form["c_name"]
        id_value=request.form["id_value"]
        return render_template("course.html",c_name=c_name,id_value=id_value)
app.run(debug=True)  