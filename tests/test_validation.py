import pytest
import allure
from playwright.sync_api import Page, expect

# для инфо поле "квартира" у нас без валидации почему-то, на него тест не писала

# это просто для проверки что поля регистрации заполняются
def test_reg_reg(first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.fill_personal_data_second_step()


# Для некоторых шагов allure steps написаны в page

# ПРОВЕРКА ОБЯЗАТЕЛЬНЫХ ПОЛЕЙ НА 1-ОМ ШАГЕ РЕГИСТРАЦИИ

@allure.feature('Валидация полей на первом шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка обязательных полей на первом шаге регистрации')
def test_empty_firststep_fields_error(first_step_reg):
    first_step_reg.open_first_step_reg()
    first_step_reg.click_next_step_button_firstpage()
    first_step_reg.first_step_empty_fields_error()


#ПРОВЕРКА ПОЛЯ ФАМИЛИЯ
@allure.feature('Валидация полей на первом шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Фамилия"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("Иванов", None),
        ("Ivanov", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("123", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("Ив@нов", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("", "Необходимо заполнить «Фамилия»."),
        ("Иванов-Петров", None),
    ]
)
def test_last_name_field(page: Page, value: str, expected_error: str, first_step_reg):
    first_step_reg.open_first_step_reg()

    with allure.step(f"Ввод значения в поле Фамилия: '{value}'"):
        first_step_reg.user_lastname_input.fill(value)
        first_step_reg.user_lastname_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(first_step_reg.error_wrong_symbols).not_to_be_visible()
            expect(first_step_reg.error_empty_last_name).not_to_be_visible()
        else:
            if "Используйте только русские буквы и тире (допускается два слова через пробел)" in expected_error:
                expect(first_step_reg.error_wrong_symbols).to_be_visible()
                error_message = first_step_reg.error_wrong_symbols.text_content()
            else:
                expect(first_step_reg.error_empty_last_name).to_be_visible()
                error_message = first_step_reg.error_empty_last_name.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'


#ПРОВЕРКА ПОЛЯ ИМЯ
@allure.feature('Валидация полей на первом шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Имя"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("Иван", None),
        ("Ivanov", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("123", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("Ив@н", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("", "Необходимо заполнить «Имя»."),
        ("Иван-Ваня", None),
    ]
)
def test_first_name_field(page: Page, value: str, expected_error: str, first_step_reg):
    first_step_reg.open_first_step_reg()

    with allure.step(f"Ввод значения в поле Имя: '{value}'"):
        first_step_reg.user_firstname_input.fill(value)
        first_step_reg.user_firstname_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(first_step_reg.error_wrong_symbols).not_to_be_visible()
            expect(first_step_reg.error_empty_first_name).not_to_be_visible()
        else:
            if "Используйте только русские буквы и тире (допускается два слова через пробел)" in expected_error:
                expect(first_step_reg.error_wrong_symbols).to_be_visible()
                error_message = first_step_reg.error_wrong_symbols.text_content()
            else:
                expect(first_step_reg.error_empty_first_name).to_be_visible()
                error_message = first_step_reg.error_empty_first_name.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'

#ПРОВЕРКА ПОЛЯ ОТЧЕСТВО
@allure.feature('Валидация полей на первом шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Отчество"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("Иван", None),
        ("Ivanovich", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("123", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("Ив@нович", "Используйте только русские буквы и тире (допускается два слова через пробел)"),
        ("", "В случае отсутствия установите «Нет отчества как в паспорте»"),
        ("Иванович-Петрович", None),
    ]
)
def test_middle_name_field(page: Page, value: str, expected_error: str, first_step_reg):
    first_step_reg.open_first_step_reg()

    with allure.step(f"Ввод значения в поле Отчество: '{value}'"):
        first_step_reg.user_middlename_input.fill(value)
        first_step_reg.user_middlename_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(first_step_reg.error_wrong_symbols).not_to_be_visible()
            expect(first_step_reg.error_empty_middle_name).not_to_be_visible()
        else:
            if "Используйте только русские буквы и тире (допускается два слова через пробел)" in expected_error:
                expect(first_step_reg.error_wrong_symbols).to_be_visible()
                error_message = first_step_reg.error_wrong_symbols.text_content()
            else:
                expect(first_step_reg.error_empty_middle_name).to_be_visible()
                error_message = first_step_reg.error_empty_middle_name.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'


#ПРОВЕРКА ПОЛЯ ДАТА РОЖДЕНИЯ
@allure.feature('Валидация полей на первом шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Дата рождения"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("01.08.2000", None),
        ("05.01.20", "Неправильный формат даты"),
        ("ДатаРожд", "Необходимо заполнить «Дата рождения»."),
        ("DataRojd", "Необходимо заполнить «Дата рождения»."),
        ("", "Необходимо заполнить «Дата рождения»."),
        ("#$%#@", "Необходимо заполнить «Дата рождения»."),
    ]
)
def test_birth_date_field(page: Page, value: str, expected_error: str, first_step_reg):
    first_step_reg.open_first_step_reg()

    with allure.step(f"Ввод значения в поле Дата рождения: '{value}'"):
        first_step_reg.birthdate_input.fill(value)
        first_step_reg.birthdate_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(first_step_reg.error_wrong_birth_date).not_to_be_visible()
            expect(first_step_reg.error_empty_birth_date).not_to_be_visible()
        else:
            if "Неправильный формат даты" in expected_error:
                expect(first_step_reg.error_wrong_birth_date).to_be_visible()
                error_message = first_step_reg.error_wrong_birth_date.text_content()
            else:
                expect(first_step_reg.error_empty_birth_date).to_be_visible()
                error_message = first_step_reg.error_empty_birth_date.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'


#ПРОВЕРКА ПОЛЯ "Мобильный телефон"
@allure.feature('Валидация полей на первом шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Мобильный телефон"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("9991234567", None),
        ("999123456", "Используйте формат: +7 (9XX) XXX-XX-XX"),
        ("9", "Используйте формат: +7 (9XX) XXX-XX-XX"),
        ("8991234567", "Используйте формат: +7 (9XX) XXX-XX-XX"),
        ("Абвгд", "Используйте формат: +7 (9XX) XXX-XX-XX"),
        ("Latin", "Используйте формат: +7 (9XX) XXX-XX-XX"),
        ("$@%&#@", "Используйте формат: +7 (9XX) XXX-XX-XX"),
        ("", "Используйте формат: +7 (9XX) XXX-XX-XX"),
    ]
)
def test_birth_date_field(page: Page, value: str, expected_error: str, first_step_reg):
    first_step_reg.open_first_step_reg()

    with allure.step(f"Ввод значения в поле Мобильный телефон: '{value}'"):
        first_step_reg.birthdate_input.fill(value)
        first_step_reg.birthdate_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(first_step_reg.error_wrong_phone).not_to_be_visible()

        else:
                expect(first_step_reg.error_wrong_phone).to_be_visible()
                error_message = first_step_reg.error_wrong_phone.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'















# ПРОВЕКА ОБЯЗАТЕЛЬНЫХ ПОЛЕЙ НА 2-ОМ ШАГЕ РЕГИСТРАЦИИ
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка обязательных полей на втором шаге регистрации')
def test_empty_secondstep_fields_error(first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.click_address_checkbox()
    second_step_reg.click_next_step_button_second()
    second_step_reg.empty_fields_error()


#Проверка обязательности чекбокса ДДО
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка обязательности чекбокса ДДО')
def test_checkDDO_is_required(first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.click_on_ddo_check()
    second_step_reg.click_next_step_button_second()
    second_step_reg.get_ddo_error_message()


#Проверка поля Серия и номер паспорта
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Серия и номер паспорта"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("6561-231311", None),
        ("seria", "Необходимо заполнить «Серия и номер паспорта»."),
        ("серия", "Необходимо заполнить «Серия и номер паспорта»."),
        ("!@:#&", "Необходимо заполнить «Серия и номер паспорта»."),
        ("", "Необходимо заполнить «Серия и номер паспорта»."),
        ("7", "Значение «Серия и номер паспорта» неверно."),
        ("7314-54742", "Значение «Серия и номер паспорта» неверно."),
    ]
)
def test_passport_num_field(page: Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()

    with allure.step(f"Ввод значения в поле Серия и номер паспорта: '{value}'"):
        second_step_reg.pass_num_input.fill(value)
        second_step_reg.pass_num_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_pass_num).not_to_be_visible()
            expect(second_step_reg.error_empty_pass_num).not_to_be_visible()
        else:
            if "Значение «Серия и номер паспорта» неверно." in expected_error:
                expect(second_step_reg.error_wrong_pass_num).to_be_visible()
                error_message = second_step_reg.error_wrong_pass_num.text_content()
            else:
                expect(second_step_reg.error_empty_pass_num).to_be_visible()
                error_message = second_step_reg.error_empty_pass_num.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'


#Проверка поля Код Подразделения
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Код подразделения"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("630-000", None),
        ("kod", "Необходимо заполнить «Код подразделения»."),
        ("код", "Необходимо заполнить «Код подразделения»."),
        ("!@:#&", "Необходимо заполнить «Код подразделения»."),
        ("", "Необходимо заполнить «Код подразделения»."),
        ("6", "Значение «Код подразделения» неверно."),
        ("630-00", "Значение «Код подразделения» неверно."),
    ]
)
def test_passport_code_field(page: Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()

    with allure.step(f"Ввод значения в поле Код подразделения: '{value}'"):
        second_step_reg.pass_code_input.fill(value)
        second_step_reg.pass_code_input.blur()
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_pass_code).not_to_be_visible()
            expect(second_step_reg.error_empty_pass_code).not_to_be_visible()
        else:
            if "Значение «Код подразделения» неверно." in expected_error:
                expect(second_step_reg.error_wrong_pass_code).to_be_visible()
                error_message = second_step_reg.error_wrong_pass_code.text_content()
            else:
                expect(second_step_reg.error_empty_pass_code).to_be_visible()
                error_message = second_step_reg.error_empty_pass_code.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'



#Проверка поля "Кем выдан"
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Кем выдан"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("Кем выдан", None),
        ("kem vidan", "Используйте только русские буквы и цифры"),
        ("!@:#&", "Используйте только русские буквы и цифры"),
        ("", "Необходимо заполнить «Кем выдан (как в паспорте)»."),
        ("1234567890", None),
    ]
)
def test_passport_name_field(page: Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()

    with allure.step(f"Ввод значения в поле Кем выдан: '{value}'"):
        second_step_reg.pass_name_input.fill(value)
        second_step_reg.pass_name_input.blur()
        # page.wait_for_selector(".error-page-field")
    with allure.step(f"Проверка: отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_pass_name).not_to_be_visible()
            expect(second_step_reg.error_empty_pass_name).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_pass_name).to_be_visible()
                error_message = second_step_reg.error_wrong_pass_name.text_content()
            else:
                expect(second_step_reg.error_empty_pass_name).to_be_visible()
                error_message = second_step_reg.error_empty_pass_name.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'




# Проверка валидации поля "Дата выдачи"
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Дата выдачи"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("01.08.2000", None),
        ("05.01.20", None),
        ("ДатаВыд", "Необходимо заполнить «Дата выдачи»."),
        ("DataVid", "Необходимо заполнить «Дата выдачи»."),
        ("#$%#@", "Необходимо заполнить «Дата выдачи»."),
        ("", "Необходимо заполнить «Дата выдачи»."),
    ]
)
def test_passport_date_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    with allure.step(f"Ввод значения в поле Дата выдачи: '{value}'"):
        second_step_reg.pass_date_input.fill(value)
        second_step_reg. pass_date_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_empty_pass_date).not_to_be_visible()
        else:
            expect(second_step_reg.error_empty_pass_date).to_be_visible()
            error_message = second_step_reg.error_empty_pass_date.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", Отображается: "{error_message}"'


