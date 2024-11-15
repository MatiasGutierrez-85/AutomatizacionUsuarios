from lib2to3.pgen2 import driver
import time
from selenium import webdriver

def crearCuenta():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/register")
    time.sleep(3)
    driver.find_element_by_id("input-rut").send_keys("16713585-4")
    time.sleep(1)
    driver.find_element_by_id("input-telephone").send_keys("987057173")
    time.sleep(1)
    driver.find_element_by_id("input-firstname").send_keys("Matias")
    time.sleep(1)
    driver.find_element_by_id("input-lastname").send_keys("Gutierrez")
    time.sleep(1)
    driver.find_element_by_id("input-email").send_keys("baron70552@eoscast.com")
    time.sleep(1)
    driver.find_element_by_name("email_confirm").send_keys("baron70552@eoscast.com")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("input-confirm").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

def iniciarSesion():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/login")
    time.sleep(3)
    driver.find_element_by_id("input-rut").send_keys("16713585-4")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(4)
    driver.find_element_by_id("input-rut").send_keys("16713585-4")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

def restablecerPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/forgotten")
    time.sleep(3)
    driver.find_element_by_id("input-email").send_keys("baron70552@eoscast.com")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

def restablecerPass2():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/reset&code=Dar7s2bfSNjGCHNtPwlokvtUo4VkWle3BUJLVPU0")
    time.sleep(3)
    driver.find_element_by_id("input-password").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("input-confirm").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)

def modificarPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://tienda.pc-express.cl/index.php?route=account/login")
    time.sleep(4)
    driver.find_element_by_id("input-rut").send_keys("16713585-4")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(4)
    driver.find_element_by_id("input-rut").send_keys("16713585-4")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)
    driver.get("https://tienda.pc-express.cl/index.php?route=account/password")
    time.sleep(1)
    driver.find_element_by_id("input-password").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("input-confirm").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_css_selector("input[type=\"submit\" i]").click()
    time.sleep(5)

crearCuenta()
# iniciarSesion()
# restablecerPass()
# restablecerPass2()
# modificarPass()
