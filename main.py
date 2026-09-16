from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv
import os
from database import *

app = Flask(__name__)
api = Api(app)
load_dotenv()
PORT = os.getenv("APP_PORT")

class HelloWorld(Resource):
    def get(self):
       
        return {'hello': 'world'}
    

class Categorias(Resource):
    def get(self):
        db1 = DataBase()
        response = db1.get_categories();
        return {'categorias': response}
        
api.add_resource(HelloWorld, '/')
api.add_resource(Categorias,"/categorias")

if __name__ == '__main__':
    app.run(debug=True,port=int(PORT))