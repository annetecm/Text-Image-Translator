import easyocr
from langdetect import detect

# Se ingresa ingles como idioma predeterminado
reader = easyocr.Reader(["en"], gpu=False)
results = reader.readtext("libroIngles.jpg")

# Unir todo el texto en una sola cadena
paragraph = " ".join([text for _, text, _ in results])

#detects the language the text is in
language = detect(paragraph)

lang = language

if lang = "af":
    lang = "afrikaans"
elif lang = "ar":
    lang = "arabic"
elif lang = "bg":
    lang = "bulgarian"
elif lang = "bn":
    lang = "bengali"
elif lang = "ca":
    lang = "catalan"
elif lang = "cs":
    lang = "checo"
elif lang = "cy":
    lang = "gales"
elif lang = "da":
    lang = "danes"
elif lang = "de":
    lang = "aleman"
elif lang = "el":
    lang = "griego"
elif lang = "en":
    lang = "ingles"
elif lang = "es":
    lang = "espanol"
elif lang = "et":
    lang = "estonio"
elif lang = "fa":
    lang = "persa"
elif lang = "fi":
    lang = "fines"
elif lang = "fr":
    lang = "frances"
elif lang = "gu":
    lang = "gujarati"
elif lang = "he":
    lang = "hebreo"
elif lang = "hi":
    lang = "hindi"
elif lang = "hr":
    lang = "croata"
elif lang = "hu":
    lang = "hungaro"
elif lang = "id":
    lang = "indonesio"
elif lang = "it":
    lang = "italiano"
elif lang = "ja":
    lang = "japones"
elif lang = "kn":
    lang = "canares"
elif lang = "ko":
    lang = "coreano"
elif lang = "lt":
    lang = "lituano"
elif lang = "lv":
    lang = "leton"
elif lang = "mk":
    lang = "macedonio"
elif lang = "ml":
    lang = "malabar"
elif lang = "mr":
    lang = "marati"
elif lang = "ne":
    lang = "nepali"
elif lang = "nl":
    lang = "holandes"
elif lang = "no":
    lang = "noruego"
elif lang = "pa":
    lang = "panyabi"
elif lang = "pl":
    lang = "polaco"
elif lang = "pt":
    lang = "portuges"
elif lang = "ro":
    lang = "rumano"
elif lang = "ru":
    lang = "ruso"
elif lang = "sk":
    lang = "eslovaco"
elif lang = "sl":
    lang = "esloveno"
elif lang = "so":
    lang = "somali"
elif lang = "sq":
    lang = "albanes"
elif lang = "sv":
    lang = "sueco"
elif lang = "sw":
    lang = "suajili"
elif lang = "ta":
    lang = "tamil"
elif lang = "te":
    lang = "telugu"
elif lang = "th":
    lang = "tai"
elif lang = "tl":
    lang = "tagalo"
elif lang = "tr":
    lang = "turco"
elif lang = "uk":
    lang = "ucraniano"
elif lang = "ur":
    lang = "urdu"
elif lang = "vi":
    lang = "vietnamita"
elif lang = "zh":
    lang = "chino"
elif lang = "zh-cn":
    lang = "chino"
elif lang = "cn":
    lang = "chino"
elif lang = "tw":
    lang = "twi"
elif lang = "zh-tw":
    lang = "twi"
    
print(lang,":\n")
print(paragraph)




