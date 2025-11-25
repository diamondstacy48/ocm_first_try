import pytest

from pages.signin_page import SigninPage


@pytest.fixture
def signin_page(page):
    return SigninPage(page)

