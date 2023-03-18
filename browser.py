from selenium.webdriver import Chrome, ChromeOptions
import time

#class BrowserBot():
opts = ChromeOptions()
#isto é bom para o outro bot porque não mostra as cenas
#opts.headless = True
driver = Chrome('chromedriver.exe', chrome_options=opts)
driver.get('https://www.portaldasfinancas.gov.pt/at/html/index.html')
element = driver.find_element_by_xpath('/html/body/div[1]/header/div[1]/div/div[2]/ul/li[2]/a').click()
element = driver.find_element_by_name('username').send_keys("username")
element = driver.find_element_by_name('password').send_keys("password")
#done
time.sleep(1)
driver.quit()
