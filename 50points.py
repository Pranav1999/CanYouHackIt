from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Firefox()
browser.get("https://hack.ainfosec.com/")
time.sleep(2)

help_button = browser.find_element_by_css_selector('[ref="helpButton"]')
help_button.click()
time.sleep(1)

account_id = browser.find_element_by_css_selector('[ref="accountID"]')
account_id.send_keys("session id here")
time.sleep(2)

account_buttons = browser.find_elements_by_class_name('btn-outline-success')
account_buttons[1].click()
time.sleep(2)

flip_containers = browser.find_elements_by_class_name("flip-container")
fifty_point_flip_container = flip_containers[1]
hover = ActionChains(browser).move_to_element(fifty_point_flip_container)
hover.perform()
time.sleep(1)

hack_button = fifty_point_flip_container.find_element_by_css_selector("div button")
hack_button.click()
time.sleep(1)

pin_inputs = browser.find_elements_by_css_selector('[ref="challengeValue"]')
pin_input = pin_inputs[1]

alert_panels = browser.find_elements_by_css_selector('[ref="alertPanel"]')
alert_panel = alert_panels[1]
submit = alert_panel.find_element_by_css_selector('div button')

for i in range(111, 9999):
    pin_input.clear()
    pin_input.send_keys(i)
    submit.click()
