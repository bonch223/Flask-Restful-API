from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.student_model import StudentModel

class Student(Resource): 

    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="You don't have a name for this person?"
    )
    parser.add_argument('course',
        type=str,
        required=True,
        help="You're not a student if you don't take a course!"
    )
    parser.add_argument('year',
        type=int,
        required=True,
        help="Don't tell me it's 2018!"
    )
    parser.add_argument('gender',
        type=str,
        required=True,
        help="It's okay, im not sexist!"
    )

    def get(self, stude_id):
        item = StudentModel.find_by_id(stude_id)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, stude_id):
        if StudentModel.find_by_id(stude_id):
            return {'message': "Student ID '{}' already exist.".format(stude_id)}, 400

        data = request.get_json()
        item = StudentModel(stude_id, **data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occured in inserting the item."}, 500

        return item.json(), 201

    @jwt_required()
    def delete(self, stude_id):
        item = StudentModel.find_by_id(stude_id)
        if item:
            item.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self, stude_id):
        data = Student.parser.parse_args()
        item = StudentModel.find_by_id(stude_id)

        if item is None:
            item = StudentModel(stude_id, **data)
        else:
            item.name = data['name']
            item.course = data['course']
            item.year = data['year']
            item.gender = data['gender']

        item.save_to_db()

        return item.json()
    
 
class StudentList(Resource):
    def get(self):
        return {'students': [student.json() for student in StudentModel.query.all()]} # list(map(lambda x: x.json(), ItemModel.query.all()))
