from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import quote
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait



# Config
login_time = 60     # Time for login (in seconds)
new_msg_time = 30   # TTime for a new message (in seconds)
send_msg_time = 20   # Time for sending a message (in seconds)
country_code = 91   # Set your country code
image_path = "D:\\whatsapp_bot\\Metropolis.png"

# Create driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
with open('msg.txt',encoding="UTF-8") as file:
    msg = file.read()
    print(msg)

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}'
        driver.get(link)
        time.sleep(new_msg_time)
        #attachment
        attch_btn=driver.find_element(By.XPATH,"//span[@data-testid='clip']")
        attch_btn.click()
        time.sleep(2)
        img_input=driver.find_element(By.XPATH,"//span[@data-testid='attach-image']")
        img_input.click()
        time.sleep(5)
        pyautogui.typewrite(image_path)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(5)

        actions = ActionChains(driver)
        for line in msg.split('\n'):
            actions.send_keys(line)
            actions.key_down(Keys.SHIFT).send_keys(Keys.ENTER).key_up(Keys.SHIFT)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)

# Quit the driver
driver.quit()