from Base_app import BasePage
from selenium.webdriver.common.by import By

class YandexSearchLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR,'input[class*=search3__input]')
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CSS_SELECTOR,'button[class*=search3__button]')
    LOCATOR_YANDEX_SUGGEST_BAR = (By.CSS_SELECTOR,'ul[class*="mini-suggest__popup-content"]')
    LOCATOR_YANDEX_SERCH = (By.CSS_SELECTOR,'div[class*="main__center"]')
    LOCATOR_YANDEX_NUBER_LINK = (By.CSS_SELECTOR,'ul[class*="serp-list_left_yes"]>li')

class SearchHelper(BasePage):

    def input_search(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST_BAR,time=2)
    
    def check_navigator_link(self):
        link_list = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_NUBER_LINK,time=2)
        link_el = [x.text for x in link_list if len(x.text) > 0]
        return link_el
    
    def check_search(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SERCH,time=2)

        
 