import time
import json
import processar_eventos
import extract
from processar_eventos import processar_eventos
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import tempfile
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")


# 1. Configurar o navegador (pode usar Chrome ou Firefox)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
try:
    # 2. Acessar página de login
    driver.get('https://www.focomarket.com.br')
    time.sleep(1)

    # 3. Preencher login e senha (AJUSTE PARA O SEU CASO)
    username = driver.find_element(By.NAME, 'LoginForm[username]')
    password = driver.find_element(By.NAME, 'LoginForm[password]')
    username.send_keys('matheus.00000@gmail.com')
    password.send_keys('@Tangerina23')
    password.send_keys(Keys.RETURN)
    time.sleep(1)  # aguarda carregar

    driver.get('https://www.focomarket.com.br/competition/future')
    time.sleep(1)

    # 4. Agora pega o código fonte da página após login
    html = driver.page_source

    with open('pagina_capturada.html', 'w', encoding='utf-8') as f:
        f.write(html)

finally:
    driver.quit()

# Chama o parser do ordenador.py
processar_eventos(html)
