from fixstures.data_fixture import page
from playwright.sync_api import expect

class CheckoutPageTwo:
    URL = "https://www.saucedemo.com/checkout-step-two.html"
    def __init__(self, page):
        self.page = page
        self.button_finish = page.locator("#finish")
        self.item_total = page.locator("[data-test='subtotal-label']")
        self.tax = page.locator("[data-test='tax-label']")
        self.total = page.locator("[data-test='total-label']")
        self.inscription = page.locator("[data-test='complete-header']")



    #Метод который возаращает сумму товаров поля Item Total
    def get_item_total_checkout(self):
        item_total_text = self.item_total.text_content()
        item_total = float(item_total_text.replace("Item total: $", ""))
        return item_total

    #Метод котороый возврашает сумму товаров поля Tax
    def get_tax_checkout(self):
        tax_text = self.tax.text_content()
        tax = float(tax_text.replace("Tax: $", ""))
        return tax


    #Метод который возвращает значение поля Total
    def get_total_checkout(self):
        total_text = self.total.text_content()
        total = float(total_text.replace("Total: $", ""))
        return total

    # Метод который нажиммает кнопку Finish
    def finish_click(self):
        self.button_finish.click()

    def verify_order_complete(self):
        finish_inscription = self.page.locator("[data-test='complete-header']")
        expect(finish_inscription).to_be_visible()
        expect(finish_inscription).to_have_text("Thank you for your order!")

