import time 
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = uc.Chrome()
driver.get("https://www.dpmgudi.com.br/cadastro/juizado_especial_internet/cadastro_publico.php")
p = driver.find_elements_by_tag_name("p")
        
def enviar():
    global driver
    restam20 = driver.find_elements_by_tag_name("h5")[0].text.split('\n')[0]
    acao = driver.find_elements_by_id("acao")[0]
    acao = Select(acao)
    acao.select_by_visible_text('Indenizatória por dano moral ou material')
    time.sleep(0.5)
    driver.find_elements_by_tag_name("input")[0].send_keys("Mylena Evangelista Santos")
    time.sleep(0.5)
    driver.find_elements_by_tag_name("input")[1].send_keys("70029366623")
    time.sleep(0.5)
    driver.find_elements_by_tag_name("input")[2].send_keys("(34)99670-7291")
    time.sleep(0.5)
    click = 0
    for i in p:
        if(len(i.find_elements_by_tag_name("input")) > 0 and i.find_elements_by_tag_name("input")[0].get_attribute("value") == "Cadastrar"):
            click = i.find_elements_by_tag_name("input")[0]
            break
    driver.find_elements_by_tag_name("input")[5].click()
    time.sleep(0.5)
