from time import sleep
from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(4)

cookie_button = browser.find_element_by_xpath("//button[text()='Allow all cookies']")
cookie_button.click()

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("user")
password_input.send_keys("password")

sleep(4)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(4)

"""save_login = browser.find_element_by_xpath("//button[text()='Save Info']")
save_login.click()"""

sleep(4)

turn_notif = browser.find_element_by_xpath("//button[text()='Not Now']")
turn_notif.click()

sleep(4)

"""for i in range(100):
    browser.find_element_by_xpath("//button[text()='Follow']").click()
    sleep(1)
    """

search_bar = browser.find_element_by_css_selector("input[placeholder='Search']")
search_bar.send_keys("NAME")
"""search_bar = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div").click()"""
search_bar = browser.find_element_by_link_text("/NAME/")

fllw_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()

sleep(4)

ok = True
lista_followers = []

while ok == True:
    if browser.find_element_by_xpath("//button[text()='Follow']"):
        browser.find_element_by_xpath("//button[text()='Follow']").click()

    else:
        ok = False
    sleep(2.5)

browser.close()





