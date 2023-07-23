from models.Template import Template
from flask import jsonify
import json


class TemplateController:
  
    def create(template_name, subject, body):
        if template_name in Template.objects(template_name=template_name):
            return 403
        template = Template(template_name=template_name, subject=subject, body=body)
        if template.save():
            return 1
        else:
            return 0
    
    def index(template_id=0):
        data = []
        if (template_id == 0):           
            
            templates = Template.objects().to_json()
            
                    
            return json.loads(templates)
            
        else:
            templates = Template.objects(id=template_id)
            for template in templates:
                    list = {"template_name":template.template_name, "subject":template.subject, "body":template.body}
                    
                    data.append(list)
                    
                    return data
        
    def update(template_id, template_name, body, subject):
        template = Template.objects(id=template_id)
        if template.count() > 0:
            if Template.objects(id=template_id).update_one(template_name=template_name, body=body, subject=subject):
                return 1
            else:
                return 0
        else:
            return 404
        
        
    
    def delete(template_id):
        template = Template.objects(id=template_id)
        if template.count() > 0:
            if Template.objects(id=template_id).delete():
                return 1
            else:
                return 0
        else:
            return 404  
            
        
        
        
        