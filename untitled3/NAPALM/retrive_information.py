from napalm import get_network_driver
import json
import getpass
def main():
    driver = get_network_driver('ios')
    optional_args = {'secret':'cisco'}
    username = input("Please Enter Your Username: \n" )
    ios = driver('192.168.15.221',username, getpass.getpass(),optional_args = optional_args)
    ios.open()
    # Get info about arp table.
    output = ios.get_arp_table()
    dump = json.dumps(output,sort_keys=True, indent= 4)

    with open("arp.txt", 'w') as f:
        f.write(dump)

    ios.close()
    ios.open()
    # get info about interfaces.
    intOutPut = ios.get_interfaces()
    dump = json.dumps(intOutPut, sort_keys=True, indent=4)

    with open('intStatus.txt', 'w') as f:
        f.write(dump)
    ios.close()
if __name__ == '__main__':
    main()