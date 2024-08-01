import os
from pypdf import PdfReader

def test_pdf():
  pdf_esperado = get_datos_pdf_esperado()
  pdf_actual = get_pdf_content('prueba.pdf')
  print(pdf_esperado)
  print(pdf_actual)
  assert pdf_esperado == pdf_actual

def get_datos_pdf_esperado():
	pdf_content = "Número de transacción: {} - Fecha de la operación: {} "
	datos = ["123", "1/1/2000"]
	return pdf_content.format(*datos)

def get_pdf_content(pdf_filename):
  text = ""
  if os.path.exists(pdf_filename):
      reader = PdfReader(pdf_filename)
      page = reader.pages[0]
      text = page.extract_text()
  return text

test_pdf()
