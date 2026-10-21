import allure
from playwright.sync_api import Page
from src.main.ui.pages.checkout_page_one import CheckoutPageOne
from src.main.ui.pages.checkout_page_two import CheckoutPageTwo

class CheckoutStep():
    def __init__(self, page: Page):
        self.page = page
        self.checkout_page_one = CheckoutPageOne(self.page)
        self.checkout_page_two = CheckoutPageTwo(self.page)

    @allure.step("Заполняет все поля ввода чекоут1")
    def enter_checkout(self, first_name: str, last_name: str, zip_postal_code: str):
      self.checkout_page_one.enter_checkout(first_name, last_name,  zip_postal_code)
      return self

    @allure.step("Возаращает сумму товаров поля Item Total")
    def get_item_total_checkout(self):
        item_item = self.checkout_page_two.get_item_total_checkout()
        return item_item

    @allure.step("Считаем сумму товаров поля Tax")
    def get_tax_checkout(self):
        tax = self.checkout_page_two.get_tax_checkout()
        return tax

    @allure.step("Считаем сумму товаров Total")
    def get_total_checkout(self):
        total = self.checkout_page_two.get_total_checkout()
        return total

    @allure.step("Нажимаем на кнопку Finish")
    def finish_checkout(self):
        self.checkout_page_two.finish_click()
        return self

    @allure.step("Проверка наличия надписи об успехе")
    def verify_order_complete(self):
        self.checkout_page_two.verify_order_complete()
        return self

    @allure.step("Проверка наличия надписи об ошибки")
    def verify_order_complete_invalid(self):
        self.checkout_page_one.verify_order_complete_invalid()
        return self