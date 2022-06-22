import datetime
from flask import Flask, request, jsonify
import mongoengine as mydb  
from werkzeug.security import generate_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from APIController import APIController
from models.Users import User
from models.Template import *
import json
from controllers.UsersController import UserController
from controllers.TemplatesController import TemplateController
app = Flask(__name__)    
 
db_name = "Test_DB"
password = "password2022" 
db_uri = "mongodb+srv://DBachelor:{}@cluster0.uvq93.mongodb.net/{}?retryWrites=true&w=majority".format(password, db_name)
mydb.connect(host=db_uri)

jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "khakinobeleatheragaracha"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)

@app.route('/')   
def home():  
    return "hello, this is our first flask website";  
 
@app.route('/users')
def users():
    users = APIController()
    return users.fetchNames()

@app.route('/register',methods = ['POST']) 
def register():
    request_data = request.get_json()
    first_name = request_data['last_name']
    last_name = request_data['first_name']
    email = request_data['email']
    password = generate_password_hash(request_data['password'], 'sha256')
    registerUser = UserController.register(first_name, last_name, email, password)
    if registerUser == 1:
        return {
            "status_code":201,
            "status_message":"user created successfully"
        }
    elif registerUser == 0:
        return {
            "status_code":400,
            "status_message":"failed to create user"
        }
    elif registerUser == 222:
        return {
                "status_message":"email already exists"
            }
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password'];
    loginUser = UserController.login(email, password)
    if loginUser == 500:
        return {
            "status_message":"no account found"
        }
    elif loginUser == 1:
        access_token = create_access_token(identity=email)
        return {
            "status_code":200,
            "status_message":"user LoggedIn successfully",
            "access_token":access_token
        }
    elif loginUser == 0:
        return {
            "status_message":"failed to login"
        }

@app.route('/template',methods = ['POST'])
@jwt_required()
def createTemplate():
    
    current_user = get_jwt_identity()
    user_from_db = User.objects(email =current_user)
    if user_from_db:
        data = request.get_json()
        template_name = data['template_name']
        subject = data['subject']
        body = data['body']
        template = TemplateController.create(template_name=template_name, subject=subject, body=body)
        if template == 500:
            return {
                'status_message':'template name already in use'
            }
        elif template==1:
            return {
                'status_code':201,
                'status_message':'Template created successfully'
            }
        else:
            return {
                'staus_message':'Failed to create template'
            }
        

@app.route("/template/<template_id>", methods=['GET'])
@app.route("/template", methods=['GET'])
@jwt_required()
def index(template_id=0):
    current_user = get_jwt_identity()
    user_from_db = User.objects(email =current_user)
    if user_from_db:
        if request.args.get('template_id') :
            template_id = request.args.get('template_id')
    
            temps = TemplateController.index(template_id)
            return {"data":temps}
            #print(temps)
        else:
            temps = TemplateController.index(template_id)
            return {"data":temps}
       
@app.route("/template/<template_id>", methods=["DELETE"])
@jwt_required()
def delete(template_id):
    current_user = get_jwt_identity()
    user_from_db = User.objects(email =current_user)
    if user_from_db:
        
        temp = TemplateController.delete(template_id)
        if temp == 404:
            return {
                "status_message":"no resource found"
            }
        elif temp == 1:
            return {
                "status_message":"resource deleted"
            }
        else:
            return {
                "status_message":"could not delete resource"
            }
        
@app.route("/template/<template_id>", methods=['PUT'])
@jwt_required()
def update(template_id): 
    current_user = get_jwt_identity()
    user_from_db = User.objects(email =current_user)
    if user_from_db:  
        data = request.get_json()
        template_name = data['template_name']
        body = data['body']
        subject = data['subject']   
        temp = TemplateController.update(template_id, template_name, body, subject)  
        if temp == 404:
            return {
            "status_message":"no resource found"
            }
        elif temp == 1:
            return {
                "status_message":"resource updated"
            }
        else:
            return {
                "status_message":"could not update resource"
            }
         
            
        
        
    
    
if __name__ =='__main__':  
    app.run(debug = True)  