import easyocr

# Se ingresa ingles como idioma predeterminado
reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext("libroIngles.jpg")

# Unir todo el texto en una sola cadena
paragraph = " ".join([text for _, text, _ in results])

# Imprimir como un solo párrafo
print("Texto detectado:\n")
print(paragraph)




