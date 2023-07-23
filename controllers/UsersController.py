from models.Users import User
from werkzeug.security import check_password_hash


class UserController:
    def register(first_name, last_name, email, password):
        if email not in User.objects:
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            if user.save():
                return 201
            else:
                return 400
        else:
            return 222
    def login(email, password):
        user = User.objects(email=email).first()
        if user:
            db_email = user.email 
            db_pass = user.password
            if check_password_hash(db_pass, password):
                return 1
            else:
                return 0 
        else:
            return 500
        
        