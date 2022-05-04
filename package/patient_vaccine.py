#Tushar Borole
#Python 2.7

from flask_restful import Resource, Api, request
from package.model import conn



class Patients_vaccine(Resource):
    """This contain apis to carry out activity with all appiontments"""

    def get(self):
        """Retrive all the appointment and return in form of json"""

        patient_vaccine = conn.execute("SELECT * from patient_vaccine ORDER BY pat_vaccine_date DESC").fetchall()
        return patient_vaccine

    def post(self):
        """Create the appoitment by assiciating patient and docter with appointment date"""

        patient_vaccine = request.get_json(force=True)
        pat_id = patient_vaccine['pat_id']
        pat_vaccine = patient_vaccine['pat_vaccine']
        pat_vaccine_date = patient_vaccine['pat_vaccine_date']
        patient_vaccine['pat_id'] = conn.execute('''INSERT INTO patient_vaccine(pat_id,pat_vaccine,pat_vaccine_date)
            VALUES(?,?,?)''', (pat_id, pat_vaccine,pat_vaccine_date)).lastrowid
        conn.commit()
        return patient_vaccine





    def delete(self):
        """Delete teh appointment by its id"""

        conn.execute("DELETE FROM patient_vaccine WHERE app_id=?")
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self):
        """Update the appointment details by the appointment id"""

        patient_vaccine = request.get_json(force=True)
        pat_id = patient_vaccine['pat_id']
        pat_vaccine = patient_vaccine['pat_vaccine']
        conn.execute("UPDATE patient_vaccine SET pat_id=?,pat_vaccine=?",
                     (pat_id, pat_vaccine))
        conn.commit()
        return patient_vaccine