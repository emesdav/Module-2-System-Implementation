import ValidationClass as Validate
from DatabaseClass import Database
import datetime

class Prescription:
    def Create(Type, PatientID, DoctorID, Quantity, Dosage):
        #Ensure each value is right
        #if Validate.ifInt(PatientID) or Validate.ifInt(DoctorID) or Validate.ifInt(Quantity) or Validate.ifFloat(Dosage):
        #Then we insert Data into Database
        sql = "INSERT INTO PrescriptionTable (Type, PatientID, PersonnelID, Quantity, Dosage, StatusID) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (Type, PatientID, DoctorID, Quantity, Dosage, 1)
        result = Database.Insert(sql, val)
        return result

    def Cancel():
        return "this is how I fight my battle"

    def View():
        sql = "SELECT * FROM PrescriptionTable WHERE StatusID = 1;"
        val = ""
        result = Database.Read(sql, val)
        return result