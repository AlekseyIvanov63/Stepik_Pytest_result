from selenium.webdriver.common.by import By
from conftest import browser
from time import sleep

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_items(browser):
    browser.get(link)
    sleep(30)
    item = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    assert item.text == 'Ajouter au panier', 'No your language'
