from flask import Flask, jsonify
from flask_cors import CORS
import time
import atexit

import serial

app = Flask(__name__)
CORS(app)


@app.before_first_request
def setupSerial():
    global arduino
    """ subistituir por /COM/ alguma coisa da porta no windows -  /dev/tty.usbmodem411 """

    # descomentar todos os arduinos
    # arduino = serial.Serial("/dev/tty.usbmodem411", 9600, timeout=1)


@app.route("/")
def index():
    """
    value = arduino.readline()
    balance = arduino.readline()
    print(value.rstrip())
    print(balance.rstrip())
    """
    return jsonify({"olá": "Mundo", "Time": "Vencedor"})


@atexit.register
def disconect():
    # arduino.closePort()
    print("Close Port")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True, use_reloader=True)
