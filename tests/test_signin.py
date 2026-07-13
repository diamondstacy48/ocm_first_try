import pytest
import allure



@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиция с не валидными данными')
@pytest.mark.parametrize('username, password', [
    ('+79254827597', 'incorrect'),
    ('неверный@емайл', '123456')
])

def test_signin_failure(signin_page, username, password):
    with allure.step('Открыть страницу авторизации'):
        signin_page.open_signin_form()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        signin_page.login_with_creds(username, password)
    with allure.step('Отображается ошибка - Неверный логин или пароль'):
        assert signin_page.get_error_message_incorrect() == 'Неверный логин или пароль'

@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизация с валидными данными')

def test_signin_success(signin_page):
    with allure.step('Открыть страницу авторизации'):
        signin_page.open_signin_form()
    with allure.step('Ввести в форму авторизации валидные данные'):
        signin_page.login_with_creds ('+79254827597', '123456')
    with allure.step('Авторизация прошла успешно'):
        signin_page.page.wait_for_url('https://rc.dev.oneclickmoney.ru/account/')


@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиция без заполнения поля "email или телефон"')
def test_signin_with_empty_username(signin_page):
    with allure.step('Открыть страницу авторизации'):
        signin_page.open_signin_form()
    with allure.step('Заполнить поле "пароль"'):
        signin_page.login_without_username('123456')
    with (allure.step('Отображается ошибка - Необходимо заполнить «Email или телефон».')):
        assert signin_page.get_error_message_empty_username() == 'Необходимо заполнить «Email или телефон».'

@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиция без заполнения поля "пароль"')
def test_signin_with_empty_password(signin_page):
    with allure.step('Открыть страницу авторизации'):
        signin_page.open_signin_form()
    with allure.step('Заполнить поле "пароль"'):
        signin_page.login_without_password('+79645123485')
    with (allure.step('Отображается ошибка - Необходимо заполнить «Пароль».')):
        assert signin_page.get_error_message_empty_password() == 'Необходимо заполнить «Пароль».'
