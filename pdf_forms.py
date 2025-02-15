import csv
import os
from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, IndirectObject

class Form:
    def __init__(self, tenant_1:str, tenant_2:str, rent:int, unit_num:str,
                  address:str, city:str, state:str, zip:int, start:str,phone1:str, phone2:str):
        self.tenant_1 = tenant_1
        self.tenant_2 = tenant_2
        self.rent = rent
        self.unit_num = unit_num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.start = start
        self.phone1 = phone1
        self.phone2 = phone2

    def all(self):
        self.master()
        self.smoke()
        self.bedbug()
        self.flood()
        self.inspection()
        self.mold()
        self.plumbing()
        self.pest()


    def master(self):
        template_pdf = 'templates/LLC_Master_Rental_Agreement_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/LLC_Master_Rental_Agreement.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        writer.update_page_form_field_values(
            writer.pages[0], 
            {"TenantsLessee":self.tenant_1,
            "TenantsLessee_2":self.tenant_2,
            "Unit Number": self.unit_num,
            "Monthly Rental Rate":f"{self.rent:.2f}",
            "t": f"{self.rent:.2f}",
            "Late Charge": f"{round(self.rent*.06,2):.2f}",
            "First months rent of": f"{self.rent:.2f}",
            "total payment of 101":f"{self.rent*2:.2f}",
            "equaling amount": f"{round(self.rent*.06,2):.2f}",
            "payment of": f"{self.rent:.2f}",
            "Unit Address": self.address,
            "ty": self.city,
            "State": self.state,
            "p": self.zip,
            "commence on": self.start
            }
        )
        writer.update_page_form_field_values(
            writer.pages[4],
            {
                "RESIDENTS Text Number": self.phone1,
                "RESIDENTS Text Number_2": self.phone2
            }
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def inspection(self):
        template_pdf = 'templates/131_Move_in_Move_Out_Inspection_Checklist_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/131_Move_in_Move_Out_Inspection_Checklist.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Resident Names": self.tenant_1}
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Resident Names": f"{self.tenant_1}, {self.tenant_2}"}
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"Rental Unit Address": f"{self.address}, #{self.unit_num}, {self.city}, {self.state} {self.zip}"}
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

    def flood(self):
        template_pdf = 'templates/158_-_Flood_Disclosure_Addendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/158_-_Flood_Disclosure_Addendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"between 2": self.tenant_1}
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"between 2": f"{self.tenant_1}, {self.tenant_2}"}
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"unit number": self.unit_num,
             "hereby known as OwnerAgent and": self.start,
             "in the city of": self.address
             }
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def bedbug(self):
        template_pdf = 'templates/148_Bedbug_Addendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/148_Bedbug_Addendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Text3": self.tenant_1}
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"Text3": f"{self.tenant_1}, {self.tenant_2}"}
            )
        writer.update_page_form_field_values(
            writer.pages[0],
            {"Text5": self.unit_num,
             "Text1": self.start,
             "Text4": self.address,
             "Text6": self.city
            }
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def pest(self):
        template_pdf = 'templates/148B_-PEST_CONTROL_ADDENDUM_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/148B_-PEST_CONTROL_ADDENDUM.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"hereby known as OwnerAgent and": self.tenant_1}
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"hereby known as OwnerAgent and": f"{self.tenant_1}, {self.tenant_2}"}
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"unit number": self.unit_num,
             "This agreement is an addendum and part of the rental agreement dated": self.start,
             "hereby known as Residents for the premises located at": self.address,
             "in the city of": self.city
             }
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def mold(self):
        template_pdf = 'templates/149_Mold Addendum To Lease_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/149_Mold Addendum To Lease.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        # fields = reader.get_form_text_fields()
        # print(fields)

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"TENANTS for the premises located at": self.tenant_1}
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"TENANTS for the premises located at": f"{self.tenant_1}, {self.tenant_2}"}
            )

        writer.update_page_form_field_values(
            writer.pages[0],
            {"CA": f"{self.address}, #{self.unit_num}, {self.city}",
             "undefined": self.zip
             }
        )


        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)
    
    def plumbing(self):
        template_pdf = 'templates/PlumbingAddendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/PlumbingAddendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        writer.append(reader)

        writer.update_page_form_field_values(
            writer.pages[0], 
            {"TENANT":self.tenant_1,
            "TENANT and":self.tenant_2,
            "in the city of": self.unit_num,
            "for the premises located at": self.address,
            "CA": self.city,
            "Plumbing": self.start
            }
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)

    def smoke(self):
        template_pdf = 'templates/SmokeFreeAddendum_TEMPLATE.pdf'
        output_pdf = f'tenants/{self.tenant_1}/SmokeFreeAddendum.pdf'

        reader = PdfReader(template_pdf)
        writer = PdfWriter()

        writer.append(reader)

        if self.tenant_2 == '':
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"THIS AGREEMENT made and entered into between": self.tenant_1}
            )
        else:
            writer.update_page_form_field_values(
                writer.pages[0], 
                {"THIS AGREEMENT made and entered into between": f"{self.tenant_1}, {self.tenant_2}"}
            )
        writer.update_page_form_field_values(
            writer.pages[0],
            {"undefined": self.unit_num,
             "Rents the premises from OwnerAgent located at": self.address,
             "Street Address": self.city,
             "Unit if applicable": self.zip
             }
        )

        os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

        with open(output_pdf, "wb") as output_file:
            writer.write(output_file)