# Проверка валидации поля "Место рождения"
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Место рождения"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("1234567890", None),
        ("место рождения", None),
        ("-@%&*", "Используйте только русские буквы и цифры"),
        ("MestoRojd", "Используйте только русские буквы и цифры"),
        ("", "Необходимо заполнить «Место рождения (как в паспорте)»."),
    ]
)
def test_birthplace_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    with allure.step(f"Ввод значения в поле Место рождения: '{value}'"):
        second_step_reg.pass_birthplace_input.fill(value)
        second_step_reg. pass_birthplace_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_birthplace).not_to_be_visible()
            expect(second_step_reg.error_empty_pass_birthplace).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_birthplace).to_be_visible()
                error_message = second_step_reg.error_wrong_birthplace.text_content()
            else:
                expect(second_step_reg.error_empty_pass_birthplace).to_be_visible()
                error_message = second_step_reg.error_empty_pass_birthplace.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'



#Проверка поля "Регион/Район" в адресе прописки
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Регион/Район"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("123", None),
        ("Самарская обл", None),
        ("&!@%?", "Используйте только русские буквы и цифры"),
        ("Region", "Используйте только русские буквы и цифры"),
        ("", "Необходимо заполнить «Регион / Район»."),
    ]
)
def test_region_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    with allure.step(f"Ввод значения в поле Регион/Район: '{value}'"):
        second_step_reg.region_input.fill(value)
        second_step_reg. region_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_region).not_to_be_visible()
            expect(second_step_reg.error_empty_region).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_region).to_be_visible()
                error_message = second_step_reg.error_wrong_region.text_content()
            else:
                expect(second_step_reg.error_empty_region).to_be_visible()
                error_message = second_step_reg.error_empty_region.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'




