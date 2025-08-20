from selenium import webdriver
from selenium.webdriver.common.by import By
import pytesseract
from PIL import Image
import requests
from io import BytesIO
import time

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.get("http://captcha.challs.olicyber.it/")
time.sleep(5)

while True:
    # trova l'immagine
    img = driver.find_element(By.TAG_NAME, "img")
    src = img.get_attribute("src")

    # scarica l'immagine
    response = requests.get(src)
    image = Image.open(BytesIO(response.content))

    # OCR con pytesseract
    numero = pytesseract.image_to_string(image, config='--psm 7 digits')

    print("Numero letto:", numero)

    # inserisci il numero nel form
    form = driver.find_element(By.NAME, "risposta")
    form.send_keys(str(numero))
    driver.find_element(By.ID, "next").click()

driver.quit()

#flag{https://xkcd.com/233/?vjc1GpKF}
