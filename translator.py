import easyocr

# OCR
reader = easyocr.Reader(['es'], gpu=False)
results = reader.readtext("libroIngles.jpg")

# Unir todo el texto en una sola cadena
paragraph = " ".join([text for _, text, _ in results])

# Imprimir como un solo párrafo
print("Texto detectado:\n")
print(paragraph)


