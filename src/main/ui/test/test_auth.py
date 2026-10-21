from playwright.sync_api import expect
import pytest
from src.main.ui.pages.catalog_page import CatalogPage
from src.main.ui.step.login_step import LoginSteps
from src.main.ui.step.catalog_step import CatalogStep


@pytest.mark.auth
class TestAuth:
        def test_login_user_standart(self, page):
                #Авторизации
                steps = LoginSteps(page)
                steps.open_login_page().login("standard_user", "secret_sauce")

                #проверка редиректа
                expect(page).to_have_url(CatalogPage.URL)

        def test_auth_logout_visual_user(self, page):
                #Авторизации
                steps = LoginSteps(page)
                steps.open_login_page().login("standard_user", "secret_sauce")

                #проверка редиректа

                expect(page).to_have_url(CatalogPage.URL)
                #Логаут и проверка корреткности редиректа, видимость кнопки авториазции
                steps_catalog = CatalogStep(page)
                steps_catalog.logout()

        def test_auth_logout_locked_user(self, page):
                # Авторизации и проверка ошибки авторизации
                steps = LoginSteps(page)
                error_text = steps.open_login_page().login("locked_out_user", "secret_sauce").login_page.get_error_message()
                assert "locked out" in error_text, "Ожидаем сообщение о заблокированном пользователе"