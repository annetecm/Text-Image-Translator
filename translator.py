import easyocr
from langdetect import detect
from deep_translator import GoogleTranslator

# OCR para inglés y español por defecto
reader = easyocr.Reader(["en", "es"], gpu=False)
results = reader.readtext("libroEspanol.jpg")

# Unir texto en un solo párrafo
paragraph = " ".join([text for _, text, _ in results])
print("Texto detectado:\n")
print(paragraph)

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

lang_name = lang_dict.get(language, "unknown")
print("\n El texto está en:", lang_name)

# Pedir idioma destino al usuario
dest_lang_input = input("¿A qué idioma quieres traducir el texto? (ej: inglés, francés, etc.): ").strip().lower()

# Traducir el texto
try:
    translated = GoogleTranslator(source='auto', target=dest_lang_input).translate(paragraph)
    print("\nTexto traducido:")
    print(translated)
except Exception as e:
    print(f"\n Error al traducir: {e}")


