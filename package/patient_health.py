#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn




class Patients_health(Resource):
    """It contain all the api carryign the activity with aand specific patient"""

    def get(self):
        """Api to retive all the patient from the database"""

        patients_health = conn.execute("SELECT * FROM patient_health  ORDER BY pat_id DESC").fetchall()
        return patients_health



    def post(self):
        """api to add the patient in the database"""

        patient_healthInput = request.get_json(force=True)
        pat_first_name=patient_healthInput['pat_first_name']
        pat_last_name = patient_healthInput['pat_last_name']
        pat_blood_pressure = patient_healthInput['pat_blood_pressure']
        pat_blood_sugar = patient_healthInput['pat_blood_sugar']
        patient_healthInput['pat_id']=conn.execute('''INSERT INTO patient_health(pat_first_name,pat_last_name,pat_blood_pressure,pat_blood_sugar)
            VALUES(?,?,?,?,?)''', (pat_first_name, pat_last_name, pat_blood_pressure,pat_blood_sugar)).lastrowid
        conn.commit()
        return patient_healthInput

class Patient_health(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrive details of the patient by it id"""

        patient_health = conn.execute("SELECT * FROM patient_health WHERE pat_id=?",(id,)).fetchall()
        return patient_health

    def delete(self,id):
        """api to delete the patiend by its id"""

        conn.execute("DELETE FROM patient_health WHERE pat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by it id"""

        patient_healthInput = request.get_json(force=True)
        pat_first_name = patient_healthInput['pat_first_name']
        pat_last_name = patient_healthInput['pat_last_name']
        pat_blood_pressure = patient_healthInput['pat_blood_pressure']
        pat_blood_sugar = patient_healthInput['pat_blood_sugar']
        conn.execute("UPDATE patient_health SET pat_first_name=?,pat_last_name=?,pat_blood_pressure=?,pat_blood_sugar=? WHERE pat_id=?",
                     (pat_first_name, pat_last_name, pat_blood_pressure,pat_blood_sugar,id))
        conn.commit()
        return patient_healthInput