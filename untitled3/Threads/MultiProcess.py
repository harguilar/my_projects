import multiprocessing as mp
import time

def name_and_date(name):
    print(f"Hello Fella {name}, Current time is: {time.time()} \n")
    print("sleeping for 2 Seconds")
    time.sleep(2)
    print("Exiting After Sleeping \n")

if __name__ == "__main__":
    process_list = list()

    for i in range(5):

        # Create a Process
        process = mp.Process(target=name_and_date, args=("Harguilar",))
        #ADD INFORMATION INTO THE PROCESS LIST
        process_list.append(process)


    for p in process_list:
        #START THE PROCESS.
        p.start()
    # JOIN THE PROCESS WITH MAIN PROCESS
    for p in process_list:
        p.join()


    print ("Other Instructions of the main Module .....")
    print ("End of the Script")