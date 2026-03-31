import pytest
import allure
from playwright.sync_api import Page, expect

# Для некоторых шагов allure steps написаны в page

# Проверка обязательных полей на 2 шаге регистрации
@allure.feature('Валидация полей на втором шаге регистрации')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка обязательных полей на вторм шаге регистрации')
def test_empty_fields_error(first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.click_address_checkbox()
    second_step_reg.click_next_step_button_second()
    second_step_reg.empty_fields_error()


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
            if "Значение «Серия и номер паспорта» неверно.»." in expected_error:
                expect(second_step_reg.error_wrong_pass_num).to_be_visible()
                error_message = second_step_reg.error_wrong_pass_num.text_content()
            else:
                expect(second_step_reg.error_empty_pass_num).to_be_visible()
                error_message = second_step_reg.error_empty_pass_num.text_content()
            assert expected_error in error_message, f'Ожидалось: "{expected_error}", отображается: "{error_message}"'



def test_reg_reg(first_step_reg, second_step_reg):
    first_step_reg.get_to_second_step()
    second_step_reg.fill_personal_data_second_step()



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