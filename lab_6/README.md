# Bank System

## Project Description
A banking system implementing basic banking operations such as:
- Account creation
- Deposits and withdrawals
- Transfers between accounts
- Account management through a Bank instance

The project also includes a set of tests to verify the system's functionality.

---

## Requirements
- Python 3.8+
- Libraries:
  - `pytest`
  - `pytest-asyncio`
  - `unittest.mock`

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/s24260-pj/s24260-tau-12.git
   cd lab_6
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## File Structure
- **bank_system.py**: Contains the implementation of the `Account` and `Bank` classes.
- **test_bank_system.py**: Contains tests for the `Account` and `Bank` classes.
- **README.md**: Project documentation.

---

## Running Tests
1. Install `pytest` and `pytest-asyncio`:
   ```bash
   pip install pytest pytest-asyncio
   ```
2. Run the tests:
   ```bash
   pytest test_bank_system.py
   ```

---

## Tests
### `Account` Class
- Tests for deposit and withdrawal functionality.
- Tests for exception handling (`InsufficientFundsError`).
- Tests for asynchronous transfers between accounts.

### `Bank` Class
- Tests for account creation.
- Tests for retrieving existing accounts.
- Tests for exceptions when accessing non-existent accounts.
- Tests for processing asynchronous transactions.

### Mocking
- Mocking external operations, e.g., delays (using `unittest.mock`).

---

## Screenshot
___

## Author
Artur Szulc (s24260)