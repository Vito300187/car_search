import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    if os.getenv('SELENOID'):
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "104.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        driver_browser = webdriver.Remote('http://localhost:4444/wd/hub', options=options, desired_capabilities=capabilities)
    else:
        if os.getenv('HEADLESS'):
            options.add_argument('--headless')
        driver_browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver_browser.set_window_size(1920, 1080)
    return driver_browser
