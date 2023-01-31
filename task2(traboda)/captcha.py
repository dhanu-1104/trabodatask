import pytesseract
from PIL import Image


# Use pytesseract to extract the text from the image
captcha_image = Image.open('captcha.png')
captcha_text = pytesseract.image_to_string(captcha_image)
print(captcha_text)
result = eval(captcha_text)
print(result)
