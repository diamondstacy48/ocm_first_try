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
        self.leg_street_input = page.locator('#uusermodel-legal_street')
        self.leg_house_num_input = page.locator('#usermodel-legal_house_number')
        self.leg_flat_num_input = page.locator('#usermodel-legal_flat')
        self.ddo_checkbox = page.locator('label[for="ddoagreementbase-check_ddo"]')
        self.next_step_button_second = page.locator('.registration-two__submit')
        self.dadata_var = page.locator('.suggestions-suggestions')
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
        self.error_empty_region = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Регион / Район».")')
        self.error_empty_city = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Город / Населенный пункт».")')
        self.error_empty_street = page.locator(
            '.error-page-field:has-text("Улица - обязательное поле (если отсутствует, укажите "нет").")')
        self.error_empty_leg_region = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Регион».")')
        self.error_empty_leg_city = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Кем выдан (как в паспорте)».")')
        self.error_empty_leg_street = page.locator(
            '.error-page-field:has-text("Необходимо заполнить «Пароль».")')
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



 #не работает, надо подумать
    def choose_dadata_first_var(self):
        self.page.wait_for_selector('.suggestions-suggestions')
        first_var_dadata = '.suggestions-suggestions:nth(0)'
        self.page.click(first_var_dadata)



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



    @allure.step("Заполнить поля на второй странице регистрации валидными данными")
    def fill_all_fields(self):
        self.pass_num_input.fill(f'630{fake_ru.msisdn()}')
        self.pass_code_input.fill('630-000')
        # self.choose_dadata_first_var()
        # self.dadata_var.nth(0).click()
        # self.pass_name_input.fill('ПРОМЫШЛЕННЫМ РУВД Г. САМАРЫ')
        self.pass_date_input.fill('01.12.2025')
        self.pass_birthplace_input.fill(fake_ru.city())
        self.region_input.fill("Самарская обл")
        self.page.wait_for_selector('.suggestions-suggestions')
        self.dadata_var.nth(0).click()
        self.city_input.fill('Самара')
        self.dadata_var.nth(0).click()
        self.street_input.fill('Волжский пр-кт')
        self.dadata_var.nth(0).click()
        self.house_num_input.fill('5')
        self.dadata_var.nth(0).click()
        self.flat_num_input.fill('55')
        
        


# Заполнение полей второго шага регистрации
    def fill_personal_data_second_step(self):
        # self.pass_num_input.fill(f'630{fake_ru.msisdn()}')
        self.pass_num_input.fill(fake_ru.bothify(text='#### ######'))
        self.pass_code_input.fill(fake_ru.bothify(text='##'))
        self.page.wait_for_selector("#passport_issuer_name__suggestions", state='visible')
        self.page.get_by_text("-0").first.click()
        self.pass_date_input.fill('01.12.2025')
        self.pass_birthplace_input.fill(fake_ru.city())
        region_text=fake_ru.region()
        self.region_input.fill(region_text)
        self.page.wait_for_selector("#passport_issuer_name__suggestions", state='visible')
        self.page.get_by_text(region_text[0]).first.click()
        self.page.wait_for_selector('#usermodel-city', state='visible')
        self.street_input.fill(fake_ru.lexify(text='?'))
        self.page.wait_for_selector("#passport_issuer_name__suggestions", state='visible')
        self.page.get_by_text("ул").first.click()
        self.house_num_input.fill(fake_ru.bothify(text='#'))
        self.page.wait_for_selector("#passport_issuer_name__suggestions", state='visible')
        self.page.get_by_text("д").first.click()
        self.flat_num_input.fill('55')
