
# Order Service System

This project demonstrates a simplified order service system consisting of the following services:

- **OrderService**: Handles order placement, including validation, inventory checks, and payment processing.
- **PaymentService**: Processes payments for orders.
- **InventoryService**: Manages inventory and checks product availability.
- **NotificationService**: Sends notifications to users about the status of their orders.

## Features

1. Place an order successfully when:
    - The product is available in inventory.
    - Payment is successfully processed.
    - A notification is sent to the user.

2. Handle errors gracefully:
    - When the product is not available.
    - When payment fails or throws an exception.

## Project Structure

### Services

- `OrderService`: Main service that orchestrates order placement.

- `PaymentService`: Interface for handling payment logic.

- `InventoryService`: Interface for inventory management.

- `NotificationService`: Interface for user notifications.


### Tests

Unit tests for `OrderService` include:

1. **Successful order placement**: Tests the happy path where all services work correctly.

2. **Unavailable product**: Ensures that orders fail if the product is not available.

3. **Payment failure**: Simulates payment processing failure.

4. **Payment exception handling**: Verifies exception handling during payment processing.


## How to Run

1. Clone the repository.

2. Import the project into your favorite Java IDE.

3. Run the tests using JUnit.


## Dependencies

- **JUnit 5**: For unit testing.

- **Mockito**: For mocking service dependencies.

## Screenshot
![image](https://github.com/user-attachments/assets/4e5744d1-405e-4aba-9b9a-07d4b7e12063)