#Проверка поля "Город / Населенный пункт" в адресе прописки
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Город / Населенный пункт"')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("1234567890", None),
        ("Город", None),
        ("@$%&!", "Используйте только русские буквы и цифры"),
        ("City", "Используйте только русские буквы и цифры"),
        ("", "Необходимо заполнить «Город / Населенный пункт»."),
    ]
)
def test_city_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.fill_region_field()
    with allure.step(f"Ввод значения в поле Город / Населенный пункт: '{value}'"):
        second_step_reg.city_input.fill(value)
        second_step_reg.city_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_city).not_to_be_visible()
            expect(second_step_reg.error_empty_city).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_city).to_be_visible()
                error_message = second_step_reg.error_wrong_city.text_content()
            else:
                expect(second_step_reg.error_empty_city).to_be_visible()
                error_message = second_step_reg.error_empty_city.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'



#Проверка поля "Улица" в адресе прописки
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Улица"')
@pytest.mark.parametrize(
    "value, expected_error",
    {
        ("1234567890", None),
        ("улица", None),
        ("!#$%@&?", "Используйте только русские буквы и цифры"),
        ("Ulitsa", "Используйте только русские буквы и цифры"),
        ("", 'Улица - обязательное поле (если отсутствует, укажите \"нет\").'),
    }
)
def test_street_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.fill_region_field()
    with allure.step(f"Ввод значения в поле Улица: '{value}'"):
        second_step_reg.street_input.fill(value)
        second_step_reg.street_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_street).not_to_be_visible()
            expect(second_step_reg.error_empty_street).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_street).to_be_visible()
                error_message = second_step_reg.error_wrong_street.text_content()
            else:
                expect(second_step_reg.error_empty_street).to_be_visible()
                error_message = second_step_reg.error_empty_street.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'


