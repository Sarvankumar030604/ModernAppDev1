from flask import Flask , render_template,request,url_for,redirect
app=Flask(__name__)

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        gender=request.form.get("gender")
        qualification=request.form.get("qual")
        stream=request.form.get("stream")
        address=request.form.get("add")
        return render_template("review.html",name=name,age=age,gender=gender,qualification=qualification,stream=stream,address=address)
    return render_template("register.html")
@app.route("/success")
def success():
    return "<h2> Your registration form has been submitted successfully </h2>"
app.run(debug=True)