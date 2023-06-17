import paramiko

hostname="HP-PC\SQLEXPRESS"
username="HP-PC\samir"

#create an SSH client instance
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#connect to the server
client.connect (hostname,username="HP-PC\samir")