import pytest
from playwright.sync_api import sync_playwright, expect
from pages.catalog_page import CatalogPage
from src.main.ui.step.catalog_step import CatalogStep

@pytest.mark.catalog
class TestCtalog:
        def test_catalog(self, auth_page, page    ):
                catalog_step = CatalogStep(auth_page)
                #Проверка редиректа
                expect(auth_page).to_have_url(CatalogPage.URL)

                #Проверка количества товаров
                count_product = catalog_step.get_product_count()
                assert 6 == count_product

        def test_sort_by_a_z(self, auth_page, page):
                catalog_step = CatalogStep(auth_page)
                #Проверка редиректа
                expect(auth_page).to_have_url(CatalogPage.URL)

                #получили список названий товаров
                names = catalog_step.sort_item("az").get_product_name()

                #проверяем что список товаров отсортирован
                assert names == sorted(names), "товары не отсортированы  a-z"

        def test_sort_by_z_a(self, auth_page, page):
                catalog_step = CatalogStep(auth_page)
                # Проверка редиректа
                expect(auth_page).to_have_url(CatalogPage.URL)

                # получили список названий товаров
                names = catalog_step.sort_item("za").get_product_name()

                # проверяем что список товаров отсортирован
                assert names == sorted(names, reverse=True), "товары не отсортированы  z - a"

        def test_sort_by_high_low(self, auth_page, page):
                catalog_step = CatalogStep(auth_page)
                # Проверка редиректа
                expect(auth_page).to_have_url(CatalogPage.URL)

                # получили список названий товаров
                names = catalog_step.sort_item("hilo").get_product_name()
                #Получаем цены
                prices = catalog_step.get_prduct_price()

                # Проверяем, что цены отсортированы по убыванию
                assert prices == sorted(prices, reverse=True), "Цены не отсортированы от высокой к низкой"

        def test_add_to_cart(self, auth_page):
                catalog_step = CatalogStep(auth_page)
                #Метода для поиска карточки по имени товара. Находим товар, кликаем по товару, переходим в корзину
                catalog_step.add_to_cart("Sauce Labs Fleece Jacket")
                #Проверка на то что в корзине есть один товар
                expect(catalog_step.get_cart_badge()).to_have_text("1")

        def test_add_remove_cards(self, auth_page, page):
                catalog_step = CatalogStep(auth_page)
                button = catalog_step.add_to_cart("Sauce Labs Backpack")
                expect(button).to_have_text("Remove")
                expect(catalog_step.get_cart_badge()).to_have_text("1")
                remove_button = catalog_step.remove_from_cart("Sauce Labs Backpack")
                expect(remove_button).to_have_text("Add to cart")
                expect(catalog_step.get_cart_badge()).not_to_be_visible()

        def test_cards_jacket(self, auth_page, page):
                step_catalog = CatalogStep(auth_page)
                name, price, detail_name, detail_price = step_catalog.open_product_details("Sauce Labs Fleece Jacket")
                assert name == detail_name
                assert price == detail_price