#Проверка поля "Дом" в адресе прописки
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Дом"')
@pytest.mark.parametrize(
    "value, expected_error",
    {
        ("1234567890", None),
        ("дом", None),
        ("", None),
        ("!#$%@&?", "Используйте только русские буквы и цифры"),
        ("dom", "Используйте только русские буквы и цифры"),
        ("99999999999", 'Значение «Дом» должно содержать максимум 10 символов.'),
    }
)
def test_house_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.fill_region_field()
    with allure.step(f"Ввод значения в поле Дом: '{value}'"):
        second_step_reg.house_num_input.fill(value)
        second_step_reg.house_num_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_house).not_to_be_visible()
            expect(second_step_reg.error_maxlenght_house).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_house).to_be_visible()
                error_message = second_step_reg.error_wrong_house.text_content()
            else:
                expect(second_step_reg.error_maxlenght_house).to_be_visible()
                error_message = second_step_reg.error_maxlenght_house.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'




#Проверка поля "Район" в адресе проживания
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Регион" в адресе проживания')
@pytest.mark.parametrize(
    "value, expected_error",
    [
        ("123", None),
        ("Самарская обл", None),
        ("&!@%?", "Используйте только русские буквы и цифры"),
        ("Region", "Используйте только русские буквы и цифры"),
        ("", "Необходимо заполнить «Регион»."),
    ]
)
def test_leg_region_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.click_address_checkbox()
    with allure.step(f"Ввод значения в поле Регион в адресе проживания: '{value}'"):
        second_step_reg.leg_region_input.fill(value)
        second_step_reg.leg_region_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_leg_region).not_to_be_visible()
            expect(second_step_reg.error_empty_leg_region).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_leg_region).to_be_visible()
                error_message = second_step_reg.error_wrong_leg_region.text_content()
            else:
                expect(second_step_reg.error_empty_leg_region).to_be_visible()
                error_message = second_step_reg.error_empty_leg_region.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'


