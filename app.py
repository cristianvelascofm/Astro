from flask import Flask, request
from flask_cors import CORS

import json
import os
import socket
import subprocess
import sys
import threading
import time
from threading import Timer


# Variables app Flask
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}) # Acepta dede todas las direcciones con el *


machine_ip = '192.168.56.1'
json_data = ''


# variables diccionario para el registro de información de la app
employed = [] # Empleados
client = [] # Clientes
product = [] # Prodcutos
supplie = [] # Insumos
date = [] # Citas
machine = [] # Máquinas
clinic_history = [] # Historia Clínica


astroDB = {}

def login_user(user):
    print('Usr: ',user)
    user_login = {}
    print ("Añgg: ",user['user_name'])
    astro_file = open('astro_file.json').read()
    file_json = json.loads(astro_file)
    print("Astro: ", file_json)
    for employed in file_json['employed']:
        
        if (employed['user_name'] == user['user_name']):
            print('Found_User')
            if (employed['password']== user['password']):
                print('Password OK')
                user_login = employed
                return user_login

            else:
                wrong = {"error": 'Login_Error' }
                return wrong


@app.route('/',methods=['GET'])
def get():
    return 'ASTRO Server by Atlas - SOLEMDev S.A.S.'


@app.route('/',methods=['POST'])
def executor():
    global json_data
    data_recived = request.json
    json_data = data_recived
    astro_file = open('astro_file.json').read()
    file_json = json.loads(astro_file)


    print('Solicitud')
    if 'action' in json_data:

        if json_data['action'] == 'login':
            employed_login = login_user(json_data)
            if employed_login:
                print('Login OK')
                return employed_login
            else:
                print('Login Error')
                ans={"error": "Login Failed"}
                return ans





if __name__ == '__main__':
    app.run(debug= True, host= machine_ip)
    # app.run(debug= True)