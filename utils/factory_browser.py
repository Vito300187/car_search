from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def get_driver():
    options = webdriver.ChromeOptions()
    driver_browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options.add_experimental_option('excludeSwitches', ['enable-automation'])
    )
    # webdriver.DesiredCapabilities.CHROME['proxy'] = {
    #     "httpProxy": "<HOST:PORT>",
    #     "ftpProxy": "<HOST:PORT>",
    #     "sslProxy": "<HOST:PORT>",
    #     "proxyType": "MANUAL",
    # }
    driver_browser.maximize_window()
    return driver_browser
