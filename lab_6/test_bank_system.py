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

@pytest.mark.parametrize("amount, expected_balance", [
    (200.0, 1200.0),
    (500.0, 1500.0),
])
def test_deposit(account, amount, expected_balance):
    account.deposit(amount)
    assert account.balance == expected_balance


@pytest.mark.parametrize("amount, expected_balance", [
    (300.0, 700.0),
    (500.0, 500.0),
    (1000.0, 0.0),
])
def test_withdraw(account, amount, expected_balance):
    account.withdraw(amount)
    assert account.balance == expected_balance


@pytest.mark.parametrize("amount", [1100.0, 1500.0, 2000.0])
def test_withdraw_insufficient_funds(account, amount):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(amount)


@pytest.mark.asyncio
@pytest.mark.parametrize("transfer_amount, expected_balance_acc1, expected_balance_acc2", [
    (400.0, 600.0, 900.0),
    (100.0, 900.0, 600.0),
    (200.0, 800.0, 700.0),
])
async def test_transfer(account, account_two, transfer_amount, expected_balance_acc1, expected_balance_acc2):
    await account.transfer(account_two, transfer_amount)
    assert account.balance == expected_balance_acc1
    assert account_two.balance == expected_balance_acc2


@pytest.mark.asyncio
@pytest.mark.parametrize("transfer_amount", [1200.0, 1500.0, 2000.0])
async def test_transfer_insufficient_funds(account, account_two, transfer_amount):
    with pytest.raises(InsufficientFundsError):
        await account.transfer(account_two, transfer_amount)


# --- Tests for Bank ---

@pytest.mark.parametrize("account_number, owner, balance", [
    ("12345", "John Doe", 1000.0),
    ("67890", "Jane Doe", 500.0),
    ("54321", "Alice", 750.0),
])
def test_create_account(bank, account_number, owner, balance):
    bank.create_account(account_number, owner, balance)
    account = bank.get_account(account_number)
    assert account.owner == owner
    assert account.balance == balance


def test_get_account_not_found(bank):
    with pytest.raises(ValueError):
        bank.get_account("99999")


@pytest.mark.parametrize("account_number, owner, balance", [
    ("12345", "John Doe", 1000.0),
    ("67890", "Jane Doe", 500.0),
])
def test_get_account(bank, account_number, owner, balance):
    bank.create_account(account_number, owner, balance)
    account = bank.get_account(account_number)
    assert account.account_number == account_number
    assert account.owner == owner
    assert account.balance == balance


@pytest.mark.asyncio
@pytest.mark.parametrize("transfer_amount, expected_balance_acc1, expected_balance_acc2", [
    (200.0, 800.0, 700.0),
    (100.0, 900.0, 600.0),
])
async def test_process_transaction(bank, transfer_amount, expected_balance_acc1, expected_balance_acc2):
    bank.create_account("12345", "John Doe", 1000.0)
    bank.create_account("67890", "Jane Doe", 500.0)

    account = bank.get_account("12345")
    account_two = bank.get_account("67890")

    async def transaction():
        await account.transfer(account_two, transfer_amount)

    await bank.process_transaction(transaction)

    assert account.balance == expected_balance_acc1
    assert account_two.balance == expected_balance_acc2


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
