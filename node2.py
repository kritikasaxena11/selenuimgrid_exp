from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


nodeUrl = "http://192.168.108.125:4444/wd/hub"
driver = webdriver.Remote(command_executor=nodeUrl,desired_capabilities=DesiredCapabilities.CHROME)

driver.get("https://github.com")
print(driver.title)
assert "GitHub" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("dzitkowskik")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.quit()