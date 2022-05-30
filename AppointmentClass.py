from DatabaseClass import Database
import datetime

class Appointment:
    def Create(Type, PersonnelID, PatientID):
      #Then we insert Data into Database
      sql = "INSERT INTO AppointmentTable (Type, PersonnelID, PatientID, StatusID) VALUES (%s, %s, %s, %s);"
      val = (Type, PersonnelID, PatientID, 1)
      result = Database.Insert(sql, val)

      return result;

    def Cancel(AppointmentID):
      sql = "UPDATE AppointmentTable SET StatusID = %s WHERE AppointmentID = %s;"
      val = (3, AppointmentID)

      result = Database.Update(sql, val)

      return result


    def Find():
      sql = "SELECT * FROM AppointmentTable WHERE StatusID = 1;"
      val = ""
      result = Database.Read(sql, val)
      
      return result

    def LastID(id):
      sql = "SELECT * FROM AppointmentTable WHERE AppointmentID = %s;"
      val = id
      result = Database.Read(sql, val)
      
      return result

    
