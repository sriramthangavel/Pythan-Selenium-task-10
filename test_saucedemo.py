from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
import logging

@pytest.mark.sanity                     # marker for regression testing
def test_operations():                  # get title, get url, get content operations
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    webpage_title = driver.title
    webpage_URL = driver.current_url
    logging.info(webpage_title)
    logging.info(webpage_URL)
    webpage_content = driver.find_element(By.TAG_NAME, "body").text
    file = open("Webpage_task_11.txt", "w")
    file.write(webpage_content)
    file.close()
    driver.quit()

@pytest.mark.positive                   # validated login (positive)
@pytest.mark.regression
def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    user_name = driver.find_element(By.XPATH,"//input[@id = 'user-name']")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.XPATH,"//input[@id = 'password']")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.send_keys(Keys.RETURN)
    logging.info("Valid login is performed")
    driver.quit()

@pytest.mark.negative                   # validated login (negative)
@pytest.mark.regression
def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    user_name = driver.find_element(By.XPATH,"//input[@id = 'user-name']")
    user_name.send_keys("standard_user123")
    password = driver.find_element(By.XPATH,"//input[@id = 'password']")
    password.send_keys("secret_sauce123")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.send_keys(Keys.RETURN)
    assert driver.find_element(By.XPATH,"//div[@class = 'error-message-container error']").is_displayed()
    logging.info("In Valid login is performed")
    driver.quit()

@pytest.mark.positive                   # validated correct title (positive)
@pytest.mark.regression
def test_check_correct_title():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    webpage_title = driver.title
    assert webpage_title == "Swag Labs"
    logging.info("Webpage title is correct")
    driver.quit()

@pytest.mark.positive                   # Validate correct URL (positive)
@pytest.mark.regression
def test_check_correctURL():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    webpage_URL = driver.current_url
    assert webpage_URL == "https://www.saucedemo.com/"
    logging.info("Webpage URL is correct")
    driver.quit()

@pytest.mark.positive                     # validate after login URL (positive)
@pytest.mark.regression
def test_after_login_correctURL():
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    user_name = driver.find_element(By.XPATH,"//input[@id = 'user-name']")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.XPATH,"//input[@id = 'password']")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.send_keys(Keys.RETURN)
    after_login_URL = driver.current_url
    time.sleep(2)
    assert after_login_URL == "https://www.saucedemo.com/inventory.html"
    logging.info("Webpage URL is correct after log in")
    driver.quit()

