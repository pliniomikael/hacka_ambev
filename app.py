from flask import Flask, jsonify
from flask_cors import CORS
import time
import atexit
from datetime import datetime
import serial

app = Flask(__name__)
CORS(app)


@app.before_first_request
def setupSerial():
    global arduino
    """ subistituir por /COM/ alguma coisa da porta no windows -  /dev/tty.usbmodem411 """

    arduino = serial.Serial("COM5", 9600, timeout=1)


@app.route("/")
def index():

    now = datetime.now()
    data = now.strftime("%d/%m/%Y")
    hora = now.strftime("%H:%M:%S")
    value = arduino.readline()
    alcool = str(value)

    return jsonify(
        {
            "date": data,
            "time": hora,
            "title": "Teor Alcoólico",
            "percent": alcool,
        }
    )


@atexit.register
def disconect():
    arduino.closePort()
    print("Close Port")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True, use_reloader=True)
