import pytest

from pages.signin_page import SigninPage
from pages.first_step_reg import FirstStep
from pages.second_step_reg import SecondStep


@pytest.fixture()
def signin_page(page):
    return SigninPage(page)


@pytest.fixture()
def first_step_reg(page):
    return FirstStep(page)


@pytest.fixture()
def second_step_reg(page):
    return SecondStep(page)

