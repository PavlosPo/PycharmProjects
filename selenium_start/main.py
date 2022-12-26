from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_driver_path = "/Users/pavlospoulos/Development/chromedriver"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.python.org")


# price = driver.find_element(by="id", value="price")
# print(price.text)

# search_bar = driver.find_element(by='name', value="field-keywords")
# print(search_bar.get_attribute(name="class"))


# logo = driver.find_element(by="id", value="nav-logo-sprites")
# print(logo.size)

# link = driver.find_element(by="css", value=".a-box-inner a-size-medium")
# print(link)


# link = driver.find_element(by="xpath", value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(link.text)

results = {}
menu = driver.find_element(by="xpath", value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
for index, item in enumerate(menu.find_elements(by='tag name', value="li")):
    time_element = item.find_element(by="tag name", value="time").get_attribute(name="datetime")[:10]
    name_element = item.find_element(by="tag name", value="a").text
    results[index] = {'time': time_element,
                      'name': name_element}

print(results)
# driver.close()
driver.quit()
