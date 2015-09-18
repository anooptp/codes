import os
import pyPdf
from pyPdf import PdfFileReader

def getPDFContent(path):
    content = ""
    p = file(path, "rb")
    pdf = pyPdf.PdfFileReader(p)
    num_pages = pdf.getNumPages()
    print "num_pages =",num_pages
    for i in range(0, num_pages):
        content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())     
    return content 


script_path = os.getcwd()
input_path = script_path+'/input'
os.chdir(input_path)
print os.getcwd()
##file_name = open('A0010047.PDF','rb')
##reader = PdfFileReader(file_name)
##contents = reader.getPage(1).extractText().split('\n')
##print contents
##file_name.close()

content = getPDFContent('A0010047.PDF')
print content

os.chdir(script_path)
print os.getcwd()
