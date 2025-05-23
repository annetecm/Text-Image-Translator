import easyocr

from langdetect import detect
from deep_translator import GoogleTranslator
import cv2 as cv

def detectLang (paragraph):
    # Detectar idioma del texto
    language = detect(paragraph)

    lang_dict = {
        "af": "afrikáans", "ar": "árabe", "bg": "búlgaro", "bn": "bengalí",
        "ca": "catalán", "cs": "checo", "cy": "galés", "da": "danés",
        "de": "alemán", "el": "griego", "en": "inglés", "es": "español",
        "et": "estonio", "fa": "persa", "fi": "finés", "fr": "francés",
        "gu": "guyaratí", "he": "hebreo", "hi": "hindi", "hr": "croata",
        "hu": "húngaro", "id": "indonesio", "it": "italiano", "ja": "japonés",
        "kn": "canarés", "ko": "coreano", "lt": "lituano", "lv": "letón",
        "mk": "macedonio", "ml": "malabar", "mr": "maratí", "ne": "nepalí",
        "nl": "neerlandés", "no": "noruego", "pa": "panyabí", "pl": "polaco",
        "pt": "portugués", "ro": "rumano", "ru": "ruso", "sk": "eslovaco",
        "sl": "esloveno", "so": "somalí", "sq": "albanés", "sv": "sueco",
        "sw": "suajili", "ta": "tamil", "te": "télugu", "th": "tailandés",
        "tl": "tagalo", "tr": "turco", "uk": "ucraniano", "ur": "urdu",
        "vi": "vietnamita", "zh": "chino (simplificado)", "zh-cn": "chino (simplificado)",
        "zh-tw": "chino (tradicional)"
    }

    lang_name = lang_dict.get(language, "desconocido")
    print("\nEl texto está en: ", lang_name)


def imageOption ():
    # Leer imagen
    img = cv.imread("libroEspanol.jpg")

    # Convertir a espacio de color LAB
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    l, a, b = cv.split(lab)

    # Aplicar CLAHE en el canal L (luminosidad)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    # Recombinar los canales y volver a BGR
    limg = cv.merge((cl, a, b))
    img_clahe = cv.cvtColor(limg, cv.COLOR_LAB2BGR)

    # Mostrar imagen mejorada
    cv.imshow("Imagen mejorada con CLAHE", img_clahe)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # OCR para inglés y español por defecto
    reader = easyocr.Reader(["en", "es"], gpu=False)
    results = reader.readtext(img_clahe)

    # Unir texto en un solo párrafo
    paragraph = " ".join([text for _, text, _ in results])
    print("Texto detectado:\n")
    print(paragraph)

    return paragraph

def textOption():
    paragraph = input("Escribe el texto a traducir: ")
    return paragraph


print("Hola! Con este codigo podras traducir un texto al idioma que quieras")
print("Tienes 3 opciones: ")
print("1. Subir un imagen con texto y traducirlo")
print("2. Escribir un texto y traducirlo")
print("3. Salir del programa")
option = input("Por favor, escribe la opcion que deseas (1/2/3): ")

while (option != "1" and option != "2" and option != "3"):
    print("Opcion no valida")
    option = input("Por favor, escribe la opcion que deseas (1/2/3): ")

if (option == "1"):
    paragraph = imageOption()
elif (option == "2"):
    paragraph = textOption()
elif(option == "3"):
    print("Hasta pronto!")
    exit()

detectLang(paragraph)

# Pedir idioma de traducción al usuario
dest_lang_input = input(" \n ¿A qué idioma quieres traducir el texto? (nombre del idioma en INGLÉS): ").strip().lower()

# Traducir el texto
try:
    translated = GoogleTranslator(source='auto', target=dest_lang_input).translate(paragraph)
    print("\nTexto traducido:")
    print(translated)
except Exception as e:
    print(f"\n Error al traducir: {e}")
