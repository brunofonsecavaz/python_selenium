#codigos padrao para automaçao web selenium--------------------------------
import time # para definir quanto tempo a pagina continuara aberta
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install()) #verifica a att atual do chrome e faz a instalaçao da versao do chromeDriver correspondente
navegador = webdriver.Chrome(service=servico)
#--------------------------------------------------------------------------

# busca o site informado para automatizaçao
navegador.get("https://dlp.hashtagtreinamentos.com/python/minicurso/minicurso-automacao/inscricao?curso=python&origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M&utm_campaign=programacao&utm_content=python%2Fminicurso%2Fminicurso-automacao%2Finscricao&conversion=lespy-jun-25")

# seleciona os elemento na pagina, que deseja automatizar usando o devtools (copia o xpath da pagina )
navegador.find_element('xpath', '//*[@id="firstname"]').send_keys('Bruno Fonseca')
navegador.find_element('xpath', '//*[@id="email"]').send_keys('bruno@email.comm')
navegador.find_element('xpath', '//*[@id="phone"]').send_keys('34991400978')

# clica no botao do navegador 
navegador.find_element('xpath', '//*[@id="_form_1925_submit"]').click()
                

time.sleep(20000) #espera o tempo determinado e depois fecha automaticamente.
navegador.quit()
