# python-opcua-data-to-database
Using Python through the OPC UA protocol, data from the induction motor and servo motor is acquired and posted to a database. The data is then pushed to a dashboard for display.

here my contribution is only on backend work:

The methodology followed to acquire data:
1) Data is accessed from SINUMERIK, including speed, current, voltage, torque, temperature, and power for both the induction and servo motors. Additionally, external sensor data from RTD and IEPE, acquired by the NI DAQ, is also pushed to the database in real time. The system acquiring the external sensor data has an OPC UA server and a sender client. The system that acquires internal motor data from the drive also accesses the external sensor data via OPC UA and subsequently pushes all the data to the database.
2) The backend work involves pushing data to four different tables in real time.

