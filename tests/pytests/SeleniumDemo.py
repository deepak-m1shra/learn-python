from selenium import webdriver

firefox_driver = webdriver.Firefox(executable_path="c://drivers//geckodriver.exe")

firefox_driver.get("http://www.google.com")
search_box = firefox_driver.find_element_by_name("q")
search_box.send_keys("python rocks!")

assert firefox_driver.title.lower().__contains__("google")

file = firefox_driver.get_screenshot_as_base64()

#  demo of other selenium functions

firefox_driver.switch_to.active_element
firefox_driver.switch_to.alert
firefox_driver.switch_to.default_content()

print(firefox_driver.name)
firefox_driver.quit()

