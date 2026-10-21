from playwright.sync_api import sync_playwright, expect
import pytest
from src.main.ui.fixstures.login_fixture import auth_page
from pages.catalog_page import CatalogPage
from src.main.ui.step.basket_step import BasketStep
from src.main.ui.step.catalog_step import CatalogStep


@pytest.mark.basket
class TestCheckoutCard():
        def test_add_jacket_add_shirt_chek_to_card(self, auth_page):
                #Инициализация обьектов
                catalog_step = CatalogStep(auth_page)
                basket_step = BasketStep(auth_page)

                #Проверка редиректа на нужный URL
                expect(auth_page).to_have_url(CatalogPage.URL)

                #Добавление двух продуктов
                catalog_step.add_to_cart("Sauce Labs Bolt T-Shirt")
                catalog_step.add_to_cart("Sauce Labs Fleece Jacket")

                #Переход в корзину
                catalog_step.add_open_cart()
                item_names = basket_step.get_all_cart_items()

                #Проверяем что товарв есть в коризне
                assert ("Sauce Labs Bolt T-Shirt" in item for item in item_names)
                assert ("Sauce Labs Fleece Jacket" in item for item in item_names)


        def test_add_jacket_add_shirt_remove_and_chek(self, auth_page, page):
                #Инициализация обьектов
                catalog_step = CatalogStep(auth_page)
                basket_step = BasketStep(auth_page)

                #Проверка редиректа на урл каталога
                expect(auth_page).to_have_url(CatalogPage.URL)

                #Добавляем два товара в корзину
                catalog_step.add_to_cart("Sauce Labs Bolt T-Shirt")
                catalog_step.add_to_cart("Sauce Labs Fleece Jacket")

                #Переходим в корзину
                catalog_step.add_open_cart()

                #Берем все продукты корзины и заприсываем в переменную
                item_names = basket_step.get_all_cart_items()

                #Проверяем что товары есть в корзине
                assert ("Sauce Labs Bolt T-Shirt" in item for item in item_names)
                assert ("Sauce Labs Fleece Jacket" in item for item in item_names)

                #Удаляем товара
                catalog_step.remove_from_cart("Sauce Labs Bolt T-Shirt")
                catalog_step.remove_from_cart("Sauce Labs Fleece Jacket")

                #Проверяем что товара больше нету, два продукта положили туда два забрали
                count_basket = catalog_step.get_product_count()
                assert count_basket == 0














