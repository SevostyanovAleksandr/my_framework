import allure
from fixstures.data_fixture import page
from src.main.ui.pages.catalog_page import CatalogPage
from playwright.sync_api import Page, expect
from src.main.ui.pages.login_page import LoginPage

class CatalogStep:
    def __init__(self, page: Page):
        self.page = page
        self.catalog_page = CatalogPage(page)

    @allure.step("Открывем страницу каталога")
    def open_catalog_page(self):
        self.catalog_page.open()
        return self

    @allure.step("Выполняем логаут, проверка корректности редиректа, видимость кнопки авторизации")
    def logout(self):
        self.catalog_page.logout()
        expect(self.page).to_have_url(LoginPage.URL)
        expect(self.page.locator("#login-button")).to_be_visible()
        return self

    @allure.step("Сортируем товары по вписанному фильтру")
    def sort_item(self, option: str):
        self.catalog_page.sort_catalog_items(option)
        return self

    @allure.step("Переход на страницу корзины")
    def add_open_cart(self):
        self.catalog_page.open_cart()
        return self

    @allure.step("Добавляем товар в корзину {product_name}")
    def add_to_cart(self, product_name: str):
       button = self.catalog_page.add_to_cart(product_name)
       return button

    @allure.step("Удаляем товар из корзины {product_name}")
    def remove_from_cart(self, product_name: str):
        button = self.catalog_page.remove_from_cart(product_name)
        return button

    @allure.step("Получаем количество товаров в корзине")
    def get_cart_count(self) -> int:
        return self.catalog_page.get_cart_count()

    @allure.step("Получаем счетчик товаров в корзине")
    def get_product_count(self) -> int:
        return self.catalog_page.get_products_count()

    @allure.step("Получаем название всех товаров")
    def get_product_name(self) -> list[str]:
        return self.catalog_page.get_products_names()

    @allure.step("Получаем список цен товаров")
    def get_prduct_price(self) -> list[float]:
        return self.catalog_page.get_products_price()

    @allure.step("Открываем страницу деталей")
    def open_product_details(self, product_name: str):
       return self.catalog_page.open_product_details(product_name)

    @allure.step("Возвращаем счетчик корзины ")
    def get_cart_badge(self):
        return self.catalog_page.cart_badge



