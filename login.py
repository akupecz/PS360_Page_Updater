from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import GOOGLE_AUTH_SECRET, EMAIL, PASS
from pyotp import *
import time

def login(driver, wait):
    # Set up topt
    totp = TOTP(GOOGLE_AUTH_SECRET)
    # Sign In to Esri 
    url = 'https://philly-stat-360-hub-1-1-phl.hub.arcgis.com/'
    driver.get(url)
    original_window = driver.current_window_handle
    time.sleep(5)

    # Find the sign in button
    sign_in_btn = driver.find_element(By.CLASS_NAME, 'splash-screen').shadow_root.find_element(By.CSS_SELECTOR, 'slot:nth-child(4) > div > calcite-button').shadow_root.find_element(By.CSS_SELECTOR, 'div > button')
    driver.execute_script("arguments[0].click();", sign_in_btn)
    wait.until(EC.number_of_windows_to_be(2))

    # Switch to new window
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, '#loginComponents > section.enterprise-info > div > div > div > div').click()

    # Sign into account
    email_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i0116')))
    email_box.send_keys(EMAIL)
    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSIButton9')))
    time.sleep(1)
    next_btn.click()
    password_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#i0118')))
    password_box.send_keys(PASS)
    next_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSIButton9')))
    time.sleep(1)
    next_btn.click()

    # OTP Authentication
    otp_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#idTxtBx_SAOTCC_OTC')))
    otp_box.send_keys(totp.now())
    time.sleep(5)
    submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSubmit_SAOTCC_Continue')))
    submit_btn.click()
    yes_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#idSIButton9')))
    yes_btn.click()

    # Switch back to original window
    driver.switch_to.window(original_window)
    return




