from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"

ruta_imagen = "img.png"
imagen_abierta = Image.open(ruta_imagen)

texto = pytesseract.image_to_string(imagen_abierta)
print(texto)



