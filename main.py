import csv
import os

from pdf_forms import Form

def main():
    with open('tenants.csv',mode='r') as file:
        csvFile = csv.reader(file)
        headers = next(csvFile)
        for lines in csvFile:
            tenant_1 = lines[0]
            tenant_2 = lines[1]
            rent = int(lines[2])
            unit_num = lines[3]
            address = lines[4]
            city = lines[5]
            state = lines[6]
            zip = lines[7]
            start = lines[8]
            phone1 = lines[9]
            phone2 = lines[10]
            form = Form(tenant_1,tenant_2,rent,unit_num,address,city,state,zip,
                        start,phone1,phone2)
            form.all()

if __name__ == "__main__":
    main()