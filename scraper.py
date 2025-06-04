from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options = options)
driver.get("https://medicinali.aifa.gov.it/it/#/it/risultati?query=044155024")

wait = WebDriverWait(driver, 0.1)


accept = wait.until(EC.element_to_be_clickable((By.ID, "disclaimercheck")))
accept.click()

button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-outline-secondary")))
button.click()

time.sleep(0.1)

element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "custom-card-result")))
element.click()

codice_atc = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "text-black.small.ng-star-inserted")))
for i in range(len(codice_atc)):
    if '-' in codice_atc[i].text:
        print(codice_atc[i].text)

driver.quit()