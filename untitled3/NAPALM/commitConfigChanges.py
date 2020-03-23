from napalm import get_network_driver
import json
import getpass
def main():
    try:
        driver = get_network_driver('ios')
        optional_args = {'secret':'cisco'}
        username = input("Please Enter Your Username: \n" )
        ios = driver('192.168.15.221',username, getpass.getpass(),optional_args = optional_args)
        ios.open()
        # Get info about arp table.
        ios.load_replace_candidate(filename="config.txt")
        #diff = ios.commit_config()
        # Compares configuration between the file and the on in the router.
        diff = ios.compare_config()
        #Roll back to the last configuration within the router
        #ios.rollback()
        if len(diff):
            print(diff)
            print ("commit changes \n")
            ios.commit_config()
            print("Done ..")
        else:
            print ("No changes to Required")
            ios.discard_config()
    except Exception as e :
        print (e)
    finally:
        ios.close()

if __name__ == '__main__':
    main()