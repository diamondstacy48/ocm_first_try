from playwright.sync_api import Page

class SigninPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('#loginform-username')
        self.password_input = page.locator('#loginform-password')
        self.login_button = page.locator('#idx_login')
        self.error_message_incorrect = page.locator('.error-page-field:has-text("Неверный логин или пароль")')
        self.error_message_username_is_empty = page.locator('.error-page-field:has-text("Необходимо заполнить «Email или телефон».")')
        self.error_message_password_is_empty = page.locator('.error-page-field:has-text("Необходимо заполнить «Пароль».")')


    def open_signin_form(self):
        self.page.goto('https://rc.dev.oneclickmoney.ru/#signin')

    def login_with_creds(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_without_username(self, password: str):
        self.password_input.fill(password)
        self.login_button.click()

    def login_without_password(self, username: str):
        self.username_input.fill(username)
        self.login_button.click()

    def get_error_message_incorrect(self):
        return self.error_message_incorrect.inner_text()

    def get_error_message_empty_username(self):
        return self.error_message_username_is_empty.inner_text()

    def get_error_message_empty_password(self):
        return self.error_message_password_is_empty.inner_text()
