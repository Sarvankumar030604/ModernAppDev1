from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///first.db'
db=SQLAlchemy(app)



class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String,nullable=False)
    Email_id=db.Column(db.String,unique=True,nullable=False)

with app.app_context():
    db.create_all()

@app.route('/create_User')
def create_User():
    user=User(username="Sarvan Kumar",password="123409876",Email_id="sarvan@localhost")
    db.session.add(user)
    db.session.commit()
    return "User Created"
@app.route('/getUsers')
def getUsers():
    users=User.query.all()
    return render_template("user.html",users=users)
@app.route("/updateUser/<int:userid>")
# def deleteUser(userid):
#     user=User.query.get(userid)
#     if user:
#         db.session.delete(user)
#         db.session.commit()
#         return "user deleted"
#     return "user not found"
def updateUser(userid):
    user=User.query.get(userid)
    if user:
        user.username="admin2"
        db.session.commit()
        return "user updated"
    return "user not found"
app.run(debug=True)
