from admissionform import db

class user(db.Model):
    first_name=db.Column(db.String(20),primary_key=True)
    middle_name=db.Column(db.String(30),nullable=False)
    last_name=db.Column(db.String(30),nullable=False,unique=True)
    rel_name=db.Column(db.String(15),nullable=False)
    addr=db.Column(db.String(15),nullable=False)
    gen=db.Column(db.String(15),nullable=False)
    DOT=db.Column(db.String(15),nullable=False)
    mobno=db.Column(db.Integer,nullable=False)
    def __str__(self):
        return f"User({self.first_name},{self.middle_name},{self.last_name})"