from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from langdetect import detect

browser = webdriver.Firefox()
browser.get("https://hack.ainfosec.com/")
time.sleep(4)

help_button = browser.find_element_by_css_selector('[ref="helpButton"]')
help_button.click()
time.sleep(1)

account_id = browser.find_element_by_css_selector('[ref="accountID"]')
account_id.send_keys("5ce16da5-4f14-41b7-acb7-16e7a82eb18f")

account_buttons = browser.find_elements_by_class_name('btn-outline-success')
account_buttons[1].click()
time.sleep(2)

flip_containers = browser.find_elements_by_class_name("flip-container")
flip_container = flip_containers[3]
hover = ActionChains(browser).move_to_element(flip_container)
hover.perform()
time.sleep(1)

hack_button = flip_container.find_element_by_css_selector("div button")
hack_button.click()
time.sleep(1)

pin_inputs = browser.find_elements_by_css_selector('[ref="challengeValue"]')
pin_input = pin_inputs[3]

alert_panels = browser.find_elements_by_css_selector('[ref="alertPanel"]')
alert_panel = alert_panels[3]
submit = alert_panel.find_element_by_css_selector('div button')

while True:
    for i in range(26):
        challenge_content = browser.find_elements_by_css_selector("[ref=challengeContent]")
        message_content = challenge_content[3].find_elements_by_tag_name("p")
        message = message_content[2].text
        message_chars = list(message)
        for j in range(len(message_chars)):
            if message_chars[j].isalpha():
                message_chars[j] = chr(((ord(message_chars[j]) - 97 - i) % 26) + 97)
        if detect(''.join(message_chars)) == 'en':
            print(''.join(message_chars))
            confirmation = input("-->")
            if not confirmation == 'y':
                continue
            pin_input.clear()
            pin_input.send_keys(''.join(message_chars))
            submit.click()
            time.sleep(1.5)
            break
