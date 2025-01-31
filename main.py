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
            form = Form(tenant_1,tenant_2,rent,unit_num)
            form.all()

if __name__ == "__main__":
    main()