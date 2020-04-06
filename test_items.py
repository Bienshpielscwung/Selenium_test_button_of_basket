import time


def test_button_of_basket(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    button = browser.find_element_by_css_selector('button.btn-add-to-basket')
    assert button.text is not None, 'Button of basket not found'
