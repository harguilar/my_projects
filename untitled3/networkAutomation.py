import paramiko
import time

def main():
    #Define The Switches IPs
    IPS = ("192.168.15.222","192.168.15.221")
    # Create the Paramiko Client
    sshClient = paramiko.SSHClient()
    #Accept SSH Keys
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #Set the Index
    idx = 0
    #Connect To the Devices

    while( idx < len(IPS)):
        #Connect To the Devices
        sshClient.connect(hostname=IPS[idx],port=22,username="hnhanga",password="Barreto18!")
        #Access The shell of the remote Device
        configure = sshClient.invoke_shell()
        # COnfigure The Switch
        configureSwitch(configure)
        #Add 1 to configure the next Device
        idx+=1

    sshClient.close()
def configureSwitch(configurations):
    # Check if The Connection is Active
    try:
        if configurations.active:
            #Configure the Devices
            configurations.send('config t \n')
            #Wait 1 Sec to Run the next line
            time.sleep(1.0)
            #Configure the Devices
            configurations.send('int loop1 \n')
            time.sleep(1.0)
            #Configure the Devices
            configurations.send('ip add 1.1.1.1 255.255.255.255 \n')
            time.sleep(1.0)
            configurations.send('end')
            #Receive the Configuration into the Screen
            output = configurations.recv(4096)
            # COnvert Bytes into Strings
            print (output.decode())
        else:
            print("Devices Could not be configured")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()









