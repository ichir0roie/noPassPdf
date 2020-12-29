import os
import PyPDF2

import glob

# todo learn gitIgnore

filePaths = glob.glob("Data/*.pdf")


with open("Password", mode="r", encoding="utf-8")as f:
    password = f.read().replace("\n", "")

for i in filePaths:
    pdf = PyPDF2.PdfFileReader(i)
    pdf.decrypt(password)
    dst_pdf = PyPDF2.PdfFileWriter()
    dst_pdf.cloneReaderDocumentRoot(pdf)

    with open(i, mode="wb")as f:
        dst_pdf.write(f)
