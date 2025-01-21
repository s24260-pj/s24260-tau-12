import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from bank_system import Account, Bank, InsufficientFundsError


# --- Fixtures ---
@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def account():
    return Account(account_number="12345", owner="John Doe", balance=1000.0)


@pytest.fixture
def account_two():
    return Account(account_number="67890", owner="Jane Doe", balance=500.0)


# --- Tests for Account ---

def test_deposit(account):
    account.deposit(200.0)
    assert account.balance == 1200.0


def test_withdraw(account):
    account.withdraw(300.0)
    assert account.balance == 700.0


def test_withdraw_insufficient_funds(account):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(1100.0)


@pytest.mark.asyncio
async def test_transfer(account, account_two):
    await account.transfer(account_two, 400.0)
    assert account.balance == 600.0
    assert account_two.balance == 900.0


@pytest.mark.asyncio
async def test_transfer_insufficient_funds(account, account_two):
    with pytest.raises(InsufficientFundsError):
        await account.transfer(account_two, 1200.0)


# --- Tests for Bank ---

def test_create_account(bank):
    bank.create_account("12345", "John Doe", 1000.0)
    account = bank.get_account("12345")
    assert account.owner == "John Doe"
    assert account.balance == 1000.0


def test_get_account_not_found(bank):
    with pytest.raises(ValueError):
        bank.get_account("99999")


def test_get_account(bank):
    bank.create_account("12345", "John Doe", 1000.0)
    account = bank.get_account("12345")
    assert account.account_number == "12345"
    assert account.owner == "John Doe"
    assert account.balance == 1000.0


@pytest.mark.asyncio
async def test_process_transaction(bank):
    bank.create_account("12345", "John Doe", 1000.0)
    bank.create_account("67890", "Jane Doe", 500.0)

    account = bank.get_account("12345")
    account_two = bank.get_account("67890")

    async def transaction():
        await account.transfer(account_two, 200.0)

    await bank.process_transaction(transaction)

    assert account.balance == 800.0
    assert account_two.balance == 700.0


def test_mocking_external_authorization():
    with patch("asyncio.sleep", return_value=None) as mock_sleep:
        account = Account(account_number="12345", owner="John Doe", balance=1000.0)
        account_two = Account(account_number="67890", owner="Jane Doe", balance=500.0)
        asyncio.run(account.transfer(account_two, 300.0))
        assert account.balance == 700.0
        assert account_two.balance == 800.0
        mock_sleep.assert_called_once()


def test_create_account_with_existing_number(bank):
    bank.create_account("12345", "John Doe", 1000.0)

    with pytest.raises(ValueError):
        bank.create_account("12345", "Jane Doe", 500.0)


@pytest.mark.asyncio
async def test_concurrent_transfers(bank):
    bank.create_account("12345", "John Doe", 1000.0)
    bank.create_account("67890", "Jane Doe", 500.0)

    account = bank.get_account("12345")
    account_two = bank.get_account("67890")

    async def transfer1():
        await account.transfer(account_two, 300.0)

    async def transfer2():
        await account.transfer(account_two, 400.0)

    await asyncio.gather(transfer1(), transfer2())

    assert account.balance == 300.0  # 1000 - 300 - 400
    assert account_two.balance == 1200.0  # 500 + 300 + 400
