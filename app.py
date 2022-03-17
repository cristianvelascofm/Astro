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

json_data = ''


@app.route('/',methods=['GET'])
def get():
    return 'Body Laser Server by Atlas - SOLEMDev S.A.S.'


@app.route('/',methods=['POST'])
def executor():
    global json_data
    content = request.json
    json_data = content
    print('Solicitud')
    if 'action' in json_data:
        ans = {}
        ans['emulacion'] = 'terminada'
        print('Proob OK')
        return ans





if __name__ == '__main__':
    app.run(debug= True, host='192.168.130.79')
    # app.run(debug= True)