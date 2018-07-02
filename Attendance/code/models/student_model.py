from db import db

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    stude_id = db.Column(db.String(9))
    name = db.Column(db.String(80))
    course = db.Column(db.String(80))
    year = db.Column(db.Integer)
    gender = db.Column(db.String(6))

    def __init__(self, stude_id, name, course, year, gender):
        self.stude_id = stude_id
        self.name = name
        self.course = course
        self.year = year
        self.gender = gender

    def json(self): 
        return {'student_id': self.stude_id, 'name': self.name, 'course': self.course, 'year': self.year, 'gender': self.gender}

    @classmethod
    def find_by_id(cls, stude_id):
        return cls.query.filter_by(stude_id=stude_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
