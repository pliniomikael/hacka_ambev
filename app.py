from flask import Flask, jsonify
from flask_cors import CORS
import time
import atexit
from datetime import datetime
import serial

app = Flask(__name__)
CORS(app)

result = {
    "5": "1532,45",
    "4,70": "1533,03",
    "4,40": "1533,62",
    "4,10": "1534,18",
    "3,80": "1534,75",
    "3,50": "1535,33",
    "3,20": "1535,92",
    "2,90": "1536,5",
    "2,60": "1537,05",
}


@app.before_first_request
def setupSerial():
    global arduino
    """ subistituir por /COM/ alguma coisa da porta no windows -  /dev/tty.usbmodem411 """

    # descomentar todos os arduinos
    # arduino = serial.Serial("COM5", 9600, timeout=1)


@app.route("/")
def index():
    # print(result["5"])
    now = datetime.now()
    data = now.strftime("%d/%m/%Y")
    hora = now.strftime("%H:%M:%S")
    # value = arduino.readline()
    # alcool = str(value)

    return jsonify(
        {
            "date": data,
            "time": hora,
            "title": "Alcool",
            "percent": "alcool",
        }
    )


@atexit.register
def disconect():
    # arduino.closePort()
    print("Close Port")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True, use_reloader=True)
