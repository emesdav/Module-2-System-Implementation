from flask import Flask, render_template, request, redirect, url_for
from AppointmentClass import Appointment
from PrescriptionClass import Prescription

app = Flask(__name__)

userType = "Patient"

########START
@app.route('/', methods=['POST', 'GET'])
@app.route('/switchuser', methods=['POST', 'GET'])
def index():
  global userType 
  userType = ""
  if request.method == 'POST':
    userType = request.form['usertype']
    if userType == "Doctor":
      return redirect('/prescriptions')
    
    if userType == "Receptionist" or userType == "Patient":
      return redirect('/appointments')

  return render_template('index.html', user = userType)

########APPOINTMENTS
@app.route('/appointments/', methods=['POST', 'GET'])
@app.route('/appointments', methods=['POST', 'GET'])
def CreateAppointment():
  state = "get"
  if request.method == 'POST':
    Type = request.form['type']
    PersonnelID = request.form['personnelid']
    PatientID = request.form['patientid']
    Appointment.Create(Type, PersonnelID, PatientID)
    state = "set"
  
  if request.method == 'GET':
    Action = request.args.get('action')
    AppointmentID = request.args.get('appointmentid')    
    if Action == "cancel":
      Appointment.Cancel(AppointmentID)
      state = "get"

  #appointment = Appointment.Create("Type", "2022-05-05", "2022-06-06", 1, 1)
  AppointmentData = Appointment.Find()
  #appointmentConfirmationData = Appointment.LastID(result)
  return render_template('CreateAppointment.html', state = state, user = userType, AppointmentData = AppointmentData)


########PRESCRIPTIONS
@app.route('/prescriptions', methods=['POST', 'GET'])
def CreatePrescription():
  state = "get"
  if request.method == 'POST':
    Type = request.form['type']
    PatientID = request.form['patientid']
    DoctorID = request.form['doctorid']
    Quantity = request.form['quantity']
    Dosage = request.form['dosage']
    Prescription.Create(Type, PatientID, DoctorID, Quantity, Dosage)
    state = "set"
  
  PrescriptionData = Prescription.View()
  return render_template('CreatePrescription.html', user = userType, PrescriptionData = PrescriptionData, state=state)

if __name__ == '__main__':
    app.run(host='0.0.0.0')