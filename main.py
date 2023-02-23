from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")

invoice_list = [[2, "pen", 0.5, 1]]
doc.render({"name": "Patrick", "invoice_list": invoice_list})
doc.save("new_invoice.docx")
