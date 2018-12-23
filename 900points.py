from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

browser = webdriver.Firefox()
browser.get("https://hack.ainfosec.com/")
time.sleep(4)

help_button = browser.find_element_by_css_selector('[ref="helpButton"]')
help_button.click()
time.sleep(1)

account_id = browser.find_element_by_css_selector('[ref="accountID"]')
account_id.send_keys("your session id here")

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

frequency = [101, 116, 97, 111, 105, 110, 115, 104, 114, 100, 108, 99, 117, 109, 119, 102, 103, 121, 112, 98, 118, 107,
             106, 120, 113, 122]


def largest_frequency(test_list):
    maxval = 0
    res = test_list[0]
    for i in test_list:
        if i == " ":
            continue
        freq = test_list.count(i)
        if freq > maxval:
            maxval = freq
            res = i

    return res


challenge_content = browser.find_elements_by_css_selector("[ref=challengeContent]")
message_content = challenge_content[3].find_elements_by_tag_name("p")
message = message_content[2].text
message_chars = list(message)

while True:
    rot_list = []
    most_frequent_char = largest_frequency(message_chars)

    for i in frequency:
        temp_message_chars = message_chars.copy()
        difference = ord(most_frequent_char) - i
        for j in range(len(message_chars)):
            if temp_message_chars[j].isalpha():
                temp_message_chars[j] = chr(((ord(temp_message_chars[j]) - difference - 97) % 26) + 97)

        rot_list.append(''.join(temp_message_chars))

    for i in range(len(rot_list)):
        print(i, "---", rot_list[i])
    i = input("-->")
    if i.isalpha():
        continue
    i = int(i)
    pin_input.clear()
    pin_input.send_keys(rot_list[i])
    submit.click()

    while True:
        try:
            old_message_chars = message_chars
            challenge_content = browser.find_elements_by_css_selector("[ref=challengeContent]")
            message_content = challenge_content[3].find_elements_by_tag_name("p")
            message = message_content[2].text
            message_chars = list(message)
            if not message_chars == old_message_chars:
                break
        except:
            continue
