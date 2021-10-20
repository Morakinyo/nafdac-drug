from pdf2docx import Converter, parse

pdf_file = 'glossary-of-terms-FDA.pdf'
word_file = 'glossary-of-terms-NAFDAC.docx'

# Converter Method
cv = Converter(pdf_file)
cv.convert(word_file, start=0, end=None)
cv.close()

# Parse Method
#parse(pdf_file, word_file, start=0, end=None)