#Проверка поля "Город" в адресе проживания
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Город" в адресе проживания')
@pytest.mark.parametrize(
     "value, expected_error",
    [
        ("1234567890", None),
        ("Город", None),
        ("@$%&!", "Используйте только русские буквы и цифры"),
        ("City", "Используйте только русские буквы и цифры"),
        ("", "Необходимо заполнить «Город»."),
    ]
)
def test_leg_city_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.click_address_checkbox()
    second_step_reg.fill_leg_region_field()
    with allure.step(f"Ввод значения в поле Город: '{value}'"):
        second_step_reg.leg_city_input.fill(value)
        second_step_reg.leg_city_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_leg_city).not_to_be_visible()
            expect(second_step_reg.error_empty_leg_city).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_leg_city).to_be_visible()
                error_message = second_step_reg.error_wrong_leg_city.text_content()
            else:
                expect(second_step_reg.error_empty_leg_city).to_be_visible()
                error_message = second_step_reg.error_empty_leg_city.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'



#Проверка поля "Улица" в адресе проживания
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Улица" в адресе проживания')
@pytest.mark.parametrize(
    "value, expected_error",
    {
        ("1234567890", None),
        ("улица", None),
        ("!#$%@&?", "Используйте только русские буквы и цифры"),
        ("Ulitsa", "Используйте только русские буквы и цифры"),
        ("", 'Улица - обязательное поле (если отсутствует, укажите \"нет\").'),
    }
)
def test_leg_street_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.click_address_checkbox()
    second_step_reg.fill_leg_region_field()
    with allure.step(f"Ввод значения в поле Улица: '{value}'"):
        second_step_reg.leg_street_input.fill(value)
        second_step_reg.leg_street_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_leg_street).not_to_be_visible()
            expect(second_step_reg.error_empty_leg_street).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_leg_street).to_be_visible()
                error_message = second_step_reg.error_wrong_leg_street.text_content()
            else:
                expect(second_step_reg.error_empty_leg_street).to_be_visible()
                error_message = second_step_reg.error_empty_leg_street.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'



#Проверка поля "Дом" в адресе проживания
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка валидации поля "Дом" в адресе проживания')
@pytest.mark.parametrize(
    "value, expected_error",
    {
        ("1234567890", None),
        ("дом", None),
        ("", None),
        ("!#$%@&?", "Используйте только русские буквы и цифры"),
        ("dom", "Используйте только русские буквы и цифры"),
        ("99999999999", 'Значение «Дом» должно содержать максимум 10 символов.'),
    }
)
def test_leg_house_field(page:Page, value: str, expected_error: str, first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.click_address_checkbox()
    second_step_reg.fill_leg_region_field()

    with allure.step(f"Ввод значения в поле Дом: '{value}'"):
        second_step_reg.leg_house_num_input.fill(value)
        second_step_reg.leg_house_num_input.blur()
    with allure.step(f"Проверка: Отображается ошибка '{expected_error}'"):
        if expected_error is None:
            expect(second_step_reg.error_wrong_house).not_to_be_visible()
            expect(second_step_reg.error_maxlenght_house).not_to_be_visible()
        else:
            if "Используйте только русские буквы и цифры" in expected_error:
                expect(second_step_reg.error_wrong_house).to_be_visible()
                error_message = second_step_reg.error_wrong_house.text_content()
            else:
                expect(second_step_reg.error_maxlenght_house).to_be_visible()
                error_message = second_step_reg.error_maxlenght_house.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'


