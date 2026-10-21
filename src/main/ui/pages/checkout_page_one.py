from fixstures.data_fixture import page
from playwright.sync_api import expect


class CheckoutPageOne():
    URL = "https://www.saucedemo.com/checkout-step-one.html"
    def __init__(self, page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.zip_postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.button_error = page.locator("[data-test='error']")
        self.button_click = page.locator("#continue")
    def open(self):
        self.page.goto(self.URL)

    def enter_checkout(self, first_name: str, last_name:str, zip_postal_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_postal_code.fill(zip_postal_code)
        self.button_click.click()

    def verify_order_complete_invalid(self):
        expect(self.button_error).to_be_visible()
        expect(self.button_error).to_have_text("Error: Last Name is required")

