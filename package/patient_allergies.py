#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn




class Patients_allergies(Resource):
    """It contain all the api carryign the activity with aand specific patient"""

    def get(self):
        """Api to retive all the patient from the database"""

        patients_allergies = conn.execute("SELECT * FROM patient_allergies  ORDER BY pat_id DESC").fetchall()
        return patients_allergies



    def post(self):
        """api to add the patient in the database"""

        patient_allergiesInput = request.get_json(force=True)
        pat_first_name=patient_allergiesInput['pat_first_name']
        pat_last_name = patient_allergiesInput['pat_last_name']
        pat_allergies = patient_allergiesInput['pat_allergies']
        patient_allergiesInput['pat_id']=conn.execute('''INSERT INTO patient_allergies(pat_first_name,pat_last_name,pat_allergies,pat_blood_sugar)
            VALUES(?,?,?,?,?)''', (pat_first_name, pat_last_name, pat_allergies)).lastrowid
        conn.commit()
        return patient_allergiesInput

class Patient_allergies(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrive details of the patient by it id"""

        patient_allergies = conn.execute("SELECT * FROM patient_allergies WHERE pat_id=?",(id,)).fetchall()
        return patient_allergies

    def delete(self,id):
        """api to delete the patiend by its id"""

        conn.execute("DELETE FROM patient_allergies WHERE pat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by it id"""

        patient_allergiesInput = request.get_json(force=True)
        pat_first_name = patient_allergiesInput['pat_first_name']
        pat_last_name = patient_allergiesInput['pat_last_name']
        pat_allergies = patient_allergiesInput['pat_allergies']
        conn.execute("UPDATE patient_allergies SET pat_first_name=?,pat_last_name=?,pat_allergies=?,pat_blood_sugar=? WHERE pat_id=?",
                     (pat_first_name, pat_last_name, pat_allergies,id))
        conn.commit()
        return patient_allergiesInput