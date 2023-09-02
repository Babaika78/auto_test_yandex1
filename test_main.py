from YandexPages import SearchHelper

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    search = yandex_main_page.input_search()
    assert search.is_enabled() == True

    in_search = yandex_main_page.enter_word("Тензор")

    suggest = yandex_main_page.check_navigation_bar()
    assert suggest.is_enabled() == True

    yandex_main_page.click_on_the_search_button()

    search_label = yandex_main_page.check_search()
    elements = yandex_main_page.check_navigator_link()

    assert search_label.is_enabled() == True
    assert "tensor" in elements[0]
    
