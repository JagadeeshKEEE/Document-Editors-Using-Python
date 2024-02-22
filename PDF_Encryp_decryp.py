from PyPDF2 import PdfReader,PdfWriter
import os

class Encryptor_Decrypter:
    def __init__(self,FileName):
        self.Filename=FileName
    def Encryptor(self):
        reader = PdfReader(self.Filename)
        writer = PdfWriter()

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)
        Encrypted_password=input("Enter the Password to Encrypt :")
        Encrypted_pdf_name=input("Enter the Encrypted file name to be saved :")
        writer.encrypt(Encrypted_password)

        with open(Encrypted_pdf_name, "wb") as f:
            writer.write(f)

    def Decryptor(self):
        reader = PdfReader(self.Filename)
        writer = PdfWriter()
        Decrypt_password=input("Enter the Password to Decrypt his file :")
        if reader.is_encrypted:
            reader.decrypt(Decrypt_password)
        for page in reader.pages:
            writer.add_page(page)
        FileName_TO_save=input("Enter the File Name to br saved :")
        with open(FileName_TO_save, "wb") as f:
            writer.write(f)
choice=''
while True:
    try:
        choice=int(input("1)PDF Encryptor \n 2)PDF Decryptor \n Enter your choice :"))
        if choice != 1 and choice != 2:
            print("<Enter Either 1 or 2 for Encryption or Decryption>")
        else:
            break
    except ValueError:
        print("<Enter Either 1 or 2>")
    except TypeError:
        print("<Pls Enter the choice correctly>")

file_name=''
while True:
    try:
        file_name = input("Enter the File Name: ")
        if os.path.exists(file_name):
            print(f"The file '{file_name}' exists.")
            break
        else:
            print(f"The file '{file_name}' does not exist. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

obj1=Encryptor_Decrypter(file_name)
if choice==1:
    obj1.Encryptor()
if choice==2:
    obj1.Decryptor()
