import mongoengine as mydb

def connect():
    db_name = "Test_DB"
    password = "password2022" 
    db_uri = "mongodb+srv://DBachelor:{}@cluster0.uvq93.mongodb.net/{}?retryWrites=true&w=majority".format(password, db_name)
    mydb.connect(host=db_uri)
    return mydb;