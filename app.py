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



# read_file = open(str(server_file)+'.json').read()

def creator():
    global employed

    
    astro_file = open('/astro_file.json').read()
    file_json = json.loads(astro_file)

    file_json['employed'] = employed
    


    with open('data.json', 'w') as outfile:
        json.dump(astroDB,outfile)
    
    
    number_version = astroDB['version']
    new_version = number_version + 1
    astroDB['version'] = new_version
    


    



@app.route('/',methods=['GET'])
def get():
    return 'ASTRO Server by Atlas - SOLEMDev S.A.S.'


@app.route('/',methods=['POST'])
def executor():
    global json_data
    data_recived = request.json
    json_data = data_recived
    print('Solicitud')
    if 'action' in json_data:
        print('Datos: ', json_data)
        ans = {}
        ans['emulacion'] = 'terminada'
        print('Proob OK')
        return ans





if __name__ == '__main__':
    app.run(debug= True, host= machine_ip)
    # app.run(debug= True)