from flask import Flask, request, jsonify
from sensor_data import Sensor_Reading

app = Flask(__name__)

@app.route('/request_data', methods=['GET'])
def send_data():
	temperature, pressure, humidity, oxygen, co, co2, proximity = Sensor_Reading()
	data = {
	"Temperature": "22.5 F"
	# ~ "Temperature": f"{temperature} F"
	# ~ "Pressure": f"{pressure}"
	# ~ "Humidity": f"{humidity}"
	# ~ "Oxygen": f"{oxygen}"
	# ~ "Carbon Monoxide": f"{co}"
	# ~ "Carbon Dioxide": f"{co2}"
	# ~ "Proximity": f"{proximity}"
	}
	return jsonify(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5000)
