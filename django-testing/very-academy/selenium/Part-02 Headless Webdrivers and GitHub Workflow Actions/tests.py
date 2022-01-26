from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class Hosttest(LiveServerTestCase):
  	
		def testhomepage(self):

				options = webdriver.FirefoxOptions()
				options.headless = True
				driver = webdriver.Firefox(
            								executable_path="./geckodriver")
				#try driver = webdriver.chrome('./chromedriver) with the driver in the project folder if you can't set to path.

				# driver = webdriver.Firefox(options=options)

				driver.get(self.live_server_url)
				# try driver.get(self.live_server_url) if driver.get('http://127.0.0.1:8000/') does not work
				
				assert "Hello, world!" in driver.title


class LoginFormTest(LiveServerTestCase):

		def testform(self):
				options = Options()
				options.headless = True
				driver = webdriver.Chrome(chrome_options=options)

				driver.get(('%s%s' % (self.live_server_url, '/accounts/login/')))

				user_name = driver.find_element_by_name('username')
				user_password = driver.find_element_by_name('password')

				submit = driver.find_element_by_id('submit')

				user_name.send_keys('admin')
				user_password.send_keys('admin')

				submit.send_keys(Keys.RETURN)

				assert 'admin' in driver.page_source
