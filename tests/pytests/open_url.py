#https://www.youtube.com/watch?v=rJPuhIS7EwQ

import time
# Changed the method of opening the browser.
# Selenium allows for the page to be refreshed.
from selenium import webdriver

# adding ability to change number of repeats
count = int(input("Number of times to be repeated: "))
# Same as before
url = input("Enter the URL : ")
print("Length of video:")
minutes = int(input("Minutes "))
seconds = int(input("Seconds "))

# Calculating the refreshrate from the user input
refreshrate = minutes * 60 + seconds
# Selecting Safari as the browser
driver = webdriver.Chrome

if url.startswith("https://"):
    driver.get(url)
    time.sleep(3)
else:
    driver.get("https://" , url)

for i in range(count):
    # Sets the page to refresh at the refreshrate.
    time.sleep(refreshrate)
    driver.refresh()