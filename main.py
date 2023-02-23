from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")


doc.render({"name": "Patrick"})
doc.save("new_invoice.docx")
