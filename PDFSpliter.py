from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_file = open(r"C:\Users\yons\PycharmProjects\PriceTracker\New中国联通关于召开2019年第二次临时股东大会的通知.pdf",
                "rb")

#
# pdf_file = open(r"C:\Users\yons\PycharmProjects\PriceTracker\Test.pdf",
#                 "rb")

pdf_reader = PdfFileReader(pdf_file)
pdf_writer = PdfFileWriter()

pdf_writer.addPage(pdf_reader.getPage(1))
pdf_writer.addPage(pdf_reader.getPage(4))
pdf_writer.addPage(pdf_reader.getPage(5))

split_file = open(r"C:\Users\yons\PycharmProjects\PriceTracker\参加股东大会需要填写的pdf.pdf",
                  "wb")


# split_file = open(r"C:\Users\yons\PycharmProjects\PriceTracker\SplitExportTest.pdf",
#                   "wb")

pdf_writer.write(split_file)

split_file.close()
pdf_file.close()
