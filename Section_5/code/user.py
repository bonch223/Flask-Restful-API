import sqlite3
from flask_restful import Resource, reqparse

class User:

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('./Section_5/code/data.db')
        cursor = conn.cursor()

        select_query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(select_query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user
        
    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('./Section_5/code/data.db')
        cursor = conn.cursor()

        select_query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(select_query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()
        return user

class UserRegister(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type = str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('password',
        type = str,
        required=True,
        help="This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "Username already taken!"}, 400

        conn = sqlite3.connect('./Section_5/code/data.db')
        cursor = conn.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query,(data['username'], data['password'],))

        conn.commit()
        conn.close()

        return {"message": "User successfully created!"}, 201