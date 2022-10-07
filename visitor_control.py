from selenium import webdriver
import numpy as np
import time

path_webdriver='/home/felipepedrosa/projetos/teste_bayesiana/chromedriver'
driver = webdriver.Chrome(path_webdriver)


driver.get('http://127.0.0.1:5000/')

clicks = 10000
for click in range(clicks):
    if np.random.random() < 0.3:
        driver.find_element('name' , 'yescheckbox').click()
        driver.find_element('id' , 'yesbtn').click()
        time.sleep(2)
    else:
        driver.find_element('name' , 'nocheckbox').click()
        driver.find_element('id' , 'nobtn').click()      
        time.sleep(2)
