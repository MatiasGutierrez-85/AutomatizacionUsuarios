from lib2to3.pgen2 import driver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def crearCuenta():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver") #Ruta de chromedriver

    driver.get("https://elpais.com/subscriptions/#/register?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com") #enlace a la página
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsEmail").send_keys("tamaca4187@dmosoft.com")
    time.sleep(1)
    driver.find_element_by_id("subsPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, "28")
    time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, "e")
    time.sleep(1) 
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, "1999")
    time.sleep(1)
    driver.find_element_by_id("subsConfirmPassword").send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.SPACE)
    time.sleep(3)
    driver.find_element_by_id("subsSignUp").click()
    time.sleep(6)

def iniciarSesion():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://elpais.com/subscriptions/#/sign-in?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com") #enlace a la página
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsEmail").send_keys("tamaca4187@dmosoft.com")
    time.sleep(1)
    driver.find_element_by_id("subsPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("subsSignIn").click()
    time.sleep(6)

def restablecerPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver") 

    driver.get("https://elpais.com/subscriptions/#/forgot-password") #enlace a la página
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsEmail").send_keys("tamaca4187@dmosoft.com")
    time.sleep(1)
    driver.find_element_by_id("subsForgotPassword").click()
    time.sleep(6)

def restablecerPass2():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://elpais.com/subscriptions/#/reset-password?nonce=S3f8LKabbTLqSrhoMSyMX1eKCtfdJ1uKax4yO_4Gmt7W2Fmj")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsPassword").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("confirmPass").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("subsResetPassword").click()
    time.sleep(6)

def modificarPass():
    driver = webdriver.Chrome("D:\Reespaldo\Guias y documentos\Criptografia\chromedriver")

    driver.get("https://elpais.com/subscriptions/#/sign-in?prod=REG&o=CABEP&backURL=https%3A%2F%2Felpais.com")
    time.sleep(3)
    driver.find_element_by_id("didomi-notice-agree-button").click()
    time.sleep(2)
    driver.find_element_by_id("subsEmail").send_keys("tamaca4187@dmosoft.com")
    time.sleep(1)
    driver.find_element_by_id("subsPassword").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("subsSignIn").click()
    time.sleep(6)
    driver.get("https://elpais.com/subscriptions/#/profile?rel=areausuario")
    time.sleep(3)
    driver.find_element_by_id("oldPassword").send_keys("qwertyui")
    time.sleep(1)
    driver.find_element_by_id("newPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("confirmPassword").send_keys("asdfghjk")
    time.sleep(1)
    driver.find_element_by_id("confirmPassword").send_keys(Keys.TAB, Keys.SPACE)
    time.sleep(6)

crearCuenta()
# iniciarSesion()
# restablecerPass()
# restablecerPass2()
# modificarPass()