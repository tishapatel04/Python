"""
AIM: Generate PDF file of your 3rd Semester Mark-sheet
"""
import aspose.words as aw
# load the PDF file
doc = aw.Document("20CE106_Marksheet.pdf")
# convert PDF to Word DOCX format
doc.save("20CE106_New.docx")
# Load word document
doc = aw.Document("20CE106_New.docx")
# Save as PDF
doc.save("20CE106_New2.pdf")
