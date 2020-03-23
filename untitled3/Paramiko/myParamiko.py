import paramiko
import time

# Create The Client to Connect
sshClient = paramiko.SSHClient()

#Connection Function
def connect(server_ip, server_port, user, passwd):

    #Accept SSH Keys
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Connect to Remote Device
    sshClient.connect(
        hostname=server_ip,
        port=server_port,
        username=user,
        password=passwd
    )
    return sshClient
#Get The Shell

def get_shell(sshClient):
    shell = sshClient.invoke_shell()
    return shell

def cmd(shell):
    try:
        #Check if the connection if Active
        if shell.active:
            shell.send("config t \n")
            time.sleep(1.0)
            shell.send("int loop1 \n")
            time.sleep(1.0)
            shell.send('ip add 1.1.1.1 255.255.255.255 \n')
        else:
            print ("Connection Could not Be Active")
    except Exception as e:
        print (e)


def main():
    IPS = ["192.168.15.222","192.168.15.221", "192.168.15.223" ]
    idx = 0
    while(idx < len(IPS)):
        connect(IPS[idx],server_port=22,username=")))))))))))",passwd="((((((")
