from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.get('https://www.4devs.com.br/gerador_de_cpf')

wait = WebDriverWait(driver, 10)

pontuation_checkbox = driver.find_element(By.ID, 'pontuacao_nao')
pontuation_checkbox.click()
time.sleep(5)

state_select = driver.find_element(By.ID, 'cpf_estado')
state_select.send_keys('AM')

while True:
    try:
        cpf_bt = driver.find_element(By.ID, 'bt_gerar_cpf')
        cpf_bt.click()

        time.sleep(2)

        cpf_generated = wait.until(EC.visibility_of_element_located((By.ID, 'texto_cpf')))
        cpf_get = cpf_generated.text

        if cpf_get is not None and cpf_get.startswith('7'):
            print(f"CPF ({cpf_get}) começa com 7!! :)")
            break
        else:
            print(f"CPF ({cpf_get}) não começa com 7. :(")
    except Exception as e:
        print(f"Erro ao gerar CPF: {e}")

driver.quit()