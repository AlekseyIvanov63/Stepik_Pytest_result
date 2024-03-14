from pages.product_page import ProductPage


link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_should_see_product_link(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()
