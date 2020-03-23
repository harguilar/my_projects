import paramiko
import time
#from scp import SCPClient
from scp import SCPClient

import getpass

def createSSHClient (server, port, user, passwd):
    #create a paramiko Client
    client = paramiko.SSHClient()
    time.sleep(1.0)
    #Accept the Keys
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #Conenct to remote host
    client.connect(server,port,user,passwd)

    return client
def main ():
    ssh = createSSHClient("192.168.10.21",22,'msfadmin', 'msfadmin')

    scp = SCPClient(ssh.get_transport())

    # Copy Files on Local Machine to remote Machine
    scp.put('myParamiko.py','/home/msfadmin/harguilar.py')

    #Close the connection
    scp.close()

if __name__ =="__main__":
    main()

    



