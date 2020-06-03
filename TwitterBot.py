#pip install selenium
#pip install chromedriver-binary

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")

class TwitterBot:
    def __init__(self,username, password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome("chromedriver_win32/chromedriver.exe")

    def login(self):
        bot=self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email=bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

# ed=TwitterBot('storyofwho','12345')
# ed.login()
