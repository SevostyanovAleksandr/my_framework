from playwright.sync_api import sync_playwright, expect
import pytest
from pages.catalog_page import CatalogPage
from src.main.ui.step.basket_step import BasketStep
from src.main.ui.step.checkout_step import CheckoutStep
from src.main.ui.step.catalog_step import CatalogStep
from src.main.ui.pages.checkout_page_one import CheckoutPageOne
from src.main.ui.pages.checkout_page_two import CheckoutPageTwo

@pytest.mark.checkout
class TestCheckoutCard():
    def test_checkout_card_standart_user(self, auth_page):
        #инициалировать 4 обькта
        catalog_step = CatalogStep(auth_page)
        basket_step = BasketStep(auth_page)
        checkout_step = CheckoutStep(auth_page)

        # проверка нужного редиректа
        expect(auth_page).to_have_url(CatalogPage.URL)

        #Добавляем продукт в корзину
        catalog_step.add_to_cart("Sauce Labs Backpack")

        #Переходим в корзину
        catalog_step.add_open_cart()

        #проверяем что есть товары в корзине
        assert 1 == catalog_step.get_product_count()

        #считаем сумму всех товаров
        price_sum_from_cart = basket_step.get_sum_item_from_cart()

        #переход на страницу чекаут
        basket_step.open_checkout()

        #проверяем нужный редирект
        expect(auth_page).to_have_url(CheckoutPageOne.URL)

        #заполняем поля воода чекают нажимаем кнопку континью
        checkout_step.enter_checkout(first_name="Said", last_name="Bek", zip_postal_code="KSSH")
        #проверяем нужный редирект
        expect(auth_page).to_have_url(CheckoutPageTwo.URL)

        #проверяем сумму item total что она соотвествует сумме товаров в корзине
        item_total = checkout_step.get_item_total_checkout()
        assert price_sum_from_cart == item_total

        #считаем сумму tax
        tax = checkout_step.get_tax_checkout()
        tax_and_item_total = tax + item_total

        #сравниваем итоговую сумму с тотал
        total_finish = checkout_step.get_total_checkout()
        assert total_finish == tax_and_item_total

        #завершаем покупку
        checkout_step.finish_checkout()

        #проверяем редиреки на нужный
        expect(auth_page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

        #проверяем коррекиность отображения надписи
        checkout_step.verify_order_complete()

    def test_checkout_card_standart_user_invalid_last_name(self, auth_page):
        # инициалировать 4 обькта
        catalog_step = CatalogStep(auth_page)
        basket_step = BasketStep(auth_page)
        checkout_step = CheckoutStep(auth_page)

        # проверка нужного редиректа
        expect(auth_page).to_have_url(CatalogPage.URL)

        # Добавляем продукт в корзину
        catalog_step.add_to_cart("Sauce Labs Backpack")
        catalog_step.add_to_cart("Sauce Labs Bolt T-Shirt")

        # Переходим в корзину
        catalog_step.add_open_cart()

        # проверяем что есть товары в корзине
        assert 2 == catalog_step.get_product_count()

        # считаем сумму всех товаров
        price_sum_from_cart = basket_step.get_sum_item_from_cart()

        # переход на страницу чекаут
        basket_step.open_checkout()

        # проверяем нужный редирект
        expect(auth_page).to_have_url(CheckoutPageOne.URL)

        # заполняем поля воода чекают нажимаем кнопку континью
        checkout_step.enter_checkout(first_name="Said", last_name="", zip_postal_code="KSSH")

        #проверка надписи об ошибки
        checkout_step.verify_order_complete_invalid()