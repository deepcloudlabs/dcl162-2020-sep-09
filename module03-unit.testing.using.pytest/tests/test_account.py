import pytest

from banking.domain import Account, InsufficientBalance, CheckingAccount

""" 
How to list fixtures:
pytest --fixtures tests\test_account.py

How to run tests with code coverage:
pytest --cov=banking
================= test session starts ===================================
platform win32 -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: C:\DEVEL\stage\tmp\dcl162-2020.sep.9\module03-unit.testing.using.pytest
plugins: cov-2.10.1
collected 9 items                                                                                                                                                       

tests\test_account.py .........     [100%]

----------- coverage: platform win32, python 3.8.5-final-0 -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
banking\__init__.py       0      0   100%
banking\domain.py        26      0   100%
-----------------------------------------
TOTAL                    26      0   100%


========================== 9 passed in 0.22s =============================

"""


@pytest.fixture
def an_account():  # (1)
    """
    creates an Account object with iban "tr1", balance 1000
    """
    return Account("tr1", 1000)


@pytest.fixture
def a_checking_account():  # (1)
    """
    creates a CheckingAccount object with iban "tr1", balance 1000, and overdraft 500
    """
    return CheckingAccount("tr1", 1000, 500)


def test_create_account(an_account):
    """
    :param an_account: takes a fixture
    tests if an account is created successfully
    """
    assert an_account.iban == "tr1"
    assert an_account.balance == 1000


def test_deposit_with_positive_amount_then_success(an_account):
    an_account.deposit(1)  # (2) call exercise method
    # verification (3)
    assert an_account.balance == 1001


def test_deposit_with_negative_amount_then_raise_ValueError(an_account):
    with pytest.raises(ValueError):
        an_account.deposit(-1)
    assert an_account.balance == 1000


def test_deposit_with_no_amount_then_raise_ValueError(an_account):
    with pytest.raises(ValueError):
        an_account.deposit(0)
    assert an_account.balance == 1000


def test_withdraw_all_balance_then_success(an_account):
    an_account.withdraw(1000)  # (2) call exercise method
    # verification (3)
    assert an_account.balance == 0


def test_withdraw_zero_amount_then_raises_ValueError(an_account):
    with pytest.raises(ValueError):
        an_account.withdraw(0)  # (2) call exercise method
    # verification (3)
    assert an_account.balance == 1000


def test_withdraw_negative_amount_then_reaises_ValueError(an_account):
    with pytest.raises(ValueError):
        an_account.withdraw(-1)  # (2) call exercise method
    # verification (3)
    assert an_account.balance == 1000


def test_withdraw_over_balance_then_raises_InsufficientBalance(an_account):
    with pytest.raises(InsufficientBalance) as e:
        an_account.withdraw(1001)  # (2) call exercise method
    # verification (3)
    # assert e.deficit == 1
    assert an_account.balance == 1000


def test_withdraw(a_checking_account):
    pass
