
# from selenium import webdriver
# # Starting a Selenium "webdriver" to pop up a real Firefox browser window

# browser = webdriver.Firefox()
# # browser = webdriver.ChromeOptions()
# # browser.binary_location = "C:\\Program Files\\Opera\\launcher.exe"

# # option = webdriver.Opera(executable_path='operadriver.exe', opera_options=browser)
# # # • Using it to open up a web page which we’re expecting to be served from the local PC

# browser.get('http://localhost:8000')
# # • Checking (making a test assertion) that the page has the word "Django" in its title



# assert 'Django' in browser.title


from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
