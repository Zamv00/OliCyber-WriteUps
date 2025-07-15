#MATH TEST -> addizione tra numeri
#ART TEST -> premi il pulsante di colore "c"
#GRAMMAR TEST -> quante "lettera" ci sono nella parola "parola"
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)



driver.get("http://infinite.challs.olicyber.it")
time.sleep(5)
i = 0

while True:
    test_type = driver.title
    print(f"Pagina numero: {i}, test type: {test_type}")

    if "MATH" in test_type:
        question = driver.find_element(By.TAG_NAME, "p").text
        numbers = list(map(int, re.findall(r'\d+', question)))
        print("Numeri da sommare: ", numbers)
        result = sum(numbers)
        print("Risultato: ", result)

        input_box = driver.find_element(By.ID, "sum")
        input_box.send_keys(str(result))
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    elif "ART" in test_type:
        question = driver.find_element(By.TAG_NAME, "p").text
        color = re.findall(r'colore (\w+)', question, re.IGNORECASE)[0].capitalize()
        print("Colore: ", color)
        button = driver.find_element(By.ID, color)
        button.click()


    elif "GRAMMAR" in test_type:
        question = driver.find_element(By.TAG_NAME, "p").text
        letter, word = re.findall(r'"(.*?)"', question)
        count = word.count(letter)
        print(f"Lettera: {letter}, Parola: {word}, Numero di lettere nella parola: {count}")

        input_box = driver.find_element(By.ID, "letter")
        input_box.send_keys(str(count))
        driver.find_element(By.XPATH, '//input[@type="submit"]').click()

    elif "YOU WIN" in test_type:
        flag = driver.find_element(By.TAG_NAME, "p").text
        print(flag)
        break

    i += 1    
    print("Prossima pagina...")

driver.quit()
#flag{y0u_mu57_b3_4_r34lly_f457_cl1ck3r!}
