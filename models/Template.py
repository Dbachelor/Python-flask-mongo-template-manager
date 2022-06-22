from config import connect
mydb = connect()


class Template(mydb.Document):
    

    
    template_name = mydb.StringField()
    subject = mydb.StringField()
    body = mydb.StringField()
    
    def toJSON(self):
        return {
            'template_name':self.template_name,
            'subject':self.subject,
            'body':self.body
        }