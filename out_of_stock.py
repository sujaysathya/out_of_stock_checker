from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from twilio.rest import Client

#client = Client("your_twillio_keys", "your_twillio_id")
driver = webdriver.Chrome('./chromedriver')
# enter items link below
driver.get("https://www.amazon.in/b?ie=UTF8&node=21725163031")

print(driver.title)
el = driver.find_element_by_tag_name('body')
str = el.text 
if(str.find("Currently unavailable.") != -1):
    print("It's still not available my guy")
else: 
    #client.messages.create(to = "+xxxxxxxxxxxx", from_ = "+xxxxxxxxxxxx", body = "its available")      
    #create a twillio account and use the assigned "from" number
    
driver.close()


