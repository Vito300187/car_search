import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    if os.environ['SELENOID']:
        desired_capabilities = {
            "browserName": 'chrome',
            "enableVNC": True,
            "enableVideo": True
        }
        driver_browser = webdriver.Remote('http://localhost:4444/wd/hub', options=options, desired_capabilities=desired_capabilities)
    elif os.environ['SELENIUM']:
        if os.getenv('HEADLESS'):
            options.add_argument('--headless')
        driver_browser = webdriver.Remote(ChromeDriverManager().install(), options=options)
    else:
        raise Exception("Incorrect params, required only SELENOID/SELENIUM and optional HEADLESS")

    driver_browser.set_window_size(1920, 1080)
    return driver_browser
