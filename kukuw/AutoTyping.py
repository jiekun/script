import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://dazi.kukuw.com/'

driver = webdriver.Chrome()
driver.get(url)
time.sleep(30)
for i in range(15):
    try:
        driver.find_element_by_xpath('//*[@id="time"]').send_keys(Keys.BACKSPACE)
        if i < 4:
            t = 2
        else:
            t = 2
        driver.find_element_by_xpath('//*[@id="time"]').send_keys(str(t))
        driver.find_element_by_xpath('//*[@id="form"]/ul[6]/li[2]/input').click()

        xpath_template = '//*[@id="{}"]/div/span'
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="i_0"]/input[2]').click()

        input_template = '//*[@id="{}"]/input[2]'
        status_template = '//*[@id="{}"]'
        for i in range(34):
            id_str = 'i_{}'.format(str(i))
            xpath = input_template.format(id_str)
            driver.find_element_by_xpath(xpath).click()
            time.sleep(0.05)
            input_content_xpath = xpath_template.format(id_str)
            input_conetnt = driver.find_element_by_xpath(input_content_xpath).text
            for each in input_conetnt.strip():
                if random.random() < 0.10:
                    driver.find_element_by_xpath(xpath).send_keys(str(random.randint(0, 9)))
                    driver.find_element_by_xpath(xpath).send_keys(Keys.BACKSPACE)
                driver.find_element_by_xpath(xpath).send_keys(each)
                time.sleep(random.uniform(0.003, 0.028))
            status = status_template.format(id_str)
            status_value = driver.find_element_by_xpath(status).get_attribute("class")
            if status_value == "typing typing_on":
                driver.find_element_by_xpath(xpath).send_keys(Keys.SPACE)
    except KeyboardInterrupt:
        quit()
    except Exception:
        time.sleep(30)

