from app import db #importar modelo api de api

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.integer, primary_key=true)
    name = db.Column(db.String(100), nullable=false)
    email = db.Column(db.String(100), nullable=false, unique=true)

