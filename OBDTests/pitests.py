import obd

connection = obd.OBD("COM6") # auto-connects to USB or RF port

cmd = obd.commands.RPM # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

