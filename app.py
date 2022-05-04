from flask import Flask,send_from_directory,render_template
from flask_restful import Resource, Api
from package.patient import Patients, Patient
from package.patient_allergies import Patients_allergies, Patient_allergies
from package.patient_health import Patients_health, Patient_health
from package.patient_vaccine import Patients_vaccine
from package.doctor import Doctors, Doctor
from package.appointment import Appointments, Appointment
from package.common import Common
import json

with open('config.json') as data_file:
    config = json.load(data_file)

app = Flask(__name__, static_url_path='')
api = Api(app)

api.add_resource(Patients, '/patient')
api.add_resource(Patient, '/patient/<int:id>')
api.add_resource(Patients_health, '/patient_health')
api.add_resource(Patient_health, '/patient_health/<int:id>')
api.add_resource(Patients_vaccine, '/patient_vaccine')
api.add_resource(Patients_allergies, '/patient_allergies')
api.add_resource(Patient_allergies, '/patient_allergies/<int:id>')
api.add_resource(Doctors, '/doctor')
api.add_resource(Doctor, '/doctor/<int:id>')
api.add_resource(Appointments, '/appointment')
api.add_resource(Appointment, '/appointment/<int:id>')
api.add_resource(Common, '/common')

# Routes

@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(debug=True,host=config['host'],port=config['port'])