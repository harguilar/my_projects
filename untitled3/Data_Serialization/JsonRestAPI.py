import json
import csv
import requests

def main():
    try:
        # Get the info from The site
        response = requests.get('https://jsonplaceholder.typicode.com/users')

        # Check the site to if open
        if response.status_code == 200:
            # Create a Python Object from Json Encoded String
            # User list of Dictionaries
            users = json.loads(response.text)
            print (users)
            with open("users.csv", 'w') as f:
                writer = csv.writer(f)
                #Write the Header to the file
                writer.writerow(("\tName\t\t\t", "City\t\t\t", "GPS\t\t\t", "Company\t\t\t"))
                #Iterate over a list of users
                for user in users:
                    #Getting the Data from teh Dictionary
                    name = user['name']
                    city = user['address']['city']
                    lat  = user['address']['geo']['lat']
                    lng = user['address']['geo']['lng']
                    geo = f'({lat}, {lng})'
                    company_name = user['company']['name']
                    # write to a CSV file
                    csv_data = (name,city, geo, company_name)
                    writer.writerow(csv_data)
        else:
            print("Could not Connecto to The Server \n")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()