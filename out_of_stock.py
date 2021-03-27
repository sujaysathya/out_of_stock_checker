from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from twilio.rest import Client

#client = Client("your_twillio_keys", "your_twillio_id")
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.amazon.in/dp/B08CFSS789/ref=cm_sw_r_wa_apa_i_.9MsFbJ5QHK36")

print(driver.title)
el = driver.find_element_by_tag_name('body')
str = el.text 
if(str.find("Currently unavailable.") != -1):
    print("It's still not available my guy")
else: 
    #client.messages.create(to = "+xxxxxxxxxxxx", from_ = "+xxxxxxxxxxxx", body = "its available")      
    #create a twillio account and use the assigned "from" number
    
driver.close()


