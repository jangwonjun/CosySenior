from models import db

class login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(10), nullable=False)
    
