from user import User


users = [
    User(1,'bob', '1234'),
    User(2,'rolf', '1234')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(paayload):
    user_id = paayload['identity']
    return userid_mapping.get(user_id, None)