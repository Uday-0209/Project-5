import time

from opcua import Client
import mysql.connector
from datetime import datetime

import numpy as np
import pandas as pd

db_config = {
    'host': 'cmti-edge.online',       # Example: 'mysql.hostinger.com'
    'user': 'u797238576_opcua',
    'password': 'Haricmti@20',
    'database': 'u797238576_opcua'
}
client2 = Client("opc.tcp://DESKTOP-QNRBON3:49580")
client1 = Client("opc.tcp://192.168.100.0:4840")
client1.session_timeout = 3000
client2.session_timeout = 3000

# Set your username and password
client1.set_user("ADMIN")
client1.set_password("ADMIN123")

client2.set_user("ADMIN")
client2.set_password("ADMIN123")



try:
    client1.connect()
    print("Client 1 connected")
    client2.connect()
    print("Client 2 connected")
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Connected to the database")
        # SQL query to create a table
    cursor = conn.cursor()

    while True:
        # Rest of your code remains the same...
        node_1 = client1.get_node("ns=2;s=/Plc/DB190.DBD72:REAL")
        node_value_1 = node_1.get_value()

        node_2 = client1.get_node("ns=2;s=/Plc/DB190.DBD76:REAL")
        node_value_2 = node_2.get_value()

        node_3 = client1.get_node("ns=2;s=/Plc/DB190.DBD80:REAL")
        node_value_3 = node_3.get_value()

        node_4 = client1.get_node("ns=2;s=/Plc/DB190.DBD84:REAL")
        node_value_4 = node_4.get_value()

        node_5 = client1.get_node("ns=2;s=/Plc/DB190.DBD88:REAL")
        node_value_5 = node_5.get_value()

        node_6 = client1.get_node("ns=2;s=/Plc/DB190.DBD92:REAL")
        node_value_6 = node_6.get_value()

        node_7 = client1.get_node("ns=2;s=/Plc/DB190.DBD24:REAL")
        node_value_7 = node_7.get_value()

        node_8 = client1.get_node("ns=2;s=/Plc/DB190.DBD28:REAL")
        node_value_8 = node_8.get_value()

        node_9 = client1.get_node("ns=2;s=/Plc/DB190.DBD32:REAL")
        node_value_9 = node_9.get_value()

        node_10 = client1.get_node("ns=2;s=/Plc/DB190.DBD36:REAL")
        node_value_10 = node_10.get_value()

        node_11 = client1.get_node("ns=2;s=/Plc/DB190.DBD40:REAL")
        node_value_11 = node_11.get_value()

        node_12 = client1.get_node("ns=2;s=/Plc/DB190.DBD44:REAL")
        node_value_12 = node_12.get_value()

        node_13 = client1.get_node("ns=2;s=/Nck/MachineAxis/measPos1[2]")
        node_value_13 = node_13.get_value()

        node_14 = client2.get_node("ns=2;s=channel 1")
        node_value_14 = node_14.get_value()

        node_15 = client2.get_node("ns=2;s=channel 2")
        node_value_15 = node_15.get_value()

        node_16 = client2.get_node("ns=2;s=channel 3")
        node_value_16 = node_16.get_value()

        node_17 = client2.get_node("ns=2;s=channel 4")
        node_value_17 = node_17.get_value()

        node_18 = client2.get_node("ns=2;s=Temp1")
        node_value_18 = node_18.get_value()

        node_19 = client2.get_node("ns=2;s=Temp 2")
        node_value_19 = node_19.get_value()

        node_20 = client2.get_node("ns=2;s=Temp 3")
        node_value_20 = node_20.get_value()

        node_21 = client2.get_node("ns=2;s=Temp 4")
        node_value_21 = node_21.get_value()

        node_22 = client2.get_node("ns=2;s=Temp 5")
        node_value_22 = node_22.get_value()


        # Get current date and time in real-world format
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        input_data = (current_time, str(node_value_1), str(node_value_2), str(node_value_3), str(node_value_4), str(node_value_5),str(node_value_6))
        feed_data = (current_time, str(node_value_13), str(node_value_7), str(node_value_8), str(node_value_9), str(node_value_10), str(node_value_11), str(node_value_12))
        Vibration_data = (current_time, str(node_value_14), str(node_value_15), str(node_value_16), str(node_value_17))
        Temperature_data = (current_time, str(node_value_18), str(node_value_19), str(node_value_20), str(node_value_21), str(node_value_22))

        # changing the input_data to a numpy array

        insert_query1 = "INSERT INTO opc (Time_stamp, Speed, Torque, Voltage, Current, Power, Temperature) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        insert_query2 = "INSERT INTO Feed_drive (Time_stamp, Position, Speed, Torque, Voltage, Current, Power, Temperature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        insert_query3 = "INSERT INTO Vibration_data (Time_stamp, X, Y, Z, Couple) VALUES (%s, %s, %s, %s, %s)"
        insert_query4 = "INSERT INTO Temperature_data (Time_stamp, Xp, Xm, Xb, Y, Yb) VALUES (%s, %s, %s, %s, %s, %s)"


        # Execute query
        cursor.execute(insert_query1, input_data)
        cursor.execute(insert_query2, feed_data)
        cursor.execute(insert_query3, Vibration_data)
        cursor.execute(insert_query4, Temperature_data)
        conn.commit()
        print(f"{cursor.rowcount} record inserted.")

        time.sleep(1)


finally:
    client1.disconnect()
    client2.disconnect()

