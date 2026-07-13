import time
import allure

from playwright.sync_api import Page, expect
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
        self.radiobutton_male = page.get_by_label("Мужчина")
        self.radiobutton_female = page.get_by_label("Женщина")
        self.no_middle_name_check = page.get_by_label("Нет отчества по паспорту")
        self.existing_phone_number_error = page.locator(
            '.error-page-field:has-text("Пользователь с таким мобильным телефоном уже зарегистрирован. Войдите в личный кабинет.")')
        self.existing_email_error = page.locator(
            '.error-page-field:has-text("Пользователь с таким email уже зарегистрирован. Войдите в личный кабинет.")')
        self.error_empty_last_name = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Фамилия».")')
        self.error_wrong_symbols = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и тире (допускается два слова через пробел)")')
        self.error_empty_first_name = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Имя».")')
        self.error_empty_middle_name = page.locator(
            '.error-page-field:has-text("В случае отсутствия установите «Нет отчества как в паспорте»")')
        self.error_empty_birth_date = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Дата рождения».")')
        self.error_wrong_birth_date = page.locator(
            '.error-page-field:has-text("Неправильный формат даты")')
        self.error_empty_phone = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Мобильный телефон».")')
        self.error_wrong_phone = page.locator(
            '.error-page-field:has-text("Используйте формат: +7 (9XX) XXX-XX-XX")')
        self.error_empty_email = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «E-mail».")')
        self.error_wrong_email = page.locator(
            '.error-page-field:has-text("Значение «E-mail» не является правильным email адресом.")')
        self.error_empty_password = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Пароль».")')
        self.error_wrong_password = page.locator(
            '.error-page-field:has-text("Значение «Пароль» должно содержать минимум 6 символов.")')
        self.error_empty_re_password = page.locator(
            ".error-page-field:has-text('Необходимо заполнить «Повторите пароль».')")
        self.error_diff_re_password = page.locator(
            '.error-page-field:has-text("Пароли должны совпадать")')




    @allure.step("Открыть первую страницу регистрации")
    def open_first_step_reg(self):
        self.page.goto(self.first_step_url, wait_until='domcontentloaded')

    @allure.step('Нажать на кнопку "Продолжить"')
    def click_next_step_button_firstpage(self):
        self.next_step_button_first.click()

    @allure.step("Проверить, что отображаются сообщения об ошибке")
    def first_step_empty_fields_error(self):
        expect(self.error_empty_last_name).to_be_visible()
        expect(self.error_empty_first_name).to_be_visible()
        expect(self.error_empty_middle_name).to_be_visible()
        expect(self.error_empty_birth_date).to_be_visible()
        expect(self.error_empty_phone).to_be_visible()
        expect(self.error_empty_email).to_be_visible()
        expect(self.error_empty_password).to_be_visible()
        expect(self.error_empty_re_password).to_be_visible()

    @allure.step('Нажать на кнопку "Продолжить" с заполненными полями')
    def click_next_step_button_first(self):
        self.next_step_button_first.click()
        self.page.wait_for_load_state('load')

    @allure.step('Кликнуть на радиобаттон "Мужчина" ')
    def click_on_male_radiobutton(self):
        self.radiobutton_male.click()

    @allure.step('Кликнуть на радиобаттон "Женщина" ')
    def click_on_female_radiobutton(self):
        self.radiobutton_female.click()

    @allure.step('Кликнуть на чекбокс "Нет отчества по паспорту" ')
    def click_on_no_midname_check(self):
        self.no_middle_name_check.click()

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




