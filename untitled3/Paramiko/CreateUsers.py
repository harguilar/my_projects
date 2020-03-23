import paramiko
import time
import getpass

def main():
    #Create a Paramiko
    ssh = paramiko.SSHClient()

    #Accept the Linux Keys
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    user = input("Please Enter the Username to be Authentication within the system \n")
    # Connect To HOst
    ssh.connect(hostname="192.168.10.21", port=22, username=user, password = getpass.getpass())
    #Invoke Shell
    configure = ssh.invoke_shell()

    try:
        if configure.active:
            option = int (input("Would you like to create a user \n 1. \\t Create \n 2. \\t Do Not Create"))
            if option == 1:
                newUser = input("Enter the New username: \n")
                configure.send(f'sudo useradd -m -d /home/{newUser} -s /bin/bash {newUser}\n')
                time.sleep(1.0)
                configure.send('msfadmin\n')
                time.sleep(1.0)
                configure.send('cat /etc/passwd \n')
                time.sleep(1.0)
                output = configure.recv(40049)
                print (output.decode())
            else:
                print ("Users cannot be created")
        else:
            print("The Connect was not unable to be made:")
    except Exception as e:
        print(e)

main()



