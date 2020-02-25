from PyPDF2 import PdfFileReader
def ocr_core(filename):
    pdf = PdfFileReader(filename)


#with open("C:\\Users\\Shubham\\Desktop\\image processing\\topcoder_sample_compliance (1).pdf", 'rb') as file:
    #pdf = PdfFileReader(file)
    page = pdf.getPage(12)
    text=page.extractText()
    print(text)
    #retrun text
    #print(page.extractText())
import os.path
path = os.path.abspath(os.path.dirname(__file__))
print(ocr_core(os.path.join("C:\\Users\\Shubham\\Desktop\\image processing\\topcoder_sample_compliance (1).pdf")))
