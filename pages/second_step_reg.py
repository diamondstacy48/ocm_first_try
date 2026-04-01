import allure
from playwright.sync_api import Page, expect
from faker import Faker
fake_ru = Faker("ru_RU")
fake_en = Faker("en_US")


class SecondStep:
    base_url = 'https://rc.dev.oneclickmoney.ru/registration/second'
    def __init__(self, page: Page):
        self.page = page
        self.pass_num_input = page.locator('#usermodel-passport_number')
        self.pass_code_input = page.locator('#usermodel-passport_issuer_code')
        self.pass_name_input = page.locator('#usermodel-passport_issuer_name')
        self.pass_date_input = page.locator('#usermodel-passport_date')
        self.pass_birthplace_input = page.locator('#usermodel-passport_birth_place')
        self.region_input = page.locator('#usermodel-region')
        self.city_input = page.locator('#usermodel-city')
        self.street_input = page.locator('#usermodel-street')
        self.house_num_input = page.locator('#usermodel-house_number')
        self.flat_num_input = page.locator('#usermodel-flat')
        self.match_address_checkbox = page.locator('label[for="usermodel-is_address_match"]')
        self.leg_region_input = page.locator('#usermodel-legal_region')
        self.leg_city_input = page.locator('#usermodel-legal_city')
        self.leg_street_input = page.locator('#usermodel-legal_street')
        self.leg_house_num_input = page.locator('#usermodel-legal_house_number')
        self.leg_flat_num_input = page.locator('#usermodel-legal_flat')
        self.ddo_checkbox = page.locator('label[for="ddoagreementbase-check_ddo"]')
        self.next_step_button_second = page.locator('.registration-two__submit')
        self.error_empty_pass_num = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Серия и номер паспорта».")')
        self.error_wrong_pass_num = page.locator(
            '.error-page-field:has-text("Значение «Серия и номер паспорта» неверно.")')
        self.error_empty_pass_code = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Код подразделения».")')
        self.error_wrong_pass_code = page.locator(
            '.error-page-field:has-text("Значение «Код подразделения» неверно.")')
        self.error_empty_pass_name = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Кем выдан (как в паспорте)».")')
        self.error_wrong_pass_name = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_empty_pass_date = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Дата выдачи».")')
        self.error_empty_pass_birthplace = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Место рождения (как в паспорте)».")')
        self.error_wrong_birthplace = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_empty_region = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Регион / Район».")')
        self.error_wrong_region = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_empty_city = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Город / Населенный пункт».")')
        self.error_wrong_city = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_empty_street = page.locator(
            ".error-page-field:has-text('Улица - обязательное поле (если отсутствует, укажите \"нет\").')")
        self.error_wrong_street = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_wrong_house = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_maxlenght_house = page.locator(
            '.error-page-field:has-text("Значение «Дом» должно содержать максимум 10 символов.")')
        self.error_empty_leg_region = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Регион».")')
        self.error_wrong_leg_region = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_empty_leg_city = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Кем выдан (как в паспорте)».")')
        self.error_wrong_leg_city = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_empty_leg_street = page.locator(
            '.error-page-field:has-text("Улица - обязательное поле (если отсутствует, укажите "нет").")')
        self.error_wrong_leg_street = page.locator(
            '.error-page-field:has-text("Используйте только русские буквы и цифры")')
        self.error_ddo_unchecked = page.locator(
            '.error-page-field:has-text("Необходимо Ваше согласие")')




# Кликнуть на чекбокс ДДО
    @allure.step("Кликнуть на чекбокс ДДО")
    def click_on_ddo_check(self):
        self.ddo_checkbox.click()

#Кликнуть на кнопку "Продолжить" 2 страница регистрации
    @allure.step('Кликнуть на кнопку "Продолжить"')
    def click_next_step_button_second(self):
        self.next_step_button_second.click()

# Проверка алерта ДДО
    @allure.step("Проверить отображение алерта ДДО")
    def get_ddo_error_message(self):
        return self.error_ddo_unchecked.inner_text()

# Кликнуть на чекбокс "Проживаю по прописке"
    @allure.step("Кликнуть на чекбокс Проживаю по прописке")
    def click_address_checkbox(self):
        self.match_address_checkbox.click()


# Проверка отображения алертов обязательных полей на 2 шаге
    @allure.step("Проверить, что отображаются сообщения об ошибке")
    def empty_fields_error(self):
        expect(self.error_empty_pass_num).to_be_visible()
        expect(self.error_empty_pass_code).to_be_visible()
        expect(self.error_empty_pass_name).to_be_visible()
        expect(self.error_empty_pass_date).to_be_visible()
        expect(self.error_empty_pass_birthplace).to_be_visible()
        expect(self.error_empty_region).to_be_visible()
        expect(self.error_empty_leg_region).to_be_visible()



    @allure.step("Заполнить поле Регион/Район")
    def fill_region_field(self):
        self.region_input.fill("Самарская обл")
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")


# Заполнение полей второго шага регистрации
    @allure.step("Заполнить поля на второй странице регистрации валидными данными")
    def fill_personal_data_second_step(self):
        # я не знаю правильно ли, но это сработало!
        self.pass_num_input.fill(f'630{fake_ru.msisdn()}')
        self.pass_code_input.fill(fake_ru.bothify(text='##'))
        self.page.wait_for_selector("#passport_issuer_name__suggestions", state='visible')
        self.page.get_by_text("-0").first.click()
        self.pass_date_input.fill('01.12.2025')
        self.pass_birthplace_input.fill(fake_ru.city())
        region_text=fake_ru.region()
        self.region_input.fill(region_text)
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.city_input.fill('г')
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.street_input.fill('ул')
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.house_num_input.fill('1')
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.flat_num_input.fill('54')
        self.click_address_checkbox()
        self.leg_region_input.fill(region_text)
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.leg_city_input.fill("г")
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.leg_street_input.fill("ул")
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.leg_house_num_input.fill("1")
        self.page.wait_for_selector('.suggestions-suggestion', state="visible")
        self.page.click(".suggestions-suggestion[data-index='0']")
        self.leg_flat_num_input.fill('12')


        # ВОТ ЭТО всё не получается из-за того, что не выбирается вариант из подсказок dadata
        # self.pass_num_input.fill(fake_ru.bothify(text='#### ######'))
        # passport_number=fake_ru.passport_number()
        # self.pass_num_input.fill(passport_number)
        # self.pass_code_input.fill(passport_number[:2])
        # self.page.wait_for_selector("#passport_issuer_name__suggestions", state='visible')
        # self.page.get_by_text("-0").first.click()
        # self.pass_date_input.fill('01.12.2025')
        # self.pass_birthplace_input.fill(fake_ru.city())
        # region_text=fake_ru.region()
        # self.region_input.fill(region_text)
        # self.page.wait_for_selector(".suggestions-suggestions", timeout=30) не видит
        # # self.page.get_by_text(region_text[0]).first.click() не работает
        #

