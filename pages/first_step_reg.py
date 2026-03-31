import time
import allure

from playwright.sync_api import Page
from faker import Faker
fake_ru = Faker("ru_RU")
fake_en = Faker("en_US")


class FirstStep:
    first_step_url = 'https://rc.dev.oneclickmoney.ru/registration/first'
    def __init__(self, page: Page):
        self.page = page
        self.user_lastname_input = page.locator('#usermodel-last_name')
        self.user_firstname_input = page.locator('#usermodel-first_name')
        self.user_middlename_input = page.locator('#usermodel-middle_name')
        self.birthdate_input = page.locator('#usermodel-birth_date')
        self.phone_input = page.locator('#usermodel-mobile_phone')
        self.email_input = page.locator('#usermodel-email')
        self.password_input = page.locator('#usermodel-password')
        self.confirm_password_input = page.locator('#usermodel-confirm_password')
        self.next_step_button_first = page.locator('#next-step-button')
        self.existing_phone_number_error = page.locator(
            '.error-page-field:has-text("Пользователь с таким мобильным телефоном уже зарегистрирован. Войдите в личный кабинет.")')
        self.existing_email_error = page.locator(
            '.error-page-field:has-text("Пользователь с таким email уже зарегистрирован. Войдите в личный кабинет.")')



    @allure.step("Открыть первую страницу регистрации")
    def open_first_step_reg(self):
        self.page.goto(self.first_step_url, wait_until='domcontentloaded')



    @allure.step('Нажать на кнопку "Продолжить"')
    def click_next_step_button_first(self):
        self.next_step_button_first.click()
        self.page.wait_for_load_state('load')


    @allure.step("Заполнить поля 1-ого шага валидными данными")
    def fill_personal_data_first_step(self):
        birth_date = fake_ru.date_of_birth(minimum_age=18, maximum_age=65)
        birth_date_str = birth_date.strftime('%d.%m.%Y')
        self.user_lastname_input.fill(fake_ru.last_name())
        self.user_firstname_input.fill(fake_ru.first_name())
        self.user_middlename_input.fill(fake_ru.middle_name())
        self.birthdate_input.fill(birth_date_str)
        self.phone_input.fill(f'9{fake_ru.msisdn()}')
        self.email_input.fill(fake_en.email())
        self.password_input.fill('123456')
        self.confirm_password_input.fill('123456')


    @allure.step("Перейти на вторую страницу регистрации")
    def get_to_second_step(self):
        self.open_first_step_reg()
        self.fill_personal_data_first_step()
        self.click_next_step_button_first()



