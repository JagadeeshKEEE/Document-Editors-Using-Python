from PyPDF2 import PdfReader
def text_reader(pdf_name,Starting_page,Ending_page):
    try:
        reader = PdfReader(pdf_name)
        number_of_pages = len(reader.pages)
        for i in range(Starting_page, Ending_page+1):
            page = reader.pages[i]
            text = page.extract_text()
            print(text, end=" ")
    except FileNotFoundError:
        print("pls enter a file Name: ")
        return False
    except ValueError as e:
        print("The Entered must be a Integer: ")
        return False
while True:
    pdf_name=input("Enter the PDF Name: ")
    try:
        Starting_page=int(input("Enter Starting page: "))
        Ending_page=int(input("Enter Ending page: "))
    except ValueError:
        print("The Entered must be a Integer: ")
        continue
    text_reader(pdf_name,Starting_page,Ending_page)
