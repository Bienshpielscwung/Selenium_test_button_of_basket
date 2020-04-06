import time


def test_item_has_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    button = browser.find_elements_by_css_selector('button.btn-add-to-basket')
    assert len(button) > 0, 'Button of basket not found'
