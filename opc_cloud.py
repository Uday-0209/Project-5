import mysql.connector
import numpy as np

# Database connection details
db_config = {
    'host': 'cmti-edge.online',       # Example: 'mysql.hostinger.com'
    'user': 'u797238576_opcua',
    'password': 'Haricmti@20',
    'database': 'u797238576_opcua'
}

# Connect to the database
try:
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Connected to the database")
        # SQL query to create a table
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Temperature_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Time_stamp DATETIME, 
        Xp varchar(10),
        Xm varchar(10),
        Xb varchar(10),
        Y varchar(10),
        Yb varchar(10)        
    )
    """
    # i = 0
    # for i in range(20):
    #     speed = np.random.choice([1200,2000,2521,154,1465,4654,454,454,4654,654,454,654])
    #     torque = np.random.choice([2.8,2.3,2.5,3.2,3.4,3.7,1.9,2.5,7.8,3.8,3.3])
    #     voltage = np.random.choice([258,266,288,245,352,326,312,253,222,213,231])
    #     current = np.random.choice([12,21,8,9,7,5,4,8,6,5,7,9])
    #     power = np.random.choice([2.4,1.4,5.4,2.3,2.4,3.2,3.3,3.4,3.6])
    #     temperature = np.random.choice([45,44,42,40,41,48,49,52,44,47])
    #
    #     data = (str(speed), str(torque), str(voltage), str(current), str(power), str(temperature))
    #
    #     # SQL query to insert data
    #     insert_query = "INSERT INTO opc (Speed, Torque, Voltage, Current, Power, Temperature) VALUES (%s, %s, %s, %s, %s, %s)"
    #
        # Execute query
        # cursor.execute(create_table_query)
        # conn.commit()
        # print(f"{cursor.rowcount} record inserted.")
        
    
    cursor.execute(create_table_query)
    conn.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")