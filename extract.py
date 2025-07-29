import time
from processar_eventos import processar_eventos
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import tempfile

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get('https://www.focomarket.com.br')

    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.NAME, 'LoginForm[username]')))
    password = wait.until(EC.presence_of_element_located((By.NAME, 'LoginForm[password]')))

    username.send_keys('matheus.00000@gmail.com')
    password.send_keys('@Tangerina23')
    password.send_keys(Keys.RETURN)

    time.sleep(2)

    driver.get('https://www.focomarket.com.br/competition/future')
    time.sleep(1)

    html = driver.page_source
    with open('pagina_capturada.html', 'w', encoding='utf-8') as f:
        f.write(html)

finally:
    driver.quit()

processar_eventos(html)
