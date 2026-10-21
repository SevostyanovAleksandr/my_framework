from playwright.sync_api import Page
from fixstures.data_fixture import page


class BasketPage():
    URL = "https://www.saucedemo.com/cart.html"
    def __init__(self, page: Page):
        self.page = page
        self.button_checkout = page.locator("#checkout")
        self.item_name = page.locator("[data-test='inventory-item']")
        self.cart_items = page.locator(".cart_item")
        self.cart_price = page.locator(".inventory_item_price")

    #Метод для перехода на страницу
    def open(self):
        self.page.goto(self.URL)

    #Метод возвращает товар по его наименованию
    def get_item_name(self, product_name: str):
        return self.item_name.filter(has_text=product_name)

    #Метод возвращает наименование всех товаров в корзине
    def get_all_cart_items(self):
        return self.item_name.all_text_contents()

    #Метод принимает название товара и удаляет его из корзины
    def remove_cart_items(self, product_name: str):
        card = self.cart_items.filter(has_text=product_name)
        button = card.locator("button")
        if button.inner_text() == "Remove":
            button.click()
        return button

    #Метод возвращает сумму всех товаров в корзине
    def get_sum_item_from_cart(self):
        prices_text = self.cart_price.all_text_contents()
        prices = [float(p.replace("$", "")) for p in prices_text]
        prices_sum = sum(prices)
        return prices_sum

    #Метод перехода на страницу проверки
    def open_checkout(self):
        self.button_checkout.click()

