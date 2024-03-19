from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()
navegador.get("https://www.findcep.com/")
time.sleep(2)

with open( nome do arquivo para salvar ,"a+" ) as salva:
        with open(nome do arquivo da lista,'r') as ceps:
                for cep in ceps:

                        # CEP 
                        search = navegador.find_element(By.XPATH,"/html/body/div/main/section[1]/div/div/div[2]/form/div/input")
                        search.click()
                        time.sleep(2)
                        search.send_keys(cep)
                        time.sleep(2)
                        Resp = navegador.find_element(By.XPATH,'//*[@id="root"]/main/section[1]/div/div/div[2]/div[2]/span[3]').text
                        print(cep,':',Resp)
                        salva.write(f'{cep},{Resp}')
                        salva.write('\n')
        
                        search.clear()                     
                        time.sleep(3)