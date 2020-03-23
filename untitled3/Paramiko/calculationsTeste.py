import paramiko
import time
import getpass
#password = getpass.getpass()
def sum (a,b):
    a = 7
    b = 8
    result = a + b
    return result

def mult(result):
    result1 = result + 9
    print("This is the Final: " + str(result1))
def main():
    #Create a Paramiko
    ssh = paramiko.SSHClient()

    #Accept the Linux Keys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect To HOst
    ssh.connect(hostname="192.168.10.21", port=22, username="msfadmin", password='msfadmin')
    #Invoke Shell
    configure = ssh.invoke_shell()
    try:
        if configure.active:
            configure.send('sudo useradd -m -d /home/harguilar -s /bin/bash harguilar\n')
            time.sleep(1.0)
            configure.send('msfadmin\n')
            time.sleep(1.0)
            configure.send('cat /etc/passwd \n')
            time.sleep(1.0)

            output = configure.recv(40049)
            print (output.decode())
        else:
            print("The Connect was not unable to be made:")
    except Exception as e:
        print(e)

main()



