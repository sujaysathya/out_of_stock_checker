from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from twilio.rest import Client
#client = Client("AC619e99f5734354f0ec4cdf4d9e9e473a", "e932bfc09beaa95a6dae81d54dd8ac90")
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.amazon.in/dp/B08CFSS789/ref=cm_sw_r_wa_apa_i_.9MsFbJ5QHK36")
print(driver.title)
el = driver.find_element_by_tag_name('body')
str1=el.text 
if(str1.find("Currently unavailable.")!=-1):
    print("its still not available my guy")
else: 
    #client.messages.create(to="+919789813179", 
                       #from_="+17733668813", 
                       #body="its available")      
  
driver.close()


