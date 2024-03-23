from BaseApp import BasePage


class TestPage(BasePage):
    def enter_keys(self, word, locator):
        field = self.find_element(locator)
        field.clear()
        field.send_keys(word)

    def click_btn(self, locator):
        self.find_element(locator).click()
