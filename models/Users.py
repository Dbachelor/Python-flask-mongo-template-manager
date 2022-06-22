from config import connect


# db_name = "Test_DB"
# password = "password2022" 
# db_uri = "mongodb+srv://DBachelor:{}@cluster0.uvq93.mongodb.net/{}?retryWrites=true&w=majority".format(password, db_name)
# mydb.connect(host=db_uri)
mydb = connect()

class User(mydb.Document):
    
    first_name = mydb.StringField()
    last_name = mydb.StringField()
    email = mydb.EmailField()
    password = mydb.StringField()
    
    def toJSON(self):
        return {
            'first_name':self.first_name,
            'last_name':self.last_name,
            'email':self.email
        }
        
    #def register(self):
        