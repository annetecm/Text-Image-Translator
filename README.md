# Text-Image-Translator

**Text-Image-Translator** es una herramienta en Python que permite extraer texto de imágenes utilizando OCR para detectar automáticamente el idioma del texto y traducirlo al idioma deseado. Es ideal para traducir contenido de libros, documentos escaneados, carteles y más.

---

## Características

-  **Detección automática de idioma**: Utiliza `langdetect` para identificar el idioma del texto extraído.
-  **Traducción multilingüe**: Traduce el texto a más de 100 idiomas utilizando `deep-translator`.
-  **Mejora de imagen**: Aplica el filtro CLAHE para mejorar la claridad del texto en imágenes con poca iluminación o bajo contraste.
-  **OCR eficiente**: Utiliza `EasyOCR` para una extracción precisa del texto en múltiples idiomas.

---

## Requisitos

Asegúrate de tener instalado Python 3.6 o superior. Luego, instala las siguientes dependencias:

```bash
pip install easyocr langdetect deep-translator opencv-python
