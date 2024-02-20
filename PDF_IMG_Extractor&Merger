from PyPDF2 import PdfWriter,PdfReader
def PDF_Image_Extractor(FileName,Sp,Ep):
    reader = PdfReader(FileName)
    for i in range(Sp,Ep):
        page = reader.pages[i]
        count = 0

        for image_file_object in page.images:
            with open(str(count) + image_file_object.name, "wb") as fp:
                fp.write(image_file_object.data)
                count += 1
def PDF_Merger(Total_Files,FinalFile):
    merger = PdfWriter()

    for pdf in Total_Files:
        merger.append(pdf)

    merger.write(FinalFile)
    merger.close()
choice=''
while True:
    try:
        choice=int(input("1)PDF_Image_Extractor \n 2)PDF_Merger \n Enter your choice: "))
        if choice != 1 and choice != 2:
            print("<Enter either 1 or 2>")
    except ValueError:
        print("<Enter a Number 1 or 2>")
    finally:
        if choice==1 or choice==2:
            break
File=''
if choice==1:
    File=input("Enter the File Name: ")
    Starting_page=int(input("Enter the Starting Page: "))
    Ending_Page=int(input("Enter the Ending Page: "))
    PDF_Image_Extractor(File,Starting_page,Ending_Page)

if choice==2:
    Files=list(map(str,input("Enter the File Names: ").split(",")))
    FinalFileName=input("Enter the FileName You want for Merged pdf: ")
    PDF_Merger(Files,FinalFileName)





