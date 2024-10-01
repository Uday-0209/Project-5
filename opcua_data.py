from opcua import Client
from opcua import ua
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the server URL and credentials
server_url = "opc.tcp://192.168.100.0:4840"
username = "ADMIN"
password = "ADMIN123"

try:
    # Create a Client instance
    client = Client(server_url)

    # Set the security policy and mode (if required)
    client.set_security_string("Basic128Rsa15,SignAndEncrypt")

    # Set username and password for authentication
    client.set_user(username)
    client.set_password(password)

    # Connect to the server
    client.connect()
    logging.info("Connected to OPC UA server")

    # Perform your operations here (e.g., read/write nodes)
    root = client.get_root_node()
    print("Root node is: ", root)

    # Example of reading a value from a node
    node_id = "ns=2;s=/Plc/DB190.DBD72:REAL"  # Replace with your node ID
    node = client.get_node(node_id)
    value = node.get_value()
    print(f"Value of node {node_id}: {value}")

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Disconnect from the server
    client.disconnect()
    logging.info("Disconnected from OPC UA server